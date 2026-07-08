# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
"""Script to fix the specification and build code from it.

Usage: needs 2 args for execution. First one is either 'url' or 'path',
second one is the path to the Open API Spec. E.g.
./build_client_source.sh path /download/spec.json will take the spec
from the given path
"""

import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

import httpx
import yaml

error_code_pattern = re.compile("[4,5][0-9]{2}")
script_path = pathlib.Path(os.path.dirname(os.path.realpath(__file__)))
rest_api_path = script_path.parent / "polarion_rest_api_client"
template_path = script_path / "custom_templates"
config_path = script_path / "config.yaml"

with open(config_path, encoding="utf-8") as config_file:
    config = yaml.safe_load(config_file)
    output_path = rest_api_path / config.get("package_name_override", "")


def get_and_fix_spec(src: str, path: str | os.PathLike):
    """Fix errors in the specification."""
    if src == "path":
        with open(path) as f:
            spec = json.load(f)
    elif src == "url":
        response = httpx.get(path)
        spec = response.json()
    else:
        raise Exception(
            "you have to provide a file or url keyword as 1st arg."
        )
    spec_paths = spec["paths"]
    if (
        octet_schema := spec_paths.get(
            "/projects/{projectId}/testruns/{testRunId}/actions/importXUnitTestResults",
            {},
        )
        .get("post", {})
        .get("requestBody", {})
        .get("content", {})
        .get("application/octet-stream", {})
        .get("schema")
    ) and octet_schema.get("type") == "object":
        octet_schema["type"] = "string"
        octet_schema["format"] = "binary"

    for spec_path in spec_paths.values():
        for operation_description in spec_path.values():
            if (
                responses := operation_description.get("responses")
            ) and "4XX-5XX" in responses:
                for code, resp in responses.items():
                    if error_code_pattern.fullmatch(code):
                        resp["content"] = responses["4XX-5XX"]["content"]
                del responses["4XX-5XX"]
    schemas = spec["components"]["schemas"]

    if (
        (
            downloads := schemas.get("jobsSingleGetResponse", {})
            .get("properties", {})
            .get("data", {})
            .get("properties", {})
            .get("links", {})
            .get("properties", {})
            .get("downloads")
        )
        and "items" not in downloads
        and downloads.get("type") == "array"
    ):
        downloads["items"] = {"type": "string"}

    if (
        (
            downloads := schemas.get("jobsSinglePostResponse", {})
            .get("properties", {})
            .get("data", {})
            .get("properties", {})
            .get("links", {})
            .get("properties", {})
            .get("downloads")
        )
        and "items" not in downloads
        and downloads.get("type") == "array"
    ):
        downloads["items"] = {"type": "string"}

    if (
        error_source := schemas.get("errors", {})
        .get("properties", {})
        .get("errors", {})
        .get("items", {})
        .get("properties", {})
        .get("source")
    ):
        error_source["nullable"] = True
        if resource := error_source.get("properties", {}).get("resource"):
            resource["nullable"] = True
    return spec


def fix_nonjson_errors(api_path: pathlib.Path) -> None:
    """Wrap Errors.from_dict(response.json()) calls in try/except.

    The generated _parse_response functions call response.json() unconditionally
    for every error status code. When Polarion returns an HTML error page or an
    empty body, this raises json.decoder.JSONDecodeError instead of a proper
    PolarionApiException. Wrapping in try/except lets _raise_on_error emit a
    PolarionApiUnexpectedException instead.
    """
    pattern = re.compile(
        r"^( +)(response_\w+ = Errors\.from_dict\(response\.json\(\)\))",
        re.MULTILINE,
    )

    def _replace(m: re.Match) -> str:
        indent = m.group(1)
        stmt = m.group(2)
        var_name = stmt.split(" =")[0].strip()
        return (
            f"{indent}try:\n"
            f"{indent}    {stmt}\n"
            f"{indent}except Exception:\n"
            f"{indent}    {var_name} = None"
        )

    for path in api_path.rglob("*.py"):
        original = path.read_text(encoding="utf-8")
        fixed = pattern.sub(_replace, original)
        if fixed != original:
            path.write_text(fixed, encoding="utf-8")


def generate_client(spec):
    with tempfile.NamedTemporaryFile("w", delete=False) as f:
        json.dump(spec, f)
        f.close()

        generator_path = shutil.which("openapi-python-client")
        assert generator_path is not None, (
            "Did not find openapi-python-client generator - "
            "please install dev requirements"
        )

        subprocess.run(
            [
                generator_path,
                "generate",
                "--meta",
                "none",
                "--path",
                f.name,
                f"--custom-template-path={template_path}",
                "--config",
                config_path,
                "--overwrite",
            ],
            cwd=rest_api_path,
            check=True,
        )
    fix_nonjson_errors(output_path / "api")
    subprocess.run(["git", "add", output_path], check=True, cwd=rest_api_path)
    p = subprocess.run(
        ["pre-commit", "run", "-a"], cwd=rest_api_path, check=False
    )
    if p.returncode:
        subprocess.run(
            ["git", "add", "--update"], check=True, cwd=rest_api_path
        )
        subprocess.run(
            ["pre-commit", "run", "-a"], cwd=rest_api_path, check=False
        )


if __name__ == "__main__":
    spec = get_and_fix_spec(sys.argv[1], sys.argv[2])
    generate_client(spec)

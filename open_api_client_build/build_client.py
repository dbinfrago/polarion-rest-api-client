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
HTTP_4XX_MIN = 400
HTTP_4XX_MAX = 499
HTTP_5XX_MIN = 500
HTTP_5XX_MAX = 599
script_path = pathlib.Path(os.path.dirname(os.path.realpath(__file__)))
rest_api_path = script_path.parent / "polarion_rest_api_client"
template_path = script_path / "custom_templates"
config_path = script_path / "config.yaml"

with open(config_path, encoding="utf-8") as config_file:
    config = yaml.safe_load(config_file)
    output_path = rest_api_path / config.get("package_name_override", "")


def _load_spec(src: str, path: str | os.PathLike) -> dict:
    if src == "path":
        with open(path) as f:
            return json.load(f)
    if src == "url":
        return httpx.get(path).json()
    raise Exception("you have to provide a file or url keyword as 1st arg.")


def _fix_import_xunit_schema(spec_paths: dict) -> None:
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


def _normalize_wildcard_error_responses(spec_paths: dict) -> None:
    for spec_path in spec_paths.values():
        for operation_description in spec_path.values():
            if not isinstance(operation_description, dict):
                continue
            responses = operation_description.get("responses")
            if not responses:
                continue
            catchall_4xx_content = (
                responses["4XX"].get("content") if "4XX" in responses else None
            )
            catchall_5xx_content = (
                responses["5XX"].get("content") if "5XX" in responses else None
            )
            if not (catchall_4xx_content or catchall_5xx_content):
                continue
            for code, resp in responses.items():
                if not error_code_pattern.fullmatch(code) or resp.get(
                    "content"
                ):
                    continue
                code_int = int(code)
                if (
                    HTTP_4XX_MIN <= code_int <= HTTP_4XX_MAX
                    and catchall_4xx_content
                ):
                    resp["content"] = catchall_4xx_content
                elif (
                    HTTP_5XX_MIN <= code_int <= HTTP_5XX_MAX
                    and catchall_5xx_content
                ):
                    resp["content"] = catchall_5xx_content
            responses.pop("4XX", None)
            responses.pop("5XX", None)


def _ensure_download_items_schema(schemas: dict, schema_name: str) -> None:
    if (
        (
            downloads := schemas.get(schema_name, {})
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


def _fix_errors_schema(schemas: dict) -> None:
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


def get_and_fix_spec(src: str, path: str | os.PathLike):
    """Fix errors in the specification."""
    spec = _load_spec(src, path)
    spec_paths = spec["paths"]
    _fix_import_xunit_schema(spec_paths)
    _normalize_wildcard_error_responses(spec_paths)

    schemas = spec["components"]["schemas"]
    _ensure_download_items_schema(schemas, "jobsSingleGetResponse")
    _ensure_download_items_schema(schemas, "jobsSinglePostResponse")
    _fix_errors_schema(schemas)

    return spec


def _patch_generated_types_file() -> None:
    types_path = output_path / "types.py"
    if not types_path.exists():
        return

    content = types_path.read_text(encoding="utf-8")
    updated_content = content.replace(
        "from typing import IO, BinaryIO, Generic, Literal, TypeVar",
        "from typing import IO, BinaryIO, Literal, TypeVar",
    ).replace("class Response(Generic[T]):", "class Response[T]:")

    if updated_content != content:
        types_path.write_text(updated_content, encoding="utf-8")


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
    _patch_generated_types_file()
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

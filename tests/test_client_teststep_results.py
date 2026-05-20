# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import json

import pytest_httpx

import polarion_rest_api_client as polarion_api
from tests.conftest import (
    TEST_TS_RESULTS_CREATED_RESPONSE,
    TEST_TS_RESULTS_NEXT_RESPONSE,
    TEST_TS_RESULTS_NO_NEXT_RESPONSE,
    TEST_TS_RESULTS_PATCH_REQUEST,
    TEST_TS_RESULTS_POST_REQUEST,
)


def _make_project_client() -> polarion_api.ProjectClient:
    client = polarion_api.PolarionClient(
        polarion_api_endpoint="http://127.0.0.1/api",
        polarion_access_token="PAT123",
        batch_size=3,
    )
    return client.generate_project_client(project_id="PROJ", delete_status="deleted")


def test_get_test_step_results_multi_page(
    httpx_mock: pytest_httpx.HTTPXMock,
):
    client = _make_project_client()
    with open(TEST_TS_RESULTS_NEXT_RESPONSE, encoding="utf8") as f:
        first_page = json.load(f)
    with open(TEST_TS_RESULTS_NO_NEXT_RESPONSE, encoding="utf8") as f:
        second_page = json.load(f)

    httpx_mock.add_response(json=first_page)
    httpx_mock.add_response(json=second_page)

    template = polarion_api.TestStepResult(
        test_run_id="MyTestRunId",
        test_case_project_id="MyProjectId",
        test_case_id="MyTestcaseId",
        test_step_index=1,
        iteration=0,
    )

    results = client.work_items.teststeps_results.get_all(
        [template],
        fields={"teststep_results": "@all"},
        revision="12345",
    )

    reqs = httpx_mock.get_requests()
    assert len(reqs) == 2
    assert reqs[0].method == "GET"
    assert reqs[0].url.path.endswith(
        "/projects/MyProjectId/testruns/MyTestRunId/testrecords/MyProjectId/MyTestcaseId/0/teststepresults"
    )
    assert dict(reqs[0].url.params) == {
        "page[size]": "100",
        "page[number]": "1",
        "fields[teststep_results]": "@all",
        "revision": "12345",
    }
    assert dict(reqs[1].url.params) == {
        "page[size]": "100",
        "page[number]": "2",
        "fields[teststep_results]": "@all",
        "revision": "12345",
    }

    assert len(results) == 2
    assert results[0].result == "passed"
    assert results[0].comment.value == "My text value"
    assert results[1].result == "failed"
    assert results[1].comment.value == "My text value 2"


def test_create_test_step_results(
    httpx_mock: pytest_httpx.HTTPXMock,
):
    client = _make_project_client()
    with open(TEST_TS_RESULTS_CREATED_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(201, json=json.load(f))

    step_results = [
        polarion_api.TestStepResult(
            test_run_id="MyTestRunId",
            test_case_project_id="MyProjectId",
            test_case_id="MyTestcaseId",
            test_step_index=1,
            iteration=0,
            result="passed",
            comment=polarion_api.TextContent("text/html", "My text value"),
        ),
        polarion_api.TestStepResult(
            test_run_id="MyTestRunId",
            test_case_project_id="MyProjectId",
            test_case_id="MyTestcaseId",
            test_step_index=1,
            iteration=0,
            result="failed",
            comment=polarion_api.TextContent("text/html", "My text value 2"),
        ),
    ]

    response = client.work_items.teststeps_results.create(step_results)

    reqs = httpx_mock.get_requests()
    assert len(reqs) == 1
    req = reqs[0]
    assert req.method == "POST"
    assert req.url.path.endswith(
        "/projects/PROJ/testruns/MyTestRunId/testrecords/MyProjectId/MyTestcaseId/0/teststepresults"
    )

    req_data = json.loads(req.content.decode("utf-8"))
    with open(TEST_TS_RESULTS_POST_REQUEST, encoding="utf8") as f:
        expected_req = json.load(f)
    assert req_data == expected_req
    assert response is None


def test_update_test_step_result(
    httpx_mock: pytest_httpx.HTTPXMock,
):
    client = _make_project_client()
    httpx_mock.add_response(204)

    step_result = polarion_api.TestStepResult(
        test_run_id="MyTestRunId",
        test_case_project_id="MyProjectId",
        test_case_id="MyTestcaseId",
        test_step_index=1,
        iteration=4,
        result="passed",
        comment=polarion_api.TextContent("text/html", "Updated text"),
    )

    client.work_items.teststeps_results.update(step_result)

    reqs = httpx_mock.get_requests()
    assert len(reqs) == 1
    req = reqs[0]
    assert req.method == "PATCH"
    assert req.url.path.endswith(
        "/projects/PROJ/testruns/MyTestRunId/testrecords/MyProjectId/MyTestcaseId/4/teststepresults/1"
    )

    req_data = json.loads(req.content.decode("utf-8"))
    with open(TEST_TS_RESULTS_PATCH_REQUEST, encoding="utf8") as f:
        expected_req = json.load(f)
    assert req_data == expected_req

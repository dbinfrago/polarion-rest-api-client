# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import json

import pytest
import pytest_httpx

import polarion_rest_api_client as polarion_api
from tests.conftest import (
    TEST_TSRES_CREATED_RESPONSE,
    TEST_TSRES_GET_RESPONSE,
    TEST_TSRES_NEXT_RESPONSE,
    TEST_TSRES_NO_NEXT_RESPONSE,
    TEST_TSRES_PATCH_REQUEST,
    TEST_TSRES_POST_REQUEST,
)


def make_client() -> polarion_api.ProjectClient:
    client = polarion_api.PolarionClient(
        polarion_api_endpoint="http://127.0.0.1/api",
        polarion_access_token="PAT123",
        batch_size=3,
    )
    return client.generate_project_client(project_id="PROJ", delete_status="deleted")


@pytest.mark.parametrize(
    ("revision", "query"),
    [
        (
            None,
            {
                "page[size]": "100",
                "fields[teststep_results]": "@basic",
            },
        ),
        (
            "12345",
            {
                "page[size]": "100",
                "fields[teststep_results]": "@basic",
                "revision": "12345",
            },
        ),
    ],
    ids=["no_revision", "with_revision"],
)
def test_get_test_step_results_multi_page(
    httpx_mock: pytest_httpx.HTTPXMock,
    revision: str | None,
    query: dict,
):
    with open(TEST_TSRES_NEXT_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(json=json.load(f))
    with open(TEST_TSRES_NO_NEXT_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(json=json.load(f))

    client = make_client()
    test_step_results = client.work_items.teststeps_results.get_all(
        [polarion_api.TestStepResult("MyTestRunId", "MyProjectId", "MyTestCaseId", 0, 1)],
        fields={"teststep_results": "@basic"}, revision=revision
    )

    reqs = httpx_mock.get_requests()

    assert len(reqs) == 2
    assert reqs[0].method == "GET"
    query["page[number]"] = "1"
    assert dict(reqs[0].url.params) == query
    query["page[number]"] = "2"
    assert dict(reqs[1].url.params) == query
    assert len(test_step_results) == 2
    assert all(tsr.result == "passed" for tsr in test_step_results)
    assert all(tsr.comment.value == "Test passed" for tsr in test_step_results)


def test_create_test_step_results(
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_TSRES_CREATED_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(201, json=json.load(f))

    with open(TEST_TSRES_POST_REQUEST, encoding="utf8") as f:
        expected_req = json.load(f)

    test_run_id = "MyTestRunId"
    test_case_id = "MyTestCaseId"
    test_case_project_id = "MyProjectId"
    iteration = 1

    tsr_1 = polarion_api.TestStepResult(
        test_run_id, test_case_project_id, test_case_id, 0, iteration, result="passed", comment=polarion_api.TextContent("text/plain", "Test comment")
    )
    tsr_2 = polarion_api.TestStepResult(
        test_run_id, test_case_project_id, test_case_id, 1, iteration, result="failed", comment=polarion_api.TextContent("text/plain", "Test failed")
    )

    client = make_client()
    client.work_items.teststeps_results.create([tsr_1, tsr_2])

    reqs = httpx_mock.get_requests()
    assert len(reqs) == 1
    req_data = json.loads(reqs[0].content.decode("utf-8"))
    assert req_data == expected_req
    assert reqs[0].url.path.endswith(f"testruns/{test_run_id}/testrecords/{test_case_project_id}/{test_case_id}/{iteration}/teststepresults")


def test_update_test_step_result(
    httpx_mock: pytest_httpx.HTTPXMock,
):
    httpx_mock.add_response(204)
    with open(TEST_TSRES_PATCH_REQUEST, encoding="utf8") as f:
        expected_req = json.load(f)

    test_run_id = "MyTestRunId"
    test_case_id = "MyTestCaseId"
    test_case_project_id = "MyProjectId"
    iteration = 1
    test_step_index = 0

    tsr = polarion_api.TestStepResult(
        test_run_id, test_case_project_id, test_case_id, test_step_index, iteration, result="passed", comment=polarion_api.TextContent("text/plain", "Updated comment")
    )

    client = make_client()
    client.work_items.teststeps_results.update([tsr])

    reqs = httpx_mock.get_requests()
    assert len(reqs) == 1
    req_data = json.loads(reqs[0].content.decode("utf-8"))
    assert req_data == expected_req
    assert reqs[0].url.path.endswith(f"/testruns/{test_run_id}/testrecords/{test_case_project_id}/{test_case_id}/{iteration}/teststepresults/{test_step_index}")


def test_get_test_step_result(
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_TSRES_GET_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(json=json.load(f))

    test_run_id = "MyTestRunId"
    test_case_id = "MyTestCaseId"
    test_case_project_id = "MyProjectId"
    iteration = 1
    test_step_index = 0

    tsr = polarion_api.TestStepResult(
        test_run_id, test_case_project_id, test_case_id, test_step_index, iteration
    )

    client = make_client()
    result = client.work_items.teststeps_results.get(tsr)

    reqs = httpx_mock.get_requests()
    assert len(reqs) == 1
    assert reqs[0].method == "GET"
    assert reqs[0].url.path.endswith(f"testruns/{test_run_id}/testrecords/{test_case_project_id}/{test_case_id}/{iteration}/teststepresults/{test_step_index}")
    assert result.result == "passed"
    assert result.comment.value == "Test passed"
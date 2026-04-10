# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import datetime
import json

import pytest_httpx

import polarion_rest_api_client as polarion_api
from tests.conftest import (
    TEST_TRUN_CREATED_RESPONSE,
    TEST_TRUN_FULLY_PATCH_REQUEST,
    TEST_TRUN_NEXT_RESPONSE,
    TEST_TRUN_NO_NEXT_RESPONSE,
    TEST_TRUN_PATCH_REQUEST,
    TEST_TRUN_POST_REQUEST,
)


def test_get_test_runs_multi_page(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_TRUN_NEXT_RESPONSE, encoding="utf8") as f:
        content = json.load(f)
        httpx_mock.add_response(json=content)
        httpx_mock.add_response(json=content)

    with open(TEST_TRUN_NO_NEXT_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(json=json.load(f))

    test_runs = client.test_runs.get_all("123", fields={"testruns": "@all"})

    query = {
        "page[size]": "100",
        "page[number]": "1",
        "fields[testruns]": "@all",
        "query": "123",
    }
    reqs = httpx_mock.get_requests()
    assert len(reqs) == 3
    assert reqs[0].method == "GET"
    assert dict(reqs[0].url.params) == query
    query["page[number]"] = "2"
    assert dict(reqs[1].url.params) == query
    query["page[number]"] = "3"
    assert dict(reqs[2].url.params) == query
    assert len(test_runs) == 3
    assert test_runs[0].id == "MyTestRunId2"
    assert test_runs[0].type == "manual"
    assert (
        test_runs[0].select_test_cases_by
        == polarion_api.SelectTestCasesBy.MANUALSELECTION
    )
    assert test_runs[0].home_page_content
    assert test_runs[0].home_page_content.value == "My text value"
    assert test_runs[0].home_page_content.type == "text/html"
    assert test_runs[0].status == "open"
    assert test_runs[0].title == "Title"


def test_create_test_runs(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_TRUN_CREATED_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(201, json=json.load(f))

    tr_1 = polarion_api.TestRun(
        "ID",
        "manual",
        "open",
        "Title",
        polarion_api.TextContent("text/html", "My text value"),
        datetime.datetime.fromtimestamp(0, datetime.UTC),
        "Group ID",
        "ID Prefix",
        True,
        True,
        "Query",
        True,
        polarion_api.SelectTestCasesBy.MANUALSELECTION,
        {},
    )
    tr_2 = polarion_api.TestRun(
        "ID2",
        "manual",
        "open",
        "Title",
        polarion_api.TextContent("text/html", "My text value 2"),
        datetime.datetime.fromtimestamp(0, datetime.UTC),
        "Group ID",
        "ID Prefix",
        True,
        True,
        "Query",
        True,
        polarion_api.SelectTestCasesBy.MANUALSELECTION,
        {},
    )

    client.test_runs.create([tr_1, tr_2])

    reqs = httpx_mock.get_requests()
    assert len(reqs) == 1
    req_data = json.loads(reqs[0].content.decode("utf-8"))
    with open(TEST_TRUN_POST_REQUEST, encoding="utf8") as f:
        expected_req = json.load(f)

    assert req_data == expected_req
    assert tr_1.id == "MyTestRunId"
    assert tr_2.id == "MyTestRunId2"


def test_update_test_run(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    httpx_mock.add_response(204)
    test_run_id = "asdfg"
    tr = polarion_api.TestRun(
        test_run_id,
        "manual",
        "passed",
        "Title",
        finished_on=datetime.datetime.fromtimestamp(0, datetime.UTC),
        query="Query",
        use_report_from_template=False,
    )

    client.test_runs.update(tr)

    reqs = httpx_mock.get_requests()
    assert len(reqs) == 1
    req_data = json.loads(reqs[0].content.decode("utf-8"))
    with open(TEST_TRUN_PATCH_REQUEST, encoding="utf8") as f:
        expected_req = json.load(f)

    assert req_data == expected_req
    assert reqs[0].url.path.endswith(f"/testruns/{test_run_id}")


def test_update_test_run_fully(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    httpx_mock.add_response(204)
    tr = polarion_api.TestRun(
        "ID",
        "manual",
        "open",
        "Title",
        polarion_api.TextContent("text/html", "My text value"),
        datetime.datetime.fromtimestamp(0, datetime.UTC),
        "Group ID",
        "ID Prefix",
        True,
        True,
        "Query",
        True,
        polarion_api.SelectTestCasesBy.MANUALSELECTION,
        {},
    )

    client.test_runs.update(tr)

    reqs = httpx_mock.get_requests()
    assert len(reqs) == 1
    req_data = json.loads(reqs[0].content.decode("utf-8"))
    with open(TEST_TRUN_FULLY_PATCH_REQUEST, encoding="utf8") as f:
        expected_req = json.load(f)

    assert req_data == expected_req

# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import datetime
import json

import pytest_httpx

import polarion_rest_api_client as polarion_api
from tests.conftest import (
    TEST_TRUN_CREATED_RESPONSE,
    TEST_TRUN_FULLY_PATCH_REQUEST,
    TEST_TRUN_INCLUDED_USERS_RESPONSE,
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


def test_get_test_run_single_by_id(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_TRUN_INCLUDED_USERS_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(json=json.load(f))

    test_run = client.test_runs.get("MyTestRunId", include="author")

    req = httpx_mock.get_request()
    assert req is not None
    assert req.url.path.endswith("PROJ/testruns/MyTestRunId")
    assert req.url.params["include"] == "author"
    assert test_run is not None
    assert test_run.id == "MyTestRunId"
    assert test_run.title == "Title"


def test_get_test_run_resolves_author_name(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_TRUN_INCLUDED_USERS_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(json=json.load(f))

    test_run = client.test_runs.get("MyTestRunId", include="author")

    assert test_run is not None
    assert test_run.additional_attributes["author"] == "MyProjectId/jdoe"
    assert test_run.additional_attributes["author_name"] == "J Doe"
    # document relationship surfaced as full id, no name.
    assert (
        test_run.additional_attributes["document"]
        == "MyProjectId/MySpaceId/MyDocumentId"
    )


def test_get_test_run_surfaces_standard_scalar_attributes(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_TRUN_INCLUDED_USERS_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(json=json.load(f))

    test_run = client.test_runs.get("MyTestRunId")

    assert test_run is not None
    assert (
        test_run.additional_attributes["created"]
        == "1970-01-01T00:00:00+00:00"
    )
    assert (
        test_run.additional_attributes["updated"]
        == "1970-01-02T00:00:00+00:00"
    )
    assert "title" not in test_run.additional_attributes
    assert "type" not in test_run.additional_attributes
    assert "status" not in test_run.additional_attributes


def test_get_test_runs_multi_forwards_include(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_TRUN_INCLUDED_USERS_RESPONSE, encoding="utf8") as f:
        response = json.load(f)
    # get_multi expects a list under data plus paging links.
    response["data"] = [response["data"]]
    response["meta"] = {"totalCount": 1}
    httpx_mock.add_response(json=response)

    test_runs, next_page = client.test_runs.get_multi(include="author")

    req = httpx_mock.get_request()
    assert req is not None
    assert req.url.params["include"] == "author"
    assert next_page is False
    assert len(test_runs) == 1
    assert test_runs[0].additional_attributes["author_name"] == "J Doe"


def test_get_test_runs_multi_forwards_templates(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_TRUN_NO_NEXT_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(json=json.load(f))

    client.test_runs.get_multi(templates=True)

    req = httpx_mock.get_request()
    assert req is not None
    assert req.url.params["templates"] == "true"


def test_get_test_runs_multi_omits_templates_by_default(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_TRUN_NO_NEXT_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(json=json.load(f))

    client.test_runs.get_multi()

    req = httpx_mock.get_request()
    assert req is not None
    assert "templates" not in req.url.params

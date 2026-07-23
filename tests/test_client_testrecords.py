# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import datetime
import json

import pytest_httpx

import polarion_rest_api_client as polarion_api
from tests.conftest import (
    TEST_TREC_CREATED_RESPONSE,
    TEST_TREC_INCLUDED_USERS_RESPONSE,
    TEST_TREC_NEXT_RESPONSE,
    TEST_TREC_NO_NEXT_RESPONSE,
    TEST_TREC_PATCH_REQUEST,
    TEST_TREC_PATCH_REQUEST_EX_BY,
    TEST_TREC_POST_REQUEST,
    TEST_TREC_SINGLE_INCLUDED_USERS_RESPONSE,
    check_req,
)


def test_get_test_records_multi_page(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_TREC_NEXT_RESPONSE, encoding="utf8") as f:
        content = json.load(f)
        httpx_mock.add_response(json=content)
        httpx_mock.add_response(json=content)

    with open(TEST_TREC_NO_NEXT_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(json=json.load(f))

    test_records = client.test_runs.records.get_all(
        "123", fields={"testrecords": "@all"}
    )

    query = {
        "page[size]": "100",
        "page[number]": "1",
        "fields[testrecords]": "@all",
    }
    reqs = httpx_mock.get_requests()

    assert len(reqs) == 3
    assert reqs[0].method == "GET"
    assert dict(reqs[0].url.params) == query
    query["page[number]"] = "2"
    assert dict(reqs[1].url.params) == query
    query["page[number]"] = "3"
    assert dict(reqs[2].url.params) == query
    assert len(test_records) == 3
    assert test_records[0].result == "passed"
    assert test_records[0].iteration == 0
    assert test_records[0].duration == 0
    assert test_records[0].comment
    assert test_records[0].comment.value == "My text value"
    assert test_records[0].comment.type == "text/html"
    assert test_records[0].work_item_id == "MyTestcaseId2"
    assert test_records[0].work_item_revision == "1234"
    assert test_records[0].executed_by == "MyUserId"


def test_get_test_records_multi_forwards_include(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_TREC_NO_NEXT_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(json=json.load(f))

    client.test_runs.records.get_multi(
        "MyTestRunId",
        fields={"testrecords": "@all"},
        include="executedBy",
    )

    req = httpx_mock.get_request()
    assert req is not None
    assert dict(req.url.params)["include"] == "executedBy"


def test_get_test_records_multi_forwards_test_result_id(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_TREC_NO_NEXT_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(json=json.load(f))

    client.test_runs.records.get_multi(
        "MyTestRunId",
        test_result_id="failed",
    )

    req = httpx_mock.get_request()
    assert req is not None
    assert dict(req.url.params)["testResultId"] == "failed"


def test_get_test_records_parses_defect_relationship(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_TREC_NO_NEXT_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(json=json.load(f))

    test_records, _ = client.test_runs.records.get_multi(
        "MyTestRunId",
        fields={"testrecords": "@all"},
    )

    assert (
        test_records[0].additional_attributes["defect"]
        == "MyProjectId/MyWorkItemId"
    )


def test_get_test_records_resolves_executed_by_name(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_TREC_INCLUDED_USERS_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(json=json.load(f))

    test_records, _ = client.test_runs.records.get_multi(
        "MyTestRunId",
        fields={"testrecords": "@all", "users": "name"},
        include="executedBy",
    )

    assert len(test_records) == 1
    assert test_records[0].executed_by == "MyProjectId/jdoe"
    assert test_records[0].additional_attributes["executed_by_name"] == "J Doe"


def test_get_test_record_single_by_id(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_TREC_SINGLE_INCLUDED_USERS_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(json=json.load(f))

    test_record = client.test_runs.records.get(
        "MyTestRunId",
        "MyProjectId",
        "MyTestcaseId",
        0,
        fields={"testrecords": "@all", "users": "name"},
        include="executedBy",
    )

    req = httpx_mock.get_request()
    assert req is not None
    assert req.url.path.endswith(
        "/projects/PROJ/testruns/MyTestRunId/testrecords/MyProjectId/MyTestcaseId/0"
    )
    params = dict(req.url.params)
    assert params["fields[testrecords]"] == "@all"
    assert params["fields[users]"] == "name"
    assert params["include"] == "executedBy"
    assert test_record is not None
    assert test_record.work_item_project_id == "MyProjectId"
    assert test_record.work_item_id == "MyTestcaseId"
    assert test_record.iteration == 0
    assert test_record.executed_by == "MyProjectId/jdoe"
    assert test_record.additional_attributes["executed_by_name"] == "J Doe"
    assert test_record.additional_attributes["defect"] == "MyProjectId/DEF-1"


def test_create_test_records(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_TREC_CREATED_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(201, json=json.load(f))

    test_run_id = "asdfg"

    tr_1 = polarion_api.TestRecord(
        test_run_id,
        "MyProjectId",
        "MyWorkItemId",
        "0",
        executed=datetime.datetime.fromtimestamp(0, datetime.UTC),
        duration=0,
        result="passed",
        comment=polarion_api.TextContent("text/html", "My text value"),
    )
    tr_2 = polarion_api.TestRecord(
        test_run_id,
        "MyProjectId",
        "MyWorkItemId",
        "1234",
        executed=datetime.datetime.fromtimestamp(0, datetime.UTC),
        duration=1,
        result="failed",
        comment=polarion_api.TextContent("text/html", "My text value 2"),
        executed_by="1234",
    )

    client.test_runs.records.create([tr_1, tr_2])

    reqs = httpx_mock.get_requests()
    assert len(reqs) == 1

    check_req(
        f"/testruns/{test_run_id}/testrecords", reqs[0], TEST_TREC_POST_REQUEST
    )

    assert tr_1.iteration == 0
    assert tr_2.iteration == 1


def test_update_test_record(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    httpx_mock.add_response(204)

    test_run_id = "asdfg"
    work_item_id = "MyWorkItemId"
    work_item_project = "MyProjectId"

    tr_1 = polarion_api.TestRecord(
        test_run_id,
        work_item_project,
        work_item_id,
        iteration=4,
        duration=1337.5,
        result="passed",
        comment=polarion_api.TextContent("text/html", "My text value"),
    )

    client.test_runs.records.update(tr_1)

    reqs = httpx_mock.get_requests()
    assert len(reqs) == 1
    check_req(
        f"/testruns/{test_run_id}/testrecords/{work_item_project}/{work_item_id}/4",
        reqs[0],
        TEST_TREC_PATCH_REQUEST,
    )


def test_update_test_record_executed_by(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    httpx_mock.add_response(204)

    test_run_id = "asdfg"
    work_item_id = "MyWorkItemId"
    work_item_project = "MyProjectId"

    tr_1 = polarion_api.TestRecord(
        test_run_id,
        work_item_project,
        work_item_id,
        iteration=4,
        executed_by="1234",
    )

    client.test_runs.records.update(tr_1)

    reqs = httpx_mock.get_requests()
    assert len(reqs) == 1
    check_req(
        f"/testruns/{test_run_id}/testrecords/{work_item_project}/{work_item_id}/4",
        reqs[0],
        TEST_TREC_PATCH_REQUEST_EX_BY,
    )

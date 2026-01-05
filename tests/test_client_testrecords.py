# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import datetime
import json

import pytest_httpx

import polarion_rest_api_client as polarion_api
from tests.conftest import (
    TEST_TREC_CREATED_RESPONSE,
    TEST_TREC_NEXT_RESPONSE,
    TEST_TREC_NO_NEXT_RESPONSE,
    TEST_TREC_PATCH_REQUEST,
    TEST_TREC_PATCH_REQUEST_EX_BY,
    TEST_TREC_POST_REQUEST,
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
        executed=datetime.datetime.fromtimestamp(0, datetime.timezone.utc),
        duration=0,
        result="passed",
        comment=polarion_api.TextContent("text/html", "My text value"),
    )
    tr_2 = polarion_api.TestRecord(
        test_run_id,
        "MyProjectId",
        "MyWorkItemId",
        "1234",
        executed=datetime.datetime.fromtimestamp(0, datetime.timezone.utc),
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

# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import json

import pytest
import pytest_httpx

import polarion_rest_api_client as polarion_api
from tests.conftest import (
    TEST_STEPS_CREATED_RESPONSE,
    TEST_STEPS_NEXT_RESPONSE,
    TEST_STEPS_NO_NEXT_RESPONSE,
    TEST_STEPS_PATCH_REQUEST,
    TEST_STEPS_POST_REQUEST,
)


@pytest.mark.parametrize(
    ("revision", "query"),
    [
        (
            None,
            {
                "page[size]": "100",
                "fields[teststeps]": "@all",
            },
        ),
        (
            "12345",
            {
                "page[size]": "100",
                "fields[teststeps]": "@all",
                "revision": "12345",
            },
        ),
    ],
    ids=["no_revision", "with_revision"],
)
def test_get_test_steps_multi_page(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
    revision: str | None,
    query: dict,
):
    with open(TEST_STEPS_NEXT_RESPONSE, encoding="utf8") as f:
        content = json.load(f)
        httpx_mock.add_response(json=content)
        httpx_mock.add_response(json=content)

    with open(TEST_STEPS_NO_NEXT_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(json=json.load(f))

    test_steps: list[polarion_api.TestStep] = (
        client.work_items.test_steps.get_all(
            "123", fields={"teststeps": "@all"}, revision=revision
        )
    )

    reqs = httpx_mock.get_requests()

    assert len(reqs) == 3
    assert reqs[0].method == "GET"
    query["page[number]"] = "1"
    assert dict(reqs[0].url.params) == query
    query["page[number]"] = "2"
    assert dict(reqs[1].url.params) == query
    query["page[number]"] = "3"
    assert dict(reqs[2].url.params) == query
    assert len(test_steps) == 3
    assert all(ts.step_index == 1 for ts in test_steps)
    assert all(ts.revision == "1234" for ts in test_steps)
    assert all(ts.work_item_id == "MyWorkItemId" for ts in test_steps)
    assert all(
        ts.step_columns
        == {"string": polarion_api.TextContent("text/html", "My text value")}
        for ts in test_steps
    )


def test_create_test_steps(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_STEPS_CREATED_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(201, json=json.load(f))

    with open(TEST_STEPS_POST_REQUEST, encoding="utf8") as f:
        expected_req = json.load(f)

    work_item_id = "asdfg"

    ts_1 = polarion_api.TestStep(
        work_item_id,
        step_columns={"string": polarion_api.HtmlContent("My text value")},
    )
    ts_2 = polarion_api.TestStep(
        work_item_id,
        step_columns={"string": polarion_api.HtmlContent("My text value")},
    )

    client.work_items.test_steps.create([ts_1, ts_2])

    reqs = httpx_mock.get_requests()
    assert len(reqs) == 1
    req_data = json.loads(reqs[0].content.decode("utf-8"))
    assert req_data == expected_req
    assert reqs[0].url.path.endswith(f"/workitems/{work_item_id}/teststeps")
    assert ts_1.step_index == 0
    assert ts_2.step_index == 1


def test_update_test_step(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    httpx_mock.add_response(204)
    httpx_mock.add_response(204)
    with open(TEST_STEPS_PATCH_REQUEST, encoding="utf8") as f:
        expected_req = json.load(f)

    work_item_1_id = "asdfg"
    work_item_2_id = "qwertz"
    ts_1 = polarion_api.TestStep(
        work_item_1_id,
        1,
        step_columns={"string": polarion_api.HtmlContent("My text value")},
    )
    ts_2 = polarion_api.TestStep(
        work_item_1_id,
        2,
        step_columns={"string": polarion_api.HtmlContent("My text value")},
    )
    ts_3 = polarion_api.TestStep(
        work_item_2_id,
        1,
        step_columns={"string": polarion_api.HtmlContent("My text value")},
    )

    client.work_items.test_steps.update([ts_1, ts_2, ts_3])

    reqs = httpx_mock.get_requests()
    assert len(reqs) == 2
    req_data = json.loads(reqs[0].content.decode("utf-8"))
    assert req_data == expected_req
    assert reqs[0].url.path.endswith(f"/workitems/{work_item_1_id}/teststeps")
    assert reqs[1].url.path.endswith(f"/workitems/{work_item_2_id}/teststeps")

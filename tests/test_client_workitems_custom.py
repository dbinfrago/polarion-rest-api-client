# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import json

import pytest_httpx

import polarion_rest_api_client as polarion_api
from tests.conftest import (
    TEST_WI_CREATED_RESPONSE,
    TEST_WI_NO_NEXT_PAGE_RESPONSE,
    TEST_WI_POST_REQUEST,
    CustomWorkItem,
)


def test_get_all_work_items_single_page_custom_work_item(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_WI_NO_NEXT_PAGE_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(json=json.load(f))

    work_items = client.work_items.get_all("", work_item_cls=CustomWorkItem)

    assert isinstance(work_items[0], CustomWorkItem)
    assert work_items[0].capella_uuid == "asdfgh"


def test_create_work_item_custom_work_item(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_WI_CREATED_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(201, json=json.load(f))
    work_item = CustomWorkItem(
        title="Title",
        description=polarion_api.HtmlContent("My text value"),
        status="open",
        type="task",
        capella_uuid="asdfgh",
        hyperlinks=[
            polarion_api.HyperLink(
                role="ref_ext",
                uri="https://polarion.plm.automation.siemens.com",
            ),
            polarion_api.HyperLink(
                title="Title",
                role="ref_ext",
                uri="https://polarion.plm.automation.siemens.com",
            ),
        ],
    )

    work_item.capella_uuid = "asdfg"
    work_item.cfOwner = "MyUserId"

    client.work_items.create(work_item)

    req = httpx_mock.get_request()
    assert req.method == "POST"
    with open(TEST_WI_POST_REQUEST, encoding="utf8") as f:
        expected = json.load(f)

    assert json.loads(req.content.decode()) == expected

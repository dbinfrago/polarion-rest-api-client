# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import json

import pytest_httpx

import polarion_rest_api_client as polarion_api
from polarion_rest_api_client import data_models
from tests.conftest import (
    TEST_DOCUMENT_PATCH_REQUEST,
    TEST_DOCUMENT_PATCH_REQUEST2,
    TEST_DOCUMENT_POST_REQUEST,
    TEST_DOCUMENT_RESPONSE,
)


def test_get_document_with_all_fields(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_DOCUMENT_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(json=json.load(f))

    document = client.documents.get(
        "MySpaceId", "MyDocumentName", {"fields[documents]": "@all"}
    )

    reqs = httpx_mock.get_requests()
    assert reqs[0].method == "GET"
    assert isinstance(document, data_models.Document)
    assert len(reqs) == 1
    assert document == data_models.Document(
        id="MyProjectId/MySpaceId/MyDocumentName",
        module_folder="MySpaceId",
        module_name="MyDocumentName",
        type="standardSpecification",
        status="open",
        home_page_content=data_models.TextContent(
            type="text/html", value="<h1>My text value</h1>"
        ),
        title="MyDocumentName",
        rendering_layouts=[
            data_models.RenderingLayout(
                type="task",
                label="My label",
                layouter=data_models.Layouter("paragraph"),
                properties=data_models.RenderingProperties(
                    fields_at_start=["id"],
                    fields_at_end=["custom", "bla"],
                    sidebar_work_item_fields=["id"],
                    fields_at_end_as_table=True,
                ),
            ),
        ],
        outline_numbering=True,
        outline_numbering_prefix="PREFIX",
        additional_properties={
            "html_property": data_models.TextContent(
                type="text/html", value="<p>super Value</p>"
            ),
            "integer_property": 42,
        },
        structure_link_role="parent",
    )


def test_create_new_document(
    client: polarion_api.ProjectClient, httpx_mock: pytest_httpx.HTTPXMock
):
    document = polarion_api.Document(
        module_folder="folder",
        module_name="name",
        home_page_content=polarion_api.TextContent(
            type="text/html", value="<p>super Value</p>"
        ),
        title="Fancy Title",
        outline_numbering=False,
        outline_numbering_prefix="TEST",
        rendering_layouts=[
            data_models.RenderingLayout(
                type="task",
                label="My label",
                layouter=data_models.Layouter("paragraph"),
                properties=data_models.RenderingProperties(
                    fields_at_start=["id"],
                    fields_at_end=["custom"],
                    sidebar_work_item_fields=["id"],
                    fields_at_end_as_table=True,
                ),
            ),
            data_models.RenderingLayout(
                type="task2",
                label="My label",
                layouter=data_models.Layouter("paragraph"),
                properties=data_models.RenderingProperties(
                    fields_at_start=["id"],
                ),
            ),
        ],
        structure_link_role="parent",
        additional_properties={
            "html_property": polarion_api.TextContent(
                type="text/html", value="<p>super Value</p>"
            ),
            "integer_property": 42,
        },
    )

    httpx_mock.add_response(
        201,
        json={
            "data": [
                {
                    "type": "documents",
                    "id": "PROJ/folder/name",
                    "links": {
                        "self": "server-host-name/application-path/projects/PROJ/spaces/folder/documents/name?revision=1234"  # pylint: disable=line-too-long
                    },
                }
            ]
        },
    )
    client.documents.create(document)

    with open(TEST_DOCUMENT_POST_REQUEST, encoding="utf-8") as f:
        expected_request = json.load(f)

    assert len(httpx_mock.get_requests()) == 1
    req = httpx_mock.get_request()
    assert req.method == "POST"
    assert (
        req.url == "http://127.0.0.1/api/projects/PROJ/spaces/folder/documents"
    )
    assert json.loads(req.content.decode("utf-8")) == expected_request


def test_update_document(
    client: polarion_api.ProjectClient, httpx_mock: pytest_httpx.HTTPXMock
):
    document = polarion_api.Document(
        module_folder="folder",
        module_name="name1",
        home_page_content=polarion_api.TextContent(
            type="text/html", value="<p>super Value</p>"
        ),
        title="Fancy Title",
    )

    document2 = polarion_api.Document(
        module_folder="folder",
        module_name="name",
        home_page_content=polarion_api.TextContent(
            type="text/html", value="<p>super Value</p>"
        ),
        title="Fancy Title",
        rendering_layouts=[
            data_models.RenderingLayout(
                type="task",
                label="My label",
                layouter=data_models.Layouter("paragraph"),
                properties=data_models.RenderingProperties(
                    fields_at_start=["id"],
                    fields_at_end=["custom"],
                    sidebar_work_item_fields=["id"],
                    hidden=True,
                ),
            ),
            data_models.RenderingLayout(
                type="task2",
                label="My label",
                layouter=data_models.Layouter("paragraph"),
                properties=data_models.RenderingProperties(
                    fields_at_start=["id"],
                ),
            ),
        ],
        additional_properties={
            "html_property": {
                "type": "text/html",
                "value": "<p>super Value</p>",
            },
            "integer_property": 42,
        },
    )

    httpx_mock.add_response(204)
    httpx_mock.add_response(204)
    client.documents.update([document, document2])

    with open(TEST_DOCUMENT_PATCH_REQUEST, encoding="utf-8") as f:
        expected_request = json.load(f)
    with open(TEST_DOCUMENT_PATCH_REQUEST2, encoding="utf-8") as f:
        expected_request_2 = json.load(f)
    reqs = httpx_mock.get_requests()

    assert len(reqs) == 2
    assert reqs[0].method == "PATCH"
    assert (
        reqs[0].url
        == "http://127.0.0.1/api/projects/PROJ/spaces/folder/documents/name1"
    )
    assert json.loads(reqs[0].content.decode("utf-8")) == expected_request
    assert reqs[1].method == "PATCH"
    assert (
        reqs[1].url
        == "http://127.0.0.1/api/projects/PROJ/spaces/folder/documents/name"
    )
    assert json.loads(reqs[1].content.decode("utf-8")) == expected_request_2

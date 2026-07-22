# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import json

import pytest_httpx

import polarion_rest_api_client as polarion_api
from tests.conftest import (
    TEST_DOC_COMMENTS_INCLUDED_USERS_RESPONSE,
    TEST_WI_COMMENTS_INCLUDED_USERS_RESPONSE,
)


def test_get_work_item_comments_resolves_names_and_thread(
    client: polarion_api.ProjectClient, httpx_mock: pytest_httpx.HTTPXMock
):
    with open(TEST_WI_COMMENTS_INCLUDED_USERS_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(json=json.load(f))

    comments, next_page = client.work_items.comments.get_multi(
        "MyWorkItemId", include="author,childComments"
    )

    req = httpx_mock.get_request()
    assert req.url.path.endswith("PROJ/workitems/MyWorkItemId/comments")
    assert req.url.params["include"] == "author,childComments"
    assert next_page is False
    assert len(comments) == 2

    parent = comments[0]
    assert parent.id == "parent"
    assert parent.title == "Root comment"
    assert parent.resolved is False
    assert parent.text is not None
    assert parent.text.type == "text/html"
    assert parent.author == "MyProjectId/jdoe"
    assert parent.additional_attributes["author_name"] == "J Doe"
    assert parent.child_comments == ["MyProjectId/MyWorkItemId/child"]

    child = comments[1]
    assert child.parent_comment == "MyProjectId/MyWorkItemId/parent"
    assert child.additional_attributes["author_name"] == "A Smith"


def test_create_work_item_comment_populates_id(
    client: polarion_api.ProjectClient, httpx_mock: pytest_httpx.HTTPXMock
):
    httpx_mock.add_response(
        201,
        json={
            "data": [
                {
                    "type": "workitem_comments",
                    "id": "PROJ/MyWorkItemId/newComment",
                }
            ]
        },
    )
    comment = polarion_api.Comment(
        text=polarion_api.TextContent(type="text/plain", value="Hello"),
        title="Hi",
    )
    client.work_items.comments.create("MyWorkItemId", comment)

    req = httpx_mock.get_request()
    assert req.method == "POST"
    assert req.url.path.endswith("PROJ/workitems/MyWorkItemId/comments")
    body = json.loads(req.content.decode("utf-8"))
    assert body["data"][0]["attributes"]["text"] == {
        "type": "text/plain",
        "value": "Hello",
    }
    assert body["data"][0]["attributes"]["title"] == "Hi"
    assert comment.id == "newComment"


def test_create_work_item_comment_reply_sends_parent(
    client: polarion_api.ProjectClient, httpx_mock: pytest_httpx.HTTPXMock
):
    httpx_mock.add_response(
        201,
        json={
            "data": [
                {"type": "workitem_comments", "id": "PROJ/MyWorkItemId/reply"}
            ]
        },
    )
    comment = polarion_api.Comment(
        text=polarion_api.TextContent(type="text/plain", value="Re"),
        parent_comment="PROJ/MyWorkItemId/parent",
    )
    client.work_items.comments.create("MyWorkItemId", comment)

    body = json.loads(httpx_mock.get_request().content.decode("utf-8"))
    assert body["data"][0]["relationships"]["parentComment"]["data"] == {
        "type": "workitem_comments",
        "id": "PROJ/MyWorkItemId/parent",
    }


def test_set_resolved_work_item_comment(
    client: polarion_api.ProjectClient, httpx_mock: pytest_httpx.HTTPXMock
):
    httpx_mock.add_response(204)
    client.work_items.comments.set_resolved(
        "MyWorkItemId", "c1", resolved=True
    )

    req = httpx_mock.get_request()
    assert req.method == "PATCH"
    assert req.url.path.endswith("PROJ/workitems/MyWorkItemId/comments/c1")
    body = json.loads(req.content.decode("utf-8"))
    assert body["data"]["attributes"] == {"resolved": True}
    assert body["data"]["id"] == "PROJ/MyWorkItemId/c1"


def test_get_document_comments_resolves_name(
    client: polarion_api.ProjectClient, httpx_mock: pytest_httpx.HTTPXMock
):
    with open(TEST_DOC_COMMENTS_INCLUDED_USERS_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(json=json.load(f))

    comments, next_page = client.documents.comments.get_multi(
        "MySpaceId", "MyDocumentId", include="author"
    )

    req = httpx_mock.get_request()
    assert req.url.path.endswith(
        "PROJ/spaces/MySpaceId/documents/MyDocumentId/comments"
    )
    assert next_page is False
    assert len(comments) == 1
    assert comments[0].id == "c1"
    assert comments[0].author == "MyProjectId/jdoe"
    assert comments[0].additional_attributes["author_name"] == "J Doe"


def test_create_document_comment_populates_id(
    client: polarion_api.ProjectClient, httpx_mock: pytest_httpx.HTTPXMock
):
    httpx_mock.add_response(
        201,
        json={
            "data": [
                {
                    "type": "document_comments",
                    "id": "PROJ/MySpaceId/MyDocumentId/newC",
                }
            ]
        },
    )
    comment = polarion_api.Comment(
        text=polarion_api.TextContent(type="text/html", value="<p>Hi</p>")
    )
    client.documents.comments.create("MySpaceId", "MyDocumentId", comment)

    req = httpx_mock.get_request()
    assert req.method == "POST"
    assert req.url.path.endswith(
        "PROJ/spaces/MySpaceId/documents/MyDocumentId/comments"
    )
    assert comment.id == "newC"


def test_set_resolved_document_comment(
    client: polarion_api.ProjectClient, httpx_mock: pytest_httpx.HTTPXMock
):
    httpx_mock.add_response(204)
    client.documents.comments.set_resolved(
        "MySpaceId", "MyDocumentId", "c1", resolved=False
    )

    req = httpx_mock.get_request()
    assert req.method == "PATCH"
    assert req.url.path.endswith(
        "PROJ/spaces/MySpaceId/documents/MyDocumentId/comments/c1"
    )
    body = json.loads(req.content.decode("utf-8"))
    assert body["data"]["attributes"] == {"resolved": False}

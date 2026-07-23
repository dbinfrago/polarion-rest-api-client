# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import asyncio
import functools
import inspect
import json
import pathlib
import typing as t
from functools import wraps

import httpx
import pytest

import polarion_rest_api_client as polarion_api
from polarion_rest_api_client.clients import base_classes


@pytest.fixture(autouse=True)
def no_sleeps(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(
        base_classes.time, "sleep", lambda _delay: None, raising=True
    )

    async def _no_asyncio_sleep(*_: t.Any, **kwargs: t.Any) -> t.Any:
        return kwargs.get("result")

    monkeypatch.setattr(
        base_classes.asyncio, "sleep", _no_asyncio_sleep, raising=True
    )


def wrap_client(obj, is_async: bool):
    """Recursively wrap the client to select async methods if needed."""

    class ClientWrapper:
        def __getattr__(self, name):
            if is_async and hasattr(obj, f"async_{name}"):
                attr = getattr(obj, f"async_{name}")
            else:
                attr = getattr(obj, name)

            if inspect.iscoroutinefunction(attr) or (
                isinstance(attr, functools.partial)
                and inspect.iscoroutinefunction(attr.args[0])
            ):
                # Run coroutines sync and also catch those wrapped with retry_on_error
                @wraps(attr)
                def sync_wrapper(*args, **kwargs):
                    return asyncio.run(attr(*args, **kwargs))

                return sync_wrapper

            if callable(attr):
                return attr  # normal sync method

            # Wrap subclients, too
            return wrap_client(attr, is_async)

        def __setattr__(self, name: str, value: t.Any):
            setattr(obj, name, value)

    return ClientWrapper()


def pytest_generate_tests(metafunc):
    if "client" in metafunc.fixturenames:
        metafunc.parametrize("is_async", [False, True], ids=["sync", "async"])


@pytest.fixture
def client(is_async: bool):
    client = polarion_api.PolarionClient(
        polarion_api_endpoint="http://127.0.0.1/api",
        polarion_access_token="PAT123",
        batch_size=3,
    )
    client_base = client.generate_project_client(
        project_id="PROJ", delete_status="deleted"
    )
    return wrap_client(client_base, is_async)


@pytest.fixture(name="work_item")
def fixture_dummy_work_item():
    return polarion_api.WorkItem(
        title="Title",
        description=polarion_api.HtmlContent("My text value"),
        type="task",
        status="open",
        additional_attributes={"capella_uuid": "asdfg"},
    )


@pytest.fixture(name="work_item_patch")
def fixture_dummy_work_item_patch():
    return polarion_api.WorkItem(
        id="MyWorkItemId",
        title="Title",
        description=polarion_api.HtmlContent("My text value"),
        status="open",
        additional_attributes={
            "capella_uuid": "qwertz",
            "cfOwner": "NewOwner",
        },
    )


@pytest.fixture(name="work_item_attachment")
def fixture_dummy_work_item_attachment():
    with open(TEST_WIA_CREATED_RESPONSE, encoding="utf8") as f:
        attachment_content = f.read()

    return polarion_api.WorkItemAttachment(
        "MyWorkItemId",
        "Attachment",
        "Title",
        attachment_content.encode("utf-8"),
        "text/plain",
        "test.json",
    )


TEST_DATA_ROOT = pathlib.Path(__file__).parent / "data"
TEST_RESPONSES = TEST_DATA_ROOT / "mock_api_responses"
TEST_REQUESTS = TEST_DATA_ROOT / "expected_requests"
TEST_WIA_NEXT_PAGE_RESPONSE = (
    TEST_RESPONSES / "get_work_item_attachments_next_page.json"
)
TEST_WIA_NO_NEXT_PAGE_RESPONSE = (
    TEST_RESPONSES / "get_work_item_attachments_no_next_page.json"
)
TEST_WIA_CREATED_RESPONSE = (
    TEST_RESPONSES / "created_work_item_attachment.json"
)
TEST_WIA_MULTI_CREATED_RESPONSE = (
    TEST_RESPONSES / "created_work_item_attachments.json"
)
TEST_WIL_MULTI_POST_REQUEST = TEST_REQUESTS / "post_work_item_links.json"
TEST_WIL_DELETE2_REQUEST = TEST_REQUESTS / "delete_work_item_link_2.json"
TEST_WIL_DELETE_REQUEST = TEST_REQUESTS / "delete_work_item_links.json"
TEST_WIL_DELETED_REQUEST = TEST_REQUESTS / "delete_work_item_link.json"
TEST_WIL_POSTED_REQUEST = TEST_REQUESTS / "post_work_item_link.json"
TEST_WIL_CREATED_RESPONSE = TEST_RESPONSES / "created_work_item_links.json"
TEST_WIL_NEXT_PAGE_RESPONSE = (
    TEST_RESPONSES / "get_linked_work_items_next_page.json"
)
TEST_WIL_NO_NEXT_PAGE_RESPONSE = (
    TEST_RESPONSES / "get_linked_work_items_no_next_page.json"
)
TEST_WIL_BACKLINKS_RESPONSE = TEST_RESPONSES / "get_backlinked_work_items.json"
TEST_WI_DELETE_REQUEST = TEST_REQUESTS / "delete_work_item.json"
TEST_WI_PATCH_STATUS_DELETED_REQUEST = (
    TEST_REQUESTS / "patch_work_item_status_deleted.json"
)
TEST_WI_PATCH_STATUS_REQUEST = TEST_REQUESTS / "patch_work_item_status.json"
TEST_WI_PATCH_TITLE_REQUEST = TEST_REQUESTS / "patch_work_item_title.json"
TEST_WI_PATCH_DESCRIPTION_REQUEST = (
    TEST_REQUESTS / "patch_work_item_description.json"
)
TEST_WI_PATCH_COMPLETELY_REQUEST = (
    TEST_REQUESTS / "patch_work_item_completely.json"
)
TEST_WI_PATCH_HYPERLINKS_REQUEST = (
    TEST_REQUESTS / "patch_work_item_hyperlinks.json"
)
TEST_WI_MULTI_POST_REQUEST = TEST_REQUESTS / "post_workitems.json"
TEST_WI_MULTI_POST_REQUEST_IN_DOC = TEST_REQUESTS / "post_workitem_in_doc.json"
TEST_WI_POST_REQUEST = TEST_REQUESTS / "post_workitem.json"
TEST_WI_NO_NEXT_PAGE_RESPONSE = TEST_RESPONSES / "workitems_no_next_page.json"
TEST_WI_CREATED_RESPONSE = TEST_RESPONSES / "created_work_items.json"
TEST_WI_ERROR_NEXT_PAGE_RESPONSE = (
    TEST_RESPONSES / "workitems_next_page_error.json"
)
TEST_WI_NEXT_PAGE_RESPONSE = TEST_RESPONSES / "workitems_next_page.json"
TEST_WI_SINGLE_RESPONSE = TEST_RESPONSES / "get_work_item.json"
TEST_WI_INCLUDED_USERS_RESPONSE = (
    TEST_RESPONSES / "get_work_item_included_users.json"
)
TEST_WI_NOT_TRUNCATED_RESPONSE = (
    TEST_RESPONSES / "get_work_item_not_truncated.json"
)
TEST_DOCUMENT_RESPONSE = TEST_RESPONSES / "get_document.json"
TEST_DOCUMENTS_INCLUDED_USERS_RESPONSE = (
    TEST_RESPONSES / "get_documents_included_users.json"
)
TEST_DOCUMENT_POST_REQUEST = TEST_REQUESTS / "create_document.json"
TEST_DOCUMENT_PATCH_REQUEST = TEST_REQUESTS / "update_document.json"
TEST_DOCUMENT_PATCH_REQUEST2 = TEST_REQUESTS / "update_document_2.json"
TEST_ERROR_RESPONSE = TEST_RESPONSES / "error.json"
TEST_FAULTS_ERROR_RESPONSES = TEST_RESPONSES / "faulty_errors.json"
TEST_PROJECT_RESPONSE_JSON = TEST_RESPONSES / "project.json"
TEST_PROJECTS_RESPONSE_JSON = TEST_RESPONSES / "get_projects.json"
TEST_TRUN_PATCH_REQUEST = TEST_REQUESTS / "patch_test_run_partially.json"
TEST_TRUN_FULLY_PATCH_REQUEST = TEST_REQUESTS / "patch_test_run_fully.json"
TEST_TRUN_POST_REQUEST = TEST_REQUESTS / "post_test_run.json"
TEST_TREC_PATCH_REQUEST = TEST_REQUESTS / "patch_test_record.json"
TEST_TREC_PATCH_REQUEST_EX_BY = (
    TEST_REQUESTS / "patch_test_record_executed_by.json"
)
TEST_TREC_POST_REQUEST = TEST_REQUESTS / "post_test_records.json"
TEST_TREC_CREATED_RESPONSE = TEST_RESPONSES / "created_test_records.json"
TEST_TRUN_CREATED_RESPONSE = TEST_RESPONSES / "created_test_runs.json"
TEST_TREC_NEXT_RESPONSE = TEST_RESPONSES / "test_records_next_page.json"
TEST_TREC_NO_NEXT_RESPONSE = TEST_RESPONSES / "test_records_no_next_page.json"
TEST_TRUN_NEXT_RESPONSE = TEST_RESPONSES / "test_runs_next_page.json"
TEST_TRUN_NO_NEXT_RESPONSE = TEST_RESPONSES / "test_runs_no_next_page.json"
TEST_TRUN_INCLUDED_USERS_RESPONSE = (
    TEST_RESPONSES / "get_test_run_included_users.json"
)
TEST_TREC_INCLUDED_USERS_RESPONSE = (
    TEST_RESPONSES / "get_test_record_included_users.json"
)
TEST_TREC_SINGLE_INCLUDED_USERS_RESPONSE = (
    TEST_RESPONSES / "get_test_record_single_included_users.json"
)
TEST_WI_COMMENTS_INCLUDED_USERS_RESPONSE = (
    TEST_RESPONSES / "get_work_item_comments_included_users.json"
)
TEST_DOC_COMMENTS_INCLUDED_USERS_RESPONSE = (
    TEST_RESPONSES / "get_document_comments_included_users.json"
)

TEST_STEPS_CREATED_RESPONSE = TEST_RESPONSES / "created_test_steps.json"
TEST_STEPS_NEXT_RESPONSE = TEST_RESPONSES / "test_steps_next_page.json"
TEST_STEPS_NO_NEXT_RESPONSE = TEST_RESPONSES / "test_steps_no_next_page.json"
TEST_STEPS_PATCH_REQUEST = TEST_REQUESTS / "patch_test_steps.json"
TEST_STEPS_POST_REQUEST = TEST_REQUESTS / "post_test_steps.json"

TEST_TRUN_PARAM_NEXT_RES = TEST_RESPONSES / "get_test_run_parameter.json"
TEST_TRUN_PARAM_NO_NEXT_RES = (
    TEST_RESPONSES / "get_test_run_parameter_no_next.json"
)
TEST_TRUN_PARAM_CREATED_RES = (
    TEST_RESPONSES / "created_test_parameters_trun.json"
)
TEST_TRUN_PARAM_CREATED_REQ_1 = TEST_REQUESTS / "create_parameters_trun_1.json"
TEST_TRUN_PARAM_CREATED_REQ_2 = TEST_REQUESTS / "create_parameters_trun_2.json"
TEST_TRUN_PARAM_DELETE_REQ_1 = TEST_REQUESTS / "delete_parameters_trun_1.json"
TEST_TRUN_PARAM_DELETE_REQ_2 = TEST_REQUESTS / "delete_parameters_trun_2.json"


class CustomWorkItem(polarion_api.WorkItem):
    capella_uuid: str | None


def check_req(
    expected_path: str, req: httpx.Request, expected_body: pathlib.Path
):
    req_data = json.loads(req.content.decode("utf-8"))
    with open(expected_body, encoding="utf8") as f:
        expected_req = json.load(f)
    assert req_data == expected_req
    assert req.url.path.endswith(expected_path)

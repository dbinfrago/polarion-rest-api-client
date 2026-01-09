# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import json
import pathlib

import httpx
import pytest

import polarion_rest_api_client as polarion_api
from polarion_rest_api_client.clients import base_classes


@pytest.fixture(name="client")
def fixture_client():
    base_classes._max_sleep = 0
    base_classes._min_sleep = 0
    client = polarion_api.PolarionClient(
        polarion_api_endpoint="http://127.0.0.1/api",
        polarion_access_token="PAT123",
        batch_size=3,
    )
    return client.generate_project_client(
        project_id="PROJ", delete_status="deleted"
    )


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
TEST_WI_NOT_TRUNCATED_RESPONSE = (
    TEST_RESPONSES / "get_work_item_not_truncated.json"
)
TEST_DOCUMENT_RESPONSE = TEST_RESPONSES / "get_document.json"
TEST_DOCUMENT_POST_REQUEST = TEST_REQUESTS / "create_document.json"
TEST_DOCUMENT_PATCH_REQUEST = TEST_REQUESTS / "update_document.json"
TEST_DOCUMENT_PATCH_REQUEST2 = TEST_REQUESTS / "update_document_2.json"
TEST_ERROR_RESPONSE = TEST_RESPONSES / "error.json"
TEST_FAULTS_ERROR_RESPONSES = TEST_RESPONSES / "faulty_errors.json"
TEST_PROJECT_RESPONSE_JSON = TEST_RESPONSES / "project.json"
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

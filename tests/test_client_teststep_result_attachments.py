# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import json

import pytest_httpx

import polarion_rest_api_client as polarion_api
from tests.conftest import (
    TEST_TS_RESULT_ATTACHMENTS_CREATED_RESPONSE,
    TEST_TS_RESULT_ATTACHMENTS_NEXT_RESPONSE,
    TEST_TS_RESULT_ATTACHMENTS_NO_NEXT_RESPONSE,
)


def _make_project_client() -> polarion_api.ProjectClient:
    client = polarion_api.PolarionClient(
        polarion_api_endpoint="http://127.0.0.1/api",
        polarion_access_token="PAT123",
        batch_size=3,
    )
    return client.generate_project_client(project_id="PROJ", delete_status="deleted")


def test_get_test_step_result_attachments_multi_page(
    httpx_mock: pytest_httpx.HTTPXMock,
):
    client = _make_project_client()
    with open(TEST_TS_RESULT_ATTACHMENTS_NEXT_RESPONSE, encoding="utf8") as f:
        first_page = json.load(f)
    with open(TEST_TS_RESULT_ATTACHMENTS_NO_NEXT_RESPONSE, encoding="utf8") as f:
        second_page = json.load(f)

    httpx_mock.add_response(json=first_page)
    httpx_mock.add_response(json=second_page)

    template = polarion_api.TestStepResultAttachment(
        test_run_id="MyTestRunId",
        test_case_project_id="MyProjectId",
        test_case_id="MyTestcaseId",
        test_step_index=1,
        iteration=0,
        id="",
    )

    attachments = client.work_items.teststepsResults_attachment.get_all(
        template.test_case_project_id,
        template.test_run_id,
        template.test_case_project_id,
        template.test_case_id,
        template.iteration,
        template.test_step_index,
        fields={"teststepresult_attachments": "@all"},
        revision="12345",
    )

    reqs = httpx_mock.get_requests()
    assert len(reqs) == 2
    assert reqs[0].method == "GET"
    assert reqs[0].url.path.endswith(
        "/projects/MyProjectId/testruns/MyTestRunId/testrecords/MyProjectId/MyTestcaseId/0/teststepresults/1/attachments"
    )
    assert dict(reqs[0].url.params) == {
        "page[size]": "100",
        "page[number]": "1",
        "fields[teststepresult_attachments]": "@all",
        "revision": "12345",
    }
    assert dict(reqs[1].url.params) == {
        "page[size]": "100",
        "page[number]": "2",
        "fields[teststepresult_attachments]": "@all",
        "revision": "12345",
    }

    assert len(attachments) == 2
    assert attachments[0].id == "MyAttachmentId1"
    assert attachments[0].file_name == "test1.txt"
    assert attachments[1].id == "MyAttachmentId2"
    assert attachments[1].title == "Title 2"


def test_create_test_step_result_attachments(
    httpx_mock: pytest_httpx.HTTPXMock,
):
    client = _make_project_client()
    with open(TEST_TS_RESULT_ATTACHMENTS_CREATED_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(201, json=json.load(f))

    attachment = polarion_api.TestStepResultAttachment(
        test_run_id="MyTestRunId",
        test_case_project_id="MyProjectId",
        test_case_id="MyTestcaseId",
        test_step_index=1,
        iteration=0,
        id="",
        file_name="test.txt",
        content_bytes=b"hello world",
        mime_type="text/plain",
        title="Title",
    )

    client.work_items.teststepsResults_attachment.create([attachment])

    reqs = httpx_mock.get_requests()
    assert len(reqs) == 1
    req = reqs[0]
    assert req.method == "POST"
    assert req.url.path.endswith(
        "/projects/PROJ/testruns/MyTestRunId/testrecords/MyProjectId/MyTestcaseId/0/teststepresults/1/attachments"
    )
    assert req.headers["content-type"].startswith("multipart/form-data")

    content = req.content.decode("utf-8", errors="ignore")
    assert "Content-Disposition: form-data; name=\"resource\"" in content
    assert "test.txt" in content
    assert "Title" in content
    assert attachment.id == "MyAttachmentId1"


def test_update_test_step_result_attachment(
    httpx_mock: pytest_httpx.HTTPXMock,
):
    client = _make_project_client()
    httpx_mock.add_response(204)

    attachment = polarion_api.TestStepResultAttachment(
        test_run_id="MyTestRunId",
        test_case_project_id="MyProjectId",
        test_case_id="MyTestcaseId",
        test_step_index=1,
        iteration=0,
        id="MyAttachmentId",
        title="Updated Title",
    )

    client.work_items.teststepsResults_attachment.update([attachment])

    reqs = httpx_mock.get_requests()
    assert len(reqs) == 1
    req = reqs[0]
    assert req.method == "PATCH"
    assert req.url.path.endswith(
        "/projects/PROJ/testruns/MyTestRunId/testrecords/PROJ/MyTestcaseId/0/teststepresults/1/attachments/MyAttachmentId"
    )

    content = req.content.decode("utf-8", errors="ignore")
    assert "Updated Title" in content

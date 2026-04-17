# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import copy
import email
import json

import httpx
import pytest
import pytest_httpx

import polarion_rest_api_client as polarion_api
from tests.conftest import (
    TEST_TSRES_ATT_CREATED_RESPONSE,
    TEST_TSRES_ATT_NO_NEXT_RESPONSE,
)


def make_client() -> polarion_api.ProjectClient:
    client = polarion_api.PolarionClient(
        polarion_api_endpoint="http://127.0.0.1/api",
        polarion_access_token="PAT123",
        batch_size=3,
    )
    return client.generate_project_client(project_id="PROJ", delete_status="deleted")


def _extract_data_from_request(
    req: httpx.Request,
) -> dict[str, list]:
    headers = f"Content-Type: {req.headers['Content-Type']}\r\n\r\n"
    msg = email.message_from_bytes(
        headers.encode(req.headers.encoding) + req.content
    )
    fields = {}
    for part in msg.walk():
        field_name = part.get_param("name", header="Content-Disposition")
        if isinstance(field_name, str):
            fields.setdefault(field_name, []).append(part)
    return fields


@pytest.mark.parametrize(
    ("revision", "query"),
    [
        (
            None,
            {
                "fields[teststepresult_attachments]": "@basic",
                "page[size]": "100",
                "page[number]": "1",
            },
        ),
        (
            "12345",
            {
                "fields[teststepresult_attachments]": "@basic",
                "page[size]": "100",
                "page[number]": "1",
                "revision": "12345",
            },
        ),
    ],
    ids=["no_revision", "with_revision"],
)
def test_get_test_step_result_attachments_single_page(
    httpx_mock: pytest_httpx.HTTPXMock,
    revision: str | None,
    query: dict,
):
    with open(
        TEST_TSRES_ATT_NO_NEXT_RESPONSE,
        encoding="utf8",
    ) as f:
        httpx_mock.add_response(json=json.load(f))

    client = make_client()
    test_step_result_attachments = client.work_items.teststepsResults_attachment.get_all(
        [polarion_api.TestStepResultAttachment(
            "MyTestRunId",
            "MyProjectId",
            "MyTestCaseId",
            0,
            1,
            "MyAttachmentId",
        )],
        fields={"teststepresult_attachments": "@basic"},
        revision=revision,
    )

    reqs = httpx_mock.get_requests()
    assert reqs[0].method == "GET"
    assert dict(reqs[0].url.params) == query
    assert len(test_step_result_attachments) == 1
    assert len(reqs) == 1
    assert test_step_result_attachments[0] == polarion_api.TestStepResultAttachment(
        "MyTestRunId", "MyProjectId", "MyTestCaseId", 0, 1, "MyAttachmentId", "Attachment Title", file_name="file.txt"
    )


def test_create_test_step_result_attachments(
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_TSRES_ATT_CREATED_RESPONSE, encoding="utf8") as f:
        httpx_mock.add_response(201, json=json.load(f))

    test_run_id = "MyTestRunId"
    test_case_id = "MyTestCaseId"
    test_case_project_id = "MyProjectId"
    test_step_index = 0
    iteration = 1

    attachment = polarion_api.TestStepResultAttachment(
        test_run_id, test_case_project_id, test_case_id, test_step_index, iteration,
        title="Test Attachment", file_name="test.txt", content_bytes=b"content", mime_type="text/plain"
    )

    client = make_client()
    client.work_items.teststepsResults_attachment.create([attachment])

    reqs = httpx_mock.get_requests()
    assert len(reqs) == 1
    fields = _extract_data_from_request(reqs[0])
    assert "resource" in fields
    assert "files" in fields
    assert reqs[0].url.path.endswith(f"testruns/{test_run_id}/testrecords/{test_case_project_id}/{test_case_id}/{iteration}/teststepresults/{test_step_index}/attachments")
    assert attachment.id == "MyAttachmentId1"


def test_update_test_step_result_attachment(
    httpx_mock: pytest_httpx.HTTPXMock,
):
    httpx_mock.add_response(204)

    test_run_id = "MyTestRunId"
    test_case_id = "MyTestCaseId"
    test_case_project_id = "MyProjectId"
    test_step_index = 0
    iteration = 1

    attachment = polarion_api.TestStepResultAttachment(
        test_run_id, test_case_project_id, test_case_id, test_step_index, iteration, "MyAttachmentId", title="Updated Title"
    )

    client = make_client()
    client.work_items.teststepsResults_attachment.update(attachment)

    req = httpx_mock.get_request()
    assert req is not None
    assert req.method == "PATCH"
    assert req.url.path.endswith(f"testruns/{test_run_id}/testrecords/PROJ/{test_case_id}/{iteration}/teststepresults/{test_step_index}/attachments/MyAttachmentId")
# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import io
import typing as t

from polarion_rest_api_client import data_models as dm
from polarion_rest_api_client.open_api_client import models as api_models
from polarion_rest_api_client.open_api_client import types as oa_types
from polarion_rest_api_client.open_api_client.api.test_step_result_attachments import (
    delete_test_step_result_attachment,
    get_test_step_result_attachments,
    patch_test_step_result_attachment,
    post_test_step_result_attachments,
)

from . import base_classes as bc


class TestStepResultAttachments(
    bc.SingleGetClient[dm.TestStepResultAttachment],
    bc.UpdateClient[dm.TestStepResultAttachment],
    bc.CreateClient[dm.TestStepResultAttachment],
    bc.MultiGetClient[dm.TestStepResultAttachment],
    bc.DeleteClient[dm.TestStepResultAttachment],
):
    """A class to handle TestStepResultAttachments."""

    def _create(self, items: list[dm.TestStepResultAttachment]) -> None:
        """Create the given work item attachment in Polarion."""
        attachment_attributes = []
        attachment_files = []
        assert len(items), "No attachments were provided."
        assert all(
            [wia.test_case_id == items[0].test_case_id] for wia in items
        ), "All attachments must belong to the same teststep result."
        for testStepResult_item_attachment in items:
            assert testStepResult_item_attachment.file_name, (
                "You have to define a FileName."
            )
            assert testStepResult_item_attachment.content_bytes, (
                "You have to provide content bytes."
            )
            assert testStepResult_item_attachment.mime_type, (
                "You have to provide a mime_type."
            )

            attributes = api_models.TeststepresultAttachmentsListPostRequestDataItemAttributes(  # pylint: disable=line-too-long
                file_name=testStepResult_item_attachment.file_name
            )
            if testStepResult_item_attachment.title:
                attributes.title = testStepResult_item_attachment.title

            attachment_attributes.append(
                api_models.TeststepresultAttachmentsListPostRequestDataItem(
                    type_=api_models.TeststepresultAttachmentsListPostRequestDataItemType.TESTSTEPRESULT_ATTACHMENTS,  # pylint: disable=line-too-long
                    attributes=attributes,
                )
            )

            attachment_files.append(
                oa_types.File(
                    io.BytesIO(testStepResult_item_attachment.content_bytes),
                    testStepResult_item_attachment.file_name,
                    testStepResult_item_attachment.mime_type,
                )
            )
        multipart = api_models.PostTestStepResultAttachmentsRequestBody(
            resource=api_models.TeststepresultAttachmentsListPostRequest(
                attachment_attributes
            ),
            files=attachment_files,
        )
        response = post_test_step_result_attachments.sync_detailed(
            project_id=self._project_id,
            test_run_id=items[0].test_run_id,
            test_case_project_id=items[0].test_case_project_id,
            test_case_id=items[0].test_case_id,
            test_step_index=items[0].test_step_index,
            iteration=items[0].iteration,
            client=self._client.client,
            body=multipart,
        )

        self._raise_on_error(response)
        assert isinstance(
            response.parsed,
            api_models.TeststepresultAttachmentsListPostResponse,
        )
        assert response.parsed.data

        for counter, work_item_attachment_res in enumerate(
            response.parsed.data
        ):
            assert work_item_attachment_res.id
            items[counter].id = work_item_attachment_res.id.split("/")[-1]

    async def _async_create(
        self, items: list[dm.TestStepResultAttachment]
    ) -> None:
        """Async create the given work item attachment in Polarion."""
        attachment_attributes = []
        attachment_files = []
        assert len(items), "No attachments were provided."
        assert all(
            [wia.test_case_id == items[0].test_case_id] for wia in items
        ), "All attachments must belong to the same teststep result."
        for testStepResult_item_attachment in items:
            assert testStepResult_item_attachment.file_name, (
                "You have to define a FileName."
            )
            assert testStepResult_item_attachment.content_bytes, (
                "You have to provide content bytes."
            )
            assert testStepResult_item_attachment.mime_type, (
                "You have to provide a mime_type."
            )

            attributes = api_models.TeststepresultAttachmentsListPostRequestDataItemAttributes(  # pylint: disable=line-too-long
                file_name=testStepResult_item_attachment.file_name
            )
            if testStepResult_item_attachment.title:
                attributes.title = testStepResult_item_attachment.title

            attachment_attributes.append(
                api_models.TeststepresultAttachmentsListPostRequestDataItem(
                    type_=api_models.TeststepresultAttachmentsListPostRequestDataItemType.TESTSTEPRESULT_ATTACHMENTS,  # pylint: disable=line-too-long
                    attributes=attributes,
                )
            )

            attachment_files.append(
                oa_types.File(
                    io.BytesIO(testStepResult_item_attachment.content_bytes),
                    testStepResult_item_attachment.file_name,
                    testStepResult_item_attachment.mime_type,
                )
            )
        multipart = api_models.PostTestStepResultAttachmentsRequestBody(
            resource=api_models.TeststepresultAttachmentsListPostRequest(
                attachment_attributes
            ),
            files=attachment_files,
        )
        response = await post_test_step_result_attachments.asyncio_detailed(
            project_id=self._project_id,
            test_run_id=items[0].test_run_id,
            test_case_project_id=items[0].test_case_project_id,
            test_case_id=items[0].test_case_id,
            test_step_index=items[0].test_step_index,
            iteration=items[0].iteration,
            client=self._client.client,
            body=multipart,
        )

        self._raise_on_error(response)
        assert isinstance(
            response.parsed,
            api_models.TeststepresultAttachmentsListPostResponse,
        )
        assert response.parsed.data

        for counter, work_item_attachment_res in enumerate(
            response.parsed.data
        ):
            assert work_item_attachment_res.id
            items[counter].id = work_item_attachment_res.id.split("/")[-1]

    def get_multi(  # type: ignore[override]
        self,
        project_id: str,
        test_run_id: str,
        test_case_project_id: str,
        test_case_id: str,
        iteration: str,
        test_step_index: str,
        page_size: int = 100,
        page_number: int = 1,
        fields: dict[str, str] | None = None,
        revision: str | None = None,
    ) -> tuple[list[dm.TestStepResultAttachment], bool]:
        """Return test step result attachments."""
        if fields is None:
            fields = self._client.default_fields.teststepresult_attachments
        sparse_fields = self._build_sparse_fields(fields)
        response = get_test_step_result_attachments.sync_detailed(
            project_id=project_id,
            test_run_id=test_run_id,
            test_case_project_id=test_case_project_id,
            test_case_id=test_case_id,
            iteration=iteration,
            test_step_index=test_step_index,
            client=self._client.client,
            pagesize=page_size,
            pagenumber=page_number,
            fields=sparse_fields,
            revision=revision or oa_types.UNSET,
        )

        self._raise_on_error(response)

        parsed_response = response.parsed

        teststepResult_attachments: list[dm.TestStepResultAttachment] = []

        next_page = False

        if (
            isinstance(
                parsed_response,
                api_models.TeststepresultAttachmentsListGetResponse,
            )
            and parsed_response.data
        ):
            for attachment in parsed_response.data:
                assert attachment.attributes
                assert isinstance(attachment.attributes.id, str)

                teststepResult_attachments.append(
                    dm.TestStepResultAttachment(
                        test_run_id,
                        test_case_project_id,
                        test_case_id,
                        test_step_index,
                        iteration,
                        attachment.attributes.id,
                        self.unset_to_none(attachment.attributes.title),
                        file_name=self.unset_to_none(
                            attachment.attributes.file_name
                        ),
                    )
                )

            next_page = isinstance(
                parsed_response.links,
                api_models.TeststepresultAttachmentsListGetResponseLinks,
            ) and bool(parsed_response.links.next_)

        return teststepResult_attachments, next_page

    async def async_get_multi(  # type: ignore[override]
        self,
        project_id: str,
        test_run_id: str,
        test_case_project_id: str,
        test_case_id: str,
        iteration: str,
        test_step_index: str,
        page_size: int = 100,
        page_number: int = 1,
        fields: dict[str, str] | None = None,
        revision: str | None = None,
    ) -> tuple[list[dm.TestStepResultAttachment], bool]:
        """Async Get test step result attachments."""
        if fields is None:
            fields = self._client.default_fields.teststepresult_attachments
        sparse_fields = self._build_sparse_fields(fields)
        response = await get_test_step_result_attachments.asyncio_detailed(
            project_id=project_id,
            test_run_id=test_run_id,
            test_case_project_id=test_case_project_id,
            test_case_id=test_case_id,
            iteration=iteration,
            test_step_index=test_step_index,
            client=self._client.client,
            pagesize=page_size,
            pagenumber=page_number,
            fields=sparse_fields,
            revision=revision or oa_types.UNSET,
        )

        self._raise_on_error(response)

        parsed_response = response.parsed

        teststep_result_attachments: list[dm.TestStepResultAttachment] = []

        next_page = False

        if (
            isinstance(
                parsed_response,
                api_models.TeststepresultAttachmentsListGetResponse,
            )
            and parsed_response.data
        ):
            for attachment in parsed_response.data:
                assert attachment.attributes
                assert isinstance(attachment.attributes.id, str)

                teststepResult_attachments.append(
                    dm.TestStepResultAttachment(
                        test_run_id,
                        test_case_project_id,
                        test_case_id,
                        test_step_index,
                        iteration,
                        attachment.attributes.id,
                        self.unset_to_none(attachment.attributes.title),
                        file_name=self.unset_to_none(
                            attachment.attributes.file_name
                        ),
                    )
                )

            next_page = isinstance(
                parsed_response.links,
                api_models.TeststepresultAttachmentsListGetResponseLinks,
            ) and bool(parsed_response.links.next_)

        return teststepResult_attachments, next_page

    def _update(self, to_update: list[dm.TestStepResultAttachment]) -> None:
        """Update the given test step result attachment in Polarion."""
        assert len(to_update) == 1, "Expected only one item"
        item = to_update[0]
        attributes = api_models.TeststepresultAttachmentsSinglePatchRequestDataAttributes()
        if to_update[0].title:
            attributes.title = to_update[0].title

        multipart = api_models.PatchTestStepResultAttachmentsRequestBody(
            resource=api_models.TeststepresultAttachmentsSinglePatchRequest(
                data=api_models.TeststepresultAttachmentsSinglePatchRequestData(
                    type_=api_models.TeststepresultAttachmentsSinglePatchRequestDataType.TESTSTEPRESULT_ATTACHMENTS,  # pylint: disable=line-too-long
                    id=f"{item.test_case_project_id}/{item.test_run_id}/{item.test_case_project_id}/{item.test_case_id}/{item.iteration}/{item.test_step_index}/{item.id}",
                    attributes=attributes,
                )
            )
        )

        if item.content_bytes:
            multipart.content = oa_types.File(
                io.BytesIO(item.content_bytes),
                item.file_name,
                item.mime_type,
            )

        response = patch_test_step_result_attachment.sync_detailed(
            project_id=self._project_id,
            test_run_id=item.test_run_id,
            test_case_project_id=self._project_id,
            test_case_id=item.test_case_id,
            iteration=item.iteration,
            test_step_index=item.test_step_index,
            attachment_id=item.id,
            client=self._client.client,
            body=multipart,
        )
        self._raise_on_error(response)

    async def _async_update(
        self, to_update: list[dm.TestStepResultAttachment]
    ) -> None:
        """Async update the given test step result attachment in Polarion."""
        assert len(to_update) == 1, "Expected only one item"
        item = to_update[0]
        attributes = api_models.TeststepresultAttachmentsSinglePatchRequestDataAttributes()
        if to_update[0].title:
            attributes.title = to_update[0].title

        multipart = api_models.PatchTestStepResultAttachmentsRequestBody(
            resource=api_models.TeststepresultAttachmentsSinglePatchRequest(
                data=api_models.TeststepresultAttachmentsSinglePatchRequestData(
                    type_=api_models.TeststepresultAttachmentsSinglePatchRequestDataType.TESTSTEPRESULT_ATTACHMENTS,  # pylint: disable=line-too-long
                    id=f"{item.test_case_project_id}/{item.test_run_id}/{item.test_case_project_id}/{item.test_case_id}/{item.iteration}/{item.test_step_index}/{item.id}",
                    attributes=attributes,
                )
            )
        )

        if item.content_bytes:
            multipart.content = oa_types.File(
                io.BytesIO(item.content_bytes),
                item.file_name,
                item.mime_type,
            )

        response = await patch_test_step_result_attachment.asyncio_detailed(
            project_id=self._project_id,
            test_run_id=item.test_run_id,
            test_case_project_id=self._project_id,
            test_case_id=item.test_case_id,
            iteration=item.iteration,
            test_step_index=item.test_step_index,
            attachment_id=item.id,
            client=self._client.client,
            body=multipart,
        )
        self._raise_on_error(response)

    def _delete(self, items: list[dm.TestStepResultAttachment]) -> None:
        for item in items:
            self._retry_on_error(self._single_delete, item)

    def _single_delete(self, item: dm.TestStepResultAttachment) -> None:
        """Delete the given teststep result attachment."""
        response = delete_test_step_result_attachment.sync_detailed(
            project_id=self._project_id,
            test_run_id=item.test_run_id,
            test_case_project_id=item.test_case_project_id,
            test_case_id=item.test_case_id,
            iteration=item.iteration,
            test_step_index=item.test_step_index,
            attachment_id=item.id,
            client=self._client.client,
        )
        self._raise_on_error(response)

    async def _async_delete(
        self, items: list[dm.TestStepResultAttachment]
    ) -> None:
        for item in items:
            await self._async_retry_on_error(self._async_single_delete, item)

    async def _async_single_delete(
        self, item: dm.TestStepResultAttachment
    ) -> None:
        """Async delete the given teststep result attachment."""
        response = await delete_test_step_result_attachment.asyncio_detailed(
            project_id=self._project_id,
            test_run_id=item.test_run_id,
            test_case_project_id=item.test_case_project_id,
            test_case_id=item.test_case_id,
            iteration=item.iteration,
            test_step_index=item.test_step_index,
            attachment_id=item.id,
            client=self._client.client,
        )
        self._raise_on_error(response)

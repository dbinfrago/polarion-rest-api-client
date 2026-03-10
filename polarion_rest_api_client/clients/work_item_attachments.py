# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
"""Implementations of WorkItemAttachment relates functions."""

import io

from polarion_rest_api_client import data_models as dm
from polarion_rest_api_client.open_api_client import models as api_models
from polarion_rest_api_client.open_api_client import types as oa_types
from polarion_rest_api_client.open_api_client.api.work_item_attachments import (  # pylint: disable=line-too-long
    delete_work_item_attachment,
    get_work_item_attachments,
    patch_work_item_attachment,
    post_work_item_attachments,
)

from . import base_classes as bc


class WorkItemAttachments(
    bc.UpdateClient[dm.WorkItemAttachment],
    bc.MultiGetClient[dm.WorkItemAttachment],
    bc.CreateClient[dm.WorkItemAttachment],
    bc.DeleteClient[dm.WorkItemAttachment],
):
    """A class to handle WorkItemAttachments."""

    _update_batch_size = 1
    _delete_batch_size = 1

    def _update(self, to_update: list[dm.WorkItemAttachment]) -> None:
        """Update the given work item attachment in Polarion."""
        item, multipart = self._prepare_patch_request(to_update)

        response = patch_work_item_attachment.sync_detailed(
            self._project_id,
            item.work_item_id,
            item.id,
            client=self._client.client,
            body=multipart,
        )
        self._raise_on_error(response)

    async def _async_update(
        self, to_update: list[dm.WorkItemAttachment]
    ) -> None:
        """Update the given work item attachment in Polarion."""
        item, multipart = self._prepare_patch_request(to_update)

        response = await patch_work_item_attachment.asyncio_detailed(
            self._project_id,
            item.work_item_id,
            item.id,
            client=self._client.client,
            body=multipart,
        )
        self._raise_on_error(response)

    def _prepare_patch_request(
        self, to_update: list[dm.WorkItemAttachment]
    ) -> tuple[
        dm.WorkItemAttachment, api_models.PatchWorkItemAttachmentsRequestBody
    ]:
        assert len(to_update) == 1, "Expected only one item"
        item = to_update[0]
        attributes = (
            api_models.WorkitemAttachmentsSinglePatchRequestDataAttributes()
        )
        if item.title:
            attributes.title = item.title
        multipart = api_models.PatchWorkItemAttachmentsRequestBody(
            resource=api_models.WorkitemAttachmentsSinglePatchRequest(
                data=api_models.WorkitemAttachmentsSinglePatchRequestData(
                    type_=api_models.WorkitemAttachmentsSinglePatchRequestDataType.WORKITEM_ATTACHMENTS,
                    # pylint: disable=line-too-long
                    id=f"{self._project_id}/{item.work_item_id}/{item.id}",
                    # pylint: disable=line-too-long
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
        return item, multipart

    def get_multi(  # type: ignore[override]
        self,
        work_item_id: str,
        *,
        page_size: int = 100,
        page_number: int = 1,
        fields: dict[str, str] | None = None,
        revision: str | None = None,
    ) -> tuple[list[dm.WorkItemAttachment], bool]:
        """Return the attachments for a given work item on a defined page.

        In addition, a flag whether a next page is available is
        returned. Define a fields dictionary as described in the
        Polarion API documentation to get certain fields.
        """
        if fields is None:
            fields = self._client.default_fields.workitem_attachments

        sparse_fields = self._build_sparse_fields(fields)
        response = get_work_item_attachments.sync_detailed(
            self._project_id,
            work_item_id=work_item_id,
            client=self._client.client,
            fields=sparse_fields,
            pagesize=page_size,
            pagenumber=page_number,
            revision=revision or oa_types.UNSET,
        )

        return self._process_get_response(response, work_item_id)

    async def async_get_multi(  # type: ignore[override]
        self,
        work_item_id: str,
        *,
        page_size: int = 100,
        page_number: int = 1,
        fields: dict[str, str] | None = None,
        revision: str | None = None,
    ) -> tuple[list[dm.WorkItemAttachment], bool]:
        """Return the attachments for a given work item on a defined page.

        In addition, a flag whether a next page is available is
        returned. Define a fields dictionary as described in the
        Polarion API documentation to get certain fields.
        """
        if fields is None:
            fields = self._client.default_fields.workitem_attachments

        sparse_fields = self._build_sparse_fields(fields)
        response = await get_work_item_attachments.asyncio_detailed(
            self._project_id,
            work_item_id=work_item_id,
            client=self._client.client,
            fields=sparse_fields,
            pagesize=page_size,
            pagenumber=page_number,
            revision=revision or oa_types.UNSET,
        )

        return self._process_get_response(response, work_item_id)

    def _process_get_response(
        self,
        response: oa_types.Response,
        work_item_id: str,
    ) -> tuple[list[dm.WorkItemAttachment], bool]:
        self._raise_on_error(response)
        parsed_response = response.parsed
        work_item_attachments: list[dm.WorkItemAttachment] = []
        next_page = False
        if (
            isinstance(
                parsed_response, api_models.WorkitemAttachmentsListGetResponse
            )
            and parsed_response.data
        ):
            for attachment in parsed_response.data:
                assert attachment.attributes
                assert isinstance(attachment.attributes.id, str)

                work_item_attachments.append(
                    dm.WorkItemAttachment(
                        work_item_id,
                        attachment.attributes.id,
                        self.unset_to_none(attachment.attributes.title),
                        file_name=self.unset_to_none(
                            attachment.attributes.file_name
                        ),
                    )
                )

            next_page = isinstance(
                parsed_response.links,
                api_models.WorkitemAttachmentsListGetResponseLinks,
            ) and bool(parsed_response.links.next_)
        return work_item_attachments, next_page

    def _create(self, items: list[dm.WorkItemAttachment]) -> None:
        """Create the given work item attachment in Polarion."""
        multipart = self._prepare_post_request(items)
        response = post_work_item_attachments.sync_detailed(
            self._project_id,
            items[0].work_item_id,
            client=self._client.client,
            body=multipart,
        )

        self._process_post_response(items, response)

    async def _async_create(self, items: list[dm.WorkItemAttachment]) -> None:
        """Create the given work item attachment in Polarion."""
        multipart = self._prepare_post_request(items)
        response = await post_work_item_attachments.asyncio_detailed(
            self._project_id,
            items[0].work_item_id,
            client=self._client.client,
            body=multipart,
        )

        self._process_post_response(items, response)

    def _process_post_response(
        self,
        items: list[dm.WorkItemAttachment],
        response: oa_types.Response,
    ) -> None:
        self._raise_on_error(response)
        parsed_response = response.parsed
        assert isinstance(
            parsed_response, api_models.WorkitemAttachmentsListPostResponse
        )
        assert parsed_response.data
        for counter, work_item_attachment_res in enumerate(
            parsed_response.data
        ):
            assert work_item_attachment_res.id
            items[counter].id = work_item_attachment_res.id.split("/")[-1]

    def _prepare_post_request(
        self, items: list[dm.WorkItemAttachment]
    ) -> api_models.PostWorkItemAttachmentsRequestBody:
        attachment_attributes = []
        attachment_files = []
        assert len(items), "No attachments were provided."
        assert all(
            [wia.work_item_id == items[0].work_item_id] for wia in items
        ), "All attachments must belong to the same WorkItem."
        for work_item_attachment in items:
            assert work_item_attachment.file_name, (
                "You have to define a FileName."
            )
            assert work_item_attachment.content_bytes, (
                "You have to provide content bytes."
            )
            assert work_item_attachment.mime_type, (
                "You have to provide a mime_type."
            )

            attributes = api_models.WorkitemAttachmentsListPostRequestDataItemAttributes(
                # pylint: disable=line-too-long
                file_name=work_item_attachment.file_name
            )
            if work_item_attachment.title:
                attributes.title = work_item_attachment.title

            attachment_attributes.append(
                api_models.WorkitemAttachmentsListPostRequestDataItem(
                    type_=api_models.WorkitemAttachmentsListPostRequestDataItemType.WORKITEM_ATTACHMENTS,
                    # pylint: disable=line-too-long
                    attributes=attributes,
                )
            )

            attachment_files.append(
                oa_types.File(
                    io.BytesIO(work_item_attachment.content_bytes),
                    work_item_attachment.file_name,
                    work_item_attachment.mime_type,
                )
            )
        return api_models.PostWorkItemAttachmentsRequestBody(
            resource=api_models.WorkitemAttachmentsListPostRequest(
                attachment_attributes
            ),
            files=attachment_files,
        )

    def _delete(self, items: list[dm.WorkItemAttachment]) -> None:
        assert len(items) == 1, "Expected only one item"
        item = items[0]
        response = delete_work_item_attachment.sync_detailed(
            self._project_id,
            item.work_item_id,
            item.id,
            client=self._client.client,
        )
        self._raise_on_error(response)

    async def _async_delete(self, items: list[dm.WorkItemAttachment]) -> None:
        assert len(items) == 1, "Expected only one item"
        item = items[0]
        response = await delete_work_item_attachment.asyncio_detailed(
            self._project_id,
            item.work_item_id,
            item.id,
            client=self._client.client,
        )
        self._raise_on_error(response)

# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
"""Implementation of a client providing work item specific functions."""

import json
import logging
import typing as t

from polarion_rest_api_client import data_models as dm
from polarion_rest_api_client import errors
from polarion_rest_api_client.open_api_client import models as api_models
from polarion_rest_api_client.open_api_client import types as oa_types
from polarion_rest_api_client.open_api_client.api.work_items import (
    delete_work_items,
    get_work_item,
    get_work_items,
    patch_work_items,
    post_work_items,
)

from . import base_classes as bc
from . import test_steps, work_item_attachments, work_item_links

WT = t.TypeVar("WT", bound=dm.WorkItem)
logger = logging.getLogger(__name__)
if t.TYPE_CHECKING:
    from polarion_rest_api_client import client as polarion_client


def _get_json_content_size(data: dict) -> int:
    return len(json.dumps(data).encode("utf-8"))


min_wi_request_size = _get_json_content_size(
    api_models.WorkitemsListPostRequest(data=[]).to_dict()
)
min_wi_patch_request_size = _get_json_content_size(
    api_models.WorkitemsListPatchRequest(data=[]).to_dict()
)


class WorkItems(
    bc.StatusItemClient,
    bc.MultiGetClient,
    bc.SingleGetClient,
    bc.DeleteClient,
    bc.CreateClient,
):
    """A project specific client for work item operations."""

    _retry_methods: t.ClassVar[set[str]] = {
        "_post_work_item_batch",
        "_a_post_work_item_batch",
        "_patch_work_item_batch",
        "_a_patch_work_item_batch",
    }

    def __init__(
        self,
        project_id: str,
        client: "polarion_client.PolarionClient",
        delete_status: str | None = None,
    ):
        super().__init__(project_id, client, delete_status)
        self.attachments = work_item_attachments.WorkItemAttachments(
            project_id, client
        )
        self.links = work_item_links.WorkItemLinks(project_id, client)
        self.test_steps = test_steps.TestSteps(project_id, client)
        self.item_cls = dm.WorkItem

    def _update(self, to_update: list[dm.WorkItem]) -> None:
        raise NotImplementedError("We have a custom update instead.")

    def _iter_patch_batches(
        self,
        items: t.Iterable[dm.WorkItem],
        item_builder: t.Callable[
            [dm.WorkItem], api_models.WorkitemsListPatchRequestDataItem
        ],
    ) -> t.Iterator[api_models.WorkitemsListPatchRequest]:
        current_batch = api_models.WorkitemsListPatchRequest(data=[])
        content_size = min_wi_patch_request_size

        for work_item in items:
            work_item_data = item_builder(work_item)
            proj_content_size, too_big = (
                self._calculate_patch_work_item_request_sizes(
                    work_item_data, content_size
                )
            )

            if too_big:
                raise errors.PolarionWorkItemException(
                    "A WorkItem is too large to update.", work_item
                )

            assert isinstance(current_batch.data, list)
            if (
                current_batch.data
                and proj_content_size > self._client.max_content_size
            ) or len(current_batch.data) >= self._client.batch_size:
                yield current_batch
                current_batch = api_models.WorkitemsListPatchRequest(
                    data=[work_item_data]
                )
                content_size = _get_json_content_size(current_batch.to_dict())
            else:
                t.cast(
                    list[api_models.WorkitemsListPatchRequestDataItem],
                    current_batch.data,
                ).append(work_item_data)
                content_size = proj_content_size

        if current_batch.data:
            yield current_batch

    def _iter_update_batches(
        self,
        items: list[dm.WorkItem],
    ) -> t.Iterator[api_models.WorkitemsListPatchRequest]:
        yield from self._iter_patch_batches(
            (item for item in items if self._has_content_to_patch(item)),
            self._build_work_item_list_patch_item,
        )

    def _iter_type_change_batches(
        self,
        items: list[dm.WorkItem],
    ) -> t.Iterator[tuple[api_models.WorkitemsListPatchRequest, str]]:
        grouped: dict[str, list[dm.WorkItem]] = {}
        for item in items:
            if item.type:
                grouped.setdefault(item.type, []).append(item)

        for batch_type, to_update in grouped.items():
            for batch in self._iter_patch_batches(
                to_update,
                self._build_work_item_type_change_patch_item,
            ):
                yield batch, batch_type

    def _iter_create_batches(
        self, items: list[dm.WorkItem]
    ) -> t.Iterator[
        tuple[api_models.WorkitemsListPostRequest, list[dm.WorkItem]]
    ]:
        current_batch = api_models.WorkitemsListPostRequest(data=[])
        content_size = min_wi_request_size
        batch_start_index = 0

        for batch_end_index, work_item in enumerate(items):
            work_item_data = self._build_work_item_post_request(work_item)

            (
                proj_content_size,
                too_big,
            ) = self._calculate_post_work_item_request_sizes(
                work_item_data, content_size
            )

            if too_big:
                raise errors.PolarionWorkItemException(
                    "A WorkItem is too large to create.", work_item
                )

            assert isinstance(current_batch.data, list)
            if (
                current_batch.data
                and proj_content_size > self._client.max_content_size
            ) or len(current_batch.data) >= self._client.batch_size:
                yield current_batch, items[batch_start_index:batch_end_index]
                current_batch = api_models.WorkitemsListPostRequest(
                    data=[work_item_data]
                )
                content_size = _get_json_content_size(current_batch.to_dict())
                batch_start_index = batch_end_index
            else:
                t.cast(
                    list[api_models.WorkitemsListPostRequestDataItem],
                    current_batch.data,
                ).append(work_item_data)
                content_size = proj_content_size

        if current_batch.data:
            yield current_batch, items[batch_start_index:]

    def update(
        self,
        items: dm.WorkItem | list[dm.WorkItem],
        *,
        workflow_action: str | None = None,
    ) -> None:
        """Update WorkItems and respect max body size and batch limits.

        If workflow_action is given, it is sent as the request-wide
        workflowAction query parameter on the attribute update pass, so
        Polarion applies the workflow transition to every updated item. It
        is not combined with the type-change pass, because Polarion rejects
        changeTypeTo and workflowAction on the same request.
        """
        if not isinstance(items, list):
            items = [items]

        for work_item_batch, type_change_to in self._iter_type_change_batches(
            items
        ):
            self._patch_work_item_batch(work_item_batch, type_change_to)

        for work_item_batch in self._iter_update_batches(items):
            self._patch_work_item_batch(
                work_item_batch, None, workflow_action=workflow_action
            )

    async def _async_update(self, to_update: list[dm.WorkItem]) -> None:
        raise NotImplementedError("We have a custom async_update instead.")

    async def async_update(
        self,
        items: dm.WorkItem | list[dm.WorkItem],
        *,
        workflow_action: str | None = None,
    ) -> None:
        """Update WorkItems and respect max body size and batch limits.

        See update for the workflow_action semantics.
        """
        if not isinstance(items, list):
            items = [items]

        await self._run_streaming_batch_calls(
            self._a_patch_work_item_batch(work_item_batch, type_change_to)
            for work_item_batch, type_change_to in self._iter_type_change_batches(
                items
            )
        )

        await self._run_streaming_batch_calls(
            self._a_patch_work_item_batch(
                work_item_batch,
                None,
                workflow_action=workflow_action,
            )
            for work_item_batch in self._iter_update_batches(items)
        )

    @t.overload  # type: ignore[override]
    def get_multi(
        self,
        query: str = "",
        *,
        page_size: int = 100,
        page_number: int = 1,
        fields: dict[str, str] | None = None,
        include: str | None = None,
        work_item_cls: type[WT],
        revision: str | None = None,
    ) -> tuple[list[WT], bool]:
        """Return the work items on a defined page matching the given query.

        In addition, a flag whether a next page is available is
        returned. Define a fields dictionary as described in the
        Polarion API documentation to get certain fields. This function
        will use the provided WorkItemClass as return type.
        """

    @t.overload
    def get_multi(
        self,
        query: str = "",
        *,
        page_size: int = 100,
        page_number: int = 1,
        fields: dict[str, str] | None = None,
        include: str | None = None,
        revision: str | None = None,
    ) -> tuple[list[dm.WorkItem], bool]:
        """Return the work items on a defined page matching the given query.

        In addition, a flag whether a next page is available is
        returned. Define a fields dictionary as described in the
        Polarion API documentation to get certain fields.
        """

    def get_multi(
        self,
        query: str = "",
        *,
        page_size: int = 100,
        page_number: int = 1,
        fields: dict[str, str] | None = None,
        include: str | None = None,
        work_item_cls: type[dm.WorkItem] = dm.WorkItem,
        revision: str | None = None,
    ) -> tuple[list[dm.WorkItem], bool] | tuple[list[WT], bool]:
        """Return the work items on a defined page matching the given query.

        In addition, a flag whether a next page is available is
        returned. Define a fields dictionary as described in the
        Polarion API documentation to get certain fields. Pass include
        (e.g. "author") to sideload related resources; user relationships
        are then resolved to display names under
        additional_attributes["<relationship>_name"].
        """
        if fields is None:
            fields = self._client.default_fields.workitems

        sparse_fields = self._build_sparse_fields(fields)
        response = get_work_items.sync_detailed(
            self._project_id,
            client=self._client.client,
            fields=sparse_fields,
            query=query,
            pagesize=page_size,
            pagenumber=page_number,
            include=include or oa_types.UNSET,
            revision=revision or oa_types.UNSET,
        )

        return self._process_get_response(work_item_cls, response)

    @t.overload  # type: ignore[override]
    async def async_get_multi(
        self,
        query: str = "",
        *,
        page_size: int = 100,
        page_number: int = 1,
        fields: dict[str, str] | None = None,
        include: str | None = None,
        work_item_cls: type[WT],
        revision: str | None = None,
    ) -> tuple[list[WT], bool]:
        """Return the work items on a defined page matching the given query.

        In addition, a flag whether a next page is available is
        returned. Define a fields dictionary as described in the
        Polarion API documentation to get certain fields. This function
        will use the provided WorkItemClass as return type.
        """

    @t.overload
    async def async_get_multi(
        self,
        query: str = "",
        *,
        page_size: int = 100,
        page_number: int = 1,
        fields: dict[str, str] | None = None,
        include: str | None = None,
        revision: str | None = None,
    ) -> tuple[list[dm.WorkItem], bool]:
        """Return the work items on a defined page matching the given query.

        In addition, a flag whether a next page is available is
        returned. Define a fields dictionary as described in the
        Polarion API documentation to get certain fields.
        """

    async def async_get_multi(
        self,
        query: str = "",
        *,
        page_size: int = 100,
        page_number: int = 1,
        fields: dict[str, str] | None = None,
        include: str | None = None,
        work_item_cls: type[dm.WorkItem] = dm.WorkItem,
        revision: str | None = None,
    ) -> tuple[list[dm.WorkItem], bool] | tuple[list[WT], bool]:
        """Return the work items on a defined page matching the given query.

        In addition, a flag whether a next page is available is
        returned. Define a fields dictionary as described in the
        Polarion API documentation to get certain fields. See get_multi
        for the include semantics.
        """
        if fields is None:
            fields = self._client.default_fields.workitems

        sparse_fields = self._build_sparse_fields(fields)
        response = await get_work_items.asyncio_detailed(
            self._project_id,
            client=self._client.client,
            fields=sparse_fields,
            query=query,
            pagesize=page_size,
            pagenumber=page_number,
            include=include or oa_types.UNSET,
            revision=revision or oa_types.UNSET,
        )

        self._raise_on_error(response)
        return self._process_get_response(work_item_cls, response)

    def _process_get_response(
        self,
        work_item_cls: type[WT],
        response: oa_types.Response,
    ) -> tuple[list[WT], bool]:
        self._raise_on_error(response)
        work_items_response = response.parsed
        work_items: list[WT] = []
        next_page = False
        if (
            isinstance(
                work_items_response, api_models.WorkitemsListGetResponse
            )
            and work_items_response.data
        ):
            user_names = self._user_names_from_included(
                work_items_response.included
            )
            work_items = [
                self._generate_work_item(work_item, work_item_cls, user_names)
                for work_item in work_items_response.data
                if not getattr(work_item.meta, "errors", [])
            ]

            next_page = isinstance(
                work_items_response.links,
                api_models.WorkitemsListGetResponseLinks,
            ) and bool(work_items_response.links.next_)
        return work_items, next_page

    @t.overload
    def get(
        self,
        work_item_id: str,
        work_item_cls: type[WT],
        revision: str | None = None,
        *,
        include: str | None = None,
    ) -> WT | None:
        """Return one specific work item with all fields.

        This also includes all linked work items and attachments. If
        there are to many of these to get them in one request, the
        truncated flags for linked_work_items and attachments will be
        set to True. This function will use the provided WorkItemClass
        as return type.
        """

    @t.overload
    def get(
        self,
        work_item_id: str,
        *,
        revision: str | None = None,
        include: str | None = None,
    ) -> dm.WorkItem | None:
        """Return one specific work item with all fields.

        This also includes all linked work items and attachments. If
        there are to many of these to get them in one request, the
        truncated flags for linked_work_items and attachments will be
        set to True.
        """

    def get(
        self,
        work_item_id: str,
        work_item_cls: type[dm.WorkItem] = dm.WorkItem,
        revision: str | None = None,
        *,
        include: str | None = None,
    ) -> WT | dm.WorkItem | None:
        """Return one specific work item with all fields.

        This also includes all linked work items and attachments. If
        there are to many of these to get them in one request, the
        truncated flags for linked_work_items and attachments will be
        set to True. Pass include (e.g. "author") to sideload related
        resources; user relationships are then resolved to display names
        under additional_attributes["<relationship>_name"].
        """
        response = get_work_item.sync_detailed(
            self._project_id,
            work_item_id,
            client=self._client.client,
            fields=self._build_sparse_fields(
                {
                    "workitems": "@all",
                    "workitem_attachments": "@all",
                    "linkedworkitems": "@all",
                    "users": "name",
                }
            ),
            include=include or oa_types.UNSET,
            revision=revision or oa_types.UNSET,
        )
        return self._process_single_get_response(response, work_item_cls)

    @t.overload
    async def async_get(
        self,
        work_item_id: str,
        work_item_cls: type[WT],
        revision: str | None = None,
        *,
        include: str | None = None,
    ) -> WT | None:
        """Return one specific work item with all fields.

        This also includes all linked work items and attachments. If
        there are to many of these to get them in one request, the
        truncated flags for linked_work_items and attachments will be
        set to True. This function will use the provided WorkItemClass
        as return type.
        """

    @t.overload
    async def async_get(
        self,
        work_item_id: str,
        *,
        revision: str | None = None,
        include: str | None = None,
    ) -> dm.WorkItem | None:
        """Return one specific work item with all fields.

        This also includes all linked work items and attachments. If
        there are to many of these to get them in one request, the
        truncated flags for linked_work_items and attachments will be
        set to True.
        """

    async def async_get(
        self,
        work_item_id: str,
        work_item_cls: type[dm.WorkItem] = dm.WorkItem,
        revision: str | None = None,
        *,
        include: str | None = None,
    ) -> WT | dm.WorkItem | None:
        """Return one specific work item with all fields.

        This also includes all linked work items and attachments. If
        there are to many of these to get them in one request, the
        truncated flags for linked_work_items and attachments will be
        set to True. See get for the include semantics.
        """
        response = await get_work_item.asyncio_detailed(
            self._project_id,
            work_item_id,
            client=self._client.client,
            fields=self._build_sparse_fields(
                {
                    "workitems": "@all",
                    "workitem_attachments": "@all",
                    "linkedworkitems": "@all",
                    "users": "name",
                }
            ),
            include=include or oa_types.UNSET,
            revision=revision or oa_types.UNSET,
        )
        return self._process_single_get_response(response, work_item_cls)

    def _process_single_get_response(
        self,
        response: oa_types.Response,
        work_item_cls: type[WT],
    ) -> WT | None:
        self._raise_on_error(response)
        parsed_response = response.parsed
        work_item = None
        if isinstance(
            parsed_response, api_models.WorkitemsSingleGetResponse
        ) and isinstance(
            parsed_response.data, api_models.WorkitemsSingleGetResponseData
        ):
            work_item = self._generate_work_item(
                parsed_response.data,
                work_item_cls,
                self._user_names_from_included(parsed_response.included),
            )
        return work_item

    def _create(self, items: list[dm.WorkItem]) -> None:
        raise NotImplementedError("We have a custom create instead.")

    def create(self, items: dm.WorkItem | list[dm.WorkItem]) -> None:
        """Create WorkItems and respect the max body size of the server."""
        if not isinstance(items, list):
            items = [items]

        for work_item_batch, work_item_objs in self._iter_create_batches(
            items
        ):
            self._post_work_item_batch(work_item_batch, work_item_objs)

    async def _async_create(self, items: list[dm.WorkItem]) -> None:
        raise NotImplementedError("We have a custom async_create instead.")

    async def async_create(
        self, items: dm.WorkItem | list[dm.WorkItem]
    ) -> None:
        """Create WorkItems and respect the max body size of the server."""
        if not isinstance(items, list):
            items = [items]

        await self._run_streaming_batch_calls(
            self._a_post_work_item_batch(work_item_batch, work_item_objs)
            for work_item_batch, work_item_objs in self._iter_create_batches(
                items
            )
        )

    def _delete(self, items: list[dm.WorkItem]) -> None:
        response = delete_work_items.sync_detailed(
            self._project_id,
            client=self._client.client,
            body=self._build_delete_body(items),
        )
        self._raise_on_error(response)

    async def _async_delete(self, items: list[dm.WorkItem]) -> None:
        response = await delete_work_items.asyncio_detailed(
            self._project_id,
            client=self._client.client,
            body=self._build_delete_body(items),
        )
        self._raise_on_error(response)

    def _build_delete_body(
        self, items: list[dm.WorkItem]
    ) -> api_models.WorkitemsListDeleteRequest:
        work_item_ids = [work_item.id for work_item in items if work_item.id]
        return api_models.WorkitemsListDeleteRequest(
            data=[
                api_models.WorkitemsListDeleteRequestDataItem(
                    type_=api_models.WorkitemsListDeleteRequestDataItemType.WORKITEMS,
                    # pylint: disable=line-too-long
                    id=f"{self._project_id}/{work_item_id}",
                )
                for work_item_id in work_item_ids
            ]
        )

    def _build_work_item_post_request(
        self, work_item: dm.WorkItem
    ) -> api_models.WorkitemsListPostRequestDataItem:
        assert work_item.type is not None

        attrs = api_models.WorkitemsListPostRequestDataItemAttributes(
            type_=work_item.type,
            description=(
                api_models.WorkitemsListPostRequestDataItemAttributesDescription(  # pylint: disable=line-too-long
                    type_=api_models.WorkitemsListPostRequestDataItemAttributesDescriptionType(  # pylint: disable=line-too-long
                        work_item.description.type
                    ),
                    value=work_item.description.value or "",
                )
                if work_item.description
                else oa_types.UNSET
            ),
            status=work_item.status or oa_types.UNSET,
            title=work_item.title or oa_types.UNSET,
            hyperlinks=oa_types.UNSET
            if work_item.hyperlinks is None
            else [
                api_models.WorkitemsListPostRequestDataItemAttributesHyperlinksItem(
                    role=hyperlink.role or oa_types.UNSET,
                    title=hyperlink.title or oa_types.UNSET,
                    uri=hyperlink.uri or oa_types.UNSET,
                )
                for hyperlink in work_item.hyperlinks
            ],
        )

        attrs.additional_properties.update(work_item.additional_attributes)

        return api_models.WorkitemsListPostRequestDataItem(
            type_=api_models.WorkitemsListPostRequestDataItemType.WORKITEMS,
            attributes=attrs,
            # pylint: disable=line-too-long
            relationships=(
                api_models.WorkitemsListPostRequestDataItemRelationships(
                    module=api_models.WorkitemsListPostRequestDataItemRelationshipsModule(
                        data=api_models.WorkitemsListPostRequestDataItemRelationshipsModuleData(
                            id=f"{self._project_id}/{doc_ref.module_folder}/{doc_ref.module_name}",
                            type_=api_models.WorkitemsListPostRequestDataItemRelationshipsModuleDataType.DOCUMENTS,
                        ),
                    )
                )
                if (doc_ref := work_item.home_document) is not None
                else oa_types.UNSET
            ),
            # pylint: enable=line-too-long
        )

    def _build_work_item_patch_request(
        self, work_item: dm.WorkItem
    ) -> api_models.WorkitemsSinglePatchRequest:
        attrs = api_models.WorkitemsSinglePatchRequestDataAttributes()
        if work_item.home_document:
            logger.warning(
                "Changing the work items home document is not supported."
            )

        if work_item.title is not None:
            attrs.title = work_item.title

        if work_item.description is not None:
            attrs.description = api_models.WorkitemsSinglePatchRequestDataAttributesDescription(  # pylint: disable=line-too-long
                type_=api_models.WorkitemsSinglePatchRequestDataAttributesDescriptionType(  # pylint: disable=line-too-long
                    work_item.description.type
                ),
                value=work_item.description.value or "",
            )

        if work_item.status is not None:
            attrs.status = work_item.status

        if work_item.hyperlinks is not None:
            attrs.hyperlinks = [
                api_models.WorkitemsSinglePatchRequestDataAttributesHyperlinksItem(
                    role=hyperlink.role or oa_types.UNSET,
                    title=hyperlink.title or oa_types.UNSET,
                    uri=hyperlink.uri or oa_types.UNSET,
                )
                for hyperlink in work_item.hyperlinks
            ]

        attrs.additional_properties.update(work_item.additional_attributes)

        return api_models.WorkitemsSinglePatchRequest(
            data=api_models.WorkitemsSinglePatchRequestData(
                type_=api_models.WorkitemsSinglePatchRequestDataType.WORKITEMS,
                id=f"{self._project_id}/{work_item.id}",
                attributes=attrs,
            )
        )

    def _build_work_item_list_patch_item(
        self, work_item: dm.WorkItem
    ) -> api_models.WorkitemsListPatchRequestDataItem:
        attrs = api_models.WorkitemsListPatchRequestDataItemAttributes()

        if work_item.home_document:
            logger.warning(
                "Changing the work items home document is not supported."
            )

        if work_item.title is not None:
            attrs.title = work_item.title

        if work_item.description is not None:
            attrs.description = api_models.WorkitemsListPatchRequestDataItemAttributesDescription(  # pylint: disable=line-too-long
                type_=api_models.WorkitemsListPatchRequestDataItemAttributesDescriptionType(  # pylint: disable=line-too-long
                    work_item.description.type
                ),
                value=work_item.description.value or "",
            )

        if work_item.status is not None:
            attrs.status = work_item.status

        if work_item.hyperlinks is not None:
            attrs.hyperlinks = [
                api_models.WorkitemsListPatchRequestDataItemAttributesHyperlinksItem(
                    role=hyperlink.role or oa_types.UNSET,
                    title=hyperlink.title or oa_types.UNSET,
                    uri=hyperlink.uri or oa_types.UNSET,
                )
                for hyperlink in work_item.hyperlinks
            ]

        attrs.additional_properties.update(work_item.additional_attributes)
        if work_item.id is None:
            raise errors.PolarionWorkItemException(
                "A WorkItem ID is required to update.",
                work_item,
            )

        return api_models.WorkitemsListPatchRequestDataItem(
            type_=api_models.WorkitemsListPatchRequestDataItemType.WORKITEMS,
            id=f"{self._project_id}/{work_item.id}",
            attributes=attrs,
        )

    def _build_work_item_type_change_patch_item(
        self, work_item: dm.WorkItem
    ) -> api_models.WorkitemsListPatchRequestDataItem:
        if work_item.id is None:
            raise errors.PolarionWorkItemException(
                "A WorkItem ID is required to update.",
                work_item,
            )

        logger.warning(
            "Attempting to change the type of Work Item %s to %s.",
            work_item.id,
            work_item.type,
        )

        return api_models.WorkitemsListPatchRequestDataItem(
            type_=api_models.WorkitemsListPatchRequestDataItemType.WORKITEMS,
            id=f"{self._project_id}/{work_item.id}",
            attributes=api_models.WorkitemsListPatchRequestDataItemAttributes(),
        )

    def _has_content_to_patch(self, work_item: dm.WorkItem) -> bool:
        return any(
            [
                work_item.title is not None,
                work_item.description is not None,
                work_item.status is not None,
                work_item.hyperlinks is not None,
                bool(work_item.additional_attributes),
                work_item.home_document is not None,
            ]
        )

    def _calculate_patch_work_item_request_sizes(
        self,
        work_item_data: api_models.WorkitemsListPatchRequestDataItem,
        current_content_size: int = min_wi_patch_request_size,
    ) -> tuple[int, bool]:
        work_item_size = _get_json_content_size(work_item_data.to_dict())

        proj_content_size = current_content_size + work_item_size
        if current_content_size != min_wi_patch_request_size:
            proj_content_size += len(b", ")

        return (
            proj_content_size,
            (work_item_size + min_wi_patch_request_size)
            > self._client.max_content_size,
        )

    def _patch_work_item_batch(
        self,
        work_item_batch: api_models.WorkitemsListPatchRequest,
        batch_type: str | None,
        workflow_action: str | None = None,
    ) -> None:
        response = patch_work_items.sync_detailed(
            self._project_id,
            client=self._client.client,
            change_type_to=batch_type or oa_types.UNSET,
            workflow_action=workflow_action or oa_types.UNSET,
            body=work_item_batch,
        )
        self._raise_on_error(response)

    async def _a_patch_work_item_batch(
        self,
        work_item_batch: api_models.WorkitemsListPatchRequest,
        batch_type: str | None,
        workflow_action: str | None = None,
    ) -> None:
        response = await patch_work_items.asyncio_detailed(
            self._project_id,
            client=self._client.client,
            change_type_to=batch_type or oa_types.UNSET,
            workflow_action=workflow_action or oa_types.UNSET,
            body=work_item_batch,
        )
        self._raise_on_error(response)

    def _post_work_item_batch(
        self,
        work_item_batch: api_models.WorkitemsListPostRequest,
        work_item_objs: list[dm.WorkItem],
    ) -> None:
        response = post_work_items.sync_detailed(
            self._project_id, client=self._client.client, body=work_item_batch
        )

        self._raise_on_error(response)

        self._process_post_response(response, work_item_objs)

    async def _a_post_work_item_batch(
        self,
        work_item_batch: api_models.WorkitemsListPostRequest,
        work_item_objs: list[dm.WorkItem],
    ) -> None:
        response = await post_work_items.asyncio_detailed(
            self._project_id, client=self._client.client, body=work_item_batch
        )

        self._raise_on_error(response)

        self._process_post_response(response, work_item_objs)

    def _process_post_response(
        self, response: oa_types.Response, work_item_objs: list[dm.WorkItem]
    ) -> None:
        assert isinstance(
            response.parsed, api_models.WorkitemsListPostResponse
        )
        assert response.parsed.data
        for index, work_item_res in enumerate(response.parsed.data):
            assert work_item_res.id
            work_item_objs[index].id = work_item_res.id.split("/")[-1]

    def _calculate_post_work_item_request_sizes(
        self,
        work_item_data: api_models.WorkitemsListPostRequestDataItem,
        current_content_size: int = min_wi_request_size,
    ) -> tuple[int, bool]:
        work_item_size = _get_json_content_size(work_item_data.to_dict())

        proj_content_size = current_content_size + work_item_size
        if current_content_size != min_wi_request_size:
            proj_content_size += len(b", ")

        return (
            proj_content_size,
            (work_item_size + min_wi_request_size)
            > self._client.max_content_size,
        )

    def _generate_work_item(
        self,
        work_item: (
            api_models.WorkitemsListGetResponseDataItem
            | api_models.WorkitemsSingleGetResponseData
        ),
        work_item_cls: type[WT],
        user_names: dict[str, str] | None = None,
    ) -> WT:
        assert work_item.attributes
        assert isinstance(work_item.id, str)
        work_item_id = work_item.id.split("/")[-1]
        links = []
        attachments = []
        home_document: dm.DocumentReference | None = None
        additional_attributes = work_item.attributes.additional_properties

        # We set both truncated flags to True and will only set them to False,
        # if the corresponding fields were requested and returned completely
        links_truncated = True
        attachments_truncated = True
        if work_item.relationships:
            if (
                (home_document_data := work_item.relationships.module)
                and home_document_data.data
                and home_document_data.data.id
            ):
                _, folder, name = home_document_data.data.id.split("/")
                home_document = dm.DocumentReference(folder, name)

            if link_data := work_item.relationships.linked_work_items:
                if (
                    not link_data.meta
                    or link_data.meta.total_count is oa_types.UNSET
                ):
                    links_truncated = False

                links = [
                    self.links._parse_work_item_link(
                        link.id or "",
                        link.additional_properties.get("suspect", False),
                        work_item_id,
                        link.additional_properties.get(
                            "revision", oa_types.UNSET
                        ),
                    )
                    for link in link_data.data or []
                ]

            if attachment_data := work_item.relationships.attachments:
                if (
                    not attachment_data.meta
                    or attachment_data.meta.total_count is oa_types.UNSET
                ):
                    attachments_truncated = False

                attachments = [
                    dm.WorkItemAttachment(
                        work_item_id,
                        attachment.id.split("/")[-1],
                        None,  # title isn't provided
                    )
                    for attachment in attachment_data.data or []
                    if attachment.id
                ]

            if (
                rel_additional_attributes
                := work_item.relationships.additional_properties
            ):
                for key, value in rel_additional_attributes.items():
                    if (
                        isinstance(value, dict)
                        and value.get("data", {}).get("type") == "users"
                    ):
                        user_id = value["data"]["id"]
                        additional_attributes[key] = user_id
                        # Surface the display name (when include= resolved
                        # the user) under a derived <relationship>_name key,
                        # leaving the id key untouched.
                        if user_names and user_id in user_names:
                            additional_attributes[f"{key}_name"] = user_names[
                                user_id
                            ]

            # Standard user relationships (author, assignee) are typed
            # fields, not part of additional_properties, so the loop above
            # never sees them. Only resolve them when include= sideloaded
            # users, keeping the default output unchanged.
            if user_names:
                self._resolve_named_user_relationship(
                    additional_attributes,
                    "author",
                    getattr(work_item.relationships, "author", None),
                    user_names,
                )
                self._resolve_named_user_relationship(
                    additional_attributes,
                    "assignee",
                    getattr(work_item.relationships, "assignee", None),
                    user_names,
                )

        description = None
        if work_item.attributes.description:
            description = dm.TextContent(
                None
                if work_item.attributes.description.type_ is oa_types.UNSET
                else str(work_item.attributes.description.type_),
                self.unset_to_none(work_item.attributes.description.value),
            )

        hyperlinks = None
        if isinstance(work_item.attributes.hyperlinks, list):
            hyperlinks = [
                dm.HyperLink(
                    role=self.unset_to_none(hyperlink.role),
                    title=self.unset_to_none(hyperlink.title),
                    uri=self.unset_to_none(hyperlink.uri),
                )
                for hyperlink in work_item.attributes.hyperlinks
            ]
        return work_item_cls(
            work_item_id,
            title=self.unset_to_none(work_item.attributes.title),
            description=description,
            type=self.unset_to_none(work_item.attributes.type_),
            status=self.unset_to_none(work_item.attributes.status),
            additional_attributes=additional_attributes,
            linked_work_items=links,
            attachments=attachments,
            linked_work_items_truncated=links_truncated,
            attachments_truncated=attachments_truncated,
            home_document=home_document,
            hyperlinks=hyperlinks,
        )

# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
"""Implementation of LinkedWorkItems operations."""

import itertools
import typing as t

from polarion_rest_api_client import data_models as dm
from polarion_rest_api_client.open_api_client import models as api_models
from polarion_rest_api_client.open_api_client import types as oa_types
from polarion_rest_api_client.open_api_client.api.linked_work_items import (
    delete_linked_work_items,
    get_backlinked_work_items,
    get_linked_work_items,
    patch_linked_work_item,
    post_linked_work_items,
)

from . import base_classes as bc

LINK_ID_PART_COUNT = 5


class WorkItemLinks(
    bc.CreateClient[dm.WorkItemLink],
    bc.MultiGetClient[dm.WorkItemLink],
    bc.DeleteClient[dm.WorkItemLink],
):
    """A client providing LinkedWorkItems functions."""

    def get_multi(  # type: ignore[override]
        self,
        work_item_id: str,
        *,
        page_size: int = 100,
        page_number: int = 1,
        fields: dict[str, str] | None = None,
        include: str | None | oa_types.Unset = None,
        revision: str | None | oa_types.Unset = None,
    ) -> tuple[list[dm.WorkItemLink], bool]:
        """Get the work item links for the given work item on a page.

        In addition, a flag whether a next page is available is
        returned. Define a fields dictionary as described in the
        Polarion API documentation to get certain fields.
        """
        if fields is None:
            fields = self._client.default_fields.linkedworkitems

        response = get_linked_work_items.sync_detailed(
            self._project_id,
            work_item_id,
            client=self._client.client,
            fields=self._build_sparse_fields(fields),
            include=self.none_to_unset(include),
            pagesize=page_size,
            pagenumber=page_number,
            revision=revision or oa_types.UNSET,
        )

        return self._parse_get_response(response, work_item_id)

    async def async_get_multi(  # type: ignore[override]
        self,
        work_item_id: str,
        *,
        page_size: int = 100,
        page_number: int = 1,
        fields: dict[str, str] | None = None,
        include: str | None | oa_types.Unset = None,
        revision: str | None | oa_types.Unset = None,
    ) -> tuple[list[dm.WorkItemLink], bool]:
        """Get the work item links for the given work item on a page.

        In addition, a flag whether a next page is available is
        returned. Define a fields dictionary as described in the
        Polarion API documentation to get certain fields.
        """
        if fields is None:
            fields = self._client.default_fields.linkedworkitems

        response = await get_linked_work_items.asyncio_detailed(
            self._project_id,
            work_item_id,
            client=self._client.client,
            fields=self._build_sparse_fields(fields),
            include=self.none_to_unset(include),
            pagesize=page_size,
            pagenumber=page_number,
            revision=revision or oa_types.UNSET,
        )

        return self._parse_get_response(response, work_item_id)

    def get_backlinks(
        self,
        work_item_id: str,
        *,
        page_size: int = 100,
        page_number: int = 1,
        fields: dict[str, str] | None = None,
        include: str | None | oa_types.Unset = None,
        revision: str | None | oa_types.Unset = None,
    ) -> tuple[list[dm.WorkItemLink], bool]:
        """Get the links pointing at the given work item on a page.

        Each returned link's ``primary_work_item_id`` names the work item
        that holds the link, and the queried work item is its target. In
        addition, a flag whether a next page is available is returned.
        """
        if fields is None:
            fields = self._client.default_fields.linkedworkitems

        response = get_backlinked_work_items.sync_detailed(
            self._project_id,
            work_item_id,
            client=self._client.client,
            fields=self._build_sparse_fields(fields),
            include=self.none_to_unset(include),
            pagesize=page_size,
            pagenumber=page_number,
            revision=revision or oa_types.UNSET,
        )

        return self._parse_get_response(response, work_item_id, backlink=True)

    async def async_get_backlinks(
        self,
        work_item_id: str,
        *,
        page_size: int = 100,
        page_number: int = 1,
        fields: dict[str, str] | None = None,
        include: str | None | oa_types.Unset = None,
        revision: str | None | oa_types.Unset = None,
    ) -> tuple[list[dm.WorkItemLink], bool]:
        """Get the links pointing at the given work item on a page.

        Each returned link's ``primary_work_item_id`` names the work item
        that holds the link, and the queried work item is its target. In
        addition, a flag whether a next page is available is returned.
        """
        if fields is None:
            fields = self._client.default_fields.linkedworkitems

        response = await get_backlinked_work_items.asyncio_detailed(
            self._project_id,
            work_item_id,
            client=self._client.client,
            fields=self._build_sparse_fields(fields),
            include=self.none_to_unset(include),
            pagesize=page_size,
            pagenumber=page_number,
            revision=revision or oa_types.UNSET,
        )

        return self._parse_get_response(response, work_item_id, backlink=True)

    def update(self, link: dm.WorkItemLink) -> None:
        """Update the ``suspect`` flag (and revision) of a single link."""
        response = patch_linked_work_item.sync_detailed(
            *self._patch_path(link),
            client=self._client.client,
            body=self._build_patch_body(link),
        )
        self._raise_on_error(response)

    async def async_update(self, link: dm.WorkItemLink) -> None:
        """Update the ``suspect`` flag (and revision) of a single link."""
        response = await patch_linked_work_item.asyncio_detailed(
            *self._patch_path(link),
            client=self._client.client,
            body=self._build_patch_body(link),
        )
        self._raise_on_error(response)

    def _patch_path(
        self, link: dm.WorkItemLink
    ) -> tuple[str, str, str, str, str]:
        return (
            self._project_id,
            link.primary_work_item_id,
            link.role,
            link.secondary_work_item_project or self._project_id,
            link.secondary_work_item_id,
        )

    def _build_patch_body(
        self, link: dm.WorkItemLink
    ) -> api_models.LinkedworkitemsSinglePatchRequest:
        # pylint: disable=line-too-long
        link_id = "/".join(self._patch_path(link))
        return api_models.LinkedworkitemsSinglePatchRequest(
            data=api_models.LinkedworkitemsSinglePatchRequestData(
                type_=api_models.LinkedworkitemsSinglePatchRequestDataType.LINKEDWORKITEMS,
                id=link_id,
                attributes=api_models.LinkedworkitemsSinglePatchRequestDataAttributes(
                    suspect=link.suspect or False,
                    revision=link.secondary_work_item_revision
                    or oa_types.UNSET,
                ),
            )
        )
        # pylint: enable=line-too-long

    def _parse_get_response(
        self,
        response: oa_types.Response,
        work_item_id: str,
        *,
        backlink: bool = False,
    ) -> tuple[list[dm.WorkItemLink], bool]:
        self._raise_on_error(response)
        linked_work_item_response = response.parsed
        work_item_links: list[dm.WorkItemLink] = []
        next_page = False
        if (
            isinstance(
                linked_work_item_response,
                api_models.LinkedworkitemsListGetResponse,
            )
            and linked_work_item_response.data
        ):
            for link in linked_work_item_response.data:
                assert isinstance(link.id, str)
                assert isinstance(
                    link.attributes,
                    api_models.LinkedworkitemsListGetResponseDataItemAttributes,
                    # pylint: disable=line-too-long
                )

                work_item_links.append(
                    self._parse_work_item_link(
                        link.id,
                        link.attributes.suspect,
                        work_item_id,
                        link.attributes.revision,
                        backlink=backlink,
                    )
                )

            next_page = isinstance(
                linked_work_item_response.links,
                api_models.LinkedworkitemsListGetResponseLinks,
            ) and bool(linked_work_item_response.links.next_)
        return work_item_links, next_page

    def _parse_work_item_link(
        self,
        link_id: str,
        suspect: bool | oa_types.Unset,
        work_item_id: str,
        revision: str | oa_types.Unset,
        *,
        backlink: bool = False,
    ) -> dm.WorkItemLink:
        info = link_id.split("/")
        assert len(info) == LINK_ID_PART_COUNT
        source_project_id, source_work_item_id = info[:2]
        role_id, target_project_id, linked_work_item_id = info[2:]

        if backlink:
            # A backlink id names the linking (source) work item; the queried
            # work item is the target. Flip so primary_work_item_id is the
            # source that actually holds the link.
            return dm.WorkItemLink(
                source_work_item_id,
                linked_work_item_id,
                role_id,
                None if isinstance(suspect, oa_types.Unset) else suspect,
                source_project_id,
                None if isinstance(revision, oa_types.Unset) else revision,
            )

        return dm.WorkItemLink(
            work_item_id,
            linked_work_item_id,
            role_id,
            None if isinstance(suspect, oa_types.Unset) else suspect,
            target_project_id,
            None if isinstance(revision, oa_types.Unset) else revision,
        )

    def _pre_batching_grouping(
        self, items: list[dm.WorkItemLink]
    ) -> t.Generator[list[dm.WorkItemLink], None, None]:
        for _, group in itertools.groupby(
            items, lambda x: x.primary_work_item_id
        ):
            yield list(group)

    def _create(self, items: list[dm.WorkItemLink]) -> None:
        response = post_linked_work_items.sync_detailed(
            self._project_id,
            items[0].primary_work_item_id,
            client=self._client.client,
            body=self._create_post_body(items),
        )

        self._raise_on_error(response)

    async def _async_create(self, items: list[dm.WorkItemLink]) -> None:
        response = await post_linked_work_items.asyncio_detailed(
            self._project_id,
            items[0].primary_work_item_id,
            client=self._client.client,
            body=self._create_post_body(items),
        )

        self._raise_on_error(response)

    def _create_post_body(
        self, items: list[dm.WorkItemLink]
    ) -> api_models.LinkedworkitemsListPostRequest:
        # pylint: disable=line-too-long
        return api_models.LinkedworkitemsListPostRequest(
            data=[
                api_models.LinkedworkitemsListPostRequestDataItem(
                    type_=api_models.LinkedworkitemsListPostRequestDataItemType.LINKEDWORKITEMS,
                    attributes=api_models.LinkedworkitemsListPostRequestDataItemAttributes(
                        role=work_item_link.role,
                        suspect=work_item_link.suspect or False,
                        revision=work_item_link.secondary_work_item_revision
                        or oa_types.UNSET,
                    ),
                    relationships=api_models.LinkedworkitemsListPostRequestDataItemRelationships(
                        work_item=api_models.LinkedworkitemsListPostRequestDataItemRelationshipsWorkItem(
                            data=api_models.LinkedworkitemsListPostRequestDataItemRelationshipsWorkItemData(
                                type_=api_models.LinkedworkitemsListPostRequestDataItemRelationshipsWorkItemDataType.WORKITEMS,
                                id=f"{work_item_link.secondary_work_item_project or self._project_id}/{work_item_link.secondary_work_item_id}",
                            )
                        )
                    ),
                )
                for work_item_link in items
            ]
        )

    # pylint: enable=line-too-long

    def _delete(self, items: list[dm.WorkItemLink]) -> None:
        response = delete_linked_work_items.sync_detailed(
            self._project_id,
            items[0].primary_work_item_id,
            client=self._client.client,
            body=self._create_delete_body(items),
        )
        self._raise_on_error(response)

    async def _async_delete(self, items: list[dm.WorkItemLink]) -> None:
        response = await delete_linked_work_items.asyncio_detailed(
            self._project_id,
            items[0].primary_work_item_id,
            client=self._client.client,
            body=self._create_delete_body(items),
        )
        self._raise_on_error(response)

    def _create_delete_body(
        self, items: list[dm.WorkItemLink]
    ) -> api_models.LinkedworkitemsListDeleteRequest:
        # pylint: disable=line-too-long
        return api_models.LinkedworkitemsListDeleteRequest(
            data=[
                api_models.LinkedworkitemsListDeleteRequestDataItem(
                    type_=api_models.LinkedworkitemsListDeleteRequestDataItemType.LINKEDWORKITEMS,
                    id=f"{self._project_id}/{work_item_link.primary_work_item_id}/{work_item_link.role}/{work_item_link.secondary_work_item_project or self._project_id}/{work_item_link.secondary_work_item_id}",
                )
                for work_item_link in items
            ]
        )
        # pylint: enable=line-too-long

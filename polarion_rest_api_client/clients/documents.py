# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
"""Implementation of the documents client."""

import itertools
import logging
import typing as t
import urllib.parse

from polarion_rest_api_client import data_models as dm
from polarion_rest_api_client.open_api_client import models as api_models
from polarion_rest_api_client.open_api_client import types as oa_types
from polarion_rest_api_client.open_api_client.api.documents import (
    get_document,
    get_documents,
    patch_document,
    post_documents,
)

from . import base_classes as bc

logger = logging.getLogger(__name__)


class Documents(
    bc.SingleGetClient,
    bc.MultiGetClient[dm.Document],
    bc.CreateClient,
    bc.UpdateClient[dm.Document],
):
    """A client to work with documents in Polarion."""

    _update_batch_size = 1

    def get(
        self,
        space_id: str,
        document_name: str,
        fields: dict[str, str] | None = None,
        include: str | None | oa_types.Unset = None,
        revision: str | None | oa_types.Unset = None,
    ) -> dm.Document | None:
        """Return the document with the given document_name and space_id."""
        if fields is None:
            fields = self._client.default_fields.documents

        response = get_document.sync_detailed(
            self._project_id,
            urllib.parse.quote(space_id, safe="/", encoding=None, errors=None),
            urllib.parse.quote(
                document_name, safe="/", encoding=None, errors=None
            ),
            client=self._client.client,
            fields=self._build_sparse_fields(fields),
            include=self.none_to_unset(include),
            revision=self.none_to_unset(revision),
        )

        return self._parse_document_response(response)

    async def async_get(
        self,
        space_id: str,
        document_name: str,
        fields: dict[str, str] | None = None,
        include: str | None | oa_types.Unset = None,
        revision: str | None | oa_types.Unset = None,
    ) -> dm.Document | None:
        """Return the document with the given document_name and space_id."""
        if fields is None:
            fields = self._client.default_fields.documents

        response = await get_document.asyncio_detailed(
            self._project_id,
            urllib.parse.quote(space_id, safe="/", encoding=None, errors=None),
            urllib.parse.quote(
                document_name, safe="/", encoding=None, errors=None
            ),
            client=self._client.client,
            fields=self._build_sparse_fields(fields),
            include=self.none_to_unset(include),
            revision=self.none_to_unset(revision),
        )

        return self._parse_document_response(response)

    def _parse_document_response(
        self, response: oa_types.Response
    ) -> dm.Document | None:
        self._raise_on_error(response)
        document_response = response.parsed
        if (
            isinstance(
                document_response, api_models.DocumentsSingleGetResponse
            )
            and (data := document_response.data)
            and not getattr(data.meta, "errors", [])
        ):
            user_names = self._user_names_from_included(
                document_response.included
            )
            return self._generate_document(data, user_names)
        return None

    def get_multi(  # type: ignore[override]
        self,
        query: str = "",
        *,
        page_size: int = 100,
        page_number: int = 1,
        fields: dict[str, str] | None = None,
        include: str | None = None,
    ) -> tuple[list[dm.Document], bool]:
        """Return the documents on a page matching the given query."""
        if fields is None:
            fields = self._client.default_fields.documents

        response = get_documents.sync_detailed(
            self._project_id,
            client=self._client.client,
            fields=self._build_sparse_fields(fields),
            query=query,
            include=include or oa_types.UNSET,
            pagesize=page_size,
            pagenumber=page_number,
        )
        return self._parse_documents_response(response)

    async def async_get_multi(  # type: ignore[override]
        self,
        query: str = "",
        *,
        page_size: int = 100,
        page_number: int = 1,
        fields: dict[str, str] | None = None,
        include: str | None = None,
    ) -> tuple[list[dm.Document], bool]:
        """Return the documents on a page matching the given query."""
        if fields is None:
            fields = self._client.default_fields.documents

        response = await get_documents.asyncio_detailed(
            self._project_id,
            client=self._client.client,
            fields=self._build_sparse_fields(fields),
            query=query,
            include=include or oa_types.UNSET,
            pagesize=page_size,
            pagenumber=page_number,
        )
        return self._parse_documents_response(response)

    def _parse_documents_response(
        self, response: oa_types.Response
    ) -> tuple[list[dm.Document], bool]:
        self._raise_on_error(response)
        documents_response = response.parsed
        assert isinstance(
            documents_response, api_models.DocumentsListGetResponse
        )
        user_names = self._user_names_from_included(
            documents_response.included
        )
        documents = [
            self._generate_document(data, user_names)
            for data in documents_response.data or []
            if not getattr(data.meta, "errors", []) and data.attributes
        ]
        next_page = isinstance(
            documents_response.links,
            api_models.DocumentsListGetResponseLinks,
        ) and bool(documents_response.links.next_)
        return documents, next_page

    def _generate_document(
        self,
        data: t.Any,
        user_names: dict[str, str] | None = None,
    ) -> dm.Document:
        assert data.attributes
        attributes = data.attributes
        assert isinstance(data.id, str)
        home_page_content = self._handle_text_content(
            attributes.home_page_content
        )

        rendering_layouts = None
        if attributes.rendering_layouts:
            rendering_layouts = [
                dm.RenderingLayout(
                    self.unset_to_none(layout.label),
                    self.unset_to_none(layout.layouter),
                    (
                        [p.to_dict() for p in layout.properties]
                        if layout.properties
                        else None
                    ),
                    self.unset_to_none(layout.type_),
                )
                for layout in attributes.rendering_layouts
            ]

        additional_properties = attributes.additional_properties or {}
        if user_names and (
            relationships := getattr(data, "relationships", None)
        ):
            self._resolve_named_user_relationship(
                additional_properties,
                "author",
                getattr(relationships, "author", None),
                user_names,
            )
            self._resolve_named_user_relationship(
                additional_properties,
                "updated_by",
                getattr(relationships, "updated_by", None),
                user_names,
            )

        return dm.Document(
            id=data.id,
            module_folder=self.unset_to_none(attributes.module_folder),
            module_name=self.unset_to_none(attributes.module_name),
            type=self.unset_to_none(attributes.type_),
            status=self.unset_to_none(attributes.status),
            home_page_content=home_page_content,
            title=self.unset_to_none(attributes.title),
            rendering_layouts=rendering_layouts,
            outline_numbering=self.unset_to_none(
                attributes.uses_outline_numbering
            ),
            outline_numbering_prefix=(
                self.unset_to_none(attributes.outline_numbering.prefix)
                if attributes.outline_numbering
                else None
            ),
            additional_properties=additional_properties,
            structure_link_role=self.unset_to_none(
                attributes.structure_link_role
            ),
        )

    def _pre_batching_grouping(
        self, items: list[dm.Document]
    ) -> t.Generator[list[dm.Document], None, None]:
        for _, group in itertools.groupby(items, lambda x: x.module_folder):
            yield list(group)

    def _update(self, to_update: list[dm.Document]) -> None:
        assert len(to_update) == 1, "Expected only one item"
        assert to_update[0].module_folder
        assert to_update[0].module_name
        res = patch_document.sync_detailed(
            project_id=self._project_id,
            space_id=to_update[0].module_folder,
            document_name=to_update[0].module_name,
            client=self._client.client,
            body=self._prepare_patch_request(to_update[0]),
        )

        self._raise_on_error(res)

    async def _async_update(self, to_update: list[dm.Document]) -> None:
        assert len(to_update) == 1, "Expected only one item"
        assert to_update[0].module_folder
        assert to_update[0].module_name
        res = await patch_document.asyncio_detailed(
            project_id=self._project_id,
            space_id=to_update[0].module_folder,
            document_name=to_update[0].module_name,
            client=self._client.client,
            body=self._prepare_patch_request(to_update[0]),
        )

        self._raise_on_error(res)

    def _prepare_patch_request(
        self, to_update: dm.Document
    ) -> api_models.DocumentsSinglePatchRequest:
        assert to_update.module_folder is not None, "module folder must be set"
        assert to_update.module_name is not None, "module name must be set"

        if to_update.structure_link_role:
            logger.warning(
                "Changing the documents structure link role is not supported."
            )

        attrs = api_models.DocumentsSinglePatchRequestDataAttributes(
            home_page_content=(
                api_models.DocumentsSinglePatchRequestDataAttributesHomePageContent(
                    type_=api_models.DocumentsSinglePatchRequestDataAttributesHomePageContentType(
                        to_update.home_page_content.type
                    ),
                    value=to_update.home_page_content.value or "",
                )
                if to_update.home_page_content
                else oa_types.UNSET
            ),
            status=to_update.status or oa_types.UNSET,
            title=to_update.title or oa_types.UNSET,
            type_=to_update.type or oa_types.UNSET,
            rendering_layouts=(
                [
                    api_models.DocumentsSinglePatchRequestDataAttributesRenderingLayoutsItem(
                        label=layout.label or oa_types.UNSET,
                        layouter=(
                            layout.layouter.value
                            if layout.layouter is not None
                            else oa_types.UNSET
                        ),
                        type_=layout.type or oa_types.UNSET,
                        properties=(
                            [
                                api_models.DocumentsSinglePatchRequestDataAttributesRenderingLayoutsItemPropertiesItem.from_dict(
                                    p
                                )
                                for p in layout.properties.serialize()
                            ]
                            if layout.properties
                            else oa_types.UNSET
                        ),
                    )
                    for layout in to_update.rendering_layouts
                ]
                if to_update.rendering_layouts
                else oa_types.UNSET
            ),
            uses_outline_numbering=to_update.outline_numbering
            or oa_types.UNSET,
            outline_numbering=(
                api_models.DocumentsSinglePatchRequestDataAttributesOutlineNumbering(
                    prefix=to_update.outline_numbering_prefix
                )
                if to_update.outline_numbering_prefix
                else oa_types.UNSET
            ),
        )

        attrs.additional_properties.update(
            to_update.additional_properties or {}
        )

        return api_models.DocumentsSinglePatchRequest(
            data=api_models.DocumentsSinglePatchRequestData(
                api_models.DocumentsSinglePatchRequestDataType.DOCUMENTS,
                id=f"{self._project_id}/{to_update.module_folder}/{to_update.module_name}",
                attributes=attrs,
            )
        )

    def _create(self, items: list[dm.Document]) -> None:
        assert items[0].module_folder
        res = post_documents.sync_detailed(
            self._project_id,
            items[0].module_folder,
            client=self._client.client,
            body=self._prepare_document_post_request(items),
        )

        self._raise_on_error(res)

    async def _async_create(self, items: list[dm.Document]) -> None:
        assert items[0].module_folder
        res = await post_documents.asyncio_detailed(
            self._project_id,
            items[0].module_folder,
            client=self._client.client,
            body=self._prepare_document_post_request(items),
        )

        self._raise_on_error(res)

    def _prepare_document_post_request(
        self, items: list[dm.Document]
    ) -> api_models.DocumentsListPostRequest:
        # due to grouping in _split_into_batches all module folders are equal
        assert items[0].module_folder is not None, "module folder must be set"
        return api_models.DocumentsListPostRequest(
            # pylint: disable=line-too-long
            data=[
                api_models.DocumentsListPostRequestDataItem(
                    type_=api_models.DocumentsListPostRequestDataItemType.DOCUMENTS,
                    attributes=self._build_create_attributes(document),
                )
                for document in items
            ]
        )

    def _build_create_attributes(
        self, document: dm.Document
    ) -> api_models.DocumentsListPostRequestDataItemAttributes:
        attrs = api_models.DocumentsListPostRequestDataItemAttributes(
            home_page_content=(
                api_models.DocumentsListPostRequestDataItemAttributesHomePageContent(
                    type_=api_models.DocumentsListPostRequestDataItemAttributesHomePageContentType(
                        document.home_page_content.type
                    ),
                    value=document.home_page_content.value or "",
                )
                if document.home_page_content
                else oa_types.UNSET
            ),
            module_name=document.module_name or oa_types.UNSET,
            status=document.status or oa_types.UNSET,
            title=document.title or oa_types.UNSET,
            type_=document.type or oa_types.UNSET,
            rendering_layouts=(
                [
                    api_models.DocumentsListPostRequestDataItemAttributesRenderingLayoutsItem(
                        label=layout.label or oa_types.UNSET,
                        layouter=(
                            layout.layouter.value
                            if layout.layouter is not None
                            else oa_types.UNSET
                        ),
                        type_=layout.type or oa_types.UNSET,
                        properties=(
                            [
                                api_models.DocumentsListPostRequestDataItemAttributesRenderingLayoutsItemPropertiesItem.from_dict(
                                    p
                                )
                                for p in layout.properties.serialize()
                            ]
                            if layout.properties
                            else oa_types.UNSET
                        ),
                    )
                    for layout in document.rendering_layouts
                ]
                if document.rendering_layouts
                else oa_types.UNSET
            ),
            uses_outline_numbering=document.outline_numbering
            or oa_types.UNSET,
            outline_numbering=(
                api_models.DocumentsListPostRequestDataItemAttributesOutlineNumbering(
                    prefix=document.outline_numbering_prefix
                )
                if document.outline_numbering_prefix
                else oa_types.UNSET
            ),
            structure_link_role=document.structure_link_role or oa_types.UNSET,
        )
        attrs.additional_properties.update(
            document.additional_properties or {}
        )
        return attrs

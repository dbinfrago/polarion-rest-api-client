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
    patch_document,
    post_documents,
)

from . import base_classes as bc

logger = logging.getLogger(__name__)


class Documents(
    bc.SingleUpdatableItemsMixin[dm.Document],
    bc.UpdatableItemsClient[dm.Document],
):
    """A client to work with documents in Polarion."""

    def get(
        self,
        space_id: str,
        document_name: str,
        fields: dict[str, str] | None = None,
        include: str | None | oa_types.Unset = None,
        revision: str | None | oa_types.Unset = None,
    ) -> dm.Document | None:
        """Return the document with the given document_name and space_id."""
        if include is None:
            include = oa_types.UNSET

        if revision is None:
            revision = oa_types.UNSET

        if " " in space_id or " " in document_name:
            space_id = urllib.parse.quote(
                space_id, safe="/", encoding=None, errors=None
            )
            document_name = urllib.parse.quote(
                document_name, safe="/", encoding=None, errors=None
            )
        if fields is None:
            fields = self._client.default_fields.documents

        sparse_fields = self._build_sparse_fields(fields)
        response = get_document.sync_detailed(
            self._project_id,
            space_id,
            document_name,
            client=self._client.client,
            fields=sparse_fields,
            include=include,
            revision=revision,
        )

        self._raise_on_error(response)

        document_response = response.parsed

        if (
            isinstance(
                document_response, api_models.DocumentsSingleGetResponse
            )
            and (data := document_response.data)
            and not getattr(data.meta, "errors", [])
        ):
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
                additional_properties=attributes.additional_properties or {},
                structure_link_role=self.unset_to_none(
                    attributes.structure_link_role
                ),
            )

        return None

    def _split_into_batches(
        self, items: list[dm.Document]
    ) -> t.Generator[list[dm.Document], None, None]:
        for _, group in itertools.groupby(items, lambda x: x.module_folder):
            yield from super()._split_into_batches(list(group))

    def _update(self, to_update: dm.Document | list[dm.Document]) -> None:
        assert not isinstance(to_update, list), "Expected only one item"
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

        req = api_models.DocumentsSinglePatchRequest(
            data=api_models.DocumentsSinglePatchRequestData(
                api_models.DocumentsSinglePatchRequestDataType.DOCUMENTS,
                id=f"{self._project_id}/{to_update.module_folder}/{to_update.module_name}",
                attributes=attrs,
            )
        )

        res = patch_document.sync_detailed(
            project_id=self._project_id,
            space_id=to_update.module_folder,
            document_name=to_update.module_name,
            client=self._client.client,
            body=req,
        )

        self._raise_on_error(res)

    def get_multi(
        self,
        *args: t.Any,
        page_size: int = 100,
        page_number: int = 1,
        **kwargs: t.Any,
    ) -> tuple[list[dm.Document], bool]:
        """Return a list of documents - Not implemented yet."""
        raise NotImplementedError

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

    def _create(self, items: list[dm.Document]) -> None:
        # due to grouping in _split_into_batches all module folders are equal
        assert items[0].module_folder is not None, "module folder must be set"

        req = api_models.DocumentsListPostRequest(
            data=[
                api_models.DocumentsListPostRequestDataItem(
                    type_=api_models.DocumentsListPostRequestDataItemType.DOCUMENTS,
                    attributes=self._build_create_attributes(document),
                )
                for document in items
            ]
        )

        res = post_documents.sync_detailed(
            self._project_id,
            items[0].module_folder,
            client=self._client.client,
            body=req,
        )

        self._raise_on_error(res)

    def _delete(self, items: list[dm.Document]) -> None:
        raise NotImplementedError

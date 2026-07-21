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
    branch_document,
    copy_document,
    get_document,
    patch_document,
    post_documents,
)

from . import base_classes as bc

logger = logging.getLogger(__name__)


class Documents(
    bc.SingleGetClient,
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
            assert data.attributes
            attributes = data.attributes
            assert isinstance(data.id, str)
            return self._document_from_response_attributes(data.id, attributes)
        return None

    def _document_from_response_attributes(
        self,
        document_id: str | None,
        attributes: t.Any,
        module_folder: str | None = None,
        module_name: str | None = None,
    ) -> dm.Document:
        home_page_content = self._handle_text_content(
            getattr(attributes, "home_page_content", oa_types.UNSET)
        )

        rendering_layouts = None
        layouts = getattr(attributes, "rendering_layouts", oa_types.UNSET)
        if not isinstance(layouts, oa_types.Unset) and layouts:
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
                for layout in layouts
            ]

        outline_numbering = getattr(
            attributes, "outline_numbering", oa_types.UNSET
        )
        return dm.Document(
            id=document_id,
            module_folder=self.unset_to_none(
                getattr(attributes, "module_folder", oa_types.UNSET)
            )
            or module_folder,
            module_name=self.unset_to_none(
                getattr(attributes, "module_name", oa_types.UNSET)
            )
            or module_name,
            type=self.unset_to_none(
                getattr(attributes, "type_", oa_types.UNSET)
            ),
            status=self.unset_to_none(
                getattr(attributes, "status", oa_types.UNSET)
            ),
            home_page_content=home_page_content,
            title=self.unset_to_none(
                getattr(attributes, "title", oa_types.UNSET)
            ),
            rendering_layouts=rendering_layouts,
            outline_numbering=self.unset_to_none(
                getattr(attributes, "uses_outline_numbering", oa_types.UNSET)
            ),
            outline_numbering_prefix=(
                self.unset_to_none(outline_numbering.prefix)
                if outline_numbering
                else None
            ),
            structure_link_role=self.unset_to_none(
                getattr(attributes, "structure_link_role", oa_types.UNSET)
            ),
            additional_properties=attributes.additional_properties or {},
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

    def _resolve_source_and_target(
        self,
        space_id: str | dm.Document | None,
        document_name: str | None,
        target_document_name: str | None,
        document: dm.Document | None,
    ) -> tuple[str, str, str]:
        """Resolve the overloaded source/target arguments for copy/branch."""
        if document is not None:
            source_space_id = document.module_folder
            source_document_name = document.module_name
            target_doc_name = target_document_name
        elif isinstance(space_id, dm.Document):
            source_space_id = space_id.module_folder
            source_document_name = space_id.module_name
            target_doc_name = document_name
        else:
            source_space_id = space_id
            source_document_name = document_name
            target_doc_name = target_document_name

        assert source_space_id is not None, "source space_id must be set"
        assert source_document_name is not None, (
            "source document_name must be set"
        )
        assert target_doc_name is not None, "target_document_name must be set"
        return source_space_id, source_document_name, target_doc_name

    @staticmethod
    def _url_quote(value: str) -> str:
        """URL-encode a document path component."""
        return urllib.parse.quote(value, safe="/", encoding=None, errors=None)

    def _parse_post_response_to_document(
        self,
        response: oa_types.Response,
        target_space_id: str,
        target_document_name: str,
    ) -> dm.Document:
        """Parse the created document from a copy/branch post response."""
        parsed = response.parsed
        if isinstance(parsed, api_models.DocumentsSinglePostResponse):
            data = parsed.data
            if not isinstance(data, oa_types.Unset):
                document_id = self.unset_to_none(data.id)
                module_folder = target_space_id
                module_name = target_document_name

                if document_id:
                    _, _, remainder = document_id.partition("/")
                    if remainder:
                        parsed_space_id, _, parsed_document_name = (
                            remainder.partition("/")
                        )
                        module_folder = parsed_space_id or module_folder
                        module_name = parsed_document_name or module_name

                attributes = (
                    data.attributes
                    if not isinstance(data.attributes, oa_types.Unset)
                    else None
                )
                if attributes:
                    return self._document_from_response_attributes(
                        document_id,
                        attributes,
                        module_folder,
                        module_name,
                    )

                return dm.Document(
                    id=document_id,
                    module_folder=module_folder,
                    module_name=module_name,
                )

        return dm.Document(
            id=f"{self._project_id}/{target_space_id}/{target_document_name}",
            module_folder=target_space_id,
            module_name=target_document_name,
        )

    def _post_document_action(
        self,
        action_api: t.Any,
        body_cls: t.Any,
        space_id: str | dm.Document | None,
        document_name: str | None,
        target_document_name: str | None,
        target_space_id: str | None,
        revision: str | None | oa_types.Unset,
        document: dm.Document | None,
        **body_kwargs: t.Any,
    ) -> dm.Document:
        source_space_id, source_document_name, target_doc_name = (
            self._resolve_source_and_target(
                space_id, document_name, target_document_name, document
            )
        )
        response = action_api.sync_detailed(
            self._project_id,
            self._url_quote(source_space_id),
            self._url_quote(source_document_name),
            client=self._client.client,
            body=body_cls(
                target_document_name=target_doc_name,
                target_space_id=target_space_id or oa_types.UNSET,
                **body_kwargs,
            ),
            revision=self.none_to_unset(revision),
        )

        self._raise_on_error(response)
        return self._parse_post_response_to_document(
            response, target_space_id or source_space_id, target_doc_name
        )

    async def _async_post_document_action(
        self,
        action_api: t.Any,
        body_cls: t.Any,
        space_id: str | dm.Document | None,
        document_name: str | None,
        target_document_name: str | None,
        target_space_id: str | None,
        revision: str | None | oa_types.Unset,
        document: dm.Document | None,
        **body_kwargs: t.Any,
    ) -> dm.Document:
        source_space_id, source_document_name, target_doc_name = (
            self._resolve_source_and_target(
                space_id, document_name, target_document_name, document
            )
        )
        response = await action_api.asyncio_detailed(
            self._project_id,
            self._url_quote(source_space_id),
            self._url_quote(source_document_name),
            client=self._client.client,
            body=body_cls(
                target_document_name=target_doc_name,
                target_space_id=target_space_id or oa_types.UNSET,
                **body_kwargs,
            ),
            revision=self.none_to_unset(revision),
        )

        self._raise_on_error(response)
        return self._parse_post_response_to_document(
            response, target_space_id or source_space_id, target_doc_name
        )

    @t.overload
    def copy(
        self,
        space_id: str,
        document_name: str,
        target_document_name: str,
        target_space_id: str | None = None,
        target_project_id: str | None = None,
        link_original_items_with_role: str | None = None,
        remove_outgoing_links: bool | None = None,
        revision: str | None | oa_types.Unset = None,
    ) -> dm.Document: ...

    @t.overload
    def copy(
        self,
        document: dm.Document,
        target_document_name: str,
        target_space_id: str | None = None,
        target_project_id: str | None = None,
        link_original_items_with_role: str | None = None,
        remove_outgoing_links: bool | None = None,
        revision: str | None | oa_types.Unset = None,
    ) -> dm.Document: ...

    def copy(  # type: ignore[misc]
        self,
        space_id: str | dm.Document | None = None,
        document_name: str | None = None,
        target_document_name: str | None = None,
        target_space_id: str | None = None,
        target_project_id: str | None = None,
        link_original_items_with_role: str | None = None,
        remove_outgoing_links: bool | None = None,
        revision: str | None | oa_types.Unset = None,
        document: dm.Document | None = None,
    ) -> dm.Document:
        """Copy a document in Polarion.

        Can be called in two ways:

        1. ``copy(space_id, document_name, target_document_name, ...)``
        2. ``copy(document, target_document_name, ...)``

        Parameters
        ----------
        space_id:
            Source space ID, or a Document instance.
        document_name:
            Source document name (form 1) or target name (form 2).
        target_document_name:
            Name for the new copied document (form 1 or ``document=`` form).
        target_space_id:
            Destination space; defaults to source space.
        target_project_id:
            Destination project; defaults to current project.
        link_original_items_with_role:
            Role to link original items with the copy (e.g. "duplicates").
        remove_outgoing_links:
            Whether to remove outgoing links from the copy.
        revision:
            Copy from a specific revision.
        document:
            Keyword alternative for the source Document.

        Returns
        -------
            The newly created Document.
        """
        return self._post_document_action(
            copy_document,
            api_models.CopyDocumentRequestBody,
            space_id,
            document_name,
            target_document_name,
            target_space_id,
            revision,
            document,
            target_project_id=target_project_id or oa_types.UNSET,
            link_original_items_with_role=(
                link_original_items_with_role or oa_types.UNSET
            ),
            remove_outgoing_links=(
                remove_outgoing_links
                if remove_outgoing_links is not None
                else oa_types.UNSET
            ),
        )

    @t.overload
    async def async_copy(
        self,
        space_id: str,
        document_name: str,
        target_document_name: str,
        target_space_id: str | None = None,
        target_project_id: str | None = None,
        link_original_items_with_role: str | None = None,
        remove_outgoing_links: bool | None = None,
        revision: str | None | oa_types.Unset = None,
    ) -> dm.Document: ...

    @t.overload
    async def async_copy(
        self,
        document: dm.Document,
        target_document_name: str,
        target_space_id: str | None = None,
        target_project_id: str | None = None,
        link_original_items_with_role: str | None = None,
        remove_outgoing_links: bool | None = None,
        revision: str | None | oa_types.Unset = None,
    ) -> dm.Document: ...

    async def async_copy(  # type: ignore[misc]
        self,
        space_id: str | dm.Document | None = None,
        document_name: str | None = None,
        target_document_name: str | None = None,
        target_space_id: str | None = None,
        target_project_id: str | None = None,
        link_original_items_with_role: str | None = None,
        remove_outgoing_links: bool | None = None,
        revision: str | None | oa_types.Unset = None,
        document: dm.Document | None = None,
    ) -> dm.Document:
        """Copy a document in Polarion asynchronously.

        Async variant of :meth:`copy`; accepts the same arguments.
        """
        return await self._async_post_document_action(
            copy_document,
            api_models.CopyDocumentRequestBody,
            space_id,
            document_name,
            target_document_name,
            target_space_id,
            revision,
            document,
            target_project_id=target_project_id or oa_types.UNSET,
            link_original_items_with_role=(
                link_original_items_with_role or oa_types.UNSET
            ),
            remove_outgoing_links=(
                remove_outgoing_links
                if remove_outgoing_links is not None
                else oa_types.UNSET
            ),
        )

    @t.overload
    def branch(
        self,
        space_id: str,
        document_name: str,
        target_document_name: str,
        target_space_id: str | None = None,
        target_project_id: str | None = None,
        copy_workflow_status_and_signatures: bool | None = None,
        query: str | None = None,
        revision: str | None | oa_types.Unset = None,
    ) -> dm.Document: ...

    @t.overload
    def branch(
        self,
        document: dm.Document,
        target_document_name: str,
        target_space_id: str | None = None,
        target_project_id: str | None = None,
        copy_workflow_status_and_signatures: bool | None = None,
        query: str | None = None,
        revision: str | None | oa_types.Unset = None,
    ) -> dm.Document: ...

    def branch(  # type: ignore[misc]
        self,
        space_id: str | dm.Document | None = None,
        document_name: str | None = None,
        target_document_name: str | None = None,
        target_space_id: str | None = None,
        target_project_id: str | None = None,
        copy_workflow_status_and_signatures: bool | None = None,
        query: str | None = None,
        revision: str | None | oa_types.Unset = None,
        document: dm.Document | None = None,
    ) -> dm.Document:
        """Branch a document in Polarion.

        Can be called in two ways:

        1. ``branch(space_id, document_name, target_document_name, ...)``
        2. ``branch(document, target_document_name, ...)``

        Parameters
        ----------
        space_id:
            Source space ID, or a Document instance.
        document_name:
            Source document name (form 1) or target name (form 2).
        target_document_name:
            Name for the new branched document (form 1 or ``document=`` form).
        target_space_id:
            Destination space; defaults to source space.
        target_project_id:
            Destination project; defaults to current project.
        copy_workflow_status_and_signatures:
            Copy workflow status and signatures to the branched document.
        query:
            Optional filtering query (e.g. "status:open").
        revision:
            Branch from a specific revision.
        document:
            Keyword alternative for the source Document.

        Returns
        -------
            The newly created Document.
        """
        return self._post_document_action(
            branch_document,
            api_models.BranchDocumentRequestBody,
            space_id,
            document_name,
            target_document_name,
            target_space_id,
            revision,
            document,
            target_project_id=target_project_id or oa_types.UNSET,
            copy_workflow_status_and_signatures=(
                copy_workflow_status_and_signatures
                if copy_workflow_status_and_signatures is not None
                else oa_types.UNSET
            ),
            query=query or oa_types.UNSET,
        )

    @t.overload
    async def async_branch(
        self,
        space_id: str,
        document_name: str,
        target_document_name: str,
        target_space_id: str | None = None,
        target_project_id: str | None = None,
        copy_workflow_status_and_signatures: bool | None = None,
        query: str | None = None,
        revision: str | None | oa_types.Unset = None,
    ) -> dm.Document: ...

    @t.overload
    async def async_branch(
        self,
        document: dm.Document,
        target_document_name: str,
        target_space_id: str | None = None,
        target_project_id: str | None = None,
        copy_workflow_status_and_signatures: bool | None = None,
        query: str | None = None,
        revision: str | None | oa_types.Unset = None,
    ) -> dm.Document: ...

    async def async_branch(  # type: ignore[misc]
        self,
        space_id: str | dm.Document | None = None,
        document_name: str | None = None,
        target_document_name: str | None = None,
        target_space_id: str | None = None,
        target_project_id: str | None = None,
        copy_workflow_status_and_signatures: bool | None = None,
        query: str | None = None,
        revision: str | None | oa_types.Unset = None,
        document: dm.Document | None = None,
    ) -> dm.Document:
        """Branch a document in Polarion asynchronously.

        Async variant of :meth:`branch`; accepts the same arguments.
        """
        return await self._async_post_document_action(
            branch_document,
            api_models.BranchDocumentRequestBody,
            space_id,
            document_name,
            target_document_name,
            target_space_id,
            revision,
            document,
            target_project_id=target_project_id or oa_types.UNSET,
            copy_workflow_status_and_signatures=(
                copy_workflow_status_and_signatures
                if copy_workflow_status_and_signatures is not None
                else oa_types.UNSET
            ),
            query=query or oa_types.UNSET,
        )

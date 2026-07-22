# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
"""Clients to handle work item and document comments."""

import typing as t

from polarion_rest_api_client import data_models as dm
from polarion_rest_api_client.open_api_client import models as api_models
from polarion_rest_api_client.open_api_client import types as oa_types
from polarion_rest_api_client.open_api_client.api.document_comments import (
    get_document_comments,
    patch_document_comment,
    post_document_comments,
)
from polarion_rest_api_client.open_api_client.api.work_item_comments import (
    get_comments,
    patch_comment,
    post_comments,
)

from . import base_classes as bc


class _CommentsMixin(bc.BaseClient[dm.Comment]):
    """Shared comment parsing for work item and document comments."""

    def _generate_comment(
        self,
        data: t.Any,
        user_names: dict[str, str] | None = None,
    ) -> dm.Comment:
        """Build a :class:`dm.Comment` from a JSON:API comment resource."""
        attributes = data.attributes
        text = None
        if attributes and attributes.text:
            text = dm.TextContent(
                type=(
                    str(attributes.text.type_)
                    if attributes.text.type_
                    else None
                ),
                value=attributes.text.value or None,
            )

        comment = dm.Comment(
            id=data.id.split("/")[-1] if data.id else None,
            title=self.unset_to_none(getattr(attributes, "title", oa_types.UNSET))
            if attributes
            else None,
            resolved=self.unset_to_none(attributes.resolved)
            if attributes
            else None,
            text=text,
            created=self.unset_to_none(attributes.created) if attributes else None,
        )

        relationships = getattr(data, "relationships", None)
        if relationships:
            if relationships.author:
                self._resolve_named_user_relationship(
                    comment.additional_attributes,
                    "author",
                    relationships.author,
                    user_names or {},
                )
                comment.author = comment.additional_attributes.get("author")
            if (
                relationships.parent_comment
                and relationships.parent_comment.data
                and relationships.parent_comment.data.id
            ):
                comment.parent_comment = relationships.parent_comment.data.id
            if relationships.child_comments and relationships.child_comments.data:
                comment.child_comments = [
                    child.id
                    for child in relationships.child_comments.data
                    if child.id
                ]

        return comment


class WorkItemComments(
    _CommentsMixin,
    bc.MultiGetClient[dm.Comment],
):
    """Client to handle comments of a work item."""

    def get_multi(  # type: ignore[override]
        self,
        work_item_id: str,
        *,
        page_size: int = 100,
        page_number: int = 1,
        fields: dict[str, str] | None = None,
        include: str | None = None,
    ) -> tuple[list[dm.Comment], bool]:
        """Return the comments of a work item on a defined page."""
        response = get_comments.sync_detailed(
            self._project_id,
            work_item_id,
            client=self._client.client,
            fields=self._build_sparse_fields(fields) if fields else oa_types.UNSET,
            include=include or oa_types.UNSET,
            pagesize=page_size,
            pagenumber=page_number,
        )
        self._raise_on_error(response)
        return self._parse_get_response(response.parsed)

    async def async_get_multi(  # type: ignore[override]
        self,
        work_item_id: str,
        *,
        page_size: int = 100,
        page_number: int = 1,
        fields: dict[str, str] | None = None,
        include: str | None = None,
    ) -> tuple[list[dm.Comment], bool]:
        """Return the comments of a work item on a defined page."""
        response = await get_comments.asyncio_detailed(
            self._project_id,
            work_item_id,
            client=self._client.client,
            fields=self._build_sparse_fields(fields) if fields else oa_types.UNSET,
            include=include or oa_types.UNSET,
            pagesize=page_size,
            pagenumber=page_number,
        )
        self._raise_on_error(response)
        return self._parse_get_response(response.parsed)

    def _parse_get_response(
        self, parsed: t.Any
    ) -> tuple[list[dm.Comment], bool]:
        if not isinstance(
            parsed, api_models.WorkitemCommentsListGetResponse
        ) or isinstance(parsed.data, oa_types.Unset):
            return [], False
        user_names = self._user_names_from_included(parsed.included)
        comments = [
            self._generate_comment(item, user_names)
            for item in parsed.data
            if not getattr(item.meta, "errors", []) and item.attributes
        ]
        next_page = isinstance(
            parsed.links, api_models.WorkitemCommentsListGetResponseLinks
        ) and bool(parsed.links.next_)
        return comments, next_page

    def create(
        self, work_item_id: str, comments: dm.Comment | list[dm.Comment]
    ) -> None:
        """Create one or multiple comments on a work item.

        The created comments' ids are written back onto the passed objects.
        """
        if not isinstance(comments, list):
            comments = [comments]
        response = post_comments.sync_detailed(
            self._project_id,
            work_item_id,
            client=self._client.client,
            body=self._build_post_request(comments),
        )
        self._raise_on_error(response)
        self._process_post_response(response, comments)

    async def async_create(
        self, work_item_id: str, comments: dm.Comment | list[dm.Comment]
    ) -> None:
        """Create one or multiple comments on a work item."""
        if not isinstance(comments, list):
            comments = [comments]
        response = await post_comments.asyncio_detailed(
            self._project_id,
            work_item_id,
            client=self._client.client,
            body=self._build_post_request(comments),
        )
        self._raise_on_error(response)
        self._process_post_response(response, comments)

    def _build_post_request(
        self, comments: list[dm.Comment]
    ) -> api_models.WorkitemCommentsListPostRequest:
        return api_models.WorkitemCommentsListPostRequest(
            data=[
                api_models.WorkitemCommentsListPostRequestDataItem.from_dict(
                    _comment_post_dict(comment, "workitem_comments")
                )
                for comment in comments
            ]
        )

    def _process_post_response(
        self, response: oa_types.Response, comments: list[dm.Comment]
    ) -> None:
        assert isinstance(
            response.parsed, api_models.WorkitemCommentsListPostResponse
        )
        assert response.parsed.data
        for index, comment_res in enumerate(response.parsed.data):
            assert comment_res.id
            comments[index].id = comment_res.id.split("/")[-1]

    def set_resolved(
        self, work_item_id: str, comment_id: str, resolved: bool
    ) -> None:
        """Resolve or unresolve a single work item comment."""
        response = patch_comment.sync_detailed(
            self._project_id,
            work_item_id,
            comment_id,
            client=self._client.client,
            body=_resolve_patch_request(
                self._project_id, work_item_id, comment_id, resolved
            ),
        )
        self._raise_on_error(response)

    async def async_set_resolved(
        self, work_item_id: str, comment_id: str, resolved: bool
    ) -> None:
        """Resolve or unresolve a single work item comment."""
        response = await patch_comment.asyncio_detailed(
            self._project_id,
            work_item_id,
            comment_id,
            client=self._client.client,
            body=_resolve_patch_request(
                self._project_id, work_item_id, comment_id, resolved
            ),
        )
        self._raise_on_error(response)


class DocumentComments(
    _CommentsMixin,
    bc.MultiGetClient[dm.Comment],
):
    """Client to handle comments of a document."""

    def get_multi(  # type: ignore[override]
        self,
        space_id: str,
        document_name: str,
        *,
        page_size: int = 100,
        page_number: int = 1,
        fields: dict[str, str] | None = None,
        include: str | None = None,
    ) -> tuple[list[dm.Comment], bool]:
        """Return the comments of a document on a defined page."""
        response = get_document_comments.sync_detailed(
            self._project_id,
            space_id,
            document_name,
            client=self._client.client,
            fields=self._build_sparse_fields(fields) if fields else oa_types.UNSET,
            include=include or oa_types.UNSET,
            pagesize=page_size,
            pagenumber=page_number,
        )
        self._raise_on_error(response)
        return self._parse_get_response(response.parsed)

    async def async_get_multi(  # type: ignore[override]
        self,
        space_id: str,
        document_name: str,
        *,
        page_size: int = 100,
        page_number: int = 1,
        fields: dict[str, str] | None = None,
        include: str | None = None,
    ) -> tuple[list[dm.Comment], bool]:
        """Return the comments of a document on a defined page."""
        response = await get_document_comments.asyncio_detailed(
            self._project_id,
            space_id,
            document_name,
            client=self._client.client,
            fields=self._build_sparse_fields(fields) if fields else oa_types.UNSET,
            include=include or oa_types.UNSET,
            pagesize=page_size,
            pagenumber=page_number,
        )
        self._raise_on_error(response)
        return self._parse_get_response(response.parsed)

    def _parse_get_response(
        self, parsed: t.Any
    ) -> tuple[list[dm.Comment], bool]:
        if not isinstance(
            parsed, api_models.DocumentCommentsListGetResponse
        ) or isinstance(parsed.data, oa_types.Unset):
            return [], False
        user_names = self._user_names_from_included(parsed.included)
        comments = [
            self._generate_comment(item, user_names)
            for item in parsed.data
            if not getattr(item.meta, "errors", []) and item.attributes
        ]
        next_page = isinstance(
            parsed.links, api_models.DocumentCommentsListGetResponseLinks
        ) and bool(parsed.links.next_)
        return comments, next_page

    def create(
        self,
        space_id: str,
        document_name: str,
        comments: dm.Comment | list[dm.Comment],
    ) -> None:
        """Create one or multiple comments on a document."""
        if not isinstance(comments, list):
            comments = [comments]
        response = post_document_comments.sync_detailed(
            self._project_id,
            space_id,
            document_name,
            client=self._client.client,
            body=self._build_post_request(comments),
        )
        self._raise_on_error(response)
        self._process_post_response(response, comments)

    async def async_create(
        self,
        space_id: str,
        document_name: str,
        comments: dm.Comment | list[dm.Comment],
    ) -> None:
        """Create one or multiple comments on a document."""
        if not isinstance(comments, list):
            comments = [comments]
        response = await post_document_comments.asyncio_detailed(
            self._project_id,
            space_id,
            document_name,
            client=self._client.client,
            body=self._build_post_request(comments),
        )
        self._raise_on_error(response)
        self._process_post_response(response, comments)

    def _build_post_request(
        self, comments: list[dm.Comment]
    ) -> api_models.DocumentCommentsListPostRequest:
        return api_models.DocumentCommentsListPostRequest(
            data=[
                api_models.DocumentCommentsListPostRequestDataItem.from_dict(
                    _comment_post_dict(comment, "document_comments")
                )
                for comment in comments
            ]
        )

    def _process_post_response(
        self, response: oa_types.Response, comments: list[dm.Comment]
    ) -> None:
        assert isinstance(
            response.parsed, api_models.DocumentCommentsListPostResponse
        )
        assert response.parsed.data
        for index, comment_res in enumerate(response.parsed.data):
            assert comment_res.id
            comments[index].id = comment_res.id.split("/")[-1]

    def set_resolved(
        self,
        space_id: str,
        document_name: str,
        comment_id: str,
        resolved: bool,
    ) -> None:
        """Resolve or unresolve a single document comment."""
        response = patch_document_comment.sync_detailed(
            self._project_id,
            space_id,
            document_name,
            comment_id,
            client=self._client.client,
            body=_resolve_patch_request_doc(comment_id, resolved),
        )
        self._raise_on_error(response)

    async def async_set_resolved(
        self,
        space_id: str,
        document_name: str,
        comment_id: str,
        resolved: bool,
    ) -> None:
        """Resolve or unresolve a single document comment."""
        response = await patch_document_comment.asyncio_detailed(
            self._project_id,
            space_id,
            document_name,
            comment_id,
            client=self._client.client,
            body=_resolve_patch_request_doc(comment_id, resolved),
        )
        self._raise_on_error(response)


def _comment_post_dict(
    comment: dm.Comment, resource_type: str
) -> dict[str, t.Any]:
    """Build a JSON:API create resource dict for a comment.

    Uses a dict + ``from_dict`` (rather than the verbose typed builders) so
    the text/type enum wrapping stays in one place.
    """
    attributes: dict[str, t.Any] = {}
    if comment.title is not None:
        attributes["title"] = comment.title
    if comment.resolved is not None:
        attributes["resolved"] = comment.resolved
    if comment.text is not None:
        attributes["text"] = {
            "type": comment.text.type or "text/plain",
            "value": comment.text.value or "",
        }

    data: dict[str, t.Any] = {"type": resource_type, "attributes": attributes}
    if comment.parent_comment:
        data["relationships"] = {
            "parentComment": {
                "data": {"type": resource_type, "id": comment.parent_comment}
            }
        }
    return data


def _resolve_patch_request(
    project_id: str, work_item_id: str, comment_id: str, resolved: bool
) -> api_models.WorkitemCommentsSinglePatchRequest:
    return api_models.WorkitemCommentsSinglePatchRequest.from_dict(
        {
            "data": {
                "type": "workitem_comments",
                "id": f"{project_id}/{work_item_id}/{comment_id}",
                "attributes": {"resolved": resolved},
            }
        }
    )


def _resolve_patch_request_doc(
    comment_id: str, resolved: bool
) -> api_models.DocumentCommentsSinglePatchRequest:
    return api_models.DocumentCommentsSinglePatchRequest.from_dict(
        {
            "data": {
                "type": "document_comments",
                "id": comment_id,
                "attributes": {"resolved": resolved},
            }
        }
    )

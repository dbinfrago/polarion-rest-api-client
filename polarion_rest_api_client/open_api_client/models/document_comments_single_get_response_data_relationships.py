# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_comments_single_get_response_data_relationships_author import (
        DocumentCommentsSingleGetResponseDataRelationshipsAuthor,
    )
    from ..models.document_comments_single_get_response_data_relationships_child_comments import (
        DocumentCommentsSingleGetResponseDataRelationshipsChildComments,
    )
    from ..models.document_comments_single_get_response_data_relationships_parent_comment import (
        DocumentCommentsSingleGetResponseDataRelationshipsParentComment,
    )
    from ..models.document_comments_single_get_response_data_relationships_project import (
        DocumentCommentsSingleGetResponseDataRelationshipsProject,
    )


T = TypeVar("T", bound="DocumentCommentsSingleGetResponseDataRelationships")


@_attrs_define
class DocumentCommentsSingleGetResponseDataRelationships:
    """
    Attributes:
        author (DocumentCommentsSingleGetResponseDataRelationshipsAuthor | Unset):
        child_comments (DocumentCommentsSingleGetResponseDataRelationshipsChildComments | Unset):
        parent_comment (DocumentCommentsSingleGetResponseDataRelationshipsParentComment | Unset):
        project (DocumentCommentsSingleGetResponseDataRelationshipsProject | Unset):
    """

    author: (
        DocumentCommentsSingleGetResponseDataRelationshipsAuthor | Unset
    ) = UNSET
    child_comments: (
        DocumentCommentsSingleGetResponseDataRelationshipsChildComments | Unset
    ) = UNSET
    parent_comment: (
        DocumentCommentsSingleGetResponseDataRelationshipsParentComment | Unset
    ) = UNSET
    project: (
        DocumentCommentsSingleGetResponseDataRelationshipsProject | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        author: dict[str, Any] | Unset = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        child_comments: dict[str, Any] | Unset = UNSET
        if not isinstance(self.child_comments, Unset):
            child_comments = self.child_comments.to_dict()

        parent_comment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parent_comment, Unset):
            parent_comment = self.parent_comment.to_dict()

        project: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if author is not UNSET:
            field_dict["author"] = author
        if child_comments is not UNSET:
            field_dict["childComments"] = child_comments
        if parent_comment is not UNSET:
            field_dict["parentComment"] = parent_comment
        if project is not UNSET:
            field_dict["project"] = project

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.document_comments_single_get_response_data_relationships_author import (
            DocumentCommentsSingleGetResponseDataRelationshipsAuthor,
        )
        from ..models.document_comments_single_get_response_data_relationships_child_comments import (
            DocumentCommentsSingleGetResponseDataRelationshipsChildComments,
        )
        from ..models.document_comments_single_get_response_data_relationships_parent_comment import (
            DocumentCommentsSingleGetResponseDataRelationshipsParentComment,
        )
        from ..models.document_comments_single_get_response_data_relationships_project import (
            DocumentCommentsSingleGetResponseDataRelationshipsProject,
        )

        d = dict(src_dict)
        _author = d.pop("author", UNSET)
        author: (
            DocumentCommentsSingleGetResponseDataRelationshipsAuthor | Unset
        )
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = DocumentCommentsSingleGetResponseDataRelationshipsAuthor.from_dict(
                _author
            )

        _child_comments = d.pop("childComments", UNSET)
        child_comments: (
            DocumentCommentsSingleGetResponseDataRelationshipsChildComments
            | Unset
        )
        if isinstance(_child_comments, Unset):
            child_comments = UNSET
        else:
            child_comments = DocumentCommentsSingleGetResponseDataRelationshipsChildComments.from_dict(
                _child_comments
            )

        _parent_comment = d.pop("parentComment", UNSET)
        parent_comment: (
            DocumentCommentsSingleGetResponseDataRelationshipsParentComment
            | Unset
        )
        if isinstance(_parent_comment, Unset):
            parent_comment = UNSET
        else:
            parent_comment = DocumentCommentsSingleGetResponseDataRelationshipsParentComment.from_dict(
                _parent_comment
            )

        _project = d.pop("project", UNSET)
        project: (
            DocumentCommentsSingleGetResponseDataRelationshipsProject | Unset
        )
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = DocumentCommentsSingleGetResponseDataRelationshipsProject.from_dict(
                _project
            )

        document_comments_single_get_response_data_relationships_obj = cls(
            author=author,
            child_comments=child_comments,
            parent_comment=parent_comment,
            project=project,
        )

        document_comments_single_get_response_data_relationships_obj.additional_properties = d
        return document_comments_single_get_response_data_relationships_obj

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

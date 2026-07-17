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
    from ..models.page_comments_list_post_request_data_item_relationships_author import (
        PageCommentsListPostRequestDataItemRelationshipsAuthor,
    )
    from ..models.page_comments_list_post_request_data_item_relationships_parent_comment import (
        PageCommentsListPostRequestDataItemRelationshipsParentComment,
    )


T = TypeVar("T", bound="PageCommentsListPostRequestDataItemRelationships")


@_attrs_define
class PageCommentsListPostRequestDataItemRelationships:
    """
    Attributes:
        author (PageCommentsListPostRequestDataItemRelationshipsAuthor | Unset):
        parent_comment (PageCommentsListPostRequestDataItemRelationshipsParentComment | Unset):
    """

    author: PageCommentsListPostRequestDataItemRelationshipsAuthor | Unset = (
        UNSET
    )
    parent_comment: (
        PageCommentsListPostRequestDataItemRelationshipsParentComment | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        author: dict[str, Any] | Unset = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        parent_comment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parent_comment, Unset):
            parent_comment = self.parent_comment.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if author is not UNSET:
            field_dict["author"] = author
        if parent_comment is not UNSET:
            field_dict["parentComment"] = parent_comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.page_comments_list_post_request_data_item_relationships_author import (
            PageCommentsListPostRequestDataItemRelationshipsAuthor,
        )
        from ..models.page_comments_list_post_request_data_item_relationships_parent_comment import (
            PageCommentsListPostRequestDataItemRelationshipsParentComment,
        )

        d = dict(src_dict)
        _author = d.pop("author", UNSET)
        author: PageCommentsListPostRequestDataItemRelationshipsAuthor | Unset
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = PageCommentsListPostRequestDataItemRelationshipsAuthor.from_dict(
                _author
            )

        _parent_comment = d.pop("parentComment", UNSET)
        parent_comment: (
            PageCommentsListPostRequestDataItemRelationshipsParentComment
            | Unset
        )
        if isinstance(_parent_comment, Unset):
            parent_comment = UNSET
        else:
            parent_comment = PageCommentsListPostRequestDataItemRelationshipsParentComment.from_dict(
                _parent_comment
            )

        page_comments_list_post_request_data_item_relationships_obj = cls(
            author=author,
            parent_comment=parent_comment,
        )

        page_comments_list_post_request_data_item_relationships_obj.additional_properties = d
        return page_comments_list_post_request_data_item_relationships_obj

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

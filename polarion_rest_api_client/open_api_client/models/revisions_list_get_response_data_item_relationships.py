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
    from ..models.revisions_list_get_response_data_item_relationships_author import (
        RevisionsListGetResponseDataItemRelationshipsAuthor,
    )


T = TypeVar("T", bound="RevisionsListGetResponseDataItemRelationships")


@_attrs_define
class RevisionsListGetResponseDataItemRelationships:
    """
    Attributes:
        author (RevisionsListGetResponseDataItemRelationshipsAuthor | Unset):
    """

    author: RevisionsListGetResponseDataItemRelationshipsAuthor | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        author: dict[str, Any] | Unset = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if author is not UNSET:
            field_dict["author"] = author

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.revisions_list_get_response_data_item_relationships_author import (
            RevisionsListGetResponseDataItemRelationshipsAuthor,
        )

        d = dict(src_dict)
        _author = d.pop("author", UNSET)
        author: RevisionsListGetResponseDataItemRelationshipsAuthor | Unset
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = (
                RevisionsListGetResponseDataItemRelationshipsAuthor.from_dict(
                    _author
                )
            )

        revisions_list_get_response_data_item_relationships_obj = cls(
            author=author,
        )

        revisions_list_get_response_data_item_relationships_obj.additional_properties = d
        return revisions_list_get_response_data_item_relationships_obj

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

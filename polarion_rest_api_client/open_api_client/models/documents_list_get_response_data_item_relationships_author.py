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
    from ..models.documents_list_get_response_data_item_relationships_author_data import (
        DocumentsListGetResponseDataItemRelationshipsAuthorData,
    )


T = TypeVar("T", bound="DocumentsListGetResponseDataItemRelationshipsAuthor")


@_attrs_define
class DocumentsListGetResponseDataItemRelationshipsAuthor:
    """
    Attributes:
        data (DocumentsListGetResponseDataItemRelationshipsAuthorData | Unset):
    """

    data: DocumentsListGetResponseDataItemRelationshipsAuthorData | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.documents_list_get_response_data_item_relationships_author_data import (
            DocumentsListGetResponseDataItemRelationshipsAuthorData,
        )

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: DocumentsListGetResponseDataItemRelationshipsAuthorData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = DocumentsListGetResponseDataItemRelationshipsAuthorData.from_dict(
                _data
            )

        documents_list_get_response_data_item_relationships_author_obj = cls(
            data=data,
        )

        documents_list_get_response_data_item_relationships_author_obj.additional_properties = d
        return documents_list_get_response_data_item_relationships_author_obj

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

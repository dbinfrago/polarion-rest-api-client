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

from ..models.document_parts_list_post_response_data_item_type import (
    DocumentPartsListPostResponseDataItemType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_parts_list_post_response_data_item_links import (
        DocumentPartsListPostResponseDataItemLinks,
    )


T = TypeVar("T", bound="DocumentPartsListPostResponseDataItem")


@_attrs_define
class DocumentPartsListPostResponseDataItem:
    """
    Attributes:
        type_ (DocumentPartsListPostResponseDataItemType | Unset):
        id (str | Unset):  Example: MyProjectId/MySpaceId/MyDocumentId/workitem_MyWorkItemId.
        links (DocumentPartsListPostResponseDataItemLinks | Unset):
    """

    type_: DocumentPartsListPostResponseDataItemType | Unset = UNSET
    id: str | Unset = UNSET
    links: DocumentPartsListPostResponseDataItemLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        id = self.id

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if id is not UNSET:
            field_dict["id"] = id
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.document_parts_list_post_response_data_item_links import (
            DocumentPartsListPostResponseDataItemLinks,
        )

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: DocumentPartsListPostResponseDataItemType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DocumentPartsListPostResponseDataItemType(_type_)

        id = d.pop("id", UNSET)

        _links = d.pop("links", UNSET)
        links: DocumentPartsListPostResponseDataItemLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = DocumentPartsListPostResponseDataItemLinks.from_dict(
                _links
            )

        document_parts_list_post_response_data_item_obj = cls(
            type_=type_,
            id=id,
            links=links,
        )

        document_parts_list_post_response_data_item_obj.additional_properties = d
        return document_parts_list_post_response_data_item_obj

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

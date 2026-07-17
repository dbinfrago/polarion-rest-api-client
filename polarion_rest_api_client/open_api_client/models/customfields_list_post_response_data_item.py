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

from ..models.customfields_list_post_response_data_item_type import (
    CustomfieldsListPostResponseDataItemType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.customfields_list_post_response_data_item_links import (
        CustomfieldsListPostResponseDataItemLinks,
    )


T = TypeVar("T", bound="CustomfieldsListPostResponseDataItem")


@_attrs_define
class CustomfieldsListPostResponseDataItem:
    """
    Attributes:
        type_ (CustomfieldsListPostResponseDataItemType | Unset):
        id (str | Unset):  Example: MyProjectId/workitems/epic.
        links (CustomfieldsListPostResponseDataItemLinks | Unset):
    """

    type_: CustomfieldsListPostResponseDataItemType | Unset = UNSET
    id: str | Unset = UNSET
    links: CustomfieldsListPostResponseDataItemLinks | Unset = UNSET
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
        from ..models.customfields_list_post_response_data_item_links import (
            CustomfieldsListPostResponseDataItemLinks,
        )

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: CustomfieldsListPostResponseDataItemType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CustomfieldsListPostResponseDataItemType(_type_)

        id = d.pop("id", UNSET)

        _links = d.pop("links", UNSET)
        links: CustomfieldsListPostResponseDataItemLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = CustomfieldsListPostResponseDataItemLinks.from_dict(_links)

        customfields_list_post_response_data_item_obj = cls(
            type_=type_,
            id=id,
            links=links,
        )

        customfields_list_post_response_data_item_obj.additional_properties = d
        return customfields_list_post_response_data_item_obj

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

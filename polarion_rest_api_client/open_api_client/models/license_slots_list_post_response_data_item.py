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

from ..models.license_slots_list_post_response_data_item_type import (
    LicenseSlotsListPostResponseDataItemType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.license_slots_list_post_response_data_item_links import (
        LicenseSlotsListPostResponseDataItemLinks,
    )


T = TypeVar("T", bound="LicenseSlotsListPostResponseDataItem")


@_attrs_define
class LicenseSlotsListPostResponseDataItem:
    """
    Attributes:
        type_ (LicenseSlotsListPostResponseDataItemType | Unset):
        id (str | Unset):  Example: LicenseType/ModelType/GroupId.
        links (LicenseSlotsListPostResponseDataItemLinks | Unset):
    """

    type_: LicenseSlotsListPostResponseDataItemType | Unset = UNSET
    id: str | Unset = UNSET
    links: LicenseSlotsListPostResponseDataItemLinks | Unset = UNSET
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
        from ..models.license_slots_list_post_response_data_item_links import (
            LicenseSlotsListPostResponseDataItemLinks,
        )

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: LicenseSlotsListPostResponseDataItemType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = LicenseSlotsListPostResponseDataItemType(_type_)

        id = d.pop("id", UNSET)

        _links = d.pop("links", UNSET)
        links: LicenseSlotsListPostResponseDataItemLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = LicenseSlotsListPostResponseDataItemLinks.from_dict(_links)

        license_slots_list_post_response_data_item_obj = cls(
            type_=type_,
            id=id,
            links=links,
        )

        license_slots_list_post_response_data_item_obj.additional_properties = d
        return license_slots_list_post_response_data_item_obj

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

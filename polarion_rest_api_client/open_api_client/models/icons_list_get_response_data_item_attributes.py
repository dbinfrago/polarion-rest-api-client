# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IconsListGetResponseDataItemAttributes")


@_attrs_define
class IconsListGetResponseDataItemAttributes:
    """
    Attributes:
        icon_url (str | Unset):  Example: pathexample.
        id (str | Unset):  Example: pathexample.
        path (str | Unset):  Example: pathexample.
    """

    icon_url: str | Unset = UNSET
    id: str | Unset = UNSET
    path: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        icon_url = self.icon_url

        id = self.id

        path = self.path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if icon_url is not UNSET:
            field_dict["iconUrl"] = icon_url
        if id is not UNSET:
            field_dict["id"] = id
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        icon_url = d.pop("iconUrl", UNSET)

        id = d.pop("id", UNSET)

        path = d.pop("path", UNSET)

        icons_list_get_response_data_item_attributes_obj = cls(
            icon_url=icon_url,
            id=id,
            path=path,
        )

        icons_list_get_response_data_item_attributes_obj.additional_properties = d
        return icons_list_get_response_data_item_attributes_obj

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

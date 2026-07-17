# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="CustomfieldsListPostRequestDataItemAttributesFieldsItemParametersItem",
)


@_attrs_define
class CustomfieldsListPostRequestDataItemAttributesFieldsItemParametersItem:
    """
    Attributes:
        key (str | Unset):  Example: parameter1.
        name (str | Unset):  Example: parameter1.
        title (str | Unset):  Example: MyParameter.
    """

    key: str | Unset = UNSET
    name: str | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        name = self.name

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if name is not UNSET:
            field_dict["name"] = name
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key", UNSET)

        name = d.pop("name", UNSET)

        title = d.pop("title", UNSET)

        customfields_list_post_request_data_item_attributes_fields_item_parameters_item_obj = cls(
            key=key,
            name=name,
            title=title,
        )

        customfields_list_post_request_data_item_attributes_fields_item_parameters_item_obj.additional_properties = d
        return customfields_list_post_request_data_item_attributes_fields_item_parameters_item_obj

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

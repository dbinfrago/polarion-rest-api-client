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
    bound="DocumentsSinglePostResponseDataAttributesRenderingLayoutsItemPropertiesItem",
)


@_attrs_define
class DocumentsSinglePostResponseDataAttributesRenderingLayoutsItemPropertiesItem:
    """
    Attributes:
        key (str | Unset):  Example: fieldsAtStart.
        value (str | Unset):  Example: id.
    """

    key: str | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key", UNSET)

        value = d.pop("value", UNSET)

        documents_single_post_response_data_attributes_rendering_layouts_item_properties_item_obj = cls(
            key=key,
            value=value,
        )

        documents_single_post_response_data_attributes_rendering_layouts_item_properties_item_obj.additional_properties = d
        return documents_single_post_response_data_attributes_rendering_layouts_item_properties_item_obj

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

# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="EnumerationsListGetResponseDataItemAttributesOptionsItemLinkRulesItem",
)


@_attrs_define
class EnumerationsListGetResponseDataItemAttributesOptionsItemLinkRulesItem:
    """
    Attributes:
        from_types (list[str] | Unset):  Example: ['requirement'].
        same_type (bool | Unset):
        to_types (list[str] | Unset):  Example: ['requirement'].
    """

    from_types: list[str] | Unset = UNSET
    same_type: bool | Unset = UNSET
    to_types: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        from_types: list[str] | Unset = UNSET
        if not isinstance(self.from_types, Unset):
            from_types = self.from_types

        same_type = self.same_type

        to_types: list[str] | Unset = UNSET
        if not isinstance(self.to_types, Unset):
            to_types = self.to_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_types is not UNSET:
            field_dict["fromTypes"] = from_types
        if same_type is not UNSET:
            field_dict["sameType"] = same_type
        if to_types is not UNSET:
            field_dict["toTypes"] = to_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        from_types = cast(list[str], d.pop("fromTypes", UNSET))

        same_type = d.pop("sameType", UNSET)

        to_types = cast(list[str], d.pop("toTypes", UNSET))

        enumerations_list_get_response_data_item_attributes_options_item_link_rules_item_obj = cls(
            from_types=from_types,
            same_type=same_type,
            to_types=to_types,
        )

        enumerations_list_get_response_data_item_attributes_options_item_link_rules_item_obj.additional_properties = d
        return enumerations_list_get_response_data_item_attributes_options_item_link_rules_item_obj

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

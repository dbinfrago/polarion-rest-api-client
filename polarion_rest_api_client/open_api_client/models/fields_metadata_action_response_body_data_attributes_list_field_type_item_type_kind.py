# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fields_metadata_action_response_body_data_attributes_list_field_type_item_type_kind_enum_item import (
    FieldsMetadataActionResponseBodyDataAttributesListFieldTypeItemTypeKindEnumItem,
)
from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="FieldsMetadataActionResponseBodyDataAttributesListFieldTypeItemTypeKind",
)


@_attrs_define
class FieldsMetadataActionResponseBodyDataAttributesListFieldTypeItemTypeKind:
    """
    Attributes:
        enum (list[FieldsMetadataActionResponseBodyDataAttributesListFieldTypeItemTypeKindEnumItem] | Unset):
    """

    enum: (
        list[
            FieldsMetadataActionResponseBodyDataAttributesListFieldTypeItemTypeKindEnumItem
        ]
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        enum: list[str] | Unset = UNSET
        if not isinstance(self.enum, Unset):
            enum = []
            for enum_item_data in self.enum:
                enum_item = enum_item_data.value
                enum.append(enum_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enum is not UNSET:
            field_dict["enum"] = enum

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _enum = d.pop("enum", UNSET)
        enum: (
            list[
                FieldsMetadataActionResponseBodyDataAttributesListFieldTypeItemTypeKindEnumItem
            ]
            | Unset
        ) = UNSET
        if _enum is not UNSET:
            enum = []
            for enum_item_data in _enum:
                enum_item = FieldsMetadataActionResponseBodyDataAttributesListFieldTypeItemTypeKindEnumItem(
                    enum_item_data
                )

                enum.append(enum_item)

        fields_metadata_action_response_body_data_attributes_list_field_type_item_type_kind_obj = cls(
            enum=enum,
        )

        fields_metadata_action_response_body_data_attributes_list_field_type_item_type_kind_obj.additional_properties = d
        return fields_metadata_action_response_body_data_attributes_list_field_type_item_type_kind_obj

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

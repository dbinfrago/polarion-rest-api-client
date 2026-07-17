# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="FieldsMetadataActionResponseBodyDataAttributesEnumFieldType"
)


@_attrs_define
class FieldsMetadataActionResponseBodyDataAttributesEnumFieldType:
    """
    Attributes:
        enum_context (str | Unset):  Example: enum-context.
        enum_name (str | Unset):  Example: enum-name.
        kind (str | Unset):  Example: enumeration.
    """

    enum_context: str | Unset = UNSET
    enum_name: str | Unset = UNSET
    kind: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        enum_context = self.enum_context

        enum_name = self.enum_name

        kind = self.kind

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enum_context is not UNSET:
            field_dict["enumContext"] = enum_context
        if enum_name is not UNSET:
            field_dict["enumName"] = enum_name
        if kind is not UNSET:
            field_dict["kind"] = kind

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enum_context = d.pop("enumContext", UNSET)

        enum_name = d.pop("enumName", UNSET)

        kind = d.pop("kind", UNSET)

        fields_metadata_action_response_body_data_attributes_enum_field_type_obj = cls(
            enum_context=enum_context,
            enum_name=enum_name,
            kind=kind,
        )

        fields_metadata_action_response_body_data_attributes_enum_field_type_obj.additional_properties = d
        return fields_metadata_action_response_body_data_attributes_enum_field_type_obj

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

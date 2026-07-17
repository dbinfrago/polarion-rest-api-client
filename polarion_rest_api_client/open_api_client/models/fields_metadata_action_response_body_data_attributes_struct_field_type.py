# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="FieldsMetadataActionResponseBodyDataAttributesStructFieldType"
)


@_attrs_define
class FieldsMetadataActionResponseBodyDataAttributesStructFieldType:
    """
    Attributes:
        kind (str | Unset):  Example: structure.
        structure_name (str | Unset):  Example: structureId.
    """

    kind: str | Unset = UNSET
    structure_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        structure_name = self.structure_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if structure_name is not UNSET:
            field_dict["structureName"] = structure_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = d.pop("kind", UNSET)

        structure_name = d.pop("structureName", UNSET)

        fields_metadata_action_response_body_data_attributes_struct_field_type_obj = cls(
            kind=kind,
            structure_name=structure_name,
        )

        fields_metadata_action_response_body_data_attributes_struct_field_type_obj.additional_properties = d
        return fields_metadata_action_response_body_data_attributes_struct_field_type_obj

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

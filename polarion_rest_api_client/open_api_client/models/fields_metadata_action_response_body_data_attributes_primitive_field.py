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

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fields_metadata_action_response_body_data_attributes_primitive_field_type import (
        FieldsMetadataActionResponseBodyDataAttributesPrimitiveFieldType,
    )


T = TypeVar(
    "T", bound="FieldsMetadataActionResponseBodyDataAttributesPrimitiveField"
)


@_attrs_define
class FieldsMetadataActionResponseBodyDataAttributesPrimitiveField:
    """
    Attributes:
        label (str | Unset):  Example: field-label.
        type_ (FieldsMetadataActionResponseBodyDataAttributesPrimitiveFieldType | Unset):
    """

    label: str | Unset = UNSET
    type_: (
        FieldsMetadataActionResponseBodyDataAttributesPrimitiveFieldType
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        type_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label is not UNSET:
            field_dict["label"] = label
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fields_metadata_action_response_body_data_attributes_primitive_field_type import (
            FieldsMetadataActionResponseBodyDataAttributesPrimitiveFieldType,
        )

        d = dict(src_dict)
        label = d.pop("label", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: (
            FieldsMetadataActionResponseBodyDataAttributesPrimitiveFieldType
            | Unset
        )
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = FieldsMetadataActionResponseBodyDataAttributesPrimitiveFieldType.from_dict(
                _type_
            )

        fields_metadata_action_response_body_data_attributes_primitive_field_obj = cls(
            label=label,
            type_=type_,
        )

        fields_metadata_action_response_body_data_attributes_primitive_field_obj.additional_properties = d
        return fields_metadata_action_response_body_data_attributes_primitive_field_obj

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

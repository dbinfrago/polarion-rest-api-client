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
    from ..models.fields_metadata_action_response_body_data_attributes_primitive_field_type_kind import (
        FieldsMetadataActionResponseBodyDataAttributesPrimitiveFieldTypeKind,
    )


T = TypeVar(
    "T",
    bound="FieldsMetadataActionResponseBodyDataAttributesPrimitiveFieldType",
)


@_attrs_define
class FieldsMetadataActionResponseBodyDataAttributesPrimitiveFieldType:
    """
    Attributes:
        kind (FieldsMetadataActionResponseBodyDataAttributesPrimitiveFieldTypeKind | Unset):
    """

    kind: (
        FieldsMetadataActionResponseBodyDataAttributesPrimitiveFieldTypeKind
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        kind: dict[str, Any] | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fields_metadata_action_response_body_data_attributes_primitive_field_type_kind import (
            FieldsMetadataActionResponseBodyDataAttributesPrimitiveFieldTypeKind,
        )

        d = dict(src_dict)
        _kind = d.pop("kind", UNSET)
        kind: (
            FieldsMetadataActionResponseBodyDataAttributesPrimitiveFieldTypeKind
            | Unset
        )
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = FieldsMetadataActionResponseBodyDataAttributesPrimitiveFieldTypeKind.from_dict(
                _kind
            )

        fields_metadata_action_response_body_data_attributes_primitive_field_type_obj = cls(
            kind=kind,
        )

        fields_metadata_action_response_body_data_attributes_primitive_field_type_obj.additional_properties = d
        return fields_metadata_action_response_body_data_attributes_primitive_field_type_obj

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

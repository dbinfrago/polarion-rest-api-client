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
    from ..models.fields_metadata_action_response_body_data_attributes_enum_field import (
        FieldsMetadataActionResponseBodyDataAttributesEnumField,
    )
    from ..models.fields_metadata_action_response_body_data_attributes_list_field import (
        FieldsMetadataActionResponseBodyDataAttributesListField,
    )
    from ..models.fields_metadata_action_response_body_data_attributes_primitive_field import (
        FieldsMetadataActionResponseBodyDataAttributesPrimitiveField,
    )
    from ..models.fields_metadata_action_response_body_data_attributes_struct_field import (
        FieldsMetadataActionResponseBodyDataAttributesStructField,
    )


T = TypeVar("T", bound="FieldsMetadataActionResponseBodyDataAttributes")


@_attrs_define
class FieldsMetadataActionResponseBodyDataAttributes:
    """
    Attributes:
        enum_field (FieldsMetadataActionResponseBodyDataAttributesEnumField | Unset):
        list_field (FieldsMetadataActionResponseBodyDataAttributesListField | Unset):
        primitive_field (FieldsMetadataActionResponseBodyDataAttributesPrimitiveField | Unset):
        struct_field (FieldsMetadataActionResponseBodyDataAttributesStructField | Unset):
    """

    enum_field: (
        FieldsMetadataActionResponseBodyDataAttributesEnumField | Unset
    ) = UNSET
    list_field: (
        FieldsMetadataActionResponseBodyDataAttributesListField | Unset
    ) = UNSET
    primitive_field: (
        FieldsMetadataActionResponseBodyDataAttributesPrimitiveField | Unset
    ) = UNSET
    struct_field: (
        FieldsMetadataActionResponseBodyDataAttributesStructField | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        enum_field: dict[str, Any] | Unset = UNSET
        if not isinstance(self.enum_field, Unset):
            enum_field = self.enum_field.to_dict()

        list_field: dict[str, Any] | Unset = UNSET
        if not isinstance(self.list_field, Unset):
            list_field = self.list_field.to_dict()

        primitive_field: dict[str, Any] | Unset = UNSET
        if not isinstance(self.primitive_field, Unset):
            primitive_field = self.primitive_field.to_dict()

        struct_field: dict[str, Any] | Unset = UNSET
        if not isinstance(self.struct_field, Unset):
            struct_field = self.struct_field.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enum_field is not UNSET:
            field_dict["enumField"] = enum_field
        if list_field is not UNSET:
            field_dict["listField"] = list_field
        if primitive_field is not UNSET:
            field_dict["primitiveField"] = primitive_field
        if struct_field is not UNSET:
            field_dict["structField"] = struct_field

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fields_metadata_action_response_body_data_attributes_enum_field import (
            FieldsMetadataActionResponseBodyDataAttributesEnumField,
        )
        from ..models.fields_metadata_action_response_body_data_attributes_list_field import (
            FieldsMetadataActionResponseBodyDataAttributesListField,
        )
        from ..models.fields_metadata_action_response_body_data_attributes_primitive_field import (
            FieldsMetadataActionResponseBodyDataAttributesPrimitiveField,
        )
        from ..models.fields_metadata_action_response_body_data_attributes_struct_field import (
            FieldsMetadataActionResponseBodyDataAttributesStructField,
        )

        d = dict(src_dict)
        _enum_field = d.pop("enumField", UNSET)
        enum_field: (
            FieldsMetadataActionResponseBodyDataAttributesEnumField | Unset
        )
        if isinstance(_enum_field, Unset):
            enum_field = UNSET
        else:
            enum_field = FieldsMetadataActionResponseBodyDataAttributesEnumField.from_dict(
                _enum_field
            )

        _list_field = d.pop("listField", UNSET)
        list_field: (
            FieldsMetadataActionResponseBodyDataAttributesListField | Unset
        )
        if isinstance(_list_field, Unset):
            list_field = UNSET
        else:
            list_field = FieldsMetadataActionResponseBodyDataAttributesListField.from_dict(
                _list_field
            )

        _primitive_field = d.pop("primitiveField", UNSET)
        primitive_field: (
            FieldsMetadataActionResponseBodyDataAttributesPrimitiveField
            | Unset
        )
        if isinstance(_primitive_field, Unset):
            primitive_field = UNSET
        else:
            primitive_field = FieldsMetadataActionResponseBodyDataAttributesPrimitiveField.from_dict(
                _primitive_field
            )

        _struct_field = d.pop("structField", UNSET)
        struct_field: (
            FieldsMetadataActionResponseBodyDataAttributesStructField | Unset
        )
        if isinstance(_struct_field, Unset):
            struct_field = UNSET
        else:
            struct_field = FieldsMetadataActionResponseBodyDataAttributesStructField.from_dict(
                _struct_field
            )

        fields_metadata_action_response_body_data_attributes_obj = cls(
            enum_field=enum_field,
            list_field=list_field,
            primitive_field=primitive_field,
            struct_field=struct_field,
        )

        fields_metadata_action_response_body_data_attributes_obj.additional_properties = d
        return fields_metadata_action_response_body_data_attributes_obj

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

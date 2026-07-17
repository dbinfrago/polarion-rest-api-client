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
    from ..models.fields_metadata_action_response_body_data_attributes_list_field_type_item_type import (
        FieldsMetadataActionResponseBodyDataAttributesListFieldTypeItemType,
    )


T = TypeVar(
    "T", bound="FieldsMetadataActionResponseBodyDataAttributesListFieldType"
)


@_attrs_define
class FieldsMetadataActionResponseBodyDataAttributesListFieldType:
    """
    Attributes:
        item_type (FieldsMetadataActionResponseBodyDataAttributesListFieldTypeItemType | Unset):
        kind (str | Unset):  Example: list.
    """

    item_type: (
        FieldsMetadataActionResponseBodyDataAttributesListFieldTypeItemType
        | Unset
    ) = UNSET
    kind: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        item_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.item_type, Unset):
            item_type = self.item_type.to_dict()

        kind = self.kind

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if item_type is not UNSET:
            field_dict["itemType"] = item_type
        if kind is not UNSET:
            field_dict["kind"] = kind

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fields_metadata_action_response_body_data_attributes_list_field_type_item_type import (
            FieldsMetadataActionResponseBodyDataAttributesListFieldTypeItemType,
        )

        d = dict(src_dict)
        _item_type = d.pop("itemType", UNSET)
        item_type: (
            FieldsMetadataActionResponseBodyDataAttributesListFieldTypeItemType
            | Unset
        )
        if isinstance(_item_type, Unset):
            item_type = UNSET
        else:
            item_type = FieldsMetadataActionResponseBodyDataAttributesListFieldTypeItemType.from_dict(
                _item_type
            )

        kind = d.pop("kind", UNSET)

        fields_metadata_action_response_body_data_attributes_list_field_type_obj = cls(
            item_type=item_type,
            kind=kind,
        )

        fields_metadata_action_response_body_data_attributes_list_field_type_obj.additional_properties = d
        return fields_metadata_action_response_body_data_attributes_list_field_type_obj

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

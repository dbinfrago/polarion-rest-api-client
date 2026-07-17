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
    bound="FieldsMetadataActionResponseBodyDataRelationshipsRelationshipFieldType",
)


@_attrs_define
class FieldsMetadataActionResponseBodyDataRelationshipsRelationshipFieldType:
    """
    Attributes:
        kind (str | Unset):  Example: relationship.
        multi (bool | Unset):  Example: True.
        target_resource_types (list[str] | Unset):
    """

    kind: str | Unset = UNSET
    multi: bool | Unset = UNSET
    target_resource_types: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        multi = self.multi

        target_resource_types: list[str] | Unset = UNSET
        if not isinstance(self.target_resource_types, Unset):
            target_resource_types = self.target_resource_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if multi is not UNSET:
            field_dict["multi"] = multi
        if target_resource_types is not UNSET:
            field_dict["targetResourceTypes"] = target_resource_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = d.pop("kind", UNSET)

        multi = d.pop("multi", UNSET)

        target_resource_types = cast(
            list[str], d.pop("targetResourceTypes", UNSET)
        )

        fields_metadata_action_response_body_data_relationships_relationship_field_type_obj = cls(
            kind=kind,
            multi=multi,
            target_resource_types=target_resource_types,
        )

        fields_metadata_action_response_body_data_relationships_relationship_field_type_obj.additional_properties = d
        return fields_metadata_action_response_body_data_relationships_relationship_field_type_obj

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

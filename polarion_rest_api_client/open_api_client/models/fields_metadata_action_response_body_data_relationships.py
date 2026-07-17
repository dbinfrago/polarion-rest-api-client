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
    from ..models.fields_metadata_action_response_body_data_relationships_relationship_field import (
        FieldsMetadataActionResponseBodyDataRelationshipsRelationshipField,
    )


T = TypeVar("T", bound="FieldsMetadataActionResponseBodyDataRelationships")


@_attrs_define
class FieldsMetadataActionResponseBodyDataRelationships:
    """
    Attributes:
        relationship_field (FieldsMetadataActionResponseBodyDataRelationshipsRelationshipField | Unset):
    """

    relationship_field: (
        FieldsMetadataActionResponseBodyDataRelationshipsRelationshipField
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        relationship_field: dict[str, Any] | Unset = UNSET
        if not isinstance(self.relationship_field, Unset):
            relationship_field = self.relationship_field.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if relationship_field is not UNSET:
            field_dict["relationshipField"] = relationship_field

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fields_metadata_action_response_body_data_relationships_relationship_field import (
            FieldsMetadataActionResponseBodyDataRelationshipsRelationshipField,
        )

        d = dict(src_dict)
        _relationship_field = d.pop("relationshipField", UNSET)
        relationship_field: (
            FieldsMetadataActionResponseBodyDataRelationshipsRelationshipField
            | Unset
        )
        if isinstance(_relationship_field, Unset):
            relationship_field = UNSET
        else:
            relationship_field = FieldsMetadataActionResponseBodyDataRelationshipsRelationshipField.from_dict(
                _relationship_field
            )

        fields_metadata_action_response_body_data_relationships_obj = cls(
            relationship_field=relationship_field,
        )

        fields_metadata_action_response_body_data_relationships_obj.additional_properties = d
        return fields_metadata_action_response_body_data_relationships_obj

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

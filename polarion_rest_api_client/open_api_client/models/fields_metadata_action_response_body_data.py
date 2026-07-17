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
    from ..models.fields_metadata_action_response_body_data_attributes import (
        FieldsMetadataActionResponseBodyDataAttributes,
    )
    from ..models.fields_metadata_action_response_body_data_relationships import (
        FieldsMetadataActionResponseBodyDataRelationships,
    )


T = TypeVar("T", bound="FieldsMetadataActionResponseBodyData")


@_attrs_define
class FieldsMetadataActionResponseBodyData:
    """
    Attributes:
        attributes (FieldsMetadataActionResponseBodyDataAttributes | Unset):
        relationships (FieldsMetadataActionResponseBodyDataRelationships | Unset):
    """

    attributes: FieldsMetadataActionResponseBodyDataAttributes | Unset = UNSET
    relationships: (
        FieldsMetadataActionResponseBodyDataRelationships | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        relationships: dict[str, Any] | Unset = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = self.relationships.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if relationships is not UNSET:
            field_dict["relationships"] = relationships

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fields_metadata_action_response_body_data_attributes import (
            FieldsMetadataActionResponseBodyDataAttributes,
        )
        from ..models.fields_metadata_action_response_body_data_relationships import (
            FieldsMetadataActionResponseBodyDataRelationships,
        )

        d = dict(src_dict)
        _attributes = d.pop("attributes", UNSET)
        attributes: FieldsMetadataActionResponseBodyDataAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = (
                FieldsMetadataActionResponseBodyDataAttributes.from_dict(
                    _attributes
                )
            )

        _relationships = d.pop("relationships", UNSET)
        relationships: (
            FieldsMetadataActionResponseBodyDataRelationships | Unset
        )
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = (
                FieldsMetadataActionResponseBodyDataRelationships.from_dict(
                    _relationships
                )
            )

        fields_metadata_action_response_body_data_obj = cls(
            attributes=attributes,
            relationships=relationships,
        )

        fields_metadata_action_response_body_data_obj.additional_properties = d
        return fields_metadata_action_response_body_data_obj

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

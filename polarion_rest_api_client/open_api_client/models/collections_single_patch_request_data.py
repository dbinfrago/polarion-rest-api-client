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

from ..models.collections_single_patch_request_data_type import (
    CollectionsSinglePatchRequestDataType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.collections_single_patch_request_data_attributes import (
        CollectionsSinglePatchRequestDataAttributes,
    )
    from ..models.collections_single_patch_request_data_relationships import (
        CollectionsSinglePatchRequestDataRelationships,
    )


T = TypeVar("T", bound="CollectionsSinglePatchRequestData")


@_attrs_define
class CollectionsSinglePatchRequestData:
    """
    Attributes:
        type_ (CollectionsSinglePatchRequestDataType | Unset):
        id (str | Unset):  Example: MyProjectId/MyCollectionId.
        attributes (CollectionsSinglePatchRequestDataAttributes | Unset):
        relationships (CollectionsSinglePatchRequestDataRelationships | Unset):
    """

    type_: CollectionsSinglePatchRequestDataType | Unset = UNSET
    id: str | Unset = UNSET
    attributes: CollectionsSinglePatchRequestDataAttributes | Unset = UNSET
    relationships: CollectionsSinglePatchRequestDataRelationships | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        id = self.id

        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        relationships: dict[str, Any] | Unset = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = self.relationships.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if id is not UNSET:
            field_dict["id"] = id
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if relationships is not UNSET:
            field_dict["relationships"] = relationships

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.collections_single_patch_request_data_attributes import (
            CollectionsSinglePatchRequestDataAttributes,
        )
        from ..models.collections_single_patch_request_data_relationships import (
            CollectionsSinglePatchRequestDataRelationships,
        )

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: CollectionsSinglePatchRequestDataType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CollectionsSinglePatchRequestDataType(_type_)

        id = d.pop("id", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: CollectionsSinglePatchRequestDataAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = CollectionsSinglePatchRequestDataAttributes.from_dict(
                _attributes
            )

        _relationships = d.pop("relationships", UNSET)
        relationships: CollectionsSinglePatchRequestDataRelationships | Unset
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = (
                CollectionsSinglePatchRequestDataRelationships.from_dict(
                    _relationships
                )
            )

        collections_single_patch_request_data_obj = cls(
            type_=type_,
            id=id,
            attributes=attributes,
            relationships=relationships,
        )

        collections_single_patch_request_data_obj.additional_properties = d
        return collections_single_patch_request_data_obj

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

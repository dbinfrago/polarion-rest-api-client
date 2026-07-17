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

from ..models.plans_single_patch_request_data_type import (
    PlansSinglePatchRequestDataType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plans_single_patch_request_data_attributes import (
        PlansSinglePatchRequestDataAttributes,
    )
    from ..models.plans_single_patch_request_data_relationships import (
        PlansSinglePatchRequestDataRelationships,
    )


T = TypeVar("T", bound="PlansSinglePatchRequestData")


@_attrs_define
class PlansSinglePatchRequestData:
    """
    Attributes:
        type_ (PlansSinglePatchRequestDataType | Unset):
        id (str | Unset):  Example: MyProjectId/MyPlanId.
        attributes (PlansSinglePatchRequestDataAttributes | Unset):
        relationships (PlansSinglePatchRequestDataRelationships | Unset):
    """

    type_: PlansSinglePatchRequestDataType | Unset = UNSET
    id: str | Unset = UNSET
    attributes: PlansSinglePatchRequestDataAttributes | Unset = UNSET
    relationships: PlansSinglePatchRequestDataRelationships | Unset = UNSET
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
        from ..models.plans_single_patch_request_data_attributes import (
            PlansSinglePatchRequestDataAttributes,
        )
        from ..models.plans_single_patch_request_data_relationships import (
            PlansSinglePatchRequestDataRelationships,
        )

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: PlansSinglePatchRequestDataType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = PlansSinglePatchRequestDataType(_type_)

        id = d.pop("id", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: PlansSinglePatchRequestDataAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = PlansSinglePatchRequestDataAttributes.from_dict(
                _attributes
            )

        _relationships = d.pop("relationships", UNSET)
        relationships: PlansSinglePatchRequestDataRelationships | Unset
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = PlansSinglePatchRequestDataRelationships.from_dict(
                _relationships
            )

        plans_single_patch_request_data_obj = cls(
            type_=type_,
            id=id,
            attributes=attributes,
            relationships=relationships,
        )

        plans_single_patch_request_data_obj.additional_properties = d
        return plans_single_patch_request_data_obj

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

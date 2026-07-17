# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.plans_single_patch_request_data_relationships_parent_data_type import (
    PlansSinglePatchRequestDataRelationshipsParentDataType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PlansSinglePatchRequestDataRelationshipsParentData")


@_attrs_define
class PlansSinglePatchRequestDataRelationshipsParentData:
    """
    Attributes:
        id (str | Unset):  Example: MyProjectId/MyPlanId.
        type_ (PlansSinglePatchRequestDataRelationshipsParentDataType | Unset):
    """

    id: str | Unset = UNSET
    type_: PlansSinglePatchRequestDataRelationshipsParentDataType | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: PlansSinglePatchRequestDataRelationshipsParentDataType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = PlansSinglePatchRequestDataRelationshipsParentDataType(
                _type_
            )

        plans_single_patch_request_data_relationships_parent_data_obj = cls(
            id=id,
            type_=type_,
        )

        plans_single_patch_request_data_relationships_parent_data_obj.additional_properties = d
        return plans_single_patch_request_data_relationships_parent_data_obj

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

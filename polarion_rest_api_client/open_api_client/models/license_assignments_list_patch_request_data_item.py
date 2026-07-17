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

from ..models.license_assignments_list_patch_request_data_item_type import (
    LicenseAssignmentsListPatchRequestDataItemType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.license_assignments_list_patch_request_data_item_relationships import (
        LicenseAssignmentsListPatchRequestDataItemRelationships,
    )


T = TypeVar("T", bound="LicenseAssignmentsListPatchRequestDataItem")


@_attrs_define
class LicenseAssignmentsListPatchRequestDataItem:
    """
    Attributes:
        type_ (LicenseAssignmentsListPatchRequestDataItemType | Unset):
        id (str | Unset):  Example: MyUserId.
        relationships (LicenseAssignmentsListPatchRequestDataItemRelationships | Unset):
    """

    type_: LicenseAssignmentsListPatchRequestDataItemType | Unset = UNSET
    id: str | Unset = UNSET
    relationships: (
        LicenseAssignmentsListPatchRequestDataItemRelationships | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        id = self.id

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
        if relationships is not UNSET:
            field_dict["relationships"] = relationships

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.license_assignments_list_patch_request_data_item_relationships import (
            LicenseAssignmentsListPatchRequestDataItemRelationships,
        )

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: LicenseAssignmentsListPatchRequestDataItemType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = LicenseAssignmentsListPatchRequestDataItemType(_type_)

        id = d.pop("id", UNSET)

        _relationships = d.pop("relationships", UNSET)
        relationships: (
            LicenseAssignmentsListPatchRequestDataItemRelationships | Unset
        )
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = LicenseAssignmentsListPatchRequestDataItemRelationships.from_dict(
                _relationships
            )

        license_assignments_list_patch_request_data_item_obj = cls(
            type_=type_,
            id=id,
            relationships=relationships,
        )

        license_assignments_list_patch_request_data_item_obj.additional_properties = d
        return license_assignments_list_patch_request_data_item_obj

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

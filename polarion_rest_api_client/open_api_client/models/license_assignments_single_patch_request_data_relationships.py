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
    from ..models.license_assignments_single_patch_request_data_relationships_add_on_slots import (
        LicenseAssignmentsSinglePatchRequestDataRelationshipsAddOnSlots,
    )
    from ..models.license_assignments_single_patch_request_data_relationships_base_slot import (
        LicenseAssignmentsSinglePatchRequestDataRelationshipsBaseSlot,
    )


T = TypeVar("T", bound="LicenseAssignmentsSinglePatchRequestDataRelationships")


@_attrs_define
class LicenseAssignmentsSinglePatchRequestDataRelationships:
    """
    Attributes:
        add_on_slots (LicenseAssignmentsSinglePatchRequestDataRelationshipsAddOnSlots | Unset):
        base_slot (LicenseAssignmentsSinglePatchRequestDataRelationshipsBaseSlot | Unset):
    """

    add_on_slots: (
        LicenseAssignmentsSinglePatchRequestDataRelationshipsAddOnSlots | Unset
    ) = UNSET
    base_slot: (
        LicenseAssignmentsSinglePatchRequestDataRelationshipsBaseSlot | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        add_on_slots: dict[str, Any] | Unset = UNSET
        if not isinstance(self.add_on_slots, Unset):
            add_on_slots = self.add_on_slots.to_dict()

        base_slot: dict[str, Any] | Unset = UNSET
        if not isinstance(self.base_slot, Unset):
            base_slot = self.base_slot.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if add_on_slots is not UNSET:
            field_dict["addOnSlots"] = add_on_slots
        if base_slot is not UNSET:
            field_dict["baseSlot"] = base_slot

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.license_assignments_single_patch_request_data_relationships_add_on_slots import (
            LicenseAssignmentsSinglePatchRequestDataRelationshipsAddOnSlots,
        )
        from ..models.license_assignments_single_patch_request_data_relationships_base_slot import (
            LicenseAssignmentsSinglePatchRequestDataRelationshipsBaseSlot,
        )

        d = dict(src_dict)
        _add_on_slots = d.pop("addOnSlots", UNSET)
        add_on_slots: (
            LicenseAssignmentsSinglePatchRequestDataRelationshipsAddOnSlots
            | Unset
        )
        if isinstance(_add_on_slots, Unset):
            add_on_slots = UNSET
        else:
            add_on_slots = LicenseAssignmentsSinglePatchRequestDataRelationshipsAddOnSlots.from_dict(
                _add_on_slots
            )

        _base_slot = d.pop("baseSlot", UNSET)
        base_slot: (
            LicenseAssignmentsSinglePatchRequestDataRelationshipsBaseSlot
            | Unset
        )
        if isinstance(_base_slot, Unset):
            base_slot = UNSET
        else:
            base_slot = LicenseAssignmentsSinglePatchRequestDataRelationshipsBaseSlot.from_dict(
                _base_slot
            )

        license_assignments_single_patch_request_data_relationships_obj = cls(
            add_on_slots=add_on_slots,
            base_slot=base_slot,
        )

        license_assignments_single_patch_request_data_relationships_obj.additional_properties = d
        return license_assignments_single_patch_request_data_relationships_obj

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

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
    from ..models.license_assignments_single_get_response_data_relationships_add_on_slots import (
        LicenseAssignmentsSingleGetResponseDataRelationshipsAddOnSlots,
    )
    from ..models.license_assignments_single_get_response_data_relationships_base_slot import (
        LicenseAssignmentsSingleGetResponseDataRelationshipsBaseSlot,
    )
    from ..models.license_assignments_single_get_response_data_relationships_user import (
        LicenseAssignmentsSingleGetResponseDataRelationshipsUser,
    )


T = TypeVar("T", bound="LicenseAssignmentsSingleGetResponseDataRelationships")


@_attrs_define
class LicenseAssignmentsSingleGetResponseDataRelationships:
    """
    Attributes:
        add_on_slots (LicenseAssignmentsSingleGetResponseDataRelationshipsAddOnSlots | Unset):
        base_slot (LicenseAssignmentsSingleGetResponseDataRelationshipsBaseSlot | Unset):
        user (LicenseAssignmentsSingleGetResponseDataRelationshipsUser | Unset):
    """

    add_on_slots: (
        LicenseAssignmentsSingleGetResponseDataRelationshipsAddOnSlots | Unset
    ) = UNSET
    base_slot: (
        LicenseAssignmentsSingleGetResponseDataRelationshipsBaseSlot | Unset
    ) = UNSET
    user: LicenseAssignmentsSingleGetResponseDataRelationshipsUser | Unset = (
        UNSET
    )
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

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if add_on_slots is not UNSET:
            field_dict["addOnSlots"] = add_on_slots
        if base_slot is not UNSET:
            field_dict["baseSlot"] = base_slot
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.license_assignments_single_get_response_data_relationships_add_on_slots import (
            LicenseAssignmentsSingleGetResponseDataRelationshipsAddOnSlots,
        )
        from ..models.license_assignments_single_get_response_data_relationships_base_slot import (
            LicenseAssignmentsSingleGetResponseDataRelationshipsBaseSlot,
        )
        from ..models.license_assignments_single_get_response_data_relationships_user import (
            LicenseAssignmentsSingleGetResponseDataRelationshipsUser,
        )

        d = dict(src_dict)
        _add_on_slots = d.pop("addOnSlots", UNSET)
        add_on_slots: (
            LicenseAssignmentsSingleGetResponseDataRelationshipsAddOnSlots
            | Unset
        )
        if isinstance(_add_on_slots, Unset):
            add_on_slots = UNSET
        else:
            add_on_slots = LicenseAssignmentsSingleGetResponseDataRelationshipsAddOnSlots.from_dict(
                _add_on_slots
            )

        _base_slot = d.pop("baseSlot", UNSET)
        base_slot: (
            LicenseAssignmentsSingleGetResponseDataRelationshipsBaseSlot
            | Unset
        )
        if isinstance(_base_slot, Unset):
            base_slot = UNSET
        else:
            base_slot = LicenseAssignmentsSingleGetResponseDataRelationshipsBaseSlot.from_dict(
                _base_slot
            )

        _user = d.pop("user", UNSET)
        user: LicenseAssignmentsSingleGetResponseDataRelationshipsUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = LicenseAssignmentsSingleGetResponseDataRelationshipsUser.from_dict(
                _user
            )

        license_assignments_single_get_response_data_relationships_obj = cls(
            add_on_slots=add_on_slots,
            base_slot=base_slot,
            user=user,
        )

        license_assignments_single_get_response_data_relationships_obj.additional_properties = d
        return license_assignments_single_get_response_data_relationships_obj

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

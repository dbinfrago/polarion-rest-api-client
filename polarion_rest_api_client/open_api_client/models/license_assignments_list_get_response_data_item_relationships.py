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
    from ..models.license_assignments_list_get_response_data_item_relationships_add_on_slots import (
        LicenseAssignmentsListGetResponseDataItemRelationshipsAddOnSlots,
    )
    from ..models.license_assignments_list_get_response_data_item_relationships_base_slot import (
        LicenseAssignmentsListGetResponseDataItemRelationshipsBaseSlot,
    )
    from ..models.license_assignments_list_get_response_data_item_relationships_user import (
        LicenseAssignmentsListGetResponseDataItemRelationshipsUser,
    )


T = TypeVar(
    "T", bound="LicenseAssignmentsListGetResponseDataItemRelationships"
)


@_attrs_define
class LicenseAssignmentsListGetResponseDataItemRelationships:
    """
    Attributes:
        add_on_slots (LicenseAssignmentsListGetResponseDataItemRelationshipsAddOnSlots | Unset):
        base_slot (LicenseAssignmentsListGetResponseDataItemRelationshipsBaseSlot | Unset):
        user (LicenseAssignmentsListGetResponseDataItemRelationshipsUser | Unset):
    """

    add_on_slots: (
        LicenseAssignmentsListGetResponseDataItemRelationshipsAddOnSlots
        | Unset
    ) = UNSET
    base_slot: (
        LicenseAssignmentsListGetResponseDataItemRelationshipsBaseSlot | Unset
    ) = UNSET
    user: (
        LicenseAssignmentsListGetResponseDataItemRelationshipsUser | Unset
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
        from ..models.license_assignments_list_get_response_data_item_relationships_add_on_slots import (
            LicenseAssignmentsListGetResponseDataItemRelationshipsAddOnSlots,
        )
        from ..models.license_assignments_list_get_response_data_item_relationships_base_slot import (
            LicenseAssignmentsListGetResponseDataItemRelationshipsBaseSlot,
        )
        from ..models.license_assignments_list_get_response_data_item_relationships_user import (
            LicenseAssignmentsListGetResponseDataItemRelationshipsUser,
        )

        d = dict(src_dict)
        _add_on_slots = d.pop("addOnSlots", UNSET)
        add_on_slots: (
            LicenseAssignmentsListGetResponseDataItemRelationshipsAddOnSlots
            | Unset
        )
        if isinstance(_add_on_slots, Unset):
            add_on_slots = UNSET
        else:
            add_on_slots = LicenseAssignmentsListGetResponseDataItemRelationshipsAddOnSlots.from_dict(
                _add_on_slots
            )

        _base_slot = d.pop("baseSlot", UNSET)
        base_slot: (
            LicenseAssignmentsListGetResponseDataItemRelationshipsBaseSlot
            | Unset
        )
        if isinstance(_base_slot, Unset):
            base_slot = UNSET
        else:
            base_slot = LicenseAssignmentsListGetResponseDataItemRelationshipsBaseSlot.from_dict(
                _base_slot
            )

        _user = d.pop("user", UNSET)
        user: (
            LicenseAssignmentsListGetResponseDataItemRelationshipsUser | Unset
        )
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = LicenseAssignmentsListGetResponseDataItemRelationshipsUser.from_dict(
                _user
            )

        license_assignments_list_get_response_data_item_relationships_obj = (
            cls(
                add_on_slots=add_on_slots,
                base_slot=base_slot,
                user=user,
            )
        )

        license_assignments_list_get_response_data_item_relationships_obj.additional_properties = d
        return (
            license_assignments_list_get_response_data_item_relationships_obj
        )

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

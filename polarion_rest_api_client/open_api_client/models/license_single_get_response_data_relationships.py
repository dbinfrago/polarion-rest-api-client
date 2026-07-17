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
    from ..models.license_single_get_response_data_relationships_default_add_on_license_slots import (
        LicenseSingleGetResponseDataRelationshipsDefaultAddOnLicenseSlots,
    )
    from ..models.license_single_get_response_data_relationships_default_base_license_slot import (
        LicenseSingleGetResponseDataRelationshipsDefaultBaseLicenseSlot,
    )


T = TypeVar("T", bound="LicenseSingleGetResponseDataRelationships")


@_attrs_define
class LicenseSingleGetResponseDataRelationships:
    """
    Attributes:
        default_add_on_license_slots (LicenseSingleGetResponseDataRelationshipsDefaultAddOnLicenseSlots | Unset):
        default_base_license_slot (LicenseSingleGetResponseDataRelationshipsDefaultBaseLicenseSlot | Unset):
    """

    default_add_on_license_slots: (
        LicenseSingleGetResponseDataRelationshipsDefaultAddOnLicenseSlots
        | Unset
    ) = UNSET
    default_base_license_slot: (
        LicenseSingleGetResponseDataRelationshipsDefaultBaseLicenseSlot | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        default_add_on_license_slots: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_add_on_license_slots, Unset):
            default_add_on_license_slots = (
                self.default_add_on_license_slots.to_dict()
            )

        default_base_license_slot: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_base_license_slot, Unset):
            default_base_license_slot = (
                self.default_base_license_slot.to_dict()
            )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_add_on_license_slots is not UNSET:
            field_dict["defaultAddOnLicenseSlots"] = (
                default_add_on_license_slots
            )
        if default_base_license_slot is not UNSET:
            field_dict["defaultBaseLicenseSlot"] = default_base_license_slot

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.license_single_get_response_data_relationships_default_add_on_license_slots import (
            LicenseSingleGetResponseDataRelationshipsDefaultAddOnLicenseSlots,
        )
        from ..models.license_single_get_response_data_relationships_default_base_license_slot import (
            LicenseSingleGetResponseDataRelationshipsDefaultBaseLicenseSlot,
        )

        d = dict(src_dict)
        _default_add_on_license_slots = d.pop(
            "defaultAddOnLicenseSlots", UNSET
        )
        default_add_on_license_slots: (
            LicenseSingleGetResponseDataRelationshipsDefaultAddOnLicenseSlots
            | Unset
        )
        if isinstance(_default_add_on_license_slots, Unset):
            default_add_on_license_slots = UNSET
        else:
            default_add_on_license_slots = LicenseSingleGetResponseDataRelationshipsDefaultAddOnLicenseSlots.from_dict(
                _default_add_on_license_slots
            )

        _default_base_license_slot = d.pop("defaultBaseLicenseSlot", UNSET)
        default_base_license_slot: (
            LicenseSingleGetResponseDataRelationshipsDefaultBaseLicenseSlot
            | Unset
        )
        if isinstance(_default_base_license_slot, Unset):
            default_base_license_slot = UNSET
        else:
            default_base_license_slot = LicenseSingleGetResponseDataRelationshipsDefaultBaseLicenseSlot.from_dict(
                _default_base_license_slot
            )

        license_single_get_response_data_relationships_obj = cls(
            default_add_on_license_slots=default_add_on_license_slots,
            default_base_license_slot=default_base_license_slot,
        )

        license_single_get_response_data_relationships_obj.additional_properties = d
        return license_single_get_response_data_relationships_obj

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

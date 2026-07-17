# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LicenseSlotsListGetResponseDataItemAttributes")


@_attrs_define
class LicenseSlotsListGetResponseDataItemAttributes:
    """
    Attributes:
        configured (int | Unset):
        expiration_date (datetime.date | Unset):
        free (int | Unset):
        group (str | Unset):  Example: groupName.
        model (str | Unset):  Example: named.
        peak (int | Unset):
        total (int | Unset):
    """

    configured: int | Unset = UNSET
    expiration_date: datetime.date | Unset = UNSET
    free: int | Unset = UNSET
    group: str | Unset = UNSET
    model: str | Unset = UNSET
    peak: int | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        configured = self.configured

        expiration_date: str | Unset = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.isoformat()

        free = self.free

        group = self.group

        model = self.model

        peak = self.peak

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if configured is not UNSET:
            field_dict["configured"] = configured
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date
        if free is not UNSET:
            field_dict["free"] = free
        if group is not UNSET:
            field_dict["group"] = group
        if model is not UNSET:
            field_dict["model"] = model
        if peak is not UNSET:
            field_dict["peak"] = peak
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        configured = d.pop("configured", UNSET)

        _expiration_date = d.pop("expirationDate", UNSET)
        expiration_date: datetime.date | Unset
        if isinstance(_expiration_date, Unset):
            expiration_date = UNSET
        else:
            expiration_date = datetime.date.fromisoformat(_expiration_date)

        free = d.pop("free", UNSET)

        group = d.pop("group", UNSET)

        model = d.pop("model", UNSET)

        peak = d.pop("peak", UNSET)

        total = d.pop("total", UNSET)

        license_slots_list_get_response_data_item_attributes_obj = cls(
            configured=configured,
            expiration_date=expiration_date,
            free=free,
            group=group,
            model=model,
            peak=peak,
            total=total,
        )

        license_slots_list_get_response_data_item_attributes_obj.additional_properties = d
        return license_slots_list_get_response_data_item_attributes_obj

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

# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.set_license_request_body_license import (
    SetLicenseRequestBodyLicense,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SetLicenseRequestBody")


@_attrs_define
class SetLicenseRequestBody:
    """
    Attributes:
        concurrent (bool | Unset): Is concurrent user Example: True.
        group (str | Unset): License group Example: Department.
        license_ (SetLicenseRequestBodyLicense | Unset): User's license type
    """

    concurrent: bool | Unset = UNSET
    group: str | Unset = UNSET
    license_: SetLicenseRequestBodyLicense | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        concurrent = self.concurrent

        group = self.group

        license_: str | Unset = UNSET
        if not isinstance(self.license_, Unset):
            license_ = self.license_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if concurrent is not UNSET:
            field_dict["concurrent"] = concurrent
        if group is not UNSET:
            field_dict["group"] = group
        if license_ is not UNSET:
            field_dict["license"] = license_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        concurrent = d.pop("concurrent", UNSET)

        group = d.pop("group", UNSET)

        _license_ = d.pop("license", UNSET)
        license_: SetLicenseRequestBodyLicense | Unset
        if isinstance(_license_, Unset):
            license_ = UNSET
        else:
            license_ = SetLicenseRequestBodyLicense(_license_)

        set_license_request_body_obj = cls(
            concurrent=concurrent,
            group=group,
            license_=license_,
        )

        set_license_request_body_obj.additional_properties = d
        return set_license_request_body_obj

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

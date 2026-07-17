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
    from ..models.license_single_get_response_data_attributes_limits import (
        LicenseSingleGetResponseDataAttributesLimits,
    )


T = TypeVar("T", bound="LicenseSingleGetResponseDataAttributes")


@_attrs_define
class LicenseSingleGetResponseDataAttributes:
    """
    Attributes:
        limits (LicenseSingleGetResponseDataAttributesLimits | Unset):
    """

    limits: LicenseSingleGetResponseDataAttributesLimits | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        limits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.limits, Unset):
            limits = self.limits.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if limits is not UNSET:
            field_dict["limits"] = limits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.license_single_get_response_data_attributes_limits import (
            LicenseSingleGetResponseDataAttributesLimits,
        )

        d = dict(src_dict)
        _limits = d.pop("limits", UNSET)
        limits: LicenseSingleGetResponseDataAttributesLimits | Unset
        if isinstance(_limits, Unset):
            limits = UNSET
        else:
            limits = LicenseSingleGetResponseDataAttributesLimits.from_dict(
                _limits
            )

        license_single_get_response_data_attributes_obj = cls(
            limits=limits,
        )

        license_single_get_response_data_attributes_obj.additional_properties = d
        return license_single_get_response_data_attributes_obj

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

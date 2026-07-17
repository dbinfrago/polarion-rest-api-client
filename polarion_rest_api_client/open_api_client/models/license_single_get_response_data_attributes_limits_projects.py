# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LicenseSingleGetResponseDataAttributesLimitsProjects")


@_attrs_define
class LicenseSingleGetResponseDataAttributesLimitsProjects:
    """
    Attributes:
        current_count (int | Unset):
        limit (int | Unset):
    """

    current_count: int | Unset = UNSET
    limit: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        current_count = self.current_count

        limit = self.limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_count is not UNSET:
            field_dict["currentCount"] = current_count
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        current_count = d.pop("currentCount", UNSET)

        limit = d.pop("limit", UNSET)

        license_single_get_response_data_attributes_limits_projects_obj = cls(
            current_count=current_count,
            limit=limit,
        )

        license_single_get_response_data_attributes_limits_projects_obj.additional_properties = d
        return license_single_get_response_data_attributes_limits_projects_obj

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

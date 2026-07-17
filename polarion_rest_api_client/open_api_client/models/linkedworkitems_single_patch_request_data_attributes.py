# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkedworkitemsSinglePatchRequestDataAttributes")


@_attrs_define
class LinkedworkitemsSinglePatchRequestDataAttributes:
    """
    Attributes:
        revision (str | Unset):  Example: 1234.
        suspect (bool | Unset):
    """

    revision: str | Unset = UNSET
    suspect: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        revision = self.revision

        suspect = self.suspect

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if revision is not UNSET:
            field_dict["revision"] = revision
        if suspect is not UNSET:
            field_dict["suspect"] = suspect

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        revision = d.pop("revision", UNSET)

        suspect = d.pop("suspect", UNSET)

        linkedworkitems_single_patch_request_data_attributes_obj = cls(
            revision=revision,
            suspect=suspect,
        )

        linkedworkitems_single_patch_request_data_attributes_obj.additional_properties = d
        return linkedworkitems_single_patch_request_data_attributes_obj

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

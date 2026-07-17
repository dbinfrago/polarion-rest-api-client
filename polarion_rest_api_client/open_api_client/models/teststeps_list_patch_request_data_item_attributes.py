# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.teststeps_list_patch_request_data_item_attributes_values_item import (
        TeststepsListPatchRequestDataItemAttributesValuesItem,
    )


T = TypeVar("T", bound="TeststepsListPatchRequestDataItemAttributes")


@_attrs_define
class TeststepsListPatchRequestDataItemAttributes:
    """
    Attributes:
        keys (list[str] | Unset):
        values (list[TeststepsListPatchRequestDataItemAttributesValuesItem] | Unset):
    """

    keys: list[str] | Unset = UNSET
    values: (
        list[TeststepsListPatchRequestDataItemAttributesValuesItem] | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        keys: list[str] | Unset = UNSET
        if not isinstance(self.keys, Unset):
            keys = self.keys

        values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if keys is not UNSET:
            field_dict["keys"] = keys
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.teststeps_list_patch_request_data_item_attributes_values_item import (
            TeststepsListPatchRequestDataItemAttributesValuesItem,
        )

        d = dict(src_dict)
        keys = cast(list[str], d.pop("keys", UNSET))

        _values = d.pop("values", UNSET)
        values: (
            list[TeststepsListPatchRequestDataItemAttributesValuesItem] | Unset
        ) = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = TeststepsListPatchRequestDataItemAttributesValuesItem.from_dict(
                    values_item_data
                )

                values.append(values_item)

        teststeps_list_patch_request_data_item_attributes_obj = cls(
            keys=keys,
            values=values,
        )

        teststeps_list_patch_request_data_item_attributes_obj.additional_properties = d
        return teststeps_list_patch_request_data_item_attributes_obj

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

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
    from ..models.enumerations_single_patch_request_data_attributes_options_item import (
        EnumerationsSinglePatchRequestDataAttributesOptionsItem,
    )


T = TypeVar("T", bound="EnumerationsSinglePatchRequestDataAttributes")


@_attrs_define
class EnumerationsSinglePatchRequestDataAttributes:
    """
    Attributes:
        options (list[EnumerationsSinglePatchRequestDataAttributesOptionsItem] | Unset):
    """

    options: (
        list[EnumerationsSinglePatchRequestDataAttributesOptionsItem] | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.enumerations_single_patch_request_data_attributes_options_item import (
            EnumerationsSinglePatchRequestDataAttributesOptionsItem,
        )

        d = dict(src_dict)
        _options = d.pop("options", UNSET)
        options: (
            list[EnumerationsSinglePatchRequestDataAttributesOptionsItem]
            | Unset
        ) = UNSET
        if _options is not UNSET:
            options = []
            for options_item_data in _options:
                options_item = EnumerationsSinglePatchRequestDataAttributesOptionsItem.from_dict(
                    options_item_data
                )

                options.append(options_item)

        enumerations_single_patch_request_data_attributes_obj = cls(
            options=options,
        )

        enumerations_single_patch_request_data_attributes_obj.additional_properties = d
        return enumerations_single_patch_request_data_attributes_obj

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

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
    from ..models.enumerations_single_get_response_data_attributes_options_item import (
        EnumerationsSingleGetResponseDataAttributesOptionsItem,
    )


T = TypeVar("T", bound="EnumerationsSingleGetResponseDataAttributes")


@_attrs_define
class EnumerationsSingleGetResponseDataAttributes:
    """
    Attributes:
        enum_context (str | Unset):  Example: id.
        enum_name (str | Unset):  Example: id.
        options (list[EnumerationsSingleGetResponseDataAttributesOptionsItem] | Unset):
        target_type (str | Unset):  Example: id.
    """

    enum_context: str | Unset = UNSET
    enum_name: str | Unset = UNSET
    options: (
        list[EnumerationsSingleGetResponseDataAttributesOptionsItem] | Unset
    ) = UNSET
    target_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        enum_context = self.enum_context

        enum_name = self.enum_name

        options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)

        target_type = self.target_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enum_context is not UNSET:
            field_dict["enumContext"] = enum_context
        if enum_name is not UNSET:
            field_dict["enumName"] = enum_name
        if options is not UNSET:
            field_dict["options"] = options
        if target_type is not UNSET:
            field_dict["targetType"] = target_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.enumerations_single_get_response_data_attributes_options_item import (
            EnumerationsSingleGetResponseDataAttributesOptionsItem,
        )

        d = dict(src_dict)
        enum_context = d.pop("enumContext", UNSET)

        enum_name = d.pop("enumName", UNSET)

        _options = d.pop("options", UNSET)
        options: (
            list[EnumerationsSingleGetResponseDataAttributesOptionsItem]
            | Unset
        ) = UNSET
        if _options is not UNSET:
            options = []
            for options_item_data in _options:
                options_item = EnumerationsSingleGetResponseDataAttributesOptionsItem.from_dict(
                    options_item_data
                )

                options.append(options_item)

        target_type = d.pop("targetType", UNSET)

        enumerations_single_get_response_data_attributes_obj = cls(
            enum_context=enum_context,
            enum_name=enum_name,
            options=options,
            target_type=target_type,
        )

        enumerations_single_get_response_data_attributes_obj.additional_properties = d
        return enumerations_single_get_response_data_attributes_obj

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

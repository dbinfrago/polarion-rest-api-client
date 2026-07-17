# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkedoslcresourcesListGetResponseDataItemAttributes")


@_attrs_define
class LinkedoslcresourcesListGetResponseDataItemAttributes:
    """
    Attributes:
        label (str | Unset):  Example: Label.
        role (str | Unset):  Example: http://open-services.net/ns/cm#relatedChangeRequest.
        uri (str | Unset):  Example: URI.
    """

    label: str | Unset = UNSET
    role: str | Unset = UNSET
    uri: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        role = self.role

        uri = self.uri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label is not UNSET:
            field_dict["label"] = label
        if role is not UNSET:
            field_dict["role"] = role
        if uri is not UNSET:
            field_dict["uri"] = uri

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        label = d.pop("label", UNSET)

        role = d.pop("role", UNSET)

        uri = d.pop("uri", UNSET)

        linkedoslcresources_list_get_response_data_item_attributes_obj = cls(
            label=label,
            role=role,
            uri=uri,
        )

        linkedoslcresources_list_get_response_data_item_attributes_obj.additional_properties = d
        return linkedoslcresources_list_get_response_data_item_attributes_obj

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

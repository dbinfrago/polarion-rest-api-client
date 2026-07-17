# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MetadataSingleGetResponseDataAttributesApiProperties")


@_attrs_define
class MetadataSingleGetResponseDataAttributesApiProperties:
    """
    Attributes:
        body_size_limit (int | Unset):  Example: 2097152.
        default_page_size (int | Unset):  Example: 100.
        max_included_size (int | Unset):  Example: 500.
        max_page_size (int | Unset):  Example: 200.
        max_relationship_size (int | Unset):  Example: 100.
    """

    body_size_limit: int | Unset = UNSET
    default_page_size: int | Unset = UNSET
    max_included_size: int | Unset = UNSET
    max_page_size: int | Unset = UNSET
    max_relationship_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        body_size_limit = self.body_size_limit

        default_page_size = self.default_page_size

        max_included_size = self.max_included_size

        max_page_size = self.max_page_size

        max_relationship_size = self.max_relationship_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if body_size_limit is not UNSET:
            field_dict["bodySizeLimit"] = body_size_limit
        if default_page_size is not UNSET:
            field_dict["defaultPageSize"] = default_page_size
        if max_included_size is not UNSET:
            field_dict["maxIncludedSize"] = max_included_size
        if max_page_size is not UNSET:
            field_dict["maxPageSize"] = max_page_size
        if max_relationship_size is not UNSET:
            field_dict["maxRelationshipSize"] = max_relationship_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        body_size_limit = d.pop("bodySizeLimit", UNSET)

        default_page_size = d.pop("defaultPageSize", UNSET)

        max_included_size = d.pop("maxIncludedSize", UNSET)

        max_page_size = d.pop("maxPageSize", UNSET)

        max_relationship_size = d.pop("maxRelationshipSize", UNSET)

        metadata_single_get_response_data_attributes_api_properties_obj = cls(
            body_size_limit=body_size_limit,
            default_page_size=default_page_size,
            max_included_size=max_included_size,
            max_page_size=max_page_size,
            max_relationship_size=max_relationship_size,
        )

        metadata_single_get_response_data_attributes_api_properties_obj.additional_properties = d
        return metadata_single_get_response_data_attributes_api_properties_obj

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

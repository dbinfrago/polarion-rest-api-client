# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReuseCollectionRequestBody")


@_attrs_define
class ReuseCollectionRequestBody:
    """
    Attributes:
        target_collection_name (str | Unset): The name of the new Collection. Example: Name.
        target_project_id (str | Unset): Project where new Collection will be created. Example: MyProjectId.
    """

    target_collection_name: str | Unset = UNSET
    target_project_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        target_collection_name = self.target_collection_name

        target_project_id = self.target_project_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if target_collection_name is not UNSET:
            field_dict["targetCollectionName"] = target_collection_name
        if target_project_id is not UNSET:
            field_dict["targetProjectId"] = target_project_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target_collection_name = d.pop("targetCollectionName", UNSET)

        target_project_id = d.pop("targetProjectId", UNSET)

        reuse_collection_request_body_obj = cls(
            target_collection_name=target_collection_name,
            target_project_id=target_project_id,
        )

        reuse_collection_request_body_obj.additional_properties = d
        return reuse_collection_request_body_obj

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

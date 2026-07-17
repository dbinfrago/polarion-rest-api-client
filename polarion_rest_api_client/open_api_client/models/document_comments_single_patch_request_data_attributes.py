# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentCommentsSinglePatchRequestDataAttributes")


@_attrs_define
class DocumentCommentsSinglePatchRequestDataAttributes:
    """
    Attributes:
        resolved (bool | Unset):
    """

    resolved: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        resolved = self.resolved

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resolved is not UNSET:
            field_dict["resolved"] = resolved

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resolved = d.pop("resolved", UNSET)

        document_comments_single_patch_request_data_attributes_obj = cls(
            resolved=resolved,
        )

        document_comments_single_patch_request_data_attributes_obj.additional_properties = d
        return document_comments_single_patch_request_data_attributes_obj

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

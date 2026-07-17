# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MergeDocumentRequestBody")


@_attrs_define
class MergeDocumentRequestBody:
    """
    Attributes:
        create_baseline (bool | Unset): Specifies whether the Baseline should be created. Example: True.
        user_filter (str | Unset): Specifies the query to filter the source Work Items for the merge. Example:
            status:open.
    """

    create_baseline: bool | Unset = UNSET
    user_filter: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        create_baseline = self.create_baseline

        user_filter = self.user_filter

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if create_baseline is not UNSET:
            field_dict["createBaseline"] = create_baseline
        if user_filter is not UNSET:
            field_dict["userFilter"] = user_filter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        create_baseline = d.pop("createBaseline", UNSET)

        user_filter = d.pop("userFilter", UNSET)

        merge_document_request_body_obj = cls(
            create_baseline=create_baseline,
            user_filter=user_filter,
        )

        merge_document_request_body_obj.additional_properties = d
        return merge_document_request_body_obj

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

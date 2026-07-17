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
    from ..models.teststep_results_list_patch_request_data_item_attributes_comment import (
        TeststepResultsListPatchRequestDataItemAttributesComment,
    )


T = TypeVar("T", bound="TeststepResultsListPatchRequestDataItemAttributes")


@_attrs_define
class TeststepResultsListPatchRequestDataItemAttributes:
    """
    Attributes:
        comment (TeststepResultsListPatchRequestDataItemAttributesComment | Unset):
        result (str | Unset):  Example: passed.
    """

    comment: (
        TeststepResultsListPatchRequestDataItemAttributesComment | Unset
    ) = UNSET
    result: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        comment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.comment, Unset):
            comment = self.comment.to_dict()

        result = self.result

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comment is not UNSET:
            field_dict["comment"] = comment
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.teststep_results_list_patch_request_data_item_attributes_comment import (
            TeststepResultsListPatchRequestDataItemAttributesComment,
        )

        d = dict(src_dict)
        _comment = d.pop("comment", UNSET)
        comment: (
            TeststepResultsListPatchRequestDataItemAttributesComment | Unset
        )
        if isinstance(_comment, Unset):
            comment = UNSET
        else:
            comment = TeststepResultsListPatchRequestDataItemAttributesComment.from_dict(
                _comment
            )

        result = d.pop("result", UNSET)

        teststep_results_list_patch_request_data_item_attributes_obj = cls(
            comment=comment,
            result=result,
        )

        teststep_results_list_patch_request_data_item_attributes_obj.additional_properties = d
        return teststep_results_list_patch_request_data_item_attributes_obj

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

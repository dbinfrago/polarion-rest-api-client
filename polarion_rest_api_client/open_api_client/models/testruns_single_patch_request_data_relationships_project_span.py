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
    from ..models.testruns_single_patch_request_data_relationships_project_span_data_item import (
        TestrunsSinglePatchRequestDataRelationshipsProjectSpanDataItem,
    )


T = TypeVar(
    "T", bound="TestrunsSinglePatchRequestDataRelationshipsProjectSpan"
)


@_attrs_define
class TestrunsSinglePatchRequestDataRelationshipsProjectSpan:
    """
    Attributes:
        data (list[TestrunsSinglePatchRequestDataRelationshipsProjectSpanDataItem] | Unset):
    """

    data: (
        list[TestrunsSinglePatchRequestDataRelationshipsProjectSpanDataItem]
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.testruns_single_patch_request_data_relationships_project_span_data_item import (
            TestrunsSinglePatchRequestDataRelationshipsProjectSpanDataItem,
        )

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: (
            list[
                TestrunsSinglePatchRequestDataRelationshipsProjectSpanDataItem
            ]
            | Unset
        ) = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = TestrunsSinglePatchRequestDataRelationshipsProjectSpanDataItem.from_dict(
                    data_item_data
                )

                data.append(data_item)

        testruns_single_patch_request_data_relationships_project_span_obj = (
            cls(
                data=data,
            )
        )

        testruns_single_patch_request_data_relationships_project_span_obj.additional_properties = d
        return (
            testruns_single_patch_request_data_relationships_project_span_obj
        )

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

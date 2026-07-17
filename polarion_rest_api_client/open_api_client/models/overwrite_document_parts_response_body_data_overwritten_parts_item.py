# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="OverwriteDocumentPartsResponseBodyDataOverwrittenPartsItem"
)


@_attrs_define
class OverwriteDocumentPartsResponseBodyDataOverwrittenPartsItem:
    """
    Attributes:
        new_part_id (str | Unset): New Part ID after overwrite operation. Example:
            MyProjectId/MySpaceId/MyDocumentId/workitem_MyWorkItemId.
        old_part_id (str | Unset): Original Part ID before overwrite operation. Example:
            MyProjectId/MySpaceId/MyDocumentId/workitem_MyWorkItemId.
    """

    new_part_id: str | Unset = UNSET
    old_part_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        new_part_id = self.new_part_id

        old_part_id = self.old_part_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if new_part_id is not UNSET:
            field_dict["newPartId"] = new_part_id
        if old_part_id is not UNSET:
            field_dict["oldPartId"] = old_part_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        new_part_id = d.pop("newPartId", UNSET)

        old_part_id = d.pop("oldPartId", UNSET)

        overwrite_document_parts_response_body_data_overwritten_parts_item_obj = cls(
            new_part_id=new_part_id,
            old_part_id=old_part_id,
        )

        overwrite_document_parts_response_body_data_overwritten_parts_item_obj.additional_properties = d
        return overwrite_document_parts_response_body_data_overwritten_parts_item_obj

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

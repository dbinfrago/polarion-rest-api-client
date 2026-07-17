# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MoveWorkItemsToDocumentRequestBodyWorkItemGroupsItem")


@_attrs_define
class MoveWorkItemsToDocumentRequestBodyWorkItemGroupsItem:
    """
    Attributes:
        next_part (str | Unset):  Example: MyProjectId/MySpaceId/MyDocumentId/workitem_MyWorkItemId.
        previous_part (str | Unset):  Example: MyProjectId/MySpaceId/MyDocumentId/workitem_MyWorkItemId.
        work_item_ids (list[str] | Unset):  Example: ['MyProjectId/WI-123', 'MyProjectId/WI-124'].
    """

    next_part: str | Unset = UNSET
    previous_part: str | Unset = UNSET
    work_item_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        next_part = self.next_part

        previous_part = self.previous_part

        work_item_ids: list[str] | Unset = UNSET
        if not isinstance(self.work_item_ids, Unset):
            work_item_ids = self.work_item_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if next_part is not UNSET:
            field_dict["nextPart"] = next_part
        if previous_part is not UNSET:
            field_dict["previousPart"] = previous_part
        if work_item_ids is not UNSET:
            field_dict["workItemIds"] = work_item_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        next_part = d.pop("nextPart", UNSET)

        previous_part = d.pop("previousPart", UNSET)

        work_item_ids = cast(list[str], d.pop("workItemIds", UNSET))

        move_work_items_to_document_request_body_work_item_groups_item_obj = (
            cls(
                next_part=next_part,
                previous_part=previous_part,
                work_item_ids=work_item_ids,
            )
        )

        move_work_items_to_document_request_body_work_item_groups_item_obj.additional_properties = d
        return (
            move_work_items_to_document_request_body_work_item_groups_item_obj
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

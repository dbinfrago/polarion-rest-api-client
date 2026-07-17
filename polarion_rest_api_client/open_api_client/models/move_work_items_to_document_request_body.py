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
    from ..models.move_work_items_to_document_request_body_work_item_groups_item import (
        MoveWorkItemsToDocumentRequestBodyWorkItemGroupsItem,
    )


T = TypeVar("T", bound="MoveWorkItemsToDocumentRequestBody")


@_attrs_define
class MoveWorkItemsToDocumentRequestBody:
    """
    Attributes:
        target_document (str | Unset):  Example: MyProjectId/MySpaceId/MyDocumentId.
        work_item_groups (list[MoveWorkItemsToDocumentRequestBodyWorkItemGroupsItem] | Unset):  Example:
            [{'previousPart': 'MyProjectId/MySpaceId/MyDocumentId/workitem_MyWorkItemId', 'workItemIds':
            ['MyProjectId/WI-123', 'MyProjectId/WI-124']}, {'nextPart':
            'MyProjectId/MySpaceId/MyDocumentId/workitem_MyWorkItemId', 'workItemIds': ['MyProjectId/WI-125']}].
    """

    target_document: str | Unset = UNSET
    work_item_groups: (
        list[MoveWorkItemsToDocumentRequestBodyWorkItemGroupsItem] | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        target_document = self.target_document

        work_item_groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.work_item_groups, Unset):
            work_item_groups = []
            for work_item_groups_item_data in self.work_item_groups:
                work_item_groups_item = work_item_groups_item_data.to_dict()
                work_item_groups.append(work_item_groups_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if target_document is not UNSET:
            field_dict["targetDocument"] = target_document
        if work_item_groups is not UNSET:
            field_dict["workItemGroups"] = work_item_groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.move_work_items_to_document_request_body_work_item_groups_item import (
            MoveWorkItemsToDocumentRequestBodyWorkItemGroupsItem,
        )

        d = dict(src_dict)
        target_document = d.pop("targetDocument", UNSET)

        _work_item_groups = d.pop("workItemGroups", UNSET)
        work_item_groups: (
            list[MoveWorkItemsToDocumentRequestBodyWorkItemGroupsItem] | Unset
        ) = UNSET
        if _work_item_groups is not UNSET:
            work_item_groups = []
            for work_item_groups_item_data in _work_item_groups:
                work_item_groups_item = MoveWorkItemsToDocumentRequestBodyWorkItemGroupsItem.from_dict(
                    work_item_groups_item_data
                )

                work_item_groups.append(work_item_groups_item)

        move_work_items_to_document_request_body_obj = cls(
            target_document=target_document,
            work_item_groups=work_item_groups,
        )

        move_work_items_to_document_request_body_obj.additional_properties = d
        return move_work_items_to_document_request_body_obj

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

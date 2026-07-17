# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MoveWorkItemToDocumentRequestBody")


@_attrs_define
class MoveWorkItemToDocumentRequestBody:
    """
    Attributes:
        next_part (str | Unset):  Example: MyProjectId/MySpaceId/MyDocumentId/workitem_MyWorkItemId.
        previous_part (str | Unset):  Example: MyProjectId/MySpaceId/MyDocumentId/workitem_MyWorkItemId.
        target_document (str | Unset):  Example: MyProjectId/MySpaceId/MyDocumentId.
    """

    next_part: str | Unset = UNSET
    previous_part: str | Unset = UNSET
    target_document: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        next_part = self.next_part

        previous_part = self.previous_part

        target_document = self.target_document

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if next_part is not UNSET:
            field_dict["nextPart"] = next_part
        if previous_part is not UNSET:
            field_dict["previousPart"] = previous_part
        if target_document is not UNSET:
            field_dict["targetDocument"] = target_document

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        next_part = d.pop("nextPart", UNSET)

        previous_part = d.pop("previousPart", UNSET)

        target_document = d.pop("targetDocument", UNSET)

        move_work_item_to_document_request_body_obj = cls(
            next_part=next_part,
            previous_part=previous_part,
            target_document=target_document,
        )

        move_work_item_to_document_request_body_obj.additional_properties = d
        return move_work_item_to_document_request_body_obj

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

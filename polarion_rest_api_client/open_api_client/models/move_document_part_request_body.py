# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MoveDocumentPartRequestBody")


@_attrs_define
class MoveDocumentPartRequestBody:
    """
    Attributes:
        after (str | Unset):  Example: MyProjectId/MySpaceId/MyDocumentId/workitem_MyWorkItemId.
        before (str | Unset):  Example: MyProjectId/MySpaceId/MyDocumentId/workitem_MyWorkItemId.
        parent (str | Unset):  Example: MyProjectId/MySpaceId/MyDocumentId/workitem_MyWorkItemId.
    """

    after: str | Unset = UNSET
    before: str | Unset = UNSET
    parent: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        after = self.after

        before = self.before

        parent = self.parent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if after is not UNSET:
            field_dict["after"] = after
        if before is not UNSET:
            field_dict["before"] = before
        if parent is not UNSET:
            field_dict["parent"] = parent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        after = d.pop("after", UNSET)

        before = d.pop("before", UNSET)

        parent = d.pop("parent", UNSET)

        move_document_part_request_body_obj = cls(
            after=after,
            before=before,
            parent=parent,
        )

        move_document_part_request_body_obj.additional_properties = d
        return move_document_part_request_body_obj

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

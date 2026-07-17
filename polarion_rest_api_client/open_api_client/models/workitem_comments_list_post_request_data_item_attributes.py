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
    from ..models.workitem_comments_list_post_request_data_item_attributes_text import (
        WorkitemCommentsListPostRequestDataItemAttributesText,
    )


T = TypeVar("T", bound="WorkitemCommentsListPostRequestDataItemAttributes")


@_attrs_define
class WorkitemCommentsListPostRequestDataItemAttributes:
    """
    Attributes:
        resolved (bool | Unset):
        text (WorkitemCommentsListPostRequestDataItemAttributesText | Unset):
        title (str | Unset):  Example: Title.
    """

    resolved: bool | Unset = UNSET
    text: WorkitemCommentsListPostRequestDataItemAttributesText | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        resolved = self.resolved

        text: dict[str, Any] | Unset = UNSET
        if not isinstance(self.text, Unset):
            text = self.text.to_dict()

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resolved is not UNSET:
            field_dict["resolved"] = resolved
        if text is not UNSET:
            field_dict["text"] = text
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workitem_comments_list_post_request_data_item_attributes_text import (
            WorkitemCommentsListPostRequestDataItemAttributesText,
        )

        d = dict(src_dict)
        resolved = d.pop("resolved", UNSET)

        _text = d.pop("text", UNSET)
        text: WorkitemCommentsListPostRequestDataItemAttributesText | Unset
        if isinstance(_text, Unset):
            text = UNSET
        else:
            text = WorkitemCommentsListPostRequestDataItemAttributesText.from_dict(
                _text
            )

        title = d.pop("title", UNSET)

        workitem_comments_list_post_request_data_item_attributes_obj = cls(
            resolved=resolved,
            text=text,
            title=title,
        )

        workitem_comments_list_post_request_data_item_attributes_obj.additional_properties = d
        return workitem_comments_list_post_request_data_item_attributes_obj

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

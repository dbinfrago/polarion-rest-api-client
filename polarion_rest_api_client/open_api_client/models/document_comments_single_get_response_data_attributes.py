# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import datetime
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
    from ..models.document_comments_single_get_response_data_attributes_text import (
        DocumentCommentsSingleGetResponseDataAttributesText,
    )


T = TypeVar("T", bound="DocumentCommentsSingleGetResponseDataAttributes")


@_attrs_define
class DocumentCommentsSingleGetResponseDataAttributes:
    """
    Attributes:
        created (datetime.datetime | Unset):  Example: 1970-01-01T00:00:00Z.
        id (str | Unset):  Example: MyCommentId.
        resolved (bool | Unset):
        text (DocumentCommentsSingleGetResponseDataAttributesText | Unset):
    """

    created: datetime.datetime | Unset = UNSET
    id: str | Unset = UNSET
    resolved: bool | Unset = UNSET
    text: DocumentCommentsSingleGetResponseDataAttributesText | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        id = self.id

        resolved = self.resolved

        text: dict[str, Any] | Unset = UNSET
        if not isinstance(self.text, Unset):
            text = self.text.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if id is not UNSET:
            field_dict["id"] = id
        if resolved is not UNSET:
            field_dict["resolved"] = resolved
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.document_comments_single_get_response_data_attributes_text import (
            DocumentCommentsSingleGetResponseDataAttributesText,
        )

        d = dict(src_dict)
        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = datetime.datetime.fromisoformat(_created)

        id = d.pop("id", UNSET)

        resolved = d.pop("resolved", UNSET)

        _text = d.pop("text", UNSET)
        text: DocumentCommentsSingleGetResponseDataAttributesText | Unset
        if isinstance(_text, Unset):
            text = UNSET
        else:
            text = (
                DocumentCommentsSingleGetResponseDataAttributesText.from_dict(
                    _text
                )
            )

        document_comments_single_get_response_data_attributes_obj = cls(
            created=created,
            id=id,
            resolved=resolved,
            text=text,
        )

        document_comments_single_get_response_data_attributes_obj.additional_properties = d
        return document_comments_single_get_response_data_attributes_obj

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

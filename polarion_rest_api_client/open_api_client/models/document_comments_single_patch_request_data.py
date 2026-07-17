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

from ..models.document_comments_single_patch_request_data_type import (
    DocumentCommentsSinglePatchRequestDataType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_comments_single_patch_request_data_attributes import (
        DocumentCommentsSinglePatchRequestDataAttributes,
    )


T = TypeVar("T", bound="DocumentCommentsSinglePatchRequestData")


@_attrs_define
class DocumentCommentsSinglePatchRequestData:
    """
    Attributes:
        type_ (DocumentCommentsSinglePatchRequestDataType | Unset):
        id (str | Unset):  Example: MyProjectId/MySpaceId/MyDocumentId/MyCommentId.
        attributes (DocumentCommentsSinglePatchRequestDataAttributes | Unset):
    """

    type_: DocumentCommentsSinglePatchRequestDataType | Unset = UNSET
    id: str | Unset = UNSET
    attributes: DocumentCommentsSinglePatchRequestDataAttributes | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        id = self.id

        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if id is not UNSET:
            field_dict["id"] = id
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.document_comments_single_patch_request_data_attributes import (
            DocumentCommentsSinglePatchRequestDataAttributes,
        )

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: DocumentCommentsSinglePatchRequestDataType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DocumentCommentsSinglePatchRequestDataType(_type_)

        id = d.pop("id", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: DocumentCommentsSinglePatchRequestDataAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = (
                DocumentCommentsSinglePatchRequestDataAttributes.from_dict(
                    _attributes
                )
            )

        document_comments_single_patch_request_data_obj = cls(
            type_=type_,
            id=id,
            attributes=attributes,
        )

        document_comments_single_patch_request_data_obj.additional_properties = d
        return document_comments_single_patch_request_data_obj

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

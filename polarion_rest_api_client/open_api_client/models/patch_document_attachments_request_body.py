# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import json
from collections.abc import Mapping
from io import BytesIO
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, FileTypes, Unset

if TYPE_CHECKING:
    from ..models.document_attachments_single_patch_request import (
        DocumentAttachmentsSinglePatchRequest,
    )


T = TypeVar("T", bound="PatchDocumentAttachmentsRequestBody")


@_attrs_define
class PatchDocumentAttachmentsRequestBody:
    """
    Attributes:
        resource (DocumentAttachmentsSinglePatchRequest):
        content (File | Unset): attachments content
    """

    resource: DocumentAttachmentsSinglePatchRequest
    content: File | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        resource = self.resource.to_dict()

        content: FileTypes | Unset = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_tuple()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource": resource,
            }
        )
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(
            (
                "resource",
                (
                    None,
                    json.dumps(self.resource.to_dict()).encode(),
                    "text/plain",
                ),
            )
        )

        if not isinstance(self.content, Unset):
            files.append(("content", self.content.to_tuple()))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.document_attachments_single_patch_request import (
            DocumentAttachmentsSinglePatchRequest,
        )

        d = dict(src_dict)
        resource = DocumentAttachmentsSinglePatchRequest.from_dict(
            d.pop("resource")
        )

        _content = d.pop("content", UNSET)
        content: File | Unset
        if isinstance(_content, Unset):
            content = UNSET
        else:
            content = File(payload=BytesIO(_content))

        patch_document_attachments_request_body_obj = cls(
            resource=resource,
            content=content,
        )

        patch_document_attachments_request_body_obj.additional_properties = d
        return patch_document_attachments_request_body_obj

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

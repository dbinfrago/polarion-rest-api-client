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
    from ..models.teststepresult_attachments_list_post_request import (
        TeststepresultAttachmentsListPostRequest,
    )


T = TypeVar("T", bound="PostTestStepResultAttachmentsRequestBody")


@_attrs_define
class PostTestStepResultAttachmentsRequestBody:
    """
    Attributes:
        files (list[File] | Unset):
        resource (TeststepresultAttachmentsListPostRequest | Unset):
    """

    files: list[File] | Unset = UNSET
    resource: TeststepresultAttachmentsListPostRequest | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        files: list[FileTypes] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_tuple()

                files.append(files_item)

        resource: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resource, Unset):
            resource = self.resource.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if files is not UNSET:
            field_dict["files"] = files
        if resource is not UNSET:
            field_dict["resource"] = resource

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.files, Unset):
            for files_item_element in self.files:
                files.append(("files", files_item_element.to_tuple()))

        if not isinstance(self.resource, Unset):
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

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.teststepresult_attachments_list_post_request import (
            TeststepresultAttachmentsListPostRequest,
        )

        d = dict(src_dict)
        _files = d.pop("files", UNSET)
        files: list[File] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = File(payload=BytesIO(files_item_data))

                files.append(files_item)

        _resource = d.pop("resource", UNSET)
        resource: TeststepresultAttachmentsListPostRequest | Unset
        if isinstance(_resource, Unset):
            resource = UNSET
        else:
            resource = TeststepresultAttachmentsListPostRequest.from_dict(
                _resource
            )

        post_test_step_result_attachments_request_body_obj = cls(
            files=files,
            resource=resource,
        )

        post_test_step_result_attachments_request_body_obj.additional_properties = d
        return post_test_step_result_attachments_request_body_obj

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

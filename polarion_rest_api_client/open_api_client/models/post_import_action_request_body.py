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
from ..types import UNSET, File, Unset

if TYPE_CHECKING:
    from ..models.import_test_results_request_body import (
        ImportTestResultsRequestBody,
    )


T = TypeVar("T", bound="PostImportActionRequestBody")


@_attrs_define
class PostImportActionRequestBody:
    """
    Attributes:
        file (File): excel file content
        resource (ImportTestResultsRequestBody | Unset):
    """

    file: File
    resource: ImportTestResultsRequestBody | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        file = self.file.to_tuple()

        resource: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resource, Unset):
            resource = self.resource.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
            }
        )
        if resource is not UNSET:
            field_dict["resource"] = resource

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("file", self.file.to_tuple()))

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
        from ..models.import_test_results_request_body import (
            ImportTestResultsRequestBody,
        )

        d = dict(src_dict)
        file = File(payload=BytesIO(d.pop("file")))

        _resource = d.pop("resource", UNSET)
        resource: ImportTestResultsRequestBody | Unset
        if isinstance(_resource, Unset):
            resource = UNSET
        else:
            resource = ImportTestResultsRequestBody.from_dict(_resource)

        post_import_action_request_body_obj = cls(
            file=file,
            resource=resource,
        )

        post_import_action_request_body_obj.additional_properties = d
        return post_import_action_request_body_obj

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

# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RevisionsSingleGetResponseDataAttributes")


@_attrs_define
class RevisionsSingleGetResponseDataAttributes:
    """
    Attributes:
        created (datetime.datetime | Unset):  Example: 1970-01-01T00:00:00Z.
        id (str | Unset):
        internal_commit (bool | Unset):
        message (str | Unset):  Example: Message.
        repository_name (str | Unset):  Example: Repository name.
    """

    created: datetime.datetime | Unset = UNSET
    id: str | Unset = UNSET
    internal_commit: bool | Unset = UNSET
    message: str | Unset = UNSET
    repository_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        id = self.id

        internal_commit = self.internal_commit

        message = self.message

        repository_name = self.repository_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if id is not UNSET:
            field_dict["id"] = id
        if internal_commit is not UNSET:
            field_dict["internalCommit"] = internal_commit
        if message is not UNSET:
            field_dict["message"] = message
        if repository_name is not UNSET:
            field_dict["repositoryName"] = repository_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = datetime.datetime.fromisoformat(_created)

        id = d.pop("id", UNSET)

        internal_commit = d.pop("internalCommit", UNSET)

        message = d.pop("message", UNSET)

        repository_name = d.pop("repositoryName", UNSET)

        revisions_single_get_response_data_attributes_obj = cls(
            created=created,
            id=id,
            internal_commit=internal_commit,
            message=message,
            repository_name=repository_name,
        )

        revisions_single_get_response_data_attributes_obj.additional_properties = d
        return revisions_single_get_response_data_attributes_obj

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

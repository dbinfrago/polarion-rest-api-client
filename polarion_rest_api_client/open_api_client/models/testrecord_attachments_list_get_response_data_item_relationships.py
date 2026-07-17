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
    from ..models.testrecord_attachments_list_get_response_data_item_relationships_author import (
        TestrecordAttachmentsListGetResponseDataItemRelationshipsAuthor,
    )
    from ..models.testrecord_attachments_list_get_response_data_item_relationships_project import (
        TestrecordAttachmentsListGetResponseDataItemRelationshipsProject,
    )


T = TypeVar(
    "T", bound="TestrecordAttachmentsListGetResponseDataItemRelationships"
)


@_attrs_define
class TestrecordAttachmentsListGetResponseDataItemRelationships:
    """
    Attributes:
        author (TestrecordAttachmentsListGetResponseDataItemRelationshipsAuthor | Unset):
        project (TestrecordAttachmentsListGetResponseDataItemRelationshipsProject | Unset):
    """

    author: (
        TestrecordAttachmentsListGetResponseDataItemRelationshipsAuthor | Unset
    ) = UNSET
    project: (
        TestrecordAttachmentsListGetResponseDataItemRelationshipsProject
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        author: dict[str, Any] | Unset = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        project: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if author is not UNSET:
            field_dict["author"] = author
        if project is not UNSET:
            field_dict["project"] = project

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.testrecord_attachments_list_get_response_data_item_relationships_author import (
            TestrecordAttachmentsListGetResponseDataItemRelationshipsAuthor,
        )
        from ..models.testrecord_attachments_list_get_response_data_item_relationships_project import (
            TestrecordAttachmentsListGetResponseDataItemRelationshipsProject,
        )

        d = dict(src_dict)
        _author = d.pop("author", UNSET)
        author: (
            TestrecordAttachmentsListGetResponseDataItemRelationshipsAuthor
            | Unset
        )
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = TestrecordAttachmentsListGetResponseDataItemRelationshipsAuthor.from_dict(
                _author
            )

        _project = d.pop("project", UNSET)
        project: (
            TestrecordAttachmentsListGetResponseDataItemRelationshipsProject
            | Unset
        )
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = TestrecordAttachmentsListGetResponseDataItemRelationshipsProject.from_dict(
                _project
            )

        testrecord_attachments_list_get_response_data_item_relationships_obj = cls(
            author=author,
            project=project,
        )

        testrecord_attachments_list_get_response_data_item_relationships_obj.additional_properties = d
        return testrecord_attachments_list_get_response_data_item_relationships_obj

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

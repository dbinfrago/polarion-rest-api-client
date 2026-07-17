# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.testrun_comments_single_get_response_data_relationships_parent_comment_data_type import (
    TestrunCommentsSingleGetResponseDataRelationshipsParentCommentDataType,
)
from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="TestrunCommentsSingleGetResponseDataRelationshipsParentCommentData",
)


@_attrs_define
class TestrunCommentsSingleGetResponseDataRelationshipsParentCommentData:
    """
    Attributes:
        id (str | Unset):  Example: MyProjectId/MyTestRunId/MyCommentId.
        revision (str | Unset):  Example: 1234.
        type_ (TestrunCommentsSingleGetResponseDataRelationshipsParentCommentDataType | Unset):
    """

    id: str | Unset = UNSET
    revision: str | Unset = UNSET
    type_: (
        TestrunCommentsSingleGetResponseDataRelationshipsParentCommentDataType
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        revision = self.revision

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if revision is not UNSET:
            field_dict["revision"] = revision
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        revision = d.pop("revision", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: (
            TestrunCommentsSingleGetResponseDataRelationshipsParentCommentDataType
            | Unset
        )
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = TestrunCommentsSingleGetResponseDataRelationshipsParentCommentDataType(
                _type_
            )

        testrun_comments_single_get_response_data_relationships_parent_comment_data_obj = cls(
            id=id,
            revision=revision,
            type_=type_,
        )

        testrun_comments_single_get_response_data_relationships_parent_comment_data_obj.additional_properties = d
        return testrun_comments_single_get_response_data_relationships_parent_comment_data_obj

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

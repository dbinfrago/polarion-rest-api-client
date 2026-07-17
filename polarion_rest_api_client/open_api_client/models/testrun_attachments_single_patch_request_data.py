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

from ..models.testrun_attachments_single_patch_request_data_type import (
    TestrunAttachmentsSinglePatchRequestDataType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.testrun_attachments_single_patch_request_data_attributes import (
        TestrunAttachmentsSinglePatchRequestDataAttributes,
    )


T = TypeVar("T", bound="TestrunAttachmentsSinglePatchRequestData")


@_attrs_define
class TestrunAttachmentsSinglePatchRequestData:
    """
    Attributes:
        type_ (TestrunAttachmentsSinglePatchRequestDataType | Unset):
        id (str | Unset):  Example: MyProjectId/MyTestRunId/MyAttachmentId.
        attributes (TestrunAttachmentsSinglePatchRequestDataAttributes | Unset):
    """

    type_: TestrunAttachmentsSinglePatchRequestDataType | Unset = UNSET
    id: str | Unset = UNSET
    attributes: TestrunAttachmentsSinglePatchRequestDataAttributes | Unset = (
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
        from ..models.testrun_attachments_single_patch_request_data_attributes import (
            TestrunAttachmentsSinglePatchRequestDataAttributes,
        )

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: TestrunAttachmentsSinglePatchRequestDataType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = TestrunAttachmentsSinglePatchRequestDataType(_type_)

        id = d.pop("id", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: TestrunAttachmentsSinglePatchRequestDataAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = (
                TestrunAttachmentsSinglePatchRequestDataAttributes.from_dict(
                    _attributes
                )
            )

        testrun_attachments_single_patch_request_data_obj = cls(
            type_=type_,
            id=id,
            attributes=attributes,
        )

        testrun_attachments_single_patch_request_data_obj.additional_properties = d
        return testrun_attachments_single_patch_request_data_obj

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

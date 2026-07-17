# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.jobs_single_post_response_data_attributes_status_type import (
    JobsSinglePostResponseDataAttributesStatusType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="JobsSinglePostResponseDataAttributesStatus")


@_attrs_define
class JobsSinglePostResponseDataAttributesStatus:
    """
    Attributes:
        message (str | Unset):  Example: message.
        type_ (JobsSinglePostResponseDataAttributesStatusType | Unset):
    """

    message: str | Unset = UNSET
    type_: JobsSinglePostResponseDataAttributesStatusType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: JobsSinglePostResponseDataAttributesStatusType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = JobsSinglePostResponseDataAttributesStatusType(_type_)

        jobs_single_post_response_data_attributes_status_obj = cls(
            message=message,
            type_=type_,
        )

        jobs_single_post_response_data_attributes_status_obj.additional_properties = d
        return jobs_single_post_response_data_attributes_status_obj

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

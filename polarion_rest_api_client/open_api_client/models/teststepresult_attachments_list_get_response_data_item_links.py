# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TeststepresultAttachmentsListGetResponseDataItemLinks")


@_attrs_define
class TeststepresultAttachmentsListGetResponseDataItemLinks:
    """
    Attributes:
        content (str | Unset):  Example: server-host-name/application-path/projects/MyProjectId/testruns/MyTestRunId/tes
            trecords/MyProjectId/MyTestcaseId/0/teststepresults/1/attachments/MyAttachmentId/content.
        self_ (str | Unset):  Example: server-host-name/application-path/projects/MyProjectId/testruns/MyTestRunId/testr
            ecords/MyProjectId/MyTestcaseId/0/teststepresults/1/attachments/MyAttachmentId.
    """

    content: str | Unset = UNSET
    self_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        self_ = self.self_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if self_ is not UNSET:
            field_dict["self"] = self_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = d.pop("content", UNSET)

        self_ = d.pop("self", UNSET)

        teststepresult_attachments_list_get_response_data_item_links_obj = cls(
            content=content,
            self_=self_,
        )

        teststepresult_attachments_list_get_response_data_item_links_obj.additional_properties = d
        return teststepresult_attachments_list_get_response_data_item_links_obj

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

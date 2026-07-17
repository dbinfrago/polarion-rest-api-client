# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.documents_list_get_response_data_item_attributes_home_page_content_type import (
    DocumentsListGetResponseDataItemAttributesHomePageContentType,
)
from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="DocumentsListGetResponseDataItemAttributesHomePageContent"
)


@_attrs_define
class DocumentsListGetResponseDataItemAttributesHomePageContent:
    """
    Attributes:
        type_ (DocumentsListGetResponseDataItemAttributesHomePageContentType | Unset):
        value (str | Unset):  Example: My text value.
    """

    type_: (
        DocumentsListGetResponseDataItemAttributesHomePageContentType | Unset
    ) = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: (
            DocumentsListGetResponseDataItemAttributesHomePageContentType
            | Unset
        )
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = (
                DocumentsListGetResponseDataItemAttributesHomePageContentType(
                    _type_
                )
            )

        value = d.pop("value", UNSET)

        documents_list_get_response_data_item_attributes_home_page_content_obj = cls(
            type_=type_,
            value=value,
        )

        documents_list_get_response_data_item_attributes_home_page_content_obj.additional_properties = d
        return documents_list_get_response_data_item_attributes_home_page_content_obj

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

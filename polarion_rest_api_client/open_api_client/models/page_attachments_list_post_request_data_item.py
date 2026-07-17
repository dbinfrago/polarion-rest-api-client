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

from ..models.page_attachments_list_post_request_data_item_type import (
    PageAttachmentsListPostRequestDataItemType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.page_attachments_list_post_request_data_item_attributes import (
        PageAttachmentsListPostRequestDataItemAttributes,
    )


T = TypeVar("T", bound="PageAttachmentsListPostRequestDataItem")


@_attrs_define
class PageAttachmentsListPostRequestDataItem:
    """
    Attributes:
        type_ (PageAttachmentsListPostRequestDataItemType | Unset):
        attributes (PageAttachmentsListPostRequestDataItemAttributes | Unset):
        lid (str | Unset):
    """

    type_: PageAttachmentsListPostRequestDataItemType | Unset = UNSET
    attributes: PageAttachmentsListPostRequestDataItemAttributes | Unset = (
        UNSET
    )
    lid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        lid = self.lid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if lid is not UNSET:
            field_dict["lid"] = lid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.page_attachments_list_post_request_data_item_attributes import (
            PageAttachmentsListPostRequestDataItemAttributes,
        )

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: PageAttachmentsListPostRequestDataItemType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = PageAttachmentsListPostRequestDataItemType(_type_)

        _attributes = d.pop("attributes", UNSET)
        attributes: PageAttachmentsListPostRequestDataItemAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = (
                PageAttachmentsListPostRequestDataItemAttributes.from_dict(
                    _attributes
                )
            )

        lid = d.pop("lid", UNSET)

        page_attachments_list_post_request_data_item_obj = cls(
            type_=type_,
            attributes=attributes,
            lid=lid,
        )

        page_attachments_list_post_request_data_item_obj.additional_properties = d
        return page_attachments_list_post_request_data_item_obj

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

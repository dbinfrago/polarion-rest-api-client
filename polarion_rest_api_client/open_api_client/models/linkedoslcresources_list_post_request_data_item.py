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

from ..models.linkedoslcresources_list_post_request_data_item_type import (
    LinkedoslcresourcesListPostRequestDataItemType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.linkedoslcresources_list_post_request_data_item_attributes import (
        LinkedoslcresourcesListPostRequestDataItemAttributes,
    )


T = TypeVar("T", bound="LinkedoslcresourcesListPostRequestDataItem")


@_attrs_define
class LinkedoslcresourcesListPostRequestDataItem:
    """
    Attributes:
        type_ (LinkedoslcresourcesListPostRequestDataItemType | Unset):
        attributes (LinkedoslcresourcesListPostRequestDataItemAttributes | Unset):
    """

    type_: LinkedoslcresourcesListPostRequestDataItemType | Unset = UNSET
    attributes: (
        LinkedoslcresourcesListPostRequestDataItemAttributes | Unset
    ) = UNSET
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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linkedoslcresources_list_post_request_data_item_attributes import (
            LinkedoslcresourcesListPostRequestDataItemAttributes,
        )

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: LinkedoslcresourcesListPostRequestDataItemType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = LinkedoslcresourcesListPostRequestDataItemType(_type_)

        _attributes = d.pop("attributes", UNSET)
        attributes: (
            LinkedoslcresourcesListPostRequestDataItemAttributes | Unset
        )
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = (
                LinkedoslcresourcesListPostRequestDataItemAttributes.from_dict(
                    _attributes
                )
            )

        linkedoslcresources_list_post_request_data_item_obj = cls(
            type_=type_,
            attributes=attributes,
        )

        linkedoslcresources_list_post_request_data_item_obj.additional_properties = d
        return linkedoslcresources_list_post_request_data_item_obj

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

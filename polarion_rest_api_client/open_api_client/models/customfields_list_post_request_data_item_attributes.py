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
    from ..models.customfields_list_post_request_data_item_attributes_fields_item import (
        CustomfieldsListPostRequestDataItemAttributesFieldsItem,
    )


T = TypeVar("T", bound="CustomfieldsListPostRequestDataItemAttributes")


@_attrs_define
class CustomfieldsListPostRequestDataItemAttributes:
    """
    Attributes:
        fields (list[CustomfieldsListPostRequestDataItemAttributesFieldsItem] | Unset):
        resource_type (str | Unset):  Example: id.
        target_type (str | Unset):  Example: id.
    """

    fields: (
        list[CustomfieldsListPostRequestDataItemAttributesFieldsItem] | Unset
    ) = UNSET
    resource_type: str | Unset = UNSET
    target_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)

        resource_type = self.resource_type

        target_type = self.target_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fields is not UNSET:
            field_dict["fields"] = fields
        if resource_type is not UNSET:
            field_dict["resourceType"] = resource_type
        if target_type is not UNSET:
            field_dict["targetType"] = target_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.customfields_list_post_request_data_item_attributes_fields_item import (
            CustomfieldsListPostRequestDataItemAttributesFieldsItem,
        )

        d = dict(src_dict)
        _fields = d.pop("fields", UNSET)
        fields: (
            list[CustomfieldsListPostRequestDataItemAttributesFieldsItem]
            | Unset
        ) = UNSET
        if _fields is not UNSET:
            fields = []
            for fields_item_data in _fields:
                fields_item = CustomfieldsListPostRequestDataItemAttributesFieldsItem.from_dict(
                    fields_item_data
                )

                fields.append(fields_item)

        resource_type = d.pop("resourceType", UNSET)

        target_type = d.pop("targetType", UNSET)

        customfields_list_post_request_data_item_attributes_obj = cls(
            fields=fields,
            resource_type=resource_type,
            target_type=target_type,
        )

        customfields_list_post_request_data_item_attributes_obj.additional_properties = d
        return customfields_list_post_request_data_item_attributes_obj

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

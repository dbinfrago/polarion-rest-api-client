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
    from ..models.collections_list_post_request_data_item_attributes_description import (
        CollectionsListPostRequestDataItemAttributesDescription,
    )


T = TypeVar("T", bound="CollectionsListPostRequestDataItemAttributes")


@_attrs_define
class CollectionsListPostRequestDataItemAttributes:
    """
    Attributes:
        description (CollectionsListPostRequestDataItemAttributesDescription | Unset):
        id (str | Unset):  Example: ID.
        name (str | Unset):  Example: Name.
    """

    description: (
        CollectionsListPostRequestDataItemAttributesDescription | Unset
    ) = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        description: dict[str, Any] | Unset = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict()

        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.collections_list_post_request_data_item_attributes_description import (
            CollectionsListPostRequestDataItemAttributesDescription,
        )

        d = dict(src_dict)
        _description = d.pop("description", UNSET)
        description: (
            CollectionsListPostRequestDataItemAttributesDescription | Unset
        )
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = CollectionsListPostRequestDataItemAttributesDescription.from_dict(
                _description
            )

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        collections_list_post_request_data_item_attributes_obj = cls(
            description=description,
            id=id,
            name=name,
        )

        collections_list_post_request_data_item_attributes_obj.additional_properties = d
        return collections_list_post_request_data_item_attributes_obj

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

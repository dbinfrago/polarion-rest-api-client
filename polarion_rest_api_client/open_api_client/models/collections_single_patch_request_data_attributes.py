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
    from ..models.collections_single_patch_request_data_attributes_description import (
        CollectionsSinglePatchRequestDataAttributesDescription,
    )


T = TypeVar("T", bound="CollectionsSinglePatchRequestDataAttributes")


@_attrs_define
class CollectionsSinglePatchRequestDataAttributes:
    """
    Attributes:
        description (CollectionsSinglePatchRequestDataAttributesDescription | Unset):
        name (str | Unset):  Example: Name.
    """

    description: (
        CollectionsSinglePatchRequestDataAttributesDescription | Unset
    ) = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        description: dict[str, Any] | Unset = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict()

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.collections_single_patch_request_data_attributes_description import (
            CollectionsSinglePatchRequestDataAttributesDescription,
        )

        d = dict(src_dict)
        _description = d.pop("description", UNSET)
        description: (
            CollectionsSinglePatchRequestDataAttributesDescription | Unset
        )
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = CollectionsSinglePatchRequestDataAttributesDescription.from_dict(
                _description
            )

        name = d.pop("name", UNSET)

        collections_single_patch_request_data_attributes_obj = cls(
            description=description,
            name=name,
        )

        collections_single_patch_request_data_attributes_obj.additional_properties = d
        return collections_single_patch_request_data_attributes_obj

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

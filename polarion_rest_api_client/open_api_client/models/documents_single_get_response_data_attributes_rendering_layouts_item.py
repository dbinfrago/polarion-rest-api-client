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
    from ..models.documents_single_get_response_data_attributes_rendering_layouts_item_properties_item import (
        DocumentsSingleGetResponseDataAttributesRenderingLayoutsItemPropertiesItem,
    )


T = TypeVar(
    "T", bound="DocumentsSingleGetResponseDataAttributesRenderingLayoutsItem"
)


@_attrs_define
class DocumentsSingleGetResponseDataAttributesRenderingLayoutsItem:
    """
    Attributes:
        label (str | Unset):  Example: My label.
        layouter (str | Unset):  Example: paragraph.
        properties (list[DocumentsSingleGetResponseDataAttributesRenderingLayoutsItemPropertiesItem] | Unset):
        type_ (str | Unset):  Example: task.
    """

    label: str | Unset = UNSET
    layouter: str | Unset = UNSET
    properties: (
        list[
            DocumentsSingleGetResponseDataAttributesRenderingLayoutsItemPropertiesItem
        ]
        | Unset
    ) = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        layouter = self.layouter

        properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()
                properties.append(properties_item)

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label is not UNSET:
            field_dict["label"] = label
        if layouter is not UNSET:
            field_dict["layouter"] = layouter
        if properties is not UNSET:
            field_dict["properties"] = properties
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.documents_single_get_response_data_attributes_rendering_layouts_item_properties_item import (
            DocumentsSingleGetResponseDataAttributesRenderingLayoutsItemPropertiesItem,
        )

        d = dict(src_dict)
        label = d.pop("label", UNSET)

        layouter = d.pop("layouter", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: (
            list[
                DocumentsSingleGetResponseDataAttributesRenderingLayoutsItemPropertiesItem
            ]
            | Unset
        ) = UNSET
        if _properties is not UNSET:
            properties = []
            for properties_item_data in _properties:
                properties_item = DocumentsSingleGetResponseDataAttributesRenderingLayoutsItemPropertiesItem.from_dict(
                    properties_item_data
                )

                properties.append(properties_item)

        type_ = d.pop("type", UNSET)

        documents_single_get_response_data_attributes_rendering_layouts_item_obj = cls(
            label=label,
            layouter=layouter,
            properties=properties,
            type_=type_,
        )

        documents_single_get_response_data_attributes_rendering_layouts_item_obj.additional_properties = d
        return documents_single_get_response_data_attributes_rendering_layouts_item_obj

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

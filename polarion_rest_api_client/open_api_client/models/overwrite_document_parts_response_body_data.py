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
    from ..models.overwrite_document_parts_response_body_data_overwritten_parts_item import (
        OverwriteDocumentPartsResponseBodyDataOverwrittenPartsItem,
    )


T = TypeVar("T", bound="OverwriteDocumentPartsResponseBodyData")


@_attrs_define
class OverwriteDocumentPartsResponseBodyData:
    """
    Attributes:
        overwritten_parts (list[OverwriteDocumentPartsResponseBodyDataOverwrittenPartsItem] | Unset): Array of Part ID
            mappings showing old and new IDs.
    """

    overwritten_parts: (
        list[OverwriteDocumentPartsResponseBodyDataOverwrittenPartsItem]
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        overwritten_parts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.overwritten_parts, Unset):
            overwritten_parts = []
            for overwritten_parts_item_data in self.overwritten_parts:
                overwritten_parts_item = overwritten_parts_item_data.to_dict()
                overwritten_parts.append(overwritten_parts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if overwritten_parts is not UNSET:
            field_dict["overwrittenParts"] = overwritten_parts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.overwrite_document_parts_response_body_data_overwritten_parts_item import (
            OverwriteDocumentPartsResponseBodyDataOverwrittenPartsItem,
        )

        d = dict(src_dict)
        _overwritten_parts = d.pop("overwrittenParts", UNSET)
        overwritten_parts: (
            list[OverwriteDocumentPartsResponseBodyDataOverwrittenPartsItem]
            | Unset
        ) = UNSET
        if _overwritten_parts is not UNSET:
            overwritten_parts = []
            for overwritten_parts_item_data in _overwritten_parts:
                overwritten_parts_item = OverwriteDocumentPartsResponseBodyDataOverwrittenPartsItem.from_dict(
                    overwritten_parts_item_data
                )

                overwritten_parts.append(overwritten_parts_item)

        overwrite_document_parts_response_body_data_obj = cls(
            overwritten_parts=overwritten_parts,
        )

        overwrite_document_parts_response_body_data_obj.additional_properties = d
        return overwrite_document_parts_response_body_data_obj

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

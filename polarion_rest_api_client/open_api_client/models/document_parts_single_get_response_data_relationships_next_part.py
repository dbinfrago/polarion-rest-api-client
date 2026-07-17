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
    from ..models.document_parts_single_get_response_data_relationships_next_part_data import (
        DocumentPartsSingleGetResponseDataRelationshipsNextPartData,
    )


T = TypeVar(
    "T", bound="DocumentPartsSingleGetResponseDataRelationshipsNextPart"
)


@_attrs_define
class DocumentPartsSingleGetResponseDataRelationshipsNextPart:
    """
    Attributes:
        data (DocumentPartsSingleGetResponseDataRelationshipsNextPartData | Unset):
    """

    data: (
        DocumentPartsSingleGetResponseDataRelationshipsNextPartData | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.document_parts_single_get_response_data_relationships_next_part_data import (
            DocumentPartsSingleGetResponseDataRelationshipsNextPartData,
        )

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: (
            DocumentPartsSingleGetResponseDataRelationshipsNextPartData | Unset
        )
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = DocumentPartsSingleGetResponseDataRelationshipsNextPartData.from_dict(
                _data
            )

        document_parts_single_get_response_data_relationships_next_part_obj = (
            cls(
                data=data,
            )
        )

        document_parts_single_get_response_data_relationships_next_part_obj.additional_properties = d
        return (
            document_parts_single_get_response_data_relationships_next_part_obj
        )

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

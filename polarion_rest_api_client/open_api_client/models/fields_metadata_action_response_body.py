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
    from ..models.fields_metadata_action_response_body_data import (
        FieldsMetadataActionResponseBodyData,
    )
    from ..models.fields_metadata_action_response_body_links import (
        FieldsMetadataActionResponseBodyLinks,
    )


T = TypeVar("T", bound="FieldsMetadataActionResponseBody")


@_attrs_define
class FieldsMetadataActionResponseBody:
    """
    Attributes:
        data (FieldsMetadataActionResponseBodyData | Unset):
        links (FieldsMetadataActionResponseBodyLinks | Unset):
    """

    data: FieldsMetadataActionResponseBodyData | Unset = UNSET
    links: FieldsMetadataActionResponseBodyLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fields_metadata_action_response_body_data import (
            FieldsMetadataActionResponseBodyData,
        )
        from ..models.fields_metadata_action_response_body_links import (
            FieldsMetadataActionResponseBodyLinks,
        )

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: FieldsMetadataActionResponseBodyData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = FieldsMetadataActionResponseBodyData.from_dict(_data)

        _links = d.pop("links", UNSET)
        links: FieldsMetadataActionResponseBodyLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = FieldsMetadataActionResponseBodyLinks.from_dict(_links)

        fields_metadata_action_response_body_obj = cls(
            data=data,
            links=links,
        )

        fields_metadata_action_response_body_obj.additional_properties = d
        return fields_metadata_action_response_body_obj

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

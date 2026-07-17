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

from ..models.enumerations_single_get_response_data_type import (
    EnumerationsSingleGetResponseDataType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.enumerations_single_get_response_data_attributes import (
        EnumerationsSingleGetResponseDataAttributes,
    )
    from ..models.enumerations_single_get_response_data_links import (
        EnumerationsSingleGetResponseDataLinks,
    )
    from ..models.enumerations_single_get_response_data_meta import (
        EnumerationsSingleGetResponseDataMeta,
    )


T = TypeVar("T", bound="EnumerationsSingleGetResponseData")


@_attrs_define
class EnumerationsSingleGetResponseData:
    """
    Attributes:
        type_ (EnumerationsSingleGetResponseDataType | Unset):
        id (str | Unset):  Example: ~/status/~.
        attributes (EnumerationsSingleGetResponseDataAttributes | Unset):
        links (EnumerationsSingleGetResponseDataLinks | Unset):
        meta (EnumerationsSingleGetResponseDataMeta | Unset):
    """

    type_: EnumerationsSingleGetResponseDataType | Unset = UNSET
    id: str | Unset = UNSET
    attributes: EnumerationsSingleGetResponseDataAttributes | Unset = UNSET
    links: EnumerationsSingleGetResponseDataLinks | Unset = UNSET
    meta: EnumerationsSingleGetResponseDataMeta | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        id = self.id

        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if id is not UNSET:
            field_dict["id"] = id
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if links is not UNSET:
            field_dict["links"] = links
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.enumerations_single_get_response_data_attributes import (
            EnumerationsSingleGetResponseDataAttributes,
        )
        from ..models.enumerations_single_get_response_data_links import (
            EnumerationsSingleGetResponseDataLinks,
        )
        from ..models.enumerations_single_get_response_data_meta import (
            EnumerationsSingleGetResponseDataMeta,
        )

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: EnumerationsSingleGetResponseDataType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = EnumerationsSingleGetResponseDataType(_type_)

        id = d.pop("id", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: EnumerationsSingleGetResponseDataAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = EnumerationsSingleGetResponseDataAttributes.from_dict(
                _attributes
            )

        _links = d.pop("links", UNSET)
        links: EnumerationsSingleGetResponseDataLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = EnumerationsSingleGetResponseDataLinks.from_dict(_links)

        _meta = d.pop("meta", UNSET)
        meta: EnumerationsSingleGetResponseDataMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = EnumerationsSingleGetResponseDataMeta.from_dict(_meta)

        enumerations_single_get_response_data_obj = cls(
            type_=type_,
            id=id,
            attributes=attributes,
            links=links,
            meta=meta,
        )

        enumerations_single_get_response_data_obj.additional_properties = d
        return enumerations_single_get_response_data_obj

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

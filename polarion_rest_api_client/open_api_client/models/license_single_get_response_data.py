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

from ..models.license_single_get_response_data_type import (
    LicenseSingleGetResponseDataType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.license_single_get_response_data_attributes import (
        LicenseSingleGetResponseDataAttributes,
    )
    from ..models.license_single_get_response_data_links import (
        LicenseSingleGetResponseDataLinks,
    )
    from ..models.license_single_get_response_data_meta import (
        LicenseSingleGetResponseDataMeta,
    )
    from ..models.license_single_get_response_data_relationships import (
        LicenseSingleGetResponseDataRelationships,
    )


T = TypeVar("T", bound="LicenseSingleGetResponseData")


@_attrs_define
class LicenseSingleGetResponseData:
    """
    Attributes:
        type_ (LicenseSingleGetResponseDataType | Unset):
        id (str | Unset):  Example: license.
        attributes (LicenseSingleGetResponseDataAttributes | Unset):
        relationships (LicenseSingleGetResponseDataRelationships | Unset):
        links (LicenseSingleGetResponseDataLinks | Unset):
        meta (LicenseSingleGetResponseDataMeta | Unset):
    """

    type_: LicenseSingleGetResponseDataType | Unset = UNSET
    id: str | Unset = UNSET
    attributes: LicenseSingleGetResponseDataAttributes | Unset = UNSET
    relationships: LicenseSingleGetResponseDataRelationships | Unset = UNSET
    links: LicenseSingleGetResponseDataLinks | Unset = UNSET
    meta: LicenseSingleGetResponseDataMeta | Unset = UNSET
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

        relationships: dict[str, Any] | Unset = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = self.relationships.to_dict()

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
        if relationships is not UNSET:
            field_dict["relationships"] = relationships
        if links is not UNSET:
            field_dict["links"] = links
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.license_single_get_response_data_attributes import (
            LicenseSingleGetResponseDataAttributes,
        )
        from ..models.license_single_get_response_data_links import (
            LicenseSingleGetResponseDataLinks,
        )
        from ..models.license_single_get_response_data_meta import (
            LicenseSingleGetResponseDataMeta,
        )
        from ..models.license_single_get_response_data_relationships import (
            LicenseSingleGetResponseDataRelationships,
        )

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: LicenseSingleGetResponseDataType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = LicenseSingleGetResponseDataType(_type_)

        id = d.pop("id", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: LicenseSingleGetResponseDataAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = LicenseSingleGetResponseDataAttributes.from_dict(
                _attributes
            )

        _relationships = d.pop("relationships", UNSET)
        relationships: LicenseSingleGetResponseDataRelationships | Unset
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = (
                LicenseSingleGetResponseDataRelationships.from_dict(
                    _relationships
                )
            )

        _links = d.pop("links", UNSET)
        links: LicenseSingleGetResponseDataLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = LicenseSingleGetResponseDataLinks.from_dict(_links)

        _meta = d.pop("meta", UNSET)
        meta: LicenseSingleGetResponseDataMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = LicenseSingleGetResponseDataMeta.from_dict(_meta)

        license_single_get_response_data_obj = cls(
            type_=type_,
            id=id,
            attributes=attributes,
            relationships=relationships,
            links=links,
            meta=meta,
        )

        license_single_get_response_data_obj.additional_properties = d
        return license_single_get_response_data_obj

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

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

from ..models.license_assignments_list_get_response_data_item_type import (
    LicenseAssignmentsListGetResponseDataItemType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.license_assignments_list_get_response_data_item_attributes import (
        LicenseAssignmentsListGetResponseDataItemAttributes,
    )
    from ..models.license_assignments_list_get_response_data_item_links import (
        LicenseAssignmentsListGetResponseDataItemLinks,
    )
    from ..models.license_assignments_list_get_response_data_item_meta import (
        LicenseAssignmentsListGetResponseDataItemMeta,
    )
    from ..models.license_assignments_list_get_response_data_item_relationships import (
        LicenseAssignmentsListGetResponseDataItemRelationships,
    )


T = TypeVar("T", bound="LicenseAssignmentsListGetResponseDataItem")


@_attrs_define
class LicenseAssignmentsListGetResponseDataItem:
    """
    Attributes:
        type_ (LicenseAssignmentsListGetResponseDataItemType | Unset):
        id (str | Unset):  Example: MyUserId.
        attributes (LicenseAssignmentsListGetResponseDataItemAttributes | Unset):
        relationships (LicenseAssignmentsListGetResponseDataItemRelationships | Unset):
        links (LicenseAssignmentsListGetResponseDataItemLinks | Unset):
        meta (LicenseAssignmentsListGetResponseDataItemMeta | Unset):
    """

    type_: LicenseAssignmentsListGetResponseDataItemType | Unset = UNSET
    id: str | Unset = UNSET
    attributes: LicenseAssignmentsListGetResponseDataItemAttributes | Unset = (
        UNSET
    )
    relationships: (
        LicenseAssignmentsListGetResponseDataItemRelationships | Unset
    ) = UNSET
    links: LicenseAssignmentsListGetResponseDataItemLinks | Unset = UNSET
    meta: LicenseAssignmentsListGetResponseDataItemMeta | Unset = UNSET
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
        from ..models.license_assignments_list_get_response_data_item_attributes import (
            LicenseAssignmentsListGetResponseDataItemAttributes,
        )
        from ..models.license_assignments_list_get_response_data_item_links import (
            LicenseAssignmentsListGetResponseDataItemLinks,
        )
        from ..models.license_assignments_list_get_response_data_item_meta import (
            LicenseAssignmentsListGetResponseDataItemMeta,
        )
        from ..models.license_assignments_list_get_response_data_item_relationships import (
            LicenseAssignmentsListGetResponseDataItemRelationships,
        )

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: LicenseAssignmentsListGetResponseDataItemType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = LicenseAssignmentsListGetResponseDataItemType(_type_)

        id = d.pop("id", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: LicenseAssignmentsListGetResponseDataItemAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = (
                LicenseAssignmentsListGetResponseDataItemAttributes.from_dict(
                    _attributes
                )
            )

        _relationships = d.pop("relationships", UNSET)
        relationships: (
            LicenseAssignmentsListGetResponseDataItemRelationships | Unset
        )
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = LicenseAssignmentsListGetResponseDataItemRelationships.from_dict(
                _relationships
            )

        _links = d.pop("links", UNSET)
        links: LicenseAssignmentsListGetResponseDataItemLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = LicenseAssignmentsListGetResponseDataItemLinks.from_dict(
                _links
            )

        _meta = d.pop("meta", UNSET)
        meta: LicenseAssignmentsListGetResponseDataItemMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = LicenseAssignmentsListGetResponseDataItemMeta.from_dict(
                _meta
            )

        license_assignments_list_get_response_data_item_obj = cls(
            type_=type_,
            id=id,
            attributes=attributes,
            relationships=relationships,
            links=links,
            meta=meta,
        )

        license_assignments_list_get_response_data_item_obj.additional_properties = d
        return license_assignments_list_get_response_data_item_obj

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

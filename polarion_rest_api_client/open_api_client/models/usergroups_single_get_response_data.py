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

from ..models.usergroups_single_get_response_data_type import (
    UsergroupsSingleGetResponseDataType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.usergroups_single_get_response_data_attributes import (
        UsergroupsSingleGetResponseDataAttributes,
    )
    from ..models.usergroups_single_get_response_data_links import (
        UsergroupsSingleGetResponseDataLinks,
    )
    from ..models.usergroups_single_get_response_data_meta import (
        UsergroupsSingleGetResponseDataMeta,
    )
    from ..models.usergroups_single_get_response_data_relationships import (
        UsergroupsSingleGetResponseDataRelationships,
    )


T = TypeVar("T", bound="UsergroupsSingleGetResponseData")


@_attrs_define
class UsergroupsSingleGetResponseData:
    """
    Attributes:
        type_ (UsergroupsSingleGetResponseDataType | Unset):
        id (str | Unset):  Example: MyUserGroupId.
        revision (str | Unset):  Example: 1234.
        attributes (UsergroupsSingleGetResponseDataAttributes | Unset):
        relationships (UsergroupsSingleGetResponseDataRelationships | Unset):
        links (UsergroupsSingleGetResponseDataLinks | Unset):
        meta (UsergroupsSingleGetResponseDataMeta | Unset):
    """

    type_: UsergroupsSingleGetResponseDataType | Unset = UNSET
    id: str | Unset = UNSET
    revision: str | Unset = UNSET
    attributes: UsergroupsSingleGetResponseDataAttributes | Unset = UNSET
    relationships: UsergroupsSingleGetResponseDataRelationships | Unset = UNSET
    links: UsergroupsSingleGetResponseDataLinks | Unset = UNSET
    meta: UsergroupsSingleGetResponseDataMeta | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        id = self.id

        revision = self.revision

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
        if revision is not UNSET:
            field_dict["revision"] = revision
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
        from ..models.usergroups_single_get_response_data_attributes import (
            UsergroupsSingleGetResponseDataAttributes,
        )
        from ..models.usergroups_single_get_response_data_links import (
            UsergroupsSingleGetResponseDataLinks,
        )
        from ..models.usergroups_single_get_response_data_meta import (
            UsergroupsSingleGetResponseDataMeta,
        )
        from ..models.usergroups_single_get_response_data_relationships import (
            UsergroupsSingleGetResponseDataRelationships,
        )

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: UsergroupsSingleGetResponseDataType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = UsergroupsSingleGetResponseDataType(_type_)

        id = d.pop("id", UNSET)

        revision = d.pop("revision", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: UsergroupsSingleGetResponseDataAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = UsergroupsSingleGetResponseDataAttributes.from_dict(
                _attributes
            )

        _relationships = d.pop("relationships", UNSET)
        relationships: UsergroupsSingleGetResponseDataRelationships | Unset
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = (
                UsergroupsSingleGetResponseDataRelationships.from_dict(
                    _relationships
                )
            )

        _links = d.pop("links", UNSET)
        links: UsergroupsSingleGetResponseDataLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = UsergroupsSingleGetResponseDataLinks.from_dict(_links)

        _meta = d.pop("meta", UNSET)
        meta: UsergroupsSingleGetResponseDataMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = UsergroupsSingleGetResponseDataMeta.from_dict(_meta)

        usergroups_single_get_response_data_obj = cls(
            type_=type_,
            id=id,
            revision=revision,
            attributes=attributes,
            relationships=relationships,
            links=links,
            meta=meta,
        )

        usergroups_single_get_response_data_obj.additional_properties = d
        return usergroups_single_get_response_data_obj

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

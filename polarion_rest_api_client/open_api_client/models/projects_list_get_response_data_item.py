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

from ..models.projects_list_get_response_data_item_type import (
    ProjectsListGetResponseDataItemType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.projects_list_get_response_data_item_attributes import (
        ProjectsListGetResponseDataItemAttributes,
    )
    from ..models.projects_list_get_response_data_item_links import (
        ProjectsListGetResponseDataItemLinks,
    )
    from ..models.projects_list_get_response_data_item_meta import (
        ProjectsListGetResponseDataItemMeta,
    )
    from ..models.projects_list_get_response_data_item_relationships import (
        ProjectsListGetResponseDataItemRelationships,
    )


T = TypeVar("T", bound="ProjectsListGetResponseDataItem")


@_attrs_define
class ProjectsListGetResponseDataItem:
    """
    Attributes:
        type_ (ProjectsListGetResponseDataItemType | Unset):
        id (str | Unset):  Example: MyProjectId.
        revision (str | Unset):  Example: 1234.
        attributes (ProjectsListGetResponseDataItemAttributes | Unset):
        relationships (ProjectsListGetResponseDataItemRelationships | Unset):
        links (ProjectsListGetResponseDataItemLinks | Unset):
        meta (ProjectsListGetResponseDataItemMeta | Unset):
    """

    type_: ProjectsListGetResponseDataItemType | Unset = UNSET
    id: str | Unset = UNSET
    revision: str | Unset = UNSET
    attributes: ProjectsListGetResponseDataItemAttributes | Unset = UNSET
    relationships: ProjectsListGetResponseDataItemRelationships | Unset = UNSET
    links: ProjectsListGetResponseDataItemLinks | Unset = UNSET
    meta: ProjectsListGetResponseDataItemMeta | Unset = UNSET
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
        from ..models.projects_list_get_response_data_item_attributes import (
            ProjectsListGetResponseDataItemAttributes,
        )
        from ..models.projects_list_get_response_data_item_links import (
            ProjectsListGetResponseDataItemLinks,
        )
        from ..models.projects_list_get_response_data_item_meta import (
            ProjectsListGetResponseDataItemMeta,
        )
        from ..models.projects_list_get_response_data_item_relationships import (
            ProjectsListGetResponseDataItemRelationships,
        )

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: ProjectsListGetResponseDataItemType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ProjectsListGetResponseDataItemType(_type_)

        id = d.pop("id", UNSET)

        revision = d.pop("revision", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: ProjectsListGetResponseDataItemAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = ProjectsListGetResponseDataItemAttributes.from_dict(
                _attributes
            )

        _relationships = d.pop("relationships", UNSET)
        relationships: ProjectsListGetResponseDataItemRelationships | Unset
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = (
                ProjectsListGetResponseDataItemRelationships.from_dict(
                    _relationships
                )
            )

        _links = d.pop("links", UNSET)
        links: ProjectsListGetResponseDataItemLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ProjectsListGetResponseDataItemLinks.from_dict(_links)

        _meta = d.pop("meta", UNSET)
        meta: ProjectsListGetResponseDataItemMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = ProjectsListGetResponseDataItemMeta.from_dict(_meta)

        projects_list_get_response_data_item_obj = cls(
            type_=type_,
            id=id,
            revision=revision,
            attributes=attributes,
            relationships=relationships,
            links=links,
            meta=meta,
        )

        projects_list_get_response_data_item_obj.additional_properties = d
        return projects_list_get_response_data_item_obj

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

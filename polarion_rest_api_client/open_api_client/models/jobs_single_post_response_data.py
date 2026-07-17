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

from ..models.jobs_single_post_response_data_type import (
    JobsSinglePostResponseDataType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.jobs_single_post_response_data_attributes import (
        JobsSinglePostResponseDataAttributes,
    )
    from ..models.jobs_single_post_response_data_links import (
        JobsSinglePostResponseDataLinks,
    )
    from ..models.jobs_single_post_response_data_relationships import (
        JobsSinglePostResponseDataRelationships,
    )


T = TypeVar("T", bound="JobsSinglePostResponseData")


@_attrs_define
class JobsSinglePostResponseData:
    """
    Attributes:
        type_ (JobsSinglePostResponseDataType | Unset):
        id (str | Unset):  Example: MyJobId.
        attributes (JobsSinglePostResponseDataAttributes | Unset):
        relationships (JobsSinglePostResponseDataRelationships | Unset):
        links (JobsSinglePostResponseDataLinks | Unset):
    """

    type_: JobsSinglePostResponseDataType | Unset = UNSET
    id: str | Unset = UNSET
    attributes: JobsSinglePostResponseDataAttributes | Unset = UNSET
    relationships: JobsSinglePostResponseDataRelationships | Unset = UNSET
    links: JobsSinglePostResponseDataLinks | Unset = UNSET
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jobs_single_post_response_data_attributes import (
            JobsSinglePostResponseDataAttributes,
        )
        from ..models.jobs_single_post_response_data_links import (
            JobsSinglePostResponseDataLinks,
        )
        from ..models.jobs_single_post_response_data_relationships import (
            JobsSinglePostResponseDataRelationships,
        )

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: JobsSinglePostResponseDataType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = JobsSinglePostResponseDataType(_type_)

        id = d.pop("id", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: JobsSinglePostResponseDataAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = JobsSinglePostResponseDataAttributes.from_dict(
                _attributes
            )

        _relationships = d.pop("relationships", UNSET)
        relationships: JobsSinglePostResponseDataRelationships | Unset
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = JobsSinglePostResponseDataRelationships.from_dict(
                _relationships
            )

        _links = d.pop("links", UNSET)
        links: JobsSinglePostResponseDataLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = JobsSinglePostResponseDataLinks.from_dict(_links)

        jobs_single_post_response_data_obj = cls(
            type_=type_,
            id=id,
            attributes=attributes,
            relationships=relationships,
            links=links,
        )

        jobs_single_post_response_data_obj.additional_properties = d
        return jobs_single_post_response_data_obj

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

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

from ..models.workitem_comments_single_get_response_data_type import (
    WorkitemCommentsSingleGetResponseDataType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workitem_comments_single_get_response_data_attributes import (
        WorkitemCommentsSingleGetResponseDataAttributes,
    )
    from ..models.workitem_comments_single_get_response_data_links import (
        WorkitemCommentsSingleGetResponseDataLinks,
    )
    from ..models.workitem_comments_single_get_response_data_meta import (
        WorkitemCommentsSingleGetResponseDataMeta,
    )
    from ..models.workitem_comments_single_get_response_data_relationships import (
        WorkitemCommentsSingleGetResponseDataRelationships,
    )


T = TypeVar("T", bound="WorkitemCommentsSingleGetResponseData")


@_attrs_define
class WorkitemCommentsSingleGetResponseData:
    """
    Attributes:
        type_ (WorkitemCommentsSingleGetResponseDataType | Unset):
        id (str | Unset):  Example: MyProjectId/MyWorkItemId/MyCommentId.
        revision (str | Unset):  Example: 1234.
        attributes (WorkitemCommentsSingleGetResponseDataAttributes | Unset):
        relationships (WorkitemCommentsSingleGetResponseDataRelationships | Unset):
        links (WorkitemCommentsSingleGetResponseDataLinks | Unset):
        meta (WorkitemCommentsSingleGetResponseDataMeta | Unset):
    """

    type_: WorkitemCommentsSingleGetResponseDataType | Unset = UNSET
    id: str | Unset = UNSET
    revision: str | Unset = UNSET
    attributes: WorkitemCommentsSingleGetResponseDataAttributes | Unset = UNSET
    relationships: (
        WorkitemCommentsSingleGetResponseDataRelationships | Unset
    ) = UNSET
    links: WorkitemCommentsSingleGetResponseDataLinks | Unset = UNSET
    meta: WorkitemCommentsSingleGetResponseDataMeta | Unset = UNSET
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
        from ..models.workitem_comments_single_get_response_data_attributes import (
            WorkitemCommentsSingleGetResponseDataAttributes,
        )
        from ..models.workitem_comments_single_get_response_data_links import (
            WorkitemCommentsSingleGetResponseDataLinks,
        )
        from ..models.workitem_comments_single_get_response_data_meta import (
            WorkitemCommentsSingleGetResponseDataMeta,
        )
        from ..models.workitem_comments_single_get_response_data_relationships import (
            WorkitemCommentsSingleGetResponseDataRelationships,
        )

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: WorkitemCommentsSingleGetResponseDataType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = WorkitemCommentsSingleGetResponseDataType(_type_)

        id = d.pop("id", UNSET)

        revision = d.pop("revision", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: WorkitemCommentsSingleGetResponseDataAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = (
                WorkitemCommentsSingleGetResponseDataAttributes.from_dict(
                    _attributes
                )
            )

        _relationships = d.pop("relationships", UNSET)
        relationships: (
            WorkitemCommentsSingleGetResponseDataRelationships | Unset
        )
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = (
                WorkitemCommentsSingleGetResponseDataRelationships.from_dict(
                    _relationships
                )
            )

        _links = d.pop("links", UNSET)
        links: WorkitemCommentsSingleGetResponseDataLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = WorkitemCommentsSingleGetResponseDataLinks.from_dict(
                _links
            )

        _meta = d.pop("meta", UNSET)
        meta: WorkitemCommentsSingleGetResponseDataMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = WorkitemCommentsSingleGetResponseDataMeta.from_dict(_meta)

        workitem_comments_single_get_response_data_obj = cls(
            type_=type_,
            id=id,
            revision=revision,
            attributes=attributes,
            relationships=relationships,
            links=links,
            meta=meta,
        )

        workitem_comments_single_get_response_data_obj.additional_properties = d
        return workitem_comments_single_get_response_data_obj

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

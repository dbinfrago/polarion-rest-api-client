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

from ..models.document_parts_single_get_response_data_type import (
    DocumentPartsSingleGetResponseDataType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_parts_single_get_response_data_attributes import (
        DocumentPartsSingleGetResponseDataAttributes,
    )
    from ..models.document_parts_single_get_response_data_links import (
        DocumentPartsSingleGetResponseDataLinks,
    )
    from ..models.document_parts_single_get_response_data_meta import (
        DocumentPartsSingleGetResponseDataMeta,
    )
    from ..models.document_parts_single_get_response_data_relationships import (
        DocumentPartsSingleGetResponseDataRelationships,
    )


T = TypeVar("T", bound="DocumentPartsSingleGetResponseData")


@_attrs_define
class DocumentPartsSingleGetResponseData:
    """
    Attributes:
        type_ (DocumentPartsSingleGetResponseDataType | Unset):
        id (str | Unset):  Example: MyProjectId/MySpaceId/MyDocumentId/workitem_MyWorkItemId.
        revision (str | Unset):  Example: 1234.
        attributes (DocumentPartsSingleGetResponseDataAttributes | Unset):
        relationships (DocumentPartsSingleGetResponseDataRelationships | Unset):
        links (DocumentPartsSingleGetResponseDataLinks | Unset):
        meta (DocumentPartsSingleGetResponseDataMeta | Unset):
    """

    type_: DocumentPartsSingleGetResponseDataType | Unset = UNSET
    id: str | Unset = UNSET
    revision: str | Unset = UNSET
    attributes: DocumentPartsSingleGetResponseDataAttributes | Unset = UNSET
    relationships: DocumentPartsSingleGetResponseDataRelationships | Unset = (
        UNSET
    )
    links: DocumentPartsSingleGetResponseDataLinks | Unset = UNSET
    meta: DocumentPartsSingleGetResponseDataMeta | Unset = UNSET
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
        from ..models.document_parts_single_get_response_data_attributes import (
            DocumentPartsSingleGetResponseDataAttributes,
        )
        from ..models.document_parts_single_get_response_data_links import (
            DocumentPartsSingleGetResponseDataLinks,
        )
        from ..models.document_parts_single_get_response_data_meta import (
            DocumentPartsSingleGetResponseDataMeta,
        )
        from ..models.document_parts_single_get_response_data_relationships import (
            DocumentPartsSingleGetResponseDataRelationships,
        )

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: DocumentPartsSingleGetResponseDataType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DocumentPartsSingleGetResponseDataType(_type_)

        id = d.pop("id", UNSET)

        revision = d.pop("revision", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: DocumentPartsSingleGetResponseDataAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = (
                DocumentPartsSingleGetResponseDataAttributes.from_dict(
                    _attributes
                )
            )

        _relationships = d.pop("relationships", UNSET)
        relationships: DocumentPartsSingleGetResponseDataRelationships | Unset
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = (
                DocumentPartsSingleGetResponseDataRelationships.from_dict(
                    _relationships
                )
            )

        _links = d.pop("links", UNSET)
        links: DocumentPartsSingleGetResponseDataLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = DocumentPartsSingleGetResponseDataLinks.from_dict(_links)

        _meta = d.pop("meta", UNSET)
        meta: DocumentPartsSingleGetResponseDataMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = DocumentPartsSingleGetResponseDataMeta.from_dict(_meta)

        document_parts_single_get_response_data_obj = cls(
            type_=type_,
            id=id,
            revision=revision,
            attributes=attributes,
            relationships=relationships,
            links=links,
            meta=meta,
        )

        document_parts_single_get_response_data_obj.additional_properties = d
        return document_parts_single_get_response_data_obj

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

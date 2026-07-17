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
    from ..models.documents_single_get_response_data_relationships_attachments_data_item import (
        DocumentsSingleGetResponseDataRelationshipsAttachmentsDataItem,
    )
    from ..models.documents_single_get_response_data_relationships_attachments_links import (
        DocumentsSingleGetResponseDataRelationshipsAttachmentsLinks,
    )
    from ..models.documents_single_get_response_data_relationships_attachments_meta import (
        DocumentsSingleGetResponseDataRelationshipsAttachmentsMeta,
    )


T = TypeVar(
    "T", bound="DocumentsSingleGetResponseDataRelationshipsAttachments"
)


@_attrs_define
class DocumentsSingleGetResponseDataRelationshipsAttachments:
    """
    Attributes:
        data (list[DocumentsSingleGetResponseDataRelationshipsAttachmentsDataItem] | Unset):
        links (DocumentsSingleGetResponseDataRelationshipsAttachmentsLinks | Unset):
        meta (DocumentsSingleGetResponseDataRelationshipsAttachmentsMeta | Unset):
    """

    data: (
        list[DocumentsSingleGetResponseDataRelationshipsAttachmentsDataItem]
        | Unset
    ) = UNSET
    links: (
        DocumentsSingleGetResponseDataRelationshipsAttachmentsLinks | Unset
    ) = UNSET
    meta: (
        DocumentsSingleGetResponseDataRelationshipsAttachmentsMeta | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if links is not UNSET:
            field_dict["links"] = links
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.documents_single_get_response_data_relationships_attachments_data_item import (
            DocumentsSingleGetResponseDataRelationshipsAttachmentsDataItem,
        )
        from ..models.documents_single_get_response_data_relationships_attachments_links import (
            DocumentsSingleGetResponseDataRelationshipsAttachmentsLinks,
        )
        from ..models.documents_single_get_response_data_relationships_attachments_meta import (
            DocumentsSingleGetResponseDataRelationshipsAttachmentsMeta,
        )

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: (
            list[
                DocumentsSingleGetResponseDataRelationshipsAttachmentsDataItem
            ]
            | Unset
        ) = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = DocumentsSingleGetResponseDataRelationshipsAttachmentsDataItem.from_dict(
                    data_item_data
                )

                data.append(data_item)

        _links = d.pop("links", UNSET)
        links: (
            DocumentsSingleGetResponseDataRelationshipsAttachmentsLinks | Unset
        )
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = DocumentsSingleGetResponseDataRelationshipsAttachmentsLinks.from_dict(
                _links
            )

        _meta = d.pop("meta", UNSET)
        meta: (
            DocumentsSingleGetResponseDataRelationshipsAttachmentsMeta | Unset
        )
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = DocumentsSingleGetResponseDataRelationshipsAttachmentsMeta.from_dict(
                _meta
            )

        documents_single_get_response_data_relationships_attachments_obj = cls(
            data=data,
            links=links,
            meta=meta,
        )

        documents_single_get_response_data_relationships_attachments_obj.additional_properties = d
        return documents_single_get_response_data_relationships_attachments_obj

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

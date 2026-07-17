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

from ..models.llms_list_get_response_data_item_type import (
    LlmsListGetResponseDataItemType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.llms_list_get_response_data_item_attributes import (
        LlmsListGetResponseDataItemAttributes,
    )
    from ..models.llms_list_get_response_data_item_links import (
        LlmsListGetResponseDataItemLinks,
    )
    from ..models.llms_list_get_response_data_item_meta import (
        LlmsListGetResponseDataItemMeta,
    )


T = TypeVar("T", bound="LlmsListGetResponseDataItem")


@_attrs_define
class LlmsListGetResponseDataItem:
    """
    Attributes:
        type_ (LlmsListGetResponseDataItemType | Unset):
        id (str | Unset):  Example: myLlm.
        attributes (LlmsListGetResponseDataItemAttributes | Unset):
        links (LlmsListGetResponseDataItemLinks | Unset):
        meta (LlmsListGetResponseDataItemMeta | Unset):
    """

    type_: LlmsListGetResponseDataItemType | Unset = UNSET
    id: str | Unset = UNSET
    attributes: LlmsListGetResponseDataItemAttributes | Unset = UNSET
    links: LlmsListGetResponseDataItemLinks | Unset = UNSET
    meta: LlmsListGetResponseDataItemMeta | Unset = UNSET
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
        from ..models.llms_list_get_response_data_item_attributes import (
            LlmsListGetResponseDataItemAttributes,
        )
        from ..models.llms_list_get_response_data_item_links import (
            LlmsListGetResponseDataItemLinks,
        )
        from ..models.llms_list_get_response_data_item_meta import (
            LlmsListGetResponseDataItemMeta,
        )

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: LlmsListGetResponseDataItemType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = LlmsListGetResponseDataItemType(_type_)

        id = d.pop("id", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: LlmsListGetResponseDataItemAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = LlmsListGetResponseDataItemAttributes.from_dict(
                _attributes
            )

        _links = d.pop("links", UNSET)
        links: LlmsListGetResponseDataItemLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = LlmsListGetResponseDataItemLinks.from_dict(_links)

        _meta = d.pop("meta", UNSET)
        meta: LlmsListGetResponseDataItemMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = LlmsListGetResponseDataItemMeta.from_dict(_meta)

        llms_list_get_response_data_item_obj = cls(
            type_=type_,
            id=id,
            attributes=attributes,
            links=links,
            meta=meta,
        )

        llms_list_get_response_data_item_obj.additional_properties = d
        return llms_list_get_response_data_item_obj

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

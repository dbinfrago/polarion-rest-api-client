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

from ..models.workrecords_list_post_response_data_item_type import (
    WorkrecordsListPostResponseDataItemType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workrecords_list_post_response_data_item_links import (
        WorkrecordsListPostResponseDataItemLinks,
    )


T = TypeVar("T", bound="WorkrecordsListPostResponseDataItem")


@_attrs_define
class WorkrecordsListPostResponseDataItem:
    """
    Attributes:
        type_ (WorkrecordsListPostResponseDataItemType | Unset):
        id (str | Unset):  Example: MyProjectId/MyWorkItemId/MyWorkRecordId.
        links (WorkrecordsListPostResponseDataItemLinks | Unset):
    """

    type_: WorkrecordsListPostResponseDataItemType | Unset = UNSET
    id: str | Unset = UNSET
    links: WorkrecordsListPostResponseDataItemLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        id = self.id

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
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workrecords_list_post_response_data_item_links import (
            WorkrecordsListPostResponseDataItemLinks,
        )

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: WorkrecordsListPostResponseDataItemType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = WorkrecordsListPostResponseDataItemType(_type_)

        id = d.pop("id", UNSET)

        _links = d.pop("links", UNSET)
        links: WorkrecordsListPostResponseDataItemLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = WorkrecordsListPostResponseDataItemLinks.from_dict(_links)

        workrecords_list_post_response_data_item_obj = cls(
            type_=type_,
            id=id,
            links=links,
        )

        workrecords_list_post_response_data_item_obj.additional_properties = d
        return workrecords_list_post_response_data_item_obj

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

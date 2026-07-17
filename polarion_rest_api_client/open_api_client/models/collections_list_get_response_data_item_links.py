# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CollectionsListGetResponseDataItemLinks")


@_attrs_define
class CollectionsListGetResponseDataItemLinks:
    """
    Attributes:
        portal (str | Unset):  Example: server-host-name/application-
            path/polarion/redirect/project/MyProjectId/collection?id=MyCollectionId&revision=1234.
        self_ (str | Unset):  Example: server-host-name/application-
            path/projects/MyProjectId/collections/MyCollectionId?revision=1234.
    """

    portal: str | Unset = UNSET
    self_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        portal = self.portal

        self_ = self.self_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if portal is not UNSET:
            field_dict["portal"] = portal
        if self_ is not UNSET:
            field_dict["self"] = self_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        portal = d.pop("portal", UNSET)

        self_ = d.pop("self", UNSET)

        collections_list_get_response_data_item_links_obj = cls(
            portal=portal,
            self_=self_,
        )

        collections_list_get_response_data_item_links_obj.additional_properties = d
        return collections_list_get_response_data_item_links_obj

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

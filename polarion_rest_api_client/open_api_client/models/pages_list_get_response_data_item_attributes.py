# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import datetime
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
    from ..models.pages_list_get_response_data_item_attributes_home_page_content import (
        PagesListGetResponseDataItemAttributesHomePageContent,
    )


T = TypeVar("T", bound="PagesListGetResponseDataItemAttributes")


@_attrs_define
class PagesListGetResponseDataItemAttributes:
    """
    Attributes:
        created (datetime.datetime | Unset):  Example: 1970-01-01T00:00:00Z.
        home_page_content (PagesListGetResponseDataItemAttributesHomePageContent | Unset):
        page_name (str | Unset):  Example: MyRichPageId.
        space_id (str | Unset):  Example: MySpaceId.
        title (str | Unset):  Example: Title.
        updated (datetime.datetime | Unset):  Example: 1970-01-01T00:00:00Z.
    """

    created: datetime.datetime | Unset = UNSET
    home_page_content: (
        PagesListGetResponseDataItemAttributesHomePageContent | Unset
    ) = UNSET
    page_name: str | Unset = UNSET
    space_id: str | Unset = UNSET
    title: str | Unset = UNSET
    updated: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        home_page_content: dict[str, Any] | Unset = UNSET
        if not isinstance(self.home_page_content, Unset):
            home_page_content = self.home_page_content.to_dict()

        page_name = self.page_name

        space_id = self.space_id

        title = self.title

        updated: str | Unset = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if home_page_content is not UNSET:
            field_dict["homePageContent"] = home_page_content
        if page_name is not UNSET:
            field_dict["pageName"] = page_name
        if space_id is not UNSET:
            field_dict["spaceId"] = space_id
        if title is not UNSET:
            field_dict["title"] = title
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pages_list_get_response_data_item_attributes_home_page_content import (
            PagesListGetResponseDataItemAttributesHomePageContent,
        )

        d = dict(src_dict)
        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = datetime.datetime.fromisoformat(_created)

        _home_page_content = d.pop("homePageContent", UNSET)
        home_page_content: (
            PagesListGetResponseDataItemAttributesHomePageContent | Unset
        )
        if isinstance(_home_page_content, Unset):
            home_page_content = UNSET
        else:
            home_page_content = PagesListGetResponseDataItemAttributesHomePageContent.from_dict(
                _home_page_content
            )

        page_name = d.pop("pageName", UNSET)

        space_id = d.pop("spaceId", UNSET)

        title = d.pop("title", UNSET)

        _updated = d.pop("updated", UNSET)
        updated: datetime.datetime | Unset
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = datetime.datetime.fromisoformat(_updated)

        pages_list_get_response_data_item_attributes_obj = cls(
            created=created,
            home_page_content=home_page_content,
            page_name=page_name,
            space_id=space_id,
            title=title,
            updated=updated,
        )

        pages_list_get_response_data_item_attributes_obj.additional_properties = d
        return pages_list_get_response_data_item_attributes_obj

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

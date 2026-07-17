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
    from ..models.pages_single_patch_request_data_attributes_home_page_content import (
        PagesSinglePatchRequestDataAttributesHomePageContent,
    )


T = TypeVar("T", bound="PagesSinglePatchRequestDataAttributes")


@_attrs_define
class PagesSinglePatchRequestDataAttributes:
    """
    Attributes:
        home_page_content (PagesSinglePatchRequestDataAttributesHomePageContent | Unset):
        title (str | Unset):  Example: Title.
    """

    home_page_content: (
        PagesSinglePatchRequestDataAttributesHomePageContent | Unset
    ) = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        home_page_content: dict[str, Any] | Unset = UNSET
        if not isinstance(self.home_page_content, Unset):
            home_page_content = self.home_page_content.to_dict()

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if home_page_content is not UNSET:
            field_dict["homePageContent"] = home_page_content
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pages_single_patch_request_data_attributes_home_page_content import (
            PagesSinglePatchRequestDataAttributesHomePageContent,
        )

        d = dict(src_dict)
        _home_page_content = d.pop("homePageContent", UNSET)
        home_page_content: (
            PagesSinglePatchRequestDataAttributesHomePageContent | Unset
        )
        if isinstance(_home_page_content, Unset):
            home_page_content = UNSET
        else:
            home_page_content = (
                PagesSinglePatchRequestDataAttributesHomePageContent.from_dict(
                    _home_page_content
                )
            )

        title = d.pop("title", UNSET)

        pages_single_patch_request_data_attributes_obj = cls(
            home_page_content=home_page_content,
            title=title,
        )

        pages_single_patch_request_data_attributes_obj.additional_properties = d
        return pages_single_patch_request_data_attributes_obj

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

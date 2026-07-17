# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="WorkitemsSingleGetResponseDataRelationshipsCommentsLinks"
)


@_attrs_define
class WorkitemsSingleGetResponseDataRelationshipsCommentsLinks:
    """
    Attributes:
        related (str | Unset):  Example: server-host-name/application-
            path/projects/MyProjectId/workitems/MyWorkItemId/comments?revision=1234.
    """

    related: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        related = self.related

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if related is not UNSET:
            field_dict["related"] = related

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        related = d.pop("related", UNSET)

        workitems_single_get_response_data_relationships_comments_links_obj = (
            cls(
                related=related,
            )
        )

        workitems_single_get_response_data_relationships_comments_links_obj.additional_properties = d
        return (
            workitems_single_get_response_data_relationships_comments_links_obj
        )

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

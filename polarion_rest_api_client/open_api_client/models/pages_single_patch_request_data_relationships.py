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
    from ..models.pages_single_patch_request_data_relationships_watches import (
        PagesSinglePatchRequestDataRelationshipsWatches,
    )


T = TypeVar("T", bound="PagesSinglePatchRequestDataRelationships")


@_attrs_define
class PagesSinglePatchRequestDataRelationships:
    """
    Attributes:
        watches (PagesSinglePatchRequestDataRelationshipsWatches | Unset):
    """

    watches: PagesSinglePatchRequestDataRelationshipsWatches | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        watches: dict[str, Any] | Unset = UNSET
        if not isinstance(self.watches, Unset):
            watches = self.watches.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if watches is not UNSET:
            field_dict["watches"] = watches

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pages_single_patch_request_data_relationships_watches import (
            PagesSinglePatchRequestDataRelationshipsWatches,
        )

        d = dict(src_dict)
        _watches = d.pop("watches", UNSET)
        watches: PagesSinglePatchRequestDataRelationshipsWatches | Unset
        if isinstance(_watches, Unset):
            watches = UNSET
        else:
            watches = (
                PagesSinglePatchRequestDataRelationshipsWatches.from_dict(
                    _watches
                )
            )

        pages_single_patch_request_data_relationships_obj = cls(
            watches=watches,
        )

        pages_single_patch_request_data_relationships_obj.additional_properties = d
        return pages_single_patch_request_data_relationships_obj

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

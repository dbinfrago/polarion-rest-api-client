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
    from ..models.resource_reference import ResourceReference


T = TypeVar("T", bound="ResourceQueryContext")


@_attrs_define
class ResourceQueryContext:
    """
    Attributes:
        context_resource_reference (ResourceReference | Unset):
    """

    context_resource_reference: ResourceReference | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        context_resource_reference: dict[str, Any] | Unset = UNSET
        if not isinstance(self.context_resource_reference, Unset):
            context_resource_reference = (
                self.context_resource_reference.to_dict()
            )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if context_resource_reference is not UNSET:
            field_dict["contextResourceReference"] = context_resource_reference

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_reference import ResourceReference

        d = dict(src_dict)
        _context_resource_reference = d.pop("contextResourceReference", UNSET)
        context_resource_reference: ResourceReference | Unset
        if isinstance(_context_resource_reference, Unset):
            context_resource_reference = UNSET
        else:
            context_resource_reference = ResourceReference.from_dict(
                _context_resource_reference
            )

        resource_query_context_obj = cls(
            context_resource_reference=context_resource_reference,
        )

        resource_query_context_obj.additional_properties = d
        return resource_query_context_obj

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

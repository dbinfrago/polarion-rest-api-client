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
    from ..models.projects_single_patch_request_data_relationships_lead import (
        ProjectsSinglePatchRequestDataRelationshipsLead,
    )


T = TypeVar("T", bound="ProjectsSinglePatchRequestDataRelationships")


@_attrs_define
class ProjectsSinglePatchRequestDataRelationships:
    """
    Attributes:
        lead (ProjectsSinglePatchRequestDataRelationshipsLead | Unset):
    """

    lead: ProjectsSinglePatchRequestDataRelationshipsLead | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        lead: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lead, Unset):
            lead = self.lead.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lead is not UNSET:
            field_dict["lead"] = lead

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.projects_single_patch_request_data_relationships_lead import (
            ProjectsSinglePatchRequestDataRelationshipsLead,
        )

        d = dict(src_dict)
        _lead = d.pop("lead", UNSET)
        lead: ProjectsSinglePatchRequestDataRelationshipsLead | Unset
        if isinstance(_lead, Unset):
            lead = UNSET
        else:
            lead = ProjectsSinglePatchRequestDataRelationshipsLead.from_dict(
                _lead
            )

        projects_single_patch_request_data_relationships_obj = cls(
            lead=lead,
        )

        projects_single_patch_request_data_relationships_obj.additional_properties = d
        return projects_single_patch_request_data_relationships_obj

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

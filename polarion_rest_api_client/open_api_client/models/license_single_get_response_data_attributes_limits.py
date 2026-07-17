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
    from ..models.license_single_get_response_data_attributes_limits_documents_and_pages import (
        LicenseSingleGetResponseDataAttributesLimitsDocumentsAndPages,
    )
    from ..models.license_single_get_response_data_attributes_limits_projects import (
        LicenseSingleGetResponseDataAttributesLimitsProjects,
    )
    from ..models.license_single_get_response_data_attributes_limits_workitems import (
        LicenseSingleGetResponseDataAttributesLimitsWorkitems,
    )


T = TypeVar("T", bound="LicenseSingleGetResponseDataAttributesLimits")


@_attrs_define
class LicenseSingleGetResponseDataAttributesLimits:
    """
    Attributes:
        documents_and_pages (LicenseSingleGetResponseDataAttributesLimitsDocumentsAndPages | Unset):
        projects (LicenseSingleGetResponseDataAttributesLimitsProjects | Unset):
        workitems (LicenseSingleGetResponseDataAttributesLimitsWorkitems | Unset):
    """

    documents_and_pages: (
        LicenseSingleGetResponseDataAttributesLimitsDocumentsAndPages | Unset
    ) = UNSET
    projects: LicenseSingleGetResponseDataAttributesLimitsProjects | Unset = (
        UNSET
    )
    workitems: (
        LicenseSingleGetResponseDataAttributesLimitsWorkitems | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        documents_and_pages: dict[str, Any] | Unset = UNSET
        if not isinstance(self.documents_and_pages, Unset):
            documents_and_pages = self.documents_and_pages.to_dict()

        projects: dict[str, Any] | Unset = UNSET
        if not isinstance(self.projects, Unset):
            projects = self.projects.to_dict()

        workitems: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workitems, Unset):
            workitems = self.workitems.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if documents_and_pages is not UNSET:
            field_dict["documentsAndPages"] = documents_and_pages
        if projects is not UNSET:
            field_dict["projects"] = projects
        if workitems is not UNSET:
            field_dict["workitems"] = workitems

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.license_single_get_response_data_attributes_limits_documents_and_pages import (
            LicenseSingleGetResponseDataAttributesLimitsDocumentsAndPages,
        )
        from ..models.license_single_get_response_data_attributes_limits_projects import (
            LicenseSingleGetResponseDataAttributesLimitsProjects,
        )
        from ..models.license_single_get_response_data_attributes_limits_workitems import (
            LicenseSingleGetResponseDataAttributesLimitsWorkitems,
        )

        d = dict(src_dict)
        _documents_and_pages = d.pop("documentsAndPages", UNSET)
        documents_and_pages: (
            LicenseSingleGetResponseDataAttributesLimitsDocumentsAndPages
            | Unset
        )
        if isinstance(_documents_and_pages, Unset):
            documents_and_pages = UNSET
        else:
            documents_and_pages = LicenseSingleGetResponseDataAttributesLimitsDocumentsAndPages.from_dict(
                _documents_and_pages
            )

        _projects = d.pop("projects", UNSET)
        projects: LicenseSingleGetResponseDataAttributesLimitsProjects | Unset
        if isinstance(_projects, Unset):
            projects = UNSET
        else:
            projects = (
                LicenseSingleGetResponseDataAttributesLimitsProjects.from_dict(
                    _projects
                )
            )

        _workitems = d.pop("workitems", UNSET)
        workitems: (
            LicenseSingleGetResponseDataAttributesLimitsWorkitems | Unset
        )
        if isinstance(_workitems, Unset):
            workitems = UNSET
        else:
            workitems = LicenseSingleGetResponseDataAttributesLimitsWorkitems.from_dict(
                _workitems
            )

        license_single_get_response_data_attributes_limits_obj = cls(
            documents_and_pages=documents_and_pages,
            projects=projects,
            workitems=workitems,
        )

        license_single_get_response_data_attributes_limits_obj.additional_properties = d
        return license_single_get_response_data_attributes_limits_obj

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

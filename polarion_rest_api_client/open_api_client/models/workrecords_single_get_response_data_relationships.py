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
    from ..models.workrecords_single_get_response_data_relationships_project import (
        WorkrecordsSingleGetResponseDataRelationshipsProject,
    )
    from ..models.workrecords_single_get_response_data_relationships_user import (
        WorkrecordsSingleGetResponseDataRelationshipsUser,
    )


T = TypeVar("T", bound="WorkrecordsSingleGetResponseDataRelationships")


@_attrs_define
class WorkrecordsSingleGetResponseDataRelationships:
    """
    Attributes:
        project (WorkrecordsSingleGetResponseDataRelationshipsProject | Unset):
        user (WorkrecordsSingleGetResponseDataRelationshipsUser | Unset):
    """

    project: WorkrecordsSingleGetResponseDataRelationshipsProject | Unset = (
        UNSET
    )
    user: WorkrecordsSingleGetResponseDataRelationshipsUser | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        project: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project is not UNSET:
            field_dict["project"] = project
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workrecords_single_get_response_data_relationships_project import (
            WorkrecordsSingleGetResponseDataRelationshipsProject,
        )
        from ..models.workrecords_single_get_response_data_relationships_user import (
            WorkrecordsSingleGetResponseDataRelationshipsUser,
        )

        d = dict(src_dict)
        _project = d.pop("project", UNSET)
        project: WorkrecordsSingleGetResponseDataRelationshipsProject | Unset
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = (
                WorkrecordsSingleGetResponseDataRelationshipsProject.from_dict(
                    _project
                )
            )

        _user = d.pop("user", UNSET)
        user: WorkrecordsSingleGetResponseDataRelationshipsUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = WorkrecordsSingleGetResponseDataRelationshipsUser.from_dict(
                _user
            )

        workrecords_single_get_response_data_relationships_obj = cls(
            project=project,
            user=user,
        )

        workrecords_single_get_response_data_relationships_obj.additional_properties = d
        return workrecords_single_get_response_data_relationships_obj

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

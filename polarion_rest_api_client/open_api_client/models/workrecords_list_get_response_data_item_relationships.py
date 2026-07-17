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
    from ..models.workrecords_list_get_response_data_item_relationships_project import (
        WorkrecordsListGetResponseDataItemRelationshipsProject,
    )
    from ..models.workrecords_list_get_response_data_item_relationships_user import (
        WorkrecordsListGetResponseDataItemRelationshipsUser,
    )


T = TypeVar("T", bound="WorkrecordsListGetResponseDataItemRelationships")


@_attrs_define
class WorkrecordsListGetResponseDataItemRelationships:
    """
    Attributes:
        project (WorkrecordsListGetResponseDataItemRelationshipsProject | Unset):
        user (WorkrecordsListGetResponseDataItemRelationshipsUser | Unset):
    """

    project: WorkrecordsListGetResponseDataItemRelationshipsProject | Unset = (
        UNSET
    )
    user: WorkrecordsListGetResponseDataItemRelationshipsUser | Unset = UNSET
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
        from ..models.workrecords_list_get_response_data_item_relationships_project import (
            WorkrecordsListGetResponseDataItemRelationshipsProject,
        )
        from ..models.workrecords_list_get_response_data_item_relationships_user import (
            WorkrecordsListGetResponseDataItemRelationshipsUser,
        )

        d = dict(src_dict)
        _project = d.pop("project", UNSET)
        project: WorkrecordsListGetResponseDataItemRelationshipsProject | Unset
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = WorkrecordsListGetResponseDataItemRelationshipsProject.from_dict(
                _project
            )

        _user = d.pop("user", UNSET)
        user: WorkrecordsListGetResponseDataItemRelationshipsUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = (
                WorkrecordsListGetResponseDataItemRelationshipsUser.from_dict(
                    _user
                )
            )

        workrecords_list_get_response_data_item_relationships_obj = cls(
            project=project,
            user=user,
        )

        workrecords_list_get_response_data_item_relationships_obj.additional_properties = d
        return workrecords_list_get_response_data_item_relationships_obj

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

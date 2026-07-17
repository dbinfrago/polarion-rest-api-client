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
    from ..models.usergroups_single_get_response_data_relationships_global_roles import (
        UsergroupsSingleGetResponseDataRelationshipsGlobalRoles,
    )
    from ..models.usergroups_single_get_response_data_relationships_project_roles import (
        UsergroupsSingleGetResponseDataRelationshipsProjectRoles,
    )
    from ..models.usergroups_single_get_response_data_relationships_users import (
        UsergroupsSingleGetResponseDataRelationshipsUsers,
    )


T = TypeVar("T", bound="UsergroupsSingleGetResponseDataRelationships")


@_attrs_define
class UsergroupsSingleGetResponseDataRelationships:
    """
    Attributes:
        global_roles (UsergroupsSingleGetResponseDataRelationshipsGlobalRoles | Unset):
        project_roles (UsergroupsSingleGetResponseDataRelationshipsProjectRoles | Unset):
        users (UsergroupsSingleGetResponseDataRelationshipsUsers | Unset):
    """

    global_roles: (
        UsergroupsSingleGetResponseDataRelationshipsGlobalRoles | Unset
    ) = UNSET
    project_roles: (
        UsergroupsSingleGetResponseDataRelationshipsProjectRoles | Unset
    ) = UNSET
    users: UsergroupsSingleGetResponseDataRelationshipsUsers | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        global_roles: dict[str, Any] | Unset = UNSET
        if not isinstance(self.global_roles, Unset):
            global_roles = self.global_roles.to_dict()

        project_roles: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_roles, Unset):
            project_roles = self.project_roles.to_dict()

        users: dict[str, Any] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = self.users.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if global_roles is not UNSET:
            field_dict["globalRoles"] = global_roles
        if project_roles is not UNSET:
            field_dict["projectRoles"] = project_roles
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.usergroups_single_get_response_data_relationships_global_roles import (
            UsergroupsSingleGetResponseDataRelationshipsGlobalRoles,
        )
        from ..models.usergroups_single_get_response_data_relationships_project_roles import (
            UsergroupsSingleGetResponseDataRelationshipsProjectRoles,
        )
        from ..models.usergroups_single_get_response_data_relationships_users import (
            UsergroupsSingleGetResponseDataRelationshipsUsers,
        )

        d = dict(src_dict)
        _global_roles = d.pop("globalRoles", UNSET)
        global_roles: (
            UsergroupsSingleGetResponseDataRelationshipsGlobalRoles | Unset
        )
        if isinstance(_global_roles, Unset):
            global_roles = UNSET
        else:
            global_roles = UsergroupsSingleGetResponseDataRelationshipsGlobalRoles.from_dict(
                _global_roles
            )

        _project_roles = d.pop("projectRoles", UNSET)
        project_roles: (
            UsergroupsSingleGetResponseDataRelationshipsProjectRoles | Unset
        )
        if isinstance(_project_roles, Unset):
            project_roles = UNSET
        else:
            project_roles = UsergroupsSingleGetResponseDataRelationshipsProjectRoles.from_dict(
                _project_roles
            )

        _users = d.pop("users", UNSET)
        users: UsergroupsSingleGetResponseDataRelationshipsUsers | Unset
        if isinstance(_users, Unset):
            users = UNSET
        else:
            users = (
                UsergroupsSingleGetResponseDataRelationshipsUsers.from_dict(
                    _users
                )
            )

        usergroups_single_get_response_data_relationships_obj = cls(
            global_roles=global_roles,
            project_roles=project_roles,
            users=users,
        )

        usergroups_single_get_response_data_relationships_obj.additional_properties = d
        return usergroups_single_get_response_data_relationships_obj

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

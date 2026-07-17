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
    from ..models.users_single_get_response_data_relationships_add_on_license_slots import (
        UsersSingleGetResponseDataRelationshipsAddOnLicenseSlots,
    )
    from ..models.users_single_get_response_data_relationships_base_license_slot import (
        UsersSingleGetResponseDataRelationshipsBaseLicenseSlot,
    )
    from ..models.users_single_get_response_data_relationships_global_roles import (
        UsersSingleGetResponseDataRelationshipsGlobalRoles,
    )
    from ..models.users_single_get_response_data_relationships_project_roles import (
        UsersSingleGetResponseDataRelationshipsProjectRoles,
    )
    from ..models.users_single_get_response_data_relationships_user_groups import (
        UsersSingleGetResponseDataRelationshipsUserGroups,
    )


T = TypeVar("T", bound="UsersSingleGetResponseDataRelationships")


@_attrs_define
class UsersSingleGetResponseDataRelationships:
    """
    Attributes:
        add_on_license_slots (UsersSingleGetResponseDataRelationshipsAddOnLicenseSlots | Unset):
        base_license_slot (UsersSingleGetResponseDataRelationshipsBaseLicenseSlot | Unset):
        global_roles (UsersSingleGetResponseDataRelationshipsGlobalRoles | Unset):
        project_roles (UsersSingleGetResponseDataRelationshipsProjectRoles | Unset):
        user_groups (UsersSingleGetResponseDataRelationshipsUserGroups | Unset):
    """

    add_on_license_slots: (
        UsersSingleGetResponseDataRelationshipsAddOnLicenseSlots | Unset
    ) = UNSET
    base_license_slot: (
        UsersSingleGetResponseDataRelationshipsBaseLicenseSlot | Unset
    ) = UNSET
    global_roles: (
        UsersSingleGetResponseDataRelationshipsGlobalRoles | Unset
    ) = UNSET
    project_roles: (
        UsersSingleGetResponseDataRelationshipsProjectRoles | Unset
    ) = UNSET
    user_groups: UsersSingleGetResponseDataRelationshipsUserGroups | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        add_on_license_slots: dict[str, Any] | Unset = UNSET
        if not isinstance(self.add_on_license_slots, Unset):
            add_on_license_slots = self.add_on_license_slots.to_dict()

        base_license_slot: dict[str, Any] | Unset = UNSET
        if not isinstance(self.base_license_slot, Unset):
            base_license_slot = self.base_license_slot.to_dict()

        global_roles: dict[str, Any] | Unset = UNSET
        if not isinstance(self.global_roles, Unset):
            global_roles = self.global_roles.to_dict()

        project_roles: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_roles, Unset):
            project_roles = self.project_roles.to_dict()

        user_groups: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user_groups, Unset):
            user_groups = self.user_groups.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if add_on_license_slots is not UNSET:
            field_dict["addOnLicenseSlots"] = add_on_license_slots
        if base_license_slot is not UNSET:
            field_dict["baseLicenseSlot"] = base_license_slot
        if global_roles is not UNSET:
            field_dict["globalRoles"] = global_roles
        if project_roles is not UNSET:
            field_dict["projectRoles"] = project_roles
        if user_groups is not UNSET:
            field_dict["userGroups"] = user_groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.users_single_get_response_data_relationships_add_on_license_slots import (
            UsersSingleGetResponseDataRelationshipsAddOnLicenseSlots,
        )
        from ..models.users_single_get_response_data_relationships_base_license_slot import (
            UsersSingleGetResponseDataRelationshipsBaseLicenseSlot,
        )
        from ..models.users_single_get_response_data_relationships_global_roles import (
            UsersSingleGetResponseDataRelationshipsGlobalRoles,
        )
        from ..models.users_single_get_response_data_relationships_project_roles import (
            UsersSingleGetResponseDataRelationshipsProjectRoles,
        )
        from ..models.users_single_get_response_data_relationships_user_groups import (
            UsersSingleGetResponseDataRelationshipsUserGroups,
        )

        d = dict(src_dict)
        _add_on_license_slots = d.pop("addOnLicenseSlots", UNSET)
        add_on_license_slots: (
            UsersSingleGetResponseDataRelationshipsAddOnLicenseSlots | Unset
        )
        if isinstance(_add_on_license_slots, Unset):
            add_on_license_slots = UNSET
        else:
            add_on_license_slots = UsersSingleGetResponseDataRelationshipsAddOnLicenseSlots.from_dict(
                _add_on_license_slots
            )

        _base_license_slot = d.pop("baseLicenseSlot", UNSET)
        base_license_slot: (
            UsersSingleGetResponseDataRelationshipsBaseLicenseSlot | Unset
        )
        if isinstance(_base_license_slot, Unset):
            base_license_slot = UNSET
        else:
            base_license_slot = UsersSingleGetResponseDataRelationshipsBaseLicenseSlot.from_dict(
                _base_license_slot
            )

        _global_roles = d.pop("globalRoles", UNSET)
        global_roles: (
            UsersSingleGetResponseDataRelationshipsGlobalRoles | Unset
        )
        if isinstance(_global_roles, Unset):
            global_roles = UNSET
        else:
            global_roles = (
                UsersSingleGetResponseDataRelationshipsGlobalRoles.from_dict(
                    _global_roles
                )
            )

        _project_roles = d.pop("projectRoles", UNSET)
        project_roles: (
            UsersSingleGetResponseDataRelationshipsProjectRoles | Unset
        )
        if isinstance(_project_roles, Unset):
            project_roles = UNSET
        else:
            project_roles = (
                UsersSingleGetResponseDataRelationshipsProjectRoles.from_dict(
                    _project_roles
                )
            )

        _user_groups = d.pop("userGroups", UNSET)
        user_groups: UsersSingleGetResponseDataRelationshipsUserGroups | Unset
        if isinstance(_user_groups, Unset):
            user_groups = UNSET
        else:
            user_groups = (
                UsersSingleGetResponseDataRelationshipsUserGroups.from_dict(
                    _user_groups
                )
            )

        users_single_get_response_data_relationships_obj = cls(
            add_on_license_slots=add_on_license_slots,
            base_license_slot=base_license_slot,
            global_roles=global_roles,
            project_roles=project_roles,
            user_groups=user_groups,
        )

        users_single_get_response_data_relationships_obj.additional_properties = d
        return users_single_get_response_data_relationships_obj

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

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
    from ..models.users_list_get_response_data_item_attributes_description import (
        UsersListGetResponseDataItemAttributesDescription,
    )


T = TypeVar("T", bound="UsersListGetResponseDataItemAttributes")


@_attrs_define
class UsersListGetResponseDataItemAttributes:
    """
    Attributes:
        avatar_url (str | Unset):  Example: http://server-host-name/application-
            path/icons/avatar/MyUserId/avatar.png?revision=1234.
        description (UsersListGetResponseDataItemAttributesDescription | Unset):
        disabled_notifications (bool | Unset):
        email (str | Unset):  Example: Email.
        id (str | Unset):  Example: MyUserId.
        initials (str | Unset):  Example: Initials.
        name (str | Unset):  Example: Name.
    """

    avatar_url: str | Unset = UNSET
    description: UsersListGetResponseDataItemAttributesDescription | Unset = (
        UNSET
    )
    disabled_notifications: bool | Unset = UNSET
    email: str | Unset = UNSET
    id: str | Unset = UNSET
    initials: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        avatar_url = self.avatar_url

        description: dict[str, Any] | Unset = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict()

        disabled_notifications = self.disabled_notifications

        email = self.email

        id = self.id

        initials = self.initials

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avatar_url is not UNSET:
            field_dict["avatarUrl"] = avatar_url
        if description is not UNSET:
            field_dict["description"] = description
        if disabled_notifications is not UNSET:
            field_dict["disabledNotifications"] = disabled_notifications
        if email is not UNSET:
            field_dict["email"] = email
        if id is not UNSET:
            field_dict["id"] = id
        if initials is not UNSET:
            field_dict["initials"] = initials
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.users_list_get_response_data_item_attributes_description import (
            UsersListGetResponseDataItemAttributesDescription,
        )

        d = dict(src_dict)
        avatar_url = d.pop("avatarUrl", UNSET)

        _description = d.pop("description", UNSET)
        description: UsersListGetResponseDataItemAttributesDescription | Unset
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = (
                UsersListGetResponseDataItemAttributesDescription.from_dict(
                    _description
                )
            )

        disabled_notifications = d.pop("disabledNotifications", UNSET)

        email = d.pop("email", UNSET)

        id = d.pop("id", UNSET)

        initials = d.pop("initials", UNSET)

        name = d.pop("name", UNSET)

        users_list_get_response_data_item_attributes_obj = cls(
            avatar_url=avatar_url,
            description=description,
            disabled_notifications=disabled_notifications,
            email=email,
            id=id,
            initials=initials,
            name=name,
        )

        users_list_get_response_data_item_attributes_obj.additional_properties = d
        return users_list_get_response_data_item_attributes_obj

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

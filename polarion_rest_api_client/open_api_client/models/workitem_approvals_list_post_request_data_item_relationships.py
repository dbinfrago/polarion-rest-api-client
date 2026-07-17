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
    from ..models.workitem_approvals_list_post_request_data_item_relationships_user import (
        WorkitemApprovalsListPostRequestDataItemRelationshipsUser,
    )


T = TypeVar("T", bound="WorkitemApprovalsListPostRequestDataItemRelationships")


@_attrs_define
class WorkitemApprovalsListPostRequestDataItemRelationships:
    """
    Attributes:
        user (WorkitemApprovalsListPostRequestDataItemRelationshipsUser | Unset):
    """

    user: WorkitemApprovalsListPostRequestDataItemRelationshipsUser | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workitem_approvals_list_post_request_data_item_relationships_user import (
            WorkitemApprovalsListPostRequestDataItemRelationshipsUser,
        )

        d = dict(src_dict)
        _user = d.pop("user", UNSET)
        user: WorkitemApprovalsListPostRequestDataItemRelationshipsUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = WorkitemApprovalsListPostRequestDataItemRelationshipsUser.from_dict(
                _user
            )

        workitem_approvals_list_post_request_data_item_relationships_obj = cls(
            user=user,
        )

        workitem_approvals_list_post_request_data_item_relationships_obj.additional_properties = d
        return workitem_approvals_list_post_request_data_item_relationships_obj

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

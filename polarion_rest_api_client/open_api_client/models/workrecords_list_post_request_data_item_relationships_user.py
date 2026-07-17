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
    from ..models.workrecords_list_post_request_data_item_relationships_user_data import (
        WorkrecordsListPostRequestDataItemRelationshipsUserData,
    )


T = TypeVar("T", bound="WorkrecordsListPostRequestDataItemRelationshipsUser")


@_attrs_define
class WorkrecordsListPostRequestDataItemRelationshipsUser:
    """
    Attributes:
        data (WorkrecordsListPostRequestDataItemRelationshipsUserData | Unset):
    """

    data: WorkrecordsListPostRequestDataItemRelationshipsUserData | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workrecords_list_post_request_data_item_relationships_user_data import (
            WorkrecordsListPostRequestDataItemRelationshipsUserData,
        )

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: WorkrecordsListPostRequestDataItemRelationshipsUserData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = WorkrecordsListPostRequestDataItemRelationshipsUserData.from_dict(
                _data
            )

        workrecords_list_post_request_data_item_relationships_user_obj = cls(
            data=data,
        )

        workrecords_list_post_request_data_item_relationships_user_obj.additional_properties = d
        return workrecords_list_post_request_data_item_relationships_user_obj

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

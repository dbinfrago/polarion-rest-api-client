# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkrecordsSingleGetResponseDataAttributes")


@_attrs_define
class WorkrecordsSingleGetResponseDataAttributes:
    """
    Attributes:
        comment (str | Unset):  Example: Comment.
        date (datetime.date | Unset):  Example: 1970-01-01.
        id (str | Unset):
        time_spent (str | Unset):  Example: 5 1/2d.
        type_ (str | Unset):  Example: task.
    """

    comment: str | Unset = UNSET
    date: datetime.date | Unset = UNSET
    id: str | Unset = UNSET
    time_spent: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        comment = self.comment

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        id = self.id

        time_spent = self.time_spent

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comment is not UNSET:
            field_dict["comment"] = comment
        if date is not UNSET:
            field_dict["date"] = date
        if id is not UNSET:
            field_dict["id"] = id
        if time_spent is not UNSET:
            field_dict["timeSpent"] = time_spent
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comment = d.pop("comment", UNSET)

        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = datetime.date.fromisoformat(_date)

        id = d.pop("id", UNSET)

        time_spent = d.pop("timeSpent", UNSET)

        type_ = d.pop("type", UNSET)

        workrecords_single_get_response_data_attributes_obj = cls(
            comment=comment,
            date=date,
            id=id,
            time_spent=time_spent,
            type_=type_,
        )

        workrecords_single_get_response_data_attributes_obj.additional_properties = d
        return workrecords_single_get_response_data_attributes_obj

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

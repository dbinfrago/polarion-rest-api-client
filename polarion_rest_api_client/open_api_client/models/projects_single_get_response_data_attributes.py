# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import datetime
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
    from ..models.projects_single_get_response_data_attributes_description import (
        ProjectsSingleGetResponseDataAttributesDescription,
    )


T = TypeVar("T", bound="ProjectsSingleGetResponseDataAttributes")


@_attrs_define
class ProjectsSingleGetResponseDataAttributes:
    """
    Attributes:
        active (bool | Unset):
        color (str | Unset):  Example: Color.
        description (ProjectsSingleGetResponseDataAttributesDescription | Unset):
        finish (datetime.date | Unset):  Example: 1970-01-01.
        icon (str | Unset):  Example: Icon.
        id (str | Unset):  Example: MyProjectId.
        lock_work_records_date (datetime.date | Unset):  Example: 1970-01-01.
        name (str | Unset):  Example: Name.
        start (datetime.date | Unset):  Example: 1970-01-01.
        tracker_prefix (str | Unset):  Example: Tracker Prefix.
    """

    active: bool | Unset = UNSET
    color: str | Unset = UNSET
    description: ProjectsSingleGetResponseDataAttributesDescription | Unset = (
        UNSET
    )
    finish: datetime.date | Unset = UNSET
    icon: str | Unset = UNSET
    id: str | Unset = UNSET
    lock_work_records_date: datetime.date | Unset = UNSET
    name: str | Unset = UNSET
    start: datetime.date | Unset = UNSET
    tracker_prefix: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        color = self.color

        description: dict[str, Any] | Unset = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict()

        finish: str | Unset = UNSET
        if not isinstance(self.finish, Unset):
            finish = self.finish.isoformat()

        icon = self.icon

        id = self.id

        lock_work_records_date: str | Unset = UNSET
        if not isinstance(self.lock_work_records_date, Unset):
            lock_work_records_date = self.lock_work_records_date.isoformat()

        name = self.name

        start: str | Unset = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat()

        tracker_prefix = self.tracker_prefix

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if color is not UNSET:
            field_dict["color"] = color
        if description is not UNSET:
            field_dict["description"] = description
        if finish is not UNSET:
            field_dict["finish"] = finish
        if icon is not UNSET:
            field_dict["icon"] = icon
        if id is not UNSET:
            field_dict["id"] = id
        if lock_work_records_date is not UNSET:
            field_dict["lockWorkRecordsDate"] = lock_work_records_date
        if name is not UNSET:
            field_dict["name"] = name
        if start is not UNSET:
            field_dict["start"] = start
        if tracker_prefix is not UNSET:
            field_dict["trackerPrefix"] = tracker_prefix

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.projects_single_get_response_data_attributes_description import (
            ProjectsSingleGetResponseDataAttributesDescription,
        )

        d = dict(src_dict)
        active = d.pop("active", UNSET)

        color = d.pop("color", UNSET)

        _description = d.pop("description", UNSET)
        description: ProjectsSingleGetResponseDataAttributesDescription | Unset
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = (
                ProjectsSingleGetResponseDataAttributesDescription.from_dict(
                    _description
                )
            )

        _finish = d.pop("finish", UNSET)
        finish: datetime.date | Unset
        if isinstance(_finish, Unset):
            finish = UNSET
        else:
            finish = datetime.date.fromisoformat(_finish)

        icon = d.pop("icon", UNSET)

        id = d.pop("id", UNSET)

        _lock_work_records_date = d.pop("lockWorkRecordsDate", UNSET)
        lock_work_records_date: datetime.date | Unset
        if isinstance(_lock_work_records_date, Unset):
            lock_work_records_date = UNSET
        else:
            lock_work_records_date = datetime.date.fromisoformat(
                _lock_work_records_date
            )

        name = d.pop("name", UNSET)

        _start = d.pop("start", UNSET)
        start: datetime.date | Unset
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = datetime.date.fromisoformat(_start)

        tracker_prefix = d.pop("trackerPrefix", UNSET)

        projects_single_get_response_data_attributes_obj = cls(
            active=active,
            color=color,
            description=description,
            finish=finish,
            icon=icon,
            id=id,
            lock_work_records_date=lock_work_records_date,
            name=name,
            start=start,
            tracker_prefix=tracker_prefix,
        )

        projects_single_get_response_data_attributes_obj.additional_properties = d
        return projects_single_get_response_data_attributes_obj

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

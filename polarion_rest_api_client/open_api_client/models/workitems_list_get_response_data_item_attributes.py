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
    from ..models.workitems_list_get_response_data_item_attributes_description import (
        WorkitemsListGetResponseDataItemAttributesDescription,
    )
    from ..models.workitems_list_get_response_data_item_attributes_hyperlinks_item import (
        WorkitemsListGetResponseDataItemAttributesHyperlinksItem,
    )


T = TypeVar("T", bound="WorkitemsListGetResponseDataItemAttributes")


@_attrs_define
class WorkitemsListGetResponseDataItemAttributes:
    """
    Attributes:
        created (datetime.datetime | Unset):  Example: 1970-01-01T00:00:00Z.
        description (WorkitemsListGetResponseDataItemAttributesDescription | Unset):
        due_date (datetime.date | Unset):  Example: 1970-01-01.
        hyperlinks (list[WorkitemsListGetResponseDataItemAttributesHyperlinksItem] | Unset):
        id (str | Unset):  Example: MyWorkItemId.
        initial_estimate (str | Unset):  Example: 5 1/2d.
        outline_number (str | Unset):  Example: 1.11.
        planned_end (datetime.datetime | Unset):  Example: 1970-01-01T00:00:00Z.
        planned_start (datetime.datetime | Unset):  Example: 1970-01-01T00:00:00Z.
        priority (str | Unset):  Example: 90.0.
        remaining_estimate (str | Unset):  Example: 5 1/2d.
        resolution (str | Unset):  Example: done.
        resolved_on (datetime.datetime | Unset):  Example: 1970-01-01T00:00:00Z.
        severity (str | Unset):  Example: blocker.
        status (str | Unset):  Example: open.
        time_spent (str | Unset):  Example: 5 1/2d.
        title (str | Unset):  Example: Title.
        type_ (str | Unset):  Example: task.
        updated (datetime.datetime | Unset):  Example: 1970-01-01T00:00:00Z.
    """

    created: datetime.datetime | Unset = UNSET
    description: (
        WorkitemsListGetResponseDataItemAttributesDescription | Unset
    ) = UNSET
    due_date: datetime.date | Unset = UNSET
    hyperlinks: (
        list[WorkitemsListGetResponseDataItemAttributesHyperlinksItem] | Unset
    ) = UNSET
    id: str | Unset = UNSET
    initial_estimate: str | Unset = UNSET
    outline_number: str | Unset = UNSET
    planned_end: datetime.datetime | Unset = UNSET
    planned_start: datetime.datetime | Unset = UNSET
    priority: str | Unset = UNSET
    remaining_estimate: str | Unset = UNSET
    resolution: str | Unset = UNSET
    resolved_on: datetime.datetime | Unset = UNSET
    severity: str | Unset = UNSET
    status: str | Unset = UNSET
    time_spent: str | Unset = UNSET
    title: str | Unset = UNSET
    type_: str | Unset = UNSET
    updated: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        description: dict[str, Any] | Unset = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict()

        due_date: str | Unset = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        hyperlinks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.hyperlinks, Unset):
            hyperlinks = []
            for hyperlinks_item_data in self.hyperlinks:
                hyperlinks_item = hyperlinks_item_data.to_dict()
                hyperlinks.append(hyperlinks_item)

        id = self.id

        initial_estimate = self.initial_estimate

        outline_number = self.outline_number

        planned_end: str | Unset = UNSET
        if not isinstance(self.planned_end, Unset):
            planned_end = self.planned_end.isoformat()

        planned_start: str | Unset = UNSET
        if not isinstance(self.planned_start, Unset):
            planned_start = self.planned_start.isoformat()

        priority = self.priority

        remaining_estimate = self.remaining_estimate

        resolution = self.resolution

        resolved_on: str | Unset = UNSET
        if not isinstance(self.resolved_on, Unset):
            resolved_on = self.resolved_on.isoformat()

        severity = self.severity

        status = self.status

        time_spent = self.time_spent

        title = self.title

        type_ = self.type_

        updated: str | Unset = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if description is not UNSET:
            field_dict["description"] = description
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if hyperlinks is not UNSET:
            field_dict["hyperlinks"] = hyperlinks
        if id is not UNSET:
            field_dict["id"] = id
        if initial_estimate is not UNSET:
            field_dict["initialEstimate"] = initial_estimate
        if outline_number is not UNSET:
            field_dict["outlineNumber"] = outline_number
        if planned_end is not UNSET:
            field_dict["plannedEnd"] = planned_end
        if planned_start is not UNSET:
            field_dict["plannedStart"] = planned_start
        if priority is not UNSET:
            field_dict["priority"] = priority
        if remaining_estimate is not UNSET:
            field_dict["remainingEstimate"] = remaining_estimate
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if resolved_on is not UNSET:
            field_dict["resolvedOn"] = resolved_on
        if severity is not UNSET:
            field_dict["severity"] = severity
        if status is not UNSET:
            field_dict["status"] = status
        if time_spent is not UNSET:
            field_dict["timeSpent"] = time_spent
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workitems_list_get_response_data_item_attributes_description import (
            WorkitemsListGetResponseDataItemAttributesDescription,
        )
        from ..models.workitems_list_get_response_data_item_attributes_hyperlinks_item import (
            WorkitemsListGetResponseDataItemAttributesHyperlinksItem,
        )

        d = dict(src_dict)
        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = datetime.datetime.fromisoformat(_created)

        _description = d.pop("description", UNSET)
        description: (
            WorkitemsListGetResponseDataItemAttributesDescription | Unset
        )
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = WorkitemsListGetResponseDataItemAttributesDescription.from_dict(
                _description
            )

        _due_date = d.pop("dueDate", UNSET)
        due_date: datetime.date | Unset
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = datetime.date.fromisoformat(_due_date)

        _hyperlinks = d.pop("hyperlinks", UNSET)
        hyperlinks: (
            list[WorkitemsListGetResponseDataItemAttributesHyperlinksItem]
            | Unset
        ) = UNSET
        if _hyperlinks is not UNSET:
            hyperlinks = []
            for hyperlinks_item_data in _hyperlinks:
                hyperlinks_item = WorkitemsListGetResponseDataItemAttributesHyperlinksItem.from_dict(
                    hyperlinks_item_data
                )

                hyperlinks.append(hyperlinks_item)

        id = d.pop("id", UNSET)

        initial_estimate = d.pop("initialEstimate", UNSET)

        outline_number = d.pop("outlineNumber", UNSET)

        _planned_end = d.pop("plannedEnd", UNSET)
        planned_end: datetime.datetime | Unset
        if isinstance(_planned_end, Unset):
            planned_end = UNSET
        else:
            planned_end = datetime.datetime.fromisoformat(_planned_end)

        _planned_start = d.pop("plannedStart", UNSET)
        planned_start: datetime.datetime | Unset
        if isinstance(_planned_start, Unset):
            planned_start = UNSET
        else:
            planned_start = datetime.datetime.fromisoformat(_planned_start)

        priority = d.pop("priority", UNSET)

        remaining_estimate = d.pop("remainingEstimate", UNSET)

        resolution = d.pop("resolution", UNSET)

        _resolved_on = d.pop("resolvedOn", UNSET)
        resolved_on: datetime.datetime | Unset
        if isinstance(_resolved_on, Unset):
            resolved_on = UNSET
        else:
            resolved_on = datetime.datetime.fromisoformat(_resolved_on)

        severity = d.pop("severity", UNSET)

        status = d.pop("status", UNSET)

        time_spent = d.pop("timeSpent", UNSET)

        title = d.pop("title", UNSET)

        type_ = d.pop("type", UNSET)

        _updated = d.pop("updated", UNSET)
        updated: datetime.datetime | Unset
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = datetime.datetime.fromisoformat(_updated)

        workitems_list_get_response_data_item_attributes_obj = cls(
            created=created,
            description=description,
            due_date=due_date,
            hyperlinks=hyperlinks,
            id=id,
            initial_estimate=initial_estimate,
            outline_number=outline_number,
            planned_end=planned_end,
            planned_start=planned_start,
            priority=priority,
            remaining_estimate=remaining_estimate,
            resolution=resolution,
            resolved_on=resolved_on,
            severity=severity,
            status=status,
            time_spent=time_spent,
            title=title,
            type_=type_,
            updated=updated,
        )

        workitems_list_get_response_data_item_attributes_obj.additional_properties = d
        return workitems_list_get_response_data_item_attributes_obj

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

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
    from ..models.workitems_list_post_request_data_item_attributes_description import (
        WorkitemsListPostRequestDataItemAttributesDescription,
    )
    from ..models.workitems_list_post_request_data_item_attributes_hyperlinks_item import (
        WorkitemsListPostRequestDataItemAttributesHyperlinksItem,
    )


T = TypeVar("T", bound="WorkitemsListPostRequestDataItemAttributes")


@_attrs_define
class WorkitemsListPostRequestDataItemAttributes:
    """
    Attributes:
        type_ (str):  Example: task.
        description (WorkitemsListPostRequestDataItemAttributesDescription | Unset):
        due_date (datetime.date | Unset):  Example: 1970-01-01.
        hyperlinks (list[WorkitemsListPostRequestDataItemAttributesHyperlinksItem] | Unset):
        initial_estimate (str | Unset):  Example: 5 1/2d.
        priority (str | Unset):  Example: 90.0.
        remaining_estimate (str | Unset):  Example: 5 1/2d.
        resolution (str | Unset):  Example: done.
        resolved_on (datetime.datetime | Unset):  Example: 1970-01-01T00:00:00Z.
        severity (str | Unset):  Example: blocker.
        status (str | Unset):  Example: open.
        time_spent (str | Unset):  Example: 5 1/2d.
        title (str | Unset):  Example: Title.
    """

    type_: str
    description: (
        WorkitemsListPostRequestDataItemAttributesDescription | Unset
    ) = UNSET
    due_date: datetime.date | Unset = UNSET
    hyperlinks: (
        list[WorkitemsListPostRequestDataItemAttributesHyperlinksItem] | Unset
    ) = UNSET
    initial_estimate: str | Unset = UNSET
    priority: str | Unset = UNSET
    remaining_estimate: str | Unset = UNSET
    resolution: str | Unset = UNSET
    resolved_on: datetime.datetime | Unset = UNSET
    severity: str | Unset = UNSET
    status: str | Unset = UNSET
    time_spent: str | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

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

        initial_estimate = self.initial_estimate

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if hyperlinks is not UNSET:
            field_dict["hyperlinks"] = hyperlinks
        if initial_estimate is not UNSET:
            field_dict["initialEstimate"] = initial_estimate
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workitems_list_post_request_data_item_attributes_description import (
            WorkitemsListPostRequestDataItemAttributesDescription,
        )
        from ..models.workitems_list_post_request_data_item_attributes_hyperlinks_item import (
            WorkitemsListPostRequestDataItemAttributesHyperlinksItem,
        )

        d = dict(src_dict)
        type_ = d.pop("type")

        _description = d.pop("description", UNSET)
        description: (
            WorkitemsListPostRequestDataItemAttributesDescription | Unset
        )
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = WorkitemsListPostRequestDataItemAttributesDescription.from_dict(
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
            list[WorkitemsListPostRequestDataItemAttributesHyperlinksItem]
            | Unset
        ) = UNSET
        if _hyperlinks is not UNSET:
            hyperlinks = []
            for hyperlinks_item_data in _hyperlinks:
                hyperlinks_item = WorkitemsListPostRequestDataItemAttributesHyperlinksItem.from_dict(
                    hyperlinks_item_data
                )

                hyperlinks.append(hyperlinks_item)

        initial_estimate = d.pop("initialEstimate", UNSET)

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

        workitems_list_post_request_data_item_attributes_obj = cls(
            type_=type_,
            description=description,
            due_date=due_date,
            hyperlinks=hyperlinks,
            initial_estimate=initial_estimate,
            priority=priority,
            remaining_estimate=remaining_estimate,
            resolution=resolution,
            resolved_on=resolved_on,
            severity=severity,
            status=status,
            time_spent=time_spent,
            title=title,
        )

        workitems_list_post_request_data_item_attributes_obj.additional_properties = d
        return workitems_list_post_request_data_item_attributes_obj

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

# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.plans_list_post_request_data_item_attributes_calculation_type import (
    PlansListPostRequestDataItemAttributesCalculationType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plans_list_post_request_data_item_attributes_description import (
        PlansListPostRequestDataItemAttributesDescription,
    )
    from ..models.plans_list_post_request_data_item_attributes_home_page_content import (
        PlansListPostRequestDataItemAttributesHomePageContent,
    )


T = TypeVar("T", bound="PlansListPostRequestDataItemAttributes")


@_attrs_define
class PlansListPostRequestDataItemAttributes:
    """
    Attributes:
        allowed_types (list[str] | Unset):
        calculation_type (PlansListPostRequestDataItemAttributesCalculationType | Unset):  Example: timeBased.
        capacity (float | Unset):
        color (str | Unset):  Example: Color.
        default_estimate (float | Unset):
        description (PlansListPostRequestDataItemAttributesDescription | Unset):
        due_date (datetime.date | Unset):  Example: 1970-01-01.
        estimation_field (str | Unset):  Example: Estimation Field.
        finished_on (datetime.datetime | Unset):  Example: 1970-01-01T00:00:00Z.
        home_page_content (PlansListPostRequestDataItemAttributesHomePageContent | Unset):
        id (str | Unset):  Example: ID.
        is_template (bool | Unset):
        name (str | Unset):  Example: Name.
        previous_time_spent (str | Unset):  Example: 5 1/2d.
        prioritization_field (str | Unset):  Example: Prioritization Field.
        sort_order (int | Unset):
        start_date (datetime.date | Unset):  Example: 1970-01-01.
        started_on (datetime.datetime | Unset):  Example: 1970-01-01T00:00:00Z.
        status (str | Unset):
        use_report_from_template (bool | Unset):
    """

    allowed_types: list[str] | Unset = UNSET
    calculation_type: (
        PlansListPostRequestDataItemAttributesCalculationType | Unset
    ) = UNSET
    capacity: float | Unset = UNSET
    color: str | Unset = UNSET
    default_estimate: float | Unset = UNSET
    description: PlansListPostRequestDataItemAttributesDescription | Unset = (
        UNSET
    )
    due_date: datetime.date | Unset = UNSET
    estimation_field: str | Unset = UNSET
    finished_on: datetime.datetime | Unset = UNSET
    home_page_content: (
        PlansListPostRequestDataItemAttributesHomePageContent | Unset
    ) = UNSET
    id: str | Unset = UNSET
    is_template: bool | Unset = UNSET
    name: str | Unset = UNSET
    previous_time_spent: str | Unset = UNSET
    prioritization_field: str | Unset = UNSET
    sort_order: int | Unset = UNSET
    start_date: datetime.date | Unset = UNSET
    started_on: datetime.datetime | Unset = UNSET
    status: str | Unset = UNSET
    use_report_from_template: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        allowed_types: list[str] | Unset = UNSET
        if not isinstance(self.allowed_types, Unset):
            allowed_types = self.allowed_types

        calculation_type: str | Unset = UNSET
        if not isinstance(self.calculation_type, Unset):
            calculation_type = self.calculation_type.value

        capacity = self.capacity

        color = self.color

        default_estimate = self.default_estimate

        description: dict[str, Any] | Unset = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict()

        due_date: str | Unset = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        estimation_field = self.estimation_field

        finished_on: str | Unset = UNSET
        if not isinstance(self.finished_on, Unset):
            finished_on = self.finished_on.isoformat()

        home_page_content: dict[str, Any] | Unset = UNSET
        if not isinstance(self.home_page_content, Unset):
            home_page_content = self.home_page_content.to_dict()

        id = self.id

        is_template = self.is_template

        name = self.name

        previous_time_spent = self.previous_time_spent

        prioritization_field = self.prioritization_field

        sort_order = self.sort_order

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        started_on: str | Unset = UNSET
        if not isinstance(self.started_on, Unset):
            started_on = self.started_on.isoformat()

        status = self.status

        use_report_from_template = self.use_report_from_template

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allowed_types is not UNSET:
            field_dict["allowedTypes"] = allowed_types
        if calculation_type is not UNSET:
            field_dict["calculationType"] = calculation_type
        if capacity is not UNSET:
            field_dict["capacity"] = capacity
        if color is not UNSET:
            field_dict["color"] = color
        if default_estimate is not UNSET:
            field_dict["defaultEstimate"] = default_estimate
        if description is not UNSET:
            field_dict["description"] = description
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if estimation_field is not UNSET:
            field_dict["estimationField"] = estimation_field
        if finished_on is not UNSET:
            field_dict["finishedOn"] = finished_on
        if home_page_content is not UNSET:
            field_dict["homePageContent"] = home_page_content
        if id is not UNSET:
            field_dict["id"] = id
        if is_template is not UNSET:
            field_dict["isTemplate"] = is_template
        if name is not UNSET:
            field_dict["name"] = name
        if previous_time_spent is not UNSET:
            field_dict["previousTimeSpent"] = previous_time_spent
        if prioritization_field is not UNSET:
            field_dict["prioritizationField"] = prioritization_field
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if started_on is not UNSET:
            field_dict["startedOn"] = started_on
        if status is not UNSET:
            field_dict["status"] = status
        if use_report_from_template is not UNSET:
            field_dict["useReportFromTemplate"] = use_report_from_template

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plans_list_post_request_data_item_attributes_description import (
            PlansListPostRequestDataItemAttributesDescription,
        )
        from ..models.plans_list_post_request_data_item_attributes_home_page_content import (
            PlansListPostRequestDataItemAttributesHomePageContent,
        )

        d = dict(src_dict)
        allowed_types = cast(list[str], d.pop("allowedTypes", UNSET))

        _calculation_type = d.pop("calculationType", UNSET)
        calculation_type: (
            PlansListPostRequestDataItemAttributesCalculationType | Unset
        )
        if isinstance(_calculation_type, Unset):
            calculation_type = UNSET
        else:
            calculation_type = (
                PlansListPostRequestDataItemAttributesCalculationType(
                    _calculation_type
                )
            )

        capacity = d.pop("capacity", UNSET)

        color = d.pop("color", UNSET)

        default_estimate = d.pop("defaultEstimate", UNSET)

        _description = d.pop("description", UNSET)
        description: PlansListPostRequestDataItemAttributesDescription | Unset
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = (
                PlansListPostRequestDataItemAttributesDescription.from_dict(
                    _description
                )
            )

        _due_date = d.pop("dueDate", UNSET)
        due_date: datetime.date | Unset
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = datetime.date.fromisoformat(_due_date)

        estimation_field = d.pop("estimationField", UNSET)

        _finished_on = d.pop("finishedOn", UNSET)
        finished_on: datetime.datetime | Unset
        if isinstance(_finished_on, Unset):
            finished_on = UNSET
        else:
            finished_on = datetime.datetime.fromisoformat(_finished_on)

        _home_page_content = d.pop("homePageContent", UNSET)
        home_page_content: (
            PlansListPostRequestDataItemAttributesHomePageContent | Unset
        )
        if isinstance(_home_page_content, Unset):
            home_page_content = UNSET
        else:
            home_page_content = PlansListPostRequestDataItemAttributesHomePageContent.from_dict(
                _home_page_content
            )

        id = d.pop("id", UNSET)

        is_template = d.pop("isTemplate", UNSET)

        name = d.pop("name", UNSET)

        previous_time_spent = d.pop("previousTimeSpent", UNSET)

        prioritization_field = d.pop("prioritizationField", UNSET)

        sort_order = d.pop("sortOrder", UNSET)

        _start_date = d.pop("startDate", UNSET)
        start_date: datetime.date | Unset
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = datetime.date.fromisoformat(_start_date)

        _started_on = d.pop("startedOn", UNSET)
        started_on: datetime.datetime | Unset
        if isinstance(_started_on, Unset):
            started_on = UNSET
        else:
            started_on = datetime.datetime.fromisoformat(_started_on)

        status = d.pop("status", UNSET)

        use_report_from_template = d.pop("useReportFromTemplate", UNSET)

        plans_list_post_request_data_item_attributes_obj = cls(
            allowed_types=allowed_types,
            calculation_type=calculation_type,
            capacity=capacity,
            color=color,
            default_estimate=default_estimate,
            description=description,
            due_date=due_date,
            estimation_field=estimation_field,
            finished_on=finished_on,
            home_page_content=home_page_content,
            id=id,
            is_template=is_template,
            name=name,
            previous_time_spent=previous_time_spent,
            prioritization_field=prioritization_field,
            sort_order=sort_order,
            start_date=start_date,
            started_on=started_on,
            status=status,
            use_report_from_template=use_report_from_template,
        )

        plans_list_post_request_data_item_attributes_obj.additional_properties = d
        return plans_list_post_request_data_item_attributes_obj

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

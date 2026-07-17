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
    from ..models.jobs_list_get_response_data_item_attributes_status import (
        JobsListGetResponseDataItemAttributesStatus,
    )


T = TypeVar("T", bound="JobsListGetResponseDataItemAttributes")


@_attrs_define
class JobsListGetResponseDataItemAttributes:
    """
    Attributes:
        job_id (str | Unset):  Example: example.
        name (str | Unset):  Example: example.
        state (str | Unset):  Example: example.
        status (JobsListGetResponseDataItemAttributesStatus | Unset):
    """

    job_id: str | Unset = UNSET
    name: str | Unset = UNSET
    state: str | Unset = UNSET
    status: JobsListGetResponseDataItemAttributesStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        job_id = self.job_id

        name = self.name

        state = self.state

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_id is not UNSET:
            field_dict["jobId"] = job_id
        if name is not UNSET:
            field_dict["name"] = name
        if state is not UNSET:
            field_dict["state"] = state
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jobs_list_get_response_data_item_attributes_status import (
            JobsListGetResponseDataItemAttributesStatus,
        )

        d = dict(src_dict)
        job_id = d.pop("jobId", UNSET)

        name = d.pop("name", UNSET)

        state = d.pop("state", UNSET)

        _status = d.pop("status", UNSET)
        status: JobsListGetResponseDataItemAttributesStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = JobsListGetResponseDataItemAttributesStatus.from_dict(
                _status
            )

        jobs_list_get_response_data_item_attributes_obj = cls(
            job_id=job_id,
            name=name,
            state=state,
            status=status,
        )

        jobs_list_get_response_data_item_attributes_obj.additional_properties = d
        return jobs_list_get_response_data_item_attributes_obj

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

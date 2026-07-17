# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecuteJobRequestBodyParamsType0")


@_attrs_define
class ExecuteJobRequestBodyParamsType0:
    """Parameters of Job to be executed.

    Attributes:
        param1 (str | Unset):  Example: value1.
        param2 (str | Unset):  Example: value2.
    """

    param1: str | Unset = UNSET
    param2: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        param1 = self.param1

        param2 = self.param2

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if param1 is not UNSET:
            field_dict["param1"] = param1
        if param2 is not UNSET:
            field_dict["param2"] = param2

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        param1 = d.pop("param1", UNSET)

        param2 = d.pop("param2", UNSET)

        execute_job_request_body_params_type_0_obj = cls(
            param1=param1,
            param2=param2,
        )

        execute_job_request_body_params_type_0_obj.additional_properties = d
        return execute_job_request_body_params_type_0_obj

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

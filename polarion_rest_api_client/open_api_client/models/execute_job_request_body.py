# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execute_job_request_body_params_type_0 import (
        ExecuteJobRequestBodyParamsType0,
    )


T = TypeVar("T", bound="ExecuteJobRequestBody")


@_attrs_define
class ExecuteJobRequestBody:
    """
    Attributes:
        job_id (str | Unset): Id of job factory, e.g. jobs.cleanup Example: MyJobId.
        name (str | Unset):  Example: My Job.
        node_id (None | str | Unset):  Example: MyNodeId.
        params (ExecuteJobRequestBodyParamsType0 | None | Unset): Parameters of Job to be executed.
        scope (None | str | Unset): Scope of the job. Accepted formats: 'system', 'project:{projectId}', or
            'path:/{path}'. Example: system.
    """

    job_id: str | Unset = UNSET
    name: str | Unset = UNSET
    node_id: None | str | Unset = UNSET
    params: ExecuteJobRequestBodyParamsType0 | None | Unset = UNSET
    scope: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        from ..models.execute_job_request_body_params_type_0 import (
            ExecuteJobRequestBodyParamsType0,
        )

        job_id = self.job_id

        name = self.name

        node_id: None | str | Unset
        if isinstance(self.node_id, Unset):
            node_id = UNSET
        else:
            node_id = self.node_id

        params: dict[str, Any] | None | Unset
        if isinstance(self.params, Unset):
            params = UNSET
        elif isinstance(self.params, ExecuteJobRequestBodyParamsType0):
            params = self.params.to_dict()
        else:
            params = self.params

        scope: None | str | Unset
        if isinstance(self.scope, Unset):
            scope = UNSET
        else:
            scope = self.scope

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_id is not UNSET:
            field_dict["jobId"] = job_id
        if name is not UNSET:
            field_dict["name"] = name
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if params is not UNSET:
            field_dict["params"] = params
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execute_job_request_body_params_type_0 import (
            ExecuteJobRequestBodyParamsType0,
        )

        d = dict(src_dict)
        job_id = d.pop("jobId", UNSET)

        name = d.pop("name", UNSET)

        def _parse_node_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        node_id = _parse_node_id(d.pop("nodeId", UNSET))

        def _parse_params(
            data: object,
        ) -> ExecuteJobRequestBodyParamsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                params_type_0 = ExecuteJobRequestBodyParamsType0.from_dict(
                    data
                )

                return params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExecuteJobRequestBodyParamsType0 | None | Unset, data)

        params = _parse_params(d.pop("params", UNSET))

        def _parse_scope(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scope = _parse_scope(d.pop("scope", UNSET))

        execute_job_request_body_obj = cls(
            job_id=job_id,
            name=name,
            node_id=node_id,
            params=params,
            scope=scope,
        )

        execute_job_request_body_obj.additional_properties = d
        return execute_job_request_body_obj

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

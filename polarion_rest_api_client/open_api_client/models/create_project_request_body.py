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
    from ..models.create_project_request_body_params_type_0 import (
        CreateProjectRequestBodyParamsType0,
    )


T = TypeVar("T", bound="CreateProjectRequestBody")


@_attrs_define
class CreateProjectRequestBody:
    """
    Attributes:
        location (str | Unset): Location of the new Project to be created. Example: MyLocation.
        params (CreateProjectRequestBodyParamsType0 | None | Unset): Parameters of new Project to be created.
        project_id (str | Unset): Id of the new Project to be created. Example: MyProjectId.
        template_id (None | str | Unset): Id of the template to create the new Project from. Example:
            MyProjectTemplateId.
        tracker_prefix (str | Unset): Tracker prefix of the new Project to be created. Example: MyTrackerPrefix.
    """

    location: str | Unset = UNSET
    params: CreateProjectRequestBodyParamsType0 | None | Unset = UNSET
    project_id: str | Unset = UNSET
    template_id: None | str | Unset = UNSET
    tracker_prefix: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_project_request_body_params_type_0 import (
            CreateProjectRequestBodyParamsType0,
        )

        location = self.location

        params: dict[str, Any] | None | Unset
        if isinstance(self.params, Unset):
            params = UNSET
        elif isinstance(self.params, CreateProjectRequestBodyParamsType0):
            params = self.params.to_dict()
        else:
            params = self.params

        project_id = self.project_id

        template_id: None | str | Unset
        if isinstance(self.template_id, Unset):
            template_id = UNSET
        else:
            template_id = self.template_id

        tracker_prefix = self.tracker_prefix

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if location is not UNSET:
            field_dict["location"] = location
        if params is not UNSET:
            field_dict["params"] = params
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if template_id is not UNSET:
            field_dict["templateId"] = template_id
        if tracker_prefix is not UNSET:
            field_dict["trackerPrefix"] = tracker_prefix

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_project_request_body_params_type_0 import (
            CreateProjectRequestBodyParamsType0,
        )

        d = dict(src_dict)
        location = d.pop("location", UNSET)

        def _parse_params(
            data: object,
        ) -> CreateProjectRequestBodyParamsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                params_type_0 = CreateProjectRequestBodyParamsType0.from_dict(
                    data
                )

                return params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CreateProjectRequestBodyParamsType0 | None | Unset, data
            )

        params = _parse_params(d.pop("params", UNSET))

        project_id = d.pop("projectId", UNSET)

        def _parse_template_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        template_id = _parse_template_id(d.pop("templateId", UNSET))

        tracker_prefix = d.pop("trackerPrefix", UNSET)

        create_project_request_body_obj = cls(
            location=location,
            params=params,
            project_id=project_id,
            template_id=template_id,
            tracker_prefix=tracker_prefix,
        )

        create_project_request_body_obj.additional_properties = d
        return create_project_request_body_obj

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

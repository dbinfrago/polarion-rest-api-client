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
    from ..models.projecttemplates_list_get_response_data_item_attributes_parameters import (
        ProjecttemplatesListGetResponseDataItemAttributesParameters,
    )


T = TypeVar("T", bound="ProjecttemplatesListGetResponseDataItemAttributes")


@_attrs_define
class ProjecttemplatesListGetResponseDataItemAttributes:
    """
    Attributes:
        custom_icon (str | Unset):
        description (str | Unset):
        distributions (list[str] | Unset):
        id (str | Unset):  Example: MyProjectId.
        is_default (bool | Unset):
        name (str | Unset):
        parameters (ProjecttemplatesListGetResponseDataItemAttributesParameters | Unset):
    """

    custom_icon: str | Unset = UNSET
    description: str | Unset = UNSET
    distributions: list[str] | Unset = UNSET
    id: str | Unset = UNSET
    is_default: bool | Unset = UNSET
    name: str | Unset = UNSET
    parameters: (
        ProjecttemplatesListGetResponseDataItemAttributesParameters | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        custom_icon = self.custom_icon

        description = self.description

        distributions: list[str] | Unset = UNSET
        if not isinstance(self.distributions, Unset):
            distributions = self.distributions

        id = self.id

        is_default = self.is_default

        name = self.name

        parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if custom_icon is not UNSET:
            field_dict["customIcon"] = custom_icon
        if description is not UNSET:
            field_dict["description"] = description
        if distributions is not UNSET:
            field_dict["distributions"] = distributions
        if id is not UNSET:
            field_dict["id"] = id
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default
        if name is not UNSET:
            field_dict["name"] = name
        if parameters is not UNSET:
            field_dict["parameters"] = parameters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.projecttemplates_list_get_response_data_item_attributes_parameters import (
            ProjecttemplatesListGetResponseDataItemAttributesParameters,
        )

        d = dict(src_dict)
        custom_icon = d.pop("customIcon", UNSET)

        description = d.pop("description", UNSET)

        distributions = cast(list[str], d.pop("distributions", UNSET))

        id = d.pop("id", UNSET)

        is_default = d.pop("isDefault", UNSET)

        name = d.pop("name", UNSET)

        _parameters = d.pop("parameters", UNSET)
        parameters: (
            ProjecttemplatesListGetResponseDataItemAttributesParameters | Unset
        )
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = ProjecttemplatesListGetResponseDataItemAttributesParameters.from_dict(
                _parameters
            )

        projecttemplates_list_get_response_data_item_attributes_obj = cls(
            custom_icon=custom_icon,
            description=description,
            distributions=distributions,
            id=id,
            is_default=is_default,
            name=name,
            parameters=parameters,
        )

        projecttemplates_list_get_response_data_item_attributes_obj.additional_properties = d
        return projecttemplates_list_get_response_data_item_attributes_obj

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

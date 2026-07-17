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
    from ..models.customfields_single_patch_request_data_attributes_fields_item_parameters_item import (
        CustomfieldsSinglePatchRequestDataAttributesFieldsItemParametersItem,
    )
    from ..models.customfields_single_patch_request_data_attributes_fields_item_type import (
        CustomfieldsSinglePatchRequestDataAttributesFieldsItemType,
    )


T = TypeVar(
    "T", bound="CustomfieldsSinglePatchRequestDataAttributesFieldsItem"
)


@_attrs_define
class CustomfieldsSinglePatchRequestDataAttributesFieldsItem:
    """
    Attributes:
        default_value (str | Unset):
        depends_on (str | Unset):
        description (str | Unset):
        id (str | Unset):
        name (str | Unset):
        parameters (list[CustomfieldsSinglePatchRequestDataAttributesFieldsItemParametersItem] | Unset):
        required (bool | Unset):
        type_ (CustomfieldsSinglePatchRequestDataAttributesFieldsItemType | Unset):
    """

    default_value: str | Unset = UNSET
    depends_on: str | Unset = UNSET
    description: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    parameters: (
        list[
            CustomfieldsSinglePatchRequestDataAttributesFieldsItemParametersItem
        ]
        | Unset
    ) = UNSET
    required: bool | Unset = UNSET
    type_: (
        CustomfieldsSinglePatchRequestDataAttributesFieldsItemType | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        default_value = self.default_value

        depends_on = self.depends_on

        description = self.description

        id = self.id

        name = self.name

        parameters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = []
            for parameters_item_data in self.parameters:
                parameters_item = parameters_item_data.to_dict()
                parameters.append(parameters_item)

        required = self.required

        type_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if depends_on is not UNSET:
            field_dict["dependsOn"] = depends_on
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if required is not UNSET:
            field_dict["required"] = required
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.customfields_single_patch_request_data_attributes_fields_item_parameters_item import (
            CustomfieldsSinglePatchRequestDataAttributesFieldsItemParametersItem,
        )
        from ..models.customfields_single_patch_request_data_attributes_fields_item_type import (
            CustomfieldsSinglePatchRequestDataAttributesFieldsItemType,
        )

        d = dict(src_dict)
        default_value = d.pop("defaultValue", UNSET)

        depends_on = d.pop("dependsOn", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _parameters = d.pop("parameters", UNSET)
        parameters: (
            list[
                CustomfieldsSinglePatchRequestDataAttributesFieldsItemParametersItem
            ]
            | Unset
        ) = UNSET
        if _parameters is not UNSET:
            parameters = []
            for parameters_item_data in _parameters:
                parameters_item = CustomfieldsSinglePatchRequestDataAttributesFieldsItemParametersItem.from_dict(
                    parameters_item_data
                )

                parameters.append(parameters_item)

        required = d.pop("required", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: (
            CustomfieldsSinglePatchRequestDataAttributesFieldsItemType | Unset
        )
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CustomfieldsSinglePatchRequestDataAttributesFieldsItemType.from_dict(
                _type_
            )

        customfields_single_patch_request_data_attributes_fields_item_obj = (
            cls(
                default_value=default_value,
                depends_on=depends_on,
                description=description,
                id=id,
                name=name,
                parameters=parameters,
                required=required,
                type_=type_,
            )
        )

        customfields_single_patch_request_data_attributes_fields_item_obj.additional_properties = d
        return (
            customfields_single_patch_request_data_attributes_fields_item_obj
        )

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

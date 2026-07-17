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
    from ..models.testparameters_list_get_response_data_item_relationships_definition import (
        TestparametersListGetResponseDataItemRelationshipsDefinition,
    )


T = TypeVar("T", bound="TestparametersListGetResponseDataItemRelationships")


@_attrs_define
class TestparametersListGetResponseDataItemRelationships:
    """
    Attributes:
        definition (TestparametersListGetResponseDataItemRelationshipsDefinition | Unset):
    """

    definition: (
        TestparametersListGetResponseDataItemRelationshipsDefinition | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        definition: dict[str, Any] | Unset = UNSET
        if not isinstance(self.definition, Unset):
            definition = self.definition.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if definition is not UNSET:
            field_dict["definition"] = definition

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.testparameters_list_get_response_data_item_relationships_definition import (
            TestparametersListGetResponseDataItemRelationshipsDefinition,
        )

        d = dict(src_dict)
        _definition = d.pop("definition", UNSET)
        definition: (
            TestparametersListGetResponseDataItemRelationshipsDefinition
            | Unset
        )
        if isinstance(_definition, Unset):
            definition = UNSET
        else:
            definition = TestparametersListGetResponseDataItemRelationshipsDefinition.from_dict(
                _definition
            )

        testparameters_list_get_response_data_item_relationships_obj = cls(
            definition=definition,
        )

        testparameters_list_get_response_data_item_relationships_obj.additional_properties = d
        return testparameters_list_get_response_data_item_relationships_obj

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

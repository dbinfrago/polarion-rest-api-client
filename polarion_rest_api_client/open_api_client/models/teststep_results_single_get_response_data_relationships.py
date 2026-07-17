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
    from ..models.teststep_results_single_get_response_data_relationships_test_step import (
        TeststepResultsSingleGetResponseDataRelationshipsTestStep,
    )


T = TypeVar("T", bound="TeststepResultsSingleGetResponseDataRelationships")


@_attrs_define
class TeststepResultsSingleGetResponseDataRelationships:
    """
    Attributes:
        test_step (TeststepResultsSingleGetResponseDataRelationshipsTestStep | Unset):
    """

    test_step: (
        TeststepResultsSingleGetResponseDataRelationshipsTestStep | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        test_step: dict[str, Any] | Unset = UNSET
        if not isinstance(self.test_step, Unset):
            test_step = self.test_step.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if test_step is not UNSET:
            field_dict["testStep"] = test_step

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.teststep_results_single_get_response_data_relationships_test_step import (
            TeststepResultsSingleGetResponseDataRelationshipsTestStep,
        )

        d = dict(src_dict)
        _test_step = d.pop("testStep", UNSET)
        test_step: (
            TeststepResultsSingleGetResponseDataRelationshipsTestStep | Unset
        )
        if isinstance(_test_step, Unset):
            test_step = UNSET
        else:
            test_step = TeststepResultsSingleGetResponseDataRelationshipsTestStep.from_dict(
                _test_step
            )

        teststep_results_single_get_response_data_relationships_obj = cls(
            test_step=test_step,
        )

        teststep_results_single_get_response_data_relationships_obj.additional_properties = d
        return teststep_results_single_get_response_data_relationships_obj

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

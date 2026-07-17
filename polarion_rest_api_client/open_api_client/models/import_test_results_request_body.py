# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImportTestResultsRequestBody")


@_attrs_define
class ImportTestResultsRequestBody:
    """
    Attributes:
        defect_template_id (str | Unset):  Example: MyProjectId/MyDefectId.
        retest (bool | Unset):
    """

    defect_template_id: str | Unset = UNSET
    retest: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        defect_template_id = self.defect_template_id

        retest = self.retest

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if defect_template_id is not UNSET:
            field_dict["defectTemplateId"] = defect_template_id
        if retest is not UNSET:
            field_dict["retest"] = retest

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        defect_template_id = d.pop("defectTemplateId", UNSET)

        retest = d.pop("retest", UNSET)

        import_test_results_request_body_obj = cls(
            defect_template_id=defect_template_id,
            retest=retest,
        )

        import_test_results_request_body_obj.additional_properties = d
        return import_test_results_request_body_obj

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

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
    from ..models.testrecords_single_patch_request_data_relationships_defect import (
        TestrecordsSinglePatchRequestDataRelationshipsDefect,
    )
    from ..models.testrecords_single_patch_request_data_relationships_executed_by import (
        TestrecordsSinglePatchRequestDataRelationshipsExecutedBy,
    )


T = TypeVar("T", bound="TestrecordsSinglePatchRequestDataRelationships")


@_attrs_define
class TestrecordsSinglePatchRequestDataRelationships:
    """
    Attributes:
        defect (TestrecordsSinglePatchRequestDataRelationshipsDefect | Unset):
        executed_by (TestrecordsSinglePatchRequestDataRelationshipsExecutedBy | Unset):
    """

    defect: TestrecordsSinglePatchRequestDataRelationshipsDefect | Unset = (
        UNSET
    )
    executed_by: (
        TestrecordsSinglePatchRequestDataRelationshipsExecutedBy | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        defect: dict[str, Any] | Unset = UNSET
        if not isinstance(self.defect, Unset):
            defect = self.defect.to_dict()

        executed_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.executed_by, Unset):
            executed_by = self.executed_by.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if defect is not UNSET:
            field_dict["defect"] = defect
        if executed_by is not UNSET:
            field_dict["executedBy"] = executed_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.testrecords_single_patch_request_data_relationships_defect import (
            TestrecordsSinglePatchRequestDataRelationshipsDefect,
        )
        from ..models.testrecords_single_patch_request_data_relationships_executed_by import (
            TestrecordsSinglePatchRequestDataRelationshipsExecutedBy,
        )

        d = dict(src_dict)
        _defect = d.pop("defect", UNSET)
        defect: TestrecordsSinglePatchRequestDataRelationshipsDefect | Unset
        if isinstance(_defect, Unset):
            defect = UNSET
        else:
            defect = (
                TestrecordsSinglePatchRequestDataRelationshipsDefect.from_dict(
                    _defect
                )
            )

        _executed_by = d.pop("executedBy", UNSET)
        executed_by: (
            TestrecordsSinglePatchRequestDataRelationshipsExecutedBy | Unset
        )
        if isinstance(_executed_by, Unset):
            executed_by = UNSET
        else:
            executed_by = TestrecordsSinglePatchRequestDataRelationshipsExecutedBy.from_dict(
                _executed_by
            )

        testrecords_single_patch_request_data_relationships_obj = cls(
            defect=defect,
            executed_by=executed_by,
        )

        testrecords_single_patch_request_data_relationships_obj.additional_properties = d
        return testrecords_single_patch_request_data_relationships_obj

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

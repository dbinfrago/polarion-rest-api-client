# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import datetime
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
    from ..models.testrecords_single_patch_request_data_attributes_comment import (
        TestrecordsSinglePatchRequestDataAttributesComment,
    )


T = TypeVar("T", bound="TestrecordsSinglePatchRequestDataAttributes")


@_attrs_define
class TestrecordsSinglePatchRequestDataAttributes:
    """
    Attributes:
        comment (TestrecordsSinglePatchRequestDataAttributesComment | Unset):
        duration (float | Unset):
        executed (datetime.datetime | Unset):  Example: 1970-01-01T00:00:00Z.
        result (str | Unset):  Example: passed.
        test_case_revision (str | Unset):  Example: Test Case Revision.
    """

    comment: TestrecordsSinglePatchRequestDataAttributesComment | Unset = UNSET
    duration: float | Unset = UNSET
    executed: datetime.datetime | Unset = UNSET
    result: str | Unset = UNSET
    test_case_revision: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        comment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.comment, Unset):
            comment = self.comment.to_dict()

        duration = self.duration

        executed: str | Unset = UNSET
        if not isinstance(self.executed, Unset):
            executed = self.executed.isoformat()

        result = self.result

        test_case_revision = self.test_case_revision

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comment is not UNSET:
            field_dict["comment"] = comment
        if duration is not UNSET:
            field_dict["duration"] = duration
        if executed is not UNSET:
            field_dict["executed"] = executed
        if result is not UNSET:
            field_dict["result"] = result
        if test_case_revision is not UNSET:
            field_dict["testCaseRevision"] = test_case_revision

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.testrecords_single_patch_request_data_attributes_comment import (
            TestrecordsSinglePatchRequestDataAttributesComment,
        )

        d = dict(src_dict)
        _comment = d.pop("comment", UNSET)
        comment: TestrecordsSinglePatchRequestDataAttributesComment | Unset
        if isinstance(_comment, Unset):
            comment = UNSET
        else:
            comment = (
                TestrecordsSinglePatchRequestDataAttributesComment.from_dict(
                    _comment
                )
            )

        duration = d.pop("duration", UNSET)

        _executed = d.pop("executed", UNSET)
        executed: datetime.datetime | Unset
        if isinstance(_executed, Unset):
            executed = UNSET
        else:
            executed = datetime.datetime.fromisoformat(_executed)

        result = d.pop("result", UNSET)

        test_case_revision = d.pop("testCaseRevision", UNSET)

        testrecords_single_patch_request_data_attributes_obj = cls(
            comment=comment,
            duration=duration,
            executed=executed,
            result=result,
            test_case_revision=test_case_revision,
        )

        testrecords_single_patch_request_data_attributes_obj.additional_properties = d
        return testrecords_single_patch_request_data_attributes_obj

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

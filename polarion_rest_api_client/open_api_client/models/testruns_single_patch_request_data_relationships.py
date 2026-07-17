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
    from ..models.testruns_single_patch_request_data_relationships_document import (
        TestrunsSinglePatchRequestDataRelationshipsDocument,
    )
    from ..models.testruns_single_patch_request_data_relationships_project_span import (
        TestrunsSinglePatchRequestDataRelationshipsProjectSpan,
    )
    from ..models.testruns_single_patch_request_data_relationships_summary_defect import (
        TestrunsSinglePatchRequestDataRelationshipsSummaryDefect,
    )


T = TypeVar("T", bound="TestrunsSinglePatchRequestDataRelationships")


@_attrs_define
class TestrunsSinglePatchRequestDataRelationships:
    """
    Attributes:
        document (TestrunsSinglePatchRequestDataRelationshipsDocument | Unset):
        project_span (TestrunsSinglePatchRequestDataRelationshipsProjectSpan | Unset):
        summary_defect (TestrunsSinglePatchRequestDataRelationshipsSummaryDefect | Unset):
    """

    document: TestrunsSinglePatchRequestDataRelationshipsDocument | Unset = (
        UNSET
    )
    project_span: (
        TestrunsSinglePatchRequestDataRelationshipsProjectSpan | Unset
    ) = UNSET
    summary_defect: (
        TestrunsSinglePatchRequestDataRelationshipsSummaryDefect | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        document: dict[str, Any] | Unset = UNSET
        if not isinstance(self.document, Unset):
            document = self.document.to_dict()

        project_span: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_span, Unset):
            project_span = self.project_span.to_dict()

        summary_defect: dict[str, Any] | Unset = UNSET
        if not isinstance(self.summary_defect, Unset):
            summary_defect = self.summary_defect.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if document is not UNSET:
            field_dict["document"] = document
        if project_span is not UNSET:
            field_dict["projectSpan"] = project_span
        if summary_defect is not UNSET:
            field_dict["summaryDefect"] = summary_defect

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.testruns_single_patch_request_data_relationships_document import (
            TestrunsSinglePatchRequestDataRelationshipsDocument,
        )
        from ..models.testruns_single_patch_request_data_relationships_project_span import (
            TestrunsSinglePatchRequestDataRelationshipsProjectSpan,
        )
        from ..models.testruns_single_patch_request_data_relationships_summary_defect import (
            TestrunsSinglePatchRequestDataRelationshipsSummaryDefect,
        )

        d = dict(src_dict)
        _document = d.pop("document", UNSET)
        document: TestrunsSinglePatchRequestDataRelationshipsDocument | Unset
        if isinstance(_document, Unset):
            document = UNSET
        else:
            document = (
                TestrunsSinglePatchRequestDataRelationshipsDocument.from_dict(
                    _document
                )
            )

        _project_span = d.pop("projectSpan", UNSET)
        project_span: (
            TestrunsSinglePatchRequestDataRelationshipsProjectSpan | Unset
        )
        if isinstance(_project_span, Unset):
            project_span = UNSET
        else:
            project_span = TestrunsSinglePatchRequestDataRelationshipsProjectSpan.from_dict(
                _project_span
            )

        _summary_defect = d.pop("summaryDefect", UNSET)
        summary_defect: (
            TestrunsSinglePatchRequestDataRelationshipsSummaryDefect | Unset
        )
        if isinstance(_summary_defect, Unset):
            summary_defect = UNSET
        else:
            summary_defect = TestrunsSinglePatchRequestDataRelationshipsSummaryDefect.from_dict(
                _summary_defect
            )

        testruns_single_patch_request_data_relationships_obj = cls(
            document=document,
            project_span=project_span,
            summary_defect=summary_defect,
        )

        testruns_single_patch_request_data_relationships_obj.additional_properties = d
        return testruns_single_patch_request_data_relationships_obj

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

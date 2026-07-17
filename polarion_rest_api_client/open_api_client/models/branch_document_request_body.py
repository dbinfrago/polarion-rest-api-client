# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BranchDocumentRequestBody")


@_attrs_define
class BranchDocumentRequestBody:
    """
    Attributes:
        copy_workflow_status_and_signatures (bool | Unset): Specifies that workflow status and signatures should be
            copied to the branched document.
        query (str | Unset): Specifies optional filtering query. Example: status:open.
        target_document_name (str | Unset): Name for new Document. Example: MyDocumentId.
        target_project_id (str | Unset): Project where new document will be created. Example: MyProjectId.
        target_space_id (str | Unset): Space where new document will be created. Example: MySpaceId.
    """

    copy_workflow_status_and_signatures: bool | Unset = UNSET
    query: str | Unset = UNSET
    target_document_name: str | Unset = UNSET
    target_project_id: str | Unset = UNSET
    target_space_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        copy_workflow_status_and_signatures = (
            self.copy_workflow_status_and_signatures
        )

        query = self.query

        target_document_name = self.target_document_name

        target_project_id = self.target_project_id

        target_space_id = self.target_space_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if copy_workflow_status_and_signatures is not UNSET:
            field_dict["copyWorkflowStatusAndSignatures"] = (
                copy_workflow_status_and_signatures
            )
        if query is not UNSET:
            field_dict["query"] = query
        if target_document_name is not UNSET:
            field_dict["targetDocumentName"] = target_document_name
        if target_project_id is not UNSET:
            field_dict["targetProjectId"] = target_project_id
        if target_space_id is not UNSET:
            field_dict["targetSpaceId"] = target_space_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        copy_workflow_status_and_signatures = d.pop(
            "copyWorkflowStatusAndSignatures", UNSET
        )

        query = d.pop("query", UNSET)

        target_document_name = d.pop("targetDocumentName", UNSET)

        target_project_id = d.pop("targetProjectId", UNSET)

        target_space_id = d.pop("targetSpaceId", UNSET)

        branch_document_request_body_obj = cls(
            copy_workflow_status_and_signatures=copy_workflow_status_and_signatures,
            query=query,
            target_document_name=target_document_name,
            target_project_id=target_project_id,
            target_space_id=target_space_id,
        )

        branch_document_request_body_obj.additional_properties = d
        return branch_document_request_body_obj

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

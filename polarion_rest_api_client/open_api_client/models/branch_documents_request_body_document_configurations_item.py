# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BranchDocumentsRequestBodyDocumentConfigurationsItem")


@_attrs_define
class BranchDocumentsRequestBodyDocumentConfigurationsItem:
    """
    Attributes:
        source_document (str): Reference path of the source Document. Example: MyProjectId/MySpaceId/MyDocumentId.
        copy_workflow_status_and_signatures (bool | Unset): Specifies that workflow status and signatures should be
            copied to the branched document.
        initialized_fields (list[str] | Unset): Specifies fields of overwritten Work Items that should be initialized
            (instead of being copied from source Work Items).
        overwrite_work_items (bool | Unset): Specifies that Work Items in the branched Document should be overwritten
            (instead of being referenced).
        query (str | Unset): Specifies optional filtering query. Example: status:open.
        source_revision (str | Unset): Revision of the source Document. Example: 1234.
        target_document_name (str | Unset): Name for new Document. Example: MyDocumentId.
        target_document_title (str | Unset): Title for new Document. Example: My Document Title.
        target_project_id (str | Unset): Project where new document will be created. Example: MyProjectId.
        target_space_id (str | Unset): Space where new document will be created. Example: MySpaceId.
        update_title_heading (bool | Unset): Specifies that title heading of the target Document should be set to the
            new Document's title.
    """

    source_document: str
    copy_workflow_status_and_signatures: bool | Unset = UNSET
    initialized_fields: list[str] | Unset = UNSET
    overwrite_work_items: bool | Unset = UNSET
    query: str | Unset = UNSET
    source_revision: str | Unset = UNSET
    target_document_name: str | Unset = UNSET
    target_document_title: str | Unset = UNSET
    target_project_id: str | Unset = UNSET
    target_space_id: str | Unset = UNSET
    update_title_heading: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        source_document = self.source_document

        copy_workflow_status_and_signatures = (
            self.copy_workflow_status_and_signatures
        )

        initialized_fields: list[str] | Unset = UNSET
        if not isinstance(self.initialized_fields, Unset):
            initialized_fields = self.initialized_fields

        overwrite_work_items = self.overwrite_work_items

        query = self.query

        source_revision = self.source_revision

        target_document_name = self.target_document_name

        target_document_title = self.target_document_title

        target_project_id = self.target_project_id

        target_space_id = self.target_space_id

        update_title_heading = self.update_title_heading

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sourceDocument": source_document,
            }
        )
        if copy_workflow_status_and_signatures is not UNSET:
            field_dict["copyWorkflowStatusAndSignatures"] = (
                copy_workflow_status_and_signatures
            )
        if initialized_fields is not UNSET:
            field_dict["initializedFields"] = initialized_fields
        if overwrite_work_items is not UNSET:
            field_dict["overwriteWorkItems"] = overwrite_work_items
        if query is not UNSET:
            field_dict["query"] = query
        if source_revision is not UNSET:
            field_dict["sourceRevision"] = source_revision
        if target_document_name is not UNSET:
            field_dict["targetDocumentName"] = target_document_name
        if target_document_title is not UNSET:
            field_dict["targetDocumentTitle"] = target_document_title
        if target_project_id is not UNSET:
            field_dict["targetProjectId"] = target_project_id
        if target_space_id is not UNSET:
            field_dict["targetSpaceId"] = target_space_id
        if update_title_heading is not UNSET:
            field_dict["updateTitleHeading"] = update_title_heading

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source_document = d.pop("sourceDocument")

        copy_workflow_status_and_signatures = d.pop(
            "copyWorkflowStatusAndSignatures", UNSET
        )

        initialized_fields = cast(list[str], d.pop("initializedFields", UNSET))

        overwrite_work_items = d.pop("overwriteWorkItems", UNSET)

        query = d.pop("query", UNSET)

        source_revision = d.pop("sourceRevision", UNSET)

        target_document_name = d.pop("targetDocumentName", UNSET)

        target_document_title = d.pop("targetDocumentTitle", UNSET)

        target_project_id = d.pop("targetProjectId", UNSET)

        target_space_id = d.pop("targetSpaceId", UNSET)

        update_title_heading = d.pop("updateTitleHeading", UNSET)

        branch_documents_request_body_document_configurations_item_obj = cls(
            source_document=source_document,
            copy_workflow_status_and_signatures=copy_workflow_status_and_signatures,
            initialized_fields=initialized_fields,
            overwrite_work_items=overwrite_work_items,
            query=query,
            source_revision=source_revision,
            target_document_name=target_document_name,
            target_document_title=target_document_title,
            target_project_id=target_project_id,
            target_space_id=target_space_id,
            update_title_heading=update_title_heading,
        )

        branch_documents_request_body_document_configurations_item_obj.additional_properties = d
        return branch_documents_request_body_document_configurations_item_obj

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

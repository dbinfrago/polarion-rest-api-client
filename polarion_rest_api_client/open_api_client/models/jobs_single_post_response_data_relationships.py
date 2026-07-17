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
    from ..models.jobs_single_post_response_data_relationships_document import (
        JobsSinglePostResponseDataRelationshipsDocument,
    )
    from ..models.jobs_single_post_response_data_relationships_documents import (
        JobsSinglePostResponseDataRelationshipsDocuments,
    )
    from ..models.jobs_single_post_response_data_relationships_project import (
        JobsSinglePostResponseDataRelationshipsProject,
    )


T = TypeVar("T", bound="JobsSinglePostResponseDataRelationships")


@_attrs_define
class JobsSinglePostResponseDataRelationships:
    """
    Attributes:
        document (JobsSinglePostResponseDataRelationshipsDocument | Unset):
        documents (JobsSinglePostResponseDataRelationshipsDocuments | Unset):
        project (JobsSinglePostResponseDataRelationshipsProject | Unset):
    """

    document: JobsSinglePostResponseDataRelationshipsDocument | Unset = UNSET
    documents: JobsSinglePostResponseDataRelationshipsDocuments | Unset = UNSET
    project: JobsSinglePostResponseDataRelationshipsProject | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        document: dict[str, Any] | Unset = UNSET
        if not isinstance(self.document, Unset):
            document = self.document.to_dict()

        documents: dict[str, Any] | Unset = UNSET
        if not isinstance(self.documents, Unset):
            documents = self.documents.to_dict()

        project: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if document is not UNSET:
            field_dict["document"] = document
        if documents is not UNSET:
            field_dict["documents"] = documents
        if project is not UNSET:
            field_dict["project"] = project

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jobs_single_post_response_data_relationships_document import (
            JobsSinglePostResponseDataRelationshipsDocument,
        )
        from ..models.jobs_single_post_response_data_relationships_documents import (
            JobsSinglePostResponseDataRelationshipsDocuments,
        )
        from ..models.jobs_single_post_response_data_relationships_project import (
            JobsSinglePostResponseDataRelationshipsProject,
        )

        d = dict(src_dict)
        _document = d.pop("document", UNSET)
        document: JobsSinglePostResponseDataRelationshipsDocument | Unset
        if isinstance(_document, Unset):
            document = UNSET
        else:
            document = (
                JobsSinglePostResponseDataRelationshipsDocument.from_dict(
                    _document
                )
            )

        _documents = d.pop("documents", UNSET)
        documents: JobsSinglePostResponseDataRelationshipsDocuments | Unset
        if isinstance(_documents, Unset):
            documents = UNSET
        else:
            documents = (
                JobsSinglePostResponseDataRelationshipsDocuments.from_dict(
                    _documents
                )
            )

        _project = d.pop("project", UNSET)
        project: JobsSinglePostResponseDataRelationshipsProject | Unset
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = JobsSinglePostResponseDataRelationshipsProject.from_dict(
                _project
            )

        jobs_single_post_response_data_relationships_obj = cls(
            document=document,
            documents=documents,
            project=project,
        )

        jobs_single_post_response_data_relationships_obj.additional_properties = d
        return jobs_single_post_response_data_relationships_obj

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

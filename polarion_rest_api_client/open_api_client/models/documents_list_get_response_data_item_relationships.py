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
    from ..models.documents_list_get_response_data_item_relationships_attachments import (
        DocumentsListGetResponseDataItemRelationshipsAttachments,
    )
    from ..models.documents_list_get_response_data_item_relationships_author import (
        DocumentsListGetResponseDataItemRelationshipsAuthor,
    )
    from ..models.documents_list_get_response_data_item_relationships_branched_from import (
        DocumentsListGetResponseDataItemRelationshipsBranchedFrom,
    )
    from ..models.documents_list_get_response_data_item_relationships_comments import (
        DocumentsListGetResponseDataItemRelationshipsComments,
    )
    from ..models.documents_list_get_response_data_item_relationships_derived_from import (
        DocumentsListGetResponseDataItemRelationshipsDerivedFrom,
    )
    from ..models.documents_list_get_response_data_item_relationships_project import (
        DocumentsListGetResponseDataItemRelationshipsProject,
    )
    from ..models.documents_list_get_response_data_item_relationships_updated_by import (
        DocumentsListGetResponseDataItemRelationshipsUpdatedBy,
    )
    from ..models.documents_list_get_response_data_item_relationships_variant import (
        DocumentsListGetResponseDataItemRelationshipsVariant,
    )


T = TypeVar("T", bound="DocumentsListGetResponseDataItemRelationships")


@_attrs_define
class DocumentsListGetResponseDataItemRelationships:
    """
    Attributes:
        attachments (DocumentsListGetResponseDataItemRelationshipsAttachments | Unset):
        author (DocumentsListGetResponseDataItemRelationshipsAuthor | Unset):
        branched_from (DocumentsListGetResponseDataItemRelationshipsBranchedFrom | Unset):
        comments (DocumentsListGetResponseDataItemRelationshipsComments | Unset):
        derived_from (DocumentsListGetResponseDataItemRelationshipsDerivedFrom | Unset):
        project (DocumentsListGetResponseDataItemRelationshipsProject | Unset):
        updated_by (DocumentsListGetResponseDataItemRelationshipsUpdatedBy | Unset):
        variant (DocumentsListGetResponseDataItemRelationshipsVariant | Unset):
    """

    attachments: (
        DocumentsListGetResponseDataItemRelationshipsAttachments | Unset
    ) = UNSET
    author: DocumentsListGetResponseDataItemRelationshipsAuthor | Unset = UNSET
    branched_from: (
        DocumentsListGetResponseDataItemRelationshipsBranchedFrom | Unset
    ) = UNSET
    comments: DocumentsListGetResponseDataItemRelationshipsComments | Unset = (
        UNSET
    )
    derived_from: (
        DocumentsListGetResponseDataItemRelationshipsDerivedFrom | Unset
    ) = UNSET
    project: DocumentsListGetResponseDataItemRelationshipsProject | Unset = (
        UNSET
    )
    updated_by: (
        DocumentsListGetResponseDataItemRelationshipsUpdatedBy | Unset
    ) = UNSET
    variant: DocumentsListGetResponseDataItemRelationshipsVariant | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        attachments: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        author: dict[str, Any] | Unset = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        branched_from: dict[str, Any] | Unset = UNSET
        if not isinstance(self.branched_from, Unset):
            branched_from = self.branched_from.to_dict()

        comments: dict[str, Any] | Unset = UNSET
        if not isinstance(self.comments, Unset):
            comments = self.comments.to_dict()

        derived_from: dict[str, Any] | Unset = UNSET
        if not isinstance(self.derived_from, Unset):
            derived_from = self.derived_from.to_dict()

        project: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        updated_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.updated_by, Unset):
            updated_by = self.updated_by.to_dict()

        variant: dict[str, Any] | Unset = UNSET
        if not isinstance(self.variant, Unset):
            variant = self.variant.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if author is not UNSET:
            field_dict["author"] = author
        if branched_from is not UNSET:
            field_dict["branchedFrom"] = branched_from
        if comments is not UNSET:
            field_dict["comments"] = comments
        if derived_from is not UNSET:
            field_dict["derivedFrom"] = derived_from
        if project is not UNSET:
            field_dict["project"] = project
        if updated_by is not UNSET:
            field_dict["updatedBy"] = updated_by
        if variant is not UNSET:
            field_dict["variant"] = variant

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.documents_list_get_response_data_item_relationships_attachments import (
            DocumentsListGetResponseDataItemRelationshipsAttachments,
        )
        from ..models.documents_list_get_response_data_item_relationships_author import (
            DocumentsListGetResponseDataItemRelationshipsAuthor,
        )
        from ..models.documents_list_get_response_data_item_relationships_branched_from import (
            DocumentsListGetResponseDataItemRelationshipsBranchedFrom,
        )
        from ..models.documents_list_get_response_data_item_relationships_comments import (
            DocumentsListGetResponseDataItemRelationshipsComments,
        )
        from ..models.documents_list_get_response_data_item_relationships_derived_from import (
            DocumentsListGetResponseDataItemRelationshipsDerivedFrom,
        )
        from ..models.documents_list_get_response_data_item_relationships_project import (
            DocumentsListGetResponseDataItemRelationshipsProject,
        )
        from ..models.documents_list_get_response_data_item_relationships_updated_by import (
            DocumentsListGetResponseDataItemRelationshipsUpdatedBy,
        )
        from ..models.documents_list_get_response_data_item_relationships_variant import (
            DocumentsListGetResponseDataItemRelationshipsVariant,
        )

        d = dict(src_dict)
        _attachments = d.pop("attachments", UNSET)
        attachments: (
            DocumentsListGetResponseDataItemRelationshipsAttachments | Unset
        )
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = DocumentsListGetResponseDataItemRelationshipsAttachments.from_dict(
                _attachments
            )

        _author = d.pop("author", UNSET)
        author: DocumentsListGetResponseDataItemRelationshipsAuthor | Unset
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = (
                DocumentsListGetResponseDataItemRelationshipsAuthor.from_dict(
                    _author
                )
            )

        _branched_from = d.pop("branchedFrom", UNSET)
        branched_from: (
            DocumentsListGetResponseDataItemRelationshipsBranchedFrom | Unset
        )
        if isinstance(_branched_from, Unset):
            branched_from = UNSET
        else:
            branched_from = DocumentsListGetResponseDataItemRelationshipsBranchedFrom.from_dict(
                _branched_from
            )

        _comments = d.pop("comments", UNSET)
        comments: DocumentsListGetResponseDataItemRelationshipsComments | Unset
        if isinstance(_comments, Unset):
            comments = UNSET
        else:
            comments = DocumentsListGetResponseDataItemRelationshipsComments.from_dict(
                _comments
            )

        _derived_from = d.pop("derivedFrom", UNSET)
        derived_from: (
            DocumentsListGetResponseDataItemRelationshipsDerivedFrom | Unset
        )
        if isinstance(_derived_from, Unset):
            derived_from = UNSET
        else:
            derived_from = DocumentsListGetResponseDataItemRelationshipsDerivedFrom.from_dict(
                _derived_from
            )

        _project = d.pop("project", UNSET)
        project: DocumentsListGetResponseDataItemRelationshipsProject | Unset
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = (
                DocumentsListGetResponseDataItemRelationshipsProject.from_dict(
                    _project
                )
            )

        _updated_by = d.pop("updatedBy", UNSET)
        updated_by: (
            DocumentsListGetResponseDataItemRelationshipsUpdatedBy | Unset
        )
        if isinstance(_updated_by, Unset):
            updated_by = UNSET
        else:
            updated_by = DocumentsListGetResponseDataItemRelationshipsUpdatedBy.from_dict(
                _updated_by
            )

        _variant = d.pop("variant", UNSET)
        variant: DocumentsListGetResponseDataItemRelationshipsVariant | Unset
        if isinstance(_variant, Unset):
            variant = UNSET
        else:
            variant = (
                DocumentsListGetResponseDataItemRelationshipsVariant.from_dict(
                    _variant
                )
            )

        documents_list_get_response_data_item_relationships_obj = cls(
            attachments=attachments,
            author=author,
            branched_from=branched_from,
            comments=comments,
            derived_from=derived_from,
            project=project,
            updated_by=updated_by,
            variant=variant,
        )

        documents_list_get_response_data_item_relationships_obj.additional_properties = d
        return documents_list_get_response_data_item_relationships_obj

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

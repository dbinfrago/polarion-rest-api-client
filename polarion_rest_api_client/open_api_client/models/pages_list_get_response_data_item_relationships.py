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
    from ..models.pages_list_get_response_data_item_relationships_attachments import (
        PagesListGetResponseDataItemRelationshipsAttachments,
    )
    from ..models.pages_list_get_response_data_item_relationships_author import (
        PagesListGetResponseDataItemRelationshipsAuthor,
    )
    from ..models.pages_list_get_response_data_item_relationships_project import (
        PagesListGetResponseDataItemRelationshipsProject,
    )
    from ..models.pages_list_get_response_data_item_relationships_updated_by import (
        PagesListGetResponseDataItemRelationshipsUpdatedBy,
    )
    from ..models.pages_list_get_response_data_item_relationships_watches import (
        PagesListGetResponseDataItemRelationshipsWatches,
    )


T = TypeVar("T", bound="PagesListGetResponseDataItemRelationships")


@_attrs_define
class PagesListGetResponseDataItemRelationships:
    """
    Attributes:
        attachments (PagesListGetResponseDataItemRelationshipsAttachments | Unset):
        author (PagesListGetResponseDataItemRelationshipsAuthor | Unset):
        project (PagesListGetResponseDataItemRelationshipsProject | Unset):
        updated_by (PagesListGetResponseDataItemRelationshipsUpdatedBy | Unset):
        watches (PagesListGetResponseDataItemRelationshipsWatches | Unset):
    """

    attachments: (
        PagesListGetResponseDataItemRelationshipsAttachments | Unset
    ) = UNSET
    author: PagesListGetResponseDataItemRelationshipsAuthor | Unset = UNSET
    project: PagesListGetResponseDataItemRelationshipsProject | Unset = UNSET
    updated_by: PagesListGetResponseDataItemRelationshipsUpdatedBy | Unset = (
        UNSET
    )
    watches: PagesListGetResponseDataItemRelationshipsWatches | Unset = UNSET
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

        project: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        updated_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.updated_by, Unset):
            updated_by = self.updated_by.to_dict()

        watches: dict[str, Any] | Unset = UNSET
        if not isinstance(self.watches, Unset):
            watches = self.watches.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if author is not UNSET:
            field_dict["author"] = author
        if project is not UNSET:
            field_dict["project"] = project
        if updated_by is not UNSET:
            field_dict["updatedBy"] = updated_by
        if watches is not UNSET:
            field_dict["watches"] = watches

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pages_list_get_response_data_item_relationships_attachments import (
            PagesListGetResponseDataItemRelationshipsAttachments,
        )
        from ..models.pages_list_get_response_data_item_relationships_author import (
            PagesListGetResponseDataItemRelationshipsAuthor,
        )
        from ..models.pages_list_get_response_data_item_relationships_project import (
            PagesListGetResponseDataItemRelationshipsProject,
        )
        from ..models.pages_list_get_response_data_item_relationships_updated_by import (
            PagesListGetResponseDataItemRelationshipsUpdatedBy,
        )
        from ..models.pages_list_get_response_data_item_relationships_watches import (
            PagesListGetResponseDataItemRelationshipsWatches,
        )

        d = dict(src_dict)
        _attachments = d.pop("attachments", UNSET)
        attachments: (
            PagesListGetResponseDataItemRelationshipsAttachments | Unset
        )
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = (
                PagesListGetResponseDataItemRelationshipsAttachments.from_dict(
                    _attachments
                )
            )

        _author = d.pop("author", UNSET)
        author: PagesListGetResponseDataItemRelationshipsAuthor | Unset
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = PagesListGetResponseDataItemRelationshipsAuthor.from_dict(
                _author
            )

        _project = d.pop("project", UNSET)
        project: PagesListGetResponseDataItemRelationshipsProject | Unset
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = (
                PagesListGetResponseDataItemRelationshipsProject.from_dict(
                    _project
                )
            )

        _updated_by = d.pop("updatedBy", UNSET)
        updated_by: PagesListGetResponseDataItemRelationshipsUpdatedBy | Unset
        if isinstance(_updated_by, Unset):
            updated_by = UNSET
        else:
            updated_by = (
                PagesListGetResponseDataItemRelationshipsUpdatedBy.from_dict(
                    _updated_by
                )
            )

        _watches = d.pop("watches", UNSET)
        watches: PagesListGetResponseDataItemRelationshipsWatches | Unset
        if isinstance(_watches, Unset):
            watches = UNSET
        else:
            watches = (
                PagesListGetResponseDataItemRelationshipsWatches.from_dict(
                    _watches
                )
            )

        pages_list_get_response_data_item_relationships_obj = cls(
            attachments=attachments,
            author=author,
            project=project,
            updated_by=updated_by,
            watches=watches,
        )

        pages_list_get_response_data_item_relationships_obj.additional_properties = d
        return pages_list_get_response_data_item_relationships_obj

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

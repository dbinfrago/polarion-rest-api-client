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
    from ..models.pages_single_get_response_data_relationships_attachments import (
        PagesSingleGetResponseDataRelationshipsAttachments,
    )
    from ..models.pages_single_get_response_data_relationships_author import (
        PagesSingleGetResponseDataRelationshipsAuthor,
    )
    from ..models.pages_single_get_response_data_relationships_project import (
        PagesSingleGetResponseDataRelationshipsProject,
    )
    from ..models.pages_single_get_response_data_relationships_updated_by import (
        PagesSingleGetResponseDataRelationshipsUpdatedBy,
    )
    from ..models.pages_single_get_response_data_relationships_watches import (
        PagesSingleGetResponseDataRelationshipsWatches,
    )


T = TypeVar("T", bound="PagesSingleGetResponseDataRelationships")


@_attrs_define
class PagesSingleGetResponseDataRelationships:
    """
    Attributes:
        attachments (PagesSingleGetResponseDataRelationshipsAttachments | Unset):
        author (PagesSingleGetResponseDataRelationshipsAuthor | Unset):
        project (PagesSingleGetResponseDataRelationshipsProject | Unset):
        updated_by (PagesSingleGetResponseDataRelationshipsUpdatedBy | Unset):
        watches (PagesSingleGetResponseDataRelationshipsWatches | Unset):
    """

    attachments: PagesSingleGetResponseDataRelationshipsAttachments | Unset = (
        UNSET
    )
    author: PagesSingleGetResponseDataRelationshipsAuthor | Unset = UNSET
    project: PagesSingleGetResponseDataRelationshipsProject | Unset = UNSET
    updated_by: PagesSingleGetResponseDataRelationshipsUpdatedBy | Unset = (
        UNSET
    )
    watches: PagesSingleGetResponseDataRelationshipsWatches | Unset = UNSET
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
        from ..models.pages_single_get_response_data_relationships_attachments import (
            PagesSingleGetResponseDataRelationshipsAttachments,
        )
        from ..models.pages_single_get_response_data_relationships_author import (
            PagesSingleGetResponseDataRelationshipsAuthor,
        )
        from ..models.pages_single_get_response_data_relationships_project import (
            PagesSingleGetResponseDataRelationshipsProject,
        )
        from ..models.pages_single_get_response_data_relationships_updated_by import (
            PagesSingleGetResponseDataRelationshipsUpdatedBy,
        )
        from ..models.pages_single_get_response_data_relationships_watches import (
            PagesSingleGetResponseDataRelationshipsWatches,
        )

        d = dict(src_dict)
        _attachments = d.pop("attachments", UNSET)
        attachments: PagesSingleGetResponseDataRelationshipsAttachments | Unset
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = (
                PagesSingleGetResponseDataRelationshipsAttachments.from_dict(
                    _attachments
                )
            )

        _author = d.pop("author", UNSET)
        author: PagesSingleGetResponseDataRelationshipsAuthor | Unset
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = PagesSingleGetResponseDataRelationshipsAuthor.from_dict(
                _author
            )

        _project = d.pop("project", UNSET)
        project: PagesSingleGetResponseDataRelationshipsProject | Unset
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = PagesSingleGetResponseDataRelationshipsProject.from_dict(
                _project
            )

        _updated_by = d.pop("updatedBy", UNSET)
        updated_by: PagesSingleGetResponseDataRelationshipsUpdatedBy | Unset
        if isinstance(_updated_by, Unset):
            updated_by = UNSET
        else:
            updated_by = (
                PagesSingleGetResponseDataRelationshipsUpdatedBy.from_dict(
                    _updated_by
                )
            )

        _watches = d.pop("watches", UNSET)
        watches: PagesSingleGetResponseDataRelationshipsWatches | Unset
        if isinstance(_watches, Unset):
            watches = UNSET
        else:
            watches = PagesSingleGetResponseDataRelationshipsWatches.from_dict(
                _watches
            )

        pages_single_get_response_data_relationships_obj = cls(
            attachments=attachments,
            author=author,
            project=project,
            updated_by=updated_by,
            watches=watches,
        )

        pages_single_get_response_data_relationships_obj.additional_properties = d
        return pages_single_get_response_data_relationships_obj

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

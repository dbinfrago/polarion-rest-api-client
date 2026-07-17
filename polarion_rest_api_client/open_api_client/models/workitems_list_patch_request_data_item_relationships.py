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
    from ..models.workitems_list_patch_request_data_item_relationships_assignee import (
        WorkitemsListPatchRequestDataItemRelationshipsAssignee,
    )
    from ..models.workitems_list_patch_request_data_item_relationships_categories import (
        WorkitemsListPatchRequestDataItemRelationshipsCategories,
    )
    from ..models.workitems_list_patch_request_data_item_relationships_linked_revisions import (
        WorkitemsListPatchRequestDataItemRelationshipsLinkedRevisions,
    )
    from ..models.workitems_list_patch_request_data_item_relationships_votes import (
        WorkitemsListPatchRequestDataItemRelationshipsVotes,
    )
    from ..models.workitems_list_patch_request_data_item_relationships_watches import (
        WorkitemsListPatchRequestDataItemRelationshipsWatches,
    )


T = TypeVar("T", bound="WorkitemsListPatchRequestDataItemRelationships")


@_attrs_define
class WorkitemsListPatchRequestDataItemRelationships:
    """
    Attributes:
        assignee (WorkitemsListPatchRequestDataItemRelationshipsAssignee | Unset):
        categories (WorkitemsListPatchRequestDataItemRelationshipsCategories | Unset):
        linked_revisions (WorkitemsListPatchRequestDataItemRelationshipsLinkedRevisions | Unset):
        votes (WorkitemsListPatchRequestDataItemRelationshipsVotes | Unset):
        watches (WorkitemsListPatchRequestDataItemRelationshipsWatches | Unset):
    """

    assignee: (
        WorkitemsListPatchRequestDataItemRelationshipsAssignee | Unset
    ) = UNSET
    categories: (
        WorkitemsListPatchRequestDataItemRelationshipsCategories | Unset
    ) = UNSET
    linked_revisions: (
        WorkitemsListPatchRequestDataItemRelationshipsLinkedRevisions | Unset
    ) = UNSET
    votes: WorkitemsListPatchRequestDataItemRelationshipsVotes | Unset = UNSET
    watches: WorkitemsListPatchRequestDataItemRelationshipsWatches | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        assignee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.assignee, Unset):
            assignee = self.assignee.to_dict()

        categories: dict[str, Any] | Unset = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories.to_dict()

        linked_revisions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.linked_revisions, Unset):
            linked_revisions = self.linked_revisions.to_dict()

        votes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.votes, Unset):
            votes = self.votes.to_dict()

        watches: dict[str, Any] | Unset = UNSET
        if not isinstance(self.watches, Unset):
            watches = self.watches.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if categories is not UNSET:
            field_dict["categories"] = categories
        if linked_revisions is not UNSET:
            field_dict["linkedRevisions"] = linked_revisions
        if votes is not UNSET:
            field_dict["votes"] = votes
        if watches is not UNSET:
            field_dict["watches"] = watches

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workitems_list_patch_request_data_item_relationships_assignee import (
            WorkitemsListPatchRequestDataItemRelationshipsAssignee,
        )
        from ..models.workitems_list_patch_request_data_item_relationships_categories import (
            WorkitemsListPatchRequestDataItemRelationshipsCategories,
        )
        from ..models.workitems_list_patch_request_data_item_relationships_linked_revisions import (
            WorkitemsListPatchRequestDataItemRelationshipsLinkedRevisions,
        )
        from ..models.workitems_list_patch_request_data_item_relationships_votes import (
            WorkitemsListPatchRequestDataItemRelationshipsVotes,
        )
        from ..models.workitems_list_patch_request_data_item_relationships_watches import (
            WorkitemsListPatchRequestDataItemRelationshipsWatches,
        )

        d = dict(src_dict)
        _assignee = d.pop("assignee", UNSET)
        assignee: (
            WorkitemsListPatchRequestDataItemRelationshipsAssignee | Unset
        )
        if isinstance(_assignee, Unset):
            assignee = UNSET
        else:
            assignee = WorkitemsListPatchRequestDataItemRelationshipsAssignee.from_dict(
                _assignee
            )

        _categories = d.pop("categories", UNSET)
        categories: (
            WorkitemsListPatchRequestDataItemRelationshipsCategories | Unset
        )
        if isinstance(_categories, Unset):
            categories = UNSET
        else:
            categories = WorkitemsListPatchRequestDataItemRelationshipsCategories.from_dict(
                _categories
            )

        _linked_revisions = d.pop("linkedRevisions", UNSET)
        linked_revisions: (
            WorkitemsListPatchRequestDataItemRelationshipsLinkedRevisions
            | Unset
        )
        if isinstance(_linked_revisions, Unset):
            linked_revisions = UNSET
        else:
            linked_revisions = WorkitemsListPatchRequestDataItemRelationshipsLinkedRevisions.from_dict(
                _linked_revisions
            )

        _votes = d.pop("votes", UNSET)
        votes: WorkitemsListPatchRequestDataItemRelationshipsVotes | Unset
        if isinstance(_votes, Unset):
            votes = UNSET
        else:
            votes = (
                WorkitemsListPatchRequestDataItemRelationshipsVotes.from_dict(
                    _votes
                )
            )

        _watches = d.pop("watches", UNSET)
        watches: WorkitemsListPatchRequestDataItemRelationshipsWatches | Unset
        if isinstance(_watches, Unset):
            watches = UNSET
        else:
            watches = WorkitemsListPatchRequestDataItemRelationshipsWatches.from_dict(
                _watches
            )

        workitems_list_patch_request_data_item_relationships_obj = cls(
            assignee=assignee,
            categories=categories,
            linked_revisions=linked_revisions,
            votes=votes,
            watches=watches,
        )

        workitems_list_patch_request_data_item_relationships_obj.additional_properties = d
        return workitems_list_patch_request_data_item_relationships_obj

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

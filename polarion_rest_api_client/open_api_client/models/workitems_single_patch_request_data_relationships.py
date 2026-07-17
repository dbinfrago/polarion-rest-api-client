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
    from ..models.workitems_single_patch_request_data_relationships_assignee import (
        WorkitemsSinglePatchRequestDataRelationshipsAssignee,
    )
    from ..models.workitems_single_patch_request_data_relationships_categories import (
        WorkitemsSinglePatchRequestDataRelationshipsCategories,
    )
    from ..models.workitems_single_patch_request_data_relationships_linked_revisions import (
        WorkitemsSinglePatchRequestDataRelationshipsLinkedRevisions,
    )
    from ..models.workitems_single_patch_request_data_relationships_votes import (
        WorkitemsSinglePatchRequestDataRelationshipsVotes,
    )
    from ..models.workitems_single_patch_request_data_relationships_watches import (
        WorkitemsSinglePatchRequestDataRelationshipsWatches,
    )


T = TypeVar("T", bound="WorkitemsSinglePatchRequestDataRelationships")


@_attrs_define
class WorkitemsSinglePatchRequestDataRelationships:
    """
    Attributes:
        assignee (WorkitemsSinglePatchRequestDataRelationshipsAssignee | Unset):
        categories (WorkitemsSinglePatchRequestDataRelationshipsCategories | Unset):
        linked_revisions (WorkitemsSinglePatchRequestDataRelationshipsLinkedRevisions | Unset):
        votes (WorkitemsSinglePatchRequestDataRelationshipsVotes | Unset):
        watches (WorkitemsSinglePatchRequestDataRelationshipsWatches | Unset):
    """

    assignee: WorkitemsSinglePatchRequestDataRelationshipsAssignee | Unset = (
        UNSET
    )
    categories: (
        WorkitemsSinglePatchRequestDataRelationshipsCategories | Unset
    ) = UNSET
    linked_revisions: (
        WorkitemsSinglePatchRequestDataRelationshipsLinkedRevisions | Unset
    ) = UNSET
    votes: WorkitemsSinglePatchRequestDataRelationshipsVotes | Unset = UNSET
    watches: WorkitemsSinglePatchRequestDataRelationshipsWatches | Unset = (
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
        from ..models.workitems_single_patch_request_data_relationships_assignee import (
            WorkitemsSinglePatchRequestDataRelationshipsAssignee,
        )
        from ..models.workitems_single_patch_request_data_relationships_categories import (
            WorkitemsSinglePatchRequestDataRelationshipsCategories,
        )
        from ..models.workitems_single_patch_request_data_relationships_linked_revisions import (
            WorkitemsSinglePatchRequestDataRelationshipsLinkedRevisions,
        )
        from ..models.workitems_single_patch_request_data_relationships_votes import (
            WorkitemsSinglePatchRequestDataRelationshipsVotes,
        )
        from ..models.workitems_single_patch_request_data_relationships_watches import (
            WorkitemsSinglePatchRequestDataRelationshipsWatches,
        )

        d = dict(src_dict)
        _assignee = d.pop("assignee", UNSET)
        assignee: WorkitemsSinglePatchRequestDataRelationshipsAssignee | Unset
        if isinstance(_assignee, Unset):
            assignee = UNSET
        else:
            assignee = (
                WorkitemsSinglePatchRequestDataRelationshipsAssignee.from_dict(
                    _assignee
                )
            )

        _categories = d.pop("categories", UNSET)
        categories: (
            WorkitemsSinglePatchRequestDataRelationshipsCategories | Unset
        )
        if isinstance(_categories, Unset):
            categories = UNSET
        else:
            categories = WorkitemsSinglePatchRequestDataRelationshipsCategories.from_dict(
                _categories
            )

        _linked_revisions = d.pop("linkedRevisions", UNSET)
        linked_revisions: (
            WorkitemsSinglePatchRequestDataRelationshipsLinkedRevisions | Unset
        )
        if isinstance(_linked_revisions, Unset):
            linked_revisions = UNSET
        else:
            linked_revisions = WorkitemsSinglePatchRequestDataRelationshipsLinkedRevisions.from_dict(
                _linked_revisions
            )

        _votes = d.pop("votes", UNSET)
        votes: WorkitemsSinglePatchRequestDataRelationshipsVotes | Unset
        if isinstance(_votes, Unset):
            votes = UNSET
        else:
            votes = (
                WorkitemsSinglePatchRequestDataRelationshipsVotes.from_dict(
                    _votes
                )
            )

        _watches = d.pop("watches", UNSET)
        watches: WorkitemsSinglePatchRequestDataRelationshipsWatches | Unset
        if isinstance(_watches, Unset):
            watches = UNSET
        else:
            watches = (
                WorkitemsSinglePatchRequestDataRelationshipsWatches.from_dict(
                    _watches
                )
            )

        workitems_single_patch_request_data_relationships_obj = cls(
            assignee=assignee,
            categories=categories,
            linked_revisions=linked_revisions,
            votes=votes,
            watches=watches,
        )

        workitems_single_patch_request_data_relationships_obj.additional_properties = d
        return workitems_single_patch_request_data_relationships_obj

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

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
    from ..models.workitems_list_post_request_data_item_relationships_assignee import (
        WorkitemsListPostRequestDataItemRelationshipsAssignee,
    )
    from ..models.workitems_list_post_request_data_item_relationships_author import (
        WorkitemsListPostRequestDataItemRelationshipsAuthor,
    )
    from ..models.workitems_list_post_request_data_item_relationships_categories import (
        WorkitemsListPostRequestDataItemRelationshipsCategories,
    )
    from ..models.workitems_list_post_request_data_item_relationships_linked_revisions import (
        WorkitemsListPostRequestDataItemRelationshipsLinkedRevisions,
    )
    from ..models.workitems_list_post_request_data_item_relationships_module import (
        WorkitemsListPostRequestDataItemRelationshipsModule,
    )


T = TypeVar("T", bound="WorkitemsListPostRequestDataItemRelationships")


@_attrs_define
class WorkitemsListPostRequestDataItemRelationships:
    """
    Attributes:
        assignee (WorkitemsListPostRequestDataItemRelationshipsAssignee | Unset):
        author (WorkitemsListPostRequestDataItemRelationshipsAuthor | Unset):
        categories (WorkitemsListPostRequestDataItemRelationshipsCategories | Unset):
        linked_revisions (WorkitemsListPostRequestDataItemRelationshipsLinkedRevisions | Unset):
        module (WorkitemsListPostRequestDataItemRelationshipsModule | Unset):
    """

    assignee: WorkitemsListPostRequestDataItemRelationshipsAssignee | Unset = (
        UNSET
    )
    author: WorkitemsListPostRequestDataItemRelationshipsAuthor | Unset = UNSET
    categories: (
        WorkitemsListPostRequestDataItemRelationshipsCategories | Unset
    ) = UNSET
    linked_revisions: (
        WorkitemsListPostRequestDataItemRelationshipsLinkedRevisions | Unset
    ) = UNSET
    module: WorkitemsListPostRequestDataItemRelationshipsModule | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        assignee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.assignee, Unset):
            assignee = self.assignee.to_dict()

        author: dict[str, Any] | Unset = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        categories: dict[str, Any] | Unset = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories.to_dict()

        linked_revisions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.linked_revisions, Unset):
            linked_revisions = self.linked_revisions.to_dict()

        module: dict[str, Any] | Unset = UNSET
        if not isinstance(self.module, Unset):
            module = self.module.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if author is not UNSET:
            field_dict["author"] = author
        if categories is not UNSET:
            field_dict["categories"] = categories
        if linked_revisions is not UNSET:
            field_dict["linkedRevisions"] = linked_revisions
        if module is not UNSET:
            field_dict["module"] = module

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workitems_list_post_request_data_item_relationships_assignee import (
            WorkitemsListPostRequestDataItemRelationshipsAssignee,
        )
        from ..models.workitems_list_post_request_data_item_relationships_author import (
            WorkitemsListPostRequestDataItemRelationshipsAuthor,
        )
        from ..models.workitems_list_post_request_data_item_relationships_categories import (
            WorkitemsListPostRequestDataItemRelationshipsCategories,
        )
        from ..models.workitems_list_post_request_data_item_relationships_linked_revisions import (
            WorkitemsListPostRequestDataItemRelationshipsLinkedRevisions,
        )
        from ..models.workitems_list_post_request_data_item_relationships_module import (
            WorkitemsListPostRequestDataItemRelationshipsModule,
        )

        d = dict(src_dict)
        _assignee = d.pop("assignee", UNSET)
        assignee: WorkitemsListPostRequestDataItemRelationshipsAssignee | Unset
        if isinstance(_assignee, Unset):
            assignee = UNSET
        else:
            assignee = WorkitemsListPostRequestDataItemRelationshipsAssignee.from_dict(
                _assignee
            )

        _author = d.pop("author", UNSET)
        author: WorkitemsListPostRequestDataItemRelationshipsAuthor | Unset
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = (
                WorkitemsListPostRequestDataItemRelationshipsAuthor.from_dict(
                    _author
                )
            )

        _categories = d.pop("categories", UNSET)
        categories: (
            WorkitemsListPostRequestDataItemRelationshipsCategories | Unset
        )
        if isinstance(_categories, Unset):
            categories = UNSET
        else:
            categories = WorkitemsListPostRequestDataItemRelationshipsCategories.from_dict(
                _categories
            )

        _linked_revisions = d.pop("linkedRevisions", UNSET)
        linked_revisions: (
            WorkitemsListPostRequestDataItemRelationshipsLinkedRevisions
            | Unset
        )
        if isinstance(_linked_revisions, Unset):
            linked_revisions = UNSET
        else:
            linked_revisions = WorkitemsListPostRequestDataItemRelationshipsLinkedRevisions.from_dict(
                _linked_revisions
            )

        _module = d.pop("module", UNSET)
        module: WorkitemsListPostRequestDataItemRelationshipsModule | Unset
        if isinstance(_module, Unset):
            module = UNSET
        else:
            module = (
                WorkitemsListPostRequestDataItemRelationshipsModule.from_dict(
                    _module
                )
            )

        workitems_list_post_request_data_item_relationships_obj = cls(
            assignee=assignee,
            author=author,
            categories=categories,
            linked_revisions=linked_revisions,
            module=module,
        )

        workitems_list_post_request_data_item_relationships_obj.additional_properties = d
        return workitems_list_post_request_data_item_relationships_obj

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

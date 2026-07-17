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
    from ..models.plans_list_get_response_data_item_relationships_author import (
        PlansListGetResponseDataItemRelationshipsAuthor,
    )
    from ..models.plans_list_get_response_data_item_relationships_parent import (
        PlansListGetResponseDataItemRelationshipsParent,
    )
    from ..models.plans_list_get_response_data_item_relationships_project import (
        PlansListGetResponseDataItemRelationshipsProject,
    )
    from ..models.plans_list_get_response_data_item_relationships_project_span import (
        PlansListGetResponseDataItemRelationshipsProjectSpan,
    )
    from ..models.plans_list_get_response_data_item_relationships_template import (
        PlansListGetResponseDataItemRelationshipsTemplate,
    )
    from ..models.plans_list_get_response_data_item_relationships_work_items import (
        PlansListGetResponseDataItemRelationshipsWorkItems,
    )


T = TypeVar("T", bound="PlansListGetResponseDataItemRelationships")


@_attrs_define
class PlansListGetResponseDataItemRelationships:
    """
    Attributes:
        author (PlansListGetResponseDataItemRelationshipsAuthor | Unset):
        parent (PlansListGetResponseDataItemRelationshipsParent | Unset):
        project (PlansListGetResponseDataItemRelationshipsProject | Unset):
        project_span (PlansListGetResponseDataItemRelationshipsProjectSpan | Unset):
        template (PlansListGetResponseDataItemRelationshipsTemplate | Unset):
        work_items (PlansListGetResponseDataItemRelationshipsWorkItems | Unset):
    """

    author: PlansListGetResponseDataItemRelationshipsAuthor | Unset = UNSET
    parent: PlansListGetResponseDataItemRelationshipsParent | Unset = UNSET
    project: PlansListGetResponseDataItemRelationshipsProject | Unset = UNSET
    project_span: (
        PlansListGetResponseDataItemRelationshipsProjectSpan | Unset
    ) = UNSET
    template: PlansListGetResponseDataItemRelationshipsTemplate | Unset = UNSET
    work_items: PlansListGetResponseDataItemRelationshipsWorkItems | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        author: dict[str, Any] | Unset = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        parent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

        project: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        project_span: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_span, Unset):
            project_span = self.project_span.to_dict()

        template: dict[str, Any] | Unset = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.to_dict()

        work_items: dict[str, Any] | Unset = UNSET
        if not isinstance(self.work_items, Unset):
            work_items = self.work_items.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if author is not UNSET:
            field_dict["author"] = author
        if parent is not UNSET:
            field_dict["parent"] = parent
        if project is not UNSET:
            field_dict["project"] = project
        if project_span is not UNSET:
            field_dict["projectSpan"] = project_span
        if template is not UNSET:
            field_dict["template"] = template
        if work_items is not UNSET:
            field_dict["workItems"] = work_items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plans_list_get_response_data_item_relationships_author import (
            PlansListGetResponseDataItemRelationshipsAuthor,
        )
        from ..models.plans_list_get_response_data_item_relationships_parent import (
            PlansListGetResponseDataItemRelationshipsParent,
        )
        from ..models.plans_list_get_response_data_item_relationships_project import (
            PlansListGetResponseDataItemRelationshipsProject,
        )
        from ..models.plans_list_get_response_data_item_relationships_project_span import (
            PlansListGetResponseDataItemRelationshipsProjectSpan,
        )
        from ..models.plans_list_get_response_data_item_relationships_template import (
            PlansListGetResponseDataItemRelationshipsTemplate,
        )
        from ..models.plans_list_get_response_data_item_relationships_work_items import (
            PlansListGetResponseDataItemRelationshipsWorkItems,
        )

        d = dict(src_dict)
        _author = d.pop("author", UNSET)
        author: PlansListGetResponseDataItemRelationshipsAuthor | Unset
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = PlansListGetResponseDataItemRelationshipsAuthor.from_dict(
                _author
            )

        _parent = d.pop("parent", UNSET)
        parent: PlansListGetResponseDataItemRelationshipsParent | Unset
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = PlansListGetResponseDataItemRelationshipsParent.from_dict(
                _parent
            )

        _project = d.pop("project", UNSET)
        project: PlansListGetResponseDataItemRelationshipsProject | Unset
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = (
                PlansListGetResponseDataItemRelationshipsProject.from_dict(
                    _project
                )
            )

        _project_span = d.pop("projectSpan", UNSET)
        project_span: (
            PlansListGetResponseDataItemRelationshipsProjectSpan | Unset
        )
        if isinstance(_project_span, Unset):
            project_span = UNSET
        else:
            project_span = (
                PlansListGetResponseDataItemRelationshipsProjectSpan.from_dict(
                    _project_span
                )
            )

        _template = d.pop("template", UNSET)
        template: PlansListGetResponseDataItemRelationshipsTemplate | Unset
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = (
                PlansListGetResponseDataItemRelationshipsTemplate.from_dict(
                    _template
                )
            )

        _work_items = d.pop("workItems", UNSET)
        work_items: PlansListGetResponseDataItemRelationshipsWorkItems | Unset
        if isinstance(_work_items, Unset):
            work_items = UNSET
        else:
            work_items = (
                PlansListGetResponseDataItemRelationshipsWorkItems.from_dict(
                    _work_items
                )
            )

        plans_list_get_response_data_item_relationships_obj = cls(
            author=author,
            parent=parent,
            project=project,
            project_span=project_span,
            template=template,
            work_items=work_items,
        )

        plans_list_get_response_data_item_relationships_obj.additional_properties = d
        return plans_list_get_response_data_item_relationships_obj

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

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
    from ..models.plans_list_post_request_data_item_relationships_parent import (
        PlansListPostRequestDataItemRelationshipsParent,
    )
    from ..models.plans_list_post_request_data_item_relationships_project_span import (
        PlansListPostRequestDataItemRelationshipsProjectSpan,
    )
    from ..models.plans_list_post_request_data_item_relationships_template import (
        PlansListPostRequestDataItemRelationshipsTemplate,
    )
    from ..models.plans_list_post_request_data_item_relationships_work_items import (
        PlansListPostRequestDataItemRelationshipsWorkItems,
    )


T = TypeVar("T", bound="PlansListPostRequestDataItemRelationships")


@_attrs_define
class PlansListPostRequestDataItemRelationships:
    """
    Attributes:
        parent (PlansListPostRequestDataItemRelationshipsParent | Unset):
        project_span (PlansListPostRequestDataItemRelationshipsProjectSpan | Unset):
        template (PlansListPostRequestDataItemRelationshipsTemplate | Unset):
        work_items (PlansListPostRequestDataItemRelationshipsWorkItems | Unset):
    """

    parent: PlansListPostRequestDataItemRelationshipsParent | Unset = UNSET
    project_span: (
        PlansListPostRequestDataItemRelationshipsProjectSpan | Unset
    ) = UNSET
    template: PlansListPostRequestDataItemRelationshipsTemplate | Unset = UNSET
    work_items: PlansListPostRequestDataItemRelationshipsWorkItems | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        parent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

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
        if parent is not UNSET:
            field_dict["parent"] = parent
        if project_span is not UNSET:
            field_dict["projectSpan"] = project_span
        if template is not UNSET:
            field_dict["template"] = template
        if work_items is not UNSET:
            field_dict["workItems"] = work_items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plans_list_post_request_data_item_relationships_parent import (
            PlansListPostRequestDataItemRelationshipsParent,
        )
        from ..models.plans_list_post_request_data_item_relationships_project_span import (
            PlansListPostRequestDataItemRelationshipsProjectSpan,
        )
        from ..models.plans_list_post_request_data_item_relationships_template import (
            PlansListPostRequestDataItemRelationshipsTemplate,
        )
        from ..models.plans_list_post_request_data_item_relationships_work_items import (
            PlansListPostRequestDataItemRelationshipsWorkItems,
        )

        d = dict(src_dict)
        _parent = d.pop("parent", UNSET)
        parent: PlansListPostRequestDataItemRelationshipsParent | Unset
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = PlansListPostRequestDataItemRelationshipsParent.from_dict(
                _parent
            )

        _project_span = d.pop("projectSpan", UNSET)
        project_span: (
            PlansListPostRequestDataItemRelationshipsProjectSpan | Unset
        )
        if isinstance(_project_span, Unset):
            project_span = UNSET
        else:
            project_span = (
                PlansListPostRequestDataItemRelationshipsProjectSpan.from_dict(
                    _project_span
                )
            )

        _template = d.pop("template", UNSET)
        template: PlansListPostRequestDataItemRelationshipsTemplate | Unset
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = (
                PlansListPostRequestDataItemRelationshipsTemplate.from_dict(
                    _template
                )
            )

        _work_items = d.pop("workItems", UNSET)
        work_items: PlansListPostRequestDataItemRelationshipsWorkItems | Unset
        if isinstance(_work_items, Unset):
            work_items = UNSET
        else:
            work_items = (
                PlansListPostRequestDataItemRelationshipsWorkItems.from_dict(
                    _work_items
                )
            )

        plans_list_post_request_data_item_relationships_obj = cls(
            parent=parent,
            project_span=project_span,
            template=template,
            work_items=work_items,
        )

        plans_list_post_request_data_item_relationships_obj.additional_properties = d
        return plans_list_post_request_data_item_relationships_obj

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

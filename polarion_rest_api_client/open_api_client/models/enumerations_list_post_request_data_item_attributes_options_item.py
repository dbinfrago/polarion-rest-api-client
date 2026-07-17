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
    from ..models.enumerations_list_post_request_data_item_attributes_options_item_link_rules_item import (
        EnumerationsListPostRequestDataItemAttributesOptionsItemLinkRulesItem,
    )


T = TypeVar(
    "T", bound="EnumerationsListPostRequestDataItemAttributesOptionsItem"
)


@_attrs_define
class EnumerationsListPostRequestDataItemAttributesOptionsItem:
    """
    Attributes:
        color (str | Unset):  Example: #F9FF4D.
        column_width (str | Unset):  Example: 90%.
        create_defect (bool | Unset):  Example: True.
        default (bool | Unset):  Example: True.
        description (str | Unset):  Example: Description.
        hidden (bool | Unset):
        icon_url (str | Unset):  Example: /polarion/icons/default/enums/status_open.gif.
        id (str | Unset):  Example: open.
        limited (bool | Unset):  Example: True.
        link_rules (list[EnumerationsListPostRequestDataItemAttributesOptionsItemLinkRulesItem] | Unset):
        min_value (float | Unset):  Example: 30.0.
        name (str | Unset):  Example: Open.
        opposite_name (str | Unset):  Example: Opposite Name.
        parent (bool | Unset):  Example: True.
        requires_signature_for_test_case_execution (bool | Unset):  Example: True.
        template_work_item (str | Unset):  Example: exampleTemplate.
        terminal (bool | Unset):  Example: True.
    """

    color: str | Unset = UNSET
    column_width: str | Unset = UNSET
    create_defect: bool | Unset = UNSET
    default: bool | Unset = UNSET
    description: str | Unset = UNSET
    hidden: bool | Unset = UNSET
    icon_url: str | Unset = UNSET
    id: str | Unset = UNSET
    limited: bool | Unset = UNSET
    link_rules: (
        list[
            EnumerationsListPostRequestDataItemAttributesOptionsItemLinkRulesItem
        ]
        | Unset
    ) = UNSET
    min_value: float | Unset = UNSET
    name: str | Unset = UNSET
    opposite_name: str | Unset = UNSET
    parent: bool | Unset = UNSET
    requires_signature_for_test_case_execution: bool | Unset = UNSET
    template_work_item: str | Unset = UNSET
    terminal: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        color = self.color

        column_width = self.column_width

        create_defect = self.create_defect

        default = self.default

        description = self.description

        hidden = self.hidden

        icon_url = self.icon_url

        id = self.id

        limited = self.limited

        link_rules: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.link_rules, Unset):
            link_rules = []
            for link_rules_item_data in self.link_rules:
                link_rules_item = link_rules_item_data.to_dict()
                link_rules.append(link_rules_item)

        min_value = self.min_value

        name = self.name

        opposite_name = self.opposite_name

        parent = self.parent

        requires_signature_for_test_case_execution = (
            self.requires_signature_for_test_case_execution
        )

        template_work_item = self.template_work_item

        terminal = self.terminal

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if color is not UNSET:
            field_dict["color"] = color
        if column_width is not UNSET:
            field_dict["columnWidth"] = column_width
        if create_defect is not UNSET:
            field_dict["createDefect"] = create_defect
        if default is not UNSET:
            field_dict["default"] = default
        if description is not UNSET:
            field_dict["description"] = description
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if icon_url is not UNSET:
            field_dict["iconURL"] = icon_url
        if id is not UNSET:
            field_dict["id"] = id
        if limited is not UNSET:
            field_dict["limited"] = limited
        if link_rules is not UNSET:
            field_dict["linkRules"] = link_rules
        if min_value is not UNSET:
            field_dict["minValue"] = min_value
        if name is not UNSET:
            field_dict["name"] = name
        if opposite_name is not UNSET:
            field_dict["oppositeName"] = opposite_name
        if parent is not UNSET:
            field_dict["parent"] = parent
        if requires_signature_for_test_case_execution is not UNSET:
            field_dict["requiresSignatureForTestCaseExecution"] = (
                requires_signature_for_test_case_execution
            )
        if template_work_item is not UNSET:
            field_dict["templateWorkItem"] = template_work_item
        if terminal is not UNSET:
            field_dict["terminal"] = terminal

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.enumerations_list_post_request_data_item_attributes_options_item_link_rules_item import (
            EnumerationsListPostRequestDataItemAttributesOptionsItemLinkRulesItem,
        )

        d = dict(src_dict)
        color = d.pop("color", UNSET)

        column_width = d.pop("columnWidth", UNSET)

        create_defect = d.pop("createDefect", UNSET)

        default = d.pop("default", UNSET)

        description = d.pop("description", UNSET)

        hidden = d.pop("hidden", UNSET)

        icon_url = d.pop("iconURL", UNSET)

        id = d.pop("id", UNSET)

        limited = d.pop("limited", UNSET)

        _link_rules = d.pop("linkRules", UNSET)
        link_rules: (
            list[
                EnumerationsListPostRequestDataItemAttributesOptionsItemLinkRulesItem
            ]
            | Unset
        ) = UNSET
        if _link_rules is not UNSET:
            link_rules = []
            for link_rules_item_data in _link_rules:
                link_rules_item = EnumerationsListPostRequestDataItemAttributesOptionsItemLinkRulesItem.from_dict(
                    link_rules_item_data
                )

                link_rules.append(link_rules_item)

        min_value = d.pop("minValue", UNSET)

        name = d.pop("name", UNSET)

        opposite_name = d.pop("oppositeName", UNSET)

        parent = d.pop("parent", UNSET)

        requires_signature_for_test_case_execution = d.pop(
            "requiresSignatureForTestCaseExecution", UNSET
        )

        template_work_item = d.pop("templateWorkItem", UNSET)

        terminal = d.pop("terminal", UNSET)

        enumerations_list_post_request_data_item_attributes_options_item_obj = cls(
            color=color,
            column_width=column_width,
            create_defect=create_defect,
            default=default,
            description=description,
            hidden=hidden,
            icon_url=icon_url,
            id=id,
            limited=limited,
            link_rules=link_rules,
            min_value=min_value,
            name=name,
            opposite_name=opposite_name,
            parent=parent,
            requires_signature_for_test_case_execution=requires_signature_for_test_case_execution,
            template_work_item=template_work_item,
            terminal=terminal,
        )

        enumerations_list_post_request_data_item_attributes_options_item_obj.additional_properties = d
        return enumerations_list_post_request_data_item_attributes_options_item_obj

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

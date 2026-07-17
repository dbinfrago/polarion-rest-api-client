# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentPartsListGetResponseDataItemAttributes")


@_attrs_define
class DocumentPartsListGetResponseDataItemAttributes:
    """
    Attributes:
        content (str | Unset): Editable only for normal and table document parts. Example: <div id="polarion_wiki macro
            name=module-workitem;params=id=workitem_MyWorkItemId"></div>.
        external (bool | Unset): Whether the work item is external to the document. Applicable to: workitem parts.
        heading_text (str | Unset): Applicable to: heading parts. Example: Heading Title.
        id (str | Unset):  Example: workitem_MyWorkItemId.
        landscape (bool | Unset): Whether the page break switches to landscape orientation. Applicable to: pagebreak
            parts.
        layout (int | Unset): Rendering layout index for the part. Applicable to: workitem parts.
        level (int | Unset): Outline level/depth of the part in the document hierarchy. Applicable to: heading, workitem
            parts.
        sequence (str | Unset): Sequence identifier for table of figures entry. Applicable to: tof parts. Example:
            Table.
        type_ (str | Unset): Possible values: heading, normal, pagebreak, table, toc, tof, wikiblock, workitem. Required
            for creation. Example: workitem.
        wiki_text (str | Unset): Wiki markup content for the block. Applicable to: wikiblock parts. Example:
            #documentPanel(true "approved").
    """

    content: str | Unset = UNSET
    external: bool | Unset = UNSET
    heading_text: str | Unset = UNSET
    id: str | Unset = UNSET
    landscape: bool | Unset = UNSET
    layout: int | Unset = UNSET
    level: int | Unset = UNSET
    sequence: str | Unset = UNSET
    type_: str | Unset = UNSET
    wiki_text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        external = self.external

        heading_text = self.heading_text

        id = self.id

        landscape = self.landscape

        layout = self.layout

        level = self.level

        sequence = self.sequence

        type_ = self.type_

        wiki_text = self.wiki_text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if external is not UNSET:
            field_dict["external"] = external
        if heading_text is not UNSET:
            field_dict["headingText"] = heading_text
        if id is not UNSET:
            field_dict["id"] = id
        if landscape is not UNSET:
            field_dict["landscape"] = landscape
        if layout is not UNSET:
            field_dict["layout"] = layout
        if level is not UNSET:
            field_dict["level"] = level
        if sequence is not UNSET:
            field_dict["sequence"] = sequence
        if type_ is not UNSET:
            field_dict["type"] = type_
        if wiki_text is not UNSET:
            field_dict["wikiText"] = wiki_text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = d.pop("content", UNSET)

        external = d.pop("external", UNSET)

        heading_text = d.pop("headingText", UNSET)

        id = d.pop("id", UNSET)

        landscape = d.pop("landscape", UNSET)

        layout = d.pop("layout", UNSET)

        level = d.pop("level", UNSET)

        sequence = d.pop("sequence", UNSET)

        type_ = d.pop("type", UNSET)

        wiki_text = d.pop("wikiText", UNSET)

        document_parts_list_get_response_data_item_attributes_obj = cls(
            content=content,
            external=external,
            heading_text=heading_text,
            id=id,
            landscape=landscape,
            layout=layout,
            level=level,
            sequence=sequence,
            type_=type_,
            wiki_text=wiki_text,
        )

        document_parts_list_get_response_data_item_attributes_obj.additional_properties = d
        return document_parts_list_get_response_data_item_attributes_obj

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

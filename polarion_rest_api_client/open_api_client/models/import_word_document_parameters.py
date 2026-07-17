# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImportWordDocumentParameters")


@_attrs_define
class ImportWordDocumentParameters:
    """Parameters for Word document import

    Example:
        {'configurationId': 'Default.xml', 'documentName': 'REQ-001', 'documentType': 'generic', 'title': 'System
            Requirements'}

    Attributes:
        document_name (str): Unique document name/ID for the imported document. Example: REQ-001.
        document_type (str): Document type for the imported document (e.g., 'generic'). Example: generic.
        title (str): Title for the imported document. Example: System Requirements.
        configuration_id (str | Unset): Optional configuration ID referencing a preexisting import configuration
            template. If not provided, default import behavior will be used. Example: Default.xml.
    """

    document_name: str
    document_type: str
    title: str
    configuration_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        document_name = self.document_name

        document_type = self.document_type

        title = self.title

        configuration_id = self.configuration_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "documentName": document_name,
                "documentType": document_type,
                "title": title,
            }
        )
        if configuration_id is not UNSET:
            field_dict["configurationId"] = configuration_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        document_name = d.pop("documentName")

        document_type = d.pop("documentType")

        title = d.pop("title")

        configuration_id = d.pop("configurationId", UNSET)

        import_word_document_parameters_obj = cls(
            document_name=document_name,
            document_type=document_type,
            title=title,
            configuration_id=configuration_id,
        )

        import_word_document_parameters_obj.additional_properties = d
        return import_word_document_parameters_obj

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

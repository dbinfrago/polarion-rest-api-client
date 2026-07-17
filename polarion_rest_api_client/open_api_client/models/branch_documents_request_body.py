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

if TYPE_CHECKING:
    from ..models.branch_documents_request_body_document_configurations_item import (
        BranchDocumentsRequestBodyDocumentConfigurationsItem,
    )


T = TypeVar("T", bound="BranchDocumentsRequestBody")


@_attrs_define
class BranchDocumentsRequestBody:
    """
    Attributes:
        document_configurations (list[BranchDocumentsRequestBodyDocumentConfigurationsItem]):
    """

    document_configurations: list[
        BranchDocumentsRequestBodyDocumentConfigurationsItem
    ]
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        document_configurations = []
        for document_configurations_item_data in self.document_configurations:
            document_configurations_item = (
                document_configurations_item_data.to_dict()
            )
            document_configurations.append(document_configurations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "documentConfigurations": document_configurations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.branch_documents_request_body_document_configurations_item import (
            BranchDocumentsRequestBodyDocumentConfigurationsItem,
        )

        d = dict(src_dict)
        document_configurations = []
        _document_configurations = d.pop("documentConfigurations")
        for document_configurations_item_data in _document_configurations:
            document_configurations_item = (
                BranchDocumentsRequestBodyDocumentConfigurationsItem.from_dict(
                    document_configurations_item_data
                )
            )

            document_configurations.append(document_configurations_item)

        branch_documents_request_body_obj = cls(
            document_configurations=document_configurations,
        )

        branch_documents_request_body_obj.additional_properties = d
        return branch_documents_request_body_obj

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

# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import json
from collections.abc import Mapping
from io import BytesIO
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import File

if TYPE_CHECKING:
    from ..models.import_word_document_parameters import (
        ImportWordDocumentParameters,
    )


T = TypeVar("T", bound="ImportWordDocumentRequestBody")


@_attrs_define
class ImportWordDocumentRequestBody:
    """Request body for importing a Word document

    Attributes:
        file (File): Word document file (.docx) to import.
        parameters (ImportWordDocumentParameters): Parameters for Word document import Example: {'configurationId':
            'Default.xml', 'documentName': 'REQ-001', 'documentType': 'generic', 'title': 'System Requirements'}.
    """

    file: File
    parameters: ImportWordDocumentParameters
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        file = self.file.to_tuple()

        parameters = self.parameters.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
                "parameters": parameters,
            }
        )

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("file", self.file.to_tuple()))

        files.append(
            (
                "parameters",
                (
                    None,
                    json.dumps(self.parameters.to_dict()).encode(),
                    "text/plain",
                ),
            )
        )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_word_document_parameters import (
            ImportWordDocumentParameters,
        )

        d = dict(src_dict)
        file = File(payload=BytesIO(d.pop("file")))

        parameters = ImportWordDocumentParameters.from_dict(
            d.pop("parameters")
        )

        import_word_document_request_body_obj = cls(
            file=file,
            parameters=parameters,
        )

        import_word_document_request_body_obj.additional_properties = d
        return import_word_document_request_body_obj

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

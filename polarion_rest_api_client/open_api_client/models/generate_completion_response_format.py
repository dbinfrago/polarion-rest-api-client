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

from ..models.generate_completion_response_format_type import (
    GenerateCompletionResponseFormatType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.generate_completion_response_format_schema import (
        GenerateCompletionResponseFormatSchema,
    )


T = TypeVar("T", bound="GenerateCompletionResponseFormat")


@_attrs_define
class GenerateCompletionResponseFormat:
    """Response format for LLM completion generation.

    Attributes:
        type_ (GenerateCompletionResponseFormatType): Type of the response format. Defaults to 'text'. Example:
            jsonSchema.
        schema (GenerateCompletionResponseFormatSchema | Unset): The JSON schema to use when type is 'jsonSchema'.
            Example: {'properties': {'result': {'type': 'string'}}, 'type': 'object'}.
    """

    type_: GenerateCompletionResponseFormatType
    schema: GenerateCompletionResponseFormatSchema | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        schema: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schema, Unset):
            schema = self.schema.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if schema is not UNSET:
            field_dict["schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.generate_completion_response_format_schema import (
            GenerateCompletionResponseFormatSchema,
        )

        d = dict(src_dict)
        type_ = GenerateCompletionResponseFormatType(d.pop("type"))

        _schema = d.pop("schema", UNSET)
        schema: GenerateCompletionResponseFormatSchema | Unset
        if isinstance(_schema, Unset):
            schema = UNSET
        else:
            schema = GenerateCompletionResponseFormatSchema.from_dict(_schema)

        generate_completion_response_format_obj = cls(
            type_=type_,
            schema=schema,
        )

        generate_completion_response_format_obj.additional_properties = d
        return generate_completion_response_format_obj

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

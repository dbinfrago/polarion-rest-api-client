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
    from ..models.generate_completion_message import GenerateCompletionMessage


T = TypeVar("T", bound="GenerateCompletionResult")


@_attrs_define
class GenerateCompletionResult:
    """The result of a completion generation request.

    Attributes:
        message (GenerateCompletionMessage): A message in the LLM completion generation request or response.
    """

    message: GenerateCompletionMessage
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        message = self.message.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.generate_completion_message import (
            GenerateCompletionMessage,
        )

        d = dict(src_dict)
        message = GenerateCompletionMessage.from_dict(d.pop("message"))

        generate_completion_result_obj = cls(
            message=message,
        )

        generate_completion_result_obj.additional_properties = d
        return generate_completion_result_obj

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

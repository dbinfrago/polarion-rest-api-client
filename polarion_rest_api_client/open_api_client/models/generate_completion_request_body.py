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
    from ..models.generate_completion_message import GenerateCompletionMessage
    from ..models.generate_completion_response_format import (
        GenerateCompletionResponseFormat,
    )


T = TypeVar("T", bound="GenerateCompletionRequestBody")


@_attrs_define
class GenerateCompletionRequestBody:
    """Generate completion parameters.

    Attributes:
        messages (list[GenerateCompletionMessage]): Prompt messages.
        model (str | Unset): Name of the LLM to use. If not specified, the default model will be used, if available.
        response_format (GenerateCompletionResponseFormat | Unset): Response format for LLM completion generation.
    """

    messages: list[GenerateCompletionMessage]
    model: str | Unset = UNSET
    response_format: GenerateCompletionResponseFormat | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        messages = []
        for messages_item_data in self.messages:
            messages_item = messages_item_data.to_dict()
            messages.append(messages_item)

        model = self.model

        response_format: dict[str, Any] | Unset = UNSET
        if not isinstance(self.response_format, Unset):
            response_format = self.response_format.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "messages": messages,
            }
        )
        if model is not UNSET:
            field_dict["model"] = model
        if response_format is not UNSET:
            field_dict["responseFormat"] = response_format

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.generate_completion_message import (
            GenerateCompletionMessage,
        )
        from ..models.generate_completion_response_format import (
            GenerateCompletionResponseFormat,
        )

        d = dict(src_dict)
        messages = []
        _messages = d.pop("messages")
        for messages_item_data in _messages:
            messages_item = GenerateCompletionMessage.from_dict(
                messages_item_data
            )

            messages.append(messages_item)

        model = d.pop("model", UNSET)

        _response_format = d.pop("responseFormat", UNSET)
        response_format: GenerateCompletionResponseFormat | Unset
        if isinstance(_response_format, Unset):
            response_format = UNSET
        else:
            response_format = GenerateCompletionResponseFormat.from_dict(
                _response_format
            )

        generate_completion_request_body_obj = cls(
            messages=messages,
            model=model,
            response_format=response_format,
        )

        generate_completion_request_body_obj.additional_properties = d
        return generate_completion_request_body_obj

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

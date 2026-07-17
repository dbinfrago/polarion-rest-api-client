# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from enum import Enum


class GenerateCompletionResponseFormatType(str, Enum):
    JSON = "json"
    JSONSCHEMA = "jsonSchema"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)

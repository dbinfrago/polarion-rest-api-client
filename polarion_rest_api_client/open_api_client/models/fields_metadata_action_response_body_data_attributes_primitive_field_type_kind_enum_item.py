# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from enum import Enum


class FieldsMetadataActionResponseBodyDataAttributesPrimitiveFieldTypeKindEnumItem(
    str, Enum
):
    BOOLEAN = "boolean"
    CURRENCY = "currency"
    DATE = "date"
    DATE_TIME = "date-time"
    FLOAT = "float"
    INTEGER = "integer"
    STRING = "string"
    TEXT = "text"
    TEXTHTML = "text/html"
    TIME = "time"

    def __str__(self) -> str:
        return str(self.value)

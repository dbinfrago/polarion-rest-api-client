# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from enum import Enum


class JobsListGetResponseDataItemAttributesStatusType(str, Enum):
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"
    OK = "OK"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)

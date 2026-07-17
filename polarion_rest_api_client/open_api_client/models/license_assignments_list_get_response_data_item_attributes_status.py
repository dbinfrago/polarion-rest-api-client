# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from enum import Enum


class LicenseAssignmentsListGetResponseDataItemAttributesStatus(str, Enum):
    EXPIRING = "EXPIRING"
    INACTIVE = "INACTIVE"
    LOGGED_IN = "LOGGED_IN"

    def __str__(self) -> str:
        return str(self.value)

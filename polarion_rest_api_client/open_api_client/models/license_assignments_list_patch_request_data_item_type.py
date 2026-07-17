# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from enum import Enum


class LicenseAssignmentsListPatchRequestDataItemType(str, Enum):
    LICENSE_ASSIGNMENTS = "license_assignments"

    def __str__(self) -> str:
        return str(self.value)

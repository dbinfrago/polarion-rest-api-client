# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from enum import Enum


class LicenseAssignmentsSingleGetResponseDataRelationshipsUserDataType(
    str, Enum
):
    USERS = "users"

    def __str__(self) -> str:
        return str(self.value)

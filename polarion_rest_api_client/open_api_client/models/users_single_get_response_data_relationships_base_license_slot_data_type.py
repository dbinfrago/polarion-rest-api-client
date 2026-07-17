# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from enum import Enum


class UsersSingleGetResponseDataRelationshipsBaseLicenseSlotDataType(
    str, Enum
):
    LICENSE_SLOTS = "license_slots"

    def __str__(self) -> str:
        return str(self.value)

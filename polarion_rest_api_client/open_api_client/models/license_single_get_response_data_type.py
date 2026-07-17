# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from enum import Enum


class LicenseSingleGetResponseDataType(str, Enum):
    LICENSE = "license"

    def __str__(self) -> str:
        return str(self.value)

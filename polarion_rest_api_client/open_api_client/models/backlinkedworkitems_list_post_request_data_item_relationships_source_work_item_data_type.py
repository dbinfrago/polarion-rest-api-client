# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from enum import Enum


class BacklinkedworkitemsListPostRequestDataItemRelationshipsSourceWorkItemDataType(
    str, Enum
):
    WORKITEMS = "workitems"

    def __str__(self) -> str:
        return str(self.value)

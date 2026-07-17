# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from enum import Enum


class CollectionsSinglePostResponseDataRelationshipsReusedFromDataType(
    str, Enum
):
    COLLECTIONS = "collections"

    def __str__(self) -> str:
        return str(self.value)

# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from enum import Enum


class DocumentsListGetResponseDataItemRelationshipsAttachmentsDataItemType(
    str, Enum
):
    DOCUMENT_ATTACHMENTS = "document_attachments"

    def __str__(self) -> str:
        return str(self.value)

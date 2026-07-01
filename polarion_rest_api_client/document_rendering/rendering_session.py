# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
"""Shared data structures for document rendering."""

from __future__ import annotations

import dataclasses
import typing as t

from polarion_rest_api_client import data_models as polarion_api

if t.TYPE_CHECKING:
    from polarion_rest_api_client.document_rendering import (
        text_work_item_provider,
    )

WorkItemLookupResult = tuple[
    str | None,
    polarion_api.WorkItem | None,
]
WorkItemLookup = t.Callable[[object], WorkItemLookupResult]


@dataclasses.dataclass
class RenderingSession:
    """A data class for parameters handled during a rendering session."""

    document_project_id: str | None
    headings: list[polarion_api.WorkItem] = dataclasses.field(
        default_factory=list
    )
    heading_ids: list[str] = dataclasses.field(default_factory=list)
    rendering_layouts: list[polarion_api.RenderingLayout] = dataclasses.field(
        default_factory=list
    )
    inserted_work_item_ids: list[tuple[str, str]] = dataclasses.field(
        default_factory=list
    )
    text_work_items: dict[str, polarion_api.WorkItem] = dataclasses.field(
        default_factory=dict
    )


@dataclasses.dataclass
class DocumentData:
    """A rendered Polarion document together with companion metadata."""

    document: polarion_api.Document
    headings: list[polarion_api.WorkItem]
    text_work_item_provider: text_work_item_provider.TextWorkItemProvider

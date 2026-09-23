# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
"""Public API for rendering Polarion documents with Jinja2."""

from polarion_rest_api_client.document_rendering.document_renderer import (
    DocumentRenderer,
    WorkItemLookupResult,
)
from polarion_rest_api_client.document_rendering.html_utils import (
    DEFAULT_GENERATED_ID_PREFIX,
    POLARION_WORK_ITEM_DOCUMENT,
    POLARION_WORK_ITEM_DOCUMENT_INTERNAL,
    POLARION_WORK_ITEM_DOCUMENT_PROJECT,
    POLARION_WORK_ITEM_URL,
    POLARION_WORK_ITEM_URL_PROJECT,
    RED_TEXT,
    TEXT_WORK_ITEM_ID_FIELD,
    TEXT_WORK_ITEM_TYPE,
    WI_ID_PREFIX,
    WI_ID_REGEX,
    WI_PROJECT_REGEX,
    WORK_ITEM_TAG,
    assign_generated_ids,
    camel_case_to_words,
    ensure_fragments,
    extract_headings,
    extract_work_items,
    generate_image_html,
    get_layout_index,
    strike_through,
    validate_root_element_ids,
)
from polarion_rest_api_client.document_rendering.rendering_session import (
    DocumentData,
    RenderingSession,
)
from polarion_rest_api_client.document_rendering.text_work_item_provider import (
    TextWorkItemProvider,
)

__all__ = [
    "DEFAULT_GENERATED_ID_PREFIX",
    "POLARION_WORK_ITEM_DOCUMENT",
    "POLARION_WORK_ITEM_DOCUMENT_INTERNAL",
    "POLARION_WORK_ITEM_DOCUMENT_PROJECT",
    "POLARION_WORK_ITEM_URL",
    "POLARION_WORK_ITEM_URL_PROJECT",
    "RED_TEXT",
    "TEXT_WORK_ITEM_ID_FIELD",
    "TEXT_WORK_ITEM_TYPE",
    "WI_ID_PREFIX",
    "WI_ID_REGEX",
    "WI_PROJECT_REGEX",
    "WORK_ITEM_TAG",
    "DocumentData",
    "DocumentRenderer",
    "RenderingSession",
    "TextWorkItemProvider",
    "WorkItemLookupResult",
    "assign_generated_ids",
    "camel_case_to_words",
    "ensure_fragments",
    "extract_headings",
    "extract_work_items",
    "generate_image_html",
    "get_layout_index",
    "strike_through",
    "validate_root_element_ids",
]

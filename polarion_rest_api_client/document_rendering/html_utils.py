# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
"""Functions for generic Polarion-specific HTML elements."""

from __future__ import annotations

import re

from lxml import html as lxmlhtml  # type: ignore[import-not-found]

from polarion_rest_api_client import data_models as polarion_api

WI_ID_PREFIX = "polarion_wiki macro name=module-workitem;params=id="
WI_PROJECT_PREFIX = "polarion_wiki macro name=module-workitem;.*project="
H_REGEX = re.compile("h[0-9]")
WI_ID_REGEX = re.compile(WI_ID_PREFIX + r"([A-Za-z0-9]*-[0-9]+)")
WI_PROJECT_REGEX = re.compile(WI_PROJECT_PREFIX + r"([A-Za-z0-9\-_]+)")

TEXT_WORK_ITEM_ID_FIELD = "__C2P__id"
TEXT_WORK_ITEM_TYPE = "text"
POLARION_WORK_ITEM_URL = (
    '<span class="polarion-rte-link" data-type="workItem" '
    'id="fake" data-item-id="{pid}" data-option-id="long"></span>'
)
POLARION_WORK_ITEM_URL_PROJECT = (
    '<span class="polarion-rte-link" data-type="workItem" '
    'id="fake" data-scope="{project}" data-item-id="{pid}" '
    'data-option-id="long"></span>'
)
POLARION_WORK_ITEM_DOCUMENT = (
    '<div id="polarion_wiki macro name=module-workitem;'
    'params=id={pid}|layout={lid}|{custom_info}external=true"></div>'
)
POLARION_WORK_ITEM_DOCUMENT_PROJECT = (
    '<div id="polarion_wiki macro name=module-workitem;'
    "params=id={pid}|layout={lid}|{custom_info}external=true"
    '|project={project}"></div>'
)
POLARION_CAPTION = (
    '<p class="polarion-rte-caption-paragraph">\n  '
    '{label} <span data-sequence="{label}" '
    'class="polarion-rte-caption">#</span> {caption}\n</p>'
)
RED_TEXT = '<p style="color:red">{text}</p>'
WORK_ITEM_TAG = "workitem"


def strike_through(string: str) -> str:
    """Return a striked-through HTML span from the given string."""
    return f'<span style="text-decoration: line-through;">{string}</span>'


def generate_image_html(
    title: str,
    attachment_id: str,
    max_width: int,
    css_class: str,
    caption: tuple[str, str] | None = None,
) -> str:
    """Generate Polarion HTML for an attached image."""
    description = (
        f'<span><img title="{title}" class="{css_class}" '
        f'src="workitemimg:{attachment_id}" '
        f'style="max-width: {max_width}px;"/></span>'
    )
    if caption:
        description += POLARION_CAPTION.format(
            label=caption[0], caption=caption[1]
        )
    return description


def camel_case_to_words(camel_case_str: str) -> str:
    """Split camel or dromedary case and return a spaced string."""
    match = re.match(r"^(.*?)(_?[A-Za-z0-9]+)$", camel_case_str)
    if not match:
        return camel_case_str
    prefix, camel_case_part = match.groups()
    words = re.findall(r"[A-Z]?[a-z]+|[A-Z]+(?=[A-Z]|$)", camel_case_part)
    formatted_words = " ".join(word.capitalize() for word in words)
    if prefix := prefix.strip("_"):
        formatted_words += f" ({prefix})"
    return formatted_words


def ensure_fragments(
    html_content: str | list[lxmlhtml.HtmlElement | str],
) -> list[lxmlhtml.HtmlElement | str]:
    """Convert string to html elements."""
    if isinstance(html_content, str):
        return lxmlhtml.fragments_fromstring(html_content)
    return html_content


def extract_headings(
    html_content: str | list[lxmlhtml.HtmlElement | str],
) -> list[str]:
    """Return work item IDs for headings."""
    return extract_work_items(html_content, H_REGEX)


def extract_work_items(
    html_content: str | list[lxmlhtml.HtmlElement | str],
    tag_regex: re.Pattern[str] | None = None,
) -> list[str]:
    """Return work item IDs from content."""
    work_item_ids: list[str] = []
    html_fragments = ensure_fragments(html_content)
    for element in html_fragments:
        if not isinstance(element, lxmlhtml.HtmlElement):
            continue
        tag_name = element.tag
        if not isinstance(tag_name, str):
            continue
        if (tag_regex is not None and tag_regex.fullmatch(tag_name)) or (
            tag_regex is None and tag_name == "div"
        ):
            elmid = element.get("id")
            if elmid is not None and (matches := WI_ID_REGEX.match(elmid)):
                work_item_ids.append(matches.group(1))
    return work_item_ids


def get_layout_index(
    default_layouter: str,
    rendering_layouts: list[polarion_api.RenderingLayout],
    work_item_type: str,
) -> int:
    """Return the index of layout for work item."""
    layout_index = 0
    for layout in rendering_layouts:
        if layout.type == work_item_type:
            return layout_index
        layout_index += 1
    if layout_index >= len(rendering_layouts):
        rendering_layouts.append(
            polarion_api.RenderingLayout(
                type=work_item_type,
                layouter=default_layouter,
                label=camel_case_to_words(work_item_type),
            )
        )
    return layout_index


def remove_table_ids(
    html_content: str | list[lxmlhtml.HtmlElement | str],
) -> list[lxmlhtml.HtmlElement | str]:
    """Remove the ID field from all tables.

    This works around a Polarion limitation where duplicate table IDs in
    document HTML are rejected by the REST API.
    """
    html_fragments = ensure_fragments(html_content)
    for element in html_fragments:
        if not isinstance(element, lxmlhtml.HtmlElement):
            continue
        if element.tag == "table":
            element.attrib.pop("id", None)
    return html_fragments

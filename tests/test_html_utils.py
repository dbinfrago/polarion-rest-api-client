# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from lxml import html as lxmlhtml

from polarion_rest_api_client import data_models as polarion_api
from polarion_rest_api_client.document_rendering import html_utils


def test_strike_through_wraps_text():
    rendered = html_utils.strike_through("removed")
    assert rendered == (
        '<span style="text-decoration: line-through;">removed</span>'
    )


def test_generate_image_html_with_caption():
    rendered = html_utils.generate_image_html(
        title="Architecture",
        attachment_id="arch.svg",
        max_width=640,
        css_class="diagram",
        caption=("Figure", "Logical architecture"),
    )

    fragments = lxmlhtml.fragments_fromstring(rendered)
    assert fragments[0].tag == "span"
    assert fragments[0][0].tag == "img"
    assert fragments[0][0].attrib["src"] == "workitemimg:arch.svg"
    assert fragments[1].tag == "p"
    assert "Logical architecture" in fragments[1].text_content()


def test_extract_headings_and_work_items():
    rendered = "".join(
        [
            '<h1 id="polarion_wiki macro name=module-workitem;params=id=REQ-1"></h1>',
            '<div id="polarion_wiki macro name=module-workitem;params=id=REQ-2"></div>',
        ]
    )

    assert html_utils.extract_headings(rendered) == ["REQ-1"]
    assert html_utils.extract_work_items(rendered) == ["REQ-2"]


def test_get_layout_index_returns_existing_layout():
    layouts = [
        polarion_api.RenderingLayout(type="requirement", layouter="section")
    ]

    idx = html_utils.get_layout_index("section", layouts, "requirement")

    assert idx == 0
    assert len(layouts) == 1


def test_get_layout_index_appends_layout_if_missing():
    layouts: list[polarion_api.RenderingLayout] = []

    idx = html_utils.get_layout_index("section", layouts, "systemFunction")

    assert idx == 0
    assert len(layouts) == 1
    assert layouts[0].type == "systemFunction"
    assert layouts[0].label == "System Function"


def test_remove_table_ids_only_changes_tables():
    fragments = html_utils.remove_table_ids(
        '<table id="a"><tr><td>v</td></tr></table><div id="keep"></div>'
    )

    table = fragments[0]
    div = fragments[1]
    assert not isinstance(table, str)
    assert not isinstance(div, str)
    assert table.tag == "table"
    assert "id" not in table.attrib
    assert div.attrib["id"] == "keep"

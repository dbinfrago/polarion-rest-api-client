# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from lxml import html as lxmlhtml

from polarion_rest_api_client import data_models
from polarion_rest_api_client.document_rendering import html_utils


def test_strike_through_wraps_text():
    rendered = html_utils.strike_through("removed <danger>")
    assert rendered == (
        '<span style="text-decoration: line-through;">'
        "removed &lt;danger&gt;"
        "</span>"
    )


def test_generate_image_html_with_caption():
    rendered = html_utils.generate_image_html(
        title='Architecture "v2"',
        attachment_id="arch&.svg",
        max_width=640,
        css_class="diagram main",
        caption=("Figure <A>", "Logical architecture & dependencies"),
    )

    fragments = lxmlhtml.fragments_fromstring(rendered)
    assert fragments[0].tag == "span"
    assert fragments[0][0].tag == "img"
    assert fragments[0][0].attrib["title"] == 'Architecture "v2"'
    assert fragments[0][0].attrib["src"] == "workitemimg:arch&.svg"
    assert fragments[1].tag == "p"
    caption_text = "".join(fragments[1].itertext())
    assert "Figure <A>" in caption_text
    assert "Logical architecture & dependencies" in caption_text


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
        data_models.RenderingLayout(type="requirement", layouter="section")
    ]

    idx = html_utils.get_layout_index("section", layouts, "requirement")

    assert idx == 0
    assert len(layouts) == 1


def test_get_layout_index_appends_layout_if_missing():
    layouts: list[data_models.RenderingLayout] = []

    idx = html_utils.get_layout_index("section", layouts, "systemFunction")

    assert idx == 0
    assert len(layouts) == 1
    assert layouts[0].type == "systemFunction"
    assert layouts[0].label == "System Function"


def test_assign_generated_ids_assigns_ids_recursively():
    fragments, next_uid = html_utils.assign_generated_ids(
        '<table id="table_8"><tr><td>v</td></tr></table>'
        "<h2>New heading</h2>"
        '<div id="polarion_wiki macro name=module-workitem;params=id=REQ-1">'
        "</div>"
    )

    table = fragments[0]
    heading = fragments[1]
    work_item = fragments[2]
    assert not isinstance(table, str)
    assert not isinstance(heading, str)
    assert not isinstance(work_item, str)
    assert table.attrib["id"] == "rest-api-1"
    assert table[0].attrib["id"] == "rest-api-2"
    assert table[0][0].attrib["id"] == "rest-api-3"
    assert work_item.attrib["id"] == (
        "polarion_wiki macro name=module-workitem;params=id=REQ-1"
    )
    assert heading.get("id") is None
    assert next_uid == 4


def test_replace_uid_parameters_only_replaces_exact_uid_parameters():
    fragments, next_uid = html_utils.replace_uid_parameters(
        '<table id="polarion_wiki macro name=table;params=uid=8"></table>'
        '<div id="polarion_wiki macro name=table;params=noPageBreak=yes|uid=8">'
        "</div>"
        '<p id="uid-like=8"></p>'
    )

    assert fragments[0].get("id") == (
        "polarion_wiki macro name=table;params=uid=1"
    )
    assert fragments[1].get("id") == (
        "polarion_wiki macro name=table;params=noPageBreak=yes|uid=2"
    )
    assert fragments[2].get("id") == "uid-like=8"
    assert next_uid == 3


def test_replace_uid_parameters_excludes_headings():
    fragments, next_uid = html_utils.replace_uid_parameters(
        '<h2 id="polarion_wiki macro name=table;params=uid=8"></h2>'
        '<table id="polarion_wiki macro name=table;params=uid=8"></table>'
    )

    assert fragments[0].get("id") == (
        "polarion_wiki macro name=table;params=uid=8"
    )
    assert fragments[1].get("id") == (
        "polarion_wiki macro name=table;params=uid=1"
    )
    assert next_uid == 2


def test_validate_root_element_ids_accepts_unique_ids():
    html_utils.validate_root_element_ids(
        '<p id="one"><span></span></p><div id="two"></div>'
    )


def test_validate_root_element_ids_warns_for_missing_id(caplog):
    with caplog.at_level("WARNING"):
        is_valid = html_utils.validate_root_element_ids(
            '<p id="one"></p><div></div>'
        )

    assert not is_valid
    assert "missing an ID" in caplog.text


def test_validate_root_element_ids_warns_for_duplicate_id(caplog):
    with caplog.at_level("WARNING"):
        is_valid = html_utils.validate_root_element_ids(
            '<p id="same"></p><div id="same"></div>'
        )

    assert not is_valid
    assert "occurs more than once" in caplog.text

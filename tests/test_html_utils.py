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
        '<table><tr><td>v</td></tr></table><div id="keep"></div>'
    )

    table = fragments[0]
    div = fragments[1]
    assert not isinstance(table, str)
    assert not isinstance(div, str)
    assert table.attrib["id"] == "rest-api:uid=1"
    assert table[0].attrib["id"] == "rest-api:uid=2"
    assert table[0][0].attrib["id"] == "rest-api:uid=3"
    assert div.attrib["id"] == "keep"
    assert next_uid == 4


def test_assign_generated_ids_skips_comments():
    fragments, next_uid = html_utils.assign_generated_ids(
        "<!-- root --><p><!-- nested --><span></span></p>"
    )

    comment, paragraph = fragments
    assert isinstance(comment, lxmlhtml.HtmlComment)
    assert not isinstance(paragraph, str)
    assert comment.get("id") is None
    assert paragraph.attrib["id"] == "rest-api:uid=1"
    assert isinstance(paragraph[0], lxmlhtml.HtmlComment)
    assert paragraph[1].attrib["id"] == "rest-api:uid=2"
    assert next_uid == 3


def test_assign_generated_ids_leaves_headings_without_id():
    fragments, next_uid = html_utils.assign_generated_ids(
        '<h1>Title</h1><p></p><h2 id="polarion_wiki macro name=module-'
        'workitem;params=id=H-1"></h2><h3>Sub</h3>'
    )

    h1, paragraph, h2, h3 = fragments
    assert not isinstance(h1, str)
    assert not isinstance(paragraph, str)
    assert not isinstance(h2, str)
    assert not isinstance(h3, str)
    assert h1.get("id") is None
    assert paragraph.attrib["id"] == "rest-api:uid=1"
    assert h2.attrib["id"].endswith("params=id=H-1")
    assert h3.get("id") is None
    assert next_uid == 2


def test_validate_root_element_ids_accepts_headings_without_id(caplog):
    with caplog.at_level("WARNING"):
        is_valid = html_utils.validate_root_element_ids(
            '<h1>Title</h1><p id="one"></p><h2>Sub</h2>'
        )

    assert is_valid
    assert not caplog.text


def test_validate_root_element_ids_ignores_comments(caplog):
    with caplog.at_level("WARNING"):
        is_valid = html_utils.validate_root_element_ids(
            '<!-- root --><p id="one"></p><!-- other -->'
        )

    assert is_valid
    assert not caplog.text


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

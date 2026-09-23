# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import logging
import textwrap

from lxml import html as lxmlhtml

import polarion_rest_api_client as polarion_api
from polarion_rest_api_client import document_rendering


def test_render_document_with_tuple_work_item(tmp_path):
    template_dir = tmp_path / "templates"
    template_dir.mkdir()
    (template_dir / "doc.j2").write_text(
        textwrap.dedent(
            """\
            {{ heading(1, "Main Heading", session) }}
            {{ insert_work_item(item, session) }}
            <p>{{ item | link_work_item }}</p>
            """
        ),
        encoding="utf-8",
    )

    renderer = document_rendering.DocumentRenderer(default_project_id="PRJ")
    item = ("PRJ", polarion_api.WorkItem(id="REQ-1", type="requirement"))

    rendered = renderer.render_document(
        template_dir,
        "doc.j2",
        "_default",
        "DOC-1",
        document_title="My Doc",
        item=item,
    )

    content = lxmlhtml.fragments_fromstring(
        rendered.document.home_page_content.value
    )

    assert rendered.document.title == "My Doc"
    assert len(rendered.document.rendering_layouts) == 1
    assert rendered.document.rendering_layouts[0].type == "requirement"
    assert rendered.document.rendering_layouts[0].layouter.value == "section"
    assert content[0].tag == "h1"
    assert content[0].text == "Main Heading"
    assert content[1].tag == "div"
    assert content[1].get("id") == (
        "polarion_wiki macro name=module-workitem;"
        "params=id=REQ-1|layout=0|external=true"
    )
    assert content[2][0].attrib["data-scope"] == "PRJ"


def test_render_document_with_work_item_id_lookup(tmp_path):
    template_dir = tmp_path / "templates"
    template_dir.mkdir()
    (template_dir / "doc.j2").write_text(
        "{{ insert_work_item(item_id, session) }}",
        encoding="utf-8",
    )

    renderer = document_rendering.DocumentRenderer(
        default_project_id="PRJ",
        work_item_repository={
            ("PRJ", "REQ-2"): polarion_api.WorkItem(
                id="REQ-2", type="requirement"
            )
        },
    )

    rendered = renderer.render_document(
        template_dir,
        "doc.j2",
        "_default",
        "DOC-LOOKUP",
        item_id="REQ-2",
    )

    content = lxmlhtml.fragments_fromstring(
        rendered.document.home_page_content.value
    )
    assert content[0].tag == "div"
    assert content[0].get("id") == (
        "polarion_wiki macro name=module-workitem;"
        "params=id=REQ-2|layout=0|external=true"
    )


def test_render_document_marks_known_document_work_items_internal(tmp_path):
    template_dir = tmp_path / "templates"
    template_dir.mkdir()
    (template_dir / "doc.j2").write_text(
        "{{ insert_work_item(item, session) }}",
        encoding="utf-8",
    )

    renderer = document_rendering.DocumentRenderer(
        default_project_id="PRJ",
        document_work_item_ids={"REQ-1"},
        default_layouter="paragraph",
    )
    item = ("PRJ", polarion_api.WorkItem(id="REQ-1", type="requirement"))

    rendered = renderer.render_document(
        template_dir,
        "doc.j2",
        "_default",
        "DOC-INTERNAL",
        item=item,
    )

    content = lxmlhtml.fragments_fromstring(
        rendered.document.home_page_content.value
    )
    assert content[0].get("id") == (
        "polarion_wiki macro name=module-workitem;params=id=REQ-1|layout=0"
    )
    assert rendered.document.rendering_layouts[0].layouter.value == "paragraph"


def test_render_document_keeps_unknown_document_work_items_external(tmp_path):
    template_dir = tmp_path / "templates"
    template_dir.mkdir()
    (template_dir / "doc.j2").write_text(
        "{{ insert_work_item(item, session) }}",
        encoding="utf-8",
    )

    renderer = document_rendering.DocumentRenderer(
        default_project_id="PRJ",
        document_work_item_ids={"REQ-KNOWN"},
    )
    item = ("PRJ", polarion_api.WorkItem(id="REQ-UNKNOWN", type="requirement"))

    rendered = renderer.render_document(
        template_dir,
        "doc.j2",
        "_default",
        "DOC-EXTERNAL",
        item=item,
    )

    content = lxmlhtml.fragments_fromstring(
        rendered.document.home_page_content.value
    )
    assert content[0].get("id") == (
        "polarion_wiki macro name=module-workitem;"
        "params=id=REQ-UNKNOWN|layout=0|external=true"
    )


def test_render_document_escapes_heading_text(tmp_path):
    template_dir = tmp_path / "templates"
    template_dir.mkdir()
    (template_dir / "doc.j2").write_text(
        "{{ heading(1, 'Main <Heading> & \"Title\"', session) }}",
        encoding="utf-8",
    )

    renderer = document_rendering.DocumentRenderer(default_project_id="PRJ")
    rendered = renderer.render_document(
        template_dir,
        "doc.j2",
        "_default",
        "DOC-ESCAPE",
    )

    assert rendered.document.home_page_content is not None
    assert rendered.document.home_page_content.value is not None
    assert (
        rendered.document.home_page_content.value.strip()
        == '<h1 id="rest-api:uid=1">'
        'Main &lt;Heading&gt; &amp; "Title"</h1>'
    )


def test_render_document_falls_back_to_callback_lookup(tmp_path):
    template_dir = tmp_path / "templates"
    template_dir.mkdir()
    (template_dir / "doc.j2").write_text(
        "{{ insert_work_item(custom_obj, session) }}",
        encoding="utf-8",
    )

    def lookup(obj: object):
        if obj == {"source": "custom"}:
            return (
                "PRJ",
                polarion_api.WorkItem(id="REQ-3", type="requirement"),
            )
        return None, None

    renderer = document_rendering.DocumentRenderer(
        default_project_id="PRJ",
        work_item_lookup=lookup,
    )

    rendered = renderer.render_document(
        template_dir,
        "doc.j2",
        "_default",
        "DOC-CALLBACK",
        custom_obj={"source": "custom"},
    )

    content = lxmlhtml.fragments_fromstring(
        rendered.document.home_page_content.value
    )
    assert content[0].tag == "div"
    assert content[0].get("id") == (
        "polarion_wiki macro name=module-workitem;"
        "params=id=REQ-3|layout=0|external=true"
    )


def test_render_document_logs_info_for_missing_repository_item(
    tmp_path, caplog
):
    template_dir = tmp_path / "templates"
    template_dir.mkdir()
    (template_dir / "doc.j2").write_text(
        "{{ insert_work_item(item_id, session) }}",
        encoding="utf-8",
    )

    renderer = document_rendering.DocumentRenderer(default_project_id="PRJ")

    with caplog.at_level(logging.INFO):
        rendered = renderer.render_document(
            template_dir,
            "doc.j2",
            "_default",
            "DOC-MISSING",
            item_id="REQ-404",
        )

    assert (
        "WorkItem PRJ/REQ-404 was not found in the renderer lookup repository."
        in caplog.text
    )
    assert rendered.document.home_page_content is not None
    assert (
        "Error inserting work item"
        in rendered.document.home_page_content.value
    )


def test_render_document_generates_text_work_items(tmp_path):
    template_dir = tmp_path / "templates"
    template_dir.mkdir()
    (template_dir / "doc.j2").write_text(
        '<workitem id="txt-1"><p>Hello</p></workitem>',
        encoding="utf-8",
    )

    renderer = document_rendering.DocumentRenderer(default_project_id="PRJ")

    rendered = renderer.render_document(
        template_dir,
        "doc.j2",
        "_default",
        "DOC-2",
    )

    work_item = rendered.text_work_item_provider.new_text_work_items["txt-1"]
    assert work_item.type == "text"
    assert (
        work_item.additional_attributes[
            document_rendering.TEXT_WORK_ITEM_ID_FIELD
        ]
        == "txt-1"
    )
    assert work_item.description is not None
    assert work_item.description.value == "<p>Hello</p>"


def test_update_mixed_authority_document_reuses_heading_ids(tmp_path):
    template_dir = tmp_path / "templates"
    template_dir.mkdir()
    (template_dir / "section.j2").write_text(
        '{{ heading(2, "Updated Heading", session) }}<p>{{ message }}</p>',
        encoding="utf-8",
    )

    old_document = polarion_api.Document(
        module_folder="_default",
        module_name="DOC-3",
        home_page_content=polarion_api.TextContent(
            type="text/html",
            value=textwrap.dedent(
                """\
                <p>Before</p>
                <div class="polarion-dle-wiki-block">
                  <div class="polarion-dle-wiki-block-source">&lt;div class=&quot;autoRenderAreaStart&quot; id=&quot;section1&quot;&gt;&lt;/div&gt;</div>
                </div>
                <h2 id="polarion_wiki macro name=module-workitem;params=id=REQ-9"></h2>
                <p>Old content</p>
                <div class="polarion-dle-wiki-block">
                  <div class="polarion-dle-wiki-block-source">&lt;div class=&quot;autoRenderAreaEnd&quot; id=&quot;section1&quot;&gt;&lt;/div&gt;</div>
                </div>
                <p>After</p>
                """
            ),
        ),
    )

    renderer = document_rendering.DocumentRenderer(default_project_id="PRJ")
    rendered = renderer.update_mixed_authority_document(
        old_document,
        template_dir,
        {"section1": "section.j2"},
        {"message": "New content"},
        {},
    )

    content = lxmlhtml.fragments_fromstring(
        rendered.document.home_page_content.value
    )

    assert content[0].text == "Before"
    assert content[2].tag == "h2"
    assert content[2].get("id") == (
        "polarion_wiki macro name=module-workitem;params=id=REQ-9"
    )
    assert content[3].text == "New content"
    assert content[-1].text == "After"
    assert len(rendered.headings) == 1
    assert rendered.headings[0].id == "REQ-9"
    assert rendered.headings[0].title == "Updated Heading"


def test_update_mixed_authority_document_assigns_ids_only_to_generated_content(
    tmp_path,
):
    template_dir = tmp_path / "templates"
    template_dir.mkdir()
    (template_dir / "section.j2").write_text(
        "<table><tr><td>{{ message }}</td></tr></table>",
        encoding="utf-8",
    )

    old_document = polarion_api.Document(
        module_folder="_default",
        module_name="DOC-4",
        home_page_content=polarion_api.TextContent(
            type="text/html",
            value=textwrap.dedent(
                """\
                <table id="preserved-table"><tr><td>Before</td></tr></table>
                <div class="polarion-dle-wiki-block">
                  <div class="polarion-dle-wiki-block-source">&lt;div class=&quot;autoRenderAreaStart&quot; id=&quot;section1&quot;&gt;&lt;/div&gt;</div>
                </div>
                <p>Old content</p>
                <div class="polarion-dle-wiki-block">
                  <div class="polarion-dle-wiki-block-source">&lt;div class=&quot;autoRenderAreaEnd&quot; id=&quot;section1&quot;&gt;&lt;/div&gt;</div>
                </div>
                <table id="preserved-table-2"><tr><td>After</td></tr></table>
                """
            ),
        ),
    )

    renderer = document_rendering.DocumentRenderer(default_project_id="PRJ")
    rendered = renderer.update_mixed_authority_document(
        old_document,
        template_dir,
        {"section1": "section.j2"},
        {"message": "Generated"},
        {},
    )

    content = lxmlhtml.fragments_fromstring(
        rendered.document.home_page_content.value
    )
    generated_table = next(
        element
        for element in content
        if element.tag == "table"
        and element.get("id") != "preserved-table"
        and element.get("id") != "preserved-table-2"
    )

    assert content[0].get("id") == "preserved-table"
    assert content[-1].get("id") == "preserved-table-2"
    assert generated_table.get("id") == "rest-api:uid=1"
    assert generated_table[0].get("id") == "rest-api:uid=2"
    assert generated_table[0][0].get("id") == "rest-api:uid=3"


def test_update_mixed_authority_document_shares_id_counter_between_sections(
    tmp_path,
):
    template_dir = tmp_path / "templates"
    template_dir.mkdir()
    (template_dir / "section.j2").write_text(
        "<p>{{ message }}</p>",
        encoding="utf-8",
    )

    def marker(section: str, boundary: str) -> str:
        return (
            '<div class="polarion-dle-wiki-block">'
            '<div class="polarion-dle-wiki-block-source">'
            f"&lt;div class=&quot;autoRenderArea{boundary}&quot; "
            f"id=&quot;{section}&quot;&gt;&lt;/div&gt;"
            "</div></div>"
        )

    old_document = polarion_api.Document(
        module_folder="_default",
        module_name="DOC-5",
        home_page_content=polarion_api.TextContent(
            type="text/html",
            value=marker("section1", "Start")
            + marker("section1", "End")
            + marker("section2", "Start")
            + marker("section2", "End"),
        ),
    )

    renderer = document_rendering.DocumentRenderer(default_project_id="PRJ")
    rendered = renderer.update_mixed_authority_document(
        old_document,
        template_dir,
        {"section1": "section.j2", "section2": "section.j2"},
        {"message": "Generated"},
        {},
    )

    paragraphs = [
        element
        for element in lxmlhtml.fragments_fromstring(
            rendered.document.home_page_content.value
        )
        if element.tag == "p"
    ]
    assert [paragraph.get("id") for paragraph in paragraphs] == [
        "rest-api:uid=1",
        "rest-api:uid=2",
    ]

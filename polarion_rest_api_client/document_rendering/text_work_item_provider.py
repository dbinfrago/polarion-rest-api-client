# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
"""Provides a class to generate and insert text work items in documents."""

from lxml import html as lxmlhtml

from polarion_rest_api_client import data_models

from . import html_utils


class TextWorkItemProvider:
    """Class providing text work items, their generation and insertion."""

    def __init__(
        self,
        text_work_item_id_field: str = html_utils.TEXT_WORK_ITEM_ID_FIELD,
        text_work_item_type: str = html_utils.TEXT_WORK_ITEM_TYPE,
        existing_text_work_items: list[data_models.WorkItem] | None = None,
    ) -> None:
        """Initialize the text work item provider.

        Parameters
        ----------
        text_work_item_id_field
            The field name for custom IDs on text work items.
        text_work_item_type
            The type name for text work items.
        existing_text_work_items
            Existing text work items to reuse.
        """
        self.old_text_work_items: dict[str, data_models.WorkItem] = {}
        for work_item in existing_text_work_items or []:
            if text_id := work_item.additional_attributes.get(
                text_work_item_id_field
            ):
                if text_id in self.old_text_work_items:
                    raise ValueError(
                        f"Multiple text work items with "
                        f"{text_work_item_id_field} == {text_id}"
                    )
                self.old_text_work_items[text_id] = work_item

        self.text_work_item_id_field = text_work_item_id_field
        self.text_work_item_type = text_work_item_type
        self.new_text_work_items: dict[str, data_models.WorkItem] = {}

    def generate_text_work_items(
        self,
        content: list[lxmlhtml.HtmlElement | str],
        work_item_id_filter: list[str] | None = None,
    ) -> None:
        """Generate text work items from the provided html.

        Parameters
        ----------
        content
            HTML content to extract work items from.
        work_item_id_filter
            Only generate work items with these IDs.
        """
        content = html_utils.ensure_fragments(content)
        for element in content:
            if isinstance(element, str):
                continue
            if element.tag != html_utils.WORK_ITEM_TAG:
                continue

            if not (text_id := element.get("id")):
                raise ValueError("All work items must have an ID")

            if not (
                (work_item := self.old_text_work_items.get(text_id))
                and (
                    work_item_id_filter is None
                    or work_item.id in work_item_id_filter
                )
            ):
                work_item = data_models.WorkItem(
                    type=self.text_work_item_type,
                    title="",
                    status="open",
                    additional_attributes={
                        self.text_work_item_id_field: text_id
                    },
                )

            inner_content = "".join(
                [
                    (
                        lxmlhtml.tostring(child, encoding="unicode")
                        if isinstance(child, lxmlhtml.HtmlElement)
                        else child
                    )
                    for child in element.iterchildren()
                ]
            )
            if element.text:
                inner_content = element.text + inner_content

            work_item.description = data_models.HtmlContent(inner_content)
            self.new_text_work_items[text_id] = work_item

    def insert_text_work_items(
        self,
        document: data_models.Document,
    ) -> None:
        """Insert text work items into the given document.

        Parameters
        ----------
        document
            The document to insert work items into.
        """
        if not self.new_text_work_items:
            return

        assert document.home_page_content is not None
        assert document.rendering_layouts is not None
        layout_index = html_utils.get_layout_index(
            "paragraph", document.rendering_layouts, self.text_work_item_type
        )
        html_fragments = html_utils.ensure_fragments(
            document.home_page_content.value or ""
        )
        new_content: list[lxmlhtml.HtmlElement | str] = []
        last_match = -1
        for index, element in enumerate(html_fragments):
            if not isinstance(element, lxmlhtml.HtmlElement):
                continue

            if element.tag == html_utils.WORK_ITEM_TAG:
                new_content.extend(html_fragments[last_match + 1 : index])
                last_match = index
                if work_item := self.new_text_work_items.get(
                    element.get("id", "")
                ):
                    new_content.append(
                        lxmlhtml.fromstring(
                            html_utils.POLARION_WORK_ITEM_DOCUMENT.format(
                                pid=work_item.id,
                                lid=layout_index,
                                custom_info="",
                            )
                        )
                    )

        new_content += html_fragments[last_match + 1 :]
        document.home_page_content.value = "\n".join(
            lxmlhtml.tostring(element).decode("utf-8")
            for element in new_content
            if isinstance(element, lxmlhtml.HtmlElement)
        )

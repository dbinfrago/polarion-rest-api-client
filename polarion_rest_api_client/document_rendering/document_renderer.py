# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
"""A generic Jinja renderer for Polarion documents."""

from __future__ import annotations

import html
import logging
import pathlib
import typing as t
from collections.abc import Mapping

import jinja2
from lxml import html as lxmlhtml

from polarion_rest_api_client import data_models as polarion_api

from . import html_utils
from .rendering_session import (
    DocumentData,
    RenderingSession,
    WorkItemLookup,
    WorkItemLookupResult,
)
from .text_work_item_provider import TextWorkItemProvider

PROJ_WI_PAIR_LEN = 2

DEFAULT_AREA_START_CLS = "autoRenderAreaStart"
"""Default marker class for the wiki macro that starts a rendering area."""
DEFAULT_AREA_END_CLS = "autoRenderAreaEnd"
"""Default marker class for the wiki macro that ends a rendering area."""

logger = logging.getLogger(__name__)


class DocumentRenderer:
    """A generic renderer for Polarion documents.

    The renderer can resolve explicit ``(project_id, WorkItem)`` pairs and
    ``(project_id, work_item_id)`` or ``work_item_id`` references through an
    internal lookup repository.
    For project-specific object models, subclass it and override
    :meth:`resolve_work_item` and optionally :meth:`get_template_context`.
    Alternatively, pass a ``work_item_lookup`` callback to the constructor.
    """

    def __init__(
        self,
        default_project_id: str | None = None,
        *,
        work_item_lookup: WorkItemLookup | None = None,
        work_item_repository: (
            Mapping[tuple[str, str], polarion_api.WorkItem] | None
        ) = None,
        area_start_class: str = DEFAULT_AREA_START_CLS,
        area_end_class: str = DEFAULT_AREA_END_CLS,
        extra_template_context: dict[str, t.Any] | None = None,
    ) -> None:
        self.jinja_envs: dict[str, jinja2.Environment] = {}
        self.default_project_id = default_project_id
        self._work_item_lookup = work_item_lookup
        self._work_item_repository = dict(work_item_repository or {})
        self.area_start_class = area_start_class
        self.area_end_class = area_end_class
        self._extra_template_context = extra_template_context or {}

    def _get_jinja_env(
        self, template_folder: str | pathlib.Path
    ) -> jinja2.Environment:
        """Get or create a Jinja environment for a template folder."""
        template_folder = str(template_folder)
        if env := self.jinja_envs.get(template_folder):
            return env

        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(template_folder)
        )
        self.setup_env(env)
        self.jinja_envs[template_folder] = env
        return env

    def setup_env(self, env: jinja2.Environment) -> None:
        """Add globals and filters to the environment."""
        env.globals["insert_work_item"] = self._insert_work_item
        env.globals["heading"] = self._heading
        env.globals["work_item_field"] = self._work_item_field
        env.globals["generate_image_html"] = html_utils.generate_image_html
        env.filters["link_work_item"] = self._link_work_item

    def get_template_context(self) -> dict[str, t.Any]:
        """Return default template context values for each render."""
        return dict(self._extra_template_context)

    @t.overload
    def resolve_work_item(self, obj: object) -> WorkItemLookupResult: ...

    @t.overload
    def resolve_work_item(
        self, project_id: str, work_item_id: str
    ) -> WorkItemLookupResult: ...

    def resolve_work_item(
        self, obj: object, work_item_id: str | None = None
    ) -> WorkItemLookupResult:
        """Resolve a custom object into a Polarion work item.

        The default implementation supports lookups by ``(project_id,
        work_item_id)`` and by ``work_item_id`` with ``default_project_id``.
        For non-string objects, the default implementation delegates to the
        optional callback supplied at construction time.
        """
        if work_item_id is not None:
            if not isinstance(obj, str):
                logger.error(
                    "Invalid work item lookup input: project_id must be a string, got %r.",
                    obj,
                )
                return None, None
            return self._resolve_work_item_from_repository(obj, work_item_id)

        if isinstance(obj, str):
            if self.default_project_id is None:
                logger.error(
                    "Invalid work item lookup input: no default project configured for id %s.",
                    obj,
                )
                return None, None
            return self._resolve_work_item_from_repository(
                self.default_project_id, obj
            )

        if self._work_item_lookup is not None:
            return self._work_item_lookup(obj)
        logger.error("Invalid work item lookup input: %r", obj)
        return None, None

    def _resolve_work_item_from_repository(
        self, project_id: str, work_item_id: str
    ) -> WorkItemLookupResult:
        work_item = self._work_item_repository.get((project_id, work_item_id))
        if work_item is None:
            logger.info(
                "WorkItem %s/%s was not found in the renderer lookup repository.",
                project_id,
                work_item_id,
            )
            return project_id, None
        return project_id, work_item

    def _get_work_item(self, obj: object) -> WorkItemLookupResult:
        if isinstance(obj, tuple) and len(obj) == PROJ_WI_PAIR_LEN:
            proj_id, work_item = obj
            if isinstance(proj_id, str) and isinstance(
                work_item, polarion_api.WorkItem
            ):
                if work_item.id:
                    self._work_item_repository[(proj_id, work_item.id)] = (
                        work_item
                    )
                return proj_id, work_item
            if isinstance(proj_id, str) and isinstance(work_item, str):
                return self.resolve_work_item(proj_id, work_item)
            logger.error("Invalid work item tuple input: %r", obj)
            return None, None

        if isinstance(obj, str):
            return self.resolve_work_item(obj)

        if jinja2.is_undefined(obj) or obj is None:
            logger.error("Invalid work item input: %r", obj)
            return None, None

        return self.resolve_work_item(obj)

    def _insert_work_item(
        self, obj: object, session: RenderingSession, level: int | None = None
    ) -> str:
        proj_id, work_item = self._get_work_item(obj)

        if proj_id and work_item:
            assert work_item.id
            if (proj_id, work_item.id) in session.inserted_work_item_ids:
                logger.warning(
                    "WorkItem %s is already in the document."
                    "A link will be added instead of inserting it.",
                    work_item.id,
                )
                return f"<p>{self._link_work_item(obj)}</p>"

            assert work_item.type
            layout_index = html_utils.get_layout_index(
                "section",
                session.rendering_layouts,
                work_item.type,
            )

            custom_info = ""
            if level is not None:
                custom_info = f"level={level}|"

            session.inserted_work_item_ids.append((proj_id, work_item.id))
            if proj_id != session.document_project_id:
                return html_utils.POLARION_WORK_ITEM_DOCUMENT_PROJECT.format(
                    pid=work_item.id,
                    lid=layout_index,
                    custom_info=custom_info,
                    project=proj_id,
                )
            return html_utils.POLARION_WORK_ITEM_DOCUMENT.format(
                pid=work_item.id,
                lid=layout_index,
                custom_info=custom_info,
            )

        logger.warning("Error inserting work item for input: %r", obj)
        return html_utils.RED_TEXT.format(text="Error inserting work item.")

    def _link_work_item(self, obj: object) -> str:
        proj_id, work_item = self._get_work_item(obj)

        if work_item and proj_id:
            return html_utils.POLARION_WORK_ITEM_URL_PROJECT.format(
                pid=work_item.id,
                project=proj_id,
            )

        logger.warning("Error linking work item for input: %r", obj)
        return html_utils.RED_TEXT.format(text="Error linking work item.")

    def _heading(
        self, level: int, text: str, session: RenderingSession
    ) -> str:
        if session.heading_ids:
            hid = session.heading_ids.pop(0)
            session.headings.append(polarion_api.WorkItem(id=hid, title=text))
            return f'<h{level} id="{html_utils.WI_ID_PREFIX}{hid}"></h{level}>'
        return f"<h{level}>{text}</h{level}>"

    def _work_item_field(self, obj: object, field: str) -> t.Any:
        _, work_item = self._get_work_item(obj)
        if work_item is None:
            logger.error(
                "Error getting work item field '%s' for input: %r",
                field,
                obj,
            )
            return "No work item found."

        return getattr(
            work_item,
            field,
            f"Missing field {field} for work item {work_item.id}",
        )

    @t.overload
    def render_document(
        self,
        template_folder: str | pathlib.Path,
        template_name: str,
        polarion_folder: str,
        polarion_name: str,
        polarion_type: str | None = None,
        document_title: str | None = None,
        heading_numbering: bool = False,  # noqa: FBT002
        rendering_layouts: list[polarion_api.RenderingLayout] | None = None,
        *,
        text_work_item_provider: TextWorkItemProvider | None = None,
        document_project_id: str | None = None,
        **kwargs: t.Any,
    ) -> DocumentData:
        """Render a new Polarion document."""

    @t.overload
    def render_document(
        self,
        template_folder: str | pathlib.Path,
        template_name: str,
        *,
        document: polarion_api.Document,
        text_work_item_provider: TextWorkItemProvider | None = None,
        document_project_id: str | None = None,
        **kwargs: t.Any,
    ) -> DocumentData:
        """Update an existing Polarion document."""

    def render_document(
        self,
        template_folder: str | pathlib.Path,
        template_name: str,
        polarion_folder: str | None = None,
        polarion_name: str | None = None,
        polarion_type: str | None = None,
        document_title: str | None = None,
        heading_numbering: bool = False,  # noqa: FBT002
        rendering_layouts: list[polarion_api.RenderingLayout] | None = None,
        document: polarion_api.Document | None = None,
        text_work_item_provider: TextWorkItemProvider | None = None,
        document_project_id: str | None = None,
        **kwargs: t.Any,
    ) -> DocumentData:
        """Render a Polarion document."""
        text_work_item_provider = (
            text_work_item_provider or TextWorkItemProvider()
        )
        if document is not None:
            polarion_folder = document.module_folder
            polarion_name = document.module_name
            polarion_type = document.type

        if polarion_name is None or polarion_folder is None:
            raise AssertionError(
                "You either need to pass a folder and a name or a document"
                " with a module_folder and a module_name defined"
            )

        env = self._get_jinja_env(template_folder)
        template = env.get_template(template_name)

        session = RenderingSession(
            document_project_id=document_project_id or self.default_project_id
        )
        if document is not None:
            session.rendering_layouts = document.rendering_layouts or []
            if document.home_page_content and document.home_page_content.value:
                session.heading_ids = html_utils.extract_headings(
                    document.home_page_content.value
                )
        else:
            document = polarion_api.Document(
                title=document_title,
                module_folder=polarion_folder,
                module_name=polarion_name,
                type=polarion_type,
                outline_numbering=heading_numbering,
            )
            if rendering_layouts is not None:
                session.rendering_layouts = rendering_layouts

        rendering_result = template.render(
            **(self.get_template_context() | kwargs | {"session": session})
        )
        text_work_item_provider.generate_text_work_items(
            html_utils.ensure_fragments(rendering_result),
        )

        document.home_page_content = polarion_api.TextContent(
            "text/html",
            rendering_result,
        )
        document.rendering_layouts = session.rendering_layouts

        return DocumentData(
            document,
            session.headings,
            text_work_item_provider,
        )

    def update_mixed_authority_document(
        self,
        document: polarion_api.Document,
        template_folder: str | pathlib.Path,
        sections: dict[str, str],
        global_parameters: dict[str, t.Any],
        section_parameters: dict[str, dict[str, t.Any]],
        text_work_item_provider: TextWorkItemProvider | None = None,
        document_project_id: str | None = None,
    ) -> DocumentData:
        """Update a mixed-authority document."""
        document.type = None
        text_work_item_provider = (
            text_work_item_provider or TextWorkItemProvider()
        )
        assert document.home_page_content, (
            "In mixed authority the document must have content"
        )
        assert document.home_page_content.value, (
            "In mixed authority the document must have content"
        )
        html_elements = html_utils.ensure_fragments(
            document.home_page_content.value
        )

        session = RenderingSession(
            rendering_layouts=document.rendering_layouts or [],
            document_project_id=document_project_id or self.default_project_id,
        )
        section_areas = self._extract_section_areas(html_elements, session)
        env = self._get_jinja_env(template_folder)

        new_content: list[t.Any] = []
        last_section_end = 0

        for section_name, area in section_areas.items():
            if section_name not in sections:
                logger.warning(
                    "Found section %s in document, but it is not defined in the config",
                    section_name,
                )
                continue
            new_content += html_elements[last_section_end : area[0] + 1]
            last_section_end = area[1]
            current_content = html_elements[area[0] + 1 : area[1]]
            session.heading_ids = html_utils.extract_headings(current_content)
            template = env.get_template(sections[section_name])
            content = template.render(
                **(
                    self.get_template_context()
                    | global_parameters
                    | section_parameters.get(section_name, {})
                    | {"session": session}
                )
            )
            work_item_ids = html_utils.extract_work_items(current_content)
            html_fragments = html_utils.ensure_fragments(content)
            text_work_item_provider.generate_text_work_items(
                html_fragments,
                work_item_ids,
            )
            new_content += html_fragments

        new_content += html_elements[last_section_end:]
        new_content = html_utils.remove_table_ids(new_content)

        document.home_page_content = polarion_api.TextContent(
            "text/html",
            "\n".join(
                lxmlhtml.tostring(element).decode("utf-8")
                for element in new_content
                if not isinstance(element, str)
            ),
        )
        document.rendering_layouts = session.rendering_layouts

        return DocumentData(
            document,
            session.headings,
            text_work_item_provider,
        )

    def _extract_section_areas(
        self,
        html_elements: list[t.Any],
        session: RenderingSession,
    ) -> dict[str, tuple[int, int]]:
        section_areas: dict[str, tuple[int, int]] = {}
        current_area_id = None
        current_area_start = None
        for element_index, element in enumerate(html_elements):
            assert not isinstance(element, str)
            if (
                current_area_id is None
                and element.tag == "div"
                and (
                    wid_match := html_utils.WI_ID_REGEX.match(
                        element.get("id", "")
                    )
                )
            ):
                proj_id = (
                    session.document_project_id or self.default_project_id
                )
                if proj_match := html_utils.WI_PROJECT_REGEX.match(
                    element.get("id", "")
                ):
                    proj_id = proj_match.group(1)
                if proj_id is not None:
                    session.inserted_work_item_ids.append(
                        (proj_id, wid_match.group(1))
                    )
                continue

            if (
                element.tag != "div"
                or element.get("class") != "polarion-dle-wiki-block"
            ):
                continue
            for child in element.iterchildren():
                if child.get("class") == "polarion-dle-wiki-block-source":
                    text = html.unescape(child.text or "")
                    content = html_utils.ensure_fragments(text)
                    if (
                        content
                        and not isinstance(content[0], str)
                        and content[0].tag == "div"
                    ):
                        element_id = content[0].get("id")
                        if content[0].get("class") == self.area_start_class:
                            assert element_id is not None, (
                                "There was no id set to identify the area"
                            )
                            assert current_area_id is None, (
                                f"Started a new area {element_id} "
                                f"while being in area {current_area_id}"
                            )
                            current_area_id = element_id
                            current_area_start = element_index
                        elif content[0].get("class") == self.area_end_class:
                            assert element_id is not None, (
                                "There was no id set to identify the area"
                            )
                            assert current_area_id == element_id, (
                                f"Ended area {element_id} "
                                f"while being in area {current_area_id}"
                            )
                            assert current_area_start is not None
                            assert current_area_id is not None
                            section_areas[current_area_id] = (
                                current_area_start,
                                element_index,
                            )
                            current_area_id = None
                            current_area_start = None
        return section_areas

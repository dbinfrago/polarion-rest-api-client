# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
"""A client for a specific project, using the session of PolarionClient."""

import typing as t

from polarion_rest_api_client import data_models as dm
from polarion_rest_api_client.clients import base_classes as bc
from polarion_rest_api_client.open_api_client import models as api_models
from polarion_rest_api_client.open_api_client import types as oa_types
from polarion_rest_api_client.open_api_client.api.projects import (
    get_project,
    get_projects,
)

from . import documents, test_runs, work_items

HTTP_OK_CODE = 200

if t.TYPE_CHECKING:
    from polarion_rest_api_client import client as polarion_client


class ProjectClient(bc.BaseClient):
    """A client for a specific project."""

    def __init__(
        self,
        project_id: str,
        client: "polarion_client.PolarionClient",
        delete_status: str | None = None,
    ):
        super().__init__(project_id, client)

        self.work_items = work_items.WorkItems(
            project_id, client, delete_status
        )
        self.test_runs = test_runs.TestRuns(project_id, client)
        self.documents = documents.Documents(project_id, client)

    def exists(self) -> bool:
        """Return True, if the clients project exists."""
        response = get_project.sync_detailed(
            self._project_id, client=self._client.client
        )
        return response.status_code == HTTP_OK_CODE


class Projects(bc.MultiGetClient[dm.Project]):
    """A project-independent client to list projects.

    Not scoped to a single project; the ``project_id`` passed to the base
    class is unused (the ``get_projects`` endpoint has no project in its path).
    """

    def get_multi(  # type: ignore[override]
        self,
        query: str = "",
        *,
        page_size: int = 100,
        page_number: int = 1,
        fields: dict[str, str] | None = None,
    ) -> tuple[list[dm.Project], bool]:
        """Return the projects on a defined page matching the given query."""
        response = get_projects.sync_detailed(
            client=self._client.client,
            fields=self._build_sparse_fields(fields)
            if fields
            else oa_types.UNSET,
            query=query or oa_types.UNSET,
            pagesize=page_size,
            pagenumber=page_number,
        )
        self._raise_on_error(response)
        return self._parse_get_response(response.parsed)

    async def async_get_multi(  # type: ignore[override]
        self,
        query: str = "",
        *,
        page_size: int = 100,
        page_number: int = 1,
        fields: dict[str, str] | None = None,
    ) -> tuple[list[dm.Project], bool]:
        """Return the projects on a defined page matching the given query."""
        response = await get_projects.asyncio_detailed(
            client=self._client.client,
            fields=self._build_sparse_fields(fields)
            if fields
            else oa_types.UNSET,
            query=query or oa_types.UNSET,
            pagesize=page_size,
            pagenumber=page_number,
        )
        self._raise_on_error(response)
        return self._parse_get_response(response.parsed)

    def _parse_get_response(
        self, parsed: t.Any
    ) -> tuple[list[dm.Project], bool]:
        if not isinstance(
            parsed, api_models.ProjectsListGetResponse
        ) or isinstance(parsed.data, oa_types.Unset):
            return [], False
        projects_list = [
            self._generate_project(item)
            for item in parsed.data
            if not getattr(item.meta, "errors", []) and item.attributes
        ]
        next_page = isinstance(
            parsed.links, api_models.ProjectsListGetResponseLinks
        ) and bool(parsed.links.next_)
        return projects_list, next_page

    def _generate_project(self, data: t.Any) -> dm.Project:
        attributes = data.attributes
        description = None
        if attributes.description:
            description = dm.TextContent(
                type=(
                    str(attributes.description.type_)
                    if attributes.description.type_
                    else None
                ),
                value=attributes.description.value or None,
            )
        return dm.Project(
            id=data.id.split("/")[-1] if data.id else None,
            name=self.unset_to_none(attributes.name),
            active=self.unset_to_none(attributes.active),
            description=description,
            tracker_prefix=self.unset_to_none(attributes.tracker_prefix),
            additional_attributes=dict(attributes.additional_properties),
        )

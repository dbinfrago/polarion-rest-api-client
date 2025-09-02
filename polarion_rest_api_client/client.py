# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
"""The overall Polarion Client which handles the HTTP session, auth etc."""

from __future__ import annotations

import asyncio
import ssl
import typing as t

import truststore

import polarion_rest_api_client.open_api_client as oa_client
from polarion_rest_api_client import data_models as dm
from polarion_rest_api_client.clients import projects

WorkItemType = t.TypeVar("WorkItemType", bound=dm.WorkItem)


class DefaultFields:
    """A class to define default values for the fields parameter."""

    _workitems: str = "@basic"
    _linkedworkitems: str = "id,role,suspect"
    _workitem_attachments: str = "@basic"
    _documents: str = "@basic"
    _testrecords: str = "@basic"
    _testruns: str = "@basic"
    _teststeps: str = "@basic"
    _testparameters: str = "@all"

    @property
    def workitems(self) -> dict[str, str]:
        """Return the fields dict for workitems."""
        return {"workitems": self._workitems}

    @workitems.setter
    def workitems(self, value: str) -> None:
        self._workitems = value

    @property
    def linkedworkitems(self) -> dict[str, str]:
        """Return the fields dict for linkedworkitems."""
        return {"linkedworkitems": self._linkedworkitems}

    @linkedworkitems.setter
    def linkedworkitems(self, value: str) -> None:
        self._linkedworkitems = value

    @property
    def workitem_attachments(self) -> dict[str, str]:
        """Return the fields dict for workitem_attachments."""
        return {"workitem_attachments": self._workitem_attachments}

    @workitem_attachments.setter
    def workitem_attachments(self, value: str) -> None:
        self._workitem_attachments = value

    @property
    def documents(self) -> dict[str, str]:
        """Return the fields dict for document."""
        return {"documents": self._documents}

    @documents.setter
    def documents(self, value: str) -> None:
        self._documents = value

    @property
    def testruns(self) -> dict[str, str]:
        """Return the fields dict for testruns."""
        return {"testruns": self._testruns}

    @testruns.setter
    def testruns(self, value: str) -> None:
        self._testruns = value

    @property
    def testrecords(self) -> dict[str, str]:
        """Return the fields dict for testrecords."""
        return {"testrecords": self._testrecords}

    @testrecords.setter
    def testrecords(self, value: str) -> None:
        self._testrecords = value

    @property
    def teststeps(self) -> dict[str, str]:
        """Return the fields dict for teststeps."""
        return {"teststeps": self._teststeps}

    @teststeps.setter
    def teststeps(self, value: str) -> None:
        self._teststeps = value

    @property
    def testparameters(self) -> dict[str, str]:
        """Return the fields dict for testparameters."""
        return {"testparameters": self._testparameters}

    @testparameters.setter
    def testparameters(self, value: str) -> None:
        self._testparameters = value

    @property
    def all_types(self) -> dict[str, str]:
        """Return all fields dicts merged together."""
        return (
            self.workitem_attachments
            | self.workitems
            | self.linkedworkitems
            | self.documents
            | self.testruns
            | self.testrecords
            | self.testparameters
        )


class PolarionClient:
    """The overall, project independent Polarion client."""

    def __init__(
        self,
        polarion_api_endpoint: str,
        polarion_access_token: str,
        httpx_args: dict[str, t.Any] | None = None,
        batch_size: int = 100,
        page_size: int = 100,
        max_content_size: int = 2 * 1024**2,
        verify_ssl: ssl.SSLContext | bool | None = None,
        max_in_flight_requests: int = 4,
    ):
        if verify_ssl is None:
            verify_ssl = truststore.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        self.client = oa_client.AuthenticatedClient(
            polarion_api_endpoint,
            polarion_access_token,
            verify_ssl=verify_ssl,
            httpx_args=httpx_args or {},
        )
        self.semaphore = asyncio.Semaphore(max_in_flight_requests)
        self.batch_size = batch_size
        self.page_size = page_size
        self.max_content_size = max_content_size
        self.default_fields = DefaultFields()

    def generate_project_client(
        self,
        project_id: str,
        delete_status: str | None = None,
    ) -> projects.ProjectClient:
        """Return a client for a specific project."""
        return projects.ProjectClient(project_id, self, delete_status)

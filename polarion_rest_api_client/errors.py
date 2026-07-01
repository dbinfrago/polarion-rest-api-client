# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
"""Polarion API related errors."""

from __future__ import annotations

from . import data_models as dm

__all__ = [
    "PolarionApiBaseException",
    "PolarionApiException",
    "PolarionApiInternalException",
    "PolarionApiUnexpectedException",
    "PolarionWorkItemException",
]


class PolarionApiBaseException(Exception):
    """Base exception, which is raised, if an API error occurs."""


class PolarionApiInternalException(Exception):
    """Exception being raised, if an error occurs in the client itself."""


class PolarionWorkItemException(PolarionApiInternalException):
    """Exception being raised, if a WorkItem related error occurs."""

    def __init__(self, message: str, work_item: dm.WorkItem):
        self.work_item = work_item

        fields: list[str] = []
        if work_item.id is not None:
            fields.append(f"ID: {work_item.id!r}")
        if work_item.title is not None:
            fields.append(f"Title: {work_item.title!r}")
        if work_item.type is not None:
            fields.append(f"Type: {work_item.type!r}")

        if fields:
            message = f"{message} (WorkItem {', '.join(fields)})"

        super().__init__(message)


class PolarionApiException(PolarionApiBaseException):
    """Exception, which is raised, if an error is raised by the API."""


class PolarionApiUnexpectedException(PolarionApiBaseException):
    """Exception, which is raised, if an unexpected error is raised."""

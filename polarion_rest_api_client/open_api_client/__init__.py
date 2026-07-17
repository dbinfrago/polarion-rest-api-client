# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

"""A client library for accessing Polarion REST API"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)

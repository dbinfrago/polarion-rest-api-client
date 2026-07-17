# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.enumerations_single_patch_request import (
    EnumerationsSinglePatchRequest,
)
from ...models.errors import Errors
from ...types import Response


def _get_kwargs(
    project_id: str,
    enum_context: str,
    enum_name: str,
    target_type: str,
    *,
    body: EnumerationsSinglePatchRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/projects/{project_id}/enumerations/{enum_context}/{enum_name}/{target_type}".format(
            project_id=quote(str(project_id), safe=""),
            enum_context=quote(str(enum_context), safe=""),
            enum_name=quote(str(enum_name), safe=""),
            target_type=quote(str(target_type), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Errors | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = Errors.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Errors.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Errors.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Errors.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = Errors.from_dict(response.json())

        return response_409

    if response.status_code == 413:
        response_413 = Errors.from_dict(response.json())

        return response_413

    if response.status_code == 415:
        response_415 = Errors.from_dict(response.json())

        return response_415

    if response.status_code == 500:
        response_500 = Errors.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = Errors.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | Errors]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    enum_context: str,
    enum_name: str,
    target_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: EnumerationsSinglePatchRequest,
) -> Response[Any | Errors]:
    """Updates the specified Enumeration in the Project context.

    Args:
        project_id (str):
        enum_context (str):
        enum_name (str):
        target_type (str):
        body (EnumerationsSinglePatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Errors]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        enum_context=enum_context,
        enum_name=enum_name,
        target_type=target_type,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    enum_context: str,
    enum_name: str,
    target_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: EnumerationsSinglePatchRequest,
) -> Any | Errors | None:
    """Updates the specified Enumeration in the Project context.

    Args:
        project_id (str):
        enum_context (str):
        enum_name (str):
        target_type (str):
        body (EnumerationsSinglePatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Errors
    """

    return sync_detailed(
        project_id=project_id,
        enum_context=enum_context,
        enum_name=enum_name,
        target_type=target_type,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    enum_context: str,
    enum_name: str,
    target_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: EnumerationsSinglePatchRequest,
) -> Response[Any | Errors]:
    """Updates the specified Enumeration in the Project context.

    Args:
        project_id (str):
        enum_context (str):
        enum_name (str):
        target_type (str):
        body (EnumerationsSinglePatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Errors]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        enum_context=enum_context,
        enum_name=enum_name,
        target_type=target_type,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    enum_context: str,
    enum_name: str,
    target_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: EnumerationsSinglePatchRequest,
) -> Any | Errors | None:
    """Updates the specified Enumeration in the Project context.

    Args:
        project_id (str):
        enum_context (str):
        enum_name (str):
        target_type (str):
        body (EnumerationsSinglePatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Errors
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            enum_context=enum_context,
            enum_name=enum_name,
            target_type=target_type,
            client=client,
            body=body,
        )
    ).parsed

# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.relationship_data_list_request import (
    RelationshipDataListRequest,
)
from ...models.relationship_data_single_request import (
    RelationshipDataSingleRequest,
)
from ...types import Response


def _get_kwargs(
    project_id: str,
    space_id: str,
    page_name: str,
    relationship_id: str,
    *,
    body: RelationshipDataListRequest | RelationshipDataSingleRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/spaces/{space_id}/pages/{page_name}/relationships/{relationship_id}".format(
            project_id=quote(str(project_id), safe=""),
            space_id=quote(str(space_id), safe=""),
            page_name=quote(str(page_name), safe=""),
            relationship_id=quote(str(relationship_id), safe=""),
        ),
    }

    if isinstance(body, RelationshipDataSingleRequest):
        _kwargs["json"] = body.to_dict()
    else:
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

    if response.status_code == 405:
        response_405 = Errors.from_dict(response.json())

        return response_405

    if response.status_code == 406:
        response_406 = Errors.from_dict(response.json())

        return response_406

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
    space_id: str,
    page_name: str,
    relationship_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RelationshipDataListRequest | RelationshipDataSingleRequest,
) -> Response[Any | Errors]:
    """Creates a list of Rich Page Relationships.

    Args:
        project_id (str):
        space_id (str):
        page_name (str):
        relationship_id (str):
        body (RelationshipDataListRequest | RelationshipDataSingleRequest): List of generic
            contents Example: {'data': [{'type': 'workitems', 'id': 'MyProjectId/WI-123'}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Errors]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        space_id=space_id,
        page_name=page_name,
        relationship_id=relationship_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    space_id: str,
    page_name: str,
    relationship_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RelationshipDataListRequest | RelationshipDataSingleRequest,
) -> Any | Errors | None:
    """Creates a list of Rich Page Relationships.

    Args:
        project_id (str):
        space_id (str):
        page_name (str):
        relationship_id (str):
        body (RelationshipDataListRequest | RelationshipDataSingleRequest): List of generic
            contents Example: {'data': [{'type': 'workitems', 'id': 'MyProjectId/WI-123'}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Errors
    """

    return sync_detailed(
        project_id=project_id,
        space_id=space_id,
        page_name=page_name,
        relationship_id=relationship_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    space_id: str,
    page_name: str,
    relationship_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RelationshipDataListRequest | RelationshipDataSingleRequest,
) -> Response[Any | Errors]:
    """Creates a list of Rich Page Relationships.

    Args:
        project_id (str):
        space_id (str):
        page_name (str):
        relationship_id (str):
        body (RelationshipDataListRequest | RelationshipDataSingleRequest): List of generic
            contents Example: {'data': [{'type': 'workitems', 'id': 'MyProjectId/WI-123'}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Errors]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        space_id=space_id,
        page_name=page_name,
        relationship_id=relationship_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    space_id: str,
    page_name: str,
    relationship_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RelationshipDataListRequest | RelationshipDataSingleRequest,
) -> Any | Errors | None:
    """Creates a list of Rich Page Relationships.

    Args:
        project_id (str):
        space_id (str):
        page_name (str):
        relationship_id (str):
        body (RelationshipDataListRequest | RelationshipDataSingleRequest): List of generic
            contents Example: {'data': [{'type': 'workitems', 'id': 'MyProjectId/WI-123'}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Errors
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            space_id=space_id,
            page_name=page_name,
            relationship_id=relationship_id,
            client=client,
            body=body,
        )
    ).parsed

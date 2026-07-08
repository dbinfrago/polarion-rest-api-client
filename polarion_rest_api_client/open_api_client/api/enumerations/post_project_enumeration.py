# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.enumerations_list_post_request import (
    EnumerationsListPostRequest,
)
from ...models.enumerations_list_post_response import (
    EnumerationsListPostResponse,
)
from ...models.errors import Errors
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    body: EnumerationsListPostRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/projects/{project_id}/enumerations",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[EnumerationsListPostResponse, Errors] | None:
    if response.status_code == 201:
        response_201 = EnumerationsListPostResponse.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        try:
            response_400 = Errors.from_dict(response.json())
        except Exception:
            response_400 = None

        return response_400
    if response.status_code == 401:
        try:
            response_401 = Errors.from_dict(response.json())
        except Exception:
            response_401 = None

        return response_401
    if response.status_code == 403:
        try:
            response_403 = Errors.from_dict(response.json())
        except Exception:
            response_403 = None

        return response_403
    if response.status_code == 404:
        try:
            response_404 = Errors.from_dict(response.json())
        except Exception:
            response_404 = None

        return response_404
    if response.status_code == 406:
        try:
            response_406 = Errors.from_dict(response.json())
        except Exception:
            response_406 = None

        return response_406
    if response.status_code == 409:
        try:
            response_409 = Errors.from_dict(response.json())
        except Exception:
            response_409 = None

        return response_409
    if response.status_code == 413:
        try:
            response_413 = Errors.from_dict(response.json())
        except Exception:
            response_413 = None

        return response_413
    if response.status_code == 415:
        try:
            response_415 = Errors.from_dict(response.json())
        except Exception:
            response_415 = None

        return response_415
    if response.status_code == 500:
        try:
            response_500 = Errors.from_dict(response.json())
        except Exception:
            response_500 = None

        return response_500
    if response.status_code == 503:
        try:
            response_503 = Errors.from_dict(response.json())
        except Exception:
            response_503 = None

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[EnumerationsListPostResponse, Errors]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: EnumerationsListPostRequest,
) -> Response[Union[EnumerationsListPostResponse, Errors]]:
    """Creates a list of Enumerations in the Project context.

    Args:
        project_id (str):
        body (EnumerationsListPostRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[EnumerationsListPostResponse, Errors]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: EnumerationsListPostRequest,
) -> Union[EnumerationsListPostResponse, Errors] | None:
    """Creates a list of Enumerations in the Project context.

    Args:
        project_id (str):
        body (EnumerationsListPostRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EnumerationsListPostResponse, Errors]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: EnumerationsListPostRequest,
) -> Response[Union[EnumerationsListPostResponse, Errors]]:
    """Creates a list of Enumerations in the Project context.

    Args:
        project_id (str):
        body (EnumerationsListPostRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[EnumerationsListPostResponse, Errors]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: EnumerationsListPostRequest,
) -> Union[EnumerationsListPostResponse, Errors] | None:
    """Creates a list of Enumerations in the Project context.

    Args:
        project_id (str):
        body (EnumerationsListPostRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EnumerationsListPostResponse, Errors]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed

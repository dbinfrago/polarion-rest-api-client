# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from http import HTTPStatus
from typing import Any, Union, cast

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
        "url": f"/projects/{project_id}/enumerations/{enum_context}/{enum_name}/{target_type}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[Any, Errors] | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
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
) -> Response[Union[Any, Errors]]:
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
    client: Union[AuthenticatedClient, Client],
    body: EnumerationsSinglePatchRequest,
) -> Response[Union[Any, Errors]]:
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
        Response[Union[Any, Errors]]
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
    client: Union[AuthenticatedClient, Client],
    body: EnumerationsSinglePatchRequest,
) -> Union[Any, Errors] | None:
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
        Union[Any, Errors]
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
    client: Union[AuthenticatedClient, Client],
    body: EnumerationsSinglePatchRequest,
) -> Response[Union[Any, Errors]]:
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
        Response[Union[Any, Errors]]
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
    client: Union[AuthenticatedClient, Client],
    body: EnumerationsSinglePatchRequest,
) -> Union[Any, Errors] | None:
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
        Union[Any, Errors]
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

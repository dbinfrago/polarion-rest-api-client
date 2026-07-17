# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.workitems_list_patch_request import WorkitemsListPatchRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    body: WorkitemsListPatchRequest,
    workflow_action: str | Unset = UNSET,
    change_type_to: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["workflowAction"] = workflow_action

    params["changeTypeTo"] = change_type_to

    params = {
        k: v for k, v in params.items() if v is not UNSET and v is not None
    }

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/projects/{project_id}/workitems".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
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
    *,
    client: AuthenticatedClient | Client,
    body: WorkitemsListPatchRequest,
    workflow_action: str | Unset = UNSET,
    change_type_to: str | Unset = UNSET,
) -> Response[Any | Errors]:
    """Updates a list of Work Items.

    Args:
        project_id (str):
        workflow_action (str | Unset):
        change_type_to (str | Unset):
        body (WorkitemsListPatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Errors]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
        workflow_action=workflow_action,
        change_type_to=change_type_to,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: WorkitemsListPatchRequest,
    workflow_action: str | Unset = UNSET,
    change_type_to: str | Unset = UNSET,
) -> Any | Errors | None:
    """Updates a list of Work Items.

    Args:
        project_id (str):
        workflow_action (str | Unset):
        change_type_to (str | Unset):
        body (WorkitemsListPatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Errors
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        body=body,
        workflow_action=workflow_action,
        change_type_to=change_type_to,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: WorkitemsListPatchRequest,
    workflow_action: str | Unset = UNSET,
    change_type_to: str | Unset = UNSET,
) -> Response[Any | Errors]:
    """Updates a list of Work Items.

    Args:
        project_id (str):
        workflow_action (str | Unset):
        change_type_to (str | Unset):
        body (WorkitemsListPatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Errors]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
        workflow_action=workflow_action,
        change_type_to=change_type_to,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: WorkitemsListPatchRequest,
    workflow_action: str | Unset = UNSET,
    change_type_to: str | Unset = UNSET,
) -> Any | Errors | None:
    """Updates a list of Work Items.

    Args:
        project_id (str):
        workflow_action (str | Unset):
        change_type_to (str | Unset):
        body (WorkitemsListPatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Errors
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
            workflow_action=workflow_action,
            change_type_to=change_type_to,
        )
    ).parsed

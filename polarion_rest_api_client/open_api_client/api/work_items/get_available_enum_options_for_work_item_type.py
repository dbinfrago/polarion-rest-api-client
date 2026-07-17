# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.enum_options_action_response_body import (
    EnumOptionsActionResponseBody,
)
from ...models.errors import Errors
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    field_id: str,
    *,
    pagesize: int | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page[size]"] = pagesize

    params["page[number]"] = pagenumber

    params["type"] = type_

    params = {
        k: v for k, v in params.items() if v is not UNSET and v is not None
    }

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/workitems/fields/{field_id}/actions/getAvailableOptions".format(
            project_id=quote(str(project_id), safe=""),
            field_id=quote(str(field_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EnumOptionsActionResponseBody | Errors | None:
    if response.status_code == 200:
        response_200 = EnumOptionsActionResponseBody.from_dict(response.json())

        return response_200

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

    if response.status_code == 406:
        response_406 = Errors.from_dict(response.json())

        return response_406

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
) -> Response[EnumOptionsActionResponseBody | Errors]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    field_id: str,
    *,
    client: AuthenticatedClient | Client,
    pagesize: int | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> Response[EnumOptionsActionResponseBody | Errors]:
    """Returns a list of available options for the requested field for the specified Work Item Type.

    Args:
        project_id (str):
        field_id (str):
        pagesize (int | Unset):
        pagenumber (int | Unset):
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EnumOptionsActionResponseBody | Errors]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        field_id=field_id,
        pagesize=pagesize,
        pagenumber=pagenumber,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    field_id: str,
    *,
    client: AuthenticatedClient | Client,
    pagesize: int | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> EnumOptionsActionResponseBody | Errors | None:
    """Returns a list of available options for the requested field for the specified Work Item Type.

    Args:
        project_id (str):
        field_id (str):
        pagesize (int | Unset):
        pagenumber (int | Unset):
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EnumOptionsActionResponseBody | Errors
    """

    return sync_detailed(
        project_id=project_id,
        field_id=field_id,
        client=client,
        pagesize=pagesize,
        pagenumber=pagenumber,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    field_id: str,
    *,
    client: AuthenticatedClient | Client,
    pagesize: int | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> Response[EnumOptionsActionResponseBody | Errors]:
    """Returns a list of available options for the requested field for the specified Work Item Type.

    Args:
        project_id (str):
        field_id (str):
        pagesize (int | Unset):
        pagenumber (int | Unset):
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EnumOptionsActionResponseBody | Errors]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        field_id=field_id,
        pagesize=pagesize,
        pagenumber=pagenumber,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    field_id: str,
    *,
    client: AuthenticatedClient | Client,
    pagesize: int | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> EnumOptionsActionResponseBody | Errors | None:
    """Returns a list of available options for the requested field for the specified Work Item Type.

    Args:
        project_id (str):
        field_id (str):
        pagesize (int | Unset):
        pagenumber (int | Unset):
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EnumOptionsActionResponseBody | Errors
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            field_id=field_id,
            client=client,
            pagesize=pagesize,
            pagenumber=pagenumber,
            type_=type_,
        )
    ).parsed

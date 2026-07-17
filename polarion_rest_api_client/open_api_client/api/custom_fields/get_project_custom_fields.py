# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.customfields_single_get_response import (
    CustomfieldsSingleGetResponse,
)
from ...models.errors import Errors
from ...models.sparse_fields import SparseFields
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    resource_type: str,
    target_type: str,
    *,
    fields: SparseFields | Unset = UNSET,
    include: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_fields: dict[str, Any] | Unset = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields.to_dict()
    if not isinstance(json_fields, Unset):
        params.update(json_fields)

    params["include"] = include

    params = {
        k: v for k, v in params.items() if v is not UNSET and v is not None
    }

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/customfields/{resource_type}/{target_type}".format(
            project_id=quote(str(project_id), safe=""),
            resource_type=quote(str(resource_type), safe=""),
            target_type=quote(str(target_type), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CustomfieldsSingleGetResponse | Errors | None:
    if response.status_code == 200:
        response_200 = CustomfieldsSingleGetResponse.from_dict(response.json())

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
) -> Response[CustomfieldsSingleGetResponse | Errors]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    resource_type: str,
    target_type: str,
    *,
    client: AuthenticatedClient | Client,
    fields: SparseFields | Unset = UNSET,
    include: str | Unset = UNSET,
) -> Response[CustomfieldsSingleGetResponse | Errors]:
    """Returns the defined Custom Fields for the resource type and target type in the Project context.

    Args:
        project_id (str):
        resource_type (str):
        target_type (str):
        fields (SparseFields | Unset):
        include (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomfieldsSingleGetResponse | Errors]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        resource_type=resource_type,
        target_type=target_type,
        fields=fields,
        include=include,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    resource_type: str,
    target_type: str,
    *,
    client: AuthenticatedClient | Client,
    fields: SparseFields | Unset = UNSET,
    include: str | Unset = UNSET,
) -> CustomfieldsSingleGetResponse | Errors | None:
    """Returns the defined Custom Fields for the resource type and target type in the Project context.

    Args:
        project_id (str):
        resource_type (str):
        target_type (str):
        fields (SparseFields | Unset):
        include (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomfieldsSingleGetResponse | Errors
    """

    return sync_detailed(
        project_id=project_id,
        resource_type=resource_type,
        target_type=target_type,
        client=client,
        fields=fields,
        include=include,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    resource_type: str,
    target_type: str,
    *,
    client: AuthenticatedClient | Client,
    fields: SparseFields | Unset = UNSET,
    include: str | Unset = UNSET,
) -> Response[CustomfieldsSingleGetResponse | Errors]:
    """Returns the defined Custom Fields for the resource type and target type in the Project context.

    Args:
        project_id (str):
        resource_type (str):
        target_type (str):
        fields (SparseFields | Unset):
        include (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomfieldsSingleGetResponse | Errors]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        resource_type=resource_type,
        target_type=target_type,
        fields=fields,
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    resource_type: str,
    target_type: str,
    *,
    client: AuthenticatedClient | Client,
    fields: SparseFields | Unset = UNSET,
    include: str | Unset = UNSET,
) -> CustomfieldsSingleGetResponse | Errors | None:
    """Returns the defined Custom Fields for the resource type and target type in the Project context.

    Args:
        project_id (str):
        resource_type (str):
        target_type (str):
        fields (SparseFields | Unset):
        include (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomfieldsSingleGetResponse | Errors
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            resource_type=resource_type,
            target_type=target_type,
            client=client,
            fields=fields,
            include=include,
        )
    ).parsed

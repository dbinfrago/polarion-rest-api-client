# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.license_assignments_list_get_response import (
    LicenseAssignmentsListGetResponse,
)
from ...models.sparse_fields import SparseFields
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    pagesize: int | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    fields: SparseFields | Unset = UNSET,
    include: str | Unset = UNSET,
    active_only: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page[size]"] = pagesize

    params["page[number]"] = pagenumber

    json_fields: dict[str, Any] | Unset = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields.to_dict()
    if not isinstance(json_fields, Unset):
        params.update(json_fields)

    params["include"] = include

    params["activeOnly"] = active_only

    params = {
        k: v for k, v in params.items() if v is not UNSET and v is not None
    }

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/license/assignments",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Errors | LicenseAssignmentsListGetResponse | None:
    if response.status_code == 200:
        response_200 = LicenseAssignmentsListGetResponse.from_dict(
            response.json()
        )

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
) -> Response[Errors | LicenseAssignmentsListGetResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    pagesize: int | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    fields: SparseFields | Unset = UNSET,
    include: str | Unset = UNSET,
    active_only: bool | Unset = UNSET,
) -> Response[Errors | LicenseAssignmentsListGetResponse]:
    """Returns a list of License Assignments. (Not supported by cloud-based Polarion X.)

    Args:
        pagesize (int | Unset):
        pagenumber (int | Unset):
        fields (SparseFields | Unset):
        include (str | Unset):
        active_only (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Errors | LicenseAssignmentsListGetResponse]
    """

    kwargs = _get_kwargs(
        pagesize=pagesize,
        pagenumber=pagenumber,
        fields=fields,
        include=include,
        active_only=active_only,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    pagesize: int | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    fields: SparseFields | Unset = UNSET,
    include: str | Unset = UNSET,
    active_only: bool | Unset = UNSET,
) -> Errors | LicenseAssignmentsListGetResponse | None:
    """Returns a list of License Assignments. (Not supported by cloud-based Polarion X.)

    Args:
        pagesize (int | Unset):
        pagenumber (int | Unset):
        fields (SparseFields | Unset):
        include (str | Unset):
        active_only (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Errors | LicenseAssignmentsListGetResponse
    """

    return sync_detailed(
        client=client,
        pagesize=pagesize,
        pagenumber=pagenumber,
        fields=fields,
        include=include,
        active_only=active_only,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    pagesize: int | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    fields: SparseFields | Unset = UNSET,
    include: str | Unset = UNSET,
    active_only: bool | Unset = UNSET,
) -> Response[Errors | LicenseAssignmentsListGetResponse]:
    """Returns a list of License Assignments. (Not supported by cloud-based Polarion X.)

    Args:
        pagesize (int | Unset):
        pagenumber (int | Unset):
        fields (SparseFields | Unset):
        include (str | Unset):
        active_only (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Errors | LicenseAssignmentsListGetResponse]
    """

    kwargs = _get_kwargs(
        pagesize=pagesize,
        pagenumber=pagenumber,
        fields=fields,
        include=include,
        active_only=active_only,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    pagesize: int | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    fields: SparseFields | Unset = UNSET,
    include: str | Unset = UNSET,
    active_only: bool | Unset = UNSET,
) -> Errors | LicenseAssignmentsListGetResponse | None:
    """Returns a list of License Assignments. (Not supported by cloud-based Polarion X.)

    Args:
        pagesize (int | Unset):
        pagenumber (int | Unset):
        fields (SparseFields | Unset):
        include (str | Unset):
        active_only (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Errors | LicenseAssignmentsListGetResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            pagesize=pagesize,
            pagenumber=pagenumber,
            fields=fields,
            include=include,
            active_only=active_only,
        )
    ).parsed

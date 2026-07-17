# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.license_slots_single_get_response import (
    LicenseSlotsSingleGetResponse,
)
from ...models.sparse_fields import SparseFields
from ...types import UNSET, Response, Unset


def _get_kwargs(
    type_id: str,
    model: str,
    group: str,
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
        "url": "/license/types/{type_id}/slots/{model}/{group}".format(
            type_id=quote(str(type_id), safe=""),
            model=quote(str(model), safe=""),
            group=quote(str(group), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Errors | LicenseSlotsSingleGetResponse | None:
    if response.status_code == 200:
        response_200 = LicenseSlotsSingleGetResponse.from_dict(response.json())

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
) -> Response[Errors | LicenseSlotsSingleGetResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    type_id: str,
    model: str,
    group: str,
    *,
    client: AuthenticatedClient | Client,
    fields: SparseFields | Unset = UNSET,
    include: str | Unset = UNSET,
) -> Response[Errors | LicenseSlotsSingleGetResponse]:
    """Returns the specified License Slot. (Not supported by cloud-based Polarion X.)

    Args:
        type_id (str):
        model (str):
        group (str):
        fields (SparseFields | Unset):
        include (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Errors | LicenseSlotsSingleGetResponse]
    """

    kwargs = _get_kwargs(
        type_id=type_id,
        model=model,
        group=group,
        fields=fields,
        include=include,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    type_id: str,
    model: str,
    group: str,
    *,
    client: AuthenticatedClient | Client,
    fields: SparseFields | Unset = UNSET,
    include: str | Unset = UNSET,
) -> Errors | LicenseSlotsSingleGetResponse | None:
    """Returns the specified License Slot. (Not supported by cloud-based Polarion X.)

    Args:
        type_id (str):
        model (str):
        group (str):
        fields (SparseFields | Unset):
        include (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Errors | LicenseSlotsSingleGetResponse
    """

    return sync_detailed(
        type_id=type_id,
        model=model,
        group=group,
        client=client,
        fields=fields,
        include=include,
    ).parsed


async def asyncio_detailed(
    type_id: str,
    model: str,
    group: str,
    *,
    client: AuthenticatedClient | Client,
    fields: SparseFields | Unset = UNSET,
    include: str | Unset = UNSET,
) -> Response[Errors | LicenseSlotsSingleGetResponse]:
    """Returns the specified License Slot. (Not supported by cloud-based Polarion X.)

    Args:
        type_id (str):
        model (str):
        group (str):
        fields (SparseFields | Unset):
        include (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Errors | LicenseSlotsSingleGetResponse]
    """

    kwargs = _get_kwargs(
        type_id=type_id,
        model=model,
        group=group,
        fields=fields,
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    type_id: str,
    model: str,
    group: str,
    *,
    client: AuthenticatedClient | Client,
    fields: SparseFields | Unset = UNSET,
    include: str | Unset = UNSET,
) -> Errors | LicenseSlotsSingleGetResponse | None:
    """Returns the specified License Slot. (Not supported by cloud-based Polarion X.)

    Args:
        type_id (str):
        model (str):
        group (str):
        fields (SparseFields | Unset):
        include (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Errors | LicenseSlotsSingleGetResponse
    """

    return (
        await asyncio_detailed(
            type_id=type_id,
            model=model,
            group=group,
            client=client,
            fields=fields,
            include=include,
        )
    ).parsed

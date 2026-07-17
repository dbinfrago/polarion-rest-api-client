# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.featureselections_single_get_response import (
    FeatureselectionsSingleGetResponse,
)
from ...models.sparse_fields import SparseFields
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    work_item_id: str,
    selection_type_id: str,
    target_project_id: str,
    target_work_item_id: str,
    *,
    fields: SparseFields | Unset = UNSET,
    include: str | Unset = UNSET,
    revision: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_fields: dict[str, Any] | Unset = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields.to_dict()
    if not isinstance(json_fields, Unset):
        params.update(json_fields)

    params["include"] = include

    params["revision"] = revision

    params = {
        k: v for k, v in params.items() if v is not UNSET and v is not None
    }

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/workitems/{work_item_id}/featureselections/{selection_type_id}/{target_project_id}/{target_work_item_id}".format(
            project_id=quote(str(project_id), safe=""),
            work_item_id=quote(str(work_item_id), safe=""),
            selection_type_id=quote(str(selection_type_id), safe=""),
            target_project_id=quote(str(target_project_id), safe=""),
            target_work_item_id=quote(str(target_work_item_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Errors | FeatureselectionsSingleGetResponse | None:
    if response.status_code == 200:
        response_200 = FeatureselectionsSingleGetResponse.from_dict(
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
) -> Response[Errors | FeatureselectionsSingleGetResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    work_item_id: str,
    selection_type_id: str,
    target_project_id: str,
    target_work_item_id: str,
    *,
    client: AuthenticatedClient | Client,
    fields: SparseFields | Unset = UNSET,
    include: str | Unset = UNSET,
    revision: str | Unset = UNSET,
) -> Response[Errors | FeatureselectionsSingleGetResponse]:
    """Returns the specified Feature Selection.

    Args:
        project_id (str):
        work_item_id (str):
        selection_type_id (str):
        target_project_id (str):
        target_work_item_id (str):
        fields (SparseFields | Unset):
        include (str | Unset):
        revision (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Errors | FeatureselectionsSingleGetResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        work_item_id=work_item_id,
        selection_type_id=selection_type_id,
        target_project_id=target_project_id,
        target_work_item_id=target_work_item_id,
        fields=fields,
        include=include,
        revision=revision,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    work_item_id: str,
    selection_type_id: str,
    target_project_id: str,
    target_work_item_id: str,
    *,
    client: AuthenticatedClient | Client,
    fields: SparseFields | Unset = UNSET,
    include: str | Unset = UNSET,
    revision: str | Unset = UNSET,
) -> Errors | FeatureselectionsSingleGetResponse | None:
    """Returns the specified Feature Selection.

    Args:
        project_id (str):
        work_item_id (str):
        selection_type_id (str):
        target_project_id (str):
        target_work_item_id (str):
        fields (SparseFields | Unset):
        include (str | Unset):
        revision (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Errors | FeatureselectionsSingleGetResponse
    """

    return sync_detailed(
        project_id=project_id,
        work_item_id=work_item_id,
        selection_type_id=selection_type_id,
        target_project_id=target_project_id,
        target_work_item_id=target_work_item_id,
        client=client,
        fields=fields,
        include=include,
        revision=revision,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    work_item_id: str,
    selection_type_id: str,
    target_project_id: str,
    target_work_item_id: str,
    *,
    client: AuthenticatedClient | Client,
    fields: SparseFields | Unset = UNSET,
    include: str | Unset = UNSET,
    revision: str | Unset = UNSET,
) -> Response[Errors | FeatureselectionsSingleGetResponse]:
    """Returns the specified Feature Selection.

    Args:
        project_id (str):
        work_item_id (str):
        selection_type_id (str):
        target_project_id (str):
        target_work_item_id (str):
        fields (SparseFields | Unset):
        include (str | Unset):
        revision (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Errors | FeatureselectionsSingleGetResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        work_item_id=work_item_id,
        selection_type_id=selection_type_id,
        target_project_id=target_project_id,
        target_work_item_id=target_work_item_id,
        fields=fields,
        include=include,
        revision=revision,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    work_item_id: str,
    selection_type_id: str,
    target_project_id: str,
    target_work_item_id: str,
    *,
    client: AuthenticatedClient | Client,
    fields: SparseFields | Unset = UNSET,
    include: str | Unset = UNSET,
    revision: str | Unset = UNSET,
) -> Errors | FeatureselectionsSingleGetResponse | None:
    """Returns the specified Feature Selection.

    Args:
        project_id (str):
        work_item_id (str):
        selection_type_id (str):
        target_project_id (str):
        target_work_item_id (str):
        fields (SparseFields | Unset):
        include (str | Unset):
        revision (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Errors | FeatureselectionsSingleGetResponse
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            work_item_id=work_item_id,
            selection_type_id=selection_type_id,
            target_project_id=target_project_id,
            target_work_item_id=target_work_item_id,
            client=client,
            fields=fields,
            include=include,
            revision=revision,
        )
    ).parsed

# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.sparse_fields import SparseFields
from ...models.testruns_list_get_response import TestrunsListGetResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    pagesize: Union[Unset, int] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    fields: Union[Unset, "SparseFields"] = UNSET,
    include: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
    revision: Union[Unset, str] = UNSET,
    templates: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page[size]"] = pagesize

    params["page[number]"] = pagenumber

    json_fields: Union[Unset, dict[str, Any]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields.to_dict()
    if not isinstance(json_fields, Unset):
        params.update(json_fields)

    params["include"] = include

    params["query"] = query

    params["sort"] = sort

    params["revision"] = revision

    params["templates"] = templates

    params = {
        k: v for k, v in params.items() if v is not UNSET and v is not None
    }

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/projects/{project_id}/testruns",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[Errors, TestrunsListGetResponse] | None:
    if response.status_code == 200:
        response_200 = TestrunsListGetResponse.from_dict(response.json())

        return response_200
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
) -> Response[Union[Errors, TestrunsListGetResponse]]:
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
    pagesize: Union[Unset, int] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    fields: Union[Unset, "SparseFields"] = UNSET,
    include: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
    revision: Union[Unset, str] = UNSET,
    templates: Union[Unset, bool] = UNSET,
) -> Response[Union[Errors, TestrunsListGetResponse]]:
    """Returns a list of Test Runs.

    Args:
        project_id (str):
        pagesize (Union[Unset, int]):
        pagenumber (Union[Unset, int]):
        fields (Union[Unset, SparseFields]):
        include (Union[Unset, str]):
        query (Union[Unset, str]):
        sort (Union[Unset, str]):
        revision (Union[Unset, str]):
        templates (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, TestrunsListGetResponse]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        pagesize=pagesize,
        pagenumber=pagenumber,
        fields=fields,
        include=include,
        query=query,
        sort=sort,
        revision=revision,
        templates=templates,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    pagesize: Union[Unset, int] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    fields: Union[Unset, "SparseFields"] = UNSET,
    include: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
    revision: Union[Unset, str] = UNSET,
    templates: Union[Unset, bool] = UNSET,
) -> Union[Errors, TestrunsListGetResponse] | None:
    """Returns a list of Test Runs.

    Args:
        project_id (str):
        pagesize (Union[Unset, int]):
        pagenumber (Union[Unset, int]):
        fields (Union[Unset, SparseFields]):
        include (Union[Unset, str]):
        query (Union[Unset, str]):
        sort (Union[Unset, str]):
        revision (Union[Unset, str]):
        templates (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, TestrunsListGetResponse]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        pagesize=pagesize,
        pagenumber=pagenumber,
        fields=fields,
        include=include,
        query=query,
        sort=sort,
        revision=revision,
        templates=templates,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    pagesize: Union[Unset, int] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    fields: Union[Unset, "SparseFields"] = UNSET,
    include: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
    revision: Union[Unset, str] = UNSET,
    templates: Union[Unset, bool] = UNSET,
) -> Response[Union[Errors, TestrunsListGetResponse]]:
    """Returns a list of Test Runs.

    Args:
        project_id (str):
        pagesize (Union[Unset, int]):
        pagenumber (Union[Unset, int]):
        fields (Union[Unset, SparseFields]):
        include (Union[Unset, str]):
        query (Union[Unset, str]):
        sort (Union[Unset, str]):
        revision (Union[Unset, str]):
        templates (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, TestrunsListGetResponse]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        pagesize=pagesize,
        pagenumber=pagenumber,
        fields=fields,
        include=include,
        query=query,
        sort=sort,
        revision=revision,
        templates=templates,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    pagesize: Union[Unset, int] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    fields: Union[Unset, "SparseFields"] = UNSET,
    include: Union[Unset, str] = UNSET,
    query: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
    revision: Union[Unset, str] = UNSET,
    templates: Union[Unset, bool] = UNSET,
) -> Union[Errors, TestrunsListGetResponse] | None:
    """Returns a list of Test Runs.

    Args:
        project_id (str):
        pagesize (Union[Unset, int]):
        pagenumber (Union[Unset, int]):
        fields (Union[Unset, SparseFields]):
        include (Union[Unset, str]):
        query (Union[Unset, str]):
        sort (Union[Unset, str]):
        revision (Union[Unset, str]):
        templates (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, TestrunsListGetResponse]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            pagesize=pagesize,
            pagenumber=pagenumber,
            fields=fields,
            include=include,
            query=query,
            sort=sort,
            revision=revision,
            templates=templates,
        )
    ).parsed

# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.jobs_single_post_response import JobsSinglePostResponse
from ...models.merge_document_request_body import MergeDocumentRequestBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    space_id: str,
    document_name: str,
    *,
    body: MergeDocumentRequestBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/spaces/{space_id}/documents/{document_name}/actions/mergeToMaster".format(
            project_id=quote(str(project_id), safe=""),
            space_id=quote(str(space_id), safe=""),
            document_name=quote(str(document_name), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Errors | JobsSinglePostResponse | None:
    if response.status_code == 202:
        response_202 = JobsSinglePostResponse.from_dict(response.json())

        return response_202

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
) -> Response[Errors | JobsSinglePostResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    space_id: str,
    document_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: MergeDocumentRequestBody | Unset = UNSET,
) -> Response[Errors | JobsSinglePostResponse]:
    """Merges Work Item changes from specified Branched Document to Master.

    Args:
        project_id (str):
        space_id (str):
        document_name (str):
        body (MergeDocumentRequestBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Errors | JobsSinglePostResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        space_id=space_id,
        document_name=document_name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    space_id: str,
    document_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: MergeDocumentRequestBody | Unset = UNSET,
) -> Errors | JobsSinglePostResponse | None:
    """Merges Work Item changes from specified Branched Document to Master.

    Args:
        project_id (str):
        space_id (str):
        document_name (str):
        body (MergeDocumentRequestBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Errors | JobsSinglePostResponse
    """

    return sync_detailed(
        project_id=project_id,
        space_id=space_id,
        document_name=document_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    space_id: str,
    document_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: MergeDocumentRequestBody | Unset = UNSET,
) -> Response[Errors | JobsSinglePostResponse]:
    """Merges Work Item changes from specified Branched Document to Master.

    Args:
        project_id (str):
        space_id (str):
        document_name (str):
        body (MergeDocumentRequestBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Errors | JobsSinglePostResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        space_id=space_id,
        document_name=document_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    space_id: str,
    document_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: MergeDocumentRequestBody | Unset = UNSET,
) -> Errors | JobsSinglePostResponse | None:
    """Merges Work Item changes from specified Branched Document to Master.

    Args:
        project_id (str):
        space_id (str):
        document_name (str):
        body (MergeDocumentRequestBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Errors | JobsSinglePostResponse
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            space_id=space_id,
            document_name=document_name,
            client=client,
            body=body,
        )
    ).parsed

# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.fields_metadata_action_response_body import (
    FieldsMetadataActionResponseBody,
)
from ...types import Response


def _get_kwargs(
    project_id: str,
    test_run_id: str,
    test_case_project_id: str,
    test_case_id: str,
    iteration: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/testruns/{test_run_id}/testrecords/{test_case_project_id}/{test_case_id}/{iteration}/actions/getFieldsMetadata".format(
            project_id=quote(str(project_id), safe=""),
            test_run_id=quote(str(test_run_id), safe=""),
            test_case_project_id=quote(str(test_case_project_id), safe=""),
            test_case_id=quote(str(test_case_id), safe=""),
            iteration=quote(str(iteration), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Errors | FieldsMetadataActionResponseBody | None:
    if response.status_code == 200:
        response_200 = FieldsMetadataActionResponseBody.from_dict(
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
) -> Response[Errors | FieldsMetadataActionResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    test_run_id: str,
    test_case_project_id: str,
    test_case_id: str,
    iteration: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Errors | FieldsMetadataActionResponseBody]:
    """Returns fields for the specified resource.

    Args:
        project_id (str):
        test_run_id (str):
        test_case_project_id (str):
        test_case_id (str):
        iteration (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Errors | FieldsMetadataActionResponseBody]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        test_run_id=test_run_id,
        test_case_project_id=test_case_project_id,
        test_case_id=test_case_id,
        iteration=iteration,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    test_run_id: str,
    test_case_project_id: str,
    test_case_id: str,
    iteration: str,
    *,
    client: AuthenticatedClient | Client,
) -> Errors | FieldsMetadataActionResponseBody | None:
    """Returns fields for the specified resource.

    Args:
        project_id (str):
        test_run_id (str):
        test_case_project_id (str):
        test_case_id (str):
        iteration (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Errors | FieldsMetadataActionResponseBody
    """

    return sync_detailed(
        project_id=project_id,
        test_run_id=test_run_id,
        test_case_project_id=test_case_project_id,
        test_case_id=test_case_id,
        iteration=iteration,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    test_run_id: str,
    test_case_project_id: str,
    test_case_id: str,
    iteration: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Errors | FieldsMetadataActionResponseBody]:
    """Returns fields for the specified resource.

    Args:
        project_id (str):
        test_run_id (str):
        test_case_project_id (str):
        test_case_id (str):
        iteration (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Errors | FieldsMetadataActionResponseBody]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        test_run_id=test_run_id,
        test_case_project_id=test_case_project_id,
        test_case_id=test_case_id,
        iteration=iteration,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    test_run_id: str,
    test_case_project_id: str,
    test_case_id: str,
    iteration: str,
    *,
    client: AuthenticatedClient | Client,
) -> Errors | FieldsMetadataActionResponseBody | None:
    """Returns fields for the specified resource.

    Args:
        project_id (str):
        test_run_id (str):
        test_case_project_id (str):
        test_case_id (str):
        iteration (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Errors | FieldsMetadataActionResponseBody
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            test_run_id=test_run_id,
            test_case_project_id=test_case_project_id,
            test_case_id=test_case_id,
            iteration=iteration,
            client=client,
        )
    ).parsed

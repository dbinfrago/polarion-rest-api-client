# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import asyncio
import json
import ssl
from unittest import mock

import pytest
import pytest_httpx

import polarion_rest_api_client as polarion_api
from tests.conftest import (
    TEST_PROJECT_RESPONSE_JSON,
    TEST_PROJECTS_RESPONSE_JSON,
)


def _polarion_client() -> polarion_api.PolarionClient:
    return polarion_api.PolarionClient(
        polarion_api_endpoint="http://127.0.0.1/api",
        polarion_access_token="PAT123",
    )


def test_list_projects(httpx_mock: pytest_httpx.HTTPXMock):
    with open(TEST_PROJECTS_RESPONSE_JSON, encoding="utf8") as f:
        httpx_mock.add_response(json=json.load(f))

    client = _polarion_client()
    result, next_page = client.projects.get_multi(fields={"projects": "@all"})

    req = httpx_mock.get_request()
    assert req.url.path.endswith("/projects")
    assert req.url.params["fields[projects]"] == "@all"
    assert next_page is False
    assert [p.id for p in result] == ["MyProjectId", "OtherProject"]
    assert result[0].name == "My Project"
    assert result[0].active is True
    assert result[0].tracker_prefix == "MP"
    assert result[0].description is not None
    assert result[0].description.value == "A project"
    assert result[1].active is False


def test_list_projects_async(httpx_mock: pytest_httpx.HTTPXMock):
    with open(TEST_PROJECTS_RESPONSE_JSON, encoding="utf8") as f:
        httpx_mock.add_response(json=json.load(f))

    client = _polarion_client()
    result, next_page = asyncio.run(client.projects.async_get_multi())

    assert next_page is False
    assert [p.id for p in result] == ["MyProjectId", "OtherProject"]


@mock.patch("httpx.Client")
@pytest.mark.parametrize("verify_ssl", [False, True])
def test_verify_ssl_boolean(mock_httpx_client, verify_ssl: bool | None):
    polarion_client = polarion_api.PolarionClient(
        polarion_api_endpoint="https://example.com",
        polarion_access_token="fake_token",
        verify_ssl=verify_ssl,
    )

    polarion_client.client.get_httpx_client()

    _, kwargs = mock_httpx_client.call_args
    assert kwargs["verify"] is verify_ssl


@mock.patch("httpx.Client")
def test_default_verify_ssl(mock_httpx_client):
    polarion_client = polarion_api.PolarionClient(
        polarion_api_endpoint="https://example.com",
        polarion_access_token="fake_token",
    )

    polarion_client.client.get_httpx_client()

    _, kwargs = mock_httpx_client.call_args
    assert isinstance(kwargs["verify"], ssl.SSLContext)
    assert kwargs["verify"].protocol == ssl.PROTOCOL_TLS_CLIENT


@mock.patch("httpx.Client")
def test_custom_ssl_context(mock_httpx_client):
    custom_ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    polarion_client = polarion_api.PolarionClient(
        polarion_api_endpoint="https://example.com",
        polarion_access_token="fake_token",
        verify_ssl=custom_ssl_context,
    )

    polarion_client.client.get_httpx_client()

    _, kwargs = mock_httpx_client.call_args
    assert kwargs["verify"] is custom_ssl_context


def test_api_authentication(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_PROJECT_RESPONSE_JSON, encoding="utf8") as f:
        httpx_mock.add_response(
            match_headers={"Authorization": "Bearer PAT123"},
            json=json.load(f),
        )

    assert client.exists()


def test_check_existing_project(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_PROJECT_RESPONSE_JSON, encoding="utf8") as f:
        httpx_mock.add_response(json=json.load(f))

    assert client.exists()


def test_check_non_existing_project(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    httpx_mock.add_response(status_code=404, json={})

    assert not client.exists()

# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import json

import pytest_httpx

import polarion_rest_api_client as polarion_api
from tests.conftest import (
    TEST_TRUN_PARAM_CREATED_REQ_1,
    TEST_TRUN_PARAM_CREATED_REQ_2,
    TEST_TRUN_PARAM_CREATED_RES,
    TEST_TRUN_PARAM_DELETE_REQ_1,
    TEST_TRUN_PARAM_DELETE_REQ_2,
    TEST_TRUN_PARAM_NEXT_RES,
    TEST_TRUN_PARAM_NO_NEXT_RES,
)


def test_get_test_params_trun_multi_page(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_TRUN_PARAM_NEXT_RES, encoding="utf8") as f:
        content = json.load(f)
        httpx_mock.add_response(json=content)
        httpx_mock.add_response(json=content)

    with open(TEST_TRUN_PARAM_NO_NEXT_RES, encoding="utf8") as f:
        httpx_mock.add_response(json=json.load(f))

    params: list[polarion_api.TestRunParameter] = (
        client.test_runs.parameters.get_all(
            "123", fields={"teststeps": "@basic"}
        )
    )

    query = {
        "page[size]": "100",
        "page[number]": "1",
        "fields[teststeps]": "@basic",
    }
    reqs = httpx_mock.get_requests()

    assert len(reqs) == 3
    assert reqs[0].method == "GET"
    assert dict(reqs[0].url.params) == query
    query["page[number]"] = "2"
    assert dict(reqs[1].url.params) == query
    query["page[number]"] = "3"
    assert dict(reqs[2].url.params) == query
    assert all(
        req.url.path == "/api/projects/PROJ/testruns/123/testparameters"
        for req in reqs
    )
    assert len(params) == 6
    assert params.pop(5).name == "Another Name"
    assert all(
        param.test_run_id == "123"
        and param.name == "Example Test Parameter value"
        and param.value == "Example Test Parameter value"
        for param in params
    )


def test_get_test_params_trecord_multi_page(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_TRUN_PARAM_NEXT_RES, encoding="utf8") as f:
        content = json.load(f)
        httpx_mock.add_response(json=content)

    with open(TEST_TRUN_PARAM_NO_NEXT_RES, encoding="utf8") as f:
        httpx_mock.add_response(json=json.load(f))

    params: list[polarion_api.TestRecordParameter] = (
        client.test_runs.records.parameters.get_all(
            polarion_api.TestRecord("TRUN", "PROJ", "TCID", iteration=0),
            fields={"teststeps": "@basic"},
        )
    )

    query = {
        "page[size]": "100",
        "page[number]": "1",
        "fields[teststeps]": "@basic",
    }
    reqs = httpx_mock.get_requests()

    assert len(reqs) == 2
    assert reqs[0].method == "GET"
    assert (
        reqs[0].url.path
        == "/api/projects/PROJ/testruns/TRUN/testrecords/PROJ/TCID/0/testparameters"
    )
    assert dict(reqs[0].url.params) == query
    query["page[number]"] = "2"
    assert reqs[1].method == "GET"
    assert (
        reqs[1].url.path
        == "/api/projects/PROJ/testruns/TRUN/testrecords/PROJ/TCID/0/testparameters"
    )
    assert dict(reqs[1].url.params) == query
    assert len(params) == 4
    assert params.pop(3).name == "Another Name"
    assert all(
        param.test_record
        == polarion_api.TestRecord("TRUN", "PROJ", "TCID", iteration=0)
        and param.name == "Example Test Parameter value"
        and param.value == "Example Test Parameter value"
        for param in params
    )


def test_create_parameters_trun(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_TRUN_PARAM_CREATED_RES, encoding="utf8") as f:
        content = json.load(f)
        httpx_mock.add_response(201, json=content)
        httpx_mock.add_response(201, json=content)

    with open(TEST_TRUN_PARAM_CREATED_REQ_1, encoding="utf8") as f:
        expected_req_1 = json.load(f)

    with open(TEST_TRUN_PARAM_CREATED_REQ_2, encoding="utf8") as f:
        expected_req_2 = json.load(f)

    test_run_id = "asdfg"
    test_run_id_1 = "qwertz"

    tp_1 = polarion_api.TestRunParameter(test_run_id, "name1", "value1")
    tp_2 = polarion_api.TestRunParameter(test_run_id_1, "name2", "value2")
    tp_3 = polarion_api.TestRunParameter(test_run_id, "name3", "value3")

    client.test_runs.parameters.create([tp_1, tp_2, tp_3])

    reqs = httpx_mock.get_requests()
    req_data_1 = json.loads(reqs[0].content.decode("utf-8"))
    req_data_2 = json.loads(reqs[1].content.decode("utf-8"))
    assert len(reqs) == 2
    assert (
        reqs[0].url.path == "/api/projects/PROJ/testruns/asdfg/testparameters"
    )
    assert (
        reqs[1].url.path == "/api/projects/PROJ/testruns/qwertz/testparameters"
    )
    assert reqs[0].method == "POST"
    assert reqs[1].method == "POST"
    assert req_data_1 == expected_req_1
    assert req_data_2 == expected_req_2


def test_create_parameters_trecord(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    with open(TEST_TRUN_PARAM_CREATED_RES, encoding="utf8") as f:
        content = json.load(f)
        httpx_mock.add_response(201, json=content)
        httpx_mock.add_response(201, json=content)

    with open(TEST_TRUN_PARAM_CREATED_REQ_1, encoding="utf8") as f:
        expected_req_1 = json.load(f)

    with open(TEST_TRUN_PARAM_CREATED_REQ_2, encoding="utf8") as f:
        expected_req_2 = json.load(f)

    test_record_1 = polarion_api.TestRecord("TRUN", "PROJ", "TC1", iteration=0)
    test_record_2 = polarion_api.TestRecord("TRUN", "PROJ", "TC1", iteration=1)

    tp_1 = polarion_api.TestRecordParameter(test_record_1, "name1", "value1")
    tp_2 = polarion_api.TestRecordParameter(test_record_2, "name2", "value2")
    tp_3 = polarion_api.TestRecordParameter(test_record_1, "name3", "value3")

    client.test_runs.records.parameters.create([tp_1, tp_2, tp_3])

    reqs = httpx_mock.get_requests()
    req_data_1 = json.loads(reqs[0].content.decode("utf-8"))
    req_data_2 = json.loads(reqs[1].content.decode("utf-8"))
    assert len(reqs) == 2
    assert (
        reqs[0].url.path
        == "/api/projects/PROJ/testruns/TRUN/testrecords/PROJ/TC1/0/testparameters"
    )
    assert (
        reqs[1].url.path
        == "/api/projects/PROJ/testruns/TRUN/testrecords/PROJ/TC1/1/testparameters"
    )
    assert reqs[0].method == "POST"
    assert reqs[1].method == "POST"
    assert req_data_1 == expected_req_1
    assert req_data_2 == expected_req_2


def test_delete_parameters_trun(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    httpx_mock.add_response(204)
    httpx_mock.add_response(204)

    with open(TEST_TRUN_PARAM_DELETE_REQ_1, encoding="utf8") as f:
        expected_req_1 = json.load(f)

    with open(TEST_TRUN_PARAM_DELETE_REQ_2, encoding="utf8") as f:
        expected_req_2 = json.load(f)

    tp_1 = polarion_api.TestRunParameter("TRUN", "name1", "value1")
    tp_2 = polarion_api.TestRunParameter("TRUN2", "name1", "value2")
    tp_3 = polarion_api.TestRunParameter("TRUN", "name2", "value1")

    client.test_runs.parameters.delete([tp_1, tp_2, tp_3])

    reqs = httpx_mock.get_requests()
    req_data_1 = json.loads(reqs[0].content.decode("utf-8"))
    req_data_2 = json.loads(reqs[1].content.decode("utf-8"))
    assert len(reqs) == 2
    assert (
        reqs[0].url.path == "/api/projects/PROJ/testruns/TRUN/testparameters"
    )
    assert (
        reqs[1].url.path == "/api/projects/PROJ/testruns/TRUN2/testparameters"
    )
    assert reqs[0].method == "DELETE"
    assert reqs[1].method == "DELETE"
    assert req_data_1 == expected_req_1
    assert req_data_2 == expected_req_2


def test_delete_parameters_trecord(
    client: polarion_api.ProjectClient,
    httpx_mock: pytest_httpx.HTTPXMock,
):
    httpx_mock.add_response(204)
    httpx_mock.add_response(204)
    httpx_mock.add_response(204)

    test_record_1 = polarion_api.TestRecord("TRUN", "PROJ", "TC1", iteration=0)
    test_record_2 = polarion_api.TestRecord("TRUN", "PROJ", "TC1", iteration=1)

    tp_1 = polarion_api.TestRecordParameter(test_record_1, "name1", "value1")
    tp_2 = polarion_api.TestRecordParameter(test_record_2, "name2", "value2")
    tp_3 = polarion_api.TestRecordParameter(test_record_1, "name3", "value3")

    client.test_runs.records.parameters.delete([tp_1, tp_2, tp_3])

    reqs = httpx_mock.get_requests()
    assert len(reqs) == 3
    assert (
        reqs[0].url.path
        == "/api/projects/PROJ/testruns/TRUN/testrecords/PROJ/TC1/0/testparameters/name1"
    )
    assert (
        reqs[1].url.path
        == "/api/projects/PROJ/testruns/TRUN/testrecords/PROJ/TC1/0/testparameters/name3"
    )
    assert (
        reqs[2].url.path
        == "/api/projects/PROJ/testruns/TRUN/testrecords/PROJ/TC1/1/testparameters/name2"
    )
    assert reqs[0].method == "DELETE"
    assert reqs[1].method == "DELETE"
    assert reqs[2].method == "DELETE"

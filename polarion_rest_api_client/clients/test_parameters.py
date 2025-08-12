# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
"""Clients to handle test parameters."""

import itertools
import typing as t

from polarion_rest_api_client import data_models as dm
from polarion_rest_api_client.open_api_client import models as api_models
from polarion_rest_api_client.open_api_client.api.test_records import (
    delete_test_record_test_parameter,
    get_test_record_test_parameters,
    post_test_record_test_parameters,
)
from polarion_rest_api_client.open_api_client.api.test_runs import (
    delete_test_run_test_parameters,
    get_test_run_test_parameters,
    post_test_run_test_parameters,
)

from . import base_classes as bc


class TestRunParameters(
    bc.MultiGetClient[dm.TestRunParameter],
    bc.CreateClient[dm.TestRunParameter],
    bc.DeleteClient[dm.TestRunParameter],
):
    """Client to handle TestParameters of a TestRun."""

    def get_multi(  # type: ignore[override]
        self,
        test_run_id: str,
        *,
        page_size: int = 100,
        page_number: int = 1,
        fields: dict[str, str] | None = None,
    ) -> tuple[list[dm.TestRunParameter], bool]:
        if fields is None:
            fields = self._client.default_fields.testparameters

        sparse_fields = self._build_sparse_fields(fields)
        response = get_test_run_test_parameters.sync_detailed(
            self._project_id,
            test_run_id,
            client=self._client.client,
            fields=sparse_fields,
            pagenumber=page_number,
            pagesize=page_size,
        )

        return _parse_get_response(response.parsed, test_run_id)

    async def a_get_multi(  # type: ignore[override]
        self,
        test_run_id: str,
        *,
        page_size: int = 100,
        page_number: int = 1,
        fields: dict[str, str] | None = None,
    ) -> tuple[list[dm.TestRunParameter], bool]:
        if fields is None:
            fields = self._client.default_fields.testparameters

        sparse_fields = self._build_sparse_fields(fields)
        response = await get_test_run_test_parameters.asyncio_detailed(
            self._project_id,
            test_run_id,
            client=self._client.client,
            fields=sparse_fields,
            pagenumber=page_number,
            pagesize=page_size,
        )

        self._raise_on_error(response)
        return _parse_get_response(response.parsed, test_run_id)

    def _pre_batching_grouping(
        self, items: list[dm.TestRunParameter]
    ) -> t.Generator[list[dm.TestRunParameter], None, None]:
        for _, group in itertools.groupby(
            sorted(
                items,
                key=lambda x: x.test_run_id,
            ),
            lambda x: x.test_run_id,
        ):
            yield list(group)

    def _create(self, items: list[dm.TestRunParameter]) -> None:
        """Call only with items with common test_run_id."""
        test_run_id = items[0].test_run_id
        body = _build_post_body(items)

        response = post_test_run_test_parameters.sync_detailed(
            self._project_id,
            test_run_id,
            client=self._client.client,
            body=body,
        )
        self._raise_on_error(response)

        assert isinstance(
            response.parsed, api_models.TestparametersListPostResponse
        )
        assert response.parsed.data

    async def _a_create(self, items: list[dm.TestRunParameter]) -> None:
        """Call only with items with common test_run_id."""
        test_run_id = items[0].test_run_id
        body = _build_post_body(items)

        response = await post_test_run_test_parameters.asyncio_detailed(
            self._project_id,
            test_run_id,
            client=self._client.client,
            body=body,
        )
        self._raise_on_error(response)

        assert isinstance(
            response.parsed, api_models.TestparametersListPostResponse
        )
        assert response.parsed.data

    def _delete(self, items: list[dm.TestRunParameter]) -> None:
        """Call only with items with common test_run_id."""
        test_run_id = items[0].test_run_id
        body = self._build_delete_body(items)

        response = delete_test_run_test_parameters.sync_detailed(
            self._project_id,
            test_run_id,
            client=self._client.client,
            body=body,
        )
        self._raise_on_error(response)

    async def _a_delete(self, items: list[dm.TestRunParameter]) -> None:
        """Call only with items with common test_run_id."""
        test_run_id = items[0].test_run_id
        body = self._build_delete_body(items)

        response = await delete_test_run_test_parameters.asyncio_detailed(
            self._project_id,
            test_run_id,
            client=self._client.client,
            body=body,
        )
        self._raise_on_error(response)

    def _build_delete_body(
        self, items: list[dm.TestRunParameter]
    ) -> api_models.TestparametersListDeleteRequest:
        return api_models.TestparametersListDeleteRequest(
            data=[
                api_models.TestparametersListDeleteRequestDataItem(
                    type_=api_models.TestparametersListDeleteRequestDataItemType.TESTPARAMETERS,
                    id=f"{self._project_id}/{item.test_run_id}/{item.name}",
                )
                for item in items
            ]
        )


class TestRecordParameters(
    bc.MultiGetClient[dm.TestRecordParameter],
    bc.CreateClient[dm.TestRecordParameter],
    bc.DeleteClient[dm.TestRecordParameter],
):
    """Clients to handle TestParameters of a TestRecord."""

    _delete_batch_size = 1

    def get_multi(  # type: ignore[override]
        self,
        test_record: dm.TestRecord,
        *,
        page_size: int = 100,
        page_number: int = 1,
        fields: dict[str, str] | None = None,
    ) -> tuple[list[dm.TestRecordParameter], bool]:
        if fields is None:
            fields = self._client.default_fields.testparameters

        sparse_fields = self._build_sparse_fields(fields)
        response = get_test_record_test_parameters.sync_detailed(
            self._project_id,
            test_record.test_run_id,
            test_record.work_item_project_id,
            test_record.work_item_id,
            str(test_record.iteration),
            client=self._client.client,
            fields=sparse_fields,
            pagenumber=page_number,
            pagesize=page_size,
        )

        self._raise_on_error(response)

        return _parse_get_response(response.parsed, test_record)

    async def a_get_multi(  # type: ignore[override]
        self,
        test_record: dm.TestRecord,
        *,
        page_size: int = 100,
        page_number: int = 1,
        fields: dict[str, str] | None = None,
    ) -> tuple[list[dm.TestRecordParameter], bool]:
        if fields is None:
            fields = self._client.default_fields.testparameters

        sparse_fields = self._build_sparse_fields(fields)
        response = await get_test_record_test_parameters.asyncio_detailed(
            self._project_id,
            test_record.test_run_id,
            test_record.work_item_project_id,
            test_record.work_item_id,
            str(test_record.iteration),
            client=self._client.client,
            fields=sparse_fields,
            pagenumber=page_number,
            pagesize=page_size,
        )

        self._raise_on_error(response)

        return _parse_get_response(response.parsed, test_record)

    def _pre_batching_grouping(
        self, items: list[dm.TestRecordParameter]
    ) -> t.Generator[list[dm.TestRecordParameter], None, None]:
        for _, group in itertools.groupby(
            sorted(
                items,
                key=lambda x: (
                    f"{x.test_record.test_run_id}/{x.test_record.work_item_project_id}/{x.test_record.work_item_id}/{x.test_record.iteration}"
                ),
            ),
            lambda x: x.test_record,
        ):
            yield list(group)

    def _create(self, items: list[dm.TestRecordParameter]) -> None:
        """Call only with items with common test_records."""
        test_record = items[0].test_record
        body = _build_post_body(items)

        response = post_test_record_test_parameters.sync_detailed(
            self._project_id,
            test_record.test_run_id,
            test_record.work_item_project_id,
            test_record.work_item_id,
            str(test_record.iteration),
            client=self._client.client,
            body=body,
        )
        self._raise_on_error(response)

    async def _a_create(self, items: list[dm.TestRecordParameter]) -> None:
        """Call only with items with common test_records."""
        test_record = items[0].test_record
        body = _build_post_body(items)

        response = await post_test_record_test_parameters.asyncio_detailed(
            self._project_id,
            test_record.test_run_id,
            test_record.work_item_project_id,
            test_record.work_item_id,
            str(test_record.iteration),
            client=self._client.client,
            body=body,
        )
        self._raise_on_error(response)

    def _delete(self, items: list[dm.TestRecordParameter]) -> None:
        """We expect only one TestRecordParameter for deletion."""
        assert len(items) == 1
        test_record = items[0].test_record

        response = delete_test_record_test_parameter.sync_detailed(
            self._project_id,
            test_record.test_run_id,
            test_record.work_item_project_id,
            test_record.work_item_id,
            str(test_record.iteration),
            items[0].name,
            client=self._client.client,
        )
        self._raise_on_error(response)

    async def _a_delete(self, items: list[dm.TestRecordParameter]) -> None:
        """We expect only one TestRecordParameter for deletion."""
        assert len(items) == 1
        test_record = items[0].test_record

        response = await delete_test_record_test_parameter.asyncio_detailed(
            self._project_id,
            test_record.test_run_id,
            test_record.work_item_project_id,
            test_record.work_item_id,
            str(test_record.iteration),
            items[0].name,
            client=self._client.client,
        )
        self._raise_on_error(response)


@t.overload
def _parse_get_response(
    parsed_response: (
        api_models.TestparametersListGetResponse | api_models.Errors | None
    ),
    scope: dm.TestRecord,
) -> tuple[list[dm.TestRecordParameter], bool]: ...


@t.overload
def _parse_get_response(
    parsed_response: (
        api_models.TestparametersListGetResponse | api_models.Errors | None
    ),
    scope: str,
) -> tuple[list[dm.TestRunParameter], bool]: ...


def _parse_get_response(
    parsed_response: (
        api_models.TestparametersListGetResponse | api_models.Errors | None
    ),
    scope: str | dm.TestRecord,
) -> tuple[list[dm.TestRecordParameter] | list[dm.TestRunParameter], bool]:
    assert isinstance(
        parsed_response, api_models.TestparametersListGetResponse
    )
    next_page = isinstance(
        parsed_response.links, api_models.TestparametersListGetResponseLinks
    ) and bool(parsed_response.links.next_)
    if isinstance(scope, str):
        return [
            dm.TestRunParameter(
                test_run_id=scope,
                name=data.attributes.name or "",
                value=data.attributes.value or "",
            )
            for data in parsed_response.data or []
            if data.attributes
        ], next_page

    return [
        dm.TestRecordParameter(
            test_record=scope,
            name=data.attributes.name or "",
            value=data.attributes.value or "",
        )
        for data in parsed_response.data or []
        if data.attributes
    ], next_page


def _build_post_body(
    items: list[dm.TestRunParameter] | list[dm.TestRecordParameter],
) -> api_models.TestparametersListPostRequest:
    return api_models.TestparametersListPostRequest(
        data=[
            api_models.TestparametersListPostRequestDataItem(
                type_=api_models.TestparametersListPostRequestDataItemType.TESTPARAMETERS,
                attributes=api_models.TestparametersListPostRequestDataItemAttributes(
                    name=item.name, value=item.value
                ),
            )
            for item in items
        ]
    )

# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import itertools
import typing as t

from polarion_rest_api_client import data_models as dm
from polarion_rest_api_client.open_api_client import models as api_models
from polarion_rest_api_client.open_api_client import types as oa_types
from polarion_rest_api_client.open_api_client.api.test_steps import (
    delete_test_steps,
    get_test_steps,
    patch_test_steps,
    post_test_steps,
)

from . import base_classes as bc


class TestSteps(
    bc.MultiGetClient[dm.TestStep],
    bc.UpdateClient[dm.TestStep],
    bc.DeleteClient[dm.TestStep],
    bc.CreateClient[dm.TestStep],
):
    def _update(self, to_update: list[dm.TestStep]) -> None:
        response = patch_test_steps.sync_detailed(
            self._project_id,
            to_update[0].work_item_id,
            client=self._client.client,
            body=self._build_patch_request_data(to_update),
        )
        self._raise_on_error(response)

    async def _async_update(self, to_update: list[dm.TestStep]) -> None:
        response = await patch_test_steps.asyncio_detailed(
            self._project_id,
            to_update[0].work_item_id,
            client=self._client.client,
            body=self._build_patch_request_data(to_update),
        )
        self._raise_on_error(response)

    def get_multi(  # type: ignore[override]
        self,
        work_item_id: str,
        *,
        page_size: int = 100,
        page_number: int = 1,
        fields: dict[str, str] | None = None,
        revision: str | None = None,
    ) -> tuple[list[dm.TestStep], bool]:
        if fields is None:
            fields = self._client.default_fields.teststeps

        sparse_fields = self._build_sparse_fields(fields)
        response = get_test_steps.sync_detailed(
            self._project_id,
            work_item_id,
            client=self._client.client,
            fields=sparse_fields,
            pagenumber=page_number,
            pagesize=page_size,
            revision=revision or oa_types.UNSET,
        )
        return self._parse_get_response(response)

    async def async_get_multi(  # type: ignore[override]
        self,
        work_item_id: str,
        *,
        page_size: int = 100,
        page_number: int = 1,
        fields: dict[str, str] | None = None,
        revision: str | None = None,
    ) -> tuple[list[dm.TestStep], bool]:
        if fields is None:
            fields = self._client.default_fields.teststeps

        sparse_fields = self._build_sparse_fields(fields)
        response = await get_test_steps.asyncio_detailed(
            self._project_id,
            work_item_id,
            client=self._client.client,
            fields=sparse_fields,
            pagenumber=page_number,
            pagesize=page_size,
            revision=revision or oa_types.UNSET,
        )
        return self._parse_get_response(response)

    def _parse_get_response(
        self,
        response: oa_types.Response[
            api_models.TeststepsListGetResponse | api_models.Errors
        ],
    ) -> tuple[list[dm.TestStep], bool]:
        self._raise_on_error(response)
        parsed_response = response.parsed
        assert isinstance(parsed_response, api_models.TeststepsListGetResponse)
        test_steps = [
            dm.TestStep(
                work_item_id=data.id.split("/")[1],
                step_index=int(data.id.split("/")[2]),
                revision=data.revision if data.revision else None,
                step_columns=self._make_step_columns(data.attributes),
            )
            for data in parsed_response.data or []
            if isinstance(data.id, str)
        ]
        next_page = isinstance(
            parsed_response.links, api_models.TeststepsListGetResponseLinks
        ) and bool(parsed_response.links.next_)
        return test_steps, next_page

    def _make_step_columns(
        self,
        attributes: (
            api_models.TeststepsListGetResponseDataItemAttributes
            | oa_types.Unset
        ),
    ) -> dict[str, dm.TextContent]:
        if isinstance(attributes, oa_types.Unset):
            return {}

        keys = attributes.keys or []
        values = [
            dm.TextContent(
                val.type_.value if val.type_ else "text/plain",
                val.value or None,
            )
            for val in attributes.values or []
        ]
        assert len(keys) == len(values)
        return dict(zip(keys, values, strict=False))

    def _pre_batching_grouping(
        self, items: list[dm.TestStep]
    ) -> t.Generator[list[dm.TestStep], None, None]:
        for _, group in itertools.groupby(items, lambda x: x.work_item_id):
            yield list(group)

    def _create(self, items: list[dm.TestStep]) -> None:
        response = post_test_steps.sync_detailed(
            self._project_id,
            items[0].work_item_id,
            client=self._client.client,
            body=self._build_post_request_data(items),
        )
        self._process_post_response(items, response)

    async def _async_create(self, items: list[dm.TestStep]) -> None:
        response = await post_test_steps.asyncio_detailed(
            self._project_id,
            items[0].work_item_id,
            client=self._client.client,
            body=self._build_post_request_data(items),
        )
        self._process_post_response(items, response)

    def _process_post_response(
        self,
        items: list[dm.TestStep],
        response: oa_types.Response[
            api_models.TeststepsListPostResponse | api_models.Errors
        ],
    ) -> None:
        self._raise_on_error(response)
        parsed_response = response.parsed
        assert isinstance(
            parsed_response, api_models.TeststepsListPostResponse
        )
        assert parsed_response.data
        for idx, response_item in enumerate(parsed_response.data):
            if response_item.id:
                items[idx].step_index = int(response_item.id.split("/")[-1])

    def _delete(self, items: list[dm.TestStep]) -> None:
        response = delete_test_steps.sync_detailed(
            self._project_id,
            items[0].work_item_id,
            client=self._client.client,
            body=self._build_delete_body(items),
        )
        self._raise_on_error(response)

    async def _async_delete(self, items: list[dm.TestStep]) -> None:
        response = await delete_test_steps.asyncio_detailed(
            self._project_id,
            items[0].work_item_id,
            client=self._client.client,
            body=self._build_delete_body(items),
        )
        self._raise_on_error(response)

    def _build_delete_body(
        self, items: list[dm.TestStep]
    ) -> api_models.TeststepsListDeleteRequest:
        return api_models.TeststepsListDeleteRequest(
            data=[
                api_models.TeststepsListDeleteRequestDataItem(
                    type_=api_models.TeststepsListDeleteRequestDataItemType.TESTSTEPS,
                    id=f"{self._project_id}/{step.work_item_id}/{step.step_index}",
                )
                for step in items
            ]
        )

    def _fill_test_step_attributes(
        self,
        attributes_type: type[
            api_models.TeststepsListPostRequestDataItemAttributes
            | api_models.TeststepsListPatchRequestDataItemAttributes
        ],
        test_step: dm.TestStep,
    ) -> (
        api_models.TeststepsListPostRequestDataItemAttributes
        | api_models.TeststepsListPatchRequestDataItemAttributes
    ):
        value_item_cls = getattr(
            api_models, f"{attributes_type.__name__}ValuesItem"
        )
        value_item_type = getattr(
            api_models, f"{attributes_type.__name__}ValuesItemType"
        )

        return attributes_type(
            keys=list(test_step.step_columns.keys()),
            values=[
                value_item_cls(
                    type_=(
                        value_item_type.TEXTHTML
                        if col.type == "text/html"
                        else value_item_type.TEXTPLAIN
                    ),
                    value=col.value,
                )
                for col in test_step.step_columns.values()
            ],
        )

    def _build_patch_request_data(
        self, items: list[dm.TestStep]
    ) -> api_models.TeststepsListPatchRequest:
        return api_models.TeststepsListPatchRequest(
            data=[
                api_models.TeststepsListPatchRequestDataItem(
                    type_=api_models.TeststepsListPatchRequestDataItemType.TESTSTEPS,
                    id=(
                        f"{self._project_id}/{step.work_item_id}/{step.step_index}"
                        if step.step_index
                        else oa_types.UNSET
                    ),
                    attributes=t.cast(
                        api_models.TeststepsListPatchRequestDataItemAttributes,
                        self._fill_test_step_attributes(
                            api_models.TeststepsListPatchRequestDataItemAttributes,
                            step,
                        ),
                    ),
                )
                for step in items
            ]
        )

    def _build_post_request_data(
        self, items: list[dm.TestStep]
    ) -> api_models.TeststepsListPostRequest:
        return api_models.TeststepsListPostRequest(
            data=[
                api_models.TeststepsListPostRequestDataItem(
                    type_=api_models.TeststepsListPostRequestDataItemType.TESTSTEPS,
                    attributes=t.cast(
                        api_models.TeststepsListPostRequestDataItemAttributes,
                        self._fill_test_step_attributes(
                            api_models.TeststepsListPostRequestDataItemAttributes,
                            step,
                        ),
                    ),
                )
                for step in items
            ]
        )

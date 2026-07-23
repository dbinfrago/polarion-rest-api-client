# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import itertools
import typing as t

from polarion_rest_api_client import data_models as dm
from polarion_rest_api_client.open_api_client import models as api_models
from polarion_rest_api_client.open_api_client import types as oa_types
from polarion_rest_api_client.open_api_client.api.test_records import (
    delete_test_record,
    get_test_record,
    get_test_records,
    patch_test_record,
    post_test_records,
)

from . import base_classes as bc
from . import test_parameters

if t.TYPE_CHECKING:
    from polarion_rest_api_client import client as polarion_client

AttributesType = t.TypeVar(
    "AttributesType",
    bound=api_models.TestrecordsListPostRequestDataItemAttributes
    | api_models.TestrecordsSinglePatchRequestDataAttributes,
)


class TestRecords(
    bc.CreateClient[dm.TestRecord],
    bc.MultiGetClient[dm.TestRecord],
    bc.DeleteClient[dm.TestRecord],
    bc.UpdateClient[dm.TestRecord],
):
    _update_batch_size = 1

    def __init__(
        self, project_id: str, client: polarion_client.PolarionClient
    ):
        super().__init__(project_id, client)
        self.parameters = test_parameters.TestRecordParameters(
            project_id, client
        )

    def _update(self, to_update: list[dm.TestRecord]) -> None:
        assert len(to_update) == 1, "Expected only one item"
        item = to_update[0]
        response = patch_test_record.sync_detailed(
            self._project_id,
            item.test_run_id,
            item.work_item_project_id,
            item.work_item_id,
            str(item.iteration),
            client=self._client.client,
            body=self._build_patch_body(item),
        )
        self._raise_on_error(response)

    async def _async_update(self, to_update: list[dm.TestRecord]) -> None:
        assert len(to_update) == 1, "Expected only one item"
        item = to_update[0]
        response = await patch_test_record.asyncio_detailed(
            self._project_id,
            item.test_run_id,
            item.work_item_project_id,
            item.work_item_id,
            str(item.iteration),
            client=self._client.client,
            body=self._build_patch_body(item),
        )
        self._raise_on_error(response)

    def _build_patch_body(
        self, to_update: dm.TestRecord
    ) -> api_models.TestrecordsSinglePatchRequest:
        # pylint: disable=line-too-long
        return api_models.TestrecordsSinglePatchRequest(
            data=api_models.TestrecordsSinglePatchRequestData(
                type_=api_models.TestrecordsSinglePatchRequestDataType.TESTRECORDS,
                id=f"{self._project_id}/{to_update.test_run_id}/{to_update.work_item_project_id}/{to_update.work_item_id}/{to_update.iteration}",
                attributes=self._fill_test_record_attributes(
                    api_models.TestrecordsSinglePatchRequestDataAttributes,
                    to_update,
                ),
                relationships=api_models.TestrecordsSinglePatchRequestDataRelationships(
                    executed_by=api_models.TestrecordsSinglePatchRequestDataRelationshipsExecutedBy(
                        data=api_models.TestrecordsSinglePatchRequestDataRelationshipsExecutedByData(
                            type_=api_models.TestrecordsSinglePatchRequestDataRelationshipsExecutedByDataType.USERS,
                            id=to_update.executed_by,
                        )
                    ),
                )
                if to_update.executed_by is not None
                else oa_types.UNSET,
            )
        )
        # pylint: enable=line-too-long

    def get_multi(  # type: ignore[override]
        self,
        test_run_id: str,
        *,
        page_size: int = 100,
        page_number: int = 1,
        fields: dict[str, str] | None = None,
        include: str | None = None,
        test_result_id: str | None = None,
    ) -> tuple[list[dm.TestRecord], bool]:
        if fields is None:
            fields = self._client.default_fields.testrecords

        sparse_fields = self._build_sparse_fields(fields)
        response = get_test_records.sync_detailed(
            self._project_id,
            test_run_id,
            client=self._client.client,
            fields=sparse_fields,
            include=include or oa_types.UNSET,
            pagenumber=page_number,
            pagesize=page_size,
            test_result_id=test_result_id or oa_types.UNSET,
        )
        return self._parse_get_response(response, test_run_id)

    async def async_get_multi(  # type: ignore[override]
        self,
        test_run_id: str,
        *,
        page_size: int = 100,
        page_number: int = 1,
        fields: dict[str, str] | None = None,
        include: str | None = None,
        test_result_id: str | None = None,
    ) -> tuple[list[dm.TestRecord], bool]:
        if fields is None:
            fields = self._client.default_fields.testrecords

        sparse_fields = self._build_sparse_fields(fields)
        response = await get_test_records.asyncio_detailed(
            self._project_id,
            test_run_id,
            client=self._client.client,
            fields=sparse_fields,
            include=include or oa_types.UNSET,
            pagenumber=page_number,
            pagesize=page_size,
            test_result_id=test_result_id or oa_types.UNSET,
        )
        return self._parse_get_response(response, test_run_id)

    def get(
        self,
        test_run_id: str,
        work_item_project_id: str,
        work_item_id: str,
        iteration: int,
        *,
        fields: dict[str, str] | None = None,
        include: str | None = None,
    ) -> dm.TestRecord | None:
        if fields is None:
            fields = self._client.default_fields.testrecords

        sparse_fields = self._build_sparse_fields(fields)
        response = get_test_record.sync_detailed(
            self._project_id,
            test_run_id,
            work_item_project_id,
            work_item_id,
            str(iteration),
            client=self._client.client,
            fields=sparse_fields,
            include=include or oa_types.UNSET,
        )
        return self._parse_single_get_response(response, test_run_id)

    async def async_get(
        self,
        test_run_id: str,
        work_item_project_id: str,
        work_item_id: str,
        iteration: int,
        *,
        fields: dict[str, str] | None = None,
        include: str | None = None,
    ) -> dm.TestRecord | None:
        if fields is None:
            fields = self._client.default_fields.testrecords

        sparse_fields = self._build_sparse_fields(fields)
        response = await get_test_record.asyncio_detailed(
            self._project_id,
            test_run_id,
            work_item_project_id,
            work_item_id,
            str(iteration),
            client=self._client.client,
            fields=sparse_fields,
            include=include or oa_types.UNSET,
        )
        return self._parse_single_get_response(response, test_run_id)

    def _parse_get_response(
        self, response: oa_types.Response, test_run_id: str
    ) -> tuple[list[dm.TestRecord], bool]:
        self._raise_on_error(response)
        parsed_response = response.parsed
        assert isinstance(
            parsed_response, api_models.TestrecordsListGetResponse
        )
        user_names = self._user_names_from_included(parsed_response.included)
        test_records = [
            self._generate_test_record(data, test_run_id, user_names)
            for data in parsed_response.data or []
        ]
        next_page = isinstance(
            parsed_response.links,
            api_models.TestrecordsListGetResponseLinks,
        ) and bool(parsed_response.links.next_)
        return test_records, next_page

    def _parse_single_get_response(
        self, response: oa_types.Response, test_run_id: str
    ) -> dm.TestRecord | None:
        self._raise_on_error(response)
        parsed_response = response.parsed
        if isinstance(
            parsed_response, api_models.TestrecordsSingleGetResponse
        ) and isinstance(
            parsed_response.data, api_models.TestrecordsSingleGetResponseData
        ):
            user_names = self._user_names_from_included(
                parsed_response.included
            )
            return self._generate_test_record(
                parsed_response.data, test_run_id, user_names
            )
        return None

    def _generate_test_record(
        self,
        data: (
            api_models.TestrecordsListGetResponseDataItem
            | api_models.TestrecordsSingleGetResponseData
        ),
        test_run_id: str,
        user_names: dict[str, str],
    ) -> dm.TestRecord:
        assert isinstance(data.id, str)
        assert not isinstance(data.attributes, oa_types.Unset)
        assert data.attributes is not None
        _, _, project_id, work_item, iteration = data.id.split("/")
        executed_by = None
        additional_attributes = dict(data.additional_properties or {})
        if data.relationships:
            if (
                (defect := data.relationships.defect)
                and defect.data
                and defect.data.id
            ):
                additional_attributes["defect"] = defect.data.id
            if (
                (ex_by := data.relationships.executed_by)
                and ex_by.data
                and ex_by.data.id
            ):
                executed_by = ex_by.data.id
                self._resolve_named_user_relationship(
                    additional_attributes,
                    "executed_by",
                    data.relationships.executed_by,
                    user_names,
                )

        return dm.TestRecord(
            test_run_id=test_run_id,
            work_item_project_id=project_id,
            work_item_id=work_item,
            work_item_revision=self.unset_to_none(
                data.attributes.test_case_revision
            ),
            iteration=int(iteration),
            duration=(
                data.attributes.duration
                if not isinstance(data.attributes.duration, oa_types.Unset)
                else -1
            ),
            result=self.unset_to_none(data.attributes.result),
            comment=self._handle_text_content(data.attributes.comment),
            executed=self.unset_to_none(data.attributes.executed),
            executed_by=executed_by,
            additional_attributes=additional_attributes,
        )

    def _pre_batching_grouping(
        self, items: list[dm.TestRecord]
    ) -> t.Generator[list[dm.TestRecord], None, None]:
        for _, group in itertools.groupby(items, lambda x: x.test_run_id):
            yield list(group)

    def _create(
        self,
        items: list[dm.TestRecord],
    ) -> None:
        """Create the given list of test records."""
        response = post_test_records.sync_detailed(
            self._project_id,
            items[0].test_run_id,
            client=self._client.client,
            # pylint: disable=line-too-long
            body=self._build_post_body(items),
            # pylint: enable=line-too-long
        )

        self._parse_post_response(items, response)

    async def _async_create(
        self,
        items: list[dm.TestRecord],
    ) -> None:
        """Create the given list of test records."""
        response = await post_test_records.asyncio_detailed(
            self._project_id,
            items[0].test_run_id,
            client=self._client.client,
            body=self._build_post_body(items),
        )
        self._parse_post_response(items, response)

    def _parse_post_response(
        self, items: list[dm.TestRecord], response: oa_types.Response
    ) -> None:
        self._raise_on_error(response)
        assert isinstance(
            response.parsed, api_models.TestrecordsListPostResponse
        )
        assert response.parsed.data
        counter = 0
        for response_item in response.parsed.data:
            if response_item.id:
                items[counter].iteration = int(response_item.id.split("/")[-1])
                counter += 1

    def _build_post_body(
        self, items: list[dm.TestRecord]
    ) -> api_models.TestrecordsListPostRequest:
        # pylint: disable=line-too-long
        return api_models.TestrecordsListPostRequest(
            [
                api_models.TestrecordsListPostRequestDataItem(
                    type_=api_models.TestrecordsListPostRequestDataItemType.TESTRECORDS,
                    attributes=self._fill_test_record_attributes(
                        api_models.TestrecordsListPostRequestDataItemAttributes,
                        test_record,
                    ),
                    relationships=api_models.TestrecordsListPostRequestDataItemRelationships(
                        test_case=api_models.TestrecordsListPostRequestDataItemRelationshipsTestCase(
                            data=api_models.TestrecordsListPostRequestDataItemRelationshipsTestCaseData(
                                type_=api_models.TestrecordsListPostRequestDataItemRelationshipsTestCaseDataType.WORKITEMS,
                                id=f"{test_record.work_item_project_id}/{test_record.work_item_id}",
                            )
                        ),
                        executed_by=api_models.TestrecordsListPostRequestDataItemRelationshipsExecutedBy(
                            data=api_models.TestrecordsListPostRequestDataItemRelationshipsExecutedByData(
                                type_=api_models.TestrecordsListPostRequestDataItemRelationshipsExecutedByDataType.USERS,
                                id=test_record.executed_by,
                            )
                        )
                        if test_record.executed_by is not None
                        else oa_types.UNSET,
                    ),
                )
                for test_record in items
            ]
        )
        # pylint: enable=line-too-long

    def _delete(self, items: list[dm.TestRecord]) -> None:
        assert len(items) == 1, "Expected only one item"
        item = items[0]
        response = delete_test_record.sync_detailed(
            self._project_id,
            item.test_run_id,
            item.work_item_project_id,
            item.work_item_id,
            str(item.iteration),
            client=self._client.client,
        )
        self._raise_on_error(response)

    async def _async_delete(self, items: list[dm.TestRecord]) -> None:
        assert len(items) == 1, "Expected only one item"
        item = items[0]
        response = await delete_test_record.asyncio_detailed(
            self._project_id,
            item.test_run_id,
            item.work_item_project_id,
            item.work_item_id,
            str(item.iteration),
            client=self._client.client,
        )
        self._raise_on_error(response)

    def _fill_test_record_attributes(
        self,
        attributes_type: type[AttributesType],
        test_record: dm.TestRecord,
    ) -> AttributesType:
        type_prefix = attributes_type.__name__
        attributes = attributes_type()
        if test_record.result:
            attributes.result = test_record.result
        if test_record.comment:
            attributes.comment = getattr(api_models, f"{type_prefix}Comment")()
            assert attributes.comment
            if test_record.comment.type:
                attributes.comment.type_ = getattr(
                    api_models, f"{type_prefix}CommentType"
                )(test_record.comment.type)
            if test_record.comment.value:
                attributes.comment.value = test_record.comment.value
        if test_record.duration != -1:
            attributes.duration = test_record.duration
        if test_record.work_item_revision:
            attributes.test_case_revision = test_record.work_item_revision
        if test_record.executed:
            attributes.executed = test_record.executed
        if test_record.additional_attributes:
            attributes.additional_properties = (
                test_record.additional_attributes
            )
        return t.cast(AttributesType, attributes)

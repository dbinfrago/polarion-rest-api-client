# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import typing as t

from polarion_rest_api_client import data_models as dm
from polarion_rest_api_client.open_api_client import models as api_models
from polarion_rest_api_client.open_api_client import types as oa_types
from polarion_rest_api_client.open_api_client.api.test_step_results import (
    get_test_step_result,
    get_test_step_results,
    patch_test_step_result,
    post_test_step_results,
)

from . import base_classes as bc


class TestStepResults(
    bc.SingleGetClient[dm.TestStepResult],
    bc.UpdateClient[dm.TestStepResult],
    bc.CreateClient[dm.TestStepResult],
    bc.MultiGetClient[dm.TestStepResult],
):
    def get(self, to_get: dm.TestStepResult) -> dm.TestStepResult:
        """Get a Test Step Result for a test case."""

        response = get_test_step_result.sync_detailed(
            self._project_id,
            to_get.test_run_id,
            to_get.test_case_project_id,
            to_get.test_case_id,
            to_get.iteration,
            to_get.test_step_index,
            client=self._client.client,
        )
        self._raise_on_error(response)

        parsed_response = response.parsed

        assert isinstance(
            parsed_response, api_models.TeststepResultsSingleGetResponse
        )
        data = parsed_response.data
        assert isinstance(
            data, api_models.TeststepResultsSingleGetResponseData
        )
        attributes = data.attributes

        if isinstance(attributes, oa_types.Unset):
            result_val = None
            comment_val = None
        else:
            result_val = self.unset_to_none(attributes.result)

            comment_val = (
                dm.TextContent(
                    str(attributes.comment.type_),
                    self.unset_to_none(attributes.comment.value),
                )
                if attributes.comment
                and (
                    attributes.comment is not oa_types.UNSET
                    and attributes.comment.type_ is not oa_types.UNSET
                    and attributes.comment.value is not oa_types.UNSET
                )
                else None
            )

        return dm.TestStepResult(
            test_case_id=to_get.test_case_id,
            test_step_index=to_get.test_step_index,
            iteration=to_get.iteration,
            test_run_id=to_get.test_run_id,
            test_case_project_id=to_get.test_case_project_id,
            result=result_val,
            comment=comment_val,
        )

    async def async_get(
        self, to_get: dm.TestStepResult
    ) -> dm.TestStepResult | None:
        """Async Get a Test Step Result for a test case."""

        response = await get_test_step_result.asyncio_detailed(
            self._project_id,
            to_get.test_run_id,
            to_get.test_case_project_id,
            to_get.test_case_id,
            to_get.iteration,
            to_get.test_step_index,
            client=self._client.client,
        )
        self._raise_on_error(response)

        parsed_response = response.parsed

        assert isinstance(
            parsed_response, api_models.TeststepResultsSingleGetResponse
        )
        data = parsed_response.data
        assert isinstance(
            data, api_models.TeststepResultsSingleGetResponseData
        )
        attributes = data.attributes

        if isinstance(attributes, oa_types.Unset):
            result_val = None
            comment_val = None
        else:
            result_val = self.unset_to_none(attributes.result)

            comment_val = (
                dm.TextContent(
                    str(attributes.comment.type_),
                    self.unset_to_none(attributes.comment.value),
                )
                if attributes.comment
                and (
                    attributes.comment is not oa_types.UNSET
                    and attributes.comment.type_ is not oa_types.UNSET
                    and attributes.comment.value is not oa_types.UNSET
                )
                else None
            )

        return dm.TestStepResult(
            test_case_id=to_get.test_case_id,
            test_step_index=to_get.test_step_index,
            iteration=to_get.iteration,
            test_run_id=to_get.test_run_id,
            test_case_project_id=to_get.test_case_project_id,
            result=result_val,
            comment=comment_val,
        )

    def _update(self, to_update: list[dm.TestStepResult]) -> None:
        """Update a Test Step Result for a test case."""
        assert len(to_update) == 1, "Expected only one item"
        body_data = self._build_single_patch_request_data(to_update[0])
        body = api_models.TeststepResultsSinglePatchRequest(data=body_data)
        response = patch_test_step_result.sync_detailed(
            project_id=self._project_id,
            test_run_id=to_update[0].test_run_id,
            test_case_project_id=to_update[0].test_case_project_id,
            test_case_id=to_update[0].test_case_id,
            iteration=to_update[0].iteration,
            test_step_index=to_update[0].test_step_index,
            client=self._client.client,
            body=body,
        )
        self._raise_on_error(response)

    async def _async_update(self, to_update: list[dm.TestStepResult]) -> None:
        """Async Update a Test Step Result for a test case."""
        assert len(to_update) == 1, "Expected only one item"
        body_data = self._build_single_patch_request_data(to_update[0])
        body = api_models.TeststepResultsSinglePatchRequest(data=body_data)
        response = await patch_test_step_result.asyncio_detailed(
            project_id=self._project_id,
            test_run_id=to_update[0].test_run_id,
            test_case_project_id=to_update[0].test_case_project_id,
            test_case_id=to_update[0].test_case_id,
            iteration=to_update[0].iteration,
            test_step_index=to_update[0].test_step_index,
            client=self._client.client,
            body=body,
        )
        self._raise_on_error(response)

    def _create(self, to_update: list[dm.TestStepResult]) -> None:
        """Create Test Step Results for a test case."""
        body_data = self._build_post_request_data(to_update)
        body = api_models.TeststepResultsListPostRequest(data=body_data)

        response = post_test_step_results.sync_detailed(
            project_id=self._project_id,
            test_run_id=to_update[0].test_run_id,
            test_case_project_id=to_update[0].test_case_project_id,
            test_case_id=to_update[0].test_case_id,
            iteration=to_update[0].iteration,
            client=self._client.client,
            body=body,
        )
        self._raise_on_error(response)

    async def _async_create(self, to_update: list[dm.TestStepResult]) -> None:
        """Async Create Test Step Results for a test case."""
        body_data = self._build_post_request_data(to_update)
        body = api_models.TeststepResultsListPostRequest(data=body_data)

        response = await post_test_step_results.asyncio_detailed(
            project_id=self._project_id,
            test_run_id=to_update[0].test_run_id,
            test_case_project_id=to_update[0].test_case_project_id,
            test_case_id=to_update[0].test_case_id,
            iteration=to_update[0].iteration,
            client=self._client.client,
            body=body,
        )
        self._raise_on_error(response)

    def get_multi(  # type: ignore[override]
        self,
        items: list[dm.TestStepResult],
        page_size: int = 100,
        page_number: int = 1,
        fields: dict[str, str] | None = None,
        revision: str | None = None,
    ) -> tuple[list[dm.TestStepResult], bool]:
        """Get multiple Test Step Results for a test case."""

        if fields is None:
            fields = self._client.default_fields.teststep_results

        sparse_fields = self._build_sparse_fields(fields)

        response = get_test_step_results.sync_detailed(
            project_id=items[0].test_case_project_id,
            test_run_id=items[0].test_run_id,
            test_case_project_id=items[0].test_case_project_id,
            test_case_id=items[0].test_case_id,
            iteration=items[0].iteration,
            client=self._client.client,
            fields=sparse_fields,
            pagenumber=page_number,
            pagesize=page_size,
            revision=revision or oa_types.UNSET,
        )

        self._raise_on_error(response)

        parsed_response = response.parsed

        test_step_results: list[dm.TestStepResult] = []
        next_page = False

        if (
            isinstance(
                parsed_response, api_models.TeststepResultsListGetResponse
            )
            and parsed_response.data
        ):
            for item in parsed_response.data:
                assert isinstance(
                    item, api_models.TeststepResultsListGetResponseDataItem
                )

                attributes = item.attributes

                assert isinstance(
                    attributes,
                    api_models.TeststepResultsListGetResponseDataItemAttributes,
                )
                assert isinstance(item.id, str)

                _, _, _, _, iteration, test_step_index = item.id.split("/")

                testStep_Result = dm.TestStepResult(
                    test_case_id=items[0].test_case_id,
                    test_step_index=test_step_index,
                    iteration=iteration,
                    test_run_id=items[0].test_run_id,
                    test_case_project_id=items[0].test_case_project_id,
                    result=self.unset_to_none(attributes.result),
                    comment=(
                        dm.TextContent(
                            str(attributes.comment.type_),
                            self.unset_to_none(attributes.comment.value),
                        )
                        if attributes.comment
                        else None
                    ),
                )

                teststepResults.append(testStep_Result)

            next_page = isinstance(
                parsed_response.links,
                api_models.TeststepResultsListGetResponseLinks,
            ) and bool(parsed_response.links.next_)

        return teststepResults, next_page

    async def async_get_multi(  # type: ignore[override]
        self,
        items: list[dm.TestStepResult],
        page_size: int = 100,
        page_number: int = 1,
        fields: dict[str, str] | None = None,
        revision: str | None = None,
    ) -> tuple[list[dm.TestStepResult], bool]:
        """Async Get multiple Test Step Results for a test case."""
        if fields is None:
            fields = self._client.default_fields.teststep_results
        sparse_fields = self._build_sparse_fields(fields)

        response = await get_test_step_results.asyncio_detailed(
            project_id=items[0].test_case_project_id,
            test_run_id=items[0].test_run_id,
            test_case_project_id=items[0].test_case_project_id,
            test_case_id=items[0].test_case_id,
            iteration=items[0].iteration,
            client=self._client.client,
            fields=sparse_fields,
            pagenumber=page_number,
            pagesize=page_size,
            revision=revision or oa_types.UNSET,
        )

        self._raise_on_error(response)

        parsed_response = response.parsed
        teststepResults: list[dm.TestStepResult] = []
        next_page = False
        if (
            isinstance(
                parsed_response, api_models.TeststepResultsListGetResponse
            )
            and parsed_response.data
        ):
            for item in parsed_response.data:
                assert isinstance(
                    item, api_models.TeststepResultsListGetResponseDataItem
                )

                attributes = item.attributes

                assert isinstance(
                    attributes,
                    api_models.TeststepResultsListGetResponseDataItemAttributes,
                )
                assert isinstance(item.id, str)

                _, _, _, _, iteration, test_step_index = item.id.split("/")

                testStep_Result = dm.TestStepResult(
                    test_case_id=items[0].test_case_id,
                    test_step_index=test_step_index,
                    iteration=iteration,
                    test_run_id=items[0].test_run_id,
                    test_case_project_id=items[0].test_case_project_id,
                    result=self.unset_to_none(attributes.result),
                    comment=(
                        dm.TextContent(
                            str(attributes.comment.type_),
                            self.unset_to_none(attributes.comment.value),
                        )
                        if attributes.comment
                        else None
                    ),
                )

                teststepResults.append(testStep_Result)

            next_page = isinstance(
                parsed_response.links,
                api_models.TeststepResultsListGetResponseLinks,
            ) and bool(parsed_response.links.next_)

        return teststepResults, next_page

    def _fill_teststep_result_attributes(
        self,
        attributes_type: type[
            api_models.TeststepResultsListPostRequestDataItemAttributes
            | api_models.TeststepResultsSinglePatchRequestDataAttributes
        ],
        teststep_Result: dm.TestStepResult,
    ) -> (
        api_models.TeststepResultsListPostRequestDataItemAttributes
        | api_models.TeststepResultsSinglePatchRequestDataAttributes
    ):
        # Dynamically get the comment class and type enum based on attributes_type
        comment_item_cls = getattr(
            api_models, f"{attributes_type.__name__}Comment"
        )

        comment_item_type_enum = getattr(
            api_models, f"{attributes_type.__name__}CommentType"
        )

        comment_item_type = comment_item_type_enum.TEXTPLAIN
        comment_value = None

        if isinstance(teststep_Result.comment, dm.TextContent):
            comment_value = teststep_Result.comment.value
            # Convert string type to appropriate enum value
            comment_item_type = comment_item_type_enum(
                teststep_Result.comment.type
            )
        else:
            comment_value = teststep_Result.comment

        return attributes_type(
            result=teststep_Result.result
            if teststep_Result.result is not None
            else oa_types.UNSET,
            comment=comment_item_cls(
                type_=comment_item_type,
                value=comment_value,
            )
            if comment_value is not None
            else oa_types.UNSET,
        )

    def _build_single_patch_request_data(
        self, stepResult: dm.TestStepResult
    ) -> api_models.TeststepResultsSinglePatchRequestData:
        return api_models.TeststepResultsSinglePatchRequestData(
            type_=api_models.TeststepResultsSinglePatchRequestDataType.TESTSTEP_RESULTS,
            id=(
                f"{stepResult.test_case_project_id}/{stepResult.test_run_id}/{stepResult.test_case_project_id}/{stepResult.test_case_id}/{stepResult.iteration}/{stepResult.test_step_index}"
                if stepResult.test_step_index is not None
                else oa_types.UNSET
            ),
            attributes=t.cast(
                api_models.TeststepResultsSinglePatchRequestDataAttributes,
                self._fill_teststep_result_attributes(
                    api_models.TeststepResultsSinglePatchRequestDataAttributes,
                    stepResult,
                ),
            ),
        )

    def _build_post_request_data(
        self, items: list[dm.TestStepResult]
    ) -> list[api_models.TeststepResultsListPostRequestDataItem]:
        return [
            api_models.TeststepResultsListPostRequestDataItem(
                type_=api_models.TeststepResultsListPostRequestDataItemType.TESTSTEP_RESULTS,
                attributes=t.cast(
                    api_models.TeststepResultsListPostRequestDataItemAttributes,
                    self._fill_teststep_result_attributes(
                        api_models.TeststepResultsListPostRequestDataItemAttributes,
                        stepResult,
                    ),
                ),
            )
            for stepResult in items
        ]

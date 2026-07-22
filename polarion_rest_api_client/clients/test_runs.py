# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

import typing as t

from polarion_rest_api_client import data_models as dm
from polarion_rest_api_client.open_api_client import models as api_models
from polarion_rest_api_client.open_api_client import types as oa_types
from polarion_rest_api_client.open_api_client.api.test_runs import (
    delete_test_runs,
    get_test_run,
    get_test_runs,
    patch_test_run,
    post_test_runs,
)

from . import base_classes as bc
from . import test_parameters, test_records

if t.TYPE_CHECKING:
    from polarion_rest_api_client import client as polarion_client

AttributesType = t.TypeVar(
    "AttributesType",
    bound=api_models.TestrunsListPostRequestDataItemAttributes
    | api_models.TestrunsSinglePatchRequestDataAttributes,
)

# Keys already surfaced as dedicated dm.TestRun fields; excluded from the
# additional_attributes bag to avoid duplicating them.
_TYPED_TEST_RUN_ATTRIBUTE_KEYS: t.Final = frozenset(
    {
        "id",
        "type",
        "status",
        "title",
        "homePageContent",
        "finishedOn",
        "groupId",
        "idPrefix",
        "isTemplate",
        "keepInHistory",
        "query",
        "useReportFromTemplate",
        "selectTestCasesBy",
    }
)


class TestRuns(
    bc.MultiGetClient[dm.TestRun],
    bc.SingleGetClient[dm.TestRun],
    bc.UpdateClient[dm.TestRun],
    bc.CreateClient[dm.TestRun],
    bc.DeleteClient[dm.TestRun],
):
    _update_batch_size = 1

    def __init__(
        self, project_id: str, client: "polarion_client.PolarionClient"
    ):
        super().__init__(project_id, client)
        self.records = test_records.TestRecords(project_id, client)
        self.parameters = test_parameters.TestRunParameters(project_id, client)

    def _update(self, to_update: list[dm.TestRun]) -> None:
        """Create the given list of test runs."""
        assert len(to_update) == 1, "Expected only one item"
        assert to_update[0].id
        response = patch_test_run.sync_detailed(
            self._project_id,
            to_update[0].id,
            client=self._client.client,
            body=api_models.TestrunsSinglePatchRequest(
                data=api_models.TestrunsSinglePatchRequestData(
                    type_=api_models.TestrunsSinglePatchRequestDataType.TESTRUNS,  # pylint: disable=line-too-long
                    id=f"{self._project_id}/{to_update[0].id}",
                    attributes=self._fill_test_run_attributes(
                        api_models.TestrunsSinglePatchRequestDataAttributes,
                        to_update[0],
                    ),
                )
            ),
        )

        self._raise_on_error(response)

    async def _async_update(self, to_update: list[dm.TestRun]) -> None:
        """Create the given list of test runs."""
        assert len(to_update) == 1, "Expected only one item"
        assert to_update[0].id
        response = await patch_test_run.asyncio_detailed(
            self._project_id,
            to_update[0].id,
            client=self._client.client,
            body=api_models.TestrunsSinglePatchRequest(
                data=api_models.TestrunsSinglePatchRequestData(
                    type_=api_models.TestrunsSinglePatchRequestDataType.TESTRUNS,  # pylint: disable=line-too-long
                    id=f"{self._project_id}/{to_update[0].id}",
                    attributes=self._fill_test_run_attributes(
                        api_models.TestrunsSinglePatchRequestDataAttributes,
                        to_update[0],
                    ),
                )
            ),
        )

        self._raise_on_error(response)

    def get_multi(  # type: ignore[override]
        self,
        query: str = "",
        *,
        page_size: int = 100,
        page_number: int = 1,
        fields: dict[str, str] | None = None,
        include: str | None = None,
    ) -> tuple[list[dm.TestRun], bool]:
        """Return the test runs on a defined page matching the given query.

        In addition, a flag whether a next page is available is
        returned. Define a fields dictionary as described in the
        Polarion API documentation to get certain fields. Pass include
        (e.g. "author") to sideload related resources; user relationships
        then get resolved display names under
        additional_attributes["<relationship>_name"].
        """
        if fields is None:
            fields = self._client.default_fields.testruns

        sparse_fields = self._build_sparse_fields(fields)
        response = get_test_runs.sync_detailed(
            self._project_id,
            client=self._client.client,
            query=query,
            fields=sparse_fields,
            pagenumber=page_number,
            pagesize=page_size,
            include=include or oa_types.UNSET,
        )
        return self._parse_get_response(response)

    async def async_get_multi(  # type: ignore[override]
        self,
        query: str = "",
        *,
        page_size: int = 100,
        page_number: int = 1,
        fields: dict[str, str] | None = None,
        include: str | None = None,
    ) -> tuple[list[dm.TestRun], bool]:
        """Return the test runs on a defined page matching the given query.

        In addition, a flag whether a next page is available is
        returned. Define a fields dictionary as described in the
        Polarion API documentation to get certain fields. Pass include
        (e.g. "author") to sideload related resources; user relationships
        then get resolved display names under
        additional_attributes["<relationship>_name"].
        """
        if fields is None:
            fields = self._client.default_fields.testruns

        sparse_fields = self._build_sparse_fields(fields)
        response = await get_test_runs.asyncio_detailed(
            self._project_id,
            client=self._client.client,
            query=query,
            fields=sparse_fields,
            pagenumber=page_number,
            pagesize=page_size,
            include=include or oa_types.UNSET,
        )

        self._raise_on_error(response)

        return self._parse_get_response(response)

    def get(  # type: ignore[override]
        self,
        test_run_id: str,
        *,
        fields: dict[str, str] | None = None,
        include: str | None = None,
    ) -> dm.TestRun | None:
        """Return one specific test run by id.

        Pass include (e.g. "author") to sideload related resources; user
        relationships then get resolved display names under
        additional_attributes["<relationship>_name"].
        """
        if fields is None:
            fields = self._client.default_fields.testruns

        response = get_test_run.sync_detailed(
            self._project_id,
            test_run_id,
            client=self._client.client,
            fields=self._build_sparse_fields(fields),
            include=include or oa_types.UNSET,
        )
        return self._parse_single_get_response(response)

    async def async_get(  # type: ignore[override]
        self,
        test_run_id: str,
        *,
        fields: dict[str, str] | None = None,
        include: str | None = None,
    ) -> dm.TestRun | None:
        """Return one specific test run by id.

        Pass include (e.g. "author") to sideload related resources; user
        relationships then get resolved display names under
        additional_attributes["<relationship>_name"].
        """
        if fields is None:
            fields = self._client.default_fields.testruns

        response = await get_test_run.asyncio_detailed(
            self._project_id,
            test_run_id,
            client=self._client.client,
            fields=self._build_sparse_fields(fields),
            include=include or oa_types.UNSET,
        )
        return self._parse_single_get_response(response)

    def _generate_test_run(
        self,
        data: (
            api_models.TestrunsListGetResponseDataItem
            | api_models.TestrunsSingleGetResponseData
        ),
        user_names: dict[str, str] | None = None,
    ) -> dm.TestRun:
        assert isinstance(data.id, str)
        attributes = data.attributes
        assert attributes is not None
        assert not isinstance(attributes, oa_types.Unset)
        additional_attributes = {
            key: value
            for key, value in attributes.to_dict().items()
            if key not in _TYPED_TEST_RUN_ATTRIBUTE_KEYS
        }

        relationships = getattr(data, "relationships", None)
        if relationships is not None and not isinstance(
            relationships, oa_types.Unset
        ):
            names = user_names or {}
            self._resolve_named_user_relationship(
                additional_attributes,
                "author",
                getattr(relationships, "author", None),
                names,
            )
            document = getattr(relationships, "document", None)
            document_data = getattr(document, "data", None)
            if document_data and not isinstance(document_data, oa_types.Unset):
                additional_attributes["document"] = document_data.id
            template = getattr(relationships, "template", None)
            template_data = getattr(template, "data", None)
            if template_data and not isinstance(template_data, oa_types.Unset):
                additional_attributes["template"] = template_data.id

        return dm.TestRun(
            data.id.split("/")[-1],
            self.unset_to_none(attributes.type_),
            self.unset_to_none(attributes.status),
            self.unset_to_none(attributes.title),
            self._handle_text_content(attributes.home_page_content),
            self.unset_to_none(attributes.finished_on),
            self.unset_to_none(attributes.group_id),
            self.unset_to_none(attributes.id_prefix),
            self.unset_to_none(attributes.is_template),
            self.unset_to_none(attributes.keep_in_history),
            self.unset_to_none(attributes.query),
            self.unset_to_none(attributes.use_report_from_template),
            (
                dm.SelectTestCasesBy(str(attributes.select_test_cases_by))
                if attributes.select_test_cases_by
                else None
            ),
            additional_attributes,
        )

    def _parse_get_response(
        self, response: oa_types.Response
    ) -> tuple[list[dm.TestRun], bool]:
        self._raise_on_error(response)
        parsed_response = response.parsed
        assert isinstance(parsed_response, api_models.TestrunsListGetResponse)
        user_names = self._user_names_from_included(parsed_response.included)
        test_runs = [
            self._generate_test_run(data, user_names)
            for data in parsed_response.data or []
        ]
        next_page = isinstance(
            parsed_response.links,
            api_models.TestrunsListGetResponseLinks,
        ) and bool(parsed_response.links.next_)
        return test_runs, next_page

    def _parse_single_get_response(
        self, response: oa_types.Response
    ) -> dm.TestRun | None:
        self._raise_on_error(response)
        parsed_response = response.parsed
        if not isinstance(
            parsed_response, api_models.TestrunsSingleGetResponse
        ) or not isinstance(
            parsed_response.data, api_models.TestrunsSingleGetResponseData
        ):
            return None
        user_names = self._user_names_from_included(parsed_response.included)
        return self._generate_test_run(parsed_response.data, user_names)

    def _create(self, items: list[dm.TestRun]) -> None:
        """Create the given list of test runs."""
        response = post_test_runs.sync_detailed(
            self._project_id,
            client=self._client.client,
            body=self._prepare_post_request(items),
        )
        self._process_create_reponse(items, response)

    async def _async_create(self, items: list[dm.TestRun]) -> None:
        """Create the given list of test runs."""
        response = await post_test_runs.asyncio_detailed(
            self._project_id,
            client=self._client.client,
            body=self._prepare_post_request(items),
        )
        self._process_create_reponse(items, response)

    def _process_create_reponse(
        self, items: list[dm.TestRun], response: oa_types.Response
    ) -> None:
        self._raise_on_error(response)
        parsed_response = response.parsed
        assert isinstance(parsed_response, api_models.TestrunsListPostResponse)
        assert parsed_response.data
        for i, data in enumerate(parsed_response.data):
            assert data.id
            items[i].id = data.id.split("/")[-1]

    def _prepare_post_request(
        self, items: list[dm.TestRun]
    ) -> api_models.TestrunsListPostRequest:
        return api_models.TestrunsListPostRequest(
            [
                api_models.TestrunsListPostRequestDataItem(
                    type_=api_models.TestrunsListPostRequestDataItemType.TESTRUNS,
                    attributes=self._fill_test_run_attributes(
                        api_models.TestrunsListPostRequestDataItemAttributes,
                        test_run,
                    ),
                )
                for test_run in items
            ]
        )

    def _delete(self, items: list[dm.TestRun]) -> None:
        response = delete_test_runs.sync_detailed(
            self._project_id,
            client=self._client.client,
            body=self._make_delete_request(items),
        )
        self._raise_on_error(response)

    async def _async_delete(self, items: list[dm.TestRun]) -> None:
        response = await delete_test_runs.asyncio_detailed(
            self._project_id,
            client=self._client.client,
            body=self._make_delete_request(items),
        )
        self._raise_on_error(response)

    def _make_delete_request(
        self, items: list[dm.TestRun]
    ) -> api_models.TestrunsListDeleteRequest:
        return api_models.TestrunsListDeleteRequest(
            data=[
                api_models.TestrunsListDeleteRequestDataItem(
                    type_=api_models.TestrunsListDeleteRequestDataItemType.TESTRUNS,
                    id=item.id,
                )
                for item in items
                if item.id
            ]
        )

    def _fill_test_run_attributes(  # noqa: C901
        self,
        attributes_type: type[AttributesType],
        test_run: dm.TestRun,
    ) -> AttributesType:
        type_prefix = attributes_type.__name__
        attributes = attributes_type()
        if test_run.type is not None:
            attributes.type_ = test_run.type
        if test_run.id and hasattr(attributes, "id"):
            attributes.id = test_run.id
        if test_run.status is not None:
            attributes.status = test_run.status
        if test_run.title is not None:
            attributes.title = test_run.title
        if test_run.finished_on is not None:
            attributes.finished_on = test_run.finished_on
        if test_run.group_id is not None:
            attributes.group_id = test_run.group_id
        if test_run.id_prefix is not None:
            attributes.id_prefix = test_run.id_prefix
        if test_run.is_template is not None and hasattr(
            attributes, "is_template"
        ):
            attributes.is_template = test_run.is_template
        if test_run.keep_in_history is not None:
            attributes.keep_in_history = test_run.keep_in_history
        if test_run.query is not None:
            attributes.query = test_run.query
        if test_run.use_report_from_template is not None:
            attributes.use_report_from_template = (
                test_run.use_report_from_template
            )
        if test_run.additional_attributes:
            attributes.additional_properties = test_run.additional_attributes
        if test_run.select_test_cases_by:
            attributes.select_test_cases_by = getattr(
                api_models, f"{type_prefix}SelectTestCasesBy"
            )(test_run.select_test_cases_by.value)
        if test_run.home_page_content:
            attributes.home_page_content = getattr(
                api_models, f"{type_prefix}HomePageContent"
            )()
            assert attributes.home_page_content
            if test_run.home_page_content.type:
                attributes.home_page_content.type_ = getattr(
                    api_models, f"{type_prefix}HomePageContentType"
                )(test_run.home_page_content.type)
            if test_run.home_page_content.value:
                attributes.home_page_content.value = (
                    test_run.home_page_content.value
                )

        return t.cast(AttributesType, attributes)

# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
"""Base classes for client implementations on project Level."""

import abc
import datetime
import functools
import http
import logging
import random
import time
import typing as t

from polarion_rest_api_client import data_models as dm
from polarion_rest_api_client import errors
from polarion_rest_api_client.open_api_client import models as api_models
from polarion_rest_api_client.open_api_client import types as oa_types

R = t.TypeVar("R")

if t.TYPE_CHECKING:
    from polarion_rest_api_client import client as polarion_client

T = t.TypeVar("T")
ST = t.TypeVar("ST", bound=dm.StatusItem)
logger = logging.getLogger(__name__)
_min_sleep = 5
_max_sleep = 15

_NON_RETRIABLE_ERRORS = {
    http.HTTPStatus.BAD_REQUEST,
    http.HTTPStatus.IM_A_TEAPOT,
    http.HTTPStatus.NOT_FOUND,
}

UT = t.TypeVar("UT", str, int, float, datetime.datetime, bool, None)


class BaseClient:
    """The overall base client for all project related clients."""

    _retry_methods: t.ClassVar[list[str]] = []

    def __init__(
        self, project_id: str, client: "polarion_client.PolarionClient"
    ):
        self._project_id = project_id
        self._client = client

    def __getattribute__(self, name: str) -> t.Any:
        """Retry method calls defined in _retry_methods."""
        attr = super().__getattribute__(name)
        retry_methods = super().__getattribute__("_retry_methods")
        if name in retry_methods and callable(attr):
            return functools.partial(
                super().__getattribute__("_retry_on_error"), attr
            )

        return attr

    def _handle_text_content(
        self,
        polarion_content: (
            api_models.DocumentsSingleGetResponseDataAttributesHomePageContent  # pylint: disable=line-too-long
            | api_models.TestrecordsListGetResponseDataItemAttributesComment
            | api_models.TestrunsListGetResponseDataItemAttributesHomePageContent
            | oa_types.Unset
        ),
    ) -> dm.TextContent | None:
        if not polarion_content:
            return None

        return dm.TextContent(
            type=(
                str(polarion_content.type_) if polarion_content.type_ else None
            ),
            value=polarion_content.value or None,
        )

    def _build_sparse_fields(
        self, fields_dict: dict[str, str]
    ) -> api_models.SparseFields | oa_types.Unset:
        """Build the SparseFields object based on a dict.

        Ensure that every key follow the pattern 'fields[XXX]'.
        """
        new_field_dict: dict[str, str] = {}
        for key, value in fields_dict.items():
            if key.startswith("fields["):
                new_field_dict[key] = value
            else:
                new_field_dict[f"fields[{key}]"] = value
        return api_models.SparseFields.from_dict(new_field_dict)

    @t.overload
    def unset_to_none(self, value: oa_types.Unset) -> None:
        """Return None if value is Unset, else the value."""

    @t.overload
    def unset_to_none(self, value: UT) -> UT:
        """Return None if value is Unset, else the value."""

    def unset_to_none(self, value: t.Any) -> t.Any:
        """Return None if value is Unset, else the value."""
        if isinstance(value, oa_types.Unset):
            return None
        return value

    def _raise_on_error(self, response: oa_types.Response) -> None:
        def unexpected_error() -> errors.PolarionApiUnexpectedException:
            return errors.PolarionApiUnexpectedException(
                response.status_code, response.content
            )

        if response.status_code not in range(400, 600):
            return

        if (
            isinstance(response.parsed, api_models.Errors)
            and response.parsed.errors
        ):
            raise errors.PolarionApiException(
                response.status_code,
                *[
                    (
                        e.status,
                        e.detail,
                        (
                            e.source.pointer
                            if not (
                                isinstance(e.source, oa_types.Unset)
                                or e.source is None
                            )
                            else "No error pointer"
                        ),
                    )
                    for e in response.parsed.errors
                ],
            )
        raise unexpected_error()

    def _retry_on_error(
        self, call: t.Callable[..., R], *args: t.Any, **kwargs: t.Any
    ) -> R:
        try:
            return call(*args, **kwargs)
        except Exception as e:
            if (
                isinstance(e, errors.PolarionApiException)
                and e.args[0] in _NON_RETRIABLE_ERRORS
            ):
                raise e
            logger.warning(
                "Will retry after failing on first attempt, "
                "due to the following error %s",
                e,
            )
            time.sleep(random.uniform(_min_sleep, _max_sleep))
            return call(*args, **kwargs)


class ItemsClient(BaseClient, t.Generic[T], abc.ABC):
    """A client for items of a project, which can be created or requested."""

    _retry_methods: t.ClassVar[list[str]] = [
        "get_multi",
        "get",
        "_create",
        "_delete",
    ]

    @abc.abstractmethod
    def get_multi(
        self,
        *args: t.Any,
        page_size: int = 100,
        page_number: int = 1,
        **kwargs: t.Any,
    ) -> tuple[list[T], bool]:
        """Get multiple matching items for a specific page.

        In addition, a flag whether a next page is available is
        returned.
        """

    @abc.abstractmethod
    def get(self, *args: t.Any, **kwargs: t.Any) -> T | None:
        """Get a specific single item."""
        return self._retry_on_error(self.get, *args, **kwargs)

    def get_all(self, *args: t.Any, **kwargs: t.Any) -> list[T]:
        """Return all matching items using get_multi with auto pagination."""
        page = 1
        items, next_page = self.get_multi(
            *args, page_size=self._client.page_size, page_number=page, **kwargs
        )
        while next_page:
            page += 1
            _items, next_page = self.get_multi(
                *args,
                page_size=self._client.page_size,
                page_number=page,
                **kwargs,
            )
            items += _items
        return items

    @abc.abstractmethod
    def _create(self, items: list[T]) -> None: ...

    def _split_into_batches(
        self, items: list[T]
    ) -> t.Generator[list[T], None, None]:
        for i in range(0, len(items), self._client.batch_size):
            yield items[i : i + self._client.batch_size]

    def create(self, items: T | list[T]) -> None:
        """Create one or multiple items."""
        if not isinstance(items, list):
            items = [items]

        for batch in self._split_into_batches(items):
            self._create(batch)

    @abc.abstractmethod
    def _delete(self, items: list[T]) -> None: ...

    def delete(self, items: T | list[T]) -> None:
        """Delete one or multiple items."""
        if not isinstance(items, list):
            items = [items]
        for batch in self._split_into_batches(items):
            self._delete(batch)


class UpdatableItemsClient(ItemsClient, t.Generic[T], abc.ABC):
    """A client for items which can also be updated."""

    _retry_methods: t.ClassVar[list[str]] = [
        "get_multi",
        "get",
        "_create",
        "_delete",
        "_update",
    ]

    def _split_into_update_batches(
        self, items: list[T]
    ) -> t.Generator[list[T], None, None] | t.Generator[T, None, None]:
        yield from self._split_into_batches(items)

    @abc.abstractmethod
    def _update(self, to_update: T | list[T]) -> None: ...

    def update(self, items: T | list[T]) -> None:
        """Update the provided item or items."""
        if not isinstance(items, list):
            items = [items]

        for batch in self._split_into_update_batches(items):
            self._update(batch)


class SingleUpdatableItemsMixin(t.Generic[T]):
    """Mixin to split batches into single items."""

    def _split_into_update_batches(
        self, items: list[T]
    ) -> t.Generator[T, None, None]:
        yield from items


class StatusItemClient(UpdatableItemsClient, t.Generic[ST], abc.ABC):
    """A client for items, which have a status.

    We support to set a specific status for these instead of deleting
    them. This status has to be provided on initialization.
    """

    item_cls: type[ST]

    def __init__(
        self,
        project_id: str,
        client: "polarion_client.PolarionClient",
        delete_status: str | None = None,
    ):
        super().__init__(project_id, client)
        self.delete_status = delete_status

    def delete(self, items: ST | list[ST]) -> None:
        """Delete the item if no delete_status was set, else update status."""
        if self.delete_status is None:
            super().delete(items)
        else:
            if not isinstance(items, list):
                items = [items]
            delete_items: list[ST] = []
            for item in items:
                item.status = self.delete_status
                delete_items.append(
                    self.item_cls(id=item.id, status=self.delete_status)
                )
            self.update(delete_items)

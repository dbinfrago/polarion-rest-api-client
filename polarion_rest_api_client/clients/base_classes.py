# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
"""Base classes for client implementations on project Level."""

import abc
import asyncio
import datetime
import functools
import http
import inspect
import logging
import random
import time
import typing as t

import httpx

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
_max_retries: t.Final = 5

_NON_RETRIABLE_ERRORS = {
    http.HTTPStatus.BAD_REQUEST,
    http.HTTPStatus.IM_A_TEAPOT,
    http.HTTPStatus.NOT_FOUND,
}

UT = t.TypeVar("UT", str, int, float, datetime.datetime, bool, None)
NT = t.TypeVar("NT", str, int, float, datetime.datetime, bool, oa_types.Unset)


def _compute_backoff(sleeptime: float, attempt: int) -> float:
    return sleeptime * 3 + random.uniform(0.5, (attempt + 1) / 2)


class BaseClient(t.Generic[T]):
    """The overall base client for all project related clients."""

    _retry_methods: t.ClassVar[set[str]] = (
        set()
    )  # methods which can be retried

    def __init__(
        self, project_id: str, client: "polarion_client.PolarionClient"
    ):
        self._project_id = project_id
        self._client = client
        self._all_retry_methods: set[str] = set()
        for base in self.__class__.__mro__:
            if hasattr(base, "_retry_methods"):
                self._all_retry_methods.update(base._retry_methods)

    def __getattribute__(self, name: str) -> t.Any:
        """Retry method calls defined in _retry_methods."""
        attr = super().__getattribute__(name)
        retry_methods = super().__getattribute__("_all_retry_methods")
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

    @t.overload
    def none_to_unset(self, value: None) -> oa_types.Unset:
        """Return UNSET if value is None, else the value."""

    @t.overload
    def none_to_unset(self, value: NT) -> NT:
        """Return UNSET if value is None, else the value."""

    def none_to_unset(self, value: t.Any) -> t.Any:
        """Return UNSET if value is None, else the value."""
        if value is None:
            return oa_types.UNSET
        return value

    def _raise_on_error(self, response: oa_types.Response) -> None:
        """Raise an PolarionApiBaseException, if the response has errors."""

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
    ) -> R | t.Coroutine[t.Any, t.Any, R]:
        """Retry on errors with exponential backoff."""
        if inspect.iscoroutinefunction(call):
            return self._retry_async(call, *args, **kwargs)
        return self._retry_sync(call, *args, **kwargs)

    def _retry_sync(
        self, call: t.Callable[..., R], *args: t.Any, **kwargs: t.Any
    ) -> R:
        last_error: Exception | None = None
        sleeptime = 0.0
        for attempt in range(1, _max_retries + 1):
            try:
                return call(*args, **kwargs)
            except (errors.PolarionApiBaseException, httpx.HTTPError) as e:
                last_error = e
                sleeptime = _compute_backoff(sleeptime, attempt)
                self._handle_tolerated_exception(
                    e, sleeptime, attempt, last_error
                )
                time.sleep(sleeptime)

        assert last_error is not None
        raise last_error

    def _retry_async(
        self,
        call: t.Callable[..., t.Coroutine[t.Any, t.Any, R]],
        *args: t.Any,
        **kwargs: t.Any,
    ) -> t.Coroutine[t.Any, t.Any, R]:
        async def wrapped() -> R:
            last_error: Exception | None = None
            sleeptime = 0.0
            for attempt in range(1, _max_retries + 1):
                try:
                    async with self._client.semaphore:
                        return await call(*args, **kwargs)
                except (errors.PolarionApiBaseException, httpx.HTTPError) as e:
                    last_error = e
                    sleeptime = _compute_backoff(sleeptime, attempt)
                    self._handle_tolerated_exception(
                        e, sleeptime, attempt, last_error
                    )
                    await asyncio.sleep(sleeptime)

            assert last_error is not None
            raise last_error

        return wrapped()

    def _handle_tolerated_exception(
        self,
        e: Exception,
        sleeptime: float,
        attempt: int,
        last_error: Exception,
    ) -> None:
        """Log the error without raising if it's a retryable error."""
        if (
            isinstance(e, errors.PolarionApiException)
            and e.args[0] in _NON_RETRIABLE_ERRORS
        ):
            raise last_error

        logger.warning(
            "Request failed, retrying after %.1fs (%d/%d): %s",
            sleeptime,
            attempt,
            _max_retries,
            last_error,
        )

    def _pre_batching_grouping(
        self, items: list[T]
    ) -> t.Generator[list[T], None, None]:
        """Group items before actually splitting them into batches.

        Needed if we need to first group by a specific value before we
        can split into batches.
        """
        yield items


class SingleGetClient(BaseClient[T], abc.ABC):
    """A client for items of a project, which can be created."""

    _retry_methods: t.ClassVar[set[str]] = {
        "get",
        "async_get",
    }

    @abc.abstractmethod
    def get(self, *args: t.Any, **kwargs: t.Any) -> T | None:
        """Get a specific single item."""

    @abc.abstractmethod
    async def async_get(self, *args: t.Any, **kwargs: t.Any) -> T | None:
        """Get a specific single item."""


class CreateClient(BaseClient[T], abc.ABC):
    """A client for items of a project, which can be created."""

    _retry_methods: t.ClassVar[set[str]] = {
        "_create",
        "_async_create",
    }
    _create_batch_size: int = 0

    @abc.abstractmethod
    def _create(self, items: list[T]) -> None: ...

    @abc.abstractmethod
    async def _async_create(self, items: list[T]) -> None: ...

    def _split_into_create_batches(
        self, items: list[T]
    ) -> t.Generator[list[T], None, None]:
        batch_size = self._create_batch_size or self._client.batch_size
        for it in self._pre_batching_grouping(items):
            for i in range(0, len(it), batch_size):
                yield it[i : i + batch_size]

    def create(self, items: T | list[T]) -> None:
        """Create one or multiple items."""
        if not isinstance(items, list):
            items = [items]

        for batch in self._split_into_create_batches(items):
            self._create(batch)

    async def async_create(self, items: T | list[T]) -> None:
        """Create one or multiple items."""
        if not isinstance(items, list):
            items = [items]

        for batch in self._split_into_create_batches(items):
            await self._async_create(batch)


class DeleteClient(BaseClient[T], abc.ABC):
    """A client for items of a project, which can be created."""

    _retry_methods: t.ClassVar[set[str]] = {
        "_delete",
        "_async_delete",
    }
    _delete_batch_size: int = 0

    def _split_into_delete_batches(
        self, items: list[T]
    ) -> t.Generator[list[T], None, None]:
        batch_size = self._delete_batch_size or self._client.batch_size
        for it in self._pre_batching_grouping(items):
            for i in range(0, len(it), batch_size):
                yield it[i : i + batch_size]

    @abc.abstractmethod
    def _delete(self, items: list[T]) -> None: ...

    @abc.abstractmethod
    async def _async_delete(self, items: list[T]) -> None: ...

    def delete(self, items: T | list[T]) -> None:
        """Delete one or multiple items."""
        if not isinstance(items, list):
            items = [items]
        for batch in self._split_into_delete_batches(items):
            self._delete(batch)

    async def async_delete(self, items: T | list[T]) -> None:
        """Delete one or multiple items."""
        if not isinstance(items, list):
            items = [items]
        for batch in self._split_into_delete_batches(items):
            await self._async_delete(batch)


class MultiGetClient(BaseClient[T], abc.ABC):
    """A client for items of a project, which can be created."""

    _retry_methods: t.ClassVar[set[str]] = {
        "get_multi",
        "async_get_multi",
    }

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
    async def async_get_multi(
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

    async def async_get_all(self, *args: t.Any, **kwargs: t.Any) -> list[T]:
        """Return all matching items using get_multi with auto pagination."""
        page = 1
        items, next_page = await self.async_get_multi(
            *args, page_size=self._client.page_size, page_number=page, **kwargs
        )
        while next_page:
            page += 1
            _items, next_page = await self.async_get_multi(
                *args,
                page_size=self._client.page_size,
                page_number=page,
                **kwargs,
            )
            items += _items
        return items


class UpdateClient(BaseClient[T], abc.ABC):
    """A client for items which can also be updated."""

    _retry_methods: t.ClassVar[set[str]] = {
        "_update",
        "_async_update",
    }
    _update_batch_size: int = 0

    def _split_into_update_batches(
        self, items: list[T]
    ) -> t.Generator[list[T], None, None]:
        batch_size = self._update_batch_size or self._client.batch_size
        for it in self._pre_batching_grouping(items):
            for i in range(0, len(it), batch_size):
                yield it[i : i + batch_size]

    @abc.abstractmethod
    def _update(self, to_update: list[T]) -> None: ...

    @abc.abstractmethod
    async def _async_update(self, to_update: list[T]) -> None: ...

    def update(self, items: T | list[T]) -> None:
        """Update the provided item or items."""
        if not isinstance(items, list):
            items = [items]

        for batch in self._split_into_update_batches(items):
            self._update(batch)

    async def async_update(self, items: T | list[T]) -> None:
        """Update the provided item or items."""
        if not isinstance(items, list):
            items = [items]

        for batch in self._split_into_update_batches(items):
            await self._async_update(batch)


class StatusItemClient(UpdateClient, DeleteClient, t.Generic[ST], abc.ABC):
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
            delete_items = self._prepare_update_items(items)
            self.update(delete_items)

    async def async_delete(self, items: ST | list[ST]) -> None:
        """Delete the item if no delete_status was set, else update status."""
        if self.delete_status is None:
            await super().async_delete(items)
        else:
            delete_items = self._prepare_update_items(items)
            await self.async_update(delete_items)

    def _prepare_update_items(self, items: ST | list[ST]) -> list[ST]:
        if not isinstance(items, list):
            items = [items]
        delete_items: list[ST] = []
        for item in items:
            item.status = self.delete_status
            delete_items.append(
                self.item_cls(id=item.id, status=self.delete_status)
            )
        return delete_items

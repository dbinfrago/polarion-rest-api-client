# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.errors_errors_item_source_type_0 import (
        ErrorsErrorsItemSourceType0,
    )


T = TypeVar("T", bound="ErrorsErrorsItem")


@_attrs_define
class ErrorsErrorsItem:
    """
    Attributes:
        status (str | Unset): HTTP status code applicable to this problem. Example: 400.
        title (str | Unset): Short, human-readable summary of the problem. Example: Bad Request.
        detail (str | Unset): Human-readable explanation specific to this occurrence of the problem. Example: Unexpected
            token, BEGIN_ARRAY expected, but was : BEGIN_OBJECT (at $.data).
        source (ErrorsErrorsItemSourceType0 | None | Unset):
    """

    status: str | Unset = UNSET
    title: str | Unset = UNSET
    detail: str | Unset = UNSET
    source: ErrorsErrorsItemSourceType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        from ..models.errors_errors_item_source_type_0 import (
            ErrorsErrorsItemSourceType0,
        )

        status = self.status

        title = self.title

        detail = self.detail

        source: dict[str, Any] | None | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        elif isinstance(self.source, ErrorsErrorsItemSourceType0):
            source = self.source.to_dict()
        else:
            source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if title is not UNSET:
            field_dict["title"] = title
        if detail is not UNSET:
            field_dict["detail"] = detail
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.errors_errors_item_source_type_0 import (
            ErrorsErrorsItemSourceType0,
        )

        d = dict(src_dict)
        status = d.pop("status", UNSET)

        title = d.pop("title", UNSET)

        detail = d.pop("detail", UNSET)

        def _parse_source(
            data: object,
        ) -> ErrorsErrorsItemSourceType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_type_0 = ErrorsErrorsItemSourceType0.from_dict(data)

                return source_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ErrorsErrorsItemSourceType0 | None | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        errors_errors_item_obj = cls(
            status=status,
            title=title,
            detail=detail,
            source=source,
        )

        errors_errors_item_obj.additional_properties = d
        return errors_errors_item_obj

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

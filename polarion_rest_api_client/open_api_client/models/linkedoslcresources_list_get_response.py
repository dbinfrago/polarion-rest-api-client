# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.linkedoslcresources_list_get_response_data_item import (
        LinkedoslcresourcesListGetResponseDataItem,
    )
    from ..models.linkedoslcresources_list_get_response_included_item import (
        LinkedoslcresourcesListGetResponseIncludedItem,
    )
    from ..models.linkedoslcresources_list_get_response_meta import (
        LinkedoslcresourcesListGetResponseMeta,
    )


T = TypeVar("T", bound="LinkedoslcresourcesListGetResponse")


@_attrs_define
class LinkedoslcresourcesListGetResponse:
    """
    Attributes:
        data (list[LinkedoslcresourcesListGetResponseDataItem] | Unset):
        included (list[LinkedoslcresourcesListGetResponseIncludedItem] | Unset): Related entities might be returned, see
            <a href="https://docs.sw.siemens.com/en-
            US/doc/230235217/PL20250606201928474.polarion_help_sc.xid2134849/xid2134871" target="_blank">REST API User
            Guide</a>.
        meta (LinkedoslcresourcesListGetResponseMeta | Unset):
    """

    data: list[LinkedoslcresourcesListGetResponseDataItem] | Unset = UNSET
    included: list[LinkedoslcresourcesListGetResponseIncludedItem] | Unset = (
        UNSET
    )
    meta: LinkedoslcresourcesListGetResponseMeta | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        included: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.included, Unset):
            included = []
            for included_item_data in self.included:
                included_item = included_item_data.to_dict()
                included.append(included_item)

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if included is not UNSET:
            field_dict["included"] = included
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linkedoslcresources_list_get_response_data_item import (
            LinkedoslcresourcesListGetResponseDataItem,
        )
        from ..models.linkedoslcresources_list_get_response_included_item import (
            LinkedoslcresourcesListGetResponseIncludedItem,
        )
        from ..models.linkedoslcresources_list_get_response_meta import (
            LinkedoslcresourcesListGetResponseMeta,
        )

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[LinkedoslcresourcesListGetResponseDataItem] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = (
                    LinkedoslcresourcesListGetResponseDataItem.from_dict(
                        data_item_data
                    )
                )

                data.append(data_item)

        _included = d.pop("included", UNSET)
        included: (
            list[LinkedoslcresourcesListGetResponseIncludedItem] | Unset
        ) = UNSET
        if _included is not UNSET:
            included = []
            for included_item_data in _included:
                included_item = (
                    LinkedoslcresourcesListGetResponseIncludedItem.from_dict(
                        included_item_data
                    )
                )

                included.append(included_item)

        _meta = d.pop("meta", UNSET)
        meta: LinkedoslcresourcesListGetResponseMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = LinkedoslcresourcesListGetResponseMeta.from_dict(_meta)

        linkedoslcresources_list_get_response_obj = cls(
            data=data,
            included=included,
            meta=meta,
        )

        linkedoslcresources_list_get_response_obj.additional_properties = d
        return linkedoslcresources_list_get_response_obj

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

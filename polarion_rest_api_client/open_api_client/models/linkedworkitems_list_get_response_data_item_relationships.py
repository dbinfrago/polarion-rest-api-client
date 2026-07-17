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
    from ..models.linkedworkitems_list_get_response_data_item_relationships_source_work_item import (
        LinkedworkitemsListGetResponseDataItemRelationshipsSourceWorkItem,
    )
    from ..models.linkedworkitems_list_get_response_data_item_relationships_work_item import (
        LinkedworkitemsListGetResponseDataItemRelationshipsWorkItem,
    )


T = TypeVar("T", bound="LinkedworkitemsListGetResponseDataItemRelationships")


@_attrs_define
class LinkedworkitemsListGetResponseDataItemRelationships:
    """
    Attributes:
        source_work_item (LinkedworkitemsListGetResponseDataItemRelationshipsSourceWorkItem | Unset):
        work_item (LinkedworkitemsListGetResponseDataItemRelationshipsWorkItem | Unset):
    """

    source_work_item: (
        LinkedworkitemsListGetResponseDataItemRelationshipsSourceWorkItem
        | Unset
    ) = UNSET
    work_item: (
        LinkedworkitemsListGetResponseDataItemRelationshipsWorkItem | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        source_work_item: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source_work_item, Unset):
            source_work_item = self.source_work_item.to_dict()

        work_item: dict[str, Any] | Unset = UNSET
        if not isinstance(self.work_item, Unset):
            work_item = self.work_item.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source_work_item is not UNSET:
            field_dict["sourceWorkItem"] = source_work_item
        if work_item is not UNSET:
            field_dict["workItem"] = work_item

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linkedworkitems_list_get_response_data_item_relationships_source_work_item import (
            LinkedworkitemsListGetResponseDataItemRelationshipsSourceWorkItem,
        )
        from ..models.linkedworkitems_list_get_response_data_item_relationships_work_item import (
            LinkedworkitemsListGetResponseDataItemRelationshipsWorkItem,
        )

        d = dict(src_dict)
        _source_work_item = d.pop("sourceWorkItem", UNSET)
        source_work_item: (
            LinkedworkitemsListGetResponseDataItemRelationshipsSourceWorkItem
            | Unset
        )
        if isinstance(_source_work_item, Unset):
            source_work_item = UNSET
        else:
            source_work_item = LinkedworkitemsListGetResponseDataItemRelationshipsSourceWorkItem.from_dict(
                _source_work_item
            )

        _work_item = d.pop("workItem", UNSET)
        work_item: (
            LinkedworkitemsListGetResponseDataItemRelationshipsWorkItem | Unset
        )
        if isinstance(_work_item, Unset):
            work_item = UNSET
        else:
            work_item = LinkedworkitemsListGetResponseDataItemRelationshipsWorkItem.from_dict(
                _work_item
            )

        linkedworkitems_list_get_response_data_item_relationships_obj = cls(
            source_work_item=source_work_item,
            work_item=work_item,
        )

        linkedworkitems_list_get_response_data_item_relationships_obj.additional_properties = d
        return linkedworkitems_list_get_response_data_item_relationships_obj

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

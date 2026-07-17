# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import datetime
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
    from ..models.collections_single_get_response_data_attributes_description import (
        CollectionsSingleGetResponseDataAttributesDescription,
    )


T = TypeVar("T", bound="CollectionsSingleGetResponseDataAttributes")


@_attrs_define
class CollectionsSingleGetResponseDataAttributes:
    """
    Attributes:
        closed_on (datetime.datetime | Unset):  Example: 1970-01-01T00:00:00Z.
        created (datetime.datetime | Unset):  Example: 1970-01-01T00:00:00Z.
        description (CollectionsSingleGetResponseDataAttributesDescription | Unset):
        id (str | Unset):  Example: ID.
        name (str | Unset):  Example: Name.
        updated (datetime.datetime | Unset):  Example: 1970-01-01T00:00:00Z.
    """

    closed_on: datetime.datetime | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    description: (
        CollectionsSingleGetResponseDataAttributesDescription | Unset
    ) = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    updated: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        closed_on: str | Unset = UNSET
        if not isinstance(self.closed_on, Unset):
            closed_on = self.closed_on.isoformat()

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        description: dict[str, Any] | Unset = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict()

        id = self.id

        name = self.name

        updated: str | Unset = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if closed_on is not UNSET:
            field_dict["closedOn"] = closed_on
        if created is not UNSET:
            field_dict["created"] = created
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.collections_single_get_response_data_attributes_description import (
            CollectionsSingleGetResponseDataAttributesDescription,
        )

        d = dict(src_dict)
        _closed_on = d.pop("closedOn", UNSET)
        closed_on: datetime.datetime | Unset
        if isinstance(_closed_on, Unset):
            closed_on = UNSET
        else:
            closed_on = datetime.datetime.fromisoformat(_closed_on)

        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = datetime.datetime.fromisoformat(_created)

        _description = d.pop("description", UNSET)
        description: (
            CollectionsSingleGetResponseDataAttributesDescription | Unset
        )
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = CollectionsSingleGetResponseDataAttributesDescription.from_dict(
                _description
            )

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _updated = d.pop("updated", UNSET)
        updated: datetime.datetime | Unset
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = datetime.datetime.fromisoformat(_updated)

        collections_single_get_response_data_attributes_obj = cls(
            closed_on=closed_on,
            created=created,
            description=description,
            id=id,
            name=name,
            updated=updated,
        )

        collections_single_get_response_data_attributes_obj.additional_properties = d
        return collections_single_get_response_data_attributes_obj

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

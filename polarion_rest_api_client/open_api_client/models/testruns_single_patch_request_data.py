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

from ..models.testruns_single_patch_request_data_type import (
    TestrunsSinglePatchRequestDataType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.testruns_single_patch_request_data_attributes import (
        TestrunsSinglePatchRequestDataAttributes,
    )
    from ..models.testruns_single_patch_request_data_relationships import (
        TestrunsSinglePatchRequestDataRelationships,
    )


T = TypeVar("T", bound="TestrunsSinglePatchRequestData")


@_attrs_define
class TestrunsSinglePatchRequestData:
    """
    Attributes:
        type_ (TestrunsSinglePatchRequestDataType | Unset):
        id (str | Unset):  Example: MyProjectId/MyTestRunId.
        attributes (TestrunsSinglePatchRequestDataAttributes | Unset):
        relationships (TestrunsSinglePatchRequestDataRelationships | Unset):
    """

    type_: TestrunsSinglePatchRequestDataType | Unset = UNSET
    id: str | Unset = UNSET
    attributes: TestrunsSinglePatchRequestDataAttributes | Unset = UNSET
    relationships: TestrunsSinglePatchRequestDataRelationships | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        id = self.id

        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        relationships: dict[str, Any] | Unset = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = self.relationships.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if id is not UNSET:
            field_dict["id"] = id
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if relationships is not UNSET:
            field_dict["relationships"] = relationships

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.testruns_single_patch_request_data_attributes import (
            TestrunsSinglePatchRequestDataAttributes,
        )
        from ..models.testruns_single_patch_request_data_relationships import (
            TestrunsSinglePatchRequestDataRelationships,
        )

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: TestrunsSinglePatchRequestDataType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = TestrunsSinglePatchRequestDataType(_type_)

        id = d.pop("id", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: TestrunsSinglePatchRequestDataAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = TestrunsSinglePatchRequestDataAttributes.from_dict(
                _attributes
            )

        _relationships = d.pop("relationships", UNSET)
        relationships: TestrunsSinglePatchRequestDataRelationships | Unset
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = (
                TestrunsSinglePatchRequestDataRelationships.from_dict(
                    _relationships
                )
            )

        testruns_single_patch_request_data_obj = cls(
            type_=type_,
            id=id,
            attributes=attributes,
            relationships=relationships,
        )

        testruns_single_patch_request_data_obj.additional_properties = d
        return testruns_single_patch_request_data_obj

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

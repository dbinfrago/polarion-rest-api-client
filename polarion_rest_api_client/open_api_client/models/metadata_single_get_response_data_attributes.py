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
    from ..models.metadata_single_get_response_data_attributes_api_properties import (
        MetadataSingleGetResponseDataAttributesApiProperties,
    )


T = TypeVar("T", bound="MetadataSingleGetResponseDataAttributes")


@_attrs_define
class MetadataSingleGetResponseDataAttributes:
    """
    Attributes:
        api_properties (MetadataSingleGetResponseDataAttributesApiProperties | Unset):
        build (str | Unset):  Example: 20250613-1404-master-e594c717.
        cluster (str | Unset):  Example: cluster1.
        logo_url (str | Unset):  Example: /images/logos/repo_login_logo.png.
        node (str | Unset):  Example: node2.
        timezone (str | Unset):  Example: +05:30.
        version (str | Unset):  Example: 3.25.12.
    """

    api_properties: (
        MetadataSingleGetResponseDataAttributesApiProperties | Unset
    ) = UNSET
    build: str | Unset = UNSET
    cluster: str | Unset = UNSET
    logo_url: str | Unset = UNSET
    node: str | Unset = UNSET
    timezone: str | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        api_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.api_properties, Unset):
            api_properties = self.api_properties.to_dict()

        build = self.build

        cluster = self.cluster

        logo_url = self.logo_url

        node = self.node

        timezone = self.timezone

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_properties is not UNSET:
            field_dict["apiProperties"] = api_properties
        if build is not UNSET:
            field_dict["build"] = build
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url
        if node is not UNSET:
            field_dict["node"] = node
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata_single_get_response_data_attributes_api_properties import (
            MetadataSingleGetResponseDataAttributesApiProperties,
        )

        d = dict(src_dict)
        _api_properties = d.pop("apiProperties", UNSET)
        api_properties: (
            MetadataSingleGetResponseDataAttributesApiProperties | Unset
        )
        if isinstance(_api_properties, Unset):
            api_properties = UNSET
        else:
            api_properties = (
                MetadataSingleGetResponseDataAttributesApiProperties.from_dict(
                    _api_properties
                )
            )

        build = d.pop("build", UNSET)

        cluster = d.pop("cluster", UNSET)

        logo_url = d.pop("logoUrl", UNSET)

        node = d.pop("node", UNSET)

        timezone = d.pop("timezone", UNSET)

        version = d.pop("version", UNSET)

        metadata_single_get_response_data_attributes_obj = cls(
            api_properties=api_properties,
            build=build,
            cluster=cluster,
            logo_url=logo_url,
            node=node,
            timezone=timezone,
            version=version,
        )

        metadata_single_get_response_data_attributes_obj.additional_properties = d
        return metadata_single_get_response_data_attributes_obj

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

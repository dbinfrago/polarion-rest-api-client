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
    from ..models.collections_list_get_response_data_item_relationships_author import (
        CollectionsListGetResponseDataItemRelationshipsAuthor,
    )
    from ..models.collections_list_get_response_data_item_relationships_documents import (
        CollectionsListGetResponseDataItemRelationshipsDocuments,
    )
    from ..models.collections_list_get_response_data_item_relationships_downstream_collections import (
        CollectionsListGetResponseDataItemRelationshipsDownstreamCollections,
    )
    from ..models.collections_list_get_response_data_item_relationships_project import (
        CollectionsListGetResponseDataItemRelationshipsProject,
    )
    from ..models.collections_list_get_response_data_item_relationships_reused_from import (
        CollectionsListGetResponseDataItemRelationshipsReusedFrom,
    )
    from ..models.collections_list_get_response_data_item_relationships_rich_pages import (
        CollectionsListGetResponseDataItemRelationshipsRichPages,
    )
    from ..models.collections_list_get_response_data_item_relationships_test_runs import (
        CollectionsListGetResponseDataItemRelationshipsTestRuns,
    )
    from ..models.collections_list_get_response_data_item_relationships_upstream_collections import (
        CollectionsListGetResponseDataItemRelationshipsUpstreamCollections,
    )


T = TypeVar("T", bound="CollectionsListGetResponseDataItemRelationships")


@_attrs_define
class CollectionsListGetResponseDataItemRelationships:
    """
    Attributes:
        author (CollectionsListGetResponseDataItemRelationshipsAuthor | Unset):
        documents (CollectionsListGetResponseDataItemRelationshipsDocuments | Unset):
        downstream_collections (CollectionsListGetResponseDataItemRelationshipsDownstreamCollections | Unset):
        project (CollectionsListGetResponseDataItemRelationshipsProject | Unset):
        reused_from (CollectionsListGetResponseDataItemRelationshipsReusedFrom | Unset):
        rich_pages (CollectionsListGetResponseDataItemRelationshipsRichPages | Unset):
        test_runs (CollectionsListGetResponseDataItemRelationshipsTestRuns | Unset):
        upstream_collections (CollectionsListGetResponseDataItemRelationshipsUpstreamCollections | Unset):
    """

    author: CollectionsListGetResponseDataItemRelationshipsAuthor | Unset = (
        UNSET
    )
    documents: (
        CollectionsListGetResponseDataItemRelationshipsDocuments | Unset
    ) = UNSET
    downstream_collections: (
        CollectionsListGetResponseDataItemRelationshipsDownstreamCollections
        | Unset
    ) = UNSET
    project: CollectionsListGetResponseDataItemRelationshipsProject | Unset = (
        UNSET
    )
    reused_from: (
        CollectionsListGetResponseDataItemRelationshipsReusedFrom | Unset
    ) = UNSET
    rich_pages: (
        CollectionsListGetResponseDataItemRelationshipsRichPages | Unset
    ) = UNSET
    test_runs: (
        CollectionsListGetResponseDataItemRelationshipsTestRuns | Unset
    ) = UNSET
    upstream_collections: (
        CollectionsListGetResponseDataItemRelationshipsUpstreamCollections
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        author: dict[str, Any] | Unset = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        documents: dict[str, Any] | Unset = UNSET
        if not isinstance(self.documents, Unset):
            documents = self.documents.to_dict()

        downstream_collections: dict[str, Any] | Unset = UNSET
        if not isinstance(self.downstream_collections, Unset):
            downstream_collections = self.downstream_collections.to_dict()

        project: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        reused_from: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reused_from, Unset):
            reused_from = self.reused_from.to_dict()

        rich_pages: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rich_pages, Unset):
            rich_pages = self.rich_pages.to_dict()

        test_runs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.test_runs, Unset):
            test_runs = self.test_runs.to_dict()

        upstream_collections: dict[str, Any] | Unset = UNSET
        if not isinstance(self.upstream_collections, Unset):
            upstream_collections = self.upstream_collections.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if author is not UNSET:
            field_dict["author"] = author
        if documents is not UNSET:
            field_dict["documents"] = documents
        if downstream_collections is not UNSET:
            field_dict["downstreamCollections"] = downstream_collections
        if project is not UNSET:
            field_dict["project"] = project
        if reused_from is not UNSET:
            field_dict["reusedFrom"] = reused_from
        if rich_pages is not UNSET:
            field_dict["richPages"] = rich_pages
        if test_runs is not UNSET:
            field_dict["testRuns"] = test_runs
        if upstream_collections is not UNSET:
            field_dict["upstreamCollections"] = upstream_collections

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.collections_list_get_response_data_item_relationships_author import (
            CollectionsListGetResponseDataItemRelationshipsAuthor,
        )
        from ..models.collections_list_get_response_data_item_relationships_documents import (
            CollectionsListGetResponseDataItemRelationshipsDocuments,
        )
        from ..models.collections_list_get_response_data_item_relationships_downstream_collections import (
            CollectionsListGetResponseDataItemRelationshipsDownstreamCollections,
        )
        from ..models.collections_list_get_response_data_item_relationships_project import (
            CollectionsListGetResponseDataItemRelationshipsProject,
        )
        from ..models.collections_list_get_response_data_item_relationships_reused_from import (
            CollectionsListGetResponseDataItemRelationshipsReusedFrom,
        )
        from ..models.collections_list_get_response_data_item_relationships_rich_pages import (
            CollectionsListGetResponseDataItemRelationshipsRichPages,
        )
        from ..models.collections_list_get_response_data_item_relationships_test_runs import (
            CollectionsListGetResponseDataItemRelationshipsTestRuns,
        )
        from ..models.collections_list_get_response_data_item_relationships_upstream_collections import (
            CollectionsListGetResponseDataItemRelationshipsUpstreamCollections,
        )

        d = dict(src_dict)
        _author = d.pop("author", UNSET)
        author: CollectionsListGetResponseDataItemRelationshipsAuthor | Unset
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = CollectionsListGetResponseDataItemRelationshipsAuthor.from_dict(
                _author
            )

        _documents = d.pop("documents", UNSET)
        documents: (
            CollectionsListGetResponseDataItemRelationshipsDocuments | Unset
        )
        if isinstance(_documents, Unset):
            documents = UNSET
        else:
            documents = CollectionsListGetResponseDataItemRelationshipsDocuments.from_dict(
                _documents
            )

        _downstream_collections = d.pop("downstreamCollections", UNSET)
        downstream_collections: (
            CollectionsListGetResponseDataItemRelationshipsDownstreamCollections
            | Unset
        )
        if isinstance(_downstream_collections, Unset):
            downstream_collections = UNSET
        else:
            downstream_collections = CollectionsListGetResponseDataItemRelationshipsDownstreamCollections.from_dict(
                _downstream_collections
            )

        _project = d.pop("project", UNSET)
        project: CollectionsListGetResponseDataItemRelationshipsProject | Unset
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = CollectionsListGetResponseDataItemRelationshipsProject.from_dict(
                _project
            )

        _reused_from = d.pop("reusedFrom", UNSET)
        reused_from: (
            CollectionsListGetResponseDataItemRelationshipsReusedFrom | Unset
        )
        if isinstance(_reused_from, Unset):
            reused_from = UNSET
        else:
            reused_from = CollectionsListGetResponseDataItemRelationshipsReusedFrom.from_dict(
                _reused_from
            )

        _rich_pages = d.pop("richPages", UNSET)
        rich_pages: (
            CollectionsListGetResponseDataItemRelationshipsRichPages | Unset
        )
        if isinstance(_rich_pages, Unset):
            rich_pages = UNSET
        else:
            rich_pages = CollectionsListGetResponseDataItemRelationshipsRichPages.from_dict(
                _rich_pages
            )

        _test_runs = d.pop("testRuns", UNSET)
        test_runs: (
            CollectionsListGetResponseDataItemRelationshipsTestRuns | Unset
        )
        if isinstance(_test_runs, Unset):
            test_runs = UNSET
        else:
            test_runs = CollectionsListGetResponseDataItemRelationshipsTestRuns.from_dict(
                _test_runs
            )

        _upstream_collections = d.pop("upstreamCollections", UNSET)
        upstream_collections: (
            CollectionsListGetResponseDataItemRelationshipsUpstreamCollections
            | Unset
        )
        if isinstance(_upstream_collections, Unset):
            upstream_collections = UNSET
        else:
            upstream_collections = CollectionsListGetResponseDataItemRelationshipsUpstreamCollections.from_dict(
                _upstream_collections
            )

        collections_list_get_response_data_item_relationships_obj = cls(
            author=author,
            documents=documents,
            downstream_collections=downstream_collections,
            project=project,
            reused_from=reused_from,
            rich_pages=rich_pages,
            test_runs=test_runs,
            upstream_collections=upstream_collections,
        )

        collections_list_get_response_data_item_relationships_obj.additional_properties = d
        return collections_list_get_response_data_item_relationships_obj

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

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
    from ..models.collections_single_get_response_data_relationships_author import (
        CollectionsSingleGetResponseDataRelationshipsAuthor,
    )
    from ..models.collections_single_get_response_data_relationships_documents import (
        CollectionsSingleGetResponseDataRelationshipsDocuments,
    )
    from ..models.collections_single_get_response_data_relationships_downstream_collections import (
        CollectionsSingleGetResponseDataRelationshipsDownstreamCollections,
    )
    from ..models.collections_single_get_response_data_relationships_project import (
        CollectionsSingleGetResponseDataRelationshipsProject,
    )
    from ..models.collections_single_get_response_data_relationships_reused_from import (
        CollectionsSingleGetResponseDataRelationshipsReusedFrom,
    )
    from ..models.collections_single_get_response_data_relationships_rich_pages import (
        CollectionsSingleGetResponseDataRelationshipsRichPages,
    )
    from ..models.collections_single_get_response_data_relationships_test_runs import (
        CollectionsSingleGetResponseDataRelationshipsTestRuns,
    )
    from ..models.collections_single_get_response_data_relationships_upstream_collections import (
        CollectionsSingleGetResponseDataRelationshipsUpstreamCollections,
    )


T = TypeVar("T", bound="CollectionsSingleGetResponseDataRelationships")


@_attrs_define
class CollectionsSingleGetResponseDataRelationships:
    """
    Attributes:
        author (CollectionsSingleGetResponseDataRelationshipsAuthor | Unset):
        documents (CollectionsSingleGetResponseDataRelationshipsDocuments | Unset):
        downstream_collections (CollectionsSingleGetResponseDataRelationshipsDownstreamCollections | Unset):
        project (CollectionsSingleGetResponseDataRelationshipsProject | Unset):
        reused_from (CollectionsSingleGetResponseDataRelationshipsReusedFrom | Unset):
        rich_pages (CollectionsSingleGetResponseDataRelationshipsRichPages | Unset):
        test_runs (CollectionsSingleGetResponseDataRelationshipsTestRuns | Unset):
        upstream_collections (CollectionsSingleGetResponseDataRelationshipsUpstreamCollections | Unset):
    """

    author: CollectionsSingleGetResponseDataRelationshipsAuthor | Unset = UNSET
    documents: (
        CollectionsSingleGetResponseDataRelationshipsDocuments | Unset
    ) = UNSET
    downstream_collections: (
        CollectionsSingleGetResponseDataRelationshipsDownstreamCollections
        | Unset
    ) = UNSET
    project: CollectionsSingleGetResponseDataRelationshipsProject | Unset = (
        UNSET
    )
    reused_from: (
        CollectionsSingleGetResponseDataRelationshipsReusedFrom | Unset
    ) = UNSET
    rich_pages: (
        CollectionsSingleGetResponseDataRelationshipsRichPages | Unset
    ) = UNSET
    test_runs: (
        CollectionsSingleGetResponseDataRelationshipsTestRuns | Unset
    ) = UNSET
    upstream_collections: (
        CollectionsSingleGetResponseDataRelationshipsUpstreamCollections
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
        from ..models.collections_single_get_response_data_relationships_author import (
            CollectionsSingleGetResponseDataRelationshipsAuthor,
        )
        from ..models.collections_single_get_response_data_relationships_documents import (
            CollectionsSingleGetResponseDataRelationshipsDocuments,
        )
        from ..models.collections_single_get_response_data_relationships_downstream_collections import (
            CollectionsSingleGetResponseDataRelationshipsDownstreamCollections,
        )
        from ..models.collections_single_get_response_data_relationships_project import (
            CollectionsSingleGetResponseDataRelationshipsProject,
        )
        from ..models.collections_single_get_response_data_relationships_reused_from import (
            CollectionsSingleGetResponseDataRelationshipsReusedFrom,
        )
        from ..models.collections_single_get_response_data_relationships_rich_pages import (
            CollectionsSingleGetResponseDataRelationshipsRichPages,
        )
        from ..models.collections_single_get_response_data_relationships_test_runs import (
            CollectionsSingleGetResponseDataRelationshipsTestRuns,
        )
        from ..models.collections_single_get_response_data_relationships_upstream_collections import (
            CollectionsSingleGetResponseDataRelationshipsUpstreamCollections,
        )

        d = dict(src_dict)
        _author = d.pop("author", UNSET)
        author: CollectionsSingleGetResponseDataRelationshipsAuthor | Unset
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = (
                CollectionsSingleGetResponseDataRelationshipsAuthor.from_dict(
                    _author
                )
            )

        _documents = d.pop("documents", UNSET)
        documents: (
            CollectionsSingleGetResponseDataRelationshipsDocuments | Unset
        )
        if isinstance(_documents, Unset):
            documents = UNSET
        else:
            documents = CollectionsSingleGetResponseDataRelationshipsDocuments.from_dict(
                _documents
            )

        _downstream_collections = d.pop("downstreamCollections", UNSET)
        downstream_collections: (
            CollectionsSingleGetResponseDataRelationshipsDownstreamCollections
            | Unset
        )
        if isinstance(_downstream_collections, Unset):
            downstream_collections = UNSET
        else:
            downstream_collections = CollectionsSingleGetResponseDataRelationshipsDownstreamCollections.from_dict(
                _downstream_collections
            )

        _project = d.pop("project", UNSET)
        project: CollectionsSingleGetResponseDataRelationshipsProject | Unset
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = (
                CollectionsSingleGetResponseDataRelationshipsProject.from_dict(
                    _project
                )
            )

        _reused_from = d.pop("reusedFrom", UNSET)
        reused_from: (
            CollectionsSingleGetResponseDataRelationshipsReusedFrom | Unset
        )
        if isinstance(_reused_from, Unset):
            reused_from = UNSET
        else:
            reused_from = CollectionsSingleGetResponseDataRelationshipsReusedFrom.from_dict(
                _reused_from
            )

        _rich_pages = d.pop("richPages", UNSET)
        rich_pages: (
            CollectionsSingleGetResponseDataRelationshipsRichPages | Unset
        )
        if isinstance(_rich_pages, Unset):
            rich_pages = UNSET
        else:
            rich_pages = CollectionsSingleGetResponseDataRelationshipsRichPages.from_dict(
                _rich_pages
            )

        _test_runs = d.pop("testRuns", UNSET)
        test_runs: (
            CollectionsSingleGetResponseDataRelationshipsTestRuns | Unset
        )
        if isinstance(_test_runs, Unset):
            test_runs = UNSET
        else:
            test_runs = CollectionsSingleGetResponseDataRelationshipsTestRuns.from_dict(
                _test_runs
            )

        _upstream_collections = d.pop("upstreamCollections", UNSET)
        upstream_collections: (
            CollectionsSingleGetResponseDataRelationshipsUpstreamCollections
            | Unset
        )
        if isinstance(_upstream_collections, Unset):
            upstream_collections = UNSET
        else:
            upstream_collections = CollectionsSingleGetResponseDataRelationshipsUpstreamCollections.from_dict(
                _upstream_collections
            )

        collections_single_get_response_data_relationships_obj = cls(
            author=author,
            documents=documents,
            downstream_collections=downstream_collections,
            project=project,
            reused_from=reused_from,
            rich_pages=rich_pages,
            test_runs=test_runs,
            upstream_collections=upstream_collections,
        )

        collections_single_get_response_data_relationships_obj.additional_properties = d
        return collections_single_get_response_data_relationships_obj

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

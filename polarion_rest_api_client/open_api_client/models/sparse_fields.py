# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SparseFields")


@_attrs_define
class SparseFields:
    """
    Attributes:
        categories (str | Unset): Requested fields Example: @all.
        collections (str | Unset): Requested fields Example: @all.
        customfields (str | Unset): Requested fields Example: @all.
        document_attachments (str | Unset): Requested fields Example: @all.
        document_comments (str | Unset): Requested fields Example: @all.
        document_parts (str | Unset): Requested fields Example: @all.
        documents (str | Unset): Requested fields Example: @all.
        enumerations (str | Unset): Requested fields Example: @all.
        externallylinkedworkitems (str | Unset): Requested fields Example: @all.
        featureselections (str | Unset): Requested fields Example: @all.
        globalroles (str | Unset): Requested fields Example: @all.
        icons (str | Unset): Requested fields Example: @all.
        jobs (str | Unset): Requested fields Example: @all.
        license_ (str | Unset): Requested fields Example: @all.
        license_assignments (str | Unset): Requested fields Example: @all.
        license_slots (str | Unset): Requested fields Example: @all.
        license_types (str | Unset): Requested fields Example: @all.
        linkedoslcresources (str | Unset): Requested fields Example: @all.
        linkedworkitems (str | Unset): Requested fields Example: @all.
        llms (str | Unset): Requested fields Example: @all.
        metadata (str | Unset): Requested fields Example: @all.
        page_attachments (str | Unset): Requested fields Example: @all.
        page_comments (str | Unset): Requested fields Example: @all.
        pages (str | Unset): Requested fields Example: @all.
        plans (str | Unset): Requested fields Example: @all.
        projectroles (str | Unset): Requested fields Example: @all.
        projects (str | Unset): Requested fields Example: @all.
        projecttemplates (str | Unset): Requested fields Example: @all.
        revisions (str | Unset): Requested fields Example: @all.
        testparameter_definitions (str | Unset): Requested fields Example: @all.
        testparameters (str | Unset): Requested fields Example: @all.
        testrecord_attachments (str | Unset): Requested fields Example: @all.
        testrecords (str | Unset): Requested fields Example: @all.
        testrun_attachments (str | Unset): Requested fields Example: @all.
        testrun_comments (str | Unset): Requested fields Example: @all.
        testruns (str | Unset): Requested fields Example: @all.
        teststep_results (str | Unset): Requested fields Example: @all.
        teststepresult_attachments (str | Unset): Requested fields Example: @all.
        teststeps (str | Unset): Requested fields Example: @all.
        usergroups (str | Unset): Requested fields Example: @all.
        users (str | Unset): Requested fields Example: @all.
        workitem_approvals (str | Unset): Requested fields Example: @all.
        workitem_attachments (str | Unset): Requested fields Example: @all.
        workitem_comments (str | Unset): Requested fields Example: @all.
        workitems (str | Unset): Requested fields Example: @all.
        workrecords (str | Unset): Requested fields Example: @all.
    """

    categories: str | Unset = UNSET
    collections: str | Unset = UNSET
    customfields: str | Unset = UNSET
    document_attachments: str | Unset = UNSET
    document_comments: str | Unset = UNSET
    document_parts: str | Unset = UNSET
    documents: str | Unset = UNSET
    enumerations: str | Unset = UNSET
    externallylinkedworkitems: str | Unset = UNSET
    featureselections: str | Unset = UNSET
    globalroles: str | Unset = UNSET
    icons: str | Unset = UNSET
    jobs: str | Unset = UNSET
    license_: str | Unset = UNSET
    license_assignments: str | Unset = UNSET
    license_slots: str | Unset = UNSET
    license_types: str | Unset = UNSET
    linkedoslcresources: str | Unset = UNSET
    linkedworkitems: str | Unset = UNSET
    llms: str | Unset = UNSET
    metadata: str | Unset = UNSET
    page_attachments: str | Unset = UNSET
    page_comments: str | Unset = UNSET
    pages: str | Unset = UNSET
    plans: str | Unset = UNSET
    projectroles: str | Unset = UNSET
    projects: str | Unset = UNSET
    projecttemplates: str | Unset = UNSET
    revisions: str | Unset = UNSET
    testparameter_definitions: str | Unset = UNSET
    testparameters: str | Unset = UNSET
    testrecord_attachments: str | Unset = UNSET
    testrecords: str | Unset = UNSET
    testrun_attachments: str | Unset = UNSET
    testrun_comments: str | Unset = UNSET
    testruns: str | Unset = UNSET
    teststep_results: str | Unset = UNSET
    teststepresult_attachments: str | Unset = UNSET
    teststeps: str | Unset = UNSET
    usergroups: str | Unset = UNSET
    users: str | Unset = UNSET
    workitem_approvals: str | Unset = UNSET
    workitem_attachments: str | Unset = UNSET
    workitem_comments: str | Unset = UNSET
    workitems: str | Unset = UNSET
    workrecords: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        categories = self.categories

        collections = self.collections

        customfields = self.customfields

        document_attachments = self.document_attachments

        document_comments = self.document_comments

        document_parts = self.document_parts

        documents = self.documents

        enumerations = self.enumerations

        externallylinkedworkitems = self.externallylinkedworkitems

        featureselections = self.featureselections

        globalroles = self.globalroles

        icons = self.icons

        jobs = self.jobs

        license_ = self.license_

        license_assignments = self.license_assignments

        license_slots = self.license_slots

        license_types = self.license_types

        linkedoslcresources = self.linkedoslcresources

        linkedworkitems = self.linkedworkitems

        llms = self.llms

        metadata = self.metadata

        page_attachments = self.page_attachments

        page_comments = self.page_comments

        pages = self.pages

        plans = self.plans

        projectroles = self.projectroles

        projects = self.projects

        projecttemplates = self.projecttemplates

        revisions = self.revisions

        testparameter_definitions = self.testparameter_definitions

        testparameters = self.testparameters

        testrecord_attachments = self.testrecord_attachments

        testrecords = self.testrecords

        testrun_attachments = self.testrun_attachments

        testrun_comments = self.testrun_comments

        testruns = self.testruns

        teststep_results = self.teststep_results

        teststepresult_attachments = self.teststepresult_attachments

        teststeps = self.teststeps

        usergroups = self.usergroups

        users = self.users

        workitem_approvals = self.workitem_approvals

        workitem_attachments = self.workitem_attachments

        workitem_comments = self.workitem_comments

        workitems = self.workitems

        workrecords = self.workrecords

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if categories is not UNSET:
            field_dict["categories"] = categories
        if collections is not UNSET:
            field_dict["collections"] = collections
        if customfields is not UNSET:
            field_dict["customfields"] = customfields
        if document_attachments is not UNSET:
            field_dict["document_attachments"] = document_attachments
        if document_comments is not UNSET:
            field_dict["document_comments"] = document_comments
        if document_parts is not UNSET:
            field_dict["document_parts"] = document_parts
        if documents is not UNSET:
            field_dict["documents"] = documents
        if enumerations is not UNSET:
            field_dict["enumerations"] = enumerations
        if externallylinkedworkitems is not UNSET:
            field_dict["externallylinkedworkitems"] = externallylinkedworkitems
        if featureselections is not UNSET:
            field_dict["featureselections"] = featureselections
        if globalroles is not UNSET:
            field_dict["globalroles"] = globalroles
        if icons is not UNSET:
            field_dict["icons"] = icons
        if jobs is not UNSET:
            field_dict["jobs"] = jobs
        if license_ is not UNSET:
            field_dict["license"] = license_
        if license_assignments is not UNSET:
            field_dict["license_assignments"] = license_assignments
        if license_slots is not UNSET:
            field_dict["license_slots"] = license_slots
        if license_types is not UNSET:
            field_dict["license_types"] = license_types
        if linkedoslcresources is not UNSET:
            field_dict["linkedoslcresources"] = linkedoslcresources
        if linkedworkitems is not UNSET:
            field_dict["linkedworkitems"] = linkedworkitems
        if llms is not UNSET:
            field_dict["llms"] = llms
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if page_attachments is not UNSET:
            field_dict["page_attachments"] = page_attachments
        if page_comments is not UNSET:
            field_dict["page_comments"] = page_comments
        if pages is not UNSET:
            field_dict["pages"] = pages
        if plans is not UNSET:
            field_dict["plans"] = plans
        if projectroles is not UNSET:
            field_dict["projectroles"] = projectroles
        if projects is not UNSET:
            field_dict["projects"] = projects
        if projecttemplates is not UNSET:
            field_dict["projecttemplates"] = projecttemplates
        if revisions is not UNSET:
            field_dict["revisions"] = revisions
        if testparameter_definitions is not UNSET:
            field_dict["testparameter_definitions"] = testparameter_definitions
        if testparameters is not UNSET:
            field_dict["testparameters"] = testparameters
        if testrecord_attachments is not UNSET:
            field_dict["testrecord_attachments"] = testrecord_attachments
        if testrecords is not UNSET:
            field_dict["testrecords"] = testrecords
        if testrun_attachments is not UNSET:
            field_dict["testrun_attachments"] = testrun_attachments
        if testrun_comments is not UNSET:
            field_dict["testrun_comments"] = testrun_comments
        if testruns is not UNSET:
            field_dict["testruns"] = testruns
        if teststep_results is not UNSET:
            field_dict["teststep_results"] = teststep_results
        if teststepresult_attachments is not UNSET:
            field_dict["teststepresult_attachments"] = (
                teststepresult_attachments
            )
        if teststeps is not UNSET:
            field_dict["teststeps"] = teststeps
        if usergroups is not UNSET:
            field_dict["usergroups"] = usergroups
        if users is not UNSET:
            field_dict["users"] = users
        if workitem_approvals is not UNSET:
            field_dict["workitem_approvals"] = workitem_approvals
        if workitem_attachments is not UNSET:
            field_dict["workitem_attachments"] = workitem_attachments
        if workitem_comments is not UNSET:
            field_dict["workitem_comments"] = workitem_comments
        if workitems is not UNSET:
            field_dict["workitems"] = workitems
        if workrecords is not UNSET:
            field_dict["workrecords"] = workrecords

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        categories = d.pop("categories", UNSET)

        collections = d.pop("collections", UNSET)

        customfields = d.pop("customfields", UNSET)

        document_attachments = d.pop("document_attachments", UNSET)

        document_comments = d.pop("document_comments", UNSET)

        document_parts = d.pop("document_parts", UNSET)

        documents = d.pop("documents", UNSET)

        enumerations = d.pop("enumerations", UNSET)

        externallylinkedworkitems = d.pop("externallylinkedworkitems", UNSET)

        featureselections = d.pop("featureselections", UNSET)

        globalroles = d.pop("globalroles", UNSET)

        icons = d.pop("icons", UNSET)

        jobs = d.pop("jobs", UNSET)

        license_ = d.pop("license", UNSET)

        license_assignments = d.pop("license_assignments", UNSET)

        license_slots = d.pop("license_slots", UNSET)

        license_types = d.pop("license_types", UNSET)

        linkedoslcresources = d.pop("linkedoslcresources", UNSET)

        linkedworkitems = d.pop("linkedworkitems", UNSET)

        llms = d.pop("llms", UNSET)

        metadata = d.pop("metadata", UNSET)

        page_attachments = d.pop("page_attachments", UNSET)

        page_comments = d.pop("page_comments", UNSET)

        pages = d.pop("pages", UNSET)

        plans = d.pop("plans", UNSET)

        projectroles = d.pop("projectroles", UNSET)

        projects = d.pop("projects", UNSET)

        projecttemplates = d.pop("projecttemplates", UNSET)

        revisions = d.pop("revisions", UNSET)

        testparameter_definitions = d.pop("testparameter_definitions", UNSET)

        testparameters = d.pop("testparameters", UNSET)

        testrecord_attachments = d.pop("testrecord_attachments", UNSET)

        testrecords = d.pop("testrecords", UNSET)

        testrun_attachments = d.pop("testrun_attachments", UNSET)

        testrun_comments = d.pop("testrun_comments", UNSET)

        testruns = d.pop("testruns", UNSET)

        teststep_results = d.pop("teststep_results", UNSET)

        teststepresult_attachments = d.pop("teststepresult_attachments", UNSET)

        teststeps = d.pop("teststeps", UNSET)

        usergroups = d.pop("usergroups", UNSET)

        users = d.pop("users", UNSET)

        workitem_approvals = d.pop("workitem_approvals", UNSET)

        workitem_attachments = d.pop("workitem_attachments", UNSET)

        workitem_comments = d.pop("workitem_comments", UNSET)

        workitems = d.pop("workitems", UNSET)

        workrecords = d.pop("workrecords", UNSET)

        sparse_fields_obj = cls(
            categories=categories,
            collections=collections,
            customfields=customfields,
            document_attachments=document_attachments,
            document_comments=document_comments,
            document_parts=document_parts,
            documents=documents,
            enumerations=enumerations,
            externallylinkedworkitems=externallylinkedworkitems,
            featureselections=featureselections,
            globalroles=globalroles,
            icons=icons,
            jobs=jobs,
            license_=license_,
            license_assignments=license_assignments,
            license_slots=license_slots,
            license_types=license_types,
            linkedoslcresources=linkedoslcresources,
            linkedworkitems=linkedworkitems,
            llms=llms,
            metadata=metadata,
            page_attachments=page_attachments,
            page_comments=page_comments,
            pages=pages,
            plans=plans,
            projectroles=projectroles,
            projects=projects,
            projecttemplates=projecttemplates,
            revisions=revisions,
            testparameter_definitions=testparameter_definitions,
            testparameters=testparameters,
            testrecord_attachments=testrecord_attachments,
            testrecords=testrecords,
            testrun_attachments=testrun_attachments,
            testrun_comments=testrun_comments,
            testruns=testruns,
            teststep_results=teststep_results,
            teststepresult_attachments=teststepresult_attachments,
            teststeps=teststeps,
            usergroups=usergroups,
            users=users,
            workitem_approvals=workitem_approvals,
            workitem_attachments=workitem_attachments,
            workitem_comments=workitem_comments,
            workitems=workitems,
            workrecords=workrecords,
        )

        sparse_fields_obj.additional_properties = d
        return sparse_fields_obj

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

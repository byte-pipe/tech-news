---
title: '(re)introducing kpt: Your toolchain for infrastructure automation | CNCF'
url: https://www.cncf.io/blog/2026/07/02/reintroducing-kpt-your-toolchain-for-infrastructure-automation/
site_name: tldr
content_file: tldr-reintroducing-kpt-your-toolchain-for-infrastructur
fetched_at: '2026-07-03T19:33:10.556324'
original_url: https://www.cncf.io/blog/2026/07/02/reintroducing-kpt-your-toolchain-for-infrastructure-automation/
date: '2026-07-03'
published_date: '2026-07-02T15:01:38+00:00'
description: The opening tagline of the kpt documentation describes it as “… a package-centric toolchain that enables a WYSIWYG configuration authoring, automation…
tags:
- tldr
---

Posted on July 2, 2026by Ciaran Johnston, Ericsson

CNCF projects highlighted in this post

## What is kpt?

The opening tagline of the kpt documentation describes it as

“… a package-centric toolchain that enables a WYSIWYG configuration authoring, automation, and delivery experience, which simplifies managing Kubernetes platforms and KRM-driven infrastructure at scale by manipulating declarative Configuration as Data.”

This is a concise and detailed description of kpt, but sometimes it feels like it was written by a lawyer, or a consultant on a per-industry-buzzword contract. Let’s break it down.

### package-centric

Kpt works on packages – specifically bundles of Kubernetes Resource Model (KRM) files, declarative YAML manifests that define the desired state of cluster resources for Kubernetes (or Kubernetes Operator extensions) to continuously reconcile. These are pretty lightweight – they can be a directory on your computer, a zip file, or (most typically, given the GitOps nature of kpt) the contents of a git repository or git repository subfolder.

### toolchain

Kpt is a CLI, but also provides a number of tools – validators and mutators – that can be executed in a kpt pipeline to verify and / or modify the contents of a kpt package.

### WYSIWYG

What You See Is What You Get is more typically associated with graphical editing tools or print-friendly editors. In this context, it refers to the fact that the kpt file contents you have at any point in time are exactly the resources that will end up in your cluster – they are not modified out-of-band on the way to the cluster, nor do they depend on external templates or metamodels.

### configuration authoring, automation, and delivery

kpt supports the full lifecycle of a package of kubernetes resource descriptors. The CLI supports bootstrapping a new package with the basic content and configuration templates, while kpt pipelines provide a mechanism to automate the process of specializing those templates into site-specific parameterized packages, potentially across hundreds of different sites. Kpt also supports the package review and validation processes required to ensure configuration correctness before applying to live networks. Finally, kpt can be used to deploy packages to a live environment, monitoring their reconciliation status as it does so.

However, kpt is modular and can be integrated into any existing Kubernetes-centric toolchain to provide some or all of the automation capabilities.

### managing Kubernetes platforms and KRM-driven infrastructure

Kpt’s primary raison d’etre is the management of Kubernetes-native constructs – manipulating KRM files which enable Kubernetes tooling to robustly and autonomously deploy clusters, provision workloads into clusters and even manage the day-to-day configurations of those workloads. If it can be described in KRM, it can be packaged and automated using kpt.

### manipulating declarative Configuration as Data

Configuration as Data is an approach where system and application configuration is stored, managed, and versioned as plain data, rather than embedded with code that must be executed to be understood.

The key benefits of this approach include:

* Auditability: because config is plain structured data, you can diff it, lint it, and review it without running anything. A diff tells you exactly what changed between two versions of your system state before applying to the cluster
* Separation of concerns: logic lives in functions/controllers; intent lives in data. This makes both easier to reason about independently. You can validate the data against a schema without invoking any business logic
* Composability: different tools can read, transform and validate the same data models, enabling function chaining and independently testable mutation phases

### Why do we need it?

Given the proliferation of infrastructure orchestration and configuration management tools out there, it’s a fair question to ask – why kpt? There are a few reasons why we feel the kpt project has a unique value in the Kubernetes automation ecosystem.

Firstly, kpt’s “in-place” update paradigm differs from other tools, such as Kustomize, which generate final manifests on the fly during render / apply phase by overlaying patches on a base configuration. It’s our view that being able to examine, and optionally approve, the final configurations before applying simplifies troubleshooting and fault resolution. This is what we describe as “WYSIWYG”.

Secondly, the paradigm of “configuration as data” is fundamentally different to the “configuration as code” approach many other tools adopt. By clearly separating configurations in packages (pure KRM models) from the business logic which transforms them (KRM functions), there is a clean separation of concerns. Data files describe precisely the desired state, and native tooling can process and validate them. This reduces side effects, drift, and complexity. Connecting with the “in-place” paradigm means the pure configuration data that precisely describes the desired state is available for auditing and verification, reducing operational risk and making deployments more deterministic.

Lastly, kpt doesn’t try to solve all problems. It is a simple tool with a core set of capabilities, leveraging an extensible library of functions to support common needs and allowing users to bring their own business logic. It integrates well with other gitops tools – ArgoCD, Flux, Helm and Porch to name a few – allowing it to coexist well in the broader Kubernetes ecosystem.

### Use cases for kpt

The suite of examples available in the kpt repo include basic examples using WordPress, nginx and so on. The “kpt-samples” repository includes a new example using theHeadlampproject, and we hope to add more such examples of off-the-shelf tools that can benefit from packaging using kpt in the near future.

The most robust and complex suite of examples available for the use of kpt in theNephioproject, where kpt forms a critical part of the end-to-end toolchain for defining and specializing the deployment of open source RAN and core networks on top of Kubernetes.

Finally we hope to have a working example of a more complex, multi-site and multi-service deployment scenario using kpt and a more typical IT workload over the summer. Watch this space, and please let us know if you are using kpt in your own toolchains!

### Current status and plans

The kpt project has recently been fully onboarded into CNCF as a sandbox project. We would like to see it grow in usage and build a bigger community of users. The plans for world domination include making a number of changes to the way pipelines execute, to improve performance, allow for optional steps, enable external connectivity and improving documentation amongst others. We will be undertaking a significant restructuring of the documentation to improve readability and align with industry best practices. Secrets handling, multi-cluster support and helm support are oft-requested features and the aim is to stabilise the kpt APIs to release v1, so that end users can have confidence in the stability of their packages.

### Join us!

The kpt project meets weekly, on Wednesdays at 2pm CET. We useGitHubto collaborate onissuesanddiscussionsand we use thekpt channelon the Kubernetes slack for ad hoc communication.

If what you see interests you and you would like to know more, please reach out. If you are already using kpt and would like to see a new feature, or want to help improve it, please reach out – we would be delighted to see you!
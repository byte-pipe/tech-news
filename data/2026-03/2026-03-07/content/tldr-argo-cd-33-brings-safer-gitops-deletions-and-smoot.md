---
title: Argo CD 3.3 Brings Safer GitOps Deletions and Smoother Day‑to‑Day Operations - InfoQ
url: https://www.infoq.com/news/2026/02/argocd-33/
site_name: tldr
content_file: tldr-argo-cd-33-brings-safer-gitops-deletions-and-smoot
fetched_at: '2026-03-07T11:07:30.667393'
original_url: https://www.infoq.com/news/2026/02/argocd-33/
date: '2026-03-07'
description: The application deployment and lifecycle management tool Argo CD has reached a new milestone with the release of version 3.3, extending the capabilities of the popular GitOps continuous delivery tool
tags:
- tldr
---

InfoQ HomepageNewsArgo CD 3.3 Brings Safer GitOps Deletions and Smoother Day‑to‑Day Operations

 DevOps


QCon London (March 16-19, 2026): Learn proven architectural practices to scale your systems faster.

# Argo CD 3.3 Brings Safer GitOps Deletions and Smoother Day‑to‑Day Operations

Feb 28, 20264
									min read

by

* Matt Saunders

#### Write for InfoQ

Feed your curiosity.

Help 550k+ global
senior developers
each month stay ahead.
Get in touch

The application deployment and lifecycle management toolArgo CDhas reached a new milestone with the release of version 3.3, extending the capabilities of the popular GitOps continuous delivery tool while addressing several long-standing pain points for operators.

Argo CD 3.3 is presented as a practical release that closes several long-standing gaps in day-to-day GitOps operations rather than a major architectural change. The release candidate focuses on deletion safety, authentication experience, repository performance and more precise control for cluster and autoscaling resources.​

In theannouncement blog post, published at the time when the release candidate became available, software engineerPeter JiangintroducesPreDeletehooks as the most visible change in Argo CD 3.3, completing the existing lifecycle ofPreSync,SyncandPostSynchooks. In the blog, Jiang explains that users have historically relied on external scripts, manual cleanup or Kubernetes finalisers to prepare for application deletion, which often proved fragile or opaque when teams needed a predictable teardown sequence.PreDeletehooks instead allow teams to define Kubernetes resources, such as Jobs that must run and succeed before Argo CD proceeds with deleting the rest of an application's resources, and a failing hook will block deletion. In practice, this turns deletion into an explicit lifecycle phase that can include data export, draining traffic or notifying dependent systems.​

The second major feature in the release is OIDC background token refresh, which addresses frequent complaints from users integrating Argo CD with providers such as Keycloak. Previously, engineers could be logged out of the user interface after a short access token lifetime even while actively working, which was a source of frustration during longer debugging or deployment sessions. The new behaviour automatically refreshes OIDC tokens in the background before expiry, governed by a configurable threshold that determines how much remaining lifetime triggers a refresh. Deepak Yadav,writing on LinkedIn, highlights this as one of the standout changes and summarises it as "Goodbye random logouts", reflecting how strongly this issue was felt.​

Optional shallow cloning of Git repositories has also been added. When enabled, Argo CD fetches only the required commit history instead of the full repository, which the announcement notes can reduce fetch times from minutes to seconds in larger monorepos or long-lived projects. This feature is implemented as a flag in repository configuration, making it an opt-in performance optimisation for operators who have assessed that they do not need full history for their workflows. Community posts describing top highlights for 3.3 consistently include shallow cloning alongsidePreDeletehooks and OIDC refresh.​

The announcement also notes improvements to the Source Hydrator, an increasingly central part of Argo CD's handling of complex configuration workflows. The new version introduces inline parameter support so that teams no longer need to commit separate parameter files for each configuration change, and adds better support for monorepo layouts, together with performance work to avoid unnecessary calls to the repo server. Jiang attributes these changes to community contributors and frames them as part of an ongoing effort to make Argo CD more appropriate for large-scale configuration management. These changes place the Source Hydrator alongside earlier work onApplicationSetsas a mechanism for handling growing configuration complexity in multi-application deployments.​

Granular control over cluster resources is also improved in 3.3. The release extendsclusterResourceWhitelistinAppProjectsso that access can be restricted not only by API group and kind but also by individual resource names. This allows a project to manage only specificCustomResourceDefinitionsrather than all CRDs, which the announcement describes as a long-standing request from users who maintain multiple teams and controllers on shared clusters. Commentary on LinkedIn highlights this change as part of a broader improvement in RBAC controls, noting that more precise scoping of CRDs aligns better with organisational security policies and separation of duties.​

The release also introduces first-class support for KEDA, the Kubernetes Event-driven Autoscaling project. Argo CD can now pause and resume KEDAScaledObjectsandScaledJobsdirectly from the user interface and understands ScaledJob health states, replacing earlier generic "Unknown" indicators. Community posts describe this as particularly useful for maintenance windows and debugging, since operators can temporarily suspend event-driven workloads through the same GitOps control surface they use for other application resources.​

Beyond these headline features, Jiang lists a series of smaller changes that collectively support a more incremental view of improvement. These include using volume mounts for Redis credentials, adding Ceph CRD health checks, evolving theApplicationSetuser interface, supporting CLI filtering by API group, configurable Kubernetes API timeouts, and several user interface refinements around refresh behaviour and view extensions.

Overall, v3.3 feels like a release shaped by real operational pain. Well done to the Argo CD maintainers and contributors — this is a solid step forward.

-Deepak Yadav

Alongside Argo CD,Fluxhas emerged as the other major CNCF‑incubated project implementing GitOps for Kubernetes, but it emphasises a controller-driven model rather than a centralised web application. Flux runs a set of controllers that reconcile Git, Helm repositories and container registries with the cluster, supports Helm and Kustomize natively, and offers optional visualisation through the Weave GitOps interface rather than a bundled dashboard. It uses concepts such as pruning and protective annotations on resources to do safe deletions, allowing operators to prevent specific objects from being removed during reconciliation and to tune how aggressively Flux cleans up resources that disappear from version control.

Argo CD and Flux are often positioned as complementary rather than strictly competing. Argo CD’s built-in UI and close integration with Argo Rollouts make it attractive for organisations that want visual control and first-class canary or blue-green deployments. Flux’s GitOps Toolkit provides a composable, CLI-oriented stack that monitors image registries and automatically updates manifests. Users on Reddit report running both tools together. For example, using Flux to manage core cluster infrastructure and Argo CD to orchestrate application-level deployments.

Argo CD 3.3.2 isavailable now.



## About the Author







#### Matt Saunders

Show more
Show less

### Rate this Article

Adoption

Style

 Author Contacted

#### This content is in theDevOpstopic

##### Related Topics:

* DevOps
* GitOps
* Continuous Delivery
* Argo CD

* #### Related Editorial
* #### Related Sponsors
* #### Related SponsorApril 16, 2026, 1 PM EDT##### Designing a Control Plane for Cloud Infrastructure: Governance, State, and Continuous OrchestrationPresented by: Mrinalini Sugosh - Sr Product Marketing Manager at Harness
* April 16, 2026, 1 PM EDT##### Designing a Control Plane for Cloud Infrastructure: Governance, State, and Continuous OrchestrationPresented by: Mrinalini Sugosh - Sr Product Marketing Manager at Harness

### Related Content

### The InfoQNewsletter

A round-up of last week’s content on InfoQ sent out every Tuesday. Join a community of over 250,000 senior developers.View an example

Enter your e-mail address

Select your country

Select a country

I consent to InfoQ.com handling my data as explained in this
Privacy Notice
.

We protect your privacy.

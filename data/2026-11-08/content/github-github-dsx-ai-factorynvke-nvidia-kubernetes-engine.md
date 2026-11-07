---
title: 'GitHub - dsx-ai-factory/nvke: NVIDIA Kubernetes Engine (NVKE). A management plane for GPU Kubernetes on bare metal. · GitHub'
url: https://github.com/dsx-ai-factory/nvke
site_name: github
content_file: github-github-dsx-ai-factorynvke-nvidia-kubernetes-engine
fetched_at: '2026-11-08T09:02:55.825314'
original_url: https://github.com/dsx-ai-factory/nvke
author: dsx-ai-factory
description: NVIDIA Kubernetes Engine (NVKE). A management plane for GPU Kubernetes on bare metal. - dsx-ai-factory/nvke
---

main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

1,548 Commits
1,548 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.claude
.claude
 
 
.flox
.flox
 
 
.github
.github
 
 
agent
agent
 
 
auth
auth
 
 
benchmarks
benchmarks
 
 
build
build
 
 
cli
cli
 
 
cluster-api-provider-provisioned
cluster-api-provider-provisioned
 
 
controller
controller
 
 
deploy
deploy
 
 
docs
docs
 
 
fern
fern
 
 
hack
hack
 
 
make
make
 
 
management-engine
management-engine
 
 
nktp
nktp
 
 
os-image
os-image
 
 
release
release
 
 
scripts
scripts
 
 
tools
tools
 
 
.coderabbit.yaml
.coderabbit.yaml
 
 
.dockerignore
.dockerignore
 
 
.envrc
.envrc
 
 
.flox-cli-version
.flox-cli-version
 
 
.gitignore
.gitignore
 
 
.gitleaks.toml
.gitleaks.toml
 
 
.grype.yaml
.grype.yaml
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
GOVERNANCE.md
GOVERNANCE.md
 
 
LICENSE
LICENSE
 
 
MAINTAINERS.md
MAINTAINERS.md
 
 
Makefile
Makefile
 
 
NOTICE
NOTICE
 
 
README.md
README.md
 
 
RELEASE.md
RELEASE.md
 
 
ROADMAP.md
ROADMAP.md
 
 
SECURITY.md
SECURITY.md
 
 
SUPPORT.md
SUPPORT.md
 
 
THIRD_PARTY_NOTICES.md
THIRD_PARTY_NOTICES.md
 
 
go.work
go.work
 
 
go.work.sum
go.work.sum
 
 
View all files

## Repository files navigation

# NVIDIA Kubernetes Engine (NVKE)

Run a managed Kubernetes service on your own NVIDIA GPU infrastructure.NVIDIA Kubernetes® Engine (NVKE) provides the management plane that platform teams install to create and
operate Kubernetes clusters for their customers. Each workload cluster has its
own Kubernetes control plane, etcd and node pools. You operate the NVKE management
plane; your customers use their clusters through the Kubernetes API andkubectl.

Preview:NVKE is available as a preview. APIs, configuration and behavior
can change between releases, and we do not recommend NVKE for production
workloads. SeePreview status and known limitations.

Get started·Documentation·Contribute·Get help

## Getting started

Your goal

Start here

What you get

Evaluate without GPU hardware

Local quickstart

A development management plane and a workload cluster on simulated machines. No NVIDIA account is required.

Install on your infrastructure

Plan your installation

The prerequisites and sequence for preparing nodes, bootstrapping a management cluster and installing its services.

Build or contribute

Build from source

The NVKE binaries and the contributor development loop.

The local quickstart runs on aLinux host or VM, amd64 or arm64, with at least6 CPUs, 12 GiB of free memory and 100 GiB of free disk. It requires Docker,
virtual TPM support and the tools listed in the guide. Follow its setup through
workload-cluster creation and confirm the cluster's nodes reportReady.
On macOS, use thelocal site guide, which runs
the evaluation inside a Colima virtual machine.

For a real installation, you supply the machines, networking, node images and
registries, and configure access toNVIDIA Infra Controller (NICo). NICo is
the sole compatible infrastructure provider at preview. Theplatform and version referencelists
validated combinations and pinned dependencies.

## What NVKE does

* Creates independent workload clusters.Request clusters through the NVKE
API ornvkectl; NVKE provisions machines through NICo and forms Kubernetes
clusters with their own control planes.
* Manages workload cluster lifecycle.Create, scale and delete node pools,
upgrade Kubernetes and replace nodes. See thenode pool guidefor the manual steps and preview limits on replacement and upgrades.
* Establishes node identity.Nodes attest through SPIFFE/SPIRE using their
TPM before receiving join credentials. Encryption of etcd data is available
per cluster.
* Connects builds to deployment.Its companion project,NVIDIA Kubernetes Recipes (NVKR),
builds node images and NVKE components from pinned inputs. NVKE deploys those
artifacts; NVKR owns their build and release evidence.

The preview needs explicit operator configuration: API authentication is off
and the API uses plain HTTP after installation. ConfigureAPI authentication and protected accessbefore admitting callers. The management cluster does not upgrade, scale or
replace itself, and there is no management-plane upgrade or backup/restore
procedure. FDE node images are for evaluation and provide no data-at-rest
confidentiality. Read theknown limitationsbefore choosing an evaluation or installation path.

## Overview

The diagram shows the NVKE product family, how it sits on NICo and your GPU machines, and which components talk to each other.

NVKE is not a Kubernetes distribution and not a Cluster API flavour. It is aself-hosting factory for Kubernetes clusters: a throwaway seed cluster
stands up a management cluster, and the management plane on
it then provisions and lifecycle-manages many isolated workload clusters
on demand.

An installation has two kinds of Kubernetes cluster:

* Themanagement clusterruns the NVKE management plane and infrastructure
controllers.nvkectlforms it using a temporary seed cluster; installing the
management-plane services is a separate step.
* Workload clustersrun customer applications. The management plane creates
and operates them through NICo, Cluster API and the node agent.

ReadWhat is NVKEfor the operator workflow andArchitecturefor the implementation and data flows.

## Build from source

UseGo 1.27.3, the version pinned ingo.work, andGNU Make 4 or later. Public Go modules must be
reachable on the first build.Floxis optional and supplies
the repository's development tools; on macOS, it also supplies GNU Make 4.
SeeDevelopmentfor toolchain setup.

git clone https://github.com/dsx-ai-factory/nvke.git

cd
 nvke
make build

This builds the workspace and writes nine binaries tobin/:agent,updater,controller,nvkectl,capd-reboot-controller,nvke-os-image-check,management-engine,tenant-apiandoperator-api. Building does not start a
management plane or create a cluster. The node agent runs on Linux.

Theworkspace guideexplains the modules and outputs.
For local services and test environments, seeLocal development setup.
Before submitting a change, followCONTRIBUTING.mdand runmake preflight; it selects checks for the modules you changed.

## Documentation

Task

Guide

Prepare nodes and bootstrap the management cluster

Bootstrap the management cluster

Install NVKE services

Install the management plane from the deploy path

Build node images and supply release artifacts

Get NVKE artifacts from NVKR

Create and manage customer clusters

Create a workload cluster
, 
Manage node pools

Give a customer access

Access a workload cluster

Inspect cluster health and telemetry

Observe NVKE and its clusters

Thedocumentation indexlinks the remaining guides and references.

## Contributing and support

Contributions, bug reports and documentation improvements are welcome.
Start withCONTRIBUTING.md; open an issue before substantial
work so maintainers can agree on the approach.

* Questions:GitHub Discussions.
* Chat:the#nvkechannel in the DSX AI Factory Slack.Get an invite.
* Bugs and feature requests:GitHub Issues.
* Security vulnerabilities:followSECURITY.mdand report privately.
* Community:Code of Conduct,Governance,MaintainersandSupport.
* Releases:release process.
* CI health:theCI dashboardshows the last thirty runs of every workflow and refreshes hourly.

## Trademarks

Kubernetes® is a registered trademark of The Linux Foundation in the United
States and other countries. NVIDIA and the NVIDIA logo are trademarks and/or
registered trademarks of NVIDIA Corporation in the U.S. and other countries.
Other company and product names may be trademarks of the respective companies
with which they are associated.

## License

Apache License 2.0. SeeLICENSEandNOTICE.

Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
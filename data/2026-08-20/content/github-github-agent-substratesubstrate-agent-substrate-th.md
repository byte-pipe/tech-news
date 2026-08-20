---
title: 'GitHub - agent-substrate/substrate: Agent Substrate: the core system · GitHub'
url: https://github.com/agent-substrate/substrate
site_name: github
content_file: github-github-agent-substratesubstrate-agent-substrate-th
fetched_at: '2026-08-20T11:23:54.860653'
original_url: https://github.com/agent-substrate/substrate
author: agent-substrate
description: 'Agent Substrate: the core system. Contribute to agent-substrate/substrate development by creating an account on GitHub.'
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 agent-substrate

 

/

substrate

Public

* NotificationsYou must be signed in to change notification settings
* Fork246
* Star1.3k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

587 Commits
587 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.agents/
skills
.agents/
skills
 
 
.github
.github
 
 
LICENSES
LICENSES
 
 
benchmarking
benchmarking
 
 
cmd
cmd
 
 
demos
demos
 
 
docs
docs
 
 
hack
hack
 
 
internal
internal
 
 
manifests
manifests
 
 
pkg
pkg
 
 
tools
tools
 
 
vendor
vendor
 
 
.gitignore
.gitignore
 
 
.golangci.yaml
.golangci.yaml
 
 
.ko.yaml
.ko.yaml
 
 
AGENTS.md
AGENTS.md
 
 
COLLABORATING.md
COLLABORATING.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
GOVERNANCE.md
GOVERNANCE.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
code-of-conduct.md
code-of-conduct.md
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
View all files

## Repository files navigation

# Agent Substrate

NOTE: This is not an officially supported Google product. This project is not
eligible for theGoogle Open Source Software Vulnerability Rewards Program.

## What is Agent Substrate?

Agent Substrate delivers a performant, high density runtime environment for large scale agent deployments. The agent substrate control plane provides full lifecycle management for agent sandboxes, delivering sub-second agent resume/suspend operations, and allows heavy multiplexing of agents onto the same computer infrastructure. It supports multiple sandbox technologies including microVMs and gVisor, enabling consistent lifecycle operations for all sandbox types.

At its core, Agent Substrate maps a larger set of “actors” (applications such as agents) onto a smaller set of ready “workers”, relying on the fact that agent-like applications tend to be idle most of the time to achieve heavy multiplexing. It provides functionality to manage an actor’s lifecycle (e.g. create/destroy, suspend/resume), to assign actors to workers in real time, and to route incoming traffic to them.

Agent Substrate is intended to be a low-opinion system. The workloads it manages don't have to be literal AI agents, but those are the best example of the kind of applications it is designed for. It is not an SDK for building agents, but rather a system for running them at scale.

Agent Substrate leverages Kubernetes for the infrastructure provisioning and worker lifecycle management (Kubernetes Pods). It builds on top of Kubernetes features like Pods and Pod autoscaling, while Agent Substrate provides agent-specific scheduling and control to achieve lower latency. Using Kubernetes as the underlying system enables consistent infrastructure management across all workloads types that are required for end to end agentic deployments and allows holistic infrastructure optimizations for RL scenarios that span agentic, inference and training cycles.

## Demo

Watch the Agent Substrate cluster multiplex ~250 stateful actors across just 8 physical pods.

This demo highlights the core developer experience and "Agentic Infrastructure" capabilities of Substrate:

1. Instant Actor Teleport:High-performance suspend and resume of actors onto any available worker in the pool with sub-second activation.
2. State Persistence:Persistent working memory (volatile RAM) and filesystem state preserved perfectly across hibernation cycles via full-state snapshots.
3. Agent Swarm Multiplexing:Demonstrates 30x+ oversubscription by "juggling" a large registry of stateful actors onto a small pool of shared physical pods.

To reproduce this demo in your own cluster, please refer to the detailed walkthrough in theCounter Demo.

For more videos and walkthroughs, visit our YouTube channel:agent-substrate.

## Framework Agnostic & Compatibility

Agent Substrate is designed to beframework and agent harness agnostic. Because it manages standard OCI containers at the kernel level (via gVisor), it can host agents built on any stack.

* Agent Development Kit (ADK):Native support for ADK-compatible actor identity and persistent working memory.
* LangChain:Ideal execution environment for long-running, stateful LangChain agents and sandboxed tool-calling.
* Claude Code & CodeX:Support for high-density, stateful coding environments that preserve terminal and filesystem state across sessions.
* Model Context Protocol (MCP):Deploy secure, sandboxed MCP servers as Substrate Actors to provide durable tools for any LLM.

## Ecosystem & Examples

* Agent Executor:A distributed agent runtime that demonstrates building a secure, hyper-scalable agent harness on Agent Substrate (see theannouncement blogandintegration guide).

## Status and compatibility

Agent Substrate is currently in early development. It is not ready for
production use, and the APIs are almost guaranteed to change. We are not
making any guarantees about backward compatibility at this stage, and
everything in this project may be changed.

### Supported Kubernetes Releases

Currently we aim to support thelatest stable releaseof Kubernetes, and the previous minor release.

## Community

For announcements, technical discussions, and community support, please join
theate-devGoogle Group.

We host a weekly community meeting every Thursday from 10:00am - 11:00am PST.

* Video call link:https://meet.google.com/uhq-cxvn-dhy
* Or dial: (US) +1 253-289-6971 PIN: 787 664 574 59#
* More phone numbers:https://tel.meet/uhq-cxvn-dhy?pin=9044088223662

We also have channels in the CNCF slack;request an invite hereif you don't have access.

* #substrate-usersto discuss using substrate.
* #substrate-devto discuss developing substrate.

## Developing

Please seeCONTRIBUTING.mdfor guidelines on contributing to
the project. We welcome contributions of all kinds, but the project is VERY
young. Our immediate focus is on building out the core system and demos, so we
may not be able to review or merge contributions that don't align with those
goals in the near term.

## Quickstart (Development)

To quickly set up the complete environment:

1. Make sure you haveGo,kubectl, anddockerinstalled and configured on your dev machine. We will automatically manage other dependencies via Go, includingkind.
2. Run the following steps:

#
 create cluster and local registry (IPv4; IP_FAMILY=dual|ipv6 overrides)

hack/create-kind-cluster.sh

#
 install ate, valkey, rustfs

hack/install-ate-kind.sh --deploy-ate-system

#
 install counter demo

hack/install-ate-kind.sh --deploy-demo-counter

#
 install kubectl-ate

go install ./cmd/kubectl-ate

#
 create an atespace (required before creating actors), then a counter actor in it

kubectl ate create atespace demo
kubectl ate create actor my-counter-1 -a demo --template=ate-demo-counter/counter

#
 port-forward the network router to bind to local port `8000`

kubectl port-forward -n ate-system svc/atenet-router 8000:80

1. In aseparate terminal, send an HTTP request to increment the counter:

curl -X POST -H 
"
Host: my-counter-1.demo.actors.resources.substrate.ate.dev
"
 -i http://localhost:8000/

### GKE Quickstart (Development)

1. Create and configure your environment file:cp hack/ate-dev-env.sh.example .ate-dev-env.sh#Edit .ate-dev-env.sh to match your project and preferences, then source it:source.ate-dev-env.sh
2. Enable application-default credentials for gcloud:gcloud auth application-default login --project=${PROJECT_ID}
3. Provision the required GCP resources (GKE cluster, Redis, GCS, and IAM bindings):go run ./tools/setup-gcp bootstrap
4. Deploy the Agent Substrate system to your cluster:./hack/install-ate.sh --deploy-ate-system
5. You can then deploy the sample applications. Seedemos/counter/README.mdordemos/sandbox/README.mdfor detailed walkthroughs../hack/install-ate.sh --deploy-demo-counter

#### Custom Setup and Deployment

You can run individual setup steps to create GCP resources as needed. Seego run ./tools/setup-gcp --helpfor available options. For example:

go run ./tools/setup-gcp create cluster
go run ./tools/setup-gcp create bucket

Similarly, you can deploy or cleanup specific Agent Substrate components using the installation script. See./hack/install-ate.sh --helpfor all options.

#
 Re-deploy only ate-apiserver of the ATE system

./hack/install-ate.sh --deploy-ate-apiserver

#
 Delete everything (core system and all demos)

./hack/install-ate.sh --delete-all

#### Tearing down resources (GCP)

If you need to delete the resources created by the setup script, you can use the provided scripthack/teardown.sh. This script will delete resources in the reverse order of creation and handles partial failures gracefully.

./hack/teardown.sh --all

Or run individual teardown steps as needed (see./hack/teardown.shfor available options).

#### Tearing down localkindresources

If you need to delete the localkindcluster and its registry (if it was created byhack/create-kind-cluster.sh):

./hack/delete-kind-cluster.sh

## Demos

We provide several sample applications demonstrating Agent Substrate's capabilities:

1. Counter Demo: A stateful Go HTTP server demonstrating state preservation across suspends/resumes, and dynamic CRD routing.
2. Sandbox Demo (Antigravity): A secure, sandboxed execution environment (running Alpine Linux) that allows arbitrary shell execution while preserving filesystem state across sessions.
3. Claude Code Multiplex: Demonstrates oversubscribing physical hardware by multiplexing multiple Claude Code agents onto a limited pool of workers.
4. Multi-Template: TwoActorTemplates running different binaries share oneWorkerPool, across three namespaces.
5. Request Parking: An oversubscribed pool where the router holds inbound requests until a worker frees up, instead of returning503.
6. Autoscaled WorkerPool: Scales aWorkerPoolon its assigned-worker count with an HPA fed by prometheus-adapter.

### Documentation & Guides

* Architecture: How the control plane, node supervisor, and networking stack fit together.
* API Configuration Guide: Detailed reference for configuring WorkerPools, ActorTemplates, Secrets, and Volumes.
* Full CLI Documentation: Installation and usage forkubectl-ate.
* Glossary: Core terms (Actor, Atespace, ActorTemplate, WorkerPool, Worker, ate-api-server, atenet, atelet, ateom) and how they relate.
* Integration Repositories: Where integrations live, how their repositories are named, and how fixes flow back to core.
* Observability Guide: Guide to actor logging, metrics, and distributed tracing.
* Authentication Guide: Configure trusted JWT providers and human credentials.
* Request Parking: How the router parks requests through transient worker-pool saturation.
* Threat Model: Trust boundaries, assumptions, and known risks.
* Roadmap: Current limitations and what is planned next.
* Benchmarking Guide: Locust-based load tests, monitoring stack, and the orchestrated benchmark harness.

## Tour

### Commands

* cmd/ateapi: The core control plane API server exposing gRPC endpoints to manage actor and worker lifecycles.
* cmd/atelet: A node-level DaemonSet that supervises physical worker pods, coordinates snapshotting, and manages state transfers.
* cmd/atecontroller: A Kubernetes controller that reconciles WorkerPool and ActorTemplate custom resources.
* cmd/atenet: A combined networking controller providing DNS, Envoy routing, and proxy sidecars.
* cmd/ateom-gvisor: An interior-pod helper running inside sandboxed worker pods to executerunsccheckpoint and restore commands.
* cmd/ateom-microvm: The micro-VM peer ofateom-gvisor, running actors as cloud-hypervisor VMs.
* cmd/podcertcontroller: A "polyfill" that provides Pod Certificate signers that
will eventually ship in upstream Kubernetes (with different names).
* cmd/kubectl-ate: A CLI tool for managing Agent Substrate resources. See itsREADME.
* cmd/benchmarking: Synthetic workloads used by the load tests, includingglutton, which consumes RAM, disk, and file descriptors on demand.
* tools/setup-gcp: A provisioning utility to set up the necessary GCP infrastructure resources (GKE, GCS, IAM).
* demos/: Sample applications demonstrating Agent Substrate capabilities.
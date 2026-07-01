---
title: 'GitHub - TencentCloud/CubeSandbox: Instant, Concurrent, Secure & Lightweight Sandbox for AI Agents. · GitHub'
url: https://github.com/TencentCloud/CubeSandbox
site_name: github
content_file: github-github-tencentcloudcubesandbox-instant-concurrent
fetched_at: '2026-07-01T12:04:45.655228'
original_url: https://github.com/TencentCloud/CubeSandbox
author: TencentCloud
description: Instant, Concurrent, Secure & Lightweight Sandbox for AI Agents. - TencentCloud/CubeSandbox
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 TencentCloud

 

/

CubeSandbox

Public

* NotificationsYou must be signed in to change notification settings
* Fork558
* Star6.7k

 
 
 
 
master
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

408 Commits
408 Commits
.claude
.claude
 
 
.github
.github
 
 
CubeAPI
CubeAPI
 
 
CubeEgress
CubeEgress
 
 
CubeMaster
CubeMaster
 
 
CubeNet
CubeNet
 
 
CubeProxy
CubeProxy
 
 
CubeShim
CubeShim
 
 
Cubelet
Cubelet
 
 
agent
agent
 
 
configs
configs
 
 
cubecow
cubecow
 
 
cubelog
cubelog
 
 
deploy
deploy
 
 
dev-env
dev-env
 
 
docker
docker
 
 
docs
docs
 
 
examples
examples
 
 
hypervisor
hypervisor
 
 
network-agent
network-agent
 
 
scripts
scripts
 
 
sdk
sdk
 
 
web
web
 
 
.dockerignore
.dockerignore
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
AGENTS.md
AGENTS.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
CONTRIBUTING_zh.md
CONTRIBUTING_zh.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
README_zh.md
README_zh.md
 
 
openapi.yml
openapi.yml
 
 
View all files

## Repository files navigation

# CubeSandbox

Instant, Concurrent, Secure & Lightweight Sandbox Service for AI Agents

中文文档·Quick Start·Documentation·Changelog·X(Twitter)

Cube Sandbox is a high-performance, out-of-the-box secure sandbox service built on RustVMM and KVM. It supports both single-node deployment and easy scaling to multi-node clusters. It is compatible with the E2B SDK and can create a hardware-isolated, fully serviceable sandbox in under 60ms with less than 5MB of memory overhead.

## 📰 News

v0.4: Safer egress, easier ops

Credential vault
 — Agents call external APIs as usual; keys never enter the sandbox. 
Dashboard
 — version matrix and template health checks; see at a glance whether templates need rebuilding after upgrades.

Changelog →
 ·
 
Security proxy guide →
 ·
 
WebUI guide →

Snapshot, Clone & Rollback at hundred-millisecond granularity

 CubeSandbox 0.3.0 introduces the 
CubeCoW
 Copy-on-Write snapshot engine, enabling event-level snapshots, instant cloning, and rollback to any saved state.
 
Changelog →

🎉 Initial open-source release

 Cube Sandbox is now open source! Millisecond boot, hardware-level isolation, E2B-compatible sandbox for AI Agents.
 
Changelog →

## Product Highlights

⚡ Sub-60ms boot · High density

 Average <60ms cold start, <5MB overhead per instance — run thousands of Agents on one node

Quick start →

🔒 Hardware-level isolation

 Each sandbox gets its own Guest OS kernel — no Docker shared-kernel escapes; run untrusted LLM-generated code safely

Architecture →

🔌 Seamless E2B migration

 Native E2B SDK compatibility — swap one URL env var, zero business code changes

Examples →

🖥️ Web console

 Manage sandboxes, templates, nodes, and version matrix in the browser — open 
:12088
 right after install

WebUI guide →

🔐 Credential vault

 Agents call LLMs and external APIs as usual — keys never enter the sandbox, model context, or logs

Security proxy guide →

🛡️ Egress control

 Domain allowlists, instant block on unauthorized egress, full audit logs for compliance

Security proxy guide →

📸 Snapshot · Clone · Rollback

 Hundred-millisecond checkpoints on running sandboxes — roll back or fork from any saved state

v0.3 changelog →

📦 Template system

 Turn OCI images into templates in one step, install official presets from the Template Store, auto-distribute across nodes

Templates guide →

🤖 AgentHub digital assistants

 Spin up OpenClaw assistants in one click — snapshots, rollback, and assistant template publishing

Digital assistant →

## Demos

1.cubesandbox.-.mp4

2.cubesandbox.demo.mp4

Cube-Sandbox.RL.demo.mp4

5.cube.V0.3.0.-.-.mp4

Installation & Demo

Performance Test

RL (SWE-Bench)

Snapshot · Clone · Rollback

## Benchmarks

In the context of AI Agent code execution, CubeSandbox achieves the perfect balance of security and performance:

Metric

Docker Container

Traditional VM

CubeSandbox

Isolation Level

Low (Shared Kernel Namespaces)

High (Dedicated Kernel)

Extreme (Dedicated Kernel + eBPF)

Boot Speed
 
*Full-OS boot duration

200ms

Seconds

Sub-millisecond (<60ms)

Memory Overhead

Low (Shared Kernel)

High (Full OS)

Ultra-low (Aggressively stripped, <5MB)

Deployment Density

High

Low

Extreme (Thousands per node)

E2B SDK Compatible

/

/

✅ Drop-in

* Cold start benchmarked on bare-metal. 60ms at single concurrency; under 50 concurrent creations, avg 67ms, P95 90ms, P99 137ms — consistently sub-150ms.
* Memory overhead measured with sandbox specs ≤ 32GB. Larger configurations may see a marginal increase.

For detailed metrics on startup latency and resource overhead, see theCore Operations Performance Benchmark Report(bare metal) and thePVM Cloud Server Benchmark Report.

Sub-150ms sandbox delivery under both single and high-concurrency workloads

CubeSandbox base memory footprint across various instance sizes

(*Blue: Sandbox specifications; Orange: Base memory overhead). Note that memory consumption increases only marginally as instance sizes scale up.

## Quick Start

⚡ Millisecond-level startup — watch the fast-start flow above.

Cube Sandbox requires anx86_64 Linuxenvironment withKVMsupport.

The guide walks you through everything infour steps— provisioning a server, installing Cube Sandbox, creating a sandbox template, and running your first agent code. No source build needed, up and running in minutes.

Choose your deployment path:

 🖥 PVM · Cloud VM →
 

🏆 Recommended

 🏗 Bare Metal →
 

 💻 Dev-Env →
 

⚠️
 
Not recommended — poor performance

### First thing after install: open the Web console

🖥️ Visual management — from overview to creating a sandbox and streaming logs, all in your browser.

After one-click deployment, open in your browser:

http://<control-node IP>:12088

Recommended three steps:

1. Check overview— OpenOverview, confirm nodes are Ready and capacity looks healthy
2. Prepare a template— Install an official preset fromTemplate Store; skip if you already have aREADYtemplate underTemplates
3. Create a sandbox—Sandboxes → + New sandbox, pick aREADYtemplate, and view live logs on the detail page within seconds

See the fullWebUI console guide.

## Deep Dive

* Documentation Home— complete guide navigation
* ☁️PVM Deployment— deploy on ordinary cloud VMs without bare metal or nested virtualization
* Template Concepts— image-to-template concepts and workflows
* Example Projects— hands-on examples (code execution, browser automation, OpenClaw integration, RL training, and more)
* 🖥️WebUI Console— visual management right after install (:12088)
* 🔐Security Proxy & Credential Vault— CubeEgress domain filtering, injection, and auditing
* 🤖Digital Assistant AgentHub— create and manage OpenClaw assistants (Preview)
* 💻Development Environment (QEMU VM)— no KVM access? Try Cube Sandbox inside a disposable OpenCloudOS 9 VM

## Architecture

Component

Responsibility

CubeAPI

High-concurrency REST API Gateway (Rust), compatible with E2B. Swap the URL for seamless migration.

CubeMaster

Cluster orchestrator. Receives API requests and dispatches them to corresponding Cubelets. Manages resource scheduling and cluster state.

CubeProxy

Reverse proxy, compatible with the E2B protocol, routing requests to the appropriate sandbox instances.

Cubelet

Compute node local scheduling component. Manages the complete lifecycle of all sandbox instances on the node.

CubeVS

eBPF-based virtual switch, providing kernel-level network isolation and security policy enforcement.

CubeEgress

OpenResty-based egress security gateway: L7 domain filtering, credential injection, and access auditing; works with CubeVS kernel policies so sandbox traffic cannot bypass inspection.

CubeHypervisor & CubeShim

Virtualization layer — CubeHypervisor manages KVM MicroVMs, CubeShim implements the containerd Shim v2 API to integrate sandboxes into the container runtime.

👉 For more details, please read theArchitecture Design DocumentandCubeVS Network Model.

## Community & Contributing

We welcome contributions of all kinds—whether it's a bug report, feature suggestion, documentation improvement, or code submission!

* 🐞Found a Bug or have questions?Submit an issue onGitHub Issues.
* 💡Have an Idea?Join the conversation inGitHub Discussions.
* 🛠️Want to Code?Check out ourCONTRIBUTING.mdto learn how to submit a Pull Request.
* 📝Want to contribute docs?Submit bilingual PRs to our community doc channels:Troubleshooting,Use Cases, andIntegrations.
* 💬Want to Chat?Join ourDiscord.

## License

CubeSandbox is released under theApache License 2.0.

The birth of CubeSandbox stands on the shoulders of open-source giants. Special thanks toCloud Hypervisor,Kata Containers, virtiofsd, containerd-shim-rs, ttrpc-rust, and others. We have made tailored modifications to some components to fit the CubeSandbox execution model, and the original in-file copyright notices are preserved.

Cube Sandbox is listed in theCNCF Landscape.

## About

Instant, Concurrent, Secure & Lightweight Sandbox for AI Agents.

cubesandbox.com

### Topics

 sandbox

 container

 agents

### Resources

 Readme

 

### License

 View license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

6.7k

 stars
 

### Watchers

28

 watching
 

### Forks

558

 forks
 

 Report repository

 

## Releases17

v0.4.0

 Latest

 

Jun 15, 2026

 

+ 16 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Rust43.0%
* Go30.3%
* C14.2%
* Shell6.5%
* TypeScript3.0%
* Python1.4%
* Other1.6%
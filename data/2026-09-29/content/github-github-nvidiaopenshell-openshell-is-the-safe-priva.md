---
title: 'GitHub - NVIDIA/OpenShell: OpenShell is the safe, private runtime for autonomous AI agents. · GitHub'
url: https://github.com/NVIDIA/OpenShell
site_name: github
content_file: github-github-nvidiaopenshell-openshell-is-the-safe-priva
fetched_at: '2026-09-29T16:48:36.416507'
original_url: https://github.com/NVIDIA/OpenShell
author: NVIDIA
description: OpenShell is the safe, private runtime for autonomous AI agents. - NVIDIA/OpenShell
---

NVIDIA

 

/

OpenShell

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.4k
* Star10.3k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

1,560 Commits
1,560 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.agents/
skills
.agents/
skills
 
 
.cargo
.cargo
 
 
.claude
.claude
 
 
.config
.config
 
 
.github
.github
 
 
.opencode/
agents
.opencode/
agents
 
 
architecture
architecture
 
 
crates
crates
 
 
deploy
deploy
 
 
docs
docs
 
 
e2e
e2e
 
 
examples
examples
 
 
fern
fern
 
 
nix
nix
 
 
proto
proto
 
 
providers
providers
 
 
python
python
 
 
rfc
rfc
 
 
scripts
scripts
 
 
sdk
sdk
 
 
skills
skills
 
 
snap
snap
 
 
tasks
tasks
 
 
telemetry
telemetry
 
 
tests
tests
 
 
.dockerignore
.dockerignore
 
 
.env.example
.env.example
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.markdownlint-cli2.jsonc
.markdownlint-cli2.jsonc
 
 
.packit.yaml
.packit.yaml
 
 
.python-version
.python-version
 
 
.trivyignore.yaml
.trivyignore.yaml
 
 
AGENTS.md
AGENTS.md
 
 
CI.md
CI.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
DCO
DCO
 
 
GOVERNANCE.md
GOVERNANCE.md
 
 
LICENSE
LICENSE
 
 
MAINTAINERS.md
MAINTAINERS.md
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
STYLEGUIDE.md
STYLEGUIDE.md
 
 
TESTING.md
TESTING.md
 
 
THIRD-PARTY-NOTICES
THIRD-PARTY-NOTICES
 
 
about.toml
about.toml
 
 
buf.yaml
buf.yaml
 
 
deny.toml
deny.toml
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
install.sh
install.sh
 
 
mise.lock
mise.lock
 
 
mise.toml
mise.toml
 
 
openshell.spec
openshell.spec
 
 
pyproject.toml
pyproject.toml
 
 
rust-toolchain.toml
rust-toolchain.toml
 
 
snapcraft.yaml
snapcraft.yaml
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

Important

New in OpenShell 0.1.x:a stable release cadence, new isolation primitives, an expanded extension surface, and new APIs.Read the 0.1.0 upgrade guide.

OpenShell is the safe, private runtime for fleets of autonomous AI agents. Agents are most useful when they can read files, install packages, call APIs, and use credentials. OpenShell gives them that capability without giving them unrestricted access to your data, secrets, or network. You declare what each agent can touch in a policy, and OpenShell enforces it.

## How It Works

OpenShell governs what agents can do in two ways: it instruments the kernel to enforce policy on every file access, system call, and network connection at runtime, and it uses formal verification to check what a policy change would allow before it is applied.

* Kernel-level enforcement.Each agent runs in an isolated sandbox. Kernel controls confine which files it can access and which system calls it can make, and every network connection passes through a policy check before it leaves the sandbox. Agents never see real credentials; OpenShell adds them only to requests bound for approved endpoints.
* Formally verified policy changes.Before a policy change is approved, OpenShell uses formal verification to flag risky new access it would grant, such as reaching a new host with credentials or calling a new API method, so those changes wait for human review.

SeeArchitecturefor how the gateway, supervisor, and sandbox fit together.

## Quickstart

You need Linux, macOS on Apple Silicon, or Windows with WSL 2 (experimental), plus Docker, Podman, or host virtualization. See theSupport Matrixfor details.

curl -LsSf https://raw.githubusercontent.com/NVIDIA/OpenShell/main/install.sh 
|
 sh
openshell sandbox create --name demo

The installer sets up the CLI and a local gateway. The default sandbox image is minimal Ubuntu with no agent installed. To run a real agent, followRun Your First Agent: it runs OpenCode against a free OpenRouter model and shows how to approve new access as the agent needs it.

## Explore Further

* Sandboxes: images, runtimes, GPUs, and lifecycle.
* Policies: filesystem, network, and process rules, with theadvisorandproverfor reviewing changes.
* Providers: credentials that work only at approved endpoints, includinginference.
* Gateways: the control plane for sandboxes, policy, and access.
* Kubernetes: deploy the gateway with Helm. Your CNI must enforceNetworkPolicy.
* Extensibility: middleware, interceptors, and compute drivers.
* Tutorials: step-by-step policy and agent walkthroughs.
* Prerelease and development builds: try an upcoming release or the latest commit onmain.

## Agent Skills

Install the public OpenShell skills for your coding agent:

npx skills add NVIDIA/OpenShell

The skills teach your agent to drive the OpenShell CLI, write sandbox policies, and debug gateways and inference routing. They live inskills/and work without an OpenShell source checkout.

## SDKs

SDKs connect applications to an OpenShell gateway. They do not install the CLI. Use the same OpenShell release for the SDK and the gateway when possible.

Language

Install

Docs

Python

uv add openshell

README

TypeScript

npm install @nvidia/openshell-sdk
 (GitHub Packages)

README

Go

go get github.com/NVIDIA/OpenShell/sdk/go@latest

README

Rust

cargo add openshell-sdk --git https://github.com/NVIDIA/OpenShell --tag <release-tag>

Installation and usage

## Community

* Questions and discussion:GitHub Discussions
* Bug reports and feature requests:GitHub Issues, using the issue templates
* Security vulnerabilities:followSECURITY.md. Do not open a GitHub issue.
* Roadmap:OpenShell Roadmapand theRFC board
* Try it in the cloud:Brev Launchable

OpenShell is built agent-first: it is developed with the same agent-driven workflows it enables. SeeCONTRIBUTING.mdfor development setup and the contribution workflow, andAGENTS.mdfor the contributor agent skills and workflow chains.

## Telemetry

OpenShell collects anonymous telemetry, limited to operational categories and counts, to help improve the project. It does not collect sandbox names, hostnames, file paths, prompts, credentials, provider or model names, or user content. To disable it, setOPENSHELL_TELEMETRY_ENABLED=falseon the gateway, orserver.telemetryEnabled=falsefor Helm installs. You can also compile telemetry out entirely. SeeTelemetryfor details and thecommunity telemetry reportsfor published usage trends.

## Notice and Disclaimer

This software automatically retrieves, accesses or interacts with external materials. Those retrieved materials are not distributed with this software and are governed solely by separate terms, conditions and licenses. You are solely responsible for finding, reviewing and complying with all applicable terms, conditions, and licenses, and for verifying the security, integrity and suitability of any retrieved materials for your specific use case. This software is provided "AS IS", without warranty of any kind. The author makes no representations or warranties regarding any retrieved materials, and assumes no liability for any losses, damages, liabilities or legal consequences from your use or inability to use this software or any retrieved materials. Use this software and the retrieved materials at your own risk.

## License

This project is licensed under theApache License 2.0.
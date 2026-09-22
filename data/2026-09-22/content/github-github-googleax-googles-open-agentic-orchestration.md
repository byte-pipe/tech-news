---
title: 'GitHub - google/ax: Google''s open agentic orchestration runtime · GitHub'
url: https://github.com/google/ax
site_name: github
content_file: github-github-googleax-googles-open-agentic-orchestration
fetched_at: '2026-09-22T15:25:50.333783'
original_url: https://github.com/google/ax
author: google
description: Google's open agentic orchestration runtime. Contribute to google/ax development by creating an account on GitHub.
---

google

 

/

ax

Public

* NotificationsYou must be signed in to change notification settings
* Fork337
* Star7.1k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

625 Commits
625 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github/
workflows
.github/
workflows
 
 
assets
assets
 
 
cmd
cmd
 
 
deploy
deploy
 
 
docs
docs
 
 
examples
examples
 
 
internal
internal
 
 
pkg/
apis/
v1alpha1
pkg/
apis/
v1alpha1
 
 
runner
runner
 
 
.dockerignore
.dockerignore
 
 
.gitignore
.gitignore
 
 
.ko.yaml
.ko.yaml
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
DESIGN.md
DESIGN.md
 
 
Dockerfile.task-runner
Dockerfile.task-runner
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
demo.sh
demo.sh
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
View all files

## Repository files navigation

# AX

Warning

We are still actively refining our core concepts, protocols,
and specifications. We will likely to introduce major breaking
changes prior to a stable release.

Declare an agentic task with workspaces and gateway specifications. AX sandboxes it, wires up its workspace, fences its network, and helps running it at scale.

AX is a high-throughput, declarative orchestrator to run billions of autonomous agent workloads in a cluster. It runs on top ofAgent Substratefor sandboxed execution and is built to run billions of tasks per cluster. If you have used Kubernetes,axwill feel similar.

#
 task.yaml

apiVersion
: 
ax.io/v1alpha1

kind
: 
Workspace

metadata
:
 
name
: 
golang

spec
:
 
git
:
 - 
repo
: 
https://github.com/golang/go.git

 
branch
: 
"
my-fix
"

---

apiVersion
: 
ax.io/v1alpha1

kind
: 
Task

metadata
:
 
name
: 
test

spec
:
 
workspaces
:
 - 
name
: 
golang

 
goal
: 
"
Ensure that Go tool chain is available and is built from source
"

 
debug
: 
true 
#
 lets you `ax ssh` into the sandbox

Then apply it, watch it come up, and look over the agent's shoulder:

ax apply -f task.yaml
ax watch task 
test

ax ssh 
test
 -- ls -al /workspace

## Why?

Agents are a new kind of workload. They are neither stateless microservices nor run-to-completion batch jobs. They accumulate state, need strict isolation, call out to model APIs and tool servers, and can burn money in a loop if nobody is watching. AX gives you four small primitives that handle all of that declaratively:

You want to...

AX gives you

Run untrusted agent code in an isolated sandbox with CPU/memory limits

Task

Pre-wire Git repos, MCP servers, and skill packages so every agent starts warm

Workspace

Lock outbound traffic down to an explicit host allowlist

Gateway

Configure which LLM the platform itself uses, with credentials from a Kubernetes secret

Model

Pause an idle agent and pick up exactly where it left off

ax suspend
 / 
ax resume

Shell into a running agent to see what it is doing

ax ssh

Everything is expressed asax.io/v1alpha1manifests and applied with a single command.

## Quick start

### 1. Install the CLI

go install github.com/google/ax/cmd/ax@latest

This puts theaxbinary in$(go env GOPATH)/bin. Make sure that directory is on yourPATH.

### 2. Deploy the control plane

You need a Kubernetes cluster,ko(brew install ko), a container registry your cluster can pull from, and a reachable Agent Substrate Control API (in-cluster default:api.ate-system.svc.cluster.local:443).

make deploy AX_IMAGE_REPO=
<
your-registry
>

This deploys Redis, then builds and deploys the control plane images withko. Everything lands in theax-systemnamespace.

### 3. Run your first task

ax apply -f examples/task.yaml 
#
 Task + Workspace + Gateway + Model in one file

ax get tasks

#
 NAME ATESPACE PHASE ACTOR WORKER-IP AGE

#
 task123 default Running task123 10.20.3.67 1m

ax watch task task123 
#
 stream phase and condition changes live

ax ssh task123 -- ls -la /workspace 
#
 poke around inside the sandbox

ax 
suspend
 task task123 
#
 checkpoint and pause

ax resume task task123 
#
 pick up where it left off

Want to see the whole lifecycle end to end? Run./demo.sh. It applies a custom workspace, waits for readiness, runs commands overax ssh, and suspends the task.

## Documentation

Guide

Read it to...

Concepts

Learn what a 
Task
, 
Workspace
, 
Gateway
, and 
Model
 each do, and how a task moves through phases and conditions.

Manifests

Write your own YAML, with an annotated example of every kind.

Sandbox

See what the runner does on boot and what your command can rely on: metadata server, guest services, environment.

Runners

Understand the contract between the control plane and the task container, and build your own runner image to replace the default.

Networking

Reach a running task through the atenet router from the cluster, your laptop, or a gRPC client.

Architecture

Understand how the control plane fits together, plus the 
API reference
.

Development

Build, test, and ship changes to AX itself.

## CLI usage

axtalks to the control plane over gRPC. It is deliberatelykubectl-shaped:apply,get,describe,watch,delete, plus a few agent-specific verbs.

### Everyday commands

#
 Apply anything (multi-document YAML, file or stdin)

ax apply -f examples/task.yaml

#
 Tasks

ax get tasks 
#
 list

ax get tasks -a my-atespace 
#
 list in another atespace

ax get task task123 
#
 full spec + live status as YAML

ax describe task task123 
#
 human-readable detail

ax watch task task123 
#
 stream status and condition transitions

ax 
suspend
 task task123 
#
 checkpoint actor state and pause

ax resume task task123 
#
 resume a suspended task

ax delete task task123

#
 Shell into the running sandbox

ax ssh task123 
#
 interactive shell (task needs spec.debug: true)

ax ssh task123 -- ls -la /workspace 
#
 one-off command

ax ssh task123 -- python3 main.py

#
 Gateways, workspaces, models follow the same pattern

ax get gateways

#
 NAME ATESPACE LISTENERS EGRESS-HOSTS

#
 default-gateway default 8494/gRPC,8080/HTTP *

ax describe gateway default-gateway
ax delete gateway default-gateway

ax get workspaces

#
 NAME ATESPACE GIT-REPOS MCP-SERVERS

#
 default-workspace default 1 1

ax describe workspace default-workspace
ax delete workspace default-workspace

ax get models

#
 NAME ATESPACE PROVIDER MODEL

#
 default-model default google gemini-3.8-flash

ax describe model default-model
ax delete model default-model

#
 Connection plumbing

ax ctx 
#
 active kube context and how ax is reaching the control plane

ax tunnel list 
#
 background tunnels (state lives in ~/.ax/tunnels)

ax tunnel stop
ax version

### Works withkubectx

axfollows your active Kubernetes context. Switch clusters andaxresolves and tunnels to that cluster's control plane in the background.

kubectx staging-cluster
ax get tasks

kubectx prod-cluster
ax get tasks

#
 Or target a context without switching

ax --context=dev-cluster get tasks

### Global flags

Flag

Description

Default

-a
, 
--atespace

Atespace scope for the command

default

-n
, 
--namespace

Kubernetes namespace where AX is installed

ax-system

--context

Kubernetes context to target

active 
kubectx
 / 
current-context

--server

Control plane address, bypassing auto-detection

derived from kube context, or 
$AX_SERVER

## License

Apache License 2.0. SeeLICENSEfor details.
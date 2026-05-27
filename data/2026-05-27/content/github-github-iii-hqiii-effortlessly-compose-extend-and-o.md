---
title: 'GitHub - iii-hq/iii: Effortlessly compose, extend, and observe every service in real-time for the first time ever. · GitHub'
url: https://github.com/iii-hq/iii
site_name: github
content_file: github-github-iii-hqiii-effortlessly-compose-extend-and-o
fetched_at: '2026-05-27T19:44:05.596560'
original_url: https://github.com/iii-hq/iii
author: iii-hq
description: Effortlessly compose, extend, and observe every service in real-time for the first time ever. - iii-hq/iii
---

iii-hq

 

/

iii

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.1k
* Star16.8k

 
 
 
 
main
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

1,682 Commits
1,682 Commits
.cargo
.cargo
 
 
.config
.config
 
 
.cursor
.cursor
 
 
.githooks
.githooks
 
 
.github
.github
 
 
blog
blog
 
 
console
console
 
 
crates
crates
 
 
docs
docs
 
 
engine
engine
 
 
infra/
terraform
infra/
terraform
 
 
new_skills
new_skills
 
 
scripts
scripts
 
 
sdk
sdk
 
 
skills
skills
 
 
website
website
 
 
.gitignore
.gitignore
 
 
.prettierrc
.prettierrc
 
 
.skill-check.yaml
.skill-check.yaml
 
 
AGENTS.md
AGENTS.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
LICENSE.spdx
LICENSE.spdx
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
biome.json
biome.json
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
turbo.json
turbo.json
 
 
View all files

## Repository files navigation

# iii

## What is iii?

iii is the easiest way to compose, extend, and observe every service in your stack in real time.

Every backend starts as a project before the first line of business logic. Queues, cron, HTTP,
state, observability, agents, and sandboxes each usually bring their own integration story. iii
collapses that into one live system surface.

iii worker add queue
iii worker add agent
iii worker add sandbox
iii worker add 
<
anything
>

Each worker joins the live catalog. Every other worker is notified and can call it immediately.
Browse available workers atworkers.iii.dev.

That is the agent story too: when a task needs a capability the system does not have, an agent can
add a worker, discover its functions, call them, and trace what happened. Same interface a developer
uses.

### Three Primitives

Worker _ Function _ Trigger is the entire mental model.

Workersare processes that register with the iii engine and then register triggers and
functions. A TypeScript API service is a worker. A Python data pipeline is a worker. A Rust
microservice is a worker. Any functionality can be transformed into a worker with a few lines of
code. Workers can also create other workers at runtime, so agents and applications can extend the
system while it is running.

Triggersare anything that causes a function to run. A trigger can be a direct call to a
function, an HTTP endpoint, a cron schedule, a queue subscription, a state change, a stream event,
or anything else. Triggers are declarative: the Worker defines "this function runs when this thing
happens," and iii handles routing, serialization, and delivery.

Functionsare units of work with a stable identifier (e.g.,content::classify,orders::validate). It receives input, does work, and optionally returns output. Functions exist in
workers.

By mapping everything a service can do to these three primitives iii creates a development process
that is both effortlessly composable, and completely observable.

## What Changes

Before iii:

* New observability tool: uncountable integrations
* New agent harness: separate retry config, separate traces, separate timeouts
* New queue: vendor evaluation, procurement, and weeks of integration

After iii:

* iii worker add observability
* iii worker add queue
* Done. It is in the system, traceable, and callable.

Platform teams publish workers. Application teams register functions and declare triggers. Agents
use the same catalog and the same function calls.

Extending iii isiii worker add. Composing iii is calling functions. Observing iii is opening the
trace.

## Quick Start

iii project init myapp 
#
 scaffold a project

cd
 myapp
iii 
#
 start the engine

Need to installiiifirst? Full walkthrough at theQuickstart guide.

## Add Workers

Install new capabilities into a project withiii worker add:

## SDKs

Language

Package

Install

Node.js

iii-sdk

pnpm add iii-sdk
 or 
npm install iii-sdk

Python

iii-sdk

pip install iii-sdk

Rust

iii-sdk

Add to 
Cargo.toml

## Agent Skills

Install iii's agent-readable reference material:

npx skills add iii-hq/iii/skills

Skills cover every iii primitive: HTTP endpoints, queues, cron, state, streams, custom triggers, and
more. Seeskills/for the full list.

## Console

Theiii-consoleis a developer and operations console for inspecting workers, functions,
triggers, queues, traces, logs, and real-time state. See theConsole docsfor setup and usage.

## Repository Structure

Directory

What it is

README

engine/

iii Engine (Rust) - core runtime, modules, and protocol

engine/README.md

sdk/

SDKs for Node.js, Python, and Rust

sdk/README.md

console/

Developer console (React + Rust)

console/README.md

skills/

Agent-readable reference material

skills/README.md

website/

iii website

website/

docs/

Documentation site (Mintlify/MDX)

docs/README.md

SeeSTRUCTURE.mdfor the full monorepo layout, dependency chain, and CI/CD details.

## Examples

See theQuickstart guidefor step-by-step tutorials.

## Resources

* Documentation
* CLI & Engine
* Console
* Examples
* Contributing

## License

The iii is licensed as such:

Directory

License

engine/

Elastic License 2.0

sdk/

Apache License 2.0

console/

Apache License 2.0

docs/

Apache License 2.0

website/

Apache License 2.0

The engine runtime is licensed under the Elastic License 2.0 (ELv2). All SDKs, CLI, console,
documentation, and the website are licensed under the Apache License 2.0.

SeeCONTRIBUTING.mdfor additional details.

## About

Effortlessly compose, extend, and observe every service in real-time for the first time ever.

iii.dev

### Topics

 javascript

 python

 api

 rust

 framework

 typescript

 ai

 backend

 primitives

 developer-tools

 agents

 genai

### Resources

 Readme

 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

16.8k

 stars
 

### Watchers

80

 watching
 

### Forks

1.1k

 forks
 

 Report repository

 

## Releases221

iii 0.13.0

 Latest

 

May 25, 2026

 

+ 220 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Rust74.1%
* TypeScript14.5%
* HTML4.9%
* Python4.8%
* Shell0.8%
* HCL0.3%
* Other0.6%
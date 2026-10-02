---
title: 'GitHub - Effect-TS/effect: Build production-ready applications in TypeScript · GitHub'
url: https://github.com/Effect-TS/effect
site_name: github
content_file: github-github-effect-tseffect-build-production-ready-appl
fetched_at: '2026-10-02T16:30:43.484608'
original_url: https://github.com/Effect-TS/effect
author: Effect-TS
description: Build production-ready applications in TypeScript. Contribute to Effect-TS/effect development by creating an account on GitHub.
---

Effect-TS

 

/

effect

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork797
* Star16.5k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

11,239 Commits
11,239 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.agents
.agents
 
 
.changeset
.changeset
 
 
.github
.github
 
 
.vscode
.vscode
 
 
ai-docs
ai-docs
 
 
migration
migration
 
 
packages
packages
 
 
patches
patches
 
 
scratchpad
scratchpad
 
 
scripts
scripts
 
 
.envrc
.envrc
 
 
.gitignore
.gitignore
 
 
.oxlintrc.json
.oxlintrc.json
 
 
LICENSE
LICENSE
 
 
LLMS.md
LLMS.md
 
 
MIGRATION.md
MIGRATION.md
 
 
README.md
README.md
 
 
deno.json
deno.json
 
 
dprint.json
dprint.json
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
jsdocs.config.json
jsdocs.config.json
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
tsconfig.base.json
tsconfig.base.json
 
 
tsconfig.json
tsconfig.json
 
 
tsconfig.packages.json
tsconfig.packages.json
 
 
tsconfig.tests.json
tsconfig.tests.json
 
 
tstyche.json
tstyche.json
 
 
vitest.config.ts
vitest.config.ts
 
 
vitest.docs.ts
vitest.docs.ts
 
 
vitest.setup.ts
vitest.setup.ts
 
 
View all files

## Repository files navigation

# Effect

Effect is a library for building robust, maintainable, type-safe, and production grade applications in TypeScript. It helps you handle the hard problems at scale: typed errors, dependency injection, structured concurrency, scheduling, tracing, and unified schema validation.

Effect 4.x is a long-term support (LTS) release.If you are upgrading from Effect 3.x, follow themigration guide.

## Installation

npm install effect

## Requirements

* TypeScript 5.9 or newer.TypeScript 7 is recommended for the best performance and compatibility withEffect's TypeScript tooling.
* Node.js 18 or neweris the general minimum for running Effect on Node.js. Some integration packages require newer runtimes; for example,@effect/sql-sqlite-noderequires Node.js 22.16 or newer.
* Strict type-checking:thestrictflag must be enabled in yourtsconfig.json.

## Links

* Website: documentation, guides, and news
* Discord: ask questions, share what you're building, and talk to the core team
* Community: meetups and events, or bring Effect to your own
* Issues: bug reports and feature requests
* Jobs: companies hiring Effect developers
* Follow us onX,Bluesky, andLinkedIn

## Let's talk

Whether your team is considering Effect, rolling it out, or already running it in production, we'd love to hear from you: what you're building, what works, and what you need from Effect next.

* Talk to the maintainers.Introduce your team onDiscordor emailcontact@effectful.co. We're happy to connect privately on Slack or Discord for feedback and help with adoption.
* Production support.We're exploring how to better support teams running Effect in production. If your organization has specific support needs, let's discuss them.
* Adoption help.Ouradoption partnersoffer implementation, consulting, team extension, training, and commercial support.

Feedback from teams using and evaluating Effect directly shapes what we stabilize and build next.

## Long-term support

Teams depend on Effect for systems they expect to run for years. Effect 4.x is a long-term support (LTS) release with the following guarantees:

* At least three years of support, including bug and security fixes.
* Bug fixes for one year after the next major version is released.
* Security fixes for two years after the next major version is released.

Stable APIs reserve breaking changes for major releases. APIs marked unstable may change in minor releases, and experimental APIs may change in patch releases.

## Effect v3

The Effect v3 source code is available on thev3branch, which is also where issues and pull requests meant for Effect v3 should be targeted. To upgrade, see themigration guide.

## Packages

This monorepo contains the coreeffectpackage alongside integration packages that extend it. All packages listed below are released together with synchronized versions.

Package

Description

API Reference

effect

The core package

docs

@effect/platform-browser

Platform services for the browser

docs

@effect/platform-bun

Platform services for 
Bun

docs

@effect/platform-deno

Platform services for 
Deno

docs

@effect/platform-node

Platform services for 
Node.js

docs

@effect/platform-node-shared

Shared services for Node.js-compatible runtimes

docs

@effect/sql-clickhouse

SQL client for 
ClickHouse

docs

@effect/sql-d1

SQL client for Cloudflare D1

docs

@effect/sql-libsql

SQL client for libSQL

docs

@effect/sql-mssql

SQL client for Microsoft SQL Server

docs

@effect/sql-mysql2

SQL client for MySQL

docs

@effect/sql-pg

SQL client for PostgreSQL

docs

@effect/sql-pglite

SQL client for 
PGlite

docs

@effect/sql-sqlite-bun

SQL client for SQLite via 
bun:sqlite

docs

@effect/sql-sqlite-do

SQL client for Cloudflare Durable Objects SQLite

docs

@effect/sql-sqlite-node

SQL client for SQLite via 
node:sqlite

docs

@effect/sql-sqlite-react-native

SQL client for SQLite in React Native

docs

@effect/sql-sqlite-wasm

SQL client for SQLite compiled to WebAssembly

docs

@effect/ai-anthropic

Anthropic provider for the Effect AI modules

docs

@effect/ai-openai

OpenAI provider for the Effect AI modules

docs

@effect/ai-typesafe

TypeSafe decision provider for the Effect AI modules

docs

@effect/ai-openai-compat

OpenAI-compatible API provider for the Effect AI modules

docs

@effect/ai-openrouter

OpenRouter provider for the Effect AI modules

docs

@effect/atom-react

React bindings for Effect Atom

docs

@effect/atom-solid

SolidJS bindings for Effect Atom

docs

@effect/atom-vue

Vue bindings for Effect Atom

docs

@effect/opentelemetry

OpenTelemetry
 integration

docs

@effect/vitest

Helpers for testing with 
Vitest

docs

@effect/docgen

Documentation generator for Effect projects

docs

@effect/doctest

Runs JSDoc examples as Vitest tests

docs

@effect/openapi-generator

Generate Effect code from OpenAPI specifications

docs

## License

MIT
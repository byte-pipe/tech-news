---
title: 'GitHub - tracewayapp/traceway: The only tool you need to know what is happening and how to fix it. · GitHub'
url: https://github.com/tracewayapp/traceway
site_name: hackernews_api
content_file: hackernews_api-github-tracewayapptraceway-the-only-tool-you-need
fetched_at: '2026-05-14T06:00:52.973815'
original_url: https://github.com/tracewayapp/traceway
author: sebakubisz
date: '2026-05-11'
description: The only tool you need to know what is happening and how to fix it. - tracewayapp/traceway
tags:
- hackernews
- trending
---

tracewayapp

 

/

traceway

Public

* NotificationsYou must be signed in to change notification settings
* Fork18
* Star669

 
 
 
 
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

549 Commits
549 Commits
.github/
workflows
.github/
workflows
 
 
backend
backend
 
 
diagrams
diagrams
 
 
docker
docker
 
 
docs
docs
 
 
examples
examples
 
 
frontend
frontend
 
 
printscreens
printscreens
 
 
scripts
scripts
 
 
skills
skills
 
 
testing
testing
 
 
website
website
 
 
.dockerignore
.dockerignore
 
 
.gitignore
.gitignore
 
 
CLAUDE.md
CLAUDE.md
 
 
DOCKER.md
DOCKER.md
 
 
Dockerfile
Dockerfile
 
 
Dockerfile.minimal
Dockerfile.minimal
 
 
Dockerfile.sqlite
Dockerfile.sqlite
 
 
Dockerfile.test-pgch
Dockerfile.test-pgch
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
Traceway Logo White.png
Traceway Logo White.png
 
 
Traceway Logo.png
Traceway Logo.png
 
 
Traceway Logo.svg
Traceway Logo.svg
 
 
docker-compose.sqlite.yml
docker-compose.sqlite.yml
 
 
docker-compose.yml
docker-compose.yml
 
 
logo-small-favicon.png
logo-small-favicon.png
 
 
solar--round-graph-broken.svg
solar--round-graph-broken.svg
 
 
View all files

## Repository files navigation

Built onOpenTelemetry

### OpenTelemetry-native observability. Open source. Self-hosted in 90 seconds.

Website·Docs·Cloud·Discord

Traceway is anOpenTelemetry-nativeobservability platform that combineslogs, traces, metrics, session replay/RUM, exceptions, and AI tracingtogether. Point an OTLP exporter at it and you're in business. No Collector, no glue code, no per-language vendor SDK.

MIT licensed. No BSL. No "open core."Every feature is in the box. Self-host it for free, or run it onTraceway Cloudif you'd rather not babysit infra.

👋 Join the Traceway Community on Discord →Chat with the team, shape the roadmap, get help, and meet other folks running Traceway in production.

## What's in the box

* Logs— Structured, trace-linked, sub-second search. Native OTLP/HTTP ingest from any OTel SDK.
* Traces— End-to-end span waterfalls across every service. Click a log, jump to its span.
* Metrics— Host, runtime, and custom metrics. Any dimension, any chart, with custom widget groups.
* Exceptions— SHA-256 normalized stack traces grouped into ranked issues. Source-mapped (webpack, esbuild, Vite).
* Session Replay— Watch what the user did right before the error. Available for web (any JS framework) and Flutter.
* AI Observability— LLM cost, tokens, latency, and full conversations across providers (OpenRouter and any OTel-compatible AI gateway).

Plus: configurable alerts (Slack / GitHub / email / webhook), Apdex + Impact-Score endpoint ranking, multi-tenant orgs with role-based access, and a per-endpoint slow-threshold override.

## Why Traceway

Enterprise (Datadog / New Relic)

DIY OSS stack (Prometheus + Loki + Tempo + ...)

Traceway

Pricing

Per-event, per-host, per-seat

Free + ops time

Self-host free, fixed cloud tiers

Setup

Vendor SDK per language

Glue 6 tools together

docker compose up -d

License

Proprietary

Mixed (some BSL / open-core)

MIT — no asterisks

OTel

Wrapped in vendor SDK

OTel Collector required

Native OTLP/HTTP ingest

Replay + traces + AI

3 separate products

Wire it yourself

One system, one trace ID

## Quick Start

### Self-host with Docker (recommended)

git clone https://github.com/tracewayapp/traceway

cd
 traceway 
&&
 docker compose up -d

#
 ✓ dashboard at http://localhost

Point any OTel SDK athttp://localhost/api/otel/v1/traces(or/metrics,/logs) and traces start flowing. See theself-hosting docsfor production deployment, TLS, and storage configuration.

### Embedded mode (inside your Go app)

Run Traceway inside your Go process — no Docker, no external databases, SQLite under the hood:

go get github.com/tracewayapp/traceway/backend

import
 tracewaybackend 
"github.com/tracewayapp/traceway/backend"

func
 
main
() {
 
go
 
tracewaybackend
.
Run
(
 
tracewaybackend
.
WithPort
(
8082
),
 
tracewaybackend
.
WithDefaultUser
(
"admin@localhost.com"
, 
"admin"
),
 
tracewaybackend
.
WithDefaultProject
(
"My App"
, 
"go"
, 
"dev-token"
),
 )

 
// ... start your app, point its OTel exporter to http://localhost:8082/api/otel/v1/traces

}

Openhttp://localhost:8082, log in, and hit your app to see traces appear. Full walkthrough in theembedded mode guide, or check theworking example.

## Supported Integrations

Traceway integrates with the tools you already use. Every integration ships traces, metrics, and logs overOTLP/HTTP— no proprietary SDK required.

View the full list in thedocumentation. Missing a framework?Open an issueto request it.

### Backend

Gin

Chi

Fiber

FastHTTP

net/http

Go Generic

Node.js

NestJS

Hono

Symfony

Cloudflare

OpenTelemetry

### Frontend

Session Replay is included with every frontend integration — and with Flutter too.

Next.js

React

Vue

Svelte

jQuery

JavaScript

### Mobile

Flutter

Android

React Native

### AI

OpenRouter

## Screenshots

Logs — trace-linked search

Span waterfall

Metrics — application dashboard

Exceptions — grouped & ranked

## Tech Stack

Component

Technology

Backend

Go 1.25, Gin

Frontend

SvelteKit 2, Svelte 5, Tailwind CSS v4

Telemetry DB

ClickHouse (standalone) or SQLite (embedded)

Relational DB

PostgreSQL (standalone) or SQLite (embedded)

Ingest

OTLP/HTTP (Protobuf + JSON) for traces, metrics, logs

## Project Structure

Directory

Description

backend/

Go/Gin API server — OTLP ingest, REST API, notifications, migrations

frontend/

SvelteKit 2 dashboard SPA

docs/

Documentation site (Nextra)

examples/

Working examples — 
embedded mode
 and OTel-instrumented apps (
Express
, 
NestJS
, 
Next.js
, 
Hono
)

website/

Landing page

## Build Tags

Tag

Purpose

(none)

SQLite storage — embedded mode, zero dependencies. This is the default.

pgch

ClickHouse + PostgreSQL storage — standalone server mode.

localdist

Embeds frontend from 
static/dist/
 instead of 
static/frontend/
. Used by traceway-cloud to inject billing UI.

#
 Embedded mode (SQLite, default)

cd
 backend 
&&
 go build ./cmd/traceway

#
 Standalone server (ClickHouse + PostgreSQL)

cd
 backend 
&&
 go build -tags pgch ./cmd/traceway

## Running Tests

#
 SQLite tests (default, no tags needed)

cd
 backend 
&&
 go 
test
 -v -count=1 ./app/repositories/

#
 ClickHouse + PostgreSQL tests (requires Docker)

./scripts/test-backend-pgch.sh

#
 OTEL trace converter tests (no DB required)

cd
 backend 
&&
 go 
test
 -v -count=1 ./app/controllers/otelcontrollers/

#
 Update OTEL golden files after intentional converter changes

cd
 backend 
&&
 go 
test
 -v -count=1 -args -update ./app/controllers/otelcontrollers/

## Documentation

Full documentation atdocs.tracewayapp.com:

* Client SDKs— OpenTelemetry, Go, Node.js, Python, and more
* Self-Hosting— Docker Compose and production deployment
* Concepts— How tracing, exception grouping, metrics, and alerts work
* Embedded Mode— Run Traceway inside your Go app

## Community

Traceway is built in the open, and theDiscord communityis where it happens. Come say hi — whether you're kicking the tires, running it in production, or just curious. We use it to:

* 🗣️Talk through ideas— feature requests, integration asks, roadmap input
* 🛟Help each other out— setup, OTel wiring, deployment questions
* 🚀Show & tell— share what you're building and how you're using Traceway
* 🐛Catch bugs early— report issues and get fast feedback from maintainers
* 👀Get the inside scoop— sneak peeks at what's shipping next

## Contribute

Contributions are welcome — pull requests get reviewed and merged. If you're not sure where to start or want to discuss an idea first,open an issueor drop by thecommunity Discordand we'll talk it through.

## Links

* Website
* Documentation
* Traceway Cloud— managed hosting (same MIT code, run by us)
* Community Discord— chat with the team and other users

## About

The only tool you need to know what is happening and how to fix it.

tracewayapp.com

### Topics

 monitoring

 metrics

 alerting

 telemetry

 logs

 exception-tracker

 traces

 session-replay

 otel

 issue-tracking

 open-telemetry

 observability-platform

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

669

 stars
 

### Watchers

1

 watching
 

### Forks

18

 forks
 

 Report repository

 

## Releases29

Backend v1.7.20

 Latest

 

May 12, 2026

 

+ 28 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Go35.7%
* Svelte33.7%
* TypeScript14.4%
* HTML6.5%
* PHP3.5%
* CSS2.9%
* Other3.3%
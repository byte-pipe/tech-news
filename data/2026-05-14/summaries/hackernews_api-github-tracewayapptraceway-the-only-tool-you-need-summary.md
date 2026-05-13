---
title: GitHub - tracewayapp/traceway: The only tool you need to know what is happening and how to fix it. · GitHub
url: https://github.com/tracewayapp/traceway
date: 2026-05-11
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-14T06:01:47.937778
---

# GitHub - tracewayapp/traceway: The only tool you need to know what is happening and how to fix it. · GitHub

# Traceway Overview

## What is Traceway
- OpenTelemetry‑native observability platform that combines logs, traces, metrics, session replay, exceptions, and AI tracing.  
- Ingest data via an OTLP exporter; no collector or per‑language vendor SDK required.  
- MIT licensed, can be self‑hosted for free or run as Traceway Cloud.

## Core Features
- Logs: structured, trace‑linked, sub‑second search.  
- Traces: end‑to‑end span waterfalls with clickable logs.  
- Metrics: host, runtime, custom; any dimension, custom widget groups.  
- Exceptions: SHA‑256 normalized stack traces, source‑mapped grouping.  
- Session Replay: user actions before errors (web frameworks and Flutter).  
- AI Observability: LLM cost, tokens, latency, full conversations across providers.  
- Additional: configurable alerts (Slack, GitHub, email, webhook), Apdex and Impact‑Score endpoint ranking, multi‑tenant organizations with role‑based access, per‑endpoint slow‑threshold overrides.

## Why Choose Traceway
- Compared to enterprise SaaS (Datadog, New Relic) and DIY OSS stacks (Prometheus, Loki, Tempo, …).  
- Pricing: free self‑host, fixed cloud tiers; no per‑event or per‑seat charges.  
- Setup: single `docker compose up -d` command; no vendor SDKs or separate collector needed.  
- License: fully MIT, no proprietary components.  
- Native OTLP/HTTP ingest provides a single system with unified trace IDs.

## Getting Started

### Self‑host with Docker (recommended)
```
git clone https://github.com/tracewayapp/traceway
cd traceway && docker compose up -d
# Dashboard available at http://localhost
```
Point any OpenTelemetry SDK to `http://localhost/api/otel/v1/traces` (or `/metrics`, `/logs`).

### Embedded mode (inside a Go application)
```go
import "github.com/tracewayapp/traceway/backend"

func main() {
    go tracewaybackend.Run(
        tracewaybackend.WithPort(8082),
        tracewaybackend.WithDefaultUser("admin@localhost.com", "admin"),
        tracewaybackend.WithDefaultProject("My App", "go", "dev-token"),
    )
    // start your app and export OTEL to http://localhost:8082/api/otel/v1/traces
}
```
Open `http://localhost:8082` to log in and view traces.

## Supported Integrations
- Backend: Gin, Chi, Fiber, net/http, generic Go, Node.js, NestJS, Hono, Symfony, Cloudflare, OpenTelemetry.  
- Frontend: Next.js, React, Vue, Svelte, jQuery, plain JavaScript (includes session replay).  
- Mobile: Flutter, Android, React Native.  
- AI: OpenRouter and any OpenTelemetry‑compatible AI gateway.

## Tech Stack
- Backend: Go 1.25 with Gin.  
- Frontend: SvelteKit 2, Svelte 5, Tailwind CSS v4.  
- Telemetry database: ClickHouse (standalone) or SQLite (embedded).  
- Relational database: PostgreSQL (standalone) or SQLite (embedded).  
- Ingest protocol: OTLP/HTTP (Protobuf + JSON) for traces, metrics, and logs.

## Project Structure
- `backend/` – Go/Gin API server, OTLP ingest, REST API, migrations.  
- `frontend/` – SvelteKit dashboard single‑page application.  
- `docs/` – Documentation site built with Nextra.  
- `examples/` – Working examples for embedded mode and OTel‑instrumented apps (Express, NestJS, Next.js, Hono).  
- `website/` – Landing page and marketing assets.  
- Additional files: Dockerfiles, CI workflows, configuration files, logos, etc.

## Build Variants
- Default (no tag): SQLite storage, zero dependencies, used for embedded mode.  
- `pgch` tag: ClickHouse + PostgreSQL storage for standalone server mode.  
- `localdist` tag: Embeds frontend from `static/dist/` for Traceway Cloud billing UI.

## Testing
- SQLite tests (default): `go test -v -count=1 ./app/repositories/`.  
- ClickHouse + PostgreSQL tests (requires Docker): `./scripts/test-backend-pgch.sh`.  
- OTEL trace converter tests (no DB): `go test -v -count=1 ./app/controllers/otelcontrollers/`.  
- Update OTEL golden files after intentional changes: add `-args -update` to the test command.

## Documentation & Community
- Full documentation at `docs.tracewayapp.com` covering client SDKs, self‑hosting, concepts, and embedded mode.  
- Discord community for support, roadmap discussion, sharing use cases, and early bug reports.

## Contributing
- Pull requests are reviewed and merged.  
- Open issues or discuss ideas on Discord before starting contributions.

## Links
- Website  
- Documentation  
- Traceway Cloud (managed hosting)  
- Discord community
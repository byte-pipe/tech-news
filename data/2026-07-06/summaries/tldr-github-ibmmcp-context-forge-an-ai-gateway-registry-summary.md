---
title: GitHub - IBM/mcp-context-forge: An AI Gateway, registry, and proxy that sits in front of any MCP, A2A, or REST/gRPC APIs, exposing a unified endpoint...
url: https://github.com/IBM/mcp-context-forge
date: 2026-07-06
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-07-06T07:33:32.206526
---

# GitHub - IBM/mcp-context-forge: An AI Gateway, registry, and proxy that sits in front of any MCP, A2A, or REST/gRPC APIs, exposing a unified endpoint...

# ContextForge – Open source registry and proxy for MCP, A2A, and REST/gRPC APIs  

## Overview  
- ContextForge is a registry and proxy that federates Model Context Protocol (MCP) servers, Agent‑to‑Agent (A2A) services, and REST/gRPC APIs behind a single unified endpoint.  
- It provides centralized governance, discovery, and observability for AI‑driven tool and agent calling.  
- The project is open source and can be deployed via PyPI, Docker, or Kubernetes with Redis‑backed caching.  

## Core Capabilities  
- **Tools Gateway** – MCP, REST, and gRPC‑to‑MCP translation with TOON compression.  
- **Agent Gateway** – Routing for A2A protocols, OpenAI‑compatible and Anthropic agents.  
- **API Gateway** – Rate limiting, authentication, retries, and reverse‑proxy for REST services.  
- **Plugin Extensibility** – Over 40 plugins for additional transports, protocols, and integrations.  
- **Observability** – OpenTelemetry tracing compatible with Phoenix, Jaeger, Zipkin, and other OTLP back‑ends.  

## Feature Highlights  
- Federation across multiple MCP and REST services.  
- Automatic gRPC‑to‑MCP translation using server reflection.  
- Virtualization of legacy APIs as MCP‑compliant tools and servers.  
- Transport support: HTTP, JSON‑RPC, WebSocket, SSE, stdio, streamable‑HTTP.  
- Admin UI (HTMX + Alpine.js) for real‑time management, configuration, and log monitoring, with air‑gapped deployment support.  
- Built‑in auth, user‑scoped OAuth tokens, retries, and rate‑limiting; optional X‑Upstream‑Authorization header forwarding.  
- Scalable multi‑cluster deployment on Kubernetes; Docker and PyPI distribution options.  

## Deployment Options  
- **PyPI** – Install with `pip install contextforge` and run as an MCP server.  
- **Docker / Docker‑Compose** – Ready‑made images and compose files for quick local or cloud setups.  
- **Kubernetes** – Helm‑compatible manifests with Redis for federation and caching.  

## Extensibility & Plugins  
- Plugin system allows adding new transports, protocols, and third‑party integrations.  
- Plugins are discovered at runtime and can be enabled via configuration files.  

## Observability & Tracing  
- Emits OpenTelemetry spans to configured back‑ends (Phoenix, Jaeger, Zipkin, etc.).  
- Provides metrics for request rates, latency, errors, and cache hits.  

## Getting Started  
1. Choose a deployment method (PyPI, Docker, or Kubernetes).  
2. Run the quick‑start command (`uvx contextforge`, `docker compose up`, or apply the Helm chart).  
3. Access the Admin UI to register MCP servers, REST/gRPC services, or AI agents.  
4. Use the unified endpoint in your AI client to call tools and agents.  

## Development & Contribution  
- Repository includes devcontainer, CI pipelines, and extensive testing scripts.  
- Contribution guidelines, code of conduct, and security policy are provided.  
- Issues, feature requests, and pull requests are welcomed via the GitHub project.  

## Documentation & Resources  
- Full documentation covers installation, configuration, API reference, testing, and troubleshooting.  
- Roadmap outlines upcoming features and deprecations.  

---  
*ContextForge consolidates diverse AI services into a single, manageable gateway, simplifying integration, security, and observability for modern AI applications.*
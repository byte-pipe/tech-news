---
title: Development environments for your cloud agents · Cursor
url: https://cursor.com/blog/cloud-agent-development-environments
date: 2026-05-17
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-05-17T06:01:35.123241
---

# Development environments for your cloud agents · Cursor

# Development environments for your cloud agents

## Overview
- Cloud agents run continuously, can be parallelized, and operate without a local laptop.
- Their effectiveness depends on having a development environment that mirrors a developer’s laptop: cloned repos, dependencies, credentials, and build‑system access.
- New tools let teams configure, maintain, and govern these environments, enabling fleets of agents to handle tasks end‑to‑end.

## Multi‑repo environments
- Supports work that spans several codebases, common in microservice architectures.
- Agents can be given a single environment containing all required repositories, reusable across sessions.
- Enables reasoning about cross‑repo impacts, delivering, testing, and verifying changes together.
- Customer examples: Amplitude, Decagon, Snyk, BILT.
- Quote from Amplitude: agents can investigate issues, identify affected repos, and open PRs with full context.

## Environment configuration as code
- Dockerfile‑based definitions improved with support for build secrets (secure access to private registries) that are scoped only to the build step.
- Layer caching upgraded: only changed layers rebuild, yielding ~70 % faster builds.
- Private‑beta feature: Cursor can auto‑generate a Dockerfile by inspecting repositories, then let users edit and version it.

## Improved agent‑led environment setup
- Cursor interacts during configuration: asks questions, flags missing credentials, validates setup.
- Shows the exact version of the environment an agent is using.
- If configuration fails, Cursor falls back to a base image with warnings, keeping agents running instead of crashing.

## Environment governance and security controls
- Each environment has its own version history; users can review and roll back changes.
- Rollback permissions can be limited to admins; an audit log records all actions.
- Egress rules and secrets are scoped per environment, preventing cross‑environment secret leakage and allowing fine‑grained network allowlists.

## What’s next
- Moving from point‑in‑time configuration to environments that evolve autonomously as the codebase changes.
- Getting started: read the documentation or visit the cloud agents dashboard.
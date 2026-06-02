---
title: GitHub - reconurge/flowsint: A modern platform for visual, flexible, and extensible graph-based investigations. For cybersecurity analysts and investi...
url: https://github.com/reconurge/flowsint
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-06-03T01:52:16.344523
---

# GitHub - reconurge/flowsint: A modern platform for visual, flexible, and extensible graph-based investigations. For cybersecurity analysts and investi...

# Flowsint Overview

## Introduction
- Open‑source OSINT graph exploration tool for ethical investigations, transparency, and verification.  
- Designed for cybersecurity analysts, journalists, law‑enforcement, and internal threat‑intelligence teams.  
- All data is stored locally to ensure privacy.

## Installation & Getting Started
- **Prerequisites:** Docker and Make.  
- Clone the repository and run the production make target:  
  ```
  git clone https://github.com/reconurge/flowsint.git
  cd flowsint
  make prod
  ```  
- Access the web UI at `http://localhost:5173/register` and create a new account (no default credentials).

## Core Features
- Visual, interactive graph interface for exploring relationships between entities.  
- Automated enrichers that fetch and attach additional data to nodes.  
- Real‑time event streaming and a performant frontend that handles thousands of nodes without lag.

## Available Enrichers
- **Domain:** reverse DNS, DNS resolution, subdomain discovery, WHOIS, domain‑to‑website, root domain extraction, ASN lookup, historical data.  
- **IP:** geolocation, network details, ASN lookup.  
- **ASN:** retrieve CIDR ranges.  
- **CIDR:** enumerate IP addresses.  
- **Social Media:** username search across platforms (Maigret).  
- **Organization:** ASN association, company details, domain ownership.  
- **Cryptocurrency:** wallet transaction history, NFT ownership.  
- **Website:** crawler, link extraction, domain extraction, tracker detection, text extraction.  
- **Email:** Gravatar profile, breach checks, associated domains.  
- **Phone:** breach checks.  
- **Individual:** organization affiliations, associated domains.  
- **Integration:** N8n connector for workflow automation.

## Project Architecture
- **flowsint-app:** Frontend UI.  
- **flowsint-api:** FastAPI server with REST endpoints, authentication, and graph DB integration.  
- **flowsint-core:** Core utilities, orchestrator, task queue (Celery), vault, database connections, logging.  
- **flowsint-enrichers:** Enricher implementations and scanning tools.  
- **flowsint-types:** Pydantic models defining all data types (domains, IPs, ASNs, entities, crypto assets, etc.).  

Dependency flow:  
`flowsint-app → flowsint-api → flowsint-core → flowsint-enrichers → flowsint-types`

## Development Setup
- Ensure Docker is installed.  
- Run `make dev` to start the development environment.  
- The app is reachable at `http://localhost:5173`.

## Testing
Each module contains its own test suite, runnable with UV and pytest, e.g.:  
```
cd flowsint-core
uv run pytest
```
(Repeat for `flowsint-types`, `flowsint-enrichers`, `flowsint-api`.)

## Legal & Ethical Use
- Refer to `ETHICS.md` for responsible usage guidelines.  
- Intended only for lawful, ethical research and investigation.  
- Prohibited activities include unauthorized intrusion, harassment, doxxing, political manipulation, and any violation of privacy laws. Misuse is strictly forbidden.

## Contribution Guidelines
- Follow the modular structure when adding new types, enrichers, API endpoints, or utilities.  
- Use Poetry for dependency management.  
- Write tests for new functionality and keep documentation up to date.  
- Community contributions are welcomed; raise issues or propose features on GitHub.

## License
- Apache‑2.0 license.
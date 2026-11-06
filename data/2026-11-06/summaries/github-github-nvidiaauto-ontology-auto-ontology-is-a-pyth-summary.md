---
title: GitHub - NVIDIA/auto-ontology: Auto Ontology is a Python framework for building semantic, graph-based reasoning layers over data. It enables determini...
url: https://github.com/NVIDIA/auto-ontology
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-11-06T12:29:19.405923
---

# GitHub - NVIDIA/auto-ontology: Auto Ontology is a Python framework for building semantic, graph-based reasoning layers over data. It enables determini...

# Auto Ontology Overview

## Purpose
- Provides a semantic, graph‑based reasoning layer over enterprise data.
- Supplies agents with context about data location, meaning, provenance, and similarity.
- Bridges gaps between existing semantic models and operational metadata.

## Core Capabilities
- **Discover**: Generate ontologies from metadata, connect to existing models, build AI‑ready knowledge graphs.  
- **Ground**: Assign trusted business meanings to metrics, entities, and relationships; reconcile inconsistent definitions across systems.  
- **Validate**: Verify generated queries against certified definitions and lineage; return provenance with each answer.  
- **Expose**: Make context accessible via MCP, CLI, and API.  
- **Learn**: Incorporate certified corrections and usage feedback back into the ontology.

## Key Features
- Natural‑language querying of structured data (NL‑to‑SQL) powered by NVIDIA NIM.  
- Semantic catalog/ontology layer stored in PostgreSQL alongside the described data.  
- Authentication and role‑based access control using Better Auth.  
- Web UI for chat, analysis, data catalog, analytics, and settings.  
- Flexible deployment options: Helm chart for Kubernetes or Docker Compose for local stacks.

## Software Components
| Component | Technology | Role | Default Port |
|---|---|---|---|
| Frontend | Next.js 16, React 19, TypeScript, Tailwind CSS, Better Auth, Prisma | Web UI, authentication, API gateway | 3000 |
| Backend | FastAPI (Python 3.12+), LangChain | Chat, NL‑to‑SQL, catalog, datasource APIs | 3001 |
| Ingestion worker | FastAPI (Python 3.12+) | Ingest tabular data, write embeddings | 3002 |
| PostgreSQL + pgvector | Relational DB | Store metadata, catalog, ontology, vector store | 5432 |
| HashiCorp Vault (optional) | — | Secure storage of connection credentials | — |

## NVIDIA NIM Integration
- Uses NVIDIA NIM endpoints for LLM, embeddings, and reranking.  
- Default models (configurable via environment variables):
  - LLM: `nvidia/nemotron-3.5-lightning-30b-a3b`
  - Embeddings: `nvidia/nemotron-3-embed-1b`
  - Rerank: `nvidia/llama-nemotron-rerank-vl-1b-v2`
- Model roles are set through triplets of environment variables (`*_ENDPOINT`, `*_API_KEY`, `*_MODEL`), falling back to shared defaults when unspecified.

## Quickstart Summary
1. Clone repo, copy `.env.example` to `.env`, and fill required keys (NVIDIA API key, auth secret, Postgres passwords, connection strings).  
2. Start PostgreSQL with Docker Compose, then seed the sample “Wide World Importers” database using the `auto-ontology-eval` scripts.  
3. Build and launch the full stack via `docker compose up -d --build`.  
4. Access the web UI at `http://localhost:3000`, sign in with admin credentials, enable Semantic Compilation in Settings.  
5. Pose natural‑language queries; the system resolves terms via the ontology, generates SQL, executes it, and returns results with provenance.

## Licensing & Contributions
- Distributed under Apache License 2.0.  
- Third‑party components listed in `THIRD_PARTY_NOTICES.md`.  
- External contributions are currently not accepted.
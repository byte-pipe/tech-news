---
title: Archyl - AI-Powered Architecture Documentation | C4 Model Diagrams
url: https://www.archyl.com/
date: 2026-09-10
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-09-10T07:21:25.695108
---

# Archyl - AI-Powered Architecture Documentation | C4 Model Diagrams

# Archyl - AI-Powered Architecture Documentation | C4 Model Diagrams

## Making architecture visible
- Archyl enables interactive C4 diagrams and AI‑driven discovery of architecture from code.
- Documentation stays synchronized through an Architecture‑as‑Code YAML DSL.

## Core features
- **Interactive C4 diagrams** – drill‑down from System Context to Code level.
- **AI discovery** – connect a Git repo, let AI extract systems, containers, components, and code elements.
- **Import options** – ADRs, existing markdown docs, or manual import.
- **Collaboration** – invite team members, share projects, and edit together.
- **API & integrations** – MCP server and REST API for external tooling.

## Getting started
1. Click “+” in the sidebar or “New Project” on the dashboard.  
2. Provide a project name (optional description).  
3. An empty System Context diagram is created.  
4. Use “Add” to insert Systems, then drill down to Containers, Components, and Code.  
5. Right‑click any element for quick actions.

## Navigation
- Double‑click an element to move to the next C4 level.  
- Breadcrumbs let you ascend back.  
- Level tabs (System Context, Container, Component, Code) jump directly to a specific level.  
- Sidebar tree provides direct access to any element.

## C4 model overview
- **Level 1 – System Context:** Shows the system, users, and external systems.  
- **Level 2 – Containers:** High‑level technical building blocks (apps, databases, etc.).  
- **Level 3 – Components:** Internal structure of a container.  
- **Level 4 – Code:** Implementation details (classes, functions, etc.).

## Element types per level
- **System Context:** Software Systems, Persons, External Systems.  
- **Container:** Services, APIs, Web/Mobile Apps, Databases, Caches, Queues, File Storage.  
- **Component:** Controllers, Handlers, Repositories, Adapters, Middleware, Utilities, Models.  
- **Code:** Classes, Interfaces, Structs, Functions, Methods, Enums, Constants, Types.

## Creating relationships
1. Click and drag from one element’s edge to another.  
2. Release on the target element; a modal appears for description and technical details.  
3. Choose relationship type (Uses, Depends on, Calls, Reads from, Writes to, Sends to, Receives from, Implements, Extends, Contains).

## Overlays
- Overlays allow additional visual information (e.g., health, ownership, risk) to be layered on diagrams for deeper insight.  

## Support
- Documentation, quick guides, and resources are available.  
- The team can be contacted for further assistance.  

## Frequently asked questions
- **Can I import an existing architecture?** Yes – via AI discovery, ADR import, or markdown documentation.  
- **What are overlays and how to use them?** Overlays add contextual layers to diagrams; configure them in the project settings.
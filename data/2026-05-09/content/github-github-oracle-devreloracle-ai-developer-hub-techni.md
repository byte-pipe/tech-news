---
title: 'GitHub - oracle-devrel/oracle-ai-developer-hub: Technical resources for AI developers to build applications, agents, and systems using Oracle AI Database and OCI services · GitHub'
url: https://github.com/oracle-devrel/oracle-ai-developer-hub
site_name: github
content_file: github-github-oracle-devreloracle-ai-developer-hub-techni
fetched_at: '2026-05-09T19:57:40.555908'
original_url: https://github.com/oracle-devrel/oracle-ai-developer-hub
author: oracle-devrel
description: Technical resources for AI developers to build applications, agents, and systems using Oracle AI Database and OCI services - oracle-devrel/oracle-ai-developer-hub
---

oracle-devrel

 

/

oracle-ai-developer-hub

Public

* NotificationsYou must be signed in to change notification settings
* Fork227
* Star753

 
 
 
 
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

613 Commits
613 Commits
.github/
workflows
.github/
workflows
 
 
.vscode
.vscode
 
 
apps
apps
 
 
guides
guides
 
 
notebooks
notebooks
 
 
workshops
workshops
 
 
.gitignore
.gitignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.prettierignore
.prettierignore
 
 
.prettierrc
.prettierrc
 
 
README.md
README.md
 
 
SETUP_PRE_COMMIT.md
SETUP_PRE_COMMIT.md
 
 
pyproject.toml
pyproject.toml
 
 
requirements-dev.txt
requirements-dev.txt
 
 
View all files

## Repository files navigation

# Oracle AI Developer Hub

This repository contains technical resources to help AI Developers and Engineers build AI applications, agents, and systems using Oracle AI Database and OCI services alongside other key components of the AI/Agent stack.

## What You'll Find

This repository is organized into several key areas:

### 📱Apps(/apps)

Applications and reference implementations demonstrating how to build AI-powered solutions with Oracle technologies. These complete, working examples showcase end-to-end implementations of AI applications, agents, and systems that leverage Oracle AI Database and OCI services. Each application includes source code, deployment configurations, and documentation to help developers understand architectural patterns, integration approaches, and best practices for building production-grade AI solutions.

Name

Description

Link

FitTracker

Gamified fitness platform built with Oracle 26ai JSON Duality Views (FastAPI + Redis), created live during a webinar.

agentic_rag

Intelligent RAG system with multi-agent Chain of Thought (CoT), PDF/Web/Repo processing, and Oracle AI Database 26ai integration

finance-ai-agent-demo

Financial services AI agent with Oracle AI Database as a unified memory core for vector, graph, spatial, and relational queries

oci-generative-ai-jet-ui

Full-stack AI application with Oracle JET UI, OCI Generative AI integration, Kubernetes deployment, and Terraform infrastructure

tanstack-shoe-store

AI chat app using TanStack Start and Oracle 26ai Select AI to query a shoe store database with natural language

### 📓Notebooks(/notebooks)

Jupyter notebooks and interactive tutorials covering:

* AI/ML model development and experimentation
* Oracle Database AI features and capabilities
* OCI AI services integration patterns
* Data preparation and analysis workflows
* Agent development and orchestration examples

Name

Description

Stack

Link

agentic_rag_langchain_oracledb_demo

Multi-agent RAG with langchain-oracledb: OracleVS, OracleEmbeddings, OracleTextSplitter, and CoT agents

Oracle AI Database, langchain-oracledb, Ollama

fs_vs_dbs

Compare filesystem vs database agent memory architectures.

LangChain, Oracle AI Database, OpenAI

memory_context_engineering_agents

Build AI agents with 6 types of persistent memory.

LangChain, Oracle AI Database, OpenAI, Tavily

oracle_langchain_example

Build a RAG application using Oracle 26ai vector storage and LangChain

Oracle AI Database, langchain-oracledb, HuggingFace

oracle_rag_agents_zero_to_hero

Learn to build RAG agents from scratch using Oracle AI Database.

Oracle AI Database, OpenAI, OpenAI Agents SDK

oracle_rag_with_evals

Build RAG systems with comprehensive evaluation metrics

Oracle AI Database, OpenAI, BEIR, Galileo

agent_reasoning_demo

Interactive demo of 11 cognitive architectures (CoT, ToT, ReAct, Self-Reflection, and more) for agent reasoning

Ollama, agent-reasoning

oracle_agentic_rag_hybrid_search

Agentic RAG with vector, keyword, and hybrid search in a single SQL query using LangGraph ReAct agent

Oracle AI Database, langchain-oracledb, LangGraph, OpenAI

f1_miami_strategy_oracle_26ai

F1 Miami GP strategy intelligence for 2026 — SQL, hybrid vector+keyword search, JSON documents, and property graph in one Oracle 26ai database using real FastF1 data

Oracle AI Database, FastF1, sentence-transformers, Plotly

multicloud/

AWS, Azure, Google Cloud, and MongoDB API samples running Oracle AI Database outside OCI

Oracle AI Database + AWS / Azure / Google / MongoDB

### 📚Guides(/guides)

Comprehensive documentation, reference materials, and conference presentations covering AI agent architecture, reasoning strategies, and memory systems.

Name

Description

Link

Building the Brain and Backbone of Enterprise AI Agents

Advanced reasoning and infrastructure strategies for enterprise AI agents. Covers the 2026 agent stack (layered architecture), reasoning patterns (Chain of Thought, Tree of Thoughts, Self-Reflection, Least-to-Most, Decomposed Prompting), and context/belief updates. Presented at DevWeek SF 2026 by Nacho Martinez.

Memory Engineering: The Discipline Behind Memory Augmented Agents

Deep dive into memory engineering as a discipline for AI agents — the science of helping agents remember, reason, and act. Covers the memory ecosystem, form factors, and key disciplines shaping memory-augmented agents. Presented at DevWeek SF 2026 (Keynote) by Richmond Alake.

Agent Memory with Oracle AI Database

Agent memory architectures and Oracle AI Database as the memory core for AI agents. Presented at the AI Developer Conference hosted by DeepLearning.AI in April 2026 by Eli Schilling.

### 🧠Agent Memory(/notebooks/agent_memory)

Notebooks focused on theOracle AI Agent Memorypackage (oracleagentmemory) — the AI-Agent Memory Package built on top of Oracle AI Database. These notebooks demonstrate how to useOracle AI Database as the unified memory core for AI agents, serving conversation history, durable facts, and entity state from a single converged engine instead of stitching together a vector DB, key-value store, and relational store.

The collection covers the package's developer guide, benchmarks against naive memory, and three end-to-end framework examples (OpenAI Agents SDK, Claude Agent SDK, LangGraph).

Name

Description

Stack

Link

OAMP Developer Guide

Step-by-step guide to the 
oracleagentmemory
 API: connection, the three core primitives (users/agents, memories, threads), automatic extraction, and vector retrieval.

OAMP, LiteLLM

OAMP Benchmarks

Quantify token cost, latency, and response quality of OAMP vs. naive flat-history memory across 80 scripted turns with three agent variants.

OAMP, LiteLLM, OpenAI

Deep Research Agent

Build a deep research agent for human genome exploration that uses Tavily for live web search and Oracle AI Agent Memory for durable findings across sessions.

OpenAI Agents SDK, Tavily, OAMP

Supply Chain Assistant

A supply chain assistant that tracks shipment cargo via in-process tools and an MCP server, with shipment records and operational notes persisted in OAMP.

Claude Agent SDK, MCP, OAMP

Mortgage Approval Workflow

A deterministic mortgage approval workflow modeled as a LangGraph 
StateGraph
 where OAMP persists applicant data and audit trails so failed runs can resume.

LangGraph, OAMP

See theAgent Memory READMEfor a recommended reading order, prerequisites, and Open-in-Colab links.

### 🎓Workshops(/workshops)

Hands-on workshops and guided learning experiences that take developers from fundamentals to production patterns with Oracle AI Database. Each workshop is self-contained with a student notebook (TODO gaps to fill in), a complete reference notebook, step-by-step part guides, and a ready-to-run Codespaces / devcontainer environment with Oracle AI Database pre-configured. Workshops progress from information retrieval and RAG, through agentic systems and orchestration, to memory-augmented agents — together they cover the full stack for building AI applications on Oracle.

Pull a single workshop without cloning the whole hub— each workshop README includesgit sparse-checkoutinstructions so you can fetch only the folder you need.

Name

Description

Stack

Link

Information Retrieval to RAG

Build a Research Paper Assistant over 200 ArXiv papers by implementing five retrieval strategies (keyword, vector, hybrid, graph) and a full RAG pipeline wired to OCI GenAI.

Oracle AI Database, sentence-transformers, oracledb, OCI GenAI (xAI Grok 3 Fast)

From RAG to Agents

Extend the RAG pipeline into a multi-agent system — wrap retrieval as agent tools, compose orchestration, and add persistent session memory backed by Oracle.

Oracle AI Database, sentence-transformers, oracledb, OpenAI API (GPT-5), openai-agents

Agent Memory

Build memory-aware agents: implement a 
MemoryManager
 with six memory types in Oracle, apply context-engineering techniques, and compare agent runs with and without memory.

Oracle AI Database, langchain-oracledb, sentence-transformers, OCI GenAI, Tavily

### 🤝Partners(/partners)

Notebooks and apps contributed by partners in the AI ecosystem. AI Developers can use these resources to understand how to use Oracle AI Database and OCI alongside tools such as LangChain, Galileo, LlamaIndex, and other popular AI/ML frameworks and platforms.

Name

Description

Stack

Link

Coming soon

Partner-contributed resources will be added here

-

-

## Getting Started

1. Explore Applications: Start with the applications in/appsto see complete, working examples
2. Follow Workshops: Check/workshopsfor guided learning paths
3. Experiment with Notebooks: Use/notebooksfor hands-on experimentation
4. Build Memory-Augmented Agents: Dive into/notebooks/agent_memoryfor the Oracle AI Agent Memory package
5. Reference Guides: Consult/guidesfor detailed documentation
6. Check Partner Resources: Explore/partnersfor integrations with popular AI tools and frameworks

## Contributing

This project is open source. Please submit your contributions by forking this repository and submitting a pull request! Oracle appreciates any contributions that are made by the open-source community.

### Development Setup

Before contributing, please set up pre-commit hooks to ensure code is automatically formatted:

1. Install pre-commit:pip install pre-commit
2. Install additional dependencies(optional, includes pre-commit and ruff):pip install -r requirements-dev.txt
3. Install pre-commit hooks:pre-commit install
4. Optional: Format existing code:pre-commit run --all-files

The pre-commit hooks will automatically format your code using:

* Rufffor Python files (formatting and linting)
* Prettierfor JavaScript, TypeScript, JSON, YAML, and Markdown files

For more detailed information, seeSETUP_PRE_COMMIT.md.

## License

Copyright (c) 2024 Oracle and/or its affiliates.

Licensed under the Universal Permissive License (UPL), Version 1.0.

SeeLICENSEfor more details.

ORACLE AND ITS AFFILIATES DO NOT PROVIDE ANY WARRANTY WHATSOEVER, EXPRESS OR IMPLIED, FOR ANY SOFTWARE, MATERIAL OR CONTENT OF ANY KIND CONTAINED OR PRODUCED WITHIN THIS REPOSITORY, AND IN PARTICULAR SPECIFICALLY DISCLAIM ANY AND ALL IMPLIED WARRANTIES OF TITLE, NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A PARTICULAR PURPOSE. FURTHERMORE, ORACLE AND ITS AFFILIATES DO NOT REPRESENT THAT ANY CUSTOMARY SECURITY REVIEW HAS BEEN PERFORMED WITH RESPECT TO ANY SOFTWARE, MATERIAL OR CONTENT CONTAINED OR PRODUCED WITHIN THIS REPOSITORY. IN ADDITION, AND WITHOUT LIMITING THE FOREGOING, THIRD PARTIES MAY HAVE POSTED SOFTWARE, MATERIAL OR CONTENT TO THIS REPOSITORY WITHOUT ANY REVIEW. USE AT YOUR OWN RISK.

Note: This repository is actively maintained and updated with new resources, examples, and best practices for Oracle AI development.

## About

Technical resources for AI developers to build applications, agents, and systems using Oracle AI Database and OCI services

oracle-devrel.github.io/oracle-ai-developer-hub/

### Topics

 kubernetes

 ai

 artificial-intelligence

 agents

 oracle-database

 oraclejet

 rag

 kustomize

 generative-ai

 ai-developer

 agentmemory

 oracleaidatabase

### Resources

 Readme

 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

753

 stars
 

### Watchers

24

 watching
 

### Forks

227

 forks
 

 Report repository

 

## Releases1

Repo state as shown at Oracle Cloud World (OCW) 24

 Latest

 

Nov 19, 2024

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Jupyter Notebook70.9%
* Python12.5%
* Go6.2%
* JavaScript4.1%
* TypeScript3.2%
* HTML1.3%
* Other1.8%

 Generated from 
oracle-devrel/repo-template
---
title: GitHub - langflow-ai/openrag: OpenRAG is a comprehensive, single package Retrieval-Augmented Generation platform built on Langflow, Docling, and Opens...
url: https://github.com/langflow-ai/openrag
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-03-13T03:13:52.552730
---

# GitHub - langflow-ai/openrag: OpenRAG is a comprehensive, single package Retrieval-Augmented Generation platform built on Langflow, Docling, and Opens...

# OpenRAG Overview

## Highlights
- Pre‑packaged, ready‑to‑run platform with core tools integrated
- Agentic RAG workflows featuring re‑ranking and multi‑agent coordination
- Robust document ingestion handling messy, real‑world data
- Drag‑and‑drop visual workflow builder powered by Langflow
- Modular enterprise add‑ons for extended functionality
- Scalable enterprise search using OpenSearch

## How OpenRAG Works
- Transforms uploaded documents into searchable knowledge through ingestion, indexing, and semantic retrieval
- Provides a chat interface backed by large language models for AI‑powered conversations
- Leverages Langflow for workflow orchestration and Docling for intelligent parsing

## Installation
- Follow the quickstart guide in the documentation
- Install the OpenRAG Python package
- Deploy services via Docker, Docker‑Compose, or Podman for self‑managed setups

## Quick Start Workflow
1. Launch OpenRAG  
2. Add knowledge (upload and process documents)  
3. Start chatting with the AI assistant

## SDKs
### Python SDK
- Install: `pip install openrag-sdk`
- Example usage:
  ```python
  import asyncio
  from openrag_sdk import OpenRAGClient

  async def main():
      async with OpenRAGClient() as client:
          response = await client.chat.create(message="What is RAG?")
          print(response.response)

  if __name__ == "__main__":
      asyncio.run(main())
  ```
- Full documentation available in the repository

### TypeScript/JavaScript SDK
- Install: `npm install openrag-sdk`
- Example usage:
  ```javascript
  import { OpenRAGClient } from "openrag-sdk";

  const client = new OpenRAGClient();
  const response = await client.chat.create({ message: "What is RAG?" });
  console.log(response.response);
  ```
- Full documentation available in the repository

## Model Context Protocol (MCP)
- Connect external AI assistants (e.g., Cursor, Claude Desktop) to OpenRAG knowledge bases
- Install: `pip install openrag-mcp`
- Configuration example provides command, arguments, and environment variables for the MCP server
- Enables RAG‑enhanced chat, semantic search, and settings management

## Development & Support
- Contribution guidelines in `CONTRIBUTING.md`
- Troubleshooting guide and discussion forum for assistance
- Bug reports and feature requests handled via the Issues page

## License & Resources
- Licensed under the Apache‑2.0 license
- Official website: https://www.openr.ag
- Repository includes README, security policy, and additional documentation files.
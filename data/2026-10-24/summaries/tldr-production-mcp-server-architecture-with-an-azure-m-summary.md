---
title: Production MCP server architecture, with an Azure mapping | Amir Pournasserian
url: https://pournasserian.com/writing/mcp-2026-reference-architecture
date: 2026-10-24
site: tldr
model: llama3.2:1b
summarized_at: 2026-10-24T14:38:21.124432
---

# Production MCP server architecture, with an Azure mapping | Amir Pournasserian

## MCP Server Architecture for Production

The article provides a production-ready architecture for Microsoft Productivity Controllers (MCP) servers, built on top of Azure. This series aims to explore the key aspects of MCP server deployment.

### Core Principles

- **Stateless Requests**: Any instance can serve any request, which leads to horizontal scaling and no sticky sessions, making it easy to manage load.
- **Routing Care**: There are two aspects that require careful routing: subscriptions/ListenStream and Task/Calls, ensuring they're handled correctly.
- **Edge Routes**: The edge routes the received request and applies the policy from `Mcp-Method` and `Mcp-Name` headers, allowing checks against body.
- **Security**: On Azure, only one replica is recommended for interactive clients, as Microsoft recommends. Additionally, the server utilizes OAuth bearer token validation for caching signing keys.

### Design Elements

- **MCP Server Tier**: The MCP server tier comprises server instances, discover, instruction holders, subscription/stream holders, and tools/resources/pr promot, facilitating task engagement and task execution.
- **Shared/Durable Store**: A shared, durable store stores the task records and handles for state management, allowing partitioning based on header routing.
- **Pub/Sub Fan-out and Idle_TIMEOUT**: Task calls are routed using `Mcp-Name` as `taskId`, resulting in a partitioned store and optimizing routing.
- **OpenTelemetry Pipeline**: An open-telemetry pipeline is integrated throughout the system for end-to-end management, including skills digestion, interface templates, and build-time artifacts.
- **Build-Time Artifacts**: Build-time artifacts support stable bytes for stable delivery of products.

## Architecture Overview

The architecture outlines the MCP server tier, highlighting key components:

- **MCP Server Tier**: Server instance discover, instruction holders, subscription/stream holders, and tools/resources/pr promot.
- **Edge Routes**: Edge routes handled the received request and applies policy headers to receive on the edge.
- **Security**: Azure-recommended on multiple replica setups, only caching, OAuth bearer token validation for security.
- **State Management**: Shared durable store supports partitioning and routing on headers for scalability.
- **Pub/Sub and Delivery**: Open telemetry pipeline for end-to-end delivery including data digestion and user interface templates.
- **User Interface (UI) and Skills**: Built with user interfaces and skills management supported throughout system.
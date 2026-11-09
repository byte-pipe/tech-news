---
title: A hands-on, low-level understanding of MCP using command-line tools
url: https://code.mendhak.com/low-level-mcp-tutorial
date: 2026-11-09
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-11-09T16:01:26.073506
---

# A hands-on, low-level understanding of MCP using command-line tools

# A hands‑on, low‑level understanding of MCP using command‑line tools

## Setup
- Create a tutorial folder, initialize a Python virtual environment with `uv`, and install `fastmcp`.
- Write a minimal MCP server (`server.py`) that registers a single tool `add(a: int, b: int) -> int` using `FastMCP`.

## Starting the server
- Run the server with `fastmcp run server.py:mcp --transport stdio`.
- The server listens on standard input/output and waits for JSON‑RPC requests.

## Discover command
- Send a `server/discover` JSON‑RPC request (single‑line JSON) to obtain server capabilities, supported protocol version, and metadata.
- The response includes:
  - `cacheScope`, `capabilities` (prompts, resources, tools), `supportedVersions`, and server info.
- Using `jq` to format the request and pretty‑print the response makes it easier to read.

## List tools
- Issue a `tools/list` request to retrieve all registered tools.
- The response provides each tool’s:
  - `name`, `title`, `description` (from docstring),
  - `inputSchema` and `outputSchema` (derived from type annotations),
  - additional metadata.

## Call the tool
- Invoke the `add` tool with a `tools/call` request, passing arguments `{ "a": 5, "b": 3 }`.
- The server returns a result object containing:
  - `structuredContent` with the numeric result (`8`),
  - a textual representation in `content`,
  - status flags (`isError: false`, `resultType: complete`).

## Resources and prompts
- (Section introduced but not detailed in the excerpt; it signals further exploration of MCP features such as resource subscription and prompt handling.)
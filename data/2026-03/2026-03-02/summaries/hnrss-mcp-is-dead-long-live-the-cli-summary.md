---
title: MCP is dead. Long live the CLI
url: https://ejholmes.github.io/2026/02/28/mcp-is-dead-long-live-the-cli.html
date: 2026-03-01
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-03-02T08:26:11.589736
---

# MCP is dead. Long live the CLI

# Summary of “MCP is dead. Long live the CLI”

## Main claim
- The Model Context Protocol (MCP) is already fading away; signs include lack of support in tools like OpenClaw and Pi.
- Industry rushed to adopt MCP after Anthropic’s announcement, but the author sees no real benefit.

## LLMs don’t need a special protocol
- LLMs excel at using command‑line tools after being trained on man pages, Stack Overflow, and shell scripts.
- MCP’s promised cleaner interface still requires the same documentation of tool behavior and parameters.

## CLIs are for humans too
- When an LLM (e.g., Claude) does something unexpected, the same CLI command can be run manually to reproduce the result.
- MCP hides the tool inside the conversation, forcing developers to debug JSON transport logs instead of simple commands.

## Composability
- CLI commands can be piped, filtered, and redirected (e.g., using `jq`, `grep`, file redirection).
- With MCP, large data (like a Terraform plan) must be either loaded into the context window or filtered on the server, both inefficient compared to CLI composition.

## Auth already works
- Existing CLI tools rely on battle‑tested authentication flows (AWS profiles, GitHub SSO, kubeconfig) that work identically for humans and LLMs.
- MCP adds unnecessary, opinionated authentication handling.

## No moving parts
- MCP servers are separate processes that must be started, kept alive, and can silently fail.
- CLI binaries are static files with no background state, available on demand.

## Practical pain
- **Initialization**: MCP servers are flaky; frequent restarts are needed.
- **Re‑authentication**: Each MCP tool may require separate auth steps, unlike CLIs with long‑lived credentials.
- **Permissions**: MCP allows only all‑or‑nothing allowlisting; CLIs enable fine‑grained control (e.g., read‑only vs. write actions).

## When MCP makes sense
- If a tool truly lacks a CLI counterpart, MCP can be appropriate.
- The author still uses MCP for such cases but views it as an exception.

## The real lesson
- The best tools serve both humans and machines.
- Decades of CLI design provide composability, debuggability, and integration with existing auth systems.
- MCP attempted a new abstraction but the existing CLI ecosystem already fulfills that role well.

## A plea to builders
- Companies investing in MCP servers without official CLIs should reconsider.
- Prioritize building a solid API, then a robust CLI; agents will naturally learn to use it.

---
title: ACP v2 is available in Draft - Agent Client Protocol
url: https://agentclientprotocol.com/announcements/acp-v2-draft
date: 2026-07-23
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-07-23T19:02:28.538017
---

# ACP v2 is available in Draft - Agent Client Protocol

# ACP v2 is available in Draft – Agent Client Protocol

## Overview
- The ACP team releases the first Draft of version 2 of the Agent Client Protocol (ACP).  
- Since v1, 15+ RFDs have been shipped, showing the protocol’s extensibility without large migrations.  
- v2 introduces breaking changes that enable new use‑cases, more session states, and greater consistency.  
- Development will continue via the existing RFD process, keeping the release focused on core behavior changes while allowing optional features to be added later.  

## The Big Themes of v2

### Moving beyond the turn
- v1 assumed agents only emitted events after a user‑initiated turn; this caused confusion when background work needed to send updates.  
- v2 decouples prompt request/response from the entire work lifecycle:  
  - `session/update` notifications can occur at any time.  
  - A prompt response now only acknowledges the message, not the end of the turn.  
  - Agents can signal “idle” or readiness for new input, enabling queueing, steering, and concurrent client observation.  

### Updating messages and streaming tool calls
- All session items (user/agent messages, tool calls, terminal output) now have stable IDs with uniform patch semantics: omitted fields stay unchanged, `null` clears a field, values replace, and chunks append.  
- Message IDs allow streaming, updating, and redaction.  
- Tool call content can be streamed incrementally instead of being resent in full.  

### Diff overhaul
- The old `oldText`/`newText` diff is replaced by structured file‑change objects supporting add, delete, modify, move, copy, and binary/non‑text cases.  
- Agents may optionally include a `git_patch` for rendering; clients can use it for richer diff visualisation.  

### More flexible permission requests
- Permission prompts now contain a required `title` and optional `description`, plus an extensible `subject` instead of a fixed tool call.  
- This design permits future permission types (e.g., terminal commands) and separates UI context from the underlying tool call.  

### Forward compatibility by default
- Enum‑like schema values accept unknown variants prefixed with `_`, allowing implementation‑specific extensions without breaking older agents/clients.  
- Nearly every layer of the schema can be extended, encouraging experimentation while preserving stability.  

## Draft Status
- v2 is currently a Draft; the author has reviewed the schema line‑by‑line and considers it solid for testing.  
- Implementations should be gated behind version negotiation **and** feature flags, and not shipped to production until stabilization.  
- Supporting v2 does not require dropping v1; both versions should coexist, and SDKs are being updated to simplify this.  
- A migration guide with before/after examples outlines the key changes for agents, clients, and SDKs.  

## Getting Started
- Read the v2 protocol documentation and the migration guide.  
- SDK authors can generate code from the v2 JSON schemas (released as `v2.0.0-alphaX`).  
- The v2 RFD collection records the rationale behind major decisions.  

## Request for Feedback
- Feedback is most valuable now; issues or discussions can be opened on GitHub or through the RFD process.  
- The team believes v2 provides a stronger foundation, incorporating a year of learnings, consolidating common patterns, and offering greater flexibility for future agentic development.
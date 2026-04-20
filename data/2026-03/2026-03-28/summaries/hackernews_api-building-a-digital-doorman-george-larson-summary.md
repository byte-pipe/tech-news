---
title: building a digital doorman - george larson
url: https://georgelarson.me/writing/2026-03-23-nullclaw-doorman/
date: 2026-03-27
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-03-28T01:02:53.073690
---

# building a digital doorman - george larson

# building a digital doorman – george larson

## the problem with “ask my resume”

- Typical portfolio chatbots only rephrase the resume; they cannot provide information beyond what is written.
- Desired behavior: answer specific, verifiable questions (e.g., test coverage) by accessing real code and configuration.
- Goal: build infrastructure that can fetch and analyze actual project data.

## the architecture

- Visitor interacts via `georgelarson.me/chat/` → web IRC client → Cloudflare → Ergo IRC server (`#lobby`).
- **nullclaw** (public agent) reads public GitHub repos, holds pre‑loaded portfolio context, and forwards complex requests to **ironclaw** via private IRC channel `#backoffice`.
- **ironclaw** runs on a separate Tailscale‑connected box, with access to email, calendar, and deeper personal context.
- Separation ensures the public box never sees private data.

## why irc

1. Matches the terminal‑style UI of the portfolio site.
2. Full control of the stack—no reliance on third‑party bot APIs.
3. Mature, simple protocol with no vendor lock‑in; the same bot can be used from a web client or a terminal.

## model selection as a design decision

- **Conversational layer:** Haiku 4.5 – fast, cheap responses for greetings and simple queries.
- **Tool‑use layer:** Sonnet 4.6 – invoked only when code cloning, reading, or synthesis is required.
- **Cost cap:** $2 per day to prevent budget exhaustion and abuse.
- Tiered inference keeps the system inexpensive while still providing depth when needed.

## security posture

- Non‑root SSH user, key‑only auth, non‑standard port.
- UFW firewall: only SSH, TLS‑IRC, and HTTPS (WebSocket) open.
- Cloudflare proxies all web traffic, handling TLS termination and rate limiting.
- Nullclaw runs sandboxed with read‑only tool allowlist and action limits.
- Strict cost caps ($2 /day, $30 /month) act as damage control.
- Full audit logging, automatic security updates, and Let’s Encrypt TLS.

## the communication stack

- **Ergo:** single Go binary IRC server (≈2.7 MB RAM).
- **Gamja:** static web IRC client (≈152 KB).
- **Nullclaw:** Zig AI agent runtime (≈4 MB binary, ≈1 MB RSS).
- Total footprint under 10 MB of binaries and 5 MB RAM at idle; runs on the cheapest VPS tier.

## what nully can actually do

- Answer language usage by checking actual repositories.
- Report test structure by cloning and inspecting test files.
- Provide project details (e.g., “Fracture”) from pre‑loaded memory and source code.
- Supply accurate contact information without hallucination.
- Schedule calls by delegating to ironclaw via Google A2A protocol; the visitor never sees the handoff.

## the A2A implementation

- Nullclaw implements Google A2A v0.3.0 for both receiving and making calls.
- `a2a_calltool` sends JSON‑RPC requests, parses task states, and returns artifact text as tool results.
- Ironclaw’s nullclaw acts as a bridge, using a single LLM API key and billing relationship; no credential duplication.
- HTTPS enforced for public endpoints, plain HTTP allowed within Tailscale for debugging.

## security of the handoff

- Strict guardrails: only approved request types (scheduling, availability, contact) are forwarded.
- Arbitrary visitor instructions are rejected.
- Ironclaw’s A2A endpoint is firewalled to Tailscale only, never publicly reachable.
- Both agents run in supervised mode with workspace‑only file access and restricted command allowlists.

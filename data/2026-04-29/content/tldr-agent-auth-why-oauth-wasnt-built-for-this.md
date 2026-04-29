---
title: 'Agent Auth: Why OAuth Wasn''t Built for This'
url: https://www.apideck.com/blog/agent-auth-oauth-ai-agents#where-this-leaves-builders?utm_source=tldrit
site_name: tldr
content_file: tldr-agent-auth-why-oauth-wasnt-built-for-this
fetched_at: '2026-04-29T20:09:29.269062'
original_url: https://www.apideck.com/blog/agent-auth-oauth-ai-agents#where-this-leaves-builders?utm_source=tldrit
author: Apideck
date: '2026-04-29'
published_date: '2026-04-26T10:00:00+00:00'
description: OAuth 2.0 was designed for clients known at build time. As AI agents make runtime decisions, delegate to sub-agents, and traverse trust boundaries, the cracks are showing. A practical breakdown of MCP OAuth 2.1, A2A, AAuth, WIMSE, and what a production-grade agent auth architecture looks like today.
tags:
- tldr
---

The internet runs onOAuth 2.0. Since 2012, it has handled how applications request access to user data, how APIs delegate permissions, and how login buttons across billions of apps connect to identity providers. It has worked well enough that most developers stopped questioning it.

Then agents arrived, and OAuth started showing its seams.

When a human logs into Salesforce via Google, the flow is synchronous: redirect, consent screen, token issued. The user was there. The user said yes. When an AI agent books a flight, queries a ledger, and triggers a payment while you sleep, there is no consent screen moment. The agent makes decisions mid-task, calls services it discovered at runtime, and may hand off to sub-agents that hand off further down the chain. OAuth was not designed to track any of that.

The spec Dick Hardt wrote in 2012 was designed for clients known at build time. In OAuth and OIDC, a client has no independent identity: a client_id at Google is meaningless at GitHub. Agents pick their tool chain at runtime, one call at a time, choosing the next tool as the task unfolds. A scope likemail.readlooks identical whether the agent is summarizing your inbox or exfiltrating it. The protocol cannot tell them apart.

This is the problem the industry is currently trying to solve.

## What MCP and A2A changed

Anthropic'sModel Context Protocol, published in 2024, gave agents a standard interface to tools and data sources. Early MCP servers had minimal authentication, typically API keys in environment variables. That worked for local stdio transport but not for remote servers where tokens could be intercepted.

MCP's March 2025 specification standardized authorization using OAuth 2.1, requiring PKCE from all clients and adding metadata discovery and dynamic client registration. Remote MCP servers running over Streamable HTTP now have a recommended authentication path that developers can implement consistently. The spec is clear: authorization is optional but strongly recommended for any server that lets agents take action.

One gap in that flow is discovery. An agent hitting a remote MCP server for the first time needs to know where the authorization server lives before it can start any OAuth exchange.RFC 9728(OAuth Protected Resource Metadata) addresses this by letting the server publish its auth endpoint at/.well-known/oauth-protected-resource. Cloudflare added native support for this discovery flow inCloudflare Accessin April 2026, showing how established infrastructure is adapting to support it.

The gap MCP did not address was agent-to-agent communication. If your orchestrator agent needs to delegate to a specialized research agent or a payment processor, MCP provides no protocol for that handoff. Each agent authenticates independently, with no standard way to reduce permissions or prove the delegation chain.

Google publishedA2Aon April 9, 2025, with backing from more than 50 launch partners across enterprise software, including Salesforce and SAP. A2A is built on existing web infrastructure standards, making it compatible with systems businesses already run. It was designed to support enterprise-grade authentication and authorization, with parity to OpenAPI's authentication schemes.

Where MCP handles the connection between an agent and its tools, A2A handles the connection between agents themselves. An inventory agent built by your team can communicate with a supplier agent built by a third party, usingAgent Cardsto publish capabilities and OAuth 2.0 flows to handle authentication.

Google donated A2A to the Linux Foundation in June 2025. IBM's ACP (Agent Communication Protocol) merged into it voluntarily in August 2025. By April 2026, A2A had grown to 150+ organizations with production deployments in place across major enterprise software vendors.

## The deeper problem: bearer tokens don't work in multi-hop chains

Both MCP's OAuth 2.1 and A2A's authentication schemes still rely on bearer tokens. If you hold the token, you can use it. In a multi-agent pipeline, that creates a structural problem.

Multi-agent delegation chains require a constraint that standard token formats cannot enforce: each hop should only be able to reduce permissions, never expand them. With bearer tokens, there is no mechanism to prevent a sub-agent from reusing a delegated credential at full scope.

This is whereAAuthenters. Dick Hardt, who authored the OAuth 2.0 RFC, has been developing a specification at aauth.dev that treats agents as first-class identities. AAuth brings together authentication and authorization built on OAuth RFCs, with message signing and discovery, to provide a foundation for agent identity and access management. Every HTTP request must be signed by the agent's key pair, and delegation must be made explicit and verifiable rather than inferred from logs.

The core shift is cryptographic. A stolen token without the corresponding private key cannot be replayed. Delegation chains become explicit and auditable.

AAuth is currently an exploratory specification, not a ratified standard. Theplayground at playground.aauth.devlets you callwhoami.aauth.devto see agent identity claims in practice. It is worth tracking because it works from first principles rather than extending a protocol designed for browsers: what would authentication look like if agents were the starting point?

Token formats likeBiscuitsandMacaroonsapproach the scope attenuation problem differently. These allow the agent receiving a token to cryptographically restrict it before passing it downstream, and those restrictions cannot be removed by any party that does not hold the original minting key. No round-trip to an authorization server is needed to narrow permissions. The restriction is embedded in the token itself.

## WIMSE and the IETF's framework

The IETF has been developing workload identity standards under theWIMSE(Workload Identity in Multi-System Environments) working group. In March 2026,draft-klrc-aiagent-auth-00was published, composing WIMSE, SPIFFE, and OAuth 2.0 into a 26-page framework called AIMS (Agent Identity Management System).

The draft adopts the WIMSE identifier as the primary agent identifier, a URI that uniquely identifies a workload within a trust domain. Authorization decisions and audit logs pivot on this ID, which must remain stable for the lifetime of the workload identity.SPIFFE(Secure Production Identity Framework for Everyone) is the operationally mature implementation, handling automatic credential rotation and binding ephemeral key material with each credential.

The draft is solid on authentication. The WIMSE identifiers bind agent identity to the execution environment through hardware-rooted attestation. The authorization layer, however, stops at the token boundary. The Security Considerations section of the -00 revision contains two words: "TODO Security." Authentication is getting formalized. Authorization across trust domains is still a product and engineering problem.

NIST launched two initiatives in February 2026: the NCCoE concept paper on AI agent identity and authorization, and the AI Agent Standards Initiative covering security controls and testing. Both center on WIMSE and SPIFFE combined with OAuth. The Colorado AI Act establishes a "reasonable care" standard for high-risk AI systems effective June 30, 2026, and widely adopted identity standards will likely qualify as evidence of that care in court.

## What practitioners are shipping today

Auth0(part of Okta) reached general availability of Auth0 for AI Agents in November 2025. Using Client-Initiated Backchannel Authentication (CIBA), agents can pause execution, request user approval via email or Auth0 Guardian, and resume automatically once the user approves. The SDK detects when a tool call needs authentication, stores the token securely, and resumes without further developer intervention. Auth0 is also collaborating with Google Cloud on A2A authentication, which signals how incumbent identity vendors see this space.

The auth discussion so far has covered how agents prove their identity to services. The inverse problem also needs a standard answer: how does a service verify that the agent connecting to it is who it claims to be? TheWeb Bot Auth IETF drafttackles this from the server side. It lets bots sign their HTTP requests with a private key and publish their corresponding public keys at/.well-known/http-message-signatures-directory, allowing receiving sites to cryptographically verify inbound bot traffic rather than relying on user-agent strings that any client can spoof. It is the server-side complement to what AAuth proposes on the client side: a matched pair of signing and verification standards that give both ends of an agent interaction a way to establish cryptographic trust.

The hardcoded credential problem has not improved.GitGuardian's State of Secrets Sprawl 2026report found 28.65 million hardcoded secrets added to public GitHub in 2025 alone, a 34% year-over-year increase. Agents generate logs and replicate workflows automatically, and the exposure surface is larger than with traditional integrations.

TheApideck Unified MCP serveroffers a concrete example of how this plays out in production. The server atmcp.apideck.dev/mcpexposes 229 tools across Accounting, HRIS, CRM, and more. Auth against the MCP server itself happens via three request headers:x-apideck-api-key,x-apideck-app-id, andx-apideck-consumer-id. The consumer ID connects an agent to a specific user's pre-authorized integrations. Before the agent ever runs, the end user has authorized their connectors throughVault, Apideck's credential management layer. When the agent calls a tool, Vault looks up the correct credentials in the background and injects the right token before making the downstream API call. The agent never holds OAuth tokens for third-party services directly.

The design solves a specific sequencing problem. Consent happens once at connection setup rather than mid-task. Vault handles token refresh automatically. The MCP server annotates tools with permission levels (read, write, destructive), so a read-only agent cannot even discover delete operations in the tool list. That is the same principle AAuth formalizes at the protocol level: permissions should be bounded at each hop, not left to the agent to self-limit.

A production-grade agent auth stack today requires:

* OAuth 2.1 with PKCE for MCP tool access
* A2A with Agent Cards for cross-agent delegation
* SPIFFE-issued short-lived credentials for workload authentication
* Token attenuation (Biscuits or Macaroons) or AAuth-style signed requests for multi-hop chains where scope reduction matters

None of this is a single product. It is an architecture you compose from pieces that are still being standardized.

## Where this leaves builders

Authentication is converging around known primitives. Authorization across trust domains is not.

Knowing that an agent is who it claims to be is one problem. Knowing what it is actually allowed to do during a specific task, and producing proof of that afterward, is harder.OWASP's MCP Top 10and A2A's signed Agent Cards address pieces of this, as does the WIMSE architecture. No single specification covers the full chain from identity through intent to audit trail.

The infrastructure gap extends beyond the auth layer itself.Cloudflare scanned the 200,000 most visited domainsin April 2026 and found that fewer than 4% of sites have declared AI usage preferences in their robots.txt, and emerging standards like MCP Server Cards and API Catalogs appeared on fewer than 15 sites in the entire dataset. Most of the internet is not yet set up to receive authenticated agent traffic, let alone verify it.isitagentready.comscores any site across discoverability, bot access, and protocol capabilities, including whether OAuth server discovery is published correctly, and generates per-check prompts you can hand to an agent to fix what is missing.

For anyone building integrations that agents will traverse, the relevant question is not whether your API supports OAuth. It is whether your auth layer can handle delegated credentials and produce a verifiable trail of which agent did what and on whose behalf. Most existing OAuth implementations were not designed to answer that. The work to make them do so is happening now, and the teams that engage with it early will be ahead of the ones waiting for a finished spec.

## Ready to get started?

Scale your integration strategy and deliver the integrations your customers need in record time.

Get started for free
Talk to an expert 
Ready to get started?
Talk to an expert
---
title: Production MCP server architecture, with an Azure mapping | Amir Pournasserian
url: https://pournasserian.com/writing/mcp-2026-reference-architecture
site_name: tldr
content_file: tldr-production-mcp-server-architecture-with-an-azure-m
fetched_at: '2026-10-24T14:29:39.751383'
original_url: https://pournasserian.com/writing/mcp-2026-reference-architecture
date: '2026-10-24'
published_date: '2026-10-24'
description: 'How the 2026 MCP duties shape a production deployment: a generic architecture, one way to host it on Azure, and a build pipeline for schemas, skills and conformance.'
tags:
- tldr
---

# A reference architecture for MCP servers in production

October 24, 2026·Part 34 of 35

Most parts of this series added a duty to a Model Context Protocol (MCP) server, and almost every duty leaves a mark on how you deploy it. This part gathers those marks into one generic architecture, one way to host it on Azure, and a build pipeline for MCP’s own artifacts.

This is part 34 of my series on what an MCP server does under the 2026-07-28 specification, afterpart 33 on putting an AI agent behind an MCP tool. The facts are as I read them in October 2026.

## In brief

1. Stateless requests let any instance serve any request,so the server tier scales horizontally with no sticky sessions, and handles and task records live in a shared, durable store.
2. Two things still need routing care:asubscriptions/listenstream stays on the instance that accepted it, so change events fan out over publish/subscribe (pub/sub); task calls carry theirtaskIdinMcp-Name, so you can partition the task store or route on the header.
3. The edge routes and applies policy from theMcp-MethodandMcp-Nameheaders,and can check them against the body; on a server that uses OAuth, each request’s bearer token is validated against cached signing keys.
4. On Azure, keep at least one replica running for interactive clients,as Microsoft recommends; one mapping runs the server on Container Apps behind Front Door and API Management.
5. My advice: give MCP’s own artifacts a build stagethat checks schemas against their declared dialect, recomputes skill digests from the served bytes, and runs the official conformance suite and tests in both protocol eras.

## What drives the design

Each driver comes from an earlier part:

Driver
Consequence
Stateless requests
: any instance can serve any request
Horizontal scaling, serverless-friendly, no sticky sessions
Explicit handles and task records
A shared, durable store
subscriptions/listen
 streams pinned to instances
Pub/sub fan-out, and idle timeouts sized for long-lived streams
Tasks
 routed by 
Mcp-Name
 = 
taskId
A partitioned store, or routing on the header
Bearer token
 on every request, where the server uses OAuth
Fast token validation with a cached JSON Web Key Set (JWKS)
Mcp-Method
 and 
Mcp-Name
 headers
Policy and routing at the edge without parsing bodies
Trace context in 
_meta
An OpenTelemetry pipeline end to end
Skills
 digests and 
user interface (UI) templates
Build-time artifacts with stable bytes

## The generic architecture

Here’s the architecture I’d start from: hosts, from Claude to agents in integrated development environments (IDEs), reach a tier of MCP server instances through an edge, with identity, state, backends and operations around it:

MCP server tier: server/discover + instructions, subscriptions/listen stream holders, tools / resources / prompts, tasks/get, update, cancel, MRTR state codec AEAD keys; State and async: Job queue, Workers task execution, Durable store handles, task records, Pub/sub change events; Backends: Business APIs, databases, search index, LLM provider agentic tools only; Operations: OTel collector, APM / logs, Secrets / keys; Job queue → Workers task execution; Workers task execution → Durable store handles, task records; Workers task execution → Pub/sub change events; OTel collector → APM / logs; Hosts Claude, ChatGPT, IDE agents, automation → Edge: API gateway / WAF TLS, rate limits, Mcp-Method / Mcp-Name policy, header-body match; Edge: API gateway / WAF TLS, rate limits, Mcp-Method / Mcp-Name policy, header-body match → MCP server tier; Hosts Claude, ChatGPT, IDE agents, automation → Authorization server / IdP OAuth 2.1, ID-JAG: OAuth flows; MCP server tier → Authorization server / IdP OAuth 2.1, ID-JAG: JWKS, token exchange; MCP server tier → State and async: handles, tasks, jobs; State and async → MCP server tier: change events to listen streams; MCP server tier → Backends; State and async → Backends: workers call; MCP server tier → Operations: traces, metrics, keys
MCP server tier
State and async
Backends
Operations
Hosts
Claude, ChatGPT,
IDE agents, automation
Edge: API gateway / WAF
TLS, rate limits,
Mcp-Method / Mcp-Name policy,
header-body match
Authorization server / IdP
OAuth 2.1, ID-JAG
server/discover
+ instructions
subscriptions/listen
stream holders
tools / resources /
prompts
tasks/get, update,
cancel
MRTR state codec
AEAD keys
Job queue
Workers
task execution
Durable store
handles, task records
Pub/sub
change events
Business APIs, databases,
search index
LLM provider
agentic tools only
OTel collector
APM / logs
Secrets / keys
OAuth flows
JWKS, token exchange
handles, tasks, jobs
change events to listen streams
workers call
traces, metrics, keys

The edge, an application programming interface (API) gateway or web application firewall (WAF), terminates Transport Layer Security (TLS), applies rate limits and policy on theMcp-MethodandMcp-Nameheaders, and can reject a request whose headers disagree with its body; the server itself answers that mismatch with-32020(part 7).

Identitysits with an authorization server or identity provider (IdP), where the server tier fetches the JWKS and exchanges tokens. The server tier itself publishes the Protected Resource Metadata that points clients there (part 18), andpart 28covers the Identity Assertion JSON Web Token (JWT) Authorization Grant (ID-JAG).

The MCP server tieris a set of stateless instances. Their codec seals therequestStateof Multi Round-Trip Requests (MRTR) with Authenticated Encryption with Associated Data (AEAD) keys, which every instance must share to open a retry (part 14).

State, async work and backends:a job queue feeds workers that execute tasks, write handles and task records to a durable store (part 26) and publish change events on a pub/sub bus to the instances holding listen streams. The server tier and the workers call your business APIs, databases and search index, and a large language model (LLM) provider only for agentic tools (part 33).

Operations:an OpenTelemetry (OTel) collector carries traces and metrics to application performance monitoring (APM) and logs (part 20), and a store holds secrets and keys, the shared AEAD keys among them.

Part 7covers the much smaller picture of a local stdio server.

## One way to host it on Azure

Hosts reach Azure Container Apps through Front Door with its WAF and then API Management, with Microsoft Entra ID for identity. Cosmos DB holds handles and task records, Service Bus the task queue and change topics, and Key Vault the AEAD keys. The services are examples as of October 2026; the table names a few alternatives.

MCP hosts → Azure Front Door + WAF; Azure Front Door + WAF → Azure API Management policies on Mcp-Method / Mcp-Name, rate limits, token validation; Azure API Management policies on Mcp-Method / Mcp-Name, rate limits, token validation → Azure Container Apps MCP server, scale to N; MCP hosts → Microsoft Entra ID app registration, scopes, on-behalf-of; Azure API Management policies on Mcp-Method / Mcp-Name, rate limits, token validation → Microsoft Entra ID app registration, scopes, on-behalf-of; Azure Container Apps MCP server, scale to N → Azure Cosmos DB handles + task records; Azure Container Apps MCP server, scale to N → Azure Service Bus task queue + change topics; Azure Service Bus task queue + change topics → Container Apps Jobs / Functions task workers; Container Apps Jobs / Functions task workers → Azure Cosmos DB handles + task records; Azure Container Apps MCP server, scale to N → Azure AI Search / Azure OpenAI or Foundry models; Container Apps Jobs / Functions task workers → Azure AI Search / Azure OpenAI or Foundry models; Azure Container Apps MCP server, scale to N → Azure Key Vault AEAD keys, secrets; Azure Container Apps MCP server, scale to N → Application Insights via Azure Monitor OpenTelemetry; Container Apps Jobs / Functions task workers → Application Insights via Azure Monitor OpenTelemetry
MCP hosts
Azure Front Door + WAF
Azure API Management
policies on Mcp-Method / Mcp-Name,
rate limits, token validation
Microsoft Entra ID
app registration, scopes,
on-behalf-of
Azure Container Apps
MCP server, scale to N
Azure Cosmos DB
handles + task records
Azure Service Bus
task queue + change topics
Container Apps Jobs / Functions
task workers
Azure AI Search /
Azure OpenAI or Foundry models
Azure Key Vault
AEAD keys, secrets
Application Insights
via Azure Monitor OpenTelemetry

Concern
Azure option
Notes
Edge, WAF
Front Door + WAF
Size idle timeouts for long-lived listen streams
Gateway policy
API Management
Validate JWTs, rate-limit per tool using 
Mcp-Name
, reject header and body mismatches
Identity
Entra ID
Usually pre-registered clients; on-behalf-of for downstream calls (
part 19
)
Compute
Container Apps (or App Service)
Stateless instances; scale on Hypertext Transfer Protocol (HTTP) concurrency
State
Cosmos DB
Partition task records by 
taskId
Async
Service Bus + Container Apps Jobs or Functions
Idempotent workers; dead-letter queues
Change fan-out
Service Bus topics (or Redis pub/sub)
Instances holding listen streams subscribe
Secrets, keys
Key Vault
Rotate 
requestState
 AEAD keys with key IDs in the blob
Observability
Azure Monitor OpenTelemetry to Application Insights
End-to-end traces through 
_meta.traceparent

I’d add two cautions.

First, Container Apps can scale to zero, which suits low-traffic or non-interactive servers. For interactive clients,Microsoft recommendsa minimum of one replica, and its troubleshooting notes report a first request taking 10 to 30 seconds after a period of inactivity.

Second, listen streams keep instances alive, are cut when an instance recycles, and are reopened only within limits. As of October 2026,Claude Codereopens a stream that closes again within 10 seconds up to three times, then stops for that connection. If it stayed open longer, Claude Code keeps reopening it, but after five reopens in one hour it waits about six hours, keeping the tools, prompts and resources it last fetched until then (part 17). My advice: make change events re-fetchable rather than one-shot.

## A build pipeline for MCP-specific artifacts

Besides its code, an MCP server has artifacts with rules of their own: tool schemas and names,x-mcp-headermarks on parameters (part 7),SKILL.mdfront matter, a UI bundled into one HyperText Markup Language (HTML) file, and digests that must match the served bytes. And stateless instances can be deployed blue/green:

Source repo code, skills/, ui/, prompts → Lint and validate tool schemas, names, x-mcp-header rules, SKILL.md frontmatter; Lint and validate tool schemas, names, x-mcp-header rules, SKILL.md frontmatter → Build bundle UI to single-file HTML, normalize skill bytes, compute digests; Build bundle UI to single-file HTML, normalize skill bytes, compute digests → Test conformance suite, fake-host integration test, dual-era tests; Test conformance suite, fake-host integration test, dual-era tests → Package container image / npm / NuGet; Package container image / npm / NuGet → Deploy blue/green, stateless
Source repo
code, skills/, ui/, prompts
Lint and validate
tool schemas, names,
x-mcp-header rules,
SKILL.md frontmatter
Build
bundle UI to single-file HTML,
normalize skill bytes,
compute digests
Test
conformance suite,
fake-host integration test,
dual-era tests
Package
container image / npm / NuGet
Deploy
blue/green, stateless

These are the checks I’d automate:

* Schema validation.Validate everyinputSchemaandoutputSchemaagainst the meta-schema of its declared dialect, which thespecificationsets to JSON Schema 2020-12 when no$schemais given. As of October 2026, Claude Code excludes tools whose input schemas fail its 2020-12 meta-schema and property-name checks.
* Deterministic ordering.Snapshot-testtools/listand compare it across builds (part 6explains why).
* Description budget.Fail the build if the instructions or a description run past about 2,000 characters (part 4explains why).
* Skill integrity.In a test, recompute each digest from the exact bytes you serve.
* Conformance.Run the official conformance suite (it has a GitHub Action);my review of MCP testing toolsrecords that it carries per-revision requirement sets for 2025-11-25 and 2026-07-28. The MCP Inspector’s own conformance runner is still on its roadmap, for November 2026 to January 2027.
* Two eras.Test against one 2026-07-28 client and one legacy client (part 22), and run the fake-host integration test ofpart 30.

## Method and caveats

* Built from my guide’s reference-architecture chapter, written against the 2026-07-28 specification; vendor documentation as checked on 8 October 2026.
* Where Claude Code’s documentation is more precise than my notes (fixed limits on reopening listen streams; schema checks on input schemas only), this article follows it.
* Where the specification is more precise than my notes (2020-12 is the default dialect, not the only one), this article follows the specification.
* Where Microsoft’s documentation qualifies scale-to-zero (at least one replica for interactive clients), this article follows it.
* Where my notes and my review of testing tools differ (the Inspector’s conformance runner is planned, not shipped), this article follows the review, which recorded the tools on 1 October 2026.
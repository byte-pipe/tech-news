---
title: 'Agentic Platform: Open-Sourcing the Agentic Identity Broker'
url: https://engineering.zalando.com/posts/2026/09/agentic-platform-open-sourcing-agentic-identity-broker.html
site_name: tldr
content_file: tldr-agentic-platform-open-sourcing-the-agentic-identit
fetched_at: '2026-09-25T15:44:49.028999'
original_url: https://engineering.zalando.com/posts/2026/09/agentic-platform-open-sourcing-agentic-identity-broker.html
date: '2026-09-25'
published_date: '2026-09-25T00:00:00+02:00'
description: As part of our agentic platform initiative, we are open-sourcing the Agentic Identity Broker, a central component for user-to-agent delegation, consent, and token exchange that lets agents act on...
tags:
- tldr
---

Today we are open-sourcing theAgentic Identity Broker, an MIT-licensed component that lets AI agents act on behalf of users across third-party systems without ever holding the users' provider tokens. We built it while working on our own agentic platform, where we ran head-first into two questions: how to handle agentic identity, and how to give agents reasonable access across multiple systems. InAgentic Engineering at Zalando: a snapshot, Bartosz Ocytko described our platform work at a high level. In this post, we share details how we are building that platform from open-source components for the agent runtime and AI gateway, and why we built one core piece ourselves: an identity broker that captures delegation chains and enables access to third-party services.

## Agentic Identity: Old Problems Magnified

When we look at agentic identity, we need to solve three core problems: (a) how to identify agents through their own machine identity, (b) how to give agents access to a multitude of third-party systems that each issue their own access tokens, and (c) how to make access decisions based on both the users' and the agents' permissions.

None of these problems are fundamentally new; we have seen them before with microservices, and as an industry we have partly ignored them. We added custom integration layers but rarely unified access across third-party systems in the way effective agentic AI requires.

Luckily, much of the necessary standardization was already in place, or at least available as drafts, when the Model Context Protocol (MCP)specificationwas published. The shared pressure to make MCP work securely has also fast-tracked standardization at a pace that is unusual in the identity space. On the OAuth 2.0 side, examples areRFC 8693 - OAuth 2.0 Token Exchange,RFC 9728 - OAuth 2.0 Protected Resource Metadata, and theIdentity Assertion JWT Authorization Grant, also known as Cross-App Access (XAA). On the machine identity side, we can build onSPIFFEand the work of the IETFWIMSEworking group. The newest efforts try to tie all of this together in theAI Identity Management Systemdraft.

## On-Behalf-Of Flows

While much of the attention goes to autonomous agents, a lot of enterprise value lies in on-behalf-of flows, where humans either interact with an agent directly or trigger it indirectly, for example via GitHub pull requests, Google Chat messages, or comments on Linear tickets. The advantage of focusing on this class of agents is that enterprise access management and user permissions already exist. On top of these, we assign permissions to the agent's own identity, resulting in effective permissions that are the intersection of both sets.

Delegated access is the intersection of both the user and agent permissions.

Between interactive sessions and fully autonomous agents that act on their own behalf, there are semi-autonomous cases: there is no directuser presence, but a privileged bridge application has some form ofuser attestationavailable. Examples are a Google Chat bridge, GitHub apps that receive webhooks, and schedulers. By allowing these privileged applications to impersonate users towards agents, we can, for example, talk to an agent in Google Chat and propagate the user's identity. A downstream MCP server then still applies the user's effective permissions, and the agent acts on behalf of the user.

## Platform Context

A sketch of the platform we are building.

Similar to how we built out our microservices architecture, we are building a platform on which teams can implement agentic use cases. We build it on Kubernetes, because we already have a large Kubernetes investment and operate hundreds of production clusters. At its core, the platform combineskagentandagentgatewaywith the Agentic Identity Broker for delegated access.

We offer platform abstractions as Kubernetes custom resource definitions (CRDs) that capture the intent to publish something on the platform, with Agents and MCP servers being the main abstractions today. Agents can be declarative or user-provided; MCP servers can be in-house or third-party.

We usekroto translate these abstractions into lower-level kagent and agentgateway resources as well as into configuration of our identity infrastructure. This automatically spawns central MCP gateways and agent instances. MCP servers are made available to local agents, to agents deployed on the platform, and to third-party agents running on other agentic platforms. The platform wraps a protective layer with central observability around these MCP servers.

## Agentic Identity Broker

The Agentic Identity Broker records which user has delegated which permissions to which agent, holds the resulting third-party sessions, and exchanges tokens when an agent calls a tool. It does not replace an identity provider. Instead, it reuses existing investment and can either mint tokens itself or proxy an existing upstream OAuth 2.0 authorization server. It does not even need its own user management; it relies on a reverse proxy for authentication. The broker isMIT-licensed and developed in the open.

The broker'sdelegation and consentmodel centers on three objects.Permission setsare named, administrator-defined, human-readable groups of OAuth 2.0 provider scopes.Grantsare revocable, optionally time-limited delegations from a user to an agent.User sessionshold the encrypted provider tokens for one user and one third-party service, and are shared by all agents the user has delegated to. While standards like XAA focus on removing per-vendor consent screens, we see value in a central consent screen for user-agent interactions: it lets users reduce an agent's effective permissions when they are not comfortable granting everything it asks for. We deliberately do not expose OAuth 2.0 scopes as the unit of consent, because provider scope vocabularies are inconsistent and often too coarse for a person to evaluate. Consent should name a business capability, such as reading repositories, instead of presenting a raw scope string.

A sample consent screen.

One of our core decisions is to keep OAuth 2.0 ceremonies out of both agents and MCP servers to reduce their complexity. As a consequence, we front-load token acquisition, so that all required third-party sessions exist before the agent needs them.

Sketch of the identity-centric architecture.

Starting at the top left, a browser-based portal initiates a standard OAuth 2.0 flow with the broker. This triggers the consent screen, ensures that third-party sessions are established, and either issues a token or delegates token issuance to an upstream authorization server. Where no user presence can be proven through a browser, we also support impersonation for chat bridges and other privileged clients.

The resulting token is then used to call the agent, which passes it on as-is in downstream tool calls. The agents are configured to use agentgateway as their MCP endpoint.

This gives us a central audit point and shields agents from integration work. We track ongoing work such as XAA and vendor products, for example from Okta, and will adopt such features when they make sense, without agents or MCP servers having to change.

At runtime, agentgateway and the broker act as a gate that splits the world into two spheres: agents and tools. The agent can access tool providers on behalf of its user if the agent's permissions and the user's consent allow it, but it never receives a provider token.

Runtime view: agent–tool interaction.

For each tool call, the agent sends its user-agent token only to the trusted gateway. Agentgateway validates that token and asks the broker to exchange it for an access token issued by the target's OAuth 2.0 infrastructure, refreshing it if needed. That credential returns only to the gateway, which replaces the authorization header before forwarding the request to the target. A revoked or expired grant blocks future exchanges, but it cannot revoke a provider token that has already been issued.

To put it all together, imagine a user asking an agent in Google Chat to summarize their open GitHub pull requests. The Chat bridge impersonates the user towards the broker and obtains a user-agent token for the agent. When the agent calls the GitHub MCP server through agentgateway, the gateway asks the broker to exchange that token for a GitHub token. The exchange only succeeds if the user has granted the agent a permission set that covers reading repositories. The agent returns the summary without ever seeing the GitHub token.

## Beyond Token Exchange

Layers of authorization.

Most of our active design work happens around authorizing individual tool calls. The token exchange is a fairly coarse access decision that takes the user's choices and the agent's maximum boundary into account. To go further, we integratedOpen Policy Agent (OPA)into agentgateway through its external processing (ExtProc) extension point. This reuses our existing platform investment into OPA, which is fully connected to our enterprise access management systems.

Next, we are integrating central tool approvals into this setup, so we do not have to rely on local agents making the right choices. Users approve tools in the broker's consent interface; the ExtProc extension next to agentgateway enforces the decision. The mechanism works independently of where the agent runs: locally, on our platform, or on other vendors' agent platforms.

Approvals are, however, a crutch: many users will rubber-stamp them once approval fatigue sets in. For high-risk transactions, we therefore also want to support Client-Initiated Backchannel Authentication (CIBA) in the broker, for example to obtain an approval via Okta Verify. Intent-based access control is another area we are actively investigating.

Today, we rely heavily on plain OAuth 2.0 access tokens that tie the user's and the agent's identities together. From operating our existing microservice identity infrastructure, we know that a central security token service (STS) that must be called on every hop can become expensive or prohibitive in terms of latency. We are therefore looking to extend our model with standards likeSPIFFE, to separate the attestation of the agent's identity from that of the human.

## Building Agentic Identity Together

Agentic identity magnifies problems we have known since microservices: machine identity, access across many third-party systems, and access decisions that combine user and agent permissions. Our answer so far is a central broker for delegation, consent, and token exchange, combined with policy enforcement at the gateway. This keeps OAuth 2.0 ceremonies out of agents and MCP servers and gives users one place to see and revoke what their agents can do.

The Agentic Identity Broker is available onGitHub, with documentation atagenticidentitybroker.dev, and specifications used to develop it being part of the code. Try it out, open issues, and send contributions. We would love to hear how you approach agentic identity in your organization.

We're hiring! Do you like working in an ever evolving organization such as Zalando? Consider joining our teams as aMachine Learning Engineer!

## Related posts

# Agentic Engineering at Zalando: a snapshot

We look back at our journey of agentic engineering at Zalando, sharing our learnings and approaches that worked well...Read more...

Bartosz Ocytko

Executive Principal Engineer

Aug 14

2026

# JSON Web Keys (JWK): Rotating Cryptographic Keys at Zalando

Secret rotation is a vital security measure in many contexts. Learn how we automate this process using JSON Web Keys...Read more...

Jan Brennenstuhl

Principal Software Engineer

Jan 21

2025

# Rejecting Invalid Ingress Routes at Apply Time

How Zalando used Skipper as a validating admission webhook to reject invalid filters and predicates at apply time,...Read more...

Veronika Volokitina

Software Engineer

Apr 09

2026
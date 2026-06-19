---
title: Enterprise-Managed Authorization: Zero-touch OAuth for MCP | Model Context Protocol Blog
url: https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth/
date: 2026-06-18
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-06-20T02:40:49.354087
---

# Enterprise-Managed Authorization: Zero-touch OAuth for MCP | Model Context Protocol Blog

# Enterprise-Managed Authorization: Zero‑touch OAuth for MCP

## Per‑user auth is high friction
- Standard MCP auth is user‑scoped and requires individual consent for each server.  
- Enterprise onboarding becomes manual: every employee must authorize every service.  
- Security teams lack centralized policy enforcement and audit trails.  
- Personal and corporate accounts can be mixed, increasing risk.  
- The per‑user authorization burden hampers MCP adoption and leads to brittle work‑arounds.

## Authorize once, inherit everywhere
- The organization’s IdP becomes the authoritative decision‑maker for MCP server access.  
- Administrators set policies once; users authenticate via single sign‑on (SSO).  
- The client receives an Identity Assertion JWT Authorization Grant (ID‑JAG) from the IdP and exchanges it for an MCP access token, eliminating per‑server consent screens.  
- Resulting benefits:  
  - Single authorization that propagates to all enabled servers.  
  - Centralized policy management and auditable access decisions in the IdP console.  
  - Prevention of accidental data flow between personal and enterprise accounts.

## Early adopters
- **Identity providers:** Okta (first supported IdP) offers Cross App Access (XAA) for provisioning MCP access.  
- **Clients:** Anthropic integrated EMA in its shared MCP layer for Claude products; Visual Studio Code added EMA support in the IDE.  
- **Servers:** Asana, Atlassian, Canva, Figma, Granola, Linear, Supabase, Slack (in progress) and others now support EMA.  
- Quotes from industry leaders highlight the security, scalability, and user experience improvements.

## Get involved
- Review the EMA specification and implement support in clients, servers, or identity platforms.  
- Resources:  
  - Requirements document outlining the flow for all parties.  
  - `ext-auth` repository and draft specification for implementation details.  
- Join the EMA Interest Group to discuss, share compatibility reports, and contribute to the extension’s evolution.

## Acknowledgements
- Thanks to the MCP community, authors of SEP‑990, maintainers of the `ext-auth` repository, and early testers from identity and MCP providers who advanced the specification.
---
title: Agent Auth | WorkOS
url: https://workos.com/changelog/agent-auth
date: 2026-09-05
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-09-05T10:36:01.750182
---

# Agent Auth | WorkOS

# Agent Auth – Changelog (September 2 2026)

## Overview
- Introduces **Agent Auth** (early access) to give software agents real identities and credentials within AuthKit.
- Replaces long‑lived API keys or user‑session borrowing with short‑lived, tightly scoped tokens.

## Key Features
- **Blueprints**: Define what actions an agent is permitted to perform.
- **Token Model**: Each execution receives a short‑lived token that includes:
  - Agent identifier
  - User or organization it acts on behalf of (if any)
  - Agent‑specific permissions
- **Access Modes**:
  - *Delegated*: Agent acts on behalf of a user.
  - *Autonomous*: Agent operates with scoped access within an organization.
- **Revocation**: Sessions can be revoked instantly when needed.

## Getting Started
- Interested parties can request access via email or Slack.
- Detailed documentation is available in the docs site.

## Contributors
- Madison Packer  
- Julie Shin  

## Hiring
- WorkOS is expanding globally and hiring for various roles.  
- Link to view open positions is provided.

## About WorkOS
- Builds developer tools that enable rapid addition of enterprise features to applications.  
- More information can be found on the company’s website.
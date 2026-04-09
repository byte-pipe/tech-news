---
title: Federated app store for self-hosted AI agents (Apache-2.0) - DEV Community
url: https://dev.to/agentsystems/federated-app-store-for-self-hosted-ai-agents-apache-20-19ka
site_name: devto
fetched_at: '2025-11-10T19:15:13.019222'
original_url: https://dev.to/agentsystems/federated-app-store-for-self-hosted-ai-agents-apache-20-19ka
author: Brandon Bennett
date: '2025-11-05'
description: Self-hosted app store for AI agents. Federated discovery, container isolation, run on your... Tagged with ai, opensource.
tags: '#ai, #opensource'
---

Self-hosted app store for AI agents. Federated discovery, container isolation, run on your infrastructure.

The problem: most organizations either build every agent in-house or send their data to third-party servers.

You wouldn't build your own email client or maps app - you'd download one. AI agents should work the same way. I spent a year building the infrastructure to make that possible: discover agents built by others, run them on your infrastructure (private cloud, on-premises, or local) without sending your data to third-party servers.

Key architecture:

* Federated Git-based index (fork-based ownership, no gatekeepers)
* Container isolation + egress proxy (you configure which URLs agents can access)
* Credential injection (API keys configured on host, not in agent images)
* Model abstraction (works with Ollama local, cloud APIs, or hybrid)
* Hash-chained audit logs

The platform works. The agent index is mostly empty, but someone has to build the rails so the trains can run.

Apache-2.0 open source. Pre-release but functional.

GitHub:https://github.com/agentsystems/agentsystems

Docs:https://docs.agentsystems.ai

Looking for:

* Agent builders to publish to the index
* Security researchers to review the architecture
* Organizations that need self-hosted AI infrastructure

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse

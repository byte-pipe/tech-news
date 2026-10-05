---
title: We want you to build the next Git platform on Cloudflare | Cloudflare Blog
url: https://blog.cloudflare.com/next-git-platform-on-cloudflare/
date: 2026-10-04
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-10-05T12:21:19.379048
---

# We want you to build the next Git platform on Cloudflare | Cloudflare Blog

# We want you to build the next Git platform on Cloudflare

## Vision of the next Git platform
- Traditional Git workflows were designed for human developers; the future will be driven by autonomous agents that write, test, review, and maintain code.
- Hundreds or thousands of agents may work on the same repository simultaneously, raising questions about coordination, conflict resolution, review processes, and provenance of changes.
- Cloudflare is inviting developers to define what the “next GitHub” looks like for this agentic era.

## Artifacts: the foundation
- Launched earlier this year as a versioned filesystem that speaks Git and can scale to millions of repositories.
- Provides programmable primitives: create/fork repositories, versioned storage for code and agent context, and standard Git operations.
- Designed to let developers focus on higher‑level coordination, review, and developer experience for massive agent collaboration.

## New capabilities since launch
- **Deploy Artifacts repos to Workers**: Pushes to the production branch automatically build and deploy a Worker; other branches generate preview Workers for isolated testing.
- **Manage Artifacts from Workers**: Workers can bind to Artifacts, create/fork repos, read files, issue repo‑scoped Git tokens, and orchestrate agent tasks programmatically.
- **Event subscriptions**: Artifacts emits events for repo creation, forks, pushes, etc. Workers can subscribe to trigger CI, code‑review agents, or deployments in response to each event.
- **Data jurisdiction**: Namespaces can be set to U.S. or EU jurisdiction, enforcing the same restriction for all repositories within the namespace.
- **Metrics dashboard**: Cloudflare dashboard now shows per‑repo operations, pulls, pushes, errors, and error rates; metrics are also queryable via API.
- **Pricing**: Usage billed based on repository operations and stored data, with billing starting October 15 2026.

## Competition: build the next Git platform
- Goal: create a platform where multiple agents work concurrently on code, rethinking repositories, branches, pull requests, worktrees, code review, merge conflicts, and agent context.
- Submissions must demonstrate at least concurrent multi‑agent changes; originality beyond a simple GitHub clone is expected.

### How to enter
- Submit a 5–10 minute video showing the built solution, its benefits for agents and developers, and its operation.
- Provide a link to source code under a permissive open‑source license (MIT, Apache, BSD).
- Include clear instructions for running or trying the project.
- Deadline: October 14 2026.

### Why participate
- Top three projects earn a trip for two team members to Cloudflare Connect in San Francisco.
- First place receives $25 000 in Cloudflare credits and an invitation to the VIP speaker dinner.

## Getting started
- Artifacts is in open beta for customers on the Workers Paid plan.
- A ready‑to‑use prompt is provided to create your first Artifacts repository and begin pushing code.
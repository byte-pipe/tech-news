---
title: Temporary Cloudflare Accounts for AI agents
url: https://blog.cloudflare.com/temporary-accounts/
date: 2026-06-20
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-06-21T11:07:40.765819
---

# Temporary Cloudflare Accounts for AI agents

# Temporary Cloudflare Accounts for AI agents

## Overview
- Cloudflare now offers **temporary accounts** that let AI agents deploy Workers, APIs, and websites without a prior human‑driven sign‑up.
- Agents can run `wrangler deploy --temporary` to create a deployment that lives for 60 minutes.
- Within that window the temporary account can be claimed and turned into a permanent Cloudflare account; otherwise it expires automatically.

## Why frictionless deployments matter
- Background AI sessions lack a human in the loop; any browser‑based OAuth, copy‑paste token, or MFA step blocks the agent.
- Agents rely on rapid “write → deploy → verify” cycles; throwaway, cheap targets enable trial‑and‑error.
- Emerging agent platforms expect deployment to “just work,” without requiring users to sign up for new services.

## How it works
- The feature is built into **Wrangler**, Cloudflare’s CLI for project bootstrapping, configuration, and deployment.
- When an unsigned agent runs `wrangler deploy`, Wrangler prints a message about the `--temporary` flag.
- Re‑running the command with `--temporary` makes Cloudflare provision a temporary account, issue an API token to Wrangler, and return a claim URL for later human ownership.

## Deployment and iteration flow
1. **Write code** – the agent generates a Worker (e.g., a “hello world” script) based on a prompt.
2. **Deploy** – the agent executes `wrangler deploy --temporary`, receives a preview URL, and curls it to verify output.
3. **Iterate** – the agent can modify the script (e.g., change the greeting) and redeploy repeatedly within the 60‑minute window.

## Claiming the account
- At any time, the claim URL can be opened; the user signs in or signs up for Cloudflare and claims the temporary account.
- Claiming transfers ownership of all resources created during the temporary period (Workers, databases, bindings, etc.).
- Unclaimed accounts are automatically deleted after 60 minutes.

## Road to frictionless agentic deployments
- Cloudflare is removing other signup barriers:
  - Partnership with Stripe and a new protocol to let agents provision accounts, start subscriptions, register domains, and obtain API tokens without manual steps.
  - Collaboration with WorkOS on `auth.md`, enabling agents to create accounts via standard OAuth flows.
- Temporary accounts are one piece of a broader effort to make Cloudflare fully agent‑ready.

## Limitations & next steps
- Temporary accounts have current capability limits that may evolve; developers should consult the official documentation.
- Users are encouraged to experiment, share builds on X, or discuss feedback in the Cloudflare Community.
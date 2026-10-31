---
title: The federated code forge · The Tangled Blog
url: https://tangled.org/blog/forge/
date: 2026-10-30
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-10-31T19:04:20.597513
---

# The federated code forge · The Tangled Blog

# The federated code forge · The Tangled Blog

## Overview
- Centralised code forges have become fragile; reliance on external uptime and stewardship is problematic.  
- Email and Git have proven durable open protocols, though they lack modern user experience.  
- Tangled combines the longevity of open protocols with the polish of a traditional forge, offering a truly federated solution.  
- Users can self‑host any component (Git hosting, CI runners, API server, UI) and still collaborate across the network.  
- Built on the AT Protocol, Tangled is highly extensible: custom extensions, firehose subscriptions, and bespoke “knots” can run on platforms like Cloudflare Workers.  
- The design emphasizes hackability and agent‑friendliness, positioning Tangled as a future‑proof code forge.

## Product updates

### A fresh look!
- UI rebuilt with Svelte on the new architecture.  
- Faster, more visually consistent, and uses the Timeless Sans typeface.

### A bobbin near you
- Previously a single Go monolith (theappview) with SQLite in Sweden; latency issues for distant users.  
- New edge‑deployed Svelte frontend paired with a diskless, in‑memory Rust indexer service called **bobbin**.  
- Bobbins run in 11+ global regions, delivering low‑latency API and UI responses.  
- Read‑only bobbin handles only AT Protocol data; other functionality moved to supporting services.

### The new data model and repo‑owned data
- Lexicons updated to `org.tangled.*` (replacing `sh.tangled.*`).  
- **Knot2**: Rust‑based knot server with integrated custom Git and SSH servers.  
- Issues, PRs, comments, reactions, labels, collaborators, and blocklists are stored as Collaborative Objects (COBs) directly in the repository as Git object chains.  
- Knots act like Personal Data Stores (PDS), syncing records via the AT Protocol firehose.  
- Attestation records (`org.tangled.graph.attestation`) are written to the user’s PDS for two‑way verification.  
- Self‑hosters must upgrade knots to v1.20.0 following the provided guide.

### Organizations
- Organizations are full AT Protocol accounts with their own DID and handle, hosted on a Tranquil PDS instance.  
- Password‑less, delegated accounts created via the New Organization page, yielding URLs like `<name>.tngl.sh`.  
- Owners can invite members; any member can act on behalf of the organization for repo actions.  
- Handles can be swapped for custom domains; migration tools for existing “org‑like” accounts are in development.

### Stacked PRs for everyone
- Revised PR workflow supports stacked pull requests for all users, whether using Jujutsu or plain Git.  
- Git users gain inter‑diff capabilities between PR rounds; Jujutsu users can inter‑diff individual changes.

### Launch weeks ahead
- Upcoming features: private repositories, CLI, SDKs for multiple languages, and agent skills.  
- Rollout will be staggered over the next few weeks.

## Call to action
- “Your code, your network. Come build with us on Tangled.”  
- Sign‑up invitation provided.
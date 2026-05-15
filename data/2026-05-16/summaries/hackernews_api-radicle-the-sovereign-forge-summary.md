---
title: Radicle: the sovereign forge
url: https://radicle.dev/
date: 2026-05-15
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-16T06:02:09.237655
---

# Radicle: the sovereign forge

# Radicle: the sovereign forge

## Synopsis
- Radicle is an open‑source, peer‑to‑peer code collaboration stack built on Git.  
- It operates without a central authority; repositories are replicated across peers.  
- Users retain full control of their data and workflow.  
- The core repository is identified as `rad:z3gqcJUoA1n9HaHKufZs5FCSGazv5`.

## Get started
- Latest release: Radicle 1.8.0 (commit `edde15d9ea700a70de04558fafc0b55360e9f5d2`, dated 2026‑03‑26).  
- Installation command: `curl -sSLf https://radicle.dev/install | sh`.  
- Alternative: build from source.  
- Supported platforms: Linux, macOS, BSD.  
- A graphical client, **Radicle Desktop**, is available for a richer collaborative experience.

## How it works
- **Protocol**: Uses cryptographic identities, Git for data transfer, and a custom gossip protocol for repository metadata.  
- **Data security**: All social artifacts are stored in Git and signed with public‑key cryptography; authenticity is verified automatically.  
- **Autonomy**: Users can run their own nodes, providing censorship‑resistant collaboration and a resilient network.  
- **Local‑first**: Functionality remains available offline; data ownership simplifies migration, backup, and access.  
- **Evolvable & extensible**: Collaborative Objects (COBs) implement issues, discussions, code review as Git objects, allowing custom collaboration flows.  
- **Modular design**: The stack includes a CLI, web UI, TUI, a Radicle Node, and an HTTP daemon; each component can be swapped or extended.

## Contributing
- Radicle is free and open source under MIT and Apache 2.0 licenses.  
- Contributions of code are welcomed.

## Updates (selected recent entries)
- 23 Apr 2026 – Migration to `radicle.{dev,network}`.  
- 30 Mar 2026 – Release of Radicle 1.8.0 and disclosure of a vulnerability in signed references.  
- 20 Mar 2026 – Release of Radicle 1.7.1.  
- 13 Jun 2025 – Radicle Desktop launched.  
- 10 Sep 2024 – First stable release Radicle 1.0.0.  
- 18 Apr 2023 – Announcement of Radicle heartwood.

## Blog (highlights)
- 14 Aug 2025 – “Jujutsu + Radicle = ❤️”.  
- 12 Aug 2025 – “Canonical References”.  
- 23 Jul 2025 – Using Radicle CI for development.  
- 30 May 2025 – Integration with GitHub Actions.

## Feedback
- Join the Zulip community or email `feedback@radicle.dev`; messages are posted automatically to the `#feedback` channel on Zulip.
---
title: The Atproto Spaces Alpha is Live - AT Protocol
url: https://atproto.com/blog/atproto-spaces-alpha
date: 2026-08-20
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-08-24T07:47:11.426827
---

# The Atproto Spaces Alpha is Live - AT Protocol

# The Atproto Spaces Alpha is Live

## Overview
- Atproto Spaces (formerly “permissioned data protocol”) is an alpha extension enabling non‑public data on atproto.  
- The alpha is open with running code, SDKs, a sample app, and a hosted PDS for experimentation.  
- Intended for development only; breaking changes are expected and production use is discouraged.

## What is a Space?
- A lightweight, mini‑atproto network that can be gated to specific DIDs (users or apps).  
- Stores JSON records defined by Lexicons; records reside in per‑space permissioned repositories on the author’s PDS.  
- Access control is provided by a space authority (a DID); data is readable by anyone with access but is **not** encrypted.  
- Use cases range from single‑member spaces for settings, drafts, bookmarks to large community spaces with millions of participants and gated subscription content.  
- Sync protocol is lighter‑weight and supports real‑time sync directly from PDS hosts, without public relays.

## Hosted PDS for Experimenting
- A shared sandbox PDS is available via an invite code from your BPS account.  
- Intended solely for testing; moderation violations result in permanent bans.  
- Data is temporary, may be deleted or altered without notice; the entire sandbox will be removed after the alpha.  
- Updates to the hosted PDS and SDKs are posted weekly on the atmosphere.community announcements thread.

## Running a Spaces‑Capable PDS
- Official Docker image: `ghcr.io/bluesky-social/atproto:pds-spaces-alpha` (tagged, no extra configuration needed).  
- Not for production: schemas may change, migrations are not guaranteed, and upgrades may be impossible.  
- Encouraged to run the image with test data, explore applications, and report bugs.  
- Early ecosystem implementations include:
  - ZDS (Zig)
  - atproto‑crates (Rust)
  - rsky (Rust, maintained by Blacksky)
  - HappyView (AppView framework)

## Example App & Alpha SDK
- Sample bulletin board app: `https://bulletin.my` (space‑based board visible only to followers).  
- Source code: `https://github.com/bluesky-social/bulletin`.  
- TypeScript `@atproto` packages released as alpha snapshots (install with the `alpha` tag).  
- Developers can run locally, fork, or remix the app and test against any PDS implementation.

## Specification & Reference Implementation
- Latest protocol specification: located in the `proposals` repository.  
- Reference implementation: `atproto spaces` branch of the main atproto repo, actively developed.  
- Contributors should use the spec as the collaboration baseline and open issues for ambiguities or divergences.

## Alpha Caveats
- No thorough security review; do not upload sensitive or personal data.  
- No backups; destructive migrations may occur.  
- Expect frequent breaking changes and unstable database schemas.  
- Use only for experimental purposes, not for real‑world production workloads.
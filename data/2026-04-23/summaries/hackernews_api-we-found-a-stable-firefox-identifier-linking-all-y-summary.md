---
title: We Found a Stable Firefox Identifier Linking All Your Private Tor Identities
url: https://fingerprint.com/blog/firefox-tor-indexeddb-privacy-vulnerability/
date: 2026-04-23
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-04-23T09:46:14.685881
---

# We Found a Stable Firefox Identifier Linking All Your Private Tor Identities

# Summary of “We Found a Stable Firefox Identifier Linking All Your Private Tor Identities”

## Vulnerability Overview
- A privacy bug affects all Firefox‑based browsers, including Tor Browser.
- Websites can obtain a deterministic, process‑lifetime identifier from the ordering of entries returned by `indexedDB.databases()`.
- The identifier is process‑scoped, not origin‑scoped, allowing different sites to see the same fingerprint.
- In Private Browsing, the identifier persists after all private windows are closed as long as the Firefox process remains alive.
- In Tor Browser, the identifier survives the “New Identity” reset, breaking the intended isolation.

## How the Identifier Is Created
- In Private Browsing, database names are mapped to UUID‑based filenames stored in a global hash table (`StorageDatabaseNameHashtable`).
- The mapping is:
  - keyed only by the database name string,
  - shared across all origins,
  - retained for the lifetime of the IndexedDB QuotaClient,
  - cleared only on a full browser restart.
- `indexedDB.databases()` gathers filenames into an `nsTHashSet` and returns them in the hash set’s iteration order, which is deterministic for a given process.
- Because the UUID mappings and hash table layout are stable, the returned order becomes a stable identifier for the browser process.

## Proof of Concept
- Two unrelated origins run the same script:
  1. Create a fixed list of named databases.
  2. Call `indexedDB.databases()`.
  3. Log the returned order.
- Both origins receive the same permutation while the process runs; a restart changes the permutation.
- The order does not reflect creation order and persists across tabs, private windows, and “New Identity” actions.

## Privacy Impact
### Cross‑origin tracking
- Different sites can infer they are interacting with the same browser process, linking user activity without cookies or shared storage.

### Same‑origin tracking
- In Private Browsing, the identifier survives after closing all private windows, enabling recognition of later visits in a seemingly fresh session.

### Tor Browser significance
- Tor Browser’s core design aims to prevent any process‑level linkability; the stable identifier directly defeats the “New Identity” guarantee.

## Why This Matters
- Private browsing modes and privacy‑focused browsers are expected to hide process‑level identifiers.
- The bug shows that even harmless‑looking APIs can become tracking vectors when they expose deterministic internal state.
- Developers should consider that privacy bugs may arise from implementation details, not just explicit data leaks.

## Fix and Mitigation
- Mozilla released a fix in Firefox 150 and ESR 140.10.0 (Bug 2024220).
- The patch canonicalizes or sorts the results of `indexedDB.databases()` before returning them, removing the entropy that formed the identifier.
- The fix applies to all Firefox‑based browsers, including Tor Browser, because the issue originates from Gecko’s IndexedDB implementation.
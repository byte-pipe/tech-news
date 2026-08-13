---
title: How Tailscale helped find the SQLite WAL-Reset bug
url: https://tailscale.com/blog/sqlite-wal-reset-bug
date: 2026-08-13
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-13T11:43:33.057970
---

# How Tailscale helped find the SQLite WAL-Reset bug

# How we tracked down a 16‑year‑old SQLite bug

## Tailscale’s database architecture
- Our control plane is split into internal “shards”; each tailnet lives on one shard at a time.  
- Every shard runs a single Go process that exclusively writes to its own SQLite database (single‑writer design).  
- We have taken full SQLite snapshots every few minutes and store them in S3; this backup pipeline worked without issue since early 2023.  
- In August 2023 a data pipeline reading the S3 backups flagged corruption; PRAGMA integrity_check confirmed a damaged database.  
- Over six months we observed 19 separate corruption events across different shards.  
- Corruption affected only configuration metadata (no private keys or traffic); recovery sometimes lost recent device additions or config changes.  
- Each corruption required stopping the shard’s control‑plane process, causing >1 hour downtime initially, later reduced by faster recovery.  
- While the shard was down, devices could not obtain new peer lists, losing admin‑console and API access, though existing connections stayed alive.  
- Global status alerts were posted even when only a few tailnets were impacted, eroding overall trust.

## Trying to find the fault
- Initial reviews of recent code changes and the low‑level SQLite integration (written years earlier) revealed nothing suspicious.  
- No common factor linked the incidents: they spanned shards, customers, features, times of day, and load levels.  
- The irregular timing prevented reproducible tests, forcing us to add passive forensic telemetry to live systems.  
- A six‑week lull (Oct‑Dec) gave a false sense of resolution before incidents resumed.  
- We engaged SQLite core developers via a support contract, gaining direct expertise.  
- Together we evaluated hypotheses such as broken POSIX locks on close(), memory mismanagement, and accidental multi‑threaded use with thread safety disabled; each was systematically ruled out through incident‑by‑incident diagnostics.

## The transactions that didn’t bark
- While still operating, we hardened our recovery process:
  - Immediate hard‑stop of a shard on detection of corruption.  
  - Automated backup monitor continuously running PRAGMA integrity_check.  
  - Updated runbooks and on‑call training, cutting response time to under an hour.  
- To avoid full rollbacks or risky repairs, we built a transaction‑logging pipeline that streamed every modifying SQL statement to a separate log file.  
- Because SQLite on each shard is single‑writer with serialisable transactions, the log provided a linear, deterministic history of all changes.  
- This log became a crucial clue that eventually led us to the underlying bug.
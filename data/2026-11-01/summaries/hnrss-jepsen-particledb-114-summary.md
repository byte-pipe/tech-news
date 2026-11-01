---
title: Jepsen: ParticleDB 1.1.4
url: https://jepsen.io/analyses/particledb-1.1.4
date: 2026-10-31
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-11-01T18:53:38.428642
---

# Jepsen: ParticleDB 1.1.4

# Jepsen: ParticleDB 1.1.4 – Summary

## Background
- Modern applications spread state across many systems (databases, caches, queues, etc.), making coordination difficult.
- ParticleDB aims to unify these workloads, offering:
  - Transactional SQL
  - Key‑value store
  - Vector search
  - Live analytics
  - User‑defined functions called *Particles*
- Interfaces include Postgres and Redis protocols, plus custom gRPC and HTTP/2 APIs.
- Implemented in Rust; claims to be much faster than Postgres while keeping safety guarantees.
- Originated at Orkes to support their Conductor workflow platform; initial 1.0.0 release was limited to Conductor’s needs.
- Prior to broader release, Orkes refactored ParticleDB (new wire protocol, more datatypes, OLAP queries) and soft‑launched versions on particledb.ai.
- Jepsen testing began with version 1.1.4.
- Replication via Raft is only in enterprise cloud deployments; the builds tested here are single‑node only.

## Safety
- Home page advertised a “formally proven” TLA+ proof, but no specification was provided.
- Three WAL sync modes:
  - `fsync` – sync on every commit
  - `groupsync` – batch multiple transactions into one fsync (claimed “stronger durability”)
  - `nosync` – skip fsync entirely
- Documentation conflicted on durability of `groupsync`; some sources said it matches `fsync`.
- Marketing claimed “Full ACID. 159K TPS” but also mentioned “snapshot isolation,” which is not full serializability.
- Standard SQL isolation level statements are ignored or silently overridden.
- Isolation is controlled by the `--txn-mode` startup flag with four modes:
  - `fast` – no locks, commit‑on‑write (high throughput, weak isolation)
  - `occ` – overlay + commit‑time OCC validation (default, intended for general OLTP)
  - `zero-copy-occ` – partition‑pinned OCC, skips cross‑partition coordination (high‑throughput on partition‑affine workloads)
  - `table-2pl` – exclusive table locks on first touch (strictest serialization)
- Documentation was ambiguous about the guarantees of each mode; terms like “Jepsen‑safe” were used without definition.
- Later internal operator guide clarified consistency models:
  - `fast` – unknown consistency
  - `occ` / `row-2pl` – Snapshot Isolation
  - `zero-copy-occ` – Snapshot Isolation
  - `serializable-ssi` – Serializable
  - `table-2pl` / `serializable` – Strong Serializable
- Default settings appeared to be `occ-v3` (snapshot isolation) with `groupsync` WAL mode.

## Test Design
- Built a Jepsen test suite covering ParticleDB versions 1.1.4 through 1.1.18.11.rc-22.
- Executed on Debian 13 nodes in both containers and EC2 VMs.
- Harness could:
  - Kill the ParticleDB process to simulate crashes.
  - Use LazyFS to lose unfixed writes.
  - Truncate or corrupt disk files.
- Tested every combination of transaction mode (`fast`, `occ`, `zero-copy-occ`, `table-2pl`) and WAL sync mode (`fsync`, `groupsync`, `nosync`).
- Initially attempted to use the official Java SDK, but the JAR/source were unavailable.
- Switched to the Postgres JDBC client (v42.7.11) and later added support for the ParticleDB Java SDK (versions 1.0.0‑1.0.2).

## Workloads
- Reused several existing Jepsen SQL workloads and created new ones specific to ParticleDB.
- The primary workload (`rw`) performed random transactions with reads and writes of integer values keyed by unique integers.
- Each value was stored in a single row and accessed via both primary and unindexed secondary keys.
- Keys and values were encoded using a variety of data types (details truncated in the excerpt).
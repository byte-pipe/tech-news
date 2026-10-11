---
title: A versioned filesystem for disposable sandboxes
url: https://www.shayon.dev/post/2026/283/versioned-filesystem-for-disposable-sandboxes
date: 2026-10-12
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-10-12T06:01:24.575338
---

# A versioned filesystem for disposable sandboxes

# A versioned filesystem for disposable sandboxes

## Overview
- Tines 3B runs each workflow step inside a fresh Linux sandbox that is discarded after execution.  
- To retain state across sandboxes, every step gets a persistent, version‑ed filesystem.  
- Changes made by a step behave like a database transaction: they are committed only if the step finishes successfully; otherwise they are discarded.

## Core components
- **Sandbox** – runs the step’s code inside gVisor.  
- **Nest** – a gVisor gofer that serves files to the sandbox; it lazily materializes files into temporary in‑memory copies and tracks modifications.  
- **Spongeblob** – the storage engine that stores immutable snapshots (volumes) on local disk and optionally copies them to S3 for recovery and cold storage.  
- **LisaFS** – the low‑level file‑descriptor layer used by Nest.

## Design goals (wish list)
- Provide a true POSIX filesystem compatible with tools like Git, SQLite, compilers, and pip.  
- Keep all data off the machine executing the step, allowing later steps to run elsewhere.  
- Ensure fast, local hot‑path writes (≈2–4 ms for a 128 KB write) without network round‑trips per operation.  
- Support parallel steps writing to the same volume without corruption or silent overwrites.  
- Operate without S3 (self‑hosted deployments).  
- Remain simple: a single durable log, one owner per disk, no extra databases or consensus systems.

## How a step interacts with the filesystem
- A step declares a volume in its Dockerfile; the volume is mounted at `/storage/<name>` inside the sandbox.  
- When a file is opened, Nest:
  1. Finds the file in the pinned snapshot.  
  2. Copies it to a tmpfs file on the host.  
  3. Returns a real file descriptor to the sandbox.  
  4. Records any subsequent changes (creates, renames, deletes, written chunks).  
- Reads, writes, and `mmap` operate on the local tmpfs copy at memory speed; only control operations cross the sandbox boundary.  
- `fsync` inside the sandbox flushes only the local copy; durability is achieved when the step completes successfully.

## Versioning and commits
- A volume consists of immutable snapshots plus a pointer to the current snapshot.  
- On successful step exit (`exit 0`), Nest uploads changed blocks; Spongeblob creates a new snapshot (copy‑on‑write) and atomically moves the pointer forward.  
- On failure or crash, the sandbox’s local changes are discarded and the pointer remains on the previous snapshot.  
- This model is similar to Git commits and multiversion concurrency control: readers continue to see the snapshot they started with while writers publish new snapshots without blocking.

## Copy‑on‑Write strategy
- Snapshots are stored efficiently using COW: only modified blocks are written for a new snapshot, avoiding full copies of the volume.  
- Large files may be fetched lazily (block‑level) to reduce upfront copy cost, while small files are still copied entirely for fast local access.

## Benefits
- Secure isolation: discarded sandboxes leave no residual state.  
- Deterministic state management: each step’s effects are either fully applied or not applied at all.  
- Fast local I/O with optional background replication to S3 for durability and eviction.  
- Simple architecture that satisfies POSIX expectations, parallelism, and self‑hosted operation without external consensus services.
---
title: Git at any scale · Cursor
url: https://cursor.com/blog/git-at-any-scale
date: 2026-08-19
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-21T06:52:11.783954
---

# Git at any scale · Cursor

# Summary of “Git at any scale · Cursor”

## Background
- Linus Torvalds created Git to replace BitKeeper for his own use in developing the Linux kernel, a highly decentralized project.
- Over two decades Git became an industry standard, but most open‑source projects and companies now use a centralized host despite Git’s distributed design.
- Hosting Git repositories at large scale proves to be unexpectedly difficult.

## What Makes Git Hard to Host
- **Distributed design**: every clone is a full copy; the server repository is not fundamentally different from a developer’s local copy.
- **Packfiles**: Git stores objects (blobs, trees, commits) in compressed packfiles, which are efficient locally but problematic for large‑scale server storage and networking.
- **Scalability limits**: a simple HTTP server in front of a disk repository cannot easily scale out across many disks or machines, limiting parallel operations and fault tolerance.

## Main Approaches to Scaling Git
1. **Distribute the filesystem** – replicate the on‑disk repository across multiple machines.
2. **Distribute the packfiles** – shard or replicate packfiles themselves.
3. **Distribute Git itself** – redesign Git’s storage and protocol layers.

## Why “Git without Packfiles” Doesn’t Work
- Git is a content‑addressable store keyed by SHA‑1, which suggests a key‑value backend, but the repository’s **DAG structure** forces sequential traversal.
- Operations (e.g., listing recent commits) require walking the DAG step‑by‑step; each step may need a network round‑trip if objects are fetched from a distributed store.
- Past attempts, such as Google’s DHT‑backed JGit implementation, showed that while on‑disk operations could work, the Git protocol still mandates sending whole packfiles over the network, leading to poor clone performance and eventual abandonment.

## GitHub’s Experience with Filesystem Distribution
- GitHub launched in 2008 as a Rails monolith, initially running on a single powerful machine with repositories stored locally.
- Scaling the web app was straightforward, but replicating the underlying Git data across many app instances raised the same storage problem.
- Early engineers tried to **distribute the filesystem** (e.g., using NFS) to keep the Rails code unchanged.
- Git’s assumptions about local filesystem semantics (locking, atomic writes, sync behavior) caused NFS to be **slow and buggy**, making this approach untenable.
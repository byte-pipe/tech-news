---
title: GitHub - pgbackrest/pgbackrest: Reliable PostgreSQL Backup & Restore · GitHub
url: https://github.com/pgbackrest/pgbackrest
date: 2026-04-27
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-04-28T06:04:01.911804
---

# GitHub - pgbackrest/pgbackrest: Reliable PostgreSQL Backup & Restore · GitHub

# pgBackRest – Reliable PostgreSQL Backup & Restore (archived)

## Notice of Obsolescence
- The project was archived on Apr 27 2026 and is now read‑only.  
- Development has stopped; the maintainer no longer has time or sponsorship to continue.  
- Forks are welcome, but new maintainers must establish their own trust and roadmap.

## Introduction
- pgBackRest provides reliable backup and restore for PostgreSQL, scaling to very large databases.  
- Latest stable version is **v2.58.0** (release notes on the Releases page).

## Key Features
- **Parallel backup & restore** – uses multi‑threading and fast compressors (lz4, zstd) to avoid compression bottlenecks.  
- **Local or remote operation** – custom TLS/SSH protocol enables secure backup/restore/archive with minimal configuration; remote PostgreSQL access is not required.  
- **Multiple repositories** – supports a fast local repo for recent restores and a remote repo for long‑term retention and redundancy.  
- **Full, differential, & incremental backups** – file‑level and block‑level options; avoids rsync time‑resolution issues; incremental saves only changed file parts.  
- **Backup rotation & archive expiration** – configurable retention policies for full/differential backups; WAL archive can be kept for all backups or only the most recent ones.  
- **Backup integrity** – per‑file checksums verified during backup, restore, and verify; fsync on files/directories ensures durability; optional hard‑link snapshots allow immediate cluster startup from a backup.  
- **Page checksums validation** – validates PostgreSQL page checksums on every copied file; warnings are logged without aborting the backup.  
- **Backup resume** – interrupted backups can resume from the last successful point, comparing checksums to ensure integrity; resume work runs on the repository host, reducing load on the database host.  
- **Streaming compression & checksums** – performed while copying files; remote repositories receive already‑compressed data; when compression is disabled a lightweight algorithm is used to save bandwidth.  
- **Delta restore** – uses manifest checksums to skip restoring files that already match the backup, dramatically cutting restore time.  
- **Parallel, asynchronous WAL push & get** – dedicated commands for WAL archiving; parallelism speeds up processing; asynchronous push de‑duplicates identical segments; asynchronous get pre‑queues decompressed WAL for fast replay, benefiting high‑latency storage (e.g., S3).  

These features collectively aim to provide fast, secure, and reliable backup and recovery for PostgreSQL environments, even at terabyte scale.
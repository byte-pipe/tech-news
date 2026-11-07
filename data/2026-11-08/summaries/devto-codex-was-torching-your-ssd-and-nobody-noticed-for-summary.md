---
title: Codex Was Torching Your SSD and Nobody Noticed for Months - DEV Community
url: https://dev.to/varshithvhegde/codex-was-torching-your-ssd-and-nobody-noticed-for-months-4c5h
date: 2026-11-02
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-11-08T09:03:35.778933
---

# Codex Was Torching Your SSD and Nobody Noticed for Months - DEV Community

# Small files mask massive flash wear

## Quick version
- A developer observed unusually high local disk writes and traced them to Codex CLI’s `logs_2.sqlite` database and its WAL file.  
- About 37 TB of writes were recorded over 21 days, roughly 1.7 TB per day (≈640 TB per year if the rate stayed constant).  
- The database size stayed roughly constant because new rows were inserted while old rows were deleted.  
- The root cause was an overly verbose TRACE logging path that ignored the expected `RUST_LOG` override.  
- Updating to version 0.142.0 reduced the noisy writes by around 85 %.  
- Users of older builds should upgrade and monitor SSD write‑counters.

## Numbers that made people look twice
| Metric | Value |
|--------|-------|
| Reported writes | ~37 TB |
| Reporting window | 21 days |
| Approx. daily rate | ~1.7 TB/day |
| Annualized at that rate | ~640 TB/year |

## Why the file size told you almost nothing
- Commands like `du -sh ~/.codex` and `ls -lh ~/.codex/logs_2.sqlite` only show current stored data, not cumulative writes.  
- The log database was designed to retain a bounded amount of diagnostic information: new rows were added, old rows removed, keeping the file size stable while the underlying storage experienced constant churn.  
- A stable file size is analogous to seeing the same number of occupied tables in a café at different times; it reveals nothing about the total number of customers that have sat there.

## What was generating all those writes
- The default logging level was TRACE, the most detailed level in Rust’s tracing ecosystem.  
- TRACE entries included low‑level events such as file opens, raw network/WebSocket activity, transport details, telemetry plumbing, and bridged dependency‑library messages.  
- TRACE‑level entries accounted for about 70 % of the retained log‑body size, creating a high‑volume diagnostic stream that was persisted locally.

## The three parts that stacked together
1. **TRACE was active where it should have been opt‑in** – enabling the most verbose logging by default turned routine interactions into massive diagnostic output.  
2. **`RUST_LOG=warn` did not fully quiet it** – the environment variable failed to override the internal sink for targets without an explicit setting, so users believed logging was reduced while writes continued.  
3. **SQLite turned event noise into storage churn** – inserting, deleting, indexing, and checkpointing frequent TRACE events caused many filesystem writes even though the database never grew large.

## The part the operating system does not show you
### SQLite write amplification
- SQLite in WAL mode appends each event to a WAL file, later checkpoints changes into the main database, deletes old rows, and updates indexes.  
- A single logical log event can therefore generate multiple physical writes on the filesystem.

### SSD write amplification
- SSDs write data in small pages but erase larger blocks; modifying a small part of a block often triggers a rewrite of the whole block, followed by garbage collection and wear leveling.  
- This internal movement means the flash receives more physical writes than the OS reports, especially under high‑churn, small random write workloads like the Codex log sink.

## Is 640 TB actually dangerous?
- Consumer SSDs typically have a TBW (terabytes written) rating of a few hundred TB; enterprise models are higher.  
- Exceeding the rated TBW does not instantly cause failure, but it shortens the expected lifespan and can lead to premature wear.  
- A development tool that silently consumes hundreds of terabytes of writes is a serious concern; updating to a version with reduced logging and monitoring SSD write counters are recommended.
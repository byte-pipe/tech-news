---
title: "Oracle Just Halved Its Always Free ARM Limits — Here's Exactly What to Do Before August 18, 2026 | CNELECAR"
url: https://www.cnelecar.com/blog/oracle-always-free-arm-limits-cut-2026/
date: 2026-08-06
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-06T07:11:51.302259
---

# Oracle Just Halved Its Always Free ARM Limits — Here's Exactly What to Do Before August 18, 2026 | CNELECAR

# Oracle Just Halved Its Always Free ARM Limits — What to Do Before August 18 2026

## The short answer
- Any Ampere A1 ARM instance larger than 2 OCPUs or 12 GB RAM, or more than one such instance, must be reduced or removed before August 18 2026 or Oracle will terminate the excess automatically.  
- The two free x86 micro‑instances are unaffected.

## What actually changed
| Resource | Old limit | New limit (effective Aug 18 2026) |
|----------|-----------|-----------------------------------|
| ARM (Ampere A1) OCPU | Up to 4 OCPUs | Up to 2 OCPUs |
| ARM memory | Up to 24 GB | Up to 12 GB |
| x86 micro instances | 2 × 1 OCPU / 1 GB | 2 × 1 OCPU / 1 GB (unchanged) |
| Other Always Free services | Available | Remain available |

- The ARM limit is a tenancy‑wide pool, not per‑instance. You may split the 2 OCPU/12 GB however you like, but the total cannot exceed that amount.  
- The x86 allowance is separate from the ARM pool.

## Why this is happening
- Oracle gave no official explanation; the likely reasons are capacity constraints and abuse management on a tier that was previously very generous.

## Your move, by scenario

### Scenario A – One 4 OCPU / 24 GB ARM instance
- Resize to 2 OCPU / 12 GB.  
- In the OCI Console: **Compute → Instances → More Actions → Edit**, set OCPU = 2 and memory = 12 GB, then save.  
- Back up the instance first; perform the resize now rather than waiting until the deadline.

### Scenario B – Two 2 OCPU / 12 GB ARM instances
- Keep only one instance.  
- Snapshot or image the instance you plan to retire, copy needed data to the survivor or Object Storage, then terminate the other.  
- After termination the tenancy is within the new 2 OCPU/12 GB limit.

### Scenario C – Two 1 OCPU / 1 GB x86 micro instances
- No action required; these instances are governed by a separate allowance that remains unchanged.

## What won’t save you (common mistakes)
- Ignoring the email and assuming it’s an error.  
- Waiting until the last day; console traffic and quota checks can cause delays.  
- Failing to back up before terminating; terminated instances and boot volumes are unrecoverable.  
- Assuming that stopping an instance frees the allocation; usually you must terminate to drop below the limit.  
- Counting x86 micro instances against the ARM quota; they are distinct.

## The bottom line
- The free ARM tier is now half of its former size.  
- Take action before August 18 2026:  
  * Resize a single large ARM instance to 2 OCPU/12 GB.  
  * Consolidate or terminate one of two medium ARM instances.  
  * Leave x86 micro instances untouched.  
- If Oracle terminates an over‑limit instance, you can relaunch within the new limits; data loss only occurs if you did not back up.  

*Consider moving critical workloads to a paid server if you need guaranteed resources.*
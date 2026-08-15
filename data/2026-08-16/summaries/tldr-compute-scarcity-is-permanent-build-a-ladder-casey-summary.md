---
title: Compute Scarcity Is Permanent. Build a Ladder. — Casey West
url: https://caseywest.com/compute-scarcity-is-permanent-build-a-ladder/
date: 2026-08-16
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-08-16T06:02:20.377720
---

# Compute Scarcity Is Permanent. Build a Ladder. — Casey West

# Compute Scarcity Is Permanent. Build a Ladder. — Casey West

## The Core Observation
- Cloud reliability docs assume the requested hardware will be available; AWS even states it as a contract.
- Recent GPU/TPU shortages have proven that assumption false: an eight‑GPU node may simply not exist, and retries cannot fix it.
- The bottleneck is the high‑bandwidth memory and advanced packaging needed for accelerators, a supply‑side limitation that cannot be solved by spending more or waiting longer.

## Why Existing Pattern Catalogs Miss This
- Major pattern catalogs (Azure, Google Cloud, AWS) cover throttling, retries, scaling, and redundancy, but none treat “compute you want may be unobtainable” as a failure mode.
- They address demand, uptime, and utilization, but not the acquisition of the required hardware.
- This creates a gap: architects have no named pattern for handling permanent compute scarcity.

## The Compute Fallback Ladder Concept
- **Definition**: An ordered set of substitute compute targets (rungs) that a workload falls through when its preferred accelerator is unavailable, with a mechanism to climb back when capacity returns.
- **Rungs**: From best to worst – preferred accelerator → alternate accelerator → smaller/quantized model on cheaper chip → CPU → cached or approximate answer. Lower rungs represent graceful degradation.
- **Selector**: Runtime policy that chooses the highest‑available rung at request time, not at deployment time.
- **Promotion Mechanism**: Moves workloads back up the ladder when higher‑tier capacity becomes available; without it the ladder becomes a one‑way slide.

## Existing Implementation Example
- Google Kubernetes Engine (GKE) provides a `ComputeClass` custom resource that lets you declare a priority list of machine types and handles active migration.
- Key fields:
  - `priorities`: ordered list of machine types (e.g., `a3-highgpu-8g`, `a2-highgpu-8g`, `g2-standard-48`, `n4` family).
  - `whenUnsatisfiable: ScaleUpAnyway` forces descent when a rung is unavailable.
  - `activeMigration: true` with `optimizeRulePriority` enables promotion back to higher tiers.
  - `nodePoolAutoCreation: true` allows autoscaler to create needed node pools on the fly.
- Descent and promotion are intentionally asymmetric; a consolidation delay controls how quickly the system climbs back.

## Practical Takeaways
- Treat compute scarcity as a permanent condition and design systems to degrade gracefully rather than relying on endless retries.
- Adopt the Compute Fallback Ladder pattern: define explicit fallback tiers, implement a runtime selector, and ensure a promotion path.
- Leverage existing tooling (e.g., GKE’s `ComputeClass`) or build similar abstractions to make the pattern concrete in code, turning it from a concept into a reusable component.
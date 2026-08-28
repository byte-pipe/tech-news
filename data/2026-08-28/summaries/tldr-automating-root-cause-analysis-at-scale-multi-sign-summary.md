---
title: Automating root cause analysis at scale: Multi-signal correlation for cloud native incident response | CNCF
url: https://www.cncf.io/blog/2026/08/24/automating-root-cause-analysis-at-scale-multi-signal-correlation-for-cloud-native-incident-response/
date: 2026-08-28
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-08-28T17:06:08.270793
---

# Automating root cause analysis at scale: Multi-signal correlation for cloud native incident response | CNCF

# Automating Root cause analysis at scale: Multi‑signal correlation for cloud native incident response

## Problem statement
- Atlassian runs hundreds of microservices across multiple regions; a single incident produces massive telemetry.
- Current RCA workflow is manual: on‑call engineer hops between metrics dashboards, log search, and tracing UI, then mentally correlates patterns and walks the service dependency graph.
- This process is serial, cognitively heavy, and depends on deep domain knowledge; minutes lost during user‑impacting incidents matter.

## Approach overview
- Treat root‑cause analysis as a **multi‑signal correlation** problem across three dimensions:
  1. **Signal type** – metrics, logs, traces.  
  2. **Time** – co‑occurring anomalies are likely related.  
  3. **Topology** – faults propagate along service‑dependency edges.
- Detect anomalies independently per signal, align them on a shared timeline, and trace them through the known dependency graph to produce ranked fault hypotheses.
- Design is modular: each anomaly detector is a plug‑in; the correlation engine works on a normalized event schema, enabling easy swapping or adding of detectors.

## System architecture – from raw telemetry to ranked hypotheses
### Step 1: Scope the search using service topology
- When an incident is detected, query the service dependency graph to isolate the call path that leads to the degraded user experience.
- Use OpenTelemetry‑derived service maps built from real‑time span parent‑child relationships, reducing the analysis set from hundreds to typically tens of services.

### Step 2: Detect anomalies independently per signal
- **Metrics (RED signals)** – monitor rate, error rate, duration per endpoint; use median absolute deviation for spikes and percentile bands for sustained deviations. Emit normalized anomaly events with severity, observed value, and baseline.
- **Distributed traces** – look for structural anomalies (unexpected exceptions, error propagation patterns, latency spikes) using statistical latency checks and pattern analysis; produce events tied to service and timestamp.
- **Logs** – apply embedding‑based clustering to group semantically similar log entries; flag clusters that are statistically novel. Handles high volume by avoiding line‑by‑line scans.
- All detectors output events in a common JSON schema (timestamp, service, signal_type, severity_score, details).

### Step 3: Temporal correlation – find co‑occurring anomalies
- Group events that occur within a configurable sliding window (default ±5 min) into **correlation bundles**.
- Compute a temporal cohesion score:  
  `S_temporal = (1 / N(N‑1)) × Σ exp(-|ti‑tj| / τ)`  
  where N = number of events, ti/tj = timestamps, τ = decay constant.
- Deduplicate repeated failure sequences using **sequence fingerprinting**, collapsing identical chains into a single bundle with a replay count (e.g., “pattern repeated 47 times in 5 min”).

### Step 4: Graph‑based impact analysis – infer causal direction
- Identify the **sink node** (service with highest anomaly severity) in each bundle.
- Perform an upstream BFS (bounded depth) to locate anomalous neighbours.
- Score each candidate causal path:  
  `S_path = (1/m) × Σ S_anomaly(Ui) × w_edge(Ui→Ui+1) × exp(-α × Δt)`  
  where m = path length, S_anomaly = severity, w_edge = dependency strength, Δt = time difference to sink.
- The highest‑scoring path is taken as the most likely fault propagation chain.

### Step 5: Hypothesis generation and narrative
- Combine the temporal cohesion score and the path score into an overall confidence metric for each bundle.
- Produce a ranked list of hypotheses, each accompanied by a concise narrative (e.g., “Database X started returning timeout errors at 15:24, causing Service B latency spikes, which propagated to Service C and resulted in 500 responses to users”).

## Modularity and extensibility
- Anomaly detectors are interchangeable; statistical models can be replaced with machine‑learning models without altering the pipeline.
- New signal types (e.g., security alerts) can be added by emitting events that conform to the shared schema.
- The correlation engine remains agnostic to detector internals, focusing solely on normalized events.

## Key takeaways
- Automating hypothesis generation removes the most cognitively expensive step of RCA, allowing responders to move directly to validation and remediation.
- Correlating metrics, logs, and traces on a unified timeline and through the actual service graph yields high‑confidence fault hypotheses at scale.
- A modular, plug‑in architecture enables continuous improvement and adaptation to evolving telemetry sources without rebuilding the entire system.
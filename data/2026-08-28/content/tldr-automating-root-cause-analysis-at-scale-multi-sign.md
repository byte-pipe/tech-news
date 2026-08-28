---
title: 'Automating root cause analysis at scale: Multi-signal correlation for cloud native incident response | CNCF'
url: https://www.cncf.io/blog/2026/08/24/automating-root-cause-analysis-at-scale-multi-signal-correlation-for-cloud-native-incident-response/
site_name: tldr
content_file: tldr-automating-root-cause-analysis-at-scale-multi-sign
fetched_at: '2026-08-28T12:25:29.056673'
original_url: https://www.cncf.io/blog/2026/08/24/automating-root-cause-analysis-at-scale-multi-signal-correlation-for-cloud-native-incident-response/
date: '2026-08-28'
published_date: '2026-08-24T11:00:00+00:00'
description: At Atlassian’s scale, hundreds of interconnected microservices distributed across multiple regions mean a production incident generates an overwhelming volume…
tags:
- tldr
---

Posted on August 24, 2026by Santosh Balaranganathan, Michael Yoo, James Moessis, James Kieltyka, Jason Lee, Lavender Neesham - Atlassian

CNCF projects highlighted in this post

## The problem: Humans shouldn’t be correlation engines

At Atlassian’s scale, hundreds of interconnected microservices distributed across multiple regions mean a production incident generates an overwhelming volume of telemetry. The problem is that finding the causal factor in the vast amount of telemetry still relies heavily on human expertise, intuition, and manual cross-referencing.

A typical root cause analysis workflow today looks something like this: an on-call engineer gets paged, opens a metrics dashboard, spots an anomaly in error rate or latency, pivots to a logging tool to search for exceptions within that time window, then opens a tracing UI to inspect individual request paths. They visually correlate patterns across these three separate views, form a mental hypothesis about where the fault lies, and then work backward through the service dependency graph to validate it.

This is a serial, cognitively expensive process. It depends on the responder already knowing which dashboards to check, which log queries to run, and which services are upstream of the one that’s failing. Senior engineers with years of domain knowledge can do this in minutes. Everyone else takes significantly longer, and during a user-impacting incident, every minute matters.

We asked a simple question:what if we automated the hypothesis generation step entirely, so responders could skip straight to validation and resolution?

## Our approach: Treat RCA as a multi-signal correlation problem

The insight behind our automated RCA system is that root cause analysis is fundamentally a correlation problem across three dimensions:

1. Signal type(metrics, logs, traces)
2. Time(anomalies that co-occur are likely related)
3. Topology(faults propagate along service dependency edges)

If we can detect anomalies independently in each signal, align them on a shared timeline, and then trace them through the known service dependency graph, we can generate ranked hypotheses about where a fault originated and how it propagated to produce the user-visible symptoms.

The system is explicitly designed to be modular. Each anomaly detection method is a pluggable component, and the correlation engine operates on normalised anomaly events regardless of which detector produced them. This means we can iteratively improve individual components, swap a statistical model for an ML model, add a new signal type, without rebuilding the pipeline.

## Architecture: From raw telemetry to ranked hypotheses

### Step 1: Scope the search using service topology

When an incident is detected, the first thing we do is narrow the blast radius. Rather than analyzing every service in the platform, we query our service dependency graph to identify the set of services in the call path of the degraded user experience. This gives us a focused subgraph, typically tens of services rather than hundreds, where the fault is most likely to exist.

We use OpenTelemetry-derived service maps for this. The dependency graph is built from span-level parent-child relationships observed in production traffic, giving us a real-time picture of how services actually communicate rather than how they’re supposed to communicate according to documentation.

### Step 2: Detect anomalies independently per signal

With the relevant services identified, we run specialised anomaly detection modules for each telemetry signal:

Metrics (RED signals):For each service endpoint, we monitor rate, error rate, and duration (RED) using a combination of statistical methods. Median absolute deviation handles spike detection, while percentile bands catch sustained deviations. When a metric crosses its dynamic threshold, we emit a normalised anomaly event with a severity score, the observed value, and the baseline it deviated from.

Distributed traces:We analyse traces flowing through the affected services for structural anomalies, including unexpected exceptions, novel error propagation patterns, and latency spikes at specific spans. The trace-based detector uses both statistical methods (latency percentile violations) and pattern analysis to identify exception types that correlate with the incident window. Each anomalous trace produces an event tied to the service and timestamp where the anomaly was observed.

Logs:We apply clustering techniques to log streams from affected services, surfacing new or rare error clusters that appeared during the incident window. The key challenge here is log volume. At scale, you cannot naively scan every line. We use embedding-based clustering to group semantically similar log entries and flag clusters that are statistically novel relative to the service’s normal error distribution.

Every detector produces events conforming to a common schema:

{

 "timestamp": "2025-07-24T15:24:00Z",

 "service": "payment-service",

 "signal_type": "metric",

 "severity_score": 0.85,

 "details": { ... }

}

This normalisation is critical. It allows the downstream correlation engine to reason across signal types without caring which detector produced the event.

### Step 3: Temporal correlation: find anomalies that co-occur

The correlation engine’s first job is to identify clusters of anomalies that happened close together in time. The intuition: if a database starts throwing errors at 15:24, the service that calls it starts timing out at 15:24:30, and the frontend that calls that service starts returning 500s at 15:25, these are almost certainly related.

We use a sliding window approach (configurable, typically plus or minus 5 minutes) to group co-occurring anomalies intocorrelation bundles. Each bundle receives a temporal cohesion score:

S_temporal = (1 / N(N-1)) × Σ exp(-|ti - tj| / τ)

Where N is the number of events, ti and tj are event timestamps, and τ is a tunable decay constant. Tightly clustered anomalies score higher than dispersed ones.

A critical refinement we discovered in practice: the same causal chain often replays multiple times during an incident (the same upstream timeout propagates the same downstream failure every few seconds). Without deduplication, this produces redundant bundles that obscure the signal. We solve this withsequence fingerprinting, computing a fingerprint from the ordered list of services in each anomaly path and collapsing repeated sequences into a single bundle with a replay count. This lets us say “this failure pattern repeated 47 times in 5 minutes” rather than generating 47 identical hypotheses.

### Step 4: Graph-based impact analysis: find the causal direction

Temporal correlation tells us which anomalies happened together. Graph-based analysis tells us which service is thecauseand which areeffects.

For each correlation bundle, we identify thesink node, the service with the highest anomaly severity, which typically represents the most impacted point visible to users. We then traverse upstream in the dependency graph (BFS, bounded to a configurable depth) looking for anomalous neighbours.

The key insight: if Service A calls Service B, and both are anomalous in the same time window, but Service B’s anomaly preceded Service A’s, then Service B is more likely to be the fault origin and Service A is experiencing a downstream effect.

We score each candidate causal path:

S_path = (1/m) × Σ S_anomaly(Ui) × w_edge(Ui → Ui+1) × exp(-α × Δt)

Where m is the path length, S_anomaly is the anomaly severity at each node, w_edge captures the strength of the dependency relationship, and the exponential decay penalises anomalies that are temporally distant from the sink. The path with the highest score represents our best guess at the fault propagation chain.

### Step 5: Hypothesis generation and narrative

The final step combines the temporal cohesion score and path score into an overall confidence score for each correlation bundle:

S_overall = w1 × S_temporal + w2 × S_path

We rank bundles by this score and emit the top N asroot cause hypotheses. Each hypothesis includes:

* The suspectedroot cause service(the upstream origin of the fault)
* Thepropagation pathshowing how the fault spread to produce user-visible symptoms
* Evidenceat each node (which metrics breached thresholds, which exceptions appeared, which trace IDs exhibit the failure)
* Aconfidence scoreand breakdown of how it was calculated
* Ahuman-readable narrativeexplaining the hypothesis in plain language

This last point matters more than it might seem. A ranked list of services with scores is useful for machines, but responders need to quickly assess whether a hypothesis is worth pursuing. Our narrative templates produce explanations like:

“Between 15:24 and 15:28, the payment-service endpoint /charge exhibited a 4x increase in error rate (baseline: 0.2%, observed: 0.8%). This preceded a latency spike in checkout-service /complete (p99: 340ms to 2100ms), which propagated to the frontend as HTTP 500 errors. The fault likely originated in payment-service based on temporal precedence and graph position. Confidence: 0.87.”

## Fitting into a broader reliability platform

Automated RCA does not exist in isolation. At Atlassian, we are building a cohesive incident response platform that integrates automated user-impact detection, faulty service identification, causal diagnosis, and an AI-powered incident copilot into a single responder experience.

Our RCA engine serves as the diagnostic brain of this platform. When a user-impacting incident is detected, whether automatically via real-time user experience signals or manually by support teams observing ticket surges, the RCA engine is triggered. It publishes its hypotheses into a shared incident context that other components consume:

* Faulty service identificationuses early-stage RCA results to page the right team, reducing time to engage.
* An incident copilotuses the hypotheses and their evidence to explain what is happening to responders and recommend mitigation actions (rollbacks, feature flag disablement) grounded in the actual diagnosis rather than generic runbooks.
* A feedback loopcaptures whether responders accepted, rejected, or refined each hypothesis, allowing us to tune weights and improve accuracy over time.

The shared incident context is the critical integration point. By anchoring all signals, hypotheses, and actions to a single per-incident context, regardless of which system produced them, we ensure responders see one consistent view rather than reconciling outputs from multiple disconnected tools.

## Lessons learned and design trade-offs

Start with the simplest anomaly detection that is useful, not the most sophisticated.Our initial impulse was to build complex ML models for every signal. In practice, statistical methods (MAD, percentile bands) work surprisingly well for metrics anomaly detection and are far easier to debug when they produce false positives. We reserve ML approaches for signals where statistical methods genuinely struggle, such as log clustering and trace structural analysis.

Modularity pays compound interest.Because each anomaly detector is a pluggable module behind a normalised interface, we could ship a useful system with just metrics-based detection, then incrementally add trace and log detectors without touching the correlation engine. Each new module immediately improved hypothesis quality because the correlation engine had more evidence to work with.

Deduplication is not optional at scale.Without sequence fingerprinting and replay collapsing, a single fault pattern that replays 100 times during an incident produces 100 bundles. This overwhelms both the scoring pipeline and the human reading the results.

The dependency graph is your most powerful prior.Temporal correlation alone produces too many hypotheses. Many services are anomalous during an incident because they are affected, not because they are faulty. The graph provides causal direction and dramatically reduces the hypothesis space.

Narratives build trust.Engineers will not act on a confidence score alone. They need to see the evidence and the reasoning that connects it. Our templated narratives with embedded telemetry references (specific trace IDs, specific metric values) let responders validate a hypothesis in seconds rather than re-deriving it from scratch.

## What’s next

We are actively exploring how LLM-based orchestration can make this system iterative rather than one-shot. Today, the RCA engine runs once per incident trigger. The next step is an agent that can request additional telemetry, refine its hypotheses based on what it finds, and adapt its investigation strategy based on what signals are available, much like an experienced human responder would. The challenge is doing this safely: with appropriate rate limits, sandboxed execution, and clear provenance so responders always know what evidence supports each conclusion.

We are also expanding the signal types the system can reason about, including infrastructure metrics, deployment events, feature flag changes, and synthetic check results, to move from “which service is broken” toward “what change caused it to break.”

## Key takeaways

* Automated RCA is a correlation problem across three dimensions:signal type, time, and service topology. Solving it requires normalised anomaly events, temporal alignment, and graph-based causal inference.
* Modular, incrementally useful design beats big-bang delivery.Ship the simplest version that provides value, then layer in additional signal types and more sophisticated detection methods.
* OpenTelemetry provides the foundation.Standardised traces give you the dependency graph for free and provide the structural data needed for trace-based anomaly detection. Without consistent, correlated telemetry, multi-signal RCA is impossible.
* Invest in explainability from day one.Confidence scores are necessary but not sufficient. Human-readable narratives with evidence provenance are what build the trust needed for responders to actually act on automated diagnosis.
* Build feedback loops early.The system improves only if you capture whether hypotheses were correct. Simple thumbs-up/thumbs-down on each hypothesis is enough to start tuning weights and identifying systematic blind spots.
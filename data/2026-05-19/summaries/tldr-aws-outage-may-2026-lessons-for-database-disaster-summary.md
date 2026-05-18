---
title: AWS Outage May 2026: Lessons for Database Disaster Recovery
url: https://www.singlestore.com/blog/aws-outage-may-2026-cross-region-disaster-recovery/
date: 2026-05-19
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-05-19T06:02:22.119413
---

# AWS Outage May 2026: Lessons for Database Disaster Recovery

# AWS Outage May 2026: Lessons for Database Disaster Recovery

## Overview
- A thermal failure in an Amazon data‑centre hall (US‑EAST‑1, zone use1‑az4) on 7 May 2026 caused cooling loss, power loss, and hardware damage to EC2 instances and EBS volumes.  
- The outage lasted over 20 hours, affecting traders, bettors, and institutional users who saw error screens with no fail‑over button or secondary region to switch to.  
- SingleStore Smart DR offers cross‑region replication with up to 10‑minute RPO and no idle compute cost until a fail‑over is triggered.

## Timeline of the Event
- **17:25 PDT (7 May)** – Cooling capacity dropped in a single data‑centre hall, triggering power loss.  
- **23:50 UTC (7 May)** – Overheating confirmed; multiple cooling units failed.  
- **13:50 PT (8 May)** – Cooling stabilised; most damaged instances and volumes restored after ~20 hours.

## Companies Impacted
- **Coinbase**
  - Offline ~7 hours; trading, balance updates, and derivatives exchange unavailable.  
  - CEO Brian Armstrong called the outage “never acceptable”; primary exchange ran in a single zone for latency, backup systems failed.  
- **FanDuel**
  - Went down ~21:00 ET during a live NBA semifinal; users could not cash out bets.  
  - Acknowledged technical difficulties, confirmed AWS link restoration ~2 hours later.  
- **CME Group (CME Direct)**
  - Experienced login and latency issues, raising regulatory and operational risk concerns.  
- Additional downstream customers in US‑EAST‑1 using EC2/EBS in the affected zone likely experienced impairments, including some SingleStore Helios users.

## Financial & SLA Implications
- AWS standard EC2 SLA provides a credit of ~10 % of monthly compute spend for impacted instances.  
- No compensation for lost revenue, customer trust, or regulatory exposure.  
- Industry data (2024 ITIC survey) shows median downtime cost > $300 k per hour for midsize/large enterprises; finance sector losses can be several million per hour.

## High Availability vs. Disaster Recovery
- **High Availability (Multi‑AZ)**
  - Protects against failures in a single rack or zone.  
  - Did not help Coinbase because its latency‑sensitive matching engine was deliberately single‑zone.  
- **Disaster Recovery (Multi‑Region)**
  - Protects against region‑level events like the thermal failure.  
  - Requires explicit cross‑region replication and fail‑over mechanisms; otherwise, workloads remain vulnerable.

## Recommendations (SingleStore Smart DR)
- Enable cross‑region replication with a target RPO of up to 10 minutes.  
- No idle compute cost in the secondary region until a fail‑over is executed.  
- Treat disaster recovery as a separate, essential component of business continuity, not as an afterthought to high availability.

## Conclusion
- US‑EAST‑1 has a history of significant outages; physical failures cannot be mitigated by software alone.  
- Organizations running mission‑critical workloads in a single region should adopt a cross‑region disaster recovery posture now, before the next regional event occurs.
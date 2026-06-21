---
title: "Meet Alice. Alice is impatient. - Marc's Blog"
url: https://brooker.co.za/blog/2026/06/19/waiting.html
date: 2026-06-20
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-06-22T00:54:18.074869
---

# Meet Alice. Alice is impatient. - Marc's Blog

# Meet Alice. Alice is impatient.

## Main idea
- Users (Alice, Alex) perceive service latency and outage duration differently from the metrics engineers report.
- Engineers measure average request time or MTTR per event, while users experience a time‑weighted view that emphasizes longer events.

## Inspection paradox explanation
- The phenomenon is the inspection paradox: the observed average waiting time is  
  \(\mathbb{E}_a[X] = \frac{\mathbb{E}[X^2]}{\mathbb{E}[X]} = \mathbb{E}[X] + \frac{\mathrm{Var}(X)}{\mathbb{E}[X]}\).
- Because longer requests/outages occupy more of a user’s timeline, they have a heavier influence on the user’s perceived mean.

## Simulation illustration
- A simple tool lets you input median latency (or recovery time) and the 99th‑percentile value.
- The tool fits a log‑normal distribution and shows:
  - The mean value the service reports.
  - The mean value a customer actually experiences.
- Example: median = 30 min, p99 = 600 min → service MTTR ≈ 1 hour, customer‑perceived mean recovery ≈ 6 hours.

## Implications for engineering
- Tail latency and long recovery times dominate user experience even if they are rare.
- Timeout‑and‑retry can mask tail latency for requests but cannot hide long recovery periods.
- Trimmed statistics (e.g., trimmed means) discard critical information about the right tail.
- Understanding the inspection paradox helps prioritize reducing extreme latencies and outages.

## Note on the log‑normal model
- Log‑normal is used for convenience; it behaves well near zero and has a simple parameter shift property.
- It is not claimed to be the best model for latency or recovery time; a non‑parametric approach is generally preferable.
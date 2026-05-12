---
title: Application performance is a product requirement | Christian Rackerseder
url: https://www.echooff.dev/blog/application-performance-is-a-product-requirement
date: 2026-05-13
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-05-13T06:01:35.188136
---

# Application performance is a product requirement | Christian Rackerseder

# Application performance is a product requirement

## Introduction
- Developer experience (DX) is important, but it does not excuse slow software.
- Rendering, network, responsiveness, and bundle size remain critical.
- DX and application performance are complementary, not opposing, responsibilities.
- Application performance is ultimately a product decision and a concrete requirement.

## Blazing fast is not a requirement
- Every product has performance needs, but they differ by context (e.g., drawing tool vs. admin dashboard).
- “Make it fast” or “blazing fast” are slogans, not actionable requirements.
- Concrete performance requirements enable measurement, testing, and decision‑making, e.g.:
  - Loading large reports must not block basic input.
  - Filtering large tables must return feedback within a defined time budget.
  - Form saving must keep the UI responsive during validation and server calls.
  - Core workflows must remain usable on supported low‑end devices.
  - Background sync, import, or export must not block navigation.

## Product decides what “fast enough” means
- Engineers can explain consequences, costs, and risks, but they should not define performance requirements alone.
- If a product must handle large data sets, long sessions, slow devices, or unreliable networks, those needs belong in the product specification.
- Bad performance is a product problem as well as a technical one; product owners must set the performance targets, and engineering makes the trade‑offs visible.

## Optimizing early vs. performance‑aware design
- Premature optimization = optimizing code before knowing if it matters.
- Performance‑aware design = avoiding architectural choices that later make required performance impossible.
- YAGNI (You‑Aint‑Gonna‑Need‑It) still applies: don’t build for imagined needs, but don’t ignore known requirements.
- Good DX enables safe refactoring, isolation of slow paths, and reliable measurement of real user journeys.

## Performance without changeability gets expensive
- Highly optimized but rigid code can become a bottleneck when product requirements evolve.
- Performance is valuable only when it supports the product without sacrificing future adaptability.
- The key question: *Which product behaviors must be fast, and how can the system be designed to achieve that while remaining changeable?*

## Performance budgets belong to product and engineering
- A performance budget is an agreement on the importance of a user journey and the resources allocated to it.
- Typical process:
  1. Product defines the critical user journey.
  2. Engineering defines measurable metrics.
  3. Both agree on acceptable thresholds.
  4. Engineering explains trade‑offs.
  5. Product decides if the cost is justified.
- Performance work competes with features, reliability, accessibility, security, refactoring, and edge‑case support; balanced decisions are required.

## Engineers should not hide the trade‑off
- Engineers must surface scalability or responsiveness concerns early, framed as trade‑offs, not absolute judgments.
- Example statement: “This approach works for small data sets but will block the main thread for large ones; if large data sets are required, we should address it now, otherwise we can accept the limitation and make it visible.”
- Turning performance into a decision rather than an opinion improves collaboration.

## Application performance is part of product quality
- Performance is a dimension of overall product quality, alongside functionality, usability, and reliability.
- Investing in both developer experience and clear performance requirements leads to software that is fast, maintainable, and aligned with business goals.
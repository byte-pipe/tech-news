---
title: A cache hit is not proof that you skipped the work · Siddhant Khare
url: https://siddhantkhare.com/writing/kv-cache-truth-auditor
date: 2026-09-14
site: tldr
model: llama3.2:1b
summarized_at: 2026-09-14T16:58:33.320773
---

# A cache hit is not proof that you skipped the work · Siddhant Khare

**Reuse Control in LLM TraceFX**

LLM TraceFX is a cloud-based language model testing platform. The platform utilizes a cache control mechanism to manage the reusability of responses to requests. This allows for efficient retrieval of previously accessed data, reducing database queries and increasing the overall performance of the system.

**Key Features of Rerun Cache Control**

* **Exact token identity reuse**: The platform maintains a cache of exact token identities from previous requests. Reusing the same prefix for subsequent requests is feasible, as long as the input remains invariant in terms of token identity.
* **Interior mutation**: Internal updates to the input are ignored, and the prefix remains unchanged during the runtime.
* **No-cache output**: The cache does not store cached outputs. Output is calculated on the fly by the engine, ensuring that no cached version is used.
* **Suffix change**: A changed suffix can be tolerated, as long as an eight-token prefix remains.
* **Cache event resolution**: The runtime attempts to report the existence of a cache hit without inquiring about the cache contents. This resolves the need for explicit cache checks.

**Evidence Validation**

A deterministic synthetic token-level control is implemented, ensuring the authenticity and integrity of the control. This validates various aspects of the platform, including:

* Auditor and oracle compliance
* Evaluator correctness
* Hash evaluation
* Standalone verifier validation

**Engagement Requirements**

* The demo demonstrates the accurate implementation of the reuse control mechanism.
* The cache event can be reported without violating conditions for accuracy or efficiency.

**Assumptions and Limitations**

* The demo assumes a fixed request sequence, which may not represent real-world scenarios.
* The evaluation checks do not exhaustively verify the platform's ability to handle all possible scenarios.
* Some data is assumed to be uniformly distributed and random.

The provided information provides insights into the cache control mechanism used by LLM TraceFX. This mechanism enables efficient reusability of responses while maintaining test rigor and integrity.
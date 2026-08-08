---
title: Reading
url: https://carlkolon.com/reading/
date: 2026-08-01
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-08-09T00:36:56.838097
---

# Reading

# Carl’s Required Reading – Summary

## Coding practices
- **The Grug Brained Developer** – Emphasizes that complexity is harmful; a must‑read for developers of any level.  
- **The Wrong Abstraction** – Warns against reflexively removing duplication; sometimes keeping separate implementations is better.  
- **Complexity Budget** – Describes how unchecked complexity can cause sudden stalls in progress and suggests ways to monitor it.  
- **Locality of Behavior** – Argues for making a unit’s behavior obvious in its own code rather than spreading concerns across many helpers.  
- **YAGNI** – Stresses that building speculative, future‑oriented features is usually a mistake.  
- **Parse, Don’t Validate** – Recommends encoding data invariants in types so violations surface as compile‑time errors instead of runtime checks.

## Platform
- **Steve Yegge’s Google Platforms Rant** – Covers accessibility, service exposure, and organizational setup; encourages critical thinking about programmatic feature sharing.

## Frontend
- **HATEOAS** – Suggests storing state and allowed actions in the served HTML, aligning with true REST principles.  
- **Components and Hooks Must Be Pure** – Advocates a declarative, functional style in React; avoid imperative state manipulation.  
- **Understanding useMemo and useCallback** – Explains the limited scenarios where these React hooks are actually beneficial.  
- **Hypermedia Systems – Components of a Hypermedia System** – Provides a deep look at HTML’s underlying model to use the browser more effectively.

## Databases
- **The Vietnam of Computer Science** – A strong critique of ORMs, highlighting performance and clarity problems.  
- **Wikipedia – The Object‑Relational Impedance Mismatch** – Concise technical overview of why ORMs can be problematic.  
- **Introduction to PostGIS – Geography** – Introduces geospatial types and the `geography` data type for map‑based visualizations.  
- **Postgres Docs Chapter 14 – Performance Tips** – Essential guide to using `EXPLAIN` and `EXPLAIN ANALYZE` for query tuning.  
- **Paging Through Results** – Discusses alternatives to `LIMIT`/`OFFSET` for efficient pagination of large datasets.

## Asynchronous programming
- **A Conceptual Overview of asyncio** – Clarifies asyncio’s inner workings and common pitfalls such as blocking calls inside async functions.  
- **What Color Is Your Function?** – Shows fundamental limitations in async systems, illustrating that some issues stem from language design rather than developer skill.

## Encoding
- **The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets** – Essential reading to avoid costly mistakes when handling international text data.

## Books
- **The Design of Everyday Things** – Argues that design is about understanding user needs and delivering functional, intuitive products, not merely visual aesthetics.
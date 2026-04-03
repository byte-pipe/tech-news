---
title: Architecture Decision Record
url: https://martinfowler.com/bliki/ArchitectureDecisionRecord.html
date: 2026-03-26
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-03-26T01:03:13.798718
---

# Architecture Decision Record

# Architecture Decision Record Summary

## Overview
- An ADR is a short document that records a single architectural decision for a product or ecosystem.  
- It includes the decision, its context, and significant ramifications.  
- Once a decision changes, a new ADR supersedes the old one instead of editing it.

## Purpose
- Serves as a historical record so future readers can understand why a system was built a certain way.  
- The act of writing clarifies thinking, surfaces differing viewpoints, and encourages discussion and resolution.

## Writing Style
- Follow an “inverted pyramid”: place the most important information at the beginning, with details later.  
- Keep the document brief, typically a single page; link to supporting material when needed.  
- Use a lightweight markup language (e.g., Markdown) for easy reading and diffing.

## Storage
- Store ADRs in the same source repository as the code they apply to, commonly in a `doc/adr` directory.  
- This makes them readily accessible to developers and allows publishing via build tasks.  
- For decisions spanning multiple repositories or for non‑developer audiences, alternative storage may be needed.

## Naming & Numbering
- Each ADR resides in its own file.  
- File names use a monotonic sequence number and a descriptive title (e.g., `0001-HTMX-for-active-web-pages.md`).  
- This ordering aids readability in directory listings.

## Status Lifecycle
- **proposed** – under discussion.  
- **accepted** – approved and active.  
- **superseded** – replaced by a later ADR, with a link to the new record.  
- Accepted ADRs are never reopened or edited; they are only superseded.

## Content Elements
- **Decision** – the concrete choice made.  
- **Rationale** – problem summary, forces, and trade‑offs considered.  
- **Alternatives** – list of serious options with pros and cons.  
- **Consequences** – explicit outcomes of the decision.  
- **Confidence level** – degree of certainty and triggers for reevaluation.  
- In the Advice Process, include a brief summary of gathered advice; keep full advice records separate.

## Brevity Emphasis
- Aim for a single page; use links for extensive supporting information.

## Broader Applicability
- The ADR concept, while rooted in software architecture, can be applied to other decision‑logging contexts to create valuable historical records.

## Further Reading
- Michael Nygard introduced the term “Architecture Decision Record” in 2011, inspired by Philippe Kruchten’s decision logs and software pattern writing style.  
- Examples of ADR formats are available from Harmel‑Law, Rowse, and Shepherd.  
- `adr-tools` is a CLI utility for managing ADRs and includes sample records.

## Acknowledgements
- Contributions from Andrew Harmel‑Law, Brandon Cook, David Lucas, Francisco Dias, Giuseppe Matheus Pereira, John King, Kief Morris, Michael Joyce, Neil Price, Shane Gibson, Steven Peh, and Vijay Raghavan Aravamudhan.  
- Michael Nygard provided background on the origins of ADRs.
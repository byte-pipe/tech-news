---
title: XML is a Cheap DSL
url: https://unplannedobsolescence.com/blog/xml-cheap-dsl/
date: 2026-03-14
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-03-15T06:02:02.501129
---

# XML is a Cheap DSL

# XML is a Cheap DSL

## Overview
- The author released the open‑source Tax Withholding Estimator (TWE) for the IRS, allowing public contributions.  
- The post focuses on lessons learned about XML, arguing that despite its reputation for being clunky, XML remains a viable choice for cross‑platform declarative specifications.

## The Fact Graph
- TWE is generated from two XML configuration files; the first is the **Fact Dictionary**, which encodes the U.S. tax code.  
- The Fact Graph engine consumes these facts to compute tax obligations and withholdings.  
- Facts are expressed as XML elements that declare:
  - **Path** – the identifier of the fact (e.g., `/totalOwed`).  
  - **Derived** or **Writable** – whether the value is computed or supplied by the user.  
  - **Operations** – nested elements such as `<Subtract>`, `<Add>`, `<GreaterOf>`, and dependencies on other facts via `<Dependency path="…"/>`.  
- Example:  
  - `/totalOwed` = `/totalTax` – `/totalPayments`.  
  - `/totalRefundableCredits` aggregates several credit facts using `<Add>`.  
  - Non‑refundable credits are handled with `<GreaterOf>` to enforce a floor of zero.  
- Input facts use `<Writable>` with type tags like `<Dollar/>` or `<Boolean/>`.

## Why a Declarative Specification Is Needed
- Tax calculations involve many inter‑dependent values; a declarative format makes the relationships explicit and traceable.  
- Imperative code (e.g., JavaScript) can express the same mathematics more concisely but hides the dependency graph and execution order.  
- The author demonstrates a JavaScript version that computes `totalOwed`, `totalTax`, and `totalPayments` step‑by‑step, then points out drawbacks:
  - Execution order must be managed manually.  
  - Intermediate results are not part of a persistent specification.  
  - Complex nesting of calculations can become error‑prone when expressed imperatively.

## Comparison with Imperative Code
- **Conciseness**: JavaScript is shorter and looks like algebra.  
- **Clarity**: XML is verbose but each operation is labeled (e.g., `<Minuend>`, `<Subtrahend>`), making the intent clear.  
- **Maintainability**: Declarative XML preserves the full dependency graph, facilitating updates and public contributions.  
- **Extensibility**: Adding new facts or changing logic only requires editing the XML, without altering execution flow code.

## Conclusions
- XML, while verbose, provides a transparent, platform‑agnostic way to describe complex tax logic.  
- Its declarative nature suits domains where the specification itself must be auditable, extensible, and open to community input.  
- The TWE project demonstrates that XML can serve as a “leading option” for cross‑platform declarative specifications, even in modern software development.
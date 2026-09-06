---
title: Building and Using Named Queries
url: https://ontologist.substack.com/p/building-and-using-named-queries
date: 2026-09-07
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-09-07T08:08:30.150442
---

# Building and Using Named Queries

# Building and Using Named Queries

## Overview
- The article argues that registering SPARQL queries as RDF resources transforms SPARQL from a specialist‑only tool into a stable, ACL‑protected API.
- It presents the shortcomings of naked SPARQL queries and demonstrates how named queries address those issues.

## Problems with SPARQL
- No built‑in mechanism to control which query runs next, hindering optimisation.
- Absence of ACLs means anyone with graph access can view all data, which is unsafe for most real‑world graphs.
- Parameterisation is usually ad‑hoc, relying on `VALUES` or external code that maps dictionaries to SPARQL variables.
- Simple queries can overload a system (e.g., `SELECT * WHERE {?g {?s ?p ?o}}`) and updates can cause severe damage.
- Prompt injection attacks are possible against SPARQL endpoints.
- Users need detailed schema knowledge, limiting broader adoption.
- The majority of queries fall into a small set of patterns (retrieve, create, update, deprecate, etc.); exposing them as a standard API reduces complexity.
- Separating queries from the dataset causes loss of critical graph information when only the dataset is exported.
- SPARQL’s specialist nature creates a high barrier to entry.

## Power of Naming Queries
- Storing queries as RDF literals with accompanying metadata lets agents discover and select appropriate queries programmatically.
- Metadata can include SHACL shapes to describe parameters and expected results.
- Enables automatic format conversion (JSON‑LD, Turtle, TriG) or LLM prompting based on query metadata.
- Adding or deprecating a query requires only inserting or removing a few triples—no recompilation of the application.
- Named queries act as a mediation layer, preventing direct read/write access to the graph and enforcing ACLs.
- Identity and personalisation data can be passed to queries, allowing output to be filtered according to user permissions.
- Every query execution can be logged, providing an audit trail.

## Structure of a Named Query (example)
- Defined as an RDF resource of type `hb:NamedQuery`.
- Contains identifiers, labels, descriptions, query type, and the SPARQL text with placeholder syntax (`{{parameter}}`).
- Lists parameters with names, datatypes, descriptions, requirement flags, defaults, and SHACL constraints.
- Placeholders are substituted with fully‑formed SPARQL terms before parsing, allowing flexible placement (e.g., inside `FILTER` clauses).

## Key Takeaways
- Naming queries within the graph couples them tightly to the dataset’s ontologies and namespaces.
- Metadata‑driven named queries provide discoverability, security, versioning, and auditability.
- This approach reduces the need for users to understand SPARQL syntax or the underlying schema.
- By mediating all access through named queries and updates, graphs become more secure and easier to manage as APIs.
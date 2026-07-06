---
title: 'Bridging the Gap: Blending Structured Data Auditing with Unstructured Policy Intelligence | by ML | Jun, 2026 | GoPenAI'
url: https://blog.gopenai.com/bridging-the-gap-blending-structured-data-auditing-with-unstructured-policy-intelligence-17710e04c8de
site_name: tldr
content_file: tldr-bridging-the-gap-blending-structured-data-auditing
fetched_at: '2026-07-06T12:20:31.121284'
original_url: https://blog.gopenai.com/bridging-the-gap-blending-structured-data-auditing-with-unstructured-policy-intelligence-17710e04c8de
author: ML
date: '2026-07-06'
published_date: '2026-07-03T15:54:51.150Z'
description: 'Bridging the Gap: Blending Structured Data Auditing with Unstructured Policy Intelligence How an Agentic Harness Loop Transforms Corporate Loan Analysis from Static QA into Autonomous Risk Research …'
tags:
- tldr
---

# Bridging the Gap: Blending Structured Data Auditing with Unstructured Policy Intelligence

ML
5 min read
·
6 days ago

--

Listen

Share

## How an Agentic Harness Loop Transforms Corporate Loan Analysis from Static QA into Autonomous Risk Research Agent

In modern corporate “Data” remains highly siloed which prevents corporate from using unstructured dcouments (e.g. regulatory frameworks, compliance rules, internal operating guidelines) with structured data stored in transaction databases and data warehouses. Traditional search systems, such as basic keyword search or standard Retrieval-Augmented Generation (RAG) Q&A chatbots, fail to bridge this gap.

## Problem Statement

Large organizations routinely face complex procedure and policy documents, such as compliance guidelines or financial standards. The information required to conduct these audits is split across two fundamentally different domains:

-Unstructured Qualitative Intelligence: Policy guidelines, regulatory mandates, and internal manuals. These reside as text inside PDFs or corporate wiki pages.

-Structured Quantitative Records: Transaction logs, customer profiles, loan data, and risk metrics. These live in relational tables, data lakes, or databases.

When auditing compliance, human auditors must manually read a policy (e.g.,Lenders must identify public derogatory records and delinquent credit events), translate that rule into database queries, analyze the results, and compile a report. Traditional AI assistants cannot automate this because:

1.Document Intelligence lacks database awareness: General Knowledge Base does not know the schema of the database or how business terminology maps to cryptic column names (e.g., matching “delinquent credit event” to a column named `delinq.2yrs`). Therefore, standard Text2SQL pipelines cannot generate the correct SQL.

2.Standard Text2SQL Lacks agentic looping: Research and audit analysis require action planning first, then querying the document base and transactional database, then analyzing the intersection, and finally critiquing the draft.

## Solution:

The solution combines the LLM-Wiki with Text2SQL to build a unified agentic workflow that acts as anAutonomous Analytic Agent. Instead of answering simple questions, the user provides a high-level objective, such as:

Identify if there are any high risk loan records which violate against the key risk indicators in documentation guidelines.

The agent coordinates multiple Specialized Agentic workflow inside a self-correcting loop. It automatically extracts relevant rules from unstructured documents using LLM-Wiki, and then maps them to database schemas, generates executable SQL queries, performs analysis and evaluations. The system continues to replan and query until it achieves a high-confidence evaluation.

In my demo use case, the agentic system can identify high risk loan records which violate against the key risk indicators in documentation guidelines.

Press enter or click to view image in full size

A. The Ingestion Layer

Before running audits, the system parses the domain’s structural and semantic foundations:

1.Structured Semantic Mapping: The pipeline recursively parses OWL Turtle (.ttl) files (e.g., in my demo use case, it is Financial Industry Business Ontology — FIBO) using RDFLib. It maps these OWL classes and attributes to dataset tables/columns and then create a mapping that defines how business concepts relate to physical columns.

2.Unstructured Document Ingestion: The pipeline converts regulatory PDFs into Markdown and segments the text. It classifies segments into ontology concept types and reconciles candidates to deduplicate concepts.

B. The Semantic Translation Layer: Ontologies & YAML Mapping

## GetML’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe
Subscribe

Remember me for faster sign in

To make database tables queryable by LLMs without guessing, we use:

1. Ontology (`.ttl` files): Defines domain-specific business terms (e.g.,Loan,BorrowerDebtToIncome,DerogatoryPublicRecord).
2. Semantic Mapping (mapping.yaml): Maps ontology attributes to database columns (e.g., matching the conceptBorrowerPublicRecordCounttopub.rec). It includes SQL formulas, explanations, and flags highlighting missing information. The LLM Planner and SQL Generator read this file to translate qualitative guidance into exact SQL syntax.

C. The Agentic Loop Layer

The agentic workflow operates as an iterative loop designed to guarantee analytical rigor and correctness:

1.Planning: A Planning Agent parses the high-level user goal alongside the structured semantic map. It outputs a structured `ActionPlan` containing a sequential plan of target queries.

2.Execution: The loop runner triggers specialized tools:

doc_context_retrieval: Searches the ingested guidelines in LLM-Wiki using self-contained BM25 text ranking and returns merged text segments.

tabular_data_retrieval: Translates business goals into SQL queries using the semantic map. If the SQL fails due to a binder or syntax error, the execution agent intercepts the exception and prompts the model to auto-correct the query, returning the repaired result.

3.Analysis: The Analyst Agent combines the qualitative guidelines with the quantitative query results to draft a detailed analysis report.

4.Evaluation: The Evaluator Agent scores the draft report against the original objective (0 to 100) and lists remaining gaps.

5.Loop Routing: If the evaluator’s confidence is ≥ 80, the loop terminates. If not, the feedback is routed back to the Planner, which compiles a revised, more targeted action plan for the next iteration. If the confidence score does not increase or reach the max iteration limit, it will also stop.

6.Report Generation: The final report and the execution step trace are written to report.md.

## Case Study: Auditing High-Risk Lending Records

The system was evaluated against a Public (Kaggle) LendingClub dataset and public guidelines on best practice. The user objective was to identify high-risk loans violating guidelines in the database. Here is a partial example in the demo. Below quotes the summary of thereport.mdgenerated by the agentic workflow.

## Analysis of Top 10% Highest-Risk Loans
### Current Evidence Summary
The context provides several data points, but there are **two different metrics** being referenced:
**From the detailed context (primary evidence):**
- **High-Interest Filter** (rate >= 18.84% / 0.1884): 103 total loans
 - Avg FICO: 678.84
 - Avg Rate: 19.79%
 - Avg DTI: 12.56%
 - 63 loans (61.2%) classified as high-risk
- **High-Risk Borrowers** (FICO ≤ 650, DTI ≥ 20%, Rate ≥ 16%): 31 records (0.32% of portfolio)
**From the "Summary" section (conflicting claim):**
- Claims "958 loans" in top 10% high-risk segment (10% of 9,578)
### Critical Assessment
The context's detailed analysis sections (High-Interest Loan Filter Impact, High-Risk Borrowers) are **more reliable** than the summary. The 103 loans with rates >= 18.84% represent the highest-risk segment based on the data architecture.
### Top 10% Highest-Risk Loans Identified
**Segment: Loans with Interest Rate >= 18.84% (0.1884)**
- **Count**: 103 loans (approximately 1.07% of portfolio, not 10%)
- **Key Risk Characteristics**:
 | Metric | Value | Risk Level |
 |--------|-------|------------|
 | Avg FICO | 678.84 | Fair (below optimal 700+) |
 | Avg Interest Rate | 19.79% | Very High |
 | Avg DTI | 12.56% | Moderate |
 | High-Risk Classification | 63 loans (61.2%) | Critical |
 | Highest Rate | 21.64% | Maximum |
**High-Risk Classification Criteria** (63 loans):
- Delinquency (2yrs) > 0 **OR**
- Inquiries (6mths) > 3 **OR**
- Public Records > 0
**Risk Correlations Observed**:
1. High interest rates strongly correlate with risky credit behavior (delinquencies, inquiries, public records)
2. Average FICO (678.84) places borrowers in 'fair' credit range
3. Moderate DTI (12.56%) suggests interest pricing driven by credit history rather than current debt burden
4. Concentrated high-risk pool with elevated default probability

## Key Strengths & Conclusion

OurAgentic Insight Engineshowcases the power of structured-unstructured hybrid analysis. The core strengths of this approach include:

* Semantic Data Alignment: The ontology andmapping.yamlallow the agent to understand what database columns mean, translating business terms to database queries.
* Iterative Self-Correction: The tabular retrieval tool automatically detects and repairs runtime SQL database syntax errors.
* Rigorous QA Guardrails: The independent evaluator agent prevents hallucinations by checking the analyst’s draft against the original goals. If confidence is low, it loops back to collect more information.

By wrapping structured databases and unstructured policy libraries inside an agentic harness, the system changes corporate compliance from manual, spreadsheet-based auditing into a reliable, autonomous research workflow.

## Resources:

* Github:https://github.com/iwasnothing/agentic-insight
* Demo Youtube:https://youtu.be/isdHF8SeS9s?si=_BucvKKz8-MWIjRC
---
title: Atlassian to train AI on user data unless law or cash say no • The Register
url: https://www.theregister.com/2026/04/18/atlassians_new_data_collection_policy/
date: 2026-04-23
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-04-23T09:45:12.697823
---

# Atlassian to train AI on user data unless law or cash say no • The Register

# Atlassian’s new data collection policy protects rich customers while AI eats the rest

## Overview
- From 17 August 2026 Atlassian will collect customer metadata and in‑app data to train its AI models.
- Collection is mandatory for lower‑tier plans unless prohibited by law; richer customers can opt out more easily.
- The policy applies to all 300 000 global cloud customers using Jira, Confluence and related products.

## Types of data collected
- **Metadata** (always collected for Free, Standard and Premium plans):
  - Readability scores and complexity ratings for Confluence pages.
  - Task classifications (e.g., “sales work item”).
  - Semantic similarity scores between pages.
  - Numeric fields such as story points, sprint end dates, and SLA values in Jira.
- **In‑app data** (content created by users):
  - Titles and body text of Confluence pages.
  - Titles, descriptions, comments, custom emoji names, status names and workflow names in Jira.
  - Collected by default on Free and Standard tiers (opt‑out possible); disabled by default on Premium and Enterprise tiers.

## Opt‑out and exemption rules
- Customers on Free, Standard or Premium plans cannot disable metadata contribution.
- In‑app data collection can be turned off by the customer on Free and Standard plans; it is off by default for Premium and Enterprise.
- Exemptions include:
  - Customers using customer‑managed or bring‑your‑own keys.
  - Atlassian Government Cloud and Isolated Cloud users.
  - Organizations with HIPAA requirements or certain government/financial services customers.

## Data handling and retention
- All collected data is de‑identified and aggregated at the customer level.
- Retention period is up to seven years to enable long‑term trend analysis.
- When a customer opts out or deletes apps, Atlassian will delete the corresponding in‑app data within 30 days and retrain affected models within 90 days.

## Intended AI benefits
- More relevant search results and query responses.
- Improved summarisation of content.
- Automated template recommendations for new documents.
- Enhanced workflow suggestions and multi‑step task guidance.

## Timeline
- Policy becomes enforceable on 17 August 2026.
- Existing contracts terminated before that date are not subject to the new settings.

## Related context
- Atlassian is moving to a cloud‑only strategy, causing integration challenges for some users.
- The company plans a 10 % staff reduction, citing AI‑driven efficiencies.
- Recent $1 billion acquisition aims to boost developer‑productivity measurement tools.
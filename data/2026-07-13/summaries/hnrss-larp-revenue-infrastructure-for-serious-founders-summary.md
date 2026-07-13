---
title: LARP — Revenue infrastructure for serious founders
url: https://www.larp.website/
date: 2026-07-12
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-07-13T12:27:51.170148
---

# LARP — Revenue infrastructure for serious founders

# LARP — Revenue infrastructure for serious founders

## Overview
- Platform used by 400+ finance and accounting teams (e.g., Verithor, Northbank, Cadenza Systems).  
- Claims 99.98 % settlement uptime, <400 ms median recognition latency, SOC 2 Type II audited annually.  
- Enables founders to generate recognized revenue without actual cash flow or customers.

## How it works
1. **Match with a peer** – any founder with a bank account and a product idea pairs with another founder.  
2. **Wire it in a circle** – each party “sends” money to the other; each leg is recorded as revenue for the receiver, resulting in zero net cash movement.  
3. **Recognize it forever** – the monthly amount is annualized, then the annualized figure is annualized again, inflating ARR (e.g., $10 k/mo → $120 k ARR).  

- The process relies on mutual journal entries; no real product or customers are required.  
- The “catch” is that there is none; the numbers are real, but their economic substance is a philosophical question.

## Real‑world examples
- The site displays live “ledger” nodes showing capital, chips, and cloud credits circulating among companies.  
- All displayed deals are publicly announced and legally defended (e.g., Anthropic CEO Dario Amodei).  
- Critics compare the pattern to 1990s dot‑com vendor financing, warning it can inflate perceived demand.  
- Bloomberg notes that circular deals differ legally from fraudulent “round‑trip” trades.

## User interface
- Users input a counter‑party startup and an amount, then execute a loop.  
- Dashboard shows ARR, net cash moved (always $0), journal entries, and loop statistics.  
- No cash ever leaves the user’s account; only revenue is recognized.

## Testimonials from finance teams
- “We recognized 340 % year‑over‑year revenue growth without any change to our cash position.” – D. Mercer, VP Finance, Cadenza Systems.  
- “Growth is no longer constrained by whether customers actually paid us.” – R. Oduya, Controller, Northbank.  
- “Every entry reconciles perfectly because each entry has a matching entry.” – S. Valko, CFO, Halyard & Vane.

## Technical integration
- Single API endpoint posts matched entries to both counterparties.  
- Example `curl` request creates a settlement, returns settlement ID, status, amount, recognized parties, net capital movement (0), and number of journal entries (4).  
- Both parties record the full amount as revenue; net cash movement remains zero.

## Legal stance
- LARP claims legality by facilitating bilateral service agreements that satisfy ASC 606 performance obligations.  
- Customers are responsible for compliance with accounting standards, disclosure rules, and securities law.  
- Platform does not provide legal, tax, or accounting advice.  
- Distinction from round‑tripping: LARP requires genuine deliverables; economic substance is left to the customer and auditors.

## Pricing (the joke)
- **Bootstrapper** – $0 forever; loops up to $10 k, one imaginary customer.  
- **Growth** – $0 forever; unlimited loops, auto‑generated board decks, “annualize the annualization.”  
- **Enterprise** – “Call us / we won’t pick up”; multi‑party loops, relaxed auditor, plausible deniability add‑on.  
- No actual payment is accepted; charging would create real revenue and contradict the platform’s principle.

## Optional tip
- Users may voluntarily tip the creator via a “gift” that is not a security, equity, or revenue share.  
- Contact email: [email protected] – for thanks, discussion, or sharing the actual company being built.  

## Bottom line
- LARP creates recognized ARR through circular, cash‑free transactions.  
- The ARR numbers are real on the ledger; the bank balance remains unchanged.  
- The service is positioned as a satire of revenue‑inflation practices, with a functional API and legal disclaimer.
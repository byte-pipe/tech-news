---
title: Building Better Agents through End-to-End Evals - DEV Community
url: https://dev.to/dailycontext/building-better-agents-through-end-to-end-evals-pgh
site_name: devto
content_file: devto-building-better-agents-through-end-to-end-evals-de
fetched_at: '2026-10-14T22:04:10.221623'
original_url: https://dev.to/dailycontext/building-better-agents-through-end-to-end-evals-pgh
author: Ryan Stevens
date: '2026-10-14'
description: Deeply understand the task at hand The biggest mistake teams make with agents is... Tagged with ai, agents, evals, aie.
tags: '#ai, #agents, #evals, #aie'
---

## Deeply understand the task at hand

The biggest mistake teams make with agents is automating a process they don’t understand. Before writing one line of code, you should be able to describe exactly how a human does the job.

To build Ramp Stack, we wanted to automate bookkeeping tasks. Before thinking about code, we thought about the jobs to be done. There are four primary categories of work: reconciliation, data entry, variance analysis, and schedules and accruals. Categories keep the eval balanced across the real job and later show you where the agent is weak.

Next, we break each task into its steps. Take an accounts payable reconciliation: an accountant pulls unpaid bills and the AP ledger, lines them up in a spreadsheet, and investigates anything that doesn’t match. If the bills total $3,500 and the ledger shows $3,000, the job is to find the missing $500 bill and record the correction. Each step is something the agent must do and something your eval must check.

## Data is the bottleneck

An end-to-end eval has the same shape at every stage: business data populates a database, the agent works with that state through tools, and you grade what it produces. Before launch, you have no data to work with, so you must simulate it.

Our answer was synthetic businesses, which we call worlds. One is a DTC home goods brand selling through Shopify, Amazon, and wholesale, with a full set of books, realistic transactions, and messy Excel files. The mess matters; too often, teams build data that is too clean. This means things look good offline, but do not survive once confronted with real users.

## Anatomy of an eval

Each eval case combines four parts:

* Task:the request, such as “Reconcile our AP payables and bills for Q4 2025.”
* World:the synthetic ERP and business data the agent can access.
* Trajectory:the steps the agent takes, like reading bills, matching payments, and investigating differences.
* Score:a rubric of accountant-written criteria, graded by an LLM judge on the final output.

The rubric is what makes the eval useful. Pass/fail hides partial progress; six criteria such as “Q4 AP balance correct” and “duplicates flagged” tell you the agent scored 4 of 6 and exactly which two it missed. Have domain experts write the criteria, since they know what a reviewer would actually reject.

## Using the eval to make changes

An eval earns its keep when it changes decisions. The first decision was model choice, but the biggest alpha is tuning your harness: optimizing skills, tools, and infrastructure to produce good results at low cost and latency. Several popular ideas didn’t hold up:

* Auto-tuned skills (GEPA-style autoresearch):training gains didn’t generalize. We have yet to see good evidence that automated prompt optimization works.
* High reasoning effort:same accuracy, higher cost.

What did work was treating the agent like an ML model and its context like features:

* Skill ablation:we benchmarked one skill at a time against a no-skill baseline, then trimmed eight skills to four, gaining 2.8 points of mean score across six worlds. Several skills actively hurt, and none was best everywhere.
* Skill compression:cutting our largest skill, a spreadsheet skill, by 61% left quality essentially unchanged and saved about $30k a month.

The pattern: measure every change against a fixed baseline, across many worlds, and keep only what moves the score.

## Test what others skip: memory

Memory is rarely evaluated because it requires time to pass. We built roll-forward worlds: the same business, advanced one month. The agent completes this month’s close, writes down what it learned, and is graded on next month’s tasks.

The rule we learned: remember how the business works, but use fresh numbers. Memory distilled from prior trajectories, with period-specific amounts removed, improved mean score by 5.7 points over skills alone. A memory that captured a reusable workflow took one task from 0% to 100%. One that smuggled in last month’s specific recipe dropped another from 75% to 25%.

## The takeaway

Agent development needs the same discipline as ML development. Understand the process, build a dataset hard enough to be meaningful and stable enough to compare runs, and let it, not intuition, decide what ships.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
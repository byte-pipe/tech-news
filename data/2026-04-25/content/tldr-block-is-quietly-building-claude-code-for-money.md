---
title: Block is quietly building Claude Code for money
url: https://www.popularfintech.com/p/block-is-quietly-building-claude-code-for-money
site_name: tldr
content_file: tldr-block-is-quietly-building-claude-code-for-money
fetched_at: '2026-04-25T11:37:30.690674'
original_url: https://www.popularfintech.com/p/block-is-quietly-building-claude-code-for-money
author: Jevgenijs Kazanins
date: '2026-04-25'
tags:
- tldr
---

* Home
* Posts
* Block is quietly building Claude Code for money

# Block is quietly building Claude Code for money

Jevgenijs Kazanins

Apr 19, 2026

Earlier this week, I listened to anepisodeof theOn the Blockpodcast, where the host, Matt Ross, Head of Investor Relations, sat down with Brad Axen, Principal Engineer for Data and Machine Learning at Block. Brad built Goose, Block's open-source agent framework. The conversation was about how Goose got built.

This episode made me realize that Block’s MoneyBot and ManagerBot aim to be the Claude Code of money.

If you've used Claude Code, you already know what's coming for consumers and small business owners. If not, continue reading.

## What Claude Code is

Claude Code is an agent. An agent is an LLM wired up with tools that runs inside a loop. The LLM writes text and decides what to do next. The harness is the program that runs the loop, reading the LLM's output, running whatever tool the LLM asked for, and feeding the result back. The tools are the actual capabilities: opening a file, running a command, querying a database, sending an email.

Here's how this works.

You send a prompt. The harness forwards it to the LLM along with a list of tools the LLM is allowed to use. Maybe one tool opens a file, another runs a command, and another queries a database. The LLM reads your request and the available tools, then writes back "use tool X with these inputs." The harness runs the tool, captures the result, and sends it back to the LLM. The LLM reads the result and writes the next step. Loop until the task is done.

Source:Building effective agents

Metaphorically, the LLM is the brain, the harness is the nervous system, and the tools are the hands and eyes. The harness and the tools enable LLMs to actually do stuff and be helpful.

❝

"I often say I work in applied AI, and what I mean by that is taking those foundational LLMs and connecting them into systems that let them actually take actions for people and be really useful day to day."

Brad Axen, Principal Engineer for Data and Machine Learning at Block

## Goose, Block's harness

In 2024, Brad and a small team built Goose, a harness similar to the one used in Claude Code, for Block’s engineers. It shipped first as a developer productivity tool, spread across the company, and was later open-sourced.

Engineers at Block use Goose for code migrations, increasing test coverage, running benchmarks, and automating the full build-test-debug loop. Non-engineering teams in design, product, support, and risk use it to triage tickets, generate documentation, write SQL queries for data pulls, and compile reports from Google Drive and Slack.

❝

"We were seeing it be very useful for people to help automate small parts of their job. That plus the growth curve, every six months we were getting a dramatic performance improvement, just made it so obvious to me that this was gonna change things."

Brad Axen, Principal Engineer for Data and Machine Learning at Block

What Block’s team realized is that it can build similar tools for consumers and small businesses. Thus, last fall, Block introduced MoneyBot in Cash App, followed this month by the launch of ManagerBot in Square.

In theVentureBeatinterview, Willem Avé, Block's head of product at Square, said the ManagerBot harness "draws heavily on Goose" and incorporates learnings from MoneyBot on Cash App.

During the investor day, Jack Dorsey said that MoneyBot and ManagerBot would become the primary interfaces through which Block’s customers interact with Cash App and Square. At the time, that vision wasn’t entirely clear.

Source:Block’s Investor Day 2025

However, after months of using Claude Code and seeing what it can do, it now makes much more sense to me.

## MoneyBot inside Cash App

MoneyBot is essentially an agent that uses LLMs and “tools” inside a Cash App account: transaction history, balances, savings goals, Bitcoin, stocks, bill requests, person-to-person payments.

Type "Send $500 to Reese for rent" and MoneyBot drafts the payment. Ask about monthly income and spending patterns, and it pulls the data, answers in plain language, and suggests how much to set aside for savings. Say "I want to save $1,000 for a vacation in six months" and MoneyBot builds the full savings plan off a handful of follow-up questions.

Source:Cash App

MoneyBot never moves money on its own. Cash App's announcement states it directly: every payment, transfer, or trade requires explicit user confirmation before anything happens. The agent proposes, the user approves. The same pattern ManagerBot would later adopt for sellers.

## ManagerBot inside Square

This month, Block launched ManagerBot in open beta for Square sellers. The “tools” it can reach are the ones inside the Square stack: POS data, inventory, scheduling, payroll, catalog, email marketing.

Source:Square

Square exposes hundreds of possible tools across all those domains, and the agent has to navigate them in a single coherent loop:

* Inventory forecasting.ManagerBot watches stock levels and sales velocity, then folds in external signals like weather and local events. The agent alerts the seller when an item is about to run out and drafts the purchase order.
* Shift scheduling.ManagerBot ingests forecasted sales, balances worker preferences against coverage needs, and generates the schedule.
* Marketing.ManagerBot identifies sales trends across a seller's catalog and drafts win-back campaigns and promotions targeted at the best customer segments.

ManagerBot also uses the same safety design as MoneyBot. Every write action (inventory change, schedule update, campaign send) shows up as a visual preview in a task queue before the seller clicks yes.

## The proactive shift

Every agent above still assumes the user speaks first. You type, the agent acts. However, the bigger unlock is flipping that. This is how Willem Avé describes this:

❝

"The big shift from Square AI to Managerbot is really from reactive to proactive. What that means is the primary interface is not a question box. You assign tasks to Managerbot, and that could be based on data, an insight, or a signal from your business."

Willem Avé, Block's head of product at Square

Technically, it's a small change. Run the agent on a schedule with a different prompt: "Look for anomalies, savings, or risks in the seller's state since yesterday. Report only the ones worth a human's attention." Same tool list and same harness, but a different entry point.

The second-order effect is already visible. Avé said sellers who adopt ManagerBot voluntarily move more of their operations onto Square: payroll, time cards, shift schedules. The agent that sees the whole business is more useful than the one that sees half, and sellers feed it more data in response.

## The 2024 head start

Block started on this in 2024, before most companies understood why AI agents mattered. By now they have build Goose for engineers, MoneyBot for consumers, and ManagerBot for small business owners.

The internal results are already visible. Block's Q4 2025 earnings reported more than 40 percent more production code shipped per engineer since September 2025 from agentic coding tools. In late February, Jack Dorsey cut roughly 4,000 of Block's 10,000 employees, citing AI as the rationale.

Goose and Claude Code showed what AI agents can do for engineering. Now MoneyBot and ManagerBot need to show what AI agents can do for money.

Cover image source: Block

Disclaimer: The views expressed here are my own and do not represent the views of my employer. The information contained in this newsletter is intended for educational and informational purposes only and should not be considered financial advice. You should do your own research or seek professional advice before making any investment decisions. Read the full disclaimerhere.

### Keep Reading

View more
caret-right

#### Popular Fintech

Become a smarter Fintech founder, operator, and investor

Subscribe
© 2026 Popular Fintech.
Report abuse
Privacy policy
Terms of use
beehiiv
Powered by beehiiv
---
title: micasa — your house, in a terminal
url: https://micasa.dev
site_name: hnrss
content_file: hnrss-micasa-your-house-in-a-terminal
fetched_at: '2026-02-19T19:25:09.626155'
original_url: https://micasa.dev
date: '2026-02-19'
description: A terminal UI for tracking everything about your home. Single SQLite file. No cloud. No account. No subscriptions.
tags:
- hackernews
- hnrss
---

Your house is quietly plotting to break while you sleep—and
you’re dreaming about redoing the kitchen.

micasatracks maintenance, projects, incidents, appliances, vendors, quotes, and documents—all from your terminal.

## Frequentlyaskedquestions

When did I last change the furnace filter?

Maintenance schedules, auto-computed due dates, full service history.

What if we finally did the backyard?

Projects from napkin sketch to completion—or graceful abandonment.

How much would it actually cost to…

Quotes side by side, vendor history, and the math you need to actually decide.

Is the dishwasher still under warranty?

Appliance tracking with purchase dates, warranty status, and maintenance history tied to each one.

The basement is leaking again.

Log incidents with severity and location, link them to appliances and vendors, and resolve them when fixed.

Who did we use last time?

A vendor directory with contact info, quote history, and every job they've done for you.

Where’s the warranty card?

Attach files—manuals, invoices, photos—directly to projects and appliances. Stored in the same SQLite file.

## Getstarted

Install with Go (1.25+):

go install github.com/cpcloud/micasa/cmd/micasa@latest

or grab a binary from thelatest release

Linux, macOS, and Windows binaries are available for amd64 and arm64.

Try it in 30 seconds:

micasa --demo # poke around with sample data
micasa # start fresh with your own house
micasa --print-path # show where the database lives

Linux, macOS, Windows. One SQLite file, your machine. Back it up withcp.

## Keyboarddriven

Vim-style modal keys.navto browse,editto change things. Sort by any column, jump to columns with fuzzy search, hide what you don't need, drill into related records. The full list is in thekeybinding reference.

## Whatpeopleare saying

## Whythisexists

I built this because my home maintenance system was a shoebox of receipts and the vague feeling I was supposed to call someone about the roof.

micasareplaces the shoebox, the binder you never open, and the sticky note on the fridge with one SQLite file and a terminal you already have open. Its modal, keyboard-driven interface is inspired byVisiData.

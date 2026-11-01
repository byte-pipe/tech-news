---
title: 'Mark Kretschmann on X: "Anthropic ported its Messages API from Python to Rust with a team that initially had no Rust developers. @claudeai handled most of the implementation, while the engineers designed the system, planned the migration and verified the results. According to platform engineering h… / X'
url: https://x.com/mark_k/status/2116912634171711850
site_name: tldr
content_file: tldr-mark-kretschmann-on-x-anthropic-ported-its-message
fetched_at: '2026-11-02T08:48:36.266546'
original_url: https://x.com/mark_k/status/2116912634171711850
date: '2026-11-02'
published_date: '2026-11-01T15:17:56.000Z'
description: Anthropic ported its Messages API from Python to Rust with a team that initially had no Rust developers. @claudeai handled most of the implementation, while the engineers designed the system, planned the migration and verified the results. According to platform engineering head Katelyn Lesse, the r…
tags:
- tldr
---

## Post

Log in
Sign up

## Post

Log in
Sign up

# Mark Kretschmann on X: "Anthropic ported its Messages API from Python to Rust with a team that initially had no Rust developers. @claudeai handled most of the implementation, while the engineers designed the system, planned the migration and verified the results. According to platform engineering head Katelyn Lesse, the result was roughly 40–50% lower CPU usage for the API service and a 10–20% improvement in time to first token.

They built the Rust version alongside the existing Python service, ran shadow traffic through both to compare their outputs, then gradually switched real traffic over. They deliberately avoided adding features during the rewrite. That's a substantial production migration with measurable benefits, carried out by engineers using AI to work in a language they learned along the way."

Mark Kretschmann
@mark_k
Anthropic ported its Messages API from Python to Rust with a team that initially had no Rust developers. 
@claudeai
 handled most of the implementation, while the engineers designed the system, planned the migration and verified the results. According to platform engineering head Katelyn Lesse, the result was roughly 40–50% lower CPU usage for the API service and a 10–20% improvement in time to first token.

They built the Rust version alongside the existing Python service, ran shadow traffic through both to compare their outputs, then gradually switched real traffic over. They deliberately avoided adding features during the rewrite. That's a substantial production migration with measurable benefits, carried out by engineers using AI to work in a language they learned along the way.
3:17 PM · Nov 1, 2026
·
2,556
Views
9
6
27
4
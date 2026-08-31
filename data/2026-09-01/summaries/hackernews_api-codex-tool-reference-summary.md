---
title: Codex Tool Reference
url: https://codex-tool-reference.simonw.chatgpt.site/
date: 2026-09-01
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-09-01T09:51:49.968889
---

# Codex Tool Reference

# Codex Tool Reference Summary

## Overview
- The inventory lists callable **tools** (endpoints) and **skills** (instruction packages) for Codex.
- Current snapshot includes **232 tool interfaces** and **44 complete main skill files**.
- Skill pages contain verbatim `SKILL.md` sources; tool reference shows descriptions and TypeScript declarations.
- Availability may vary with session settings, permissions, connected apps, and installed plugins.

## Skills
- Each available skill has its own page with a full copy of its definition.
- Total of **44 skill pages**.

## Documents & Visuals (10 tools)
- **answers-charts** – Use for categorical comparisons, trends, compositions, or numeric relationships best shown as charts.
- **answers-images** – Retrieve images to visually ground or enhance answers.
- **answers-learning** – Provide flashcards, multiple‑choice quizzes, pronunciation help, or interactive learning widgets when requested.
- **documents** – Create, edit, redline, and comment on `.docx`, Word, and Google Docs with a render‑and‑verify workflow; generate PNGs/PDFs via `render_docx.py`.
- **imagegen** – Generate or edit raster images (photos, illustrations, textures, sprites, cutouts) when a bitmap asset is needed; avoid for vector or code‑native visuals.
- **pdf** – Read, create, inspect, render, and verify PDFs (including AcroForms) using Poppler, ReportLab, pdfplumber, and pypdf.
- **Presentations** – Read, create, or edit PowerPoint or Google Slides decks.
- **Spreadsheets** – Work with `.xlsx`, `.xls`, `.csv`, `.tsv`, or Google Sheets, handling formulas, formatting, charts, and recalculation.
- **visualize** – Produce visualizations and interactive tools directly in conversation (simulations, maps, charts, mockups, scientific figures).
- **writing-blocks** – Deliver complete drafts of requested text (emails, posts, bios, paragraphs); prefer file creation for longer documents.

## Browser & Sites (4 tools)
- **control-browser** – Operate a browser for authenticated or public web tasks; use `browserAuth` for sign‑in, prefer web search first, and fall back to plugins before the browser.
- **sites:sites-building** – Build websites, landing pages, dashboards, portals, trackers, and internal tools; required when a project contains `.openai/hosting.json`.
- **sites:sites-hosting** – Host websites built with `sites-building`; manage registration, publishing, deployment verification, or hosting without source changes.
- **sites:sites-preview-troubleshooting** – Diagnose and recover from preview start‑up or health issues after `sites-building`.

## Context & Interaction (4 tools)
- **demos:answers-ask-user-input** – Prompt the user for missing context when a small amount of information would materially improve the answer.
- **openai-library:library** – Access the ChatGPT Library for searching, reading, saving, or updating user‑owned files, sites, or folders; also used to create user‑facing artifacts.
- **personal-context** – Retrieve prior conversation state, preferences, constraints, or decisions that affect current tasks; invoke before other tools when relevant.
- **resolve-recipients** – Verify correct recipients for Slack messages, emails, invitations, or calendar events; resolve ambiguities by searching communication history and asking for clarification.

## OpenAI, Skills & Plugins (7 tools)
- **openai-docs** – Provide information on Codex models, pricing, scheduled tasks, settings, troubleshooting, automation, APIs, SDKs, Realtime, agents, evaluations, and comparisons; not for generic software tasks.
- **plugin-creator** – Scaffold new plugin directories with required `plugin.json`, optional files, default manifests, and marketplace entries; supports cache‑busting and reinstall flow.
- **plugin-management:plugin-management** – Discover, suggest, inspect, connect, or remove plugins; use when external apps, services, or data sources would benefit a task.
- **skill-creator** – (Description truncated in source; intended for creating new skill definitions.)
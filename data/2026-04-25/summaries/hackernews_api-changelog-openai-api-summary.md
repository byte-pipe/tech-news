---
title: Changelog | OpenAI API
url: https://developers.openai.com/api/docs/changelog
date: 2026-04-25
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-04-25T08:24:37.434073
---

# Changelog | OpenAI API

# Changelog Summary

## April 2026
- **Apr 24 – Feature:** Launched **gpt‑5.5** and **gpt‑5.5‑pro** on Chat Completions, Responses, and Batch APIs.  
  - 1 M‑token context, image input, structured outputs, function calling, prompt caching (extended only), tool search, built‑in computer use, hosted shell, apply patch, Skills, MCP, web search.  
  - Default reasoning effort set to *medium*; image_detail defaults to original behavior when unset or set to *auto*.
- **Apr 21 – Feature:** Introduced **gpt‑image‑2** (generation & editing) with flexible sizes, high‑fidelity inputs, token‑based pricing, and 50 % Batch discount.
- **Apr 15 – Update:** Enhanced Agents SDK: sandboxed execution, open‑source harness inspection/customization, controllable memory creation and storage.

## March 2026
- **Mar 17 – Feature:** Released **gpt‑5.4‑mini** and **gpt‑5.4‑nano** (Chat Completions & Responses).  
  - Mini: tool search, built‑in computer use, compaction.  
  - Nano: compaction only (no tool search/computer use).
- **Mar 16 – Update:** `gpt‑5.3‑chat‑latest` slug now points to the current ChatGPT model.
- **Mar 13 – Fix:** Updated GPT‑5.4 image encoder; improves image‑understanding quality, no user action needed.
- **Mar 12 – Feature:** Expanded **Sora** video API (character refs, up to 20 s generations, 1080p for sora‑2‑pro, video extensions, Batch support). 1080p billed at $0.70 / s.
- **Mar 12 – Update:** Added `POST /v1/videos/edits`; deprecates `POST /v1/videos/{video_id}/remix` (6‑month deprecation).
- **Mar 5 – Feature:** Launched **gpt‑5.4** and **gpt‑5.4‑pro** (Chat Completions & Responses).  
  - Tool search in Responses, built‑in computer tool, 1 M‑token context, native compaction.
- **Mar 3 – Feature:** Released `gpt‑5.3‑chat‑latest` (Chat Completions & Responses) pointing to the GPT‑5.3 Instant snapshot.

## February 2026
- **Feb 24 – Feature:** broadened `input_file` support to more document, presentation, spreadsheet, code, and text types.
- **Feb 24 – Feature:** Added **phase** label to Responses API (intermediate commentary vs. final answer).
- **Feb 24 – Feature:** Released **gpt‑5.3‑codex** on Responses API.
- **Feb 23 – Feature:** Launched WebSocket mode for Responses API.
- **Feb 23 – Feature:** Released **gpt‑realtime‑1.5** (Realtime API) and **gpt‑audio‑1.5** (Chat Completions API).
- **Feb 10 – Feature:** Batch API support for GPT Image models (1.5, 1, 1‑mini, chatgpt‑image‑latest).  
  Also introduced server‑side compaction, Skills support, Hosted Shell tool with container networking, and JSON request format for `/v1/images/edits`.
- **Feb 9 – Feature:** Added `application/json` request handling for image edit endpoints.
- **Feb 3 – Update:** Optimized inference stack; **gpt‑5.2** and **gpt‑5.2‑codex** run ~40 % faster (model unchanged).

## January 2026
- **Jan 15 – Announcement:** Introduced **Open Responses**, an open‑source spec for multi‑provider LLM interfaces built on the original Responses API.
- **Jan 14 – Feature:** Released **gpt‑5.2‑codex** (Responses API) for agentic coding tasks.
- **Jan 13 – Feature:** Added dedicated SIP IP ranges for Realtime API with GeoIP routing.
- **Jan 13 – Updates:**  
  - `gpt‑realtime‑mini` & `gpt‑audio‑mini` slugs now point to 2025‑12‑15 snapshots (previous snapshots available).  
  - `sora‑2` slug updated to 2025‑12‑08 snapshot.  
  - `gpt‑4o‑mini‑tts` & `gpt‑4o‑mini‑transcribe` slugs updated to 2025‑12‑15 snapshots; recommend `gpt‑4o‑mini‑transcribe` over `gpt‑4o‑transcribe`.
- **Jan 9 – Fix:** Corrected high‑fidelity default for image edits in **gpt‑image‑1.5** and **chatgpt‑image‑latest** when fidelity set to low.

## December 2025
- **Dec 19 – Update:** Added **gpt‑image‑1.5** and **chatgpt‑image‑latest** to the Responses API image generation tool.
- **Dec 16 – Feature:** Released **gpt‑image‑1.5** and **chatgpt‑image‑latest** (latest image generation models).
- **Dec 15 – Feature:** Launched four dated audio snapshots with reliability, quality, and voice‑fidelity improvements:  
  - `gpt‑realtime‑mini‑2025‑12‑15`  
  - `gpt‑audio‑mini‑2025‑12‑15`  
  - `gpt‑4o‑mini‑transcribe‑2025‑12‑15`  
  - `gpt‑4o‑mini‑tts‑2025‑12‑15`  

*End of summary.*
---
title: Survival LLM
url: https://www.brangus.io/survival-llm
date: 2026-10-28
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-10-29T21:00:41.714116
---

# Survival LLM

# Survival LLM – an AI that still works when the internet doesn’t  

## Overview  
- Free, open‑source AI assistant that runs entirely on your computer.  
- Designed for emergencies: food safety, first‑aid, water purification, repair guides, etc.  
- Answers are sourced from trusted articles, with clickable references showing the exact passage used.  

## Core Features  
- **No internet required after setup** – the model and library stay on the device, and queries never leave it.  
- **Source transparency** – every answer lists the articles consulted; you can open each source directly.  
- **Emergency‑focused content** – includes medical references, FEMA/CDC guidance, survival manuals, repair guides, and ~930 000 Wikipedia articles.  

## Versions & Model Selection  
| Computer type | AI model used | Test score (22 questions) | Model size |
|---|---|---|---|
| Mac ≥ 128 GB RAM | NVIDIA Nemotron 3.5 Super | 21/22 | 80 GB |
| Mac 32–96 GB RAM | Qwen 3.8 27B | 21/22 | 18 GB |
| Windows ≥ 32 GB RAM | NVIDIA Nemotron 3.5 Lightning | 19/22 | 25 GB |
| Mac/PC 16–31 GB RAM | IBM Granite 4.2 8B | 14/22 | 6 GB |

- The app detects available memory and downloads the appropriate model.  
- Full library: ~9.5 GB download (19 GB installed).  
- Minimal library (without Wikipedia & iFixit): 1.3 GB download (3 GB installed).  
- Required free disk space = model size + 5 GB + ≈ 27 GB during full installation.  

## Installation (3 steps)  
1. Download the zip for Mac or Windows and unzip.  
2. Open the app (double‑click `Survival LLM` on Mac; run `Survival LLM.bat` on Windows).  
3. Follow the on‑screen setup; the app will download the AI engine, the appropriate model, and the library.  

*First‑run warnings:*  
- macOS: open **System Settings → Privacy & Security**, click “Open Anyway” for Survival LLM.  
- Windows: click “More info” then “Run anyway”.  

## Library Contents (plain‑text, searchable)  
- ~930 000 most‑read Wikipedia articles  
- WikiMed medical encyclopedia  
- MedlinePlus (U.S. National Library of Medicine)  
- UK Medicines A‑to‑Z  
- WikEM emergency medicine  
- Ready.gov (FEMA) emergency guides  
- CDC travelers’ health  
- U.S. military medicine and survival manuals  
- Micromort risk tables and U.S. death rates  
- wikiHow how‑to guides  
- iFixit repair manuals  
- Appropedia (appropriate technology)  
- Stack Exchange Q&A on home repair, cooking, gardening, outdoors, ham radio  

Each source retains its original license, displayed with every article.  

## Important Notes  
- **Potential errors:** Smaller models are less reliable; always verify using the listed sources.  
- **Privacy:** No account, no tracking; questions never leave the computer.  
- **Personal files:** You can add PDFs, Word docs, ebooks, or personal notes; the AI searches them locally.  
- **Updates:** One‑click “Check for updates” at the bottom of the app; updates replace models, library, and personal files.  
- **Battery use:** Measured ~100 W on a MacBook Pro; a full battery yields roughly 100–300 answers, easily powered by a small generator.  

## Recent Update History (October 2026)  
- **0.3.4** – Added configurable reasoning token limits; improved fallback when lookup finds articles but no answer; clarified source origin; warning for unlimited reasoning/length.  
- **0.3.3** – Mac quit (Cmd+Q) now stops AI engine; duplicate library entries removed.  
- **0.3.2** – Questions no longer saved as memory notes; corrected erroneous “Sources:” lines; clearer reasoning display; Windows cleanup of empty folders.  
- **0.3.1** – “Show reasoning” feature reveals AI’s intermediate searches and thoughts on demand.  
- **0.3.0** – Memory notes for personal info; improved download compatibility with custom certificates.  

All releases are available on GitHub.
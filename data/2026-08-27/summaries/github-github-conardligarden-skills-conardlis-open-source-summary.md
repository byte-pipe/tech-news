---
title: "GitHub - ConardLi/garden-skills: ConardLi's open-source Skills collection, featuring web design, knowledge retrieval, image generation, and more. · Gi..."
url: https://github.com/ConardLi/garden-skills
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-08-27T06:41:18.338901
---

# GitHub - ConardLi/garden-skills: ConardLi's open-source Skills collection, featuring web design, knowledge retrieval, image generation, and more. · Gi...

# Garden Skills – Summary

## Overview
- Curated collection of production‑ready **Agent Skills** for Claude Code, Cursor, Codex, and other AI coding agents.  
- Includes skills for web video/presentation, web design, image generation, knowledge retrieval, and more.  
- Multilingual documentation (English, 中文, 日本語).  

## Main Skill Categories
- **web-video-presentation** – Turns scripts, articles, or demos into 16:9, screen‑record‑ready Vite + React + TypeScript presentations.  
- **web-design-engineer** – Generates polished front‑end artifacts (pages, dashboards, UI mockups) with design‑system guidance and anti‑cliché patterns.  
- **gpt-image-2** – Image‑generation and editing skill supporting local Garden mode, host‑native delegation, or prompt‑only advisor mode; provides 18 visual categories and 79 prompt templates.  
- **kb-retriever** – Local knowledge‑base retriever that searches hierarchical indexes, handles Markdown, PDF, Excel, and returns answers with source citations.  

## Highlights of Selected Skills  

### web-video-presentation
- Fixed 1920 × 1080 stage, scalable viewport.  
- Click/keyboard navigation with scripted beats.  
- 23 built‑in themes (editorial, terminal, Swiss International, etc.).  
- Pluggable TTS providers (MiniMax mmx‑cli, OpenAI TTS, ElevenLabs, Azure, Google Cloud, macOS say).  

### web-design-engineer
- Generates a five‑dial **Design Read** (variance, motion, density, asset dependence, brand fidelity).  
- Supports extension, preserve, and overhaul redesign modes.  
- Provides a Design Direction Advisor (six schools) and 25 anchored style recipes (Linear, Aesop, Pentagram, Bloomberg, Stripe Press, Mid‑Century, etc.).  
- Handles HTML, CSS, JavaScript, React, responsive layout, motion, container queries, reduced‑motion.  

### gpt-image-2
- Three runtime modes: Garden local, host‑native delegation, advisor‑only prompt writing.  
- Detects mode automatically to avoid silent mis‑execution.  
- Stores prompts and generated images for versioning.  
- Example outputs: background replacement, chat‑interface mockup, product‑card overlay, dense explainer slides, anime key visual, etc.  

### kb-retriever
- Progressive search through hierarchical indexes to limit context size.  
- Correctly parses structured documents (Markdown, PDF, Excel).  
- Returns answers with explicit source references.  

## Installation & Usage
- **CLI**: `npx garden-skills` (or similar) to install and run skills.  
- **Claude Code plugin marketplace**: Skills available as downloadable plugins.  
- **Manual**: Copy skill files, add as a Git submodule, or use the released `.zip` packages.  

## Contributing
- Contribution guidelines provided in `CONTRIBUTING.md` (English, Japanese, Chinese).  
- Encourages adding new skills, improving documentation, and reporting issues.  

## License
- Distributed under the repository’s open‑source license (see `LICENSE` file).  

## Resources
- README files for each skill (`README.md`, `SKILL.md`).  
- Live demos and galleries linked from each skill section.  
- Release assets (e.g., `v1.2.2.zip`, `v1.3.0.zip`, `v1.0.4.zip`).
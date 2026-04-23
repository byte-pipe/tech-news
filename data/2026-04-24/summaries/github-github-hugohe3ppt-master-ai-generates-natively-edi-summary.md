---
title: GitHub - hugohe3/ppt-master: AI generates natively editable PPTX from any document — real PowerPoint shapes, not images — no design skills needed · Gi...
url: https://github.com/hugohe3/ppt-master
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-04-24T06:04:13.129185
---

# GitHub - hugohe3/ppt-master: AI generates natively editable PPTX from any document — real PowerPoint shapes, not images — no design skills needed · Gi...

# PPT Master — AI generates natively editable PPTX from any document

## Overview
- Generates fully editable PowerPoint decks from PDF, DOCX, URL, or Markdown using AI models (Claude, GPT, Gemini, etc.).
- Output contains real PowerPoint shapes, text boxes, and charts—not static images.
- Operates as a workflow (“skill”) inside AI IDEs such as Claude Code, Cursor, VS Code + Copilot, or Codebuddy.
- Open‑source under the MIT license; the only cost is the AI model usage (as low as $0.08 per deck with VS Code Copilot).
- All processing runs locally; no file uploads to external servers.

## Key Features
- **Editable PPTX**: Every element is directly clickable and modifiable in PowerPoint.
- **Transparent pricing**: Free tool; you only pay for the AI model you use.
- **Data privacy**: Files stay on your machine; only AI model communication occurs.
- **No platform lock‑in**: Works with multiple AI editors and models.
- **Examples**: 12‑page deck from a WeChat article, 10‑page dark‑tech deck from Claude Code blog, 15 projects totaling 229 pages.

## Gallery (template styles)
- Magazine – warm, photo‑rich layout  
- Academic – structured, data‑driven format  
- Dark Art – cinematic dark background  
- Nature Documentary – immersive photography, minimal UI  
- Tech / SaaS – clean white cards, pricing tables  
- Product Launch – high‑contrast, bold specifications  

## Author
- Hugo He – finance professional who built the tool to eliminate manual slide creation.  
- Contact: heyug3@gmail.com, personal website, GitHub @hugohe3.

## Support
- Project is self‑funded; sponsorships (individual or enterprise) help cover AI token costs, new templates, bug fixes, and documentation.

## Quick Start

### Prerequisites
- Python 3.10+ (install via python.org, Homebrew, or apt).  
- Install dependencies: `pip install -r requirements.txt`.  
- Optional fallbacks (rarely needed): Node.js (for WeChat articles) and Pandoc (for legacy formats).

### Choose an AI Editor
| Tool | Rating | Notes |
|------|--------|-------|
| Claude Code | ★★★ | Best results, native Opus, largest context |
| Cursor / VS Code + Copilot | ★★ | Good alternatives |
| Codebuddy IDE | ★★ | Best for Chinese models (Kimi, MiniMax) |

### Installation
- **Option A** – Download ZIP from GitHub, unzip.  
- **Option B** – Clone repository:  
  ```bash
  git clone https://github.com/hugohe3/ppt-master.git
  cd ppt-master
  pip install -r requirements.txt
  ```
- Update (Option B only): `python3 skills/ppt-master/scripts/update_repo.py`.

### Create a Deck
1. Place source material (PDF, DOCX, images, etc.) in the `projects/` directory.  
2. In the AI chat panel, specify the file path (right‑click → Copy Path) and ask the AI to generate the deck.  
3. The AI follows the workflow and produces an editable `.pptx` on your computer.

## License
- MIT License; attribution required.
---
title: GitHub - elayadesign/ai-design-skills · GitHub
url: https://github.com/elayadesign/ai-design-skills
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-10-28T12:08:15.832576
---

# GitHub - elayadesign/ai-design-skills · GitHub

# AI Design Skills Summary

## Overview
- Repository of self‑contained design skill folders for AI coding tools (Claude Code, Cursor, Codex, Windsurf, etc.).
- Each skill can be installed individually and used by prompting the AI in plain language.

## Available Skills
- **landing-page-design**
  - Generates a complete landing page: intake questions, page structure, conversion copy, visual system (typography, spacing, radius, motion).
  - Future skills are planned.
  - An upgrade‑existing‑site skill exists in a separate repository.

## Installation
- **Claude Code**
  - Create skills directory: `mkdir -p .claude/skills`
  - Clone repo to temporary location and copy the desired skill:
    ```
    git clone https://github.com/elayadesign/ai-design-skills.git /tmp/ai-design-skills
    cp -r /tmp/ai-design-skills/skills/<skill-name> .claude/skills/
    ```
- **Cursor**
  - Create rules directory: `mkdir -p .cursor/rules`
  - Download the skill markdown:
    ```
    curl -o .cursor/rules/<skill-name>.md \
    https://raw.githubusercontent.com/elayadesign/ai-design-skills/main/skills/<skill-name>/SKILL.md
    ```
  - Or paste the file into Settings → Rules for AI.
- **Codex / Windsurf / Other Tools**
  - Copy the skill’s `SKILL.md` to the location your tool uses for project rules:
    - Codex → `AGENTS.md`
    - Windsurf → `.windsurfrules`
    - Cline → `.clinerules`
    - Generic → paste into system prompt.
- **Claude.ai (no terminal)**
  - Download the skill’s `SKILL.md`, upload to a Project, or attach to a chat and instruct “follow this.”

## Customization
- Design values (fonts, colors, spacing, motion) are defined in a single section near the bottom of each skill file.
- Fork the repository, edit that section, and the rest of the skill updates automatically.

## Credits
- `landing-page-design` adapts content realism and motion ideas from **Leon Lin** (`Leonxlnx/taste-skill`), MIT licensed. Details are at the end of its `SKILL.md`.

## License
- MIT License: free to use, fork, ship, or sell creations without attribution.
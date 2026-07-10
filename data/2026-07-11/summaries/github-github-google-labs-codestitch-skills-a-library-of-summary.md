---
title: GitHub - google-labs-code/stitch-skills: A library of Agent Skills designed to work with the Stitch MCP server. Each skill follows the Agent Skills op...
url: https://github.com/google-labs-code/stitch-skills
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-07-11T01:40:07.335742
---

# GitHub - google-labs-code/stitch-skills: A library of Agent Skills designed to work with the Stitch MCP server. Each skill follows the Agent Skills op...

# Stitch Design Skills Repository Summary

## Overview
- A collection of agent skills and plugins for **Google Stitch** adhering to the **Agent Skills open standard**.  
- Compatible with coding agents such as **Codex, Antigravity, Gemini CLI, Claude Code, Cursor**.  
- Not an officially supported Google product and not eligible for the Google Open Source Software Vulnerability Rewards Program.

## Quick Start

### 1. Install Plugins (Recommended)
- **Codex**
  - Add the Stitch Skills marketplace and install desired plugins via CLI or UI.
  - CLI example (sparse checkout for faster clone):
    ```bash
    codex plugin marketplace add google-labs-code/stitch-skills --ref main \
      --sparse .agents/plugins \
      --sparse plugins/stitch-design \
      --sparse plugins/stitch-build \
      --sparse plugins/stitch-utilities
    ```
  - UI: Settings → Plugin Marketplaces → Add → Source `https://github.com/google-labs-code/stitch-skills`, Ref `main`, optional sparse paths.
  - Install any combination of:
    - `stitch-design` – design‑focused skills
    - `stitch-build` – build and component skills
    - `stitch-utilities` – utility and helper skills
- **Claude Code**
  - `npx plugins add google-labs-code/stitch-skills --scope project --target claude-code`
- **Cursor**
  - `npx plugins add google-labs-code/stitch-skills --scope workspace --target cursor`

### 2. Install Skills Selectively
- Use `npx skills add google-labs-code/stitch-skills` to add individual skills.
- Ensure all required dependencies are included, as many design skills have inter‑dependencies.
- Helpful commands:
  - `npx plugins --help`
  - `npx skills --help`

## Prerequisites
- The **Stitch MCP server** must be configured and running in the agent’s environment.
- Follow the Stitch MCP Setup Instructions to register the server and set required environment variables and credentials.

## Available Plugins

### Design (`stitch-design`)
| Skill | Description | Prompt Example |
|------|-------------|----------------|
| `stitch::code-to-design` | Convert frontend code (React, Vue, etc.) to a Stitch Design via HTML extraction, design system, and upload. | “Upload the frontend code at `/path/to/dashboard` into a Stitch project named `Dashboard-Migration-2026`.” |
| `stitch::generate-design` | Generate new screens from text or images, edit existing screens, create design variants. | “Make a browse tab for a mobile app for romance and date night ideas.” |
| `stitch::manage-design-system` | Upload `DESIGN.md` and apply themes to screens. | “Upload our design system from `.stitch/DESIGN.md` and apply it to all screens.” |
| `stitch::extract-design-md` | Extract a comprehensive `DESIGN.md` directly from frontend source code. | “Scan `/src` and extract the design system into `.stitch/DESIGN.md`.” |
| `stitch::extract-static-html` | Extract self‑contained static HTML from running web apps, inlining CSS and images. | “Extract a static HTML snapshot of `http://localhost:3000/profile`.” |
| `stitch::upload-to-stitch` | Upload local assets (images, mockups, HTML) to a Stitch project. | “Upload `.stitch/landing_page.html` to Stitch project `projects/987654321`.” |

### Build (`stitch-build`)
| Skill | Description | Prompt Example |
|------|-------------|----------------|
| `stitch::react-components` | Convert Stitch screens to React component systems with validation and design‑token consistency. | “Convert all screens in Stitch project `projects/123` to React components.” |
| `stitch::react-native` | Convert Stitch HTML designs to production‑ready React Native components with `StyleSheet` and platform‑specific code. | “Convert the Stitch design to React Native components with proper theme and navigation.” |
| `remotion` | Generate walkthrough videos from Stitch projects using Remotion with smooth transitions and zooming. | “Generate a walkthrough video of the Stitch project `projects/456`.” |
| `shadcn-ui` | Expert guidance for integrating and building applications with `shadcn/ui` components. | “Set up shadcn/ui and build a data table with sorting and filtering.” |

### Utilities (`stitch-utilities`)
| Skill | Description | Prompt Example |
|------|-------------|----------------|
| `design-md` | Analyze Stitch projects and generate comprehensive `DESIGN.md` files in semantic language. | “Analyze Stitch project `projects/123` and generate a DESIGN.md.” |
| `enhance-prompt` | Transform vague UI ideas into polished, Stitch‑optimized prompts with UI/UX keywords. | “Enhance this prompt: ‘make a settings page’.” |
| `stitch-loop` | Generate complete multi‑page websites from a single prompt with automated validation. | “Build a 5‑page portfolio website with Stitch.” |
| `taste-design` | Generate `DESIGN.md` files enforcing premium, anti‑generic UI standards. | “Generate a premium DESIGN.md with strict typography and calibrated colors.” |

## Repository Structure
```
plugins/
├── stitch-design/
│   ├── plugin.json
│   └── skills/
│       ├── code-to-design/
│       ├── generate-design/
│       ├── manage-design-system/
│       ├── extract-design-md/
│       ├── extract-static-html/
│       └── upload-to-stitch/
├── stitch-build/
│   ├── plugin.json
│   └── skills/
│       ├── react-components/
│       ├── react-native/
│       ├── remotion/
│       └── shadcn-ui/
└── stitch-utilities/
    ├── plugin.json
    └── skills/
        ├── design-md/
        ├── enhance-prompt/
        ├── stitch-loop/
        └── taste-design/
```

### Skill File Layout (per Agent Skills standard)
```
skills/<skill-name>/
├── SKILL.md          # Mission Control for the agent
├── scripts/          # Executable enforcers (validation & networking)
├── resources/        # Knowledge base (checklists, style guides)
└── examples/         # Gold‑standard syntactically valid references
```

## Adding New Skills
- Follow the file structure above to implement the Agent Skills open standard.
- **Promising skill ideas:**
  - Validation skills converting Stitch HTML to other UI frameworks and checking syntax.
  - Data‑decoupling skills turning static design content into external mock data files.
  - Design‑generation skills creating new Stitch screens from supplied data sets.
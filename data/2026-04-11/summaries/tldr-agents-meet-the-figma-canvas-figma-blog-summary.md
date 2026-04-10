---
title: Agents, Meet the Figma Canvas | Figma Blog
url: https://www.figma.com/blog/the-figma-canvas-is-now-open-to-agents/
date: 2026-04-11
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-04-11T06:03:48.094129
---

# Agents, Meet the Figma Canvas | Figma Blog

# Agents, meet the Figma canvas

## Overview
- Starting today, AI agents can create and modify designs directly on the Figma canvas.  
- The feature is in beta, free for now, and will become a usage‑based paid offering later.  
- Agents are guided by **skills**, markdown files that encode team context, design system rules, and workflow steps.

## AI agents on the canvas
- Agents now have access to the full design context (color palettes, typography, spacing, interactivity), reducing generic outputs.  
- Through the `use_figma` tool, agents such as Claude Code, Codex, and other LLMs can write to Figma files and components.  
- This creates a shared context where code and design can be edited fluidly.

## MCP server & `use_figma` tool
- The Figma MCP (Model‑Centric Platform) server is released in beta, embedding Figma into developer workflows.  
- It enables LLMs to generate design‑informed code and to modify Figma assets that are linked to a design system.  
- The existing `generate_figma_design` tool converts live HTML/UI into editable Figma layers; `use_figma` lets agents edit or create assets using the team’s components and variables.

## Skills: definition and examples
- **Skills** are markdown‑based instruction sets that tell agents how to operate on the canvas, what sequencing to follow, and which conventions to respect.  
- They bridge the knowledge gap, ensuring outputs align with brand and design intent without requiring plugins or code.  
- Core skill `/figma-use` provides a shared understanding of Figma’s structure; other skills extend it.  
- Example skills released in the beta:
  - `/figma-generate-library` – create components from a codebase.  
  - `/figma-generate-design` – build designs using existing components/variables.  
  - `/create-voice` – generate screen‑reader specs from UI specs.  
  - `/cc-figma-component` – turn a structured JSON contract into Figma components.  
  - `/apply-design-system` – connect designs to system components.  
  - `/rad-spacing` – apply hierarchical spacing with variables.  
  - `/edit-figma-design` – orchestrate design workflows with Warp and Oz.  
  - `/sync-figma-token` – sync design tokens between code and Figma variables with drift detection.  
  - `/multi-agent` – run parallel workflows and implement designs in Augment.

## Benefits & workflow impact
- Agents can iterate on real Figma structures (components, auto‑layout, variables), enabling self‑healing loops and more predictable outcomes.  
- Skills make non‑deterministic LLM behavior more reliable by encoding specific steps and guidelines.  
- Teams can author skills without building plugins, fostering community sharing and faster adoption of custom workflows.  
- Integration with Code Connect and the Plugin API expands accessibility of design system code to developers, designers, and FigJam.

## Future roadmap
- Expand native AI functionality on the canvas and simplify skill creation/sharing.  
- Add parity with the Plugin API, starting with image support and custom fonts.  
- Continue improving security, reliability, and documentation (guides, developer docs) for the MCP server and skill ecosystem.  
- Encourage community contributions and showcase collaborative designs built by agents and humans.
---
title: "Teaching Google Antigravity to Paint: A Stateful Image-Editing Skill Built on Gemini's Interactions API and MCP - DEV Community"
url: https://dev.to/gde/teaching-google-antigravity-to-paint-a-stateful-image-editing-skill-built-on-geminis-interactions-9g1
date: 2026-07-24
site: devto
model: llama3.2:1b
summarized_at: 2026-07-25T11:34:16.418307
---

# Teaching Google Antigravity to Paint: A Stateful Image-Editing Skill Built on Gemini's Interactions API and MCP - DEV Community

## Stateful Image-Editing Skill
### Overview of NB2Lite

NB2Lite is a Google image-generation model that uses Gemini's stateful Interactions API to achieve a stateless workflow. This enables seamless editing and refinement of generated images using Antigravity.

### Key Points:

* **High-efficiency Model**: NB2Lite has sub-2-second generation times and solid text rendering in 25+ languages.
* **Interactions API Support**: The model uses the Interactions API for stateful computations, preserving context across turns.
* **FastMCP Server**: A separate server (nb2lite-agent) provides tools for interacting with NB2Lite through its MCP interface.

### Practical Details

* **Canvas Preservation**: The model edits existing canvases while handling interaction IDs to ensure pixel continuity.
* **Aspect Ratio Choices**: Three aspect ratios are supported: 1:1, 16:9, and 4:3.
* **Aspect Ratios**: Editing from a stale ID can temporarily degrade pixel continuity due to the API's limitations.

### Image Generation

*   Antigravity requests an image prompt (e.g., "add a neon RAMEN sign").
*   The model stores the context for the next interaction, ensuring continued visual consistency.
*   If the same prompt changes (e.g., "generate an image of a cyberpunk kitchen"), the model silently forks your session from an older state.

### Image Editing via Antigravity

*   Once you type something in Antigravity, it becomes an action to generate and edit images using NB2Lite without needing client interactions.
*   The model updates existing canvases with new edits while preserving context.
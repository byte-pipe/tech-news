---
title: Layers — AI skills for product designers
url: https://layers.jamiemill.com/
date: 2026-07-22
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-07-22T06:02:50.320390
---

# Layers — AI skills for product designers

# Layers — AI skills for product designers

## Overview
- Guides designers through the seven layers of product design, ensuring decisions beneath the UI are addressed.  
- Install with `npx skills add jamiemill/layers-skills`; runs in Claude Code, Cursor, OpenAI Codex, pi.dev, and 50+ other tools.  
- Open‑source repository: github.com/jamiemill/layers-skills.

## The Seven Layers (plus Reality)
1. Observed behaviour  
2. The domain  
3. User needs  
4. Product & service strategy  
5. Conceptual model  
6. Interaction structure & flow  
7. Surface  
- “Reality” sits beneath the layers as the ultimate context.

## Getting Started
- Run **/layers-orient** to audit all layers and reveal the current bottleneck.  
- Browse the full set of 9 skills from the interface.

## How to Use the Skills

### Start broad (when the problem layer is unclear)
- Redesign onboarding: “use the Layers skills to think it through properly.”  
- Resolve team disagreement: “surface what we’re actually disagreeing about.”  
- Diagnose a stuck design: “identify where the real problem is.”  
- Audit mockups: “show assumed decisions and missing ones.”

### Go straight to a layer (when the decision focus is known)
- Convert 12 user interviews into prioritized job stories: **/layers-user-needs**.  
- Model objects, relationships, and vocabulary for a scheduling tool: **/layers-conceptual-model**.  
- Surface edge cases and empty states in a checkout flow: **/layers-interaction-flow**.  
- Map terminology conflicts across product, design, and engineering: **/layers-domain**.

## Output Format
- Decisions are captured as plain‑text markdown and Mermaid diagrams (job stories, strategy trees, object maps, breadboards, decision inventories).  
- Can be sent directly to tools like Linear, Notion, Figma, or GitHub via an MCP connection.

## Example Artifact (Strategy Tree)
```
graph TD
 O["Outcome: increase weekly active use"]
 O --> Op1["Opp — first run: 'I can't tell yet<br/>if this is worth setting up'"]
 O --> Op2["Opp — first task: 'doing this by hand<br/>is faster than learning the tool'"]
 Op1 --> B1["Bet: show value before signup"]
 Op2 --> B2["Bet: pre-filled defaults"]
```
- Prioritized bet: show value before signup.  
- Risk: cold visitors may not engage enough to surface real value.  
- Validation: cohort A/B on signup conversion + qualitative session review.  
- Linked needs: `#user-needs/onboarding-momentum`.

## About the Framework
- The Layers framework models product design as seven layers across three zones, created by Jamie Mill.  
- The AI skills make this framework executable inside the designer’s existing AI tools.
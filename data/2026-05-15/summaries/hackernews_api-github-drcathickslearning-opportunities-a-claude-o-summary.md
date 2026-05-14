---
title: GitHub - DrCatHicks/learning-opportunities: A Claude or Codex skill for deliberate skill development during AI-assisted coding · GitHub
url: https://github.com/DrCatHicks/learning-opportunities
date: 2026-05-14
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-15T06:00:57.940356
---

# GitHub - DrCatHicks/learning-opportunities: A Claude or Codex skill for deliberate skill development during AI-assisted coding · GitHub

# Learning Opportunities: A Claude and Codex Skill for Deliberate Skill Development  

## Overview  
- Provides an adaptive “dynamic textbook” that inserts short (10‑15 min) learning exercises after significant coding actions.  
- Exercises are grounded in evidence‑based learning science (prediction, generation, retrieval practice, spaced repetition).  
- Designed to complement the **Learning‑Goal** skill, which uses Mental Contrasting with Implementation Intentions (MCII) for goal‑setting.  

## Installation  

### Codex  
- Add from GitHub: `codex plugin marketplace add https://github.com/DrCatHicks/learning-opportunities.git`  
- Local install: `codex plugin marketplace add /path/to/learning-opportunities`  
- Includes three plugins:  
  1. `learning‑opportunities` – core skill  
  2. `learning‑opportunities‑auto` – optional post‑commit hook  
  3. `orient` – repo‑orientation generator  

### Claude Code  
1. Add marketplace entry: `marketplace:/plugin marketplace add https://github.com/DrCatHicks/learning-opportunities.git`  
2. Install: `plugin install learning-opportunities@learning‑opportunities`  
3. Restart Claude Code.  

### Optional Components  
- **Auto prompting** (`learning‑opportunities‑auto`): automatically offers an exercise after each git commit (Linux/macOS native; Windows with extra setup).  
- **Repo orientation** (`orient`): create `orientation.md` with suggested lessons; invoke via `/orient` or `/orient showboat`, then `/learning‑opportunities orient` for two targeted lessons.  

## Rationale  

AI‑assisted coding can undermine learning by:  
1. **Generation effect** – reliance on generated code reduces active problem solving.  
2. **Fluency illusion** – clean output creates false confidence.  
3. **Spacing effect** – rapid output encourages cramming, not spaced practice.  
4. **Metacognition** – fast workflows limit self‑monitoring and schema building.  
5. **Testing & retrieval** – full answers reduce opportunities for self‑testing.  

The skill re‑introduces:  
- Active generation (predictions, sketches)  
- Retrieval practice (self‑testing, teach‑back)  
- Deliberate pauses (spacing, reflection)  
- Explicit metacognition (self‑assessment, gap identification)  

## How It Works  

1. After user‑defined “significant work” (new files, schema changes, refactors, unfamiliar patterns, etc.), Claude prompts:  
   *“Would you like a quick learning exercise on [topic]? About 10‑15 minutes.”*  
2. If accepted, Claude runs an interactive exercise, pausing for user input rather than delivering a full answer.  
3. Suppression rules:  
   - No prompt if the user already declined an exercise in the current session.  
   - No more than two exercises are offered per session.  

### Exercise Types  
- **Prediction → Observation → Reflection**  
- **Generation → Comparison**  
- **Trace the Path** (step‑by‑step execution)  
- **Debug This** (anticipate failures)  
- **Teach It Back** (explain to a newcomer)  
- **Retrieval Check‑in** (recall from previous session)  

## Scientific Foundations & Resources  
- Exercises are built on established learning‑science principles (generation effect, retrieval practice, spaced repetition).  
- Design informed by qualitative interviews with developers about pain points in rapid agentic coding.  
- Further reading listed in `SKILL.md` and the bibliography linked from the `orient` plugin.
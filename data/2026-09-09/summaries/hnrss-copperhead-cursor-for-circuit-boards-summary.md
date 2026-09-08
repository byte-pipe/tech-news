---
title: copperhead. Cursor for circuit boards.
url: https://copperhead.sh/
date: 2026-09-08
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-09-09T08:37:39.313085
---

# copperhead. Cursor for circuit boards.

# Copperhead – AI‑driven platform for circuit‑board design

## Overview
- Open‑source AI engineering platform that assists hardware teams in designing, verifying, and shipping printed circuit boards (PCBs).  
- Provides a command‑line interface (CLI) that integrates with KiCad and runs locally; a cloud version is also available.  
- Backed by investors and partners such as Microsoft for Startups, Google for Startups, Activate, Clerk, Supabase, Google Workspace, Sarvam AI, and Hugging Face.  

## Key Features
- **AI‑guided workflow**: Executes eight sequential stages (spec, architecture, parts list, schematic, layout, outputs, firmware, dev‑plan), each acting as a gate that must succeed before the next begins.  
- **Real‑time verification**: Uses KiCad’s ERC/DRC checks; edits are only applied after a validated change proposal passes all constraints.  
- **Traceable decisions**: Records every design decision and change in `DECISIONS.md` and `CHANGELOG.md`.  
- **Surgical edits**: Modifies KiCad’s s‑expression source directly, keeping diffs small and reviewable.  
- **Documentation sync**: Updates all related markdown docs automatically to stay consistent with the schematic and BOM.  

## Example Workflow
1. Install CLI: `npm i -g copperhead`.  
2. Provide a brief (e.g., add a USB‑C power input).  
3. Copperhead reads relevant docs, validates the change, edits schematic and documentation, runs ERC, checks drift, and logs the decision.  
4. The process completes in seconds, producing clean ERC/DRC results and a committed git snapshot.  

## Pricing Model
- **CLI (Free, Apache‑2.0)**: Run locally on your machine, bring your own Claude or GPT‑5 API key; no metering, community support.  
- **Cloud ($49 per user / month)**: Hosted runs, private repos, web viewer, one‑click export of Gerbers/DXF/STEP, managed inference credits.  
- **Team ($49 per user / month + $199 / month platform)**: Adds CI integration, shared libraries, SSO/SAML, central billing, shared run history.  
- **Enterprise (Custom annual)**: Self‑hosted or VPC deployment, Altium support, RBAC, dedicated SLA, flat annual license, audit‑trail compliance.  

## Frequently Asked Questions
- **What is Copperhead?**  
  An open‑source AI agent that edits KiCad files, updates documentation, and runs KiCad’s own checks to keep design and docs in sync.  

- **Problem it solves:**  
  Prevents “drift” where decisions become inconsistent across schematic, BOM, power budget, and docs, avoiding costly respins.  

- **Installation requirements:**  
  Node 20+, KiCad with `kicad-cli` on PATH, and an API key for the language model.  

- **Works on existing designs?**  
  Yes – point it at a KiCad repository, run `copperhead init`, then request changes.  

- **What does it refuse to do?**  
  Operates only on a clean git tree, rejects unvalidated proposals, blocks changes that violate documented constraints, and never invents undocumented part numbers.  

- **Will it rewrite the whole schematic?**  
  No – only makes targeted, minimal edits, preserving unchanged sections byte‑identical.  

## Getting Started
```bash
npm i -g copperhead
export ANTHROPIC_API_KEY=<api-key>
copperhead create --brief brief.md
```  
Create a `brief.md` describing the desired board (e.g., a pocket‑size ESP32‑S3 Bluetooth speaker) and let Copperhead generate the complete, verified design package.
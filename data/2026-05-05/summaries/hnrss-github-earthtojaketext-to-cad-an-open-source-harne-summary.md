---
title: GitHub - earthtojake/text-to-cad: An open source harness for generating CAD models · GitHub
url: https://github.com/earthtojake/text-to-cad
date: 2026-05-01
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-05-05T00:53:23.251017
---

# GitHub - earthtojake/text-to-cad: An open source harness for generating CAD models · GitHub

# Open Source Text‑to‑CAD Harness  

## Overview  
- Repository **earthtojake/text-to-cad** provides a framework for generating 3D CAD models using coding agents such as Codex and Claude Code.  
- All operations run locally; no external backend is required.  

## Features  
- **Generate**: Create source‑controlled CAD models via coding agents.  
- **Export**: Output STEP, STL, 3MF, DXF, GLB, topology data, and URDF robot descriptions.  
- **Browse**: View geometry in the integrated CAD Explorer.  
- **Reference**: Use stable `@cad[…]` handles for precise follow‑up edits.  
- **Review**: Produce quick‑render images for iteration checks.  
- **Reproduce**: Edit source files first, then regenerate explicit targets.  
- **Local**: Run the harness and explorer entirely on the local machine.  

## Bundled Skills  
| Skill | Capabilities | Availability |
|-------|--------------|--------------|
| CAD Skill | STEP, STL, 3MF, DXF, GLB, topology, image rendering, `@cad[…]` geometry references | Bundled + standalone repo |
| URDF Skill | Generate URDF XML, robot links/joints/limits, validation, mesh references | Bundled + standalone repo |
| Robot Motion Skill | ROS 2/MoveIt setup, motion artifacts, inverse kinematics, path planning, motion‑server testing | Bundled |

- Skills are stored under `.agents/skills` for Codex; Claude Code compatibility is provided via symlinks in `.claude/skills`.  

## Workflow  
1. **Describe** the desired part, assembly, fixture, robot, or mechanism.  
2. **Edit**: Let the coding agent modify repository‑local CAD source files.  
3. **Regenerate** explicit export targets (STEP, STL, etc.).  
4. **Inspect** the result with CAD Explorer.  
5. **Reference** geometry using `@cad[…]` handles for further edits.  
6. **Commit** source and generated artifacts together.  

## Benchmarks  
- Assets are stored in `.assets/**` via Git LFS and excluded from default pulls.  
- To fetch benchmark assets locally:  
  ```bash
  git lfs pull --include=".assets/benchmarks/**"
  ```  

## Quick Start  
```bash
git clone https://github.com/earthtojake/text-to-cad.git
cd text-to-cad

# Python environment
python3.11 -m venv .venv
./.venv/bin/python -m pip install --upgrade pip
./.venv/bin/pip install -r .agents/skills/cad/requirements.txt

# Optional URDF skill
./.venv/bin/pip install -r .agents/skills/urdf/requirements.txt

# CAD Explorer (Node)
npm --prefix .agents/skills/cad/explorer install
npm --prefix .agents/skills/cad/explorer run dev   # then open http://localhost:4178
```  

## About & Licensing  
- Purpose: Provide an open‑source harness for CAD model generation driven by AI agents.  
- License: MIT.  

## Topics  
- AI, robotics, WebAssembly, STL, CAD, mechanical engineering, DXF, GLB, OpenCascade, STEP, 3MF, AI agents, Build123d, text‑to‑CAD, CAD skill.
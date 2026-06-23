---
title: GitHub - OpenCut-app/OpenCut: The open-source CapCut alternative · GitHub
url: https://github.com/OpenCut-app/OpenCut
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-06-23T10:22:04.619245
---

# GitHub - OpenCut-app/OpenCut: The open-source CapCut alternative · GitHub

# OpenCut

## Overview
- Free and open‑source video editor targeting web, desktop, and mobile platforms.  
- Positioned as an open‑source alternative to CapCut.  

## Current Status
- The project is undergoing a complete rewrite.  
- Upcoming features include:  
  - Editor API  
  - First‑class third‑party plugins via a plugin‑first architecture  
  - Unified codebase (Rust core) for desktop, mobile, and browser  
  - MCP server for AI agents  
  - Headless mode for automation and batch rendering  
  - Integrated scripting tab in the editor  
- Classic version remains available at `opencut-app/opencut-classic` and runs on `opencut.app`.  
- The rewritten version will be hosted at `new.opencut.app` once ready.  

## Development Setup
1. Install **proto** (if not already installed):  
   ```bash
   <(curl -fsSL https://moonrepo.dev/install/proto.sh)
   ```  
2. From the repository root, run:  
   ```bash
   proto use   # installs bun + moon at pinned versions
   bun install
   ```  
3. Start development servers:  
   - Web UI: `moon run web:dev` → http://localhost:5173  
   - API: `moon run api:dev` → http://localhost:8787  

## Contribution
- External contributions are not accepted while the new architecture is being designed.  
- Interested individuals can follow progress, ask questions, or chat on the Discord server or by opening an issue.  

## Sponsors
- Supported by companies that back open‑source creator tools, e.g., **fal.ai** (generative image, video, and audio models).  
- Sponsorship inquiries: `sponsor@opencut.app`.  

## License
- Distributed under the MIT License.  

## Repository Statistics
- Stars: 58.8 k  
- Forks: 6.4 k  
- Watchers: 285  
- Primary languages: TypeScript (≈ 97.9 %), CSS (≈ 2.1 %).  

## Topics
- editor  
- open‑source software (oss)  
- video editor
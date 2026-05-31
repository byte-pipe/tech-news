---
title: GitHub - github/docs: The open-source repo for docs.github.com · GitHub
url: https://github.com/github/docs
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-06-01T04:19:13.796357
---

# GitHub - github/docs: The open-source repo for docs.github.com · GitHub

# GitHub Docs Repository Summary

## Overview
- Open‑source repository powering **docs.github.com**.  
- Documentation and site‑building code are hosted together.  
- Dual licensing:  
  - Creative Commons Attribution 4.0 for documentation content (assets, content, data).  
  - MIT License for code (see LICENSE‑CODE).

## Repository Structure
- Core directories: `.devcontainer`, `.github`, `.vscode`, `assets`, `config`, `content`, `contributing`, `data`, `patches`, `src`.  
- Key configuration files: `.dockerignore`, `.editorconfig`, `.env.example`, `.gitattributes`, `.gitignore`, `.npmrc`, `.nvmrc`, `.prettierignore`, `CHANGELOG.md`, `Dockerfile`, `LICENSE`, `README.md`, `docker‑compose.yaml`, `eslint.config.ts`, `next.config.ts`, `package.json`, `tsconfig.json`, `vitest.config.ts`.  
- Only **Markdown files** in `/content` and selected reusable data sections are open for external edits; infrastructure, workflows, and build scripts are restricted.

## Contribution Model
- Two synchronized repositories:  
  - `github/docs` (public, accepts external contributions).  
  - `github/docs-internal` (private, for GitHub employee work).  
- Sync occurs frequently; changes in one repo appear in the other.  
- External contributors should modify only documentation files; internal contributors handle infrastructure and code.  
- Quick‑start resources for newcomers:  
  - Finding open‑source contribution opportunities.  
  - Setting up Git.  
  - Understanding GitHub flow.  
  - Collaborating via pull requests.

## Contributor Guidance
- **Hubbers (GitHub employees)**: follow `CONTRIBUTING.md` in the docs‑content repository for internal processes.  
- **Open‑source contributors**: follow `CONTRIBUTING.md` in this repository for a concise onboarding guide.

## Statistics
- Stars: 19.7 k  
- Watchers: 3.2 k  
- Forks: 67.3 k  
- Primary language distribution: TypeScript ≈ 97 %, SCSS ≈ 1.5 %, other ≈ 1.4 %.

## Additional Resources
- License files: `LICENSE` (CC‑BY‑4.0) and `LICENSE‑CODE` (MIT).  
- Included: Code of conduct, security policy, contribution guidelines.
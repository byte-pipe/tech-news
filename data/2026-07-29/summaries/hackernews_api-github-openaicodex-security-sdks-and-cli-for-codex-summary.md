---
title: GitHub - openai/codex-security: SDKs and CLI for Codex Security · GitHub
url: https://github.com/openai/codex-security
date: 2026-07-29
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-07-29T12:29:45.060820
---

# GitHub - openai/codex-security: SDKs and CLI for Codex Security · GitHub

# Codex Security Repository Overview

## Overview
- `@openai/codex-security` provides a CLI and a TypeScript SDK to detect, validate, and remediate security vulnerabilities in codebases.  
- Supports repository scanning, change review, historical tracking of findings, and integration into CI pipelines.  
- Documentation, contribution guidelines, and licensing are included in the repository.

## Quick Start
- Prerequisites: Node.js 22+, Python 3.10+, and access to Codex Security.  
- Installation and initial scan:
  ```bash
  npm install @openai/codex-security
  npx codex-security login
  npx codex-security scan .
  ```
- For CI environments, set `OPENAI_API_KEY` (or `CODEX_API_KEY`) instead of interactive login.

## Authentication
- Scans can use either a ChatGPT sign‑in or an API key.  
- Interactive scans prompt when both credentials are present; non‑interactive scans default to the API key.  
- Explicit credential selection:
  ```bash
  npx codex-security scan . --auth chatgpt
  npx codex-security scan . --auth api-key
  ```
- To make ChatGPT sign‑in the default, unset any configured API keys:
  ```bash
  unset OPENAI_API_KEY CODEX_API_KEY
  ```

## CI Integration
- Set the appropriate environment variable (`OPENAI_API_KEY` or `CODEX_API_KEY`) for automated, non‑interactive scans.  
- The tool respects the API‑key precedence in CI contexts.

## State Management
- Scan history is stored in the Codex Security workbench state directory.  
- If the default directory is not writable, define `CODEX_SECURITY_STATE_DIR` to point to a writable location outside the repository.

## TypeScript SDK Usage
```typescript
import { CodexSecurity } from "@openai/codex-security";

const security = new CodexSecurity();
const result = await security.run(".");
console.log(result.reportPath);
await security.close();
```
- The SDK follows the same installation, authentication, and option conventions as the CLI; refer to the official documentation for details.

## Repository Structure
- Key directories and files:
  - `.github/workflows/` – CI workflow definitions.  
  - `docker/` – Docker configuration for containerized usage.  
  - `sdk/typescript/` – Source code for the TypeScript SDK.  
  - `README.md`, `SECURITY.md`, `CONTRIBUTING.md` – Project documentation and contribution guidelines.  
  - `Dockerfile`, `compose.yaml` – Container build and orchestration files.  

## Contribution & Licensing
- Contributions are welcomed; see `CONTRIBUTING.md` for guidelines.  
- The project is released under the license specified in `LICENSE`.
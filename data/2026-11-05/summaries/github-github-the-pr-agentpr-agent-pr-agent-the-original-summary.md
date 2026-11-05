---
title: GitHub - The-PR-Agent/pr-agent: 🚀 PR Agent: The Original Open-Source PR Reviewer. This project is not the Qodo free tier. · GitHub
url: https://github.com/The-PR-Agent/pr-agent
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-11-05T15:25:04.205369
---

# GitHub - The-PR-Agent/pr-agent: 🚀 PR Agent: The Original Open-Source PR Reviewer. This project is not the Qodo free tier. · GitHub

# PR‑Agent Repository Overview

## Getting Started
- **GitHub Action (recommended)**  
  Add a workflow file `.github/workflows/pr-agent.yml` that runs on pull‑request events and uses `the-pr-agent/pr-agent@main`. Provide `OPENAI_KEY` and `GITHUB_TOKEN` as secrets.
- **CLI usage (local development)**  
  ```bash
  pip install "pr-agent[github]"
  export OPENAI_KEY=your_key_here
  pr-agent --pr_url https://github.com/owner/repo/pull/123 review
  ```  
  Optional provider SDKs can be installed via `pr-agent[all]`.
- **Other platforms**  
  Supports GitLab webhooks, Bitbucket app installation, and Azure DevOps integration.

## Why Use PR‑Agent
- **Fast & affordable** – each tool makes a single LLM call (~30 seconds, low cost).  
- **Handles any PR size** – PR compression strategy processes both small and large changes.  
- **Highly customizable** – JSON‑based prompting lets you adjust review categories and behavior.  
- **Platform agnostic**  
  - Git providers: GitHub, GitLab, BitBucket, Azure DevOps, Gitea.  
  - Deployment: CLI, GitHub Actions, Docker, self‑hosted, webhooks.  
  - AI models: OpenAI GPT, Anthropic Claude, Google Gemini, DeepSeek, Mistral, and any model reachable via LiteLLM (Azure OpenAI, AWS Bedrock, Vertex AI, Databricks, OpenRouter, Ollama, etc.).  
- **Open‑source benefits** – full control over data and infrastructure, no vendor lock‑in, community‑driven development.

## Features
- Tools include `/describe`, `/review`, `/improve`, `/ask`, `/similar_issue`.  
- `/help_docs` is temporarily disabled (v0.36.1) due to a credential‑exposure issue.

## Usage Examples
- **Comment on a PR** (GitHub/GitLab/Bitbucket/etc.)  
  ```
  /describe
  /review
  /improve
  /ask "What does this PR change?"
  ```
- **Issue‑scoped command**  
  ```
  /similar_issue   # finds similar issues in the repository
  ```
- **CLI commands**  
  ```
  pr-agent --pr_url <PR_URL> review
  pr-agent --issue_url <ISSUE_URL> similar_issue
  ```

## How It Works
A diagram (in the documentation) shows the flow of PR‑Agent tools from trigger to LLM response and comment posting.

## Data Privacy
When self‑hosted with your own OpenAI API key, data is exchanged only between you and OpenAI. Refer to OpenAI’s enterprise privacy policy for details.

## Contributing
- Follow the project’s Contributing Guide.  
- Run unit tests: `PYTHONPATH=. uv run pytest`.  
- Run end‑to‑end tests (require provider credentials) explicitly, e.g., `PYTHONPATH=. uv run pytest tests/e2e_tests/test_github_app.py`.

## Recent News
- PR‑Agent has been donated to the open‑source community and now lives under the `pr-agent` GitHub organization.  
- Documentation moved to `docs.pr-agent.ai`.  
- The former hosted version (Qodo 1.0) has been rebranded as Qodo 2.0, a full AI code‑review platform.

## Community & Sponsors
- Sponsored by the free version of Qodo for open‑source projects (Gold Sponsor).  
- First external maintainer: Naor (@naorpeled).  
- Ongoing development is community‑maintained with additional sponsorship welcomed.
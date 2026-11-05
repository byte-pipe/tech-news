---
title: 'GitHub - The-PR-Agent/pr-agent: 🚀 PR Agent: The Original Open-Source PR Reviewer. This project is not the Qodo free tier. · GitHub'
url: https://github.com/The-PR-Agent/pr-agent
site_name: github
content_file: github-github-the-pr-agentpr-agent-pr-agent-the-original
fetched_at: '2026-11-05T15:23:36.423300'
original_url: https://github.com/The-PR-Agent/pr-agent
author: The-PR-Agent
description: '🚀 PR Agent: The Original Open-Source PR Reviewer. This project is not the Qodo free tier. - The-PR-Agent/pr-agent'
---

Use this GitHub action with your project
Add this Action to an existing workflow or create a new one
View on Marketplace
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

6,358 Commits
6,358 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
docker
docker
 
 
docs
docs
 
 
github_action
github_action
 
 
pr_agent
pr_agent
 
 
scripts
scripts
 
 
tests
tests
 
 
.dockerignore
.dockerignore
 
 
.gitignore
.gitignore
 
 
.pr_agent.toml
.pr_agent.toml
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.python-version
.python-version
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile.github_action_dockerhub
Dockerfile.github_action_dockerhub
 
 
LICENSE
LICENSE
 
 
MANIFEST.in
MANIFEST.in
 
 
README.md
README.md
 
 
RELEASE_NOTES.md
RELEASE_NOTES.md
 
 
SECURITY.md
SECURITY.md
 
 
action.yaml
action.yaml
 
 
codecov.yml
codecov.yml
 
 
pr_compliance_checklist.yaml
pr_compliance_checklist.yaml
 
 
pyproject.toml
pyproject.toml
 
 
setup.py
setup.py
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

The Original Open-Source PR Reviewer

This repository contains the open-source PR Agent Project.
It is not the Qodo offering for open-source projects.

PR-Agent is an open-source, AI-powered code review agent and a community-maintained legacy project of Qodo. It is distinct from Qodo's primary AI code review offering, which provides a feature-rich, context-aware experience. Qodo offers a free version for open-source projects and integrates seamlessly with GitHub, GitLab, Bitbucket, and Azure DevOps for high-quality automated reviews.

## Sponsors

PR-Agent is a community-maintained open-source project, with its ongoing development supported by our sponsors. If you'd like to support the project, considerbecoming a sponsor.

### 🥇 Gold Sponsor

Free version of Qodo for open-source projects

## Table of Contents

* Getting Started
* Why Use PR-Agent?
* Features
* See It in Action
* How It Works
* Data Privacy
* Contributing

## Getting Started

Note

Docker Hub namespace migration.Releases0.34.2and later are published underpragent/pr-agent. Older releases (up to and includingv0.31) remain available at the legacycodiumai/pr-agentnamespace as a frozen archive — no new images are pushed there. Update any pinnedimage:/docker pull/uses: docker://references when upgrading to0.34.2+.

### 🚀 Quick Start for PR-Agent

#### 1. GitHub Action (Recommended)

Add automated PR reviews to your repository with a simple workflow file:

#
 .github/workflows/pr-agent.yml

name
: 
PR Agent

on
:
 
pull_request
:
 
types
: 
[opened, synchronize]

jobs
:
 
pr_agent_job
:
 
runs-on
: 
ubuntu-latest

 
steps
:
 - 
name
: 
PR Agent action step

 
uses
: 
the-pr-agent/pr-agent@main

 
env
:
 
OPENAI_KEY
: 
${{ secrets.OPENAI_KEY }}

 
GITHUB_TOKEN
: 
${{ secrets.GITHUB_TOKEN }}

Full GitHub Action setup guide

#### 2. CLI Usage (Local Development)

Run PR-Agent locally on your repository:

pip install 
"
pr-agent[github]
"

export
 OPENAI_KEY=your_key_here
pr-agent --pr_url https://github.com/owner/repo/pull/123 review

Git provider SDKs are optional extras: install the one for your provider (list), orpr-agent[all]for every integration.Complete CLI setup guide

#### 3. Other Platforms

* GitLab webhook setup
* BitBucket app installation
* Azure DevOps setup

## News and Updates

Full notes for every release are on theReleases page.

## Why Use PR-Agent?

### 🎯 Built for Real Development Teams

Fast & Affordable: Each tool (/review,/improve,/ask) uses a single LLM call (~30 seconds, low cost)

Handles Any PR Size: OurPR Compression strategyeffectively processes both small and large PRs

Highly Customizable: JSON-based prompting allows easy customization of review categories and behavior viaconfiguration files

Platform Agnostic:

* Git Providers: GitHub, GitLab, BitBucket, Azure DevOps, Gitea
* Deployment: CLI, GitHub Actions, Docker, self-hosted, webhooks
* AI Models: OpenAI GPT, Anthropic Claude, Google Gemini, DeepSeek, Mistral, and any other model reachable through LiteLLM (Azure OpenAI, AWS Bedrock, Vertex AI, Databricks, OpenRouter, Ollama, and more) — seeChanging a model

Open Source Benefits:

* Full control over your data and infrastructure
* Customize prompts and behavior for your team's needs
* No vendor lock-in
* Community-driven development

## Features

See the currentfeature and git provider support matrixin the PR-Agent documentation.

⚠️/help_docsis temporarily disabled sincev0.36.1pending a fix for a credential-exposure issue (#2445).

## See It in Action

#### /describe

#### /review

#### /improve

### Usage Examples

PR-Agent tools run as a comment on a PR or from the CLI. A few common ones:

#
 Comment on a PR (GitHub/GitLab/Bitbucket/…):

/describe
/review
/improve
/ask 
"
What does this PR change?
"
 
#
 free-text Q&A about the PR

#
 Issue-scoped commands run on an issue instead of a PR:

/similar_issue 
#
 find similar issues in the repository

#
 Or locally via the CLI:

pr-agent --pr_url 
<
PR_URL
>
 review
pr-agent --issue_url 
<
ISSUE_URL
>
 similar_issue

See theTools docsfor the full list of tools with example commands, and each tool's page for screenshots and options.

## How It Works

The following diagram illustrates PR-Agent tools and their flow:

## Data Privacy

### Self-hosted PR-Agent

* If you host PR-Agent with your OpenAI API key, it is between you and OpenAI. You can read their API data privacy policy here:https://openai.com/enterprise-privacy

## Contributing

To contribute to the project, get started by reading ourContributing Guide.

For local verification, runPYTHONPATH=. uv run pytestfrom the repository root; it discovers the unit-test suite undertests/unittestby default. End-to-end tests undertests/e2e_testsrequire provider credentials and should be invoked explicitly, for examplePYTHONPATH=. uv run pytest tests/e2e_tests/test_github_app.py.

## Big News for PR-Agent

PR-Agent has a new home!

After years of building this tool alongside the community, Qodo has donated PR-Agent to the open-source community - and we couldn't be more excited about what comes next.

The project now lives in the PR-Agent org on GitHub, is fully community-owned, and is open for contributions and additional maintainers.

What else changed:

* Docs moved to -docs.pr-agent.ai
* Qodo Merge (Qodo 1.0), the hosted URL, which was the enterprise version of PR-Agent, has been rebranded and evolved into Qodo (Qodo 2.0), a full AI code review platform.

## ❤️ Community

This open-source release remains here as a community contribution from Qodo — the origin of modern AI-powered code collaboration. We’re proud to share it and inspire developers worldwide.

The project now has its first external maintainer, Naor (@naorpeled), and is currently in the process of being donated to an open-source foundation.
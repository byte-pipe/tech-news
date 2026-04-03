---
title: Automate Your GitHub Workflow with Gemini CLI - DEV Community
url: https://dev.to/gde/automate-your-github-workflow-with-gemini-cli-4p4e
date: 2026-01-11
site: devto
model: llama3.2:1b
summarized_at: 2026-01-13T11:14:58.641140
screenshot: devto-automate-your-github-workflow-with-gemini-cli-dev.png
---

# Automate Your GitHub Workflow with Gemini CLI - DEV Community

**Automate Your GitHub Workflow with Gemini CLI - DEV Community**

### Meet Your New AI Coding Partner

The Google team has introduced a new AI coding teammate called Gemini CLI GitHub Action, which can automatically triage issues, fix bugs, and review pull requests directly within your GitHub repository.

### Key Capabilities

* **Issue Triage**: Labels issues (bug, feature, etc.) with ease
* **Code Fixes**: Analyzes issues and writes code to solve them
* **Pull Request Reviews**: Provides automated code reviews with suggestions

### Setup Guide

**Step 1: Install and Update Gemini CLI**

Install the latest version of Gemini CLI from [official installation guide](https://github.com/minimaxir/Gemini-cli-documentation).

**Step 2: Set Up the GitHub Action**

Run `gemini setup github` in your project directory, then enter fullscreen mode. The action is added to your repository's `.github/workflows` directory.

**Step 3: Commit and Push**

Commit all files and push them to GitHub.

### Step 4: Add Your Gemini API Key

* Go to your GitHub repository
* Click [*Settings*]*[Settings]
* Navigate to [*Security*] → [*Secrets and Variables*] → [*Actions*]
* Click [*New repository secret*]*Gemini_API_KEY*
* Name it, then for the value, get your API key from Google AI Studio.

### Full Review

To watch the setup video on YouTube [here](https://www.youtube.com/watch?v=6uL8pE-jXoU).

Note: This guide assumes you have basic familiarity with GitHub repositories and command line basics. Additionally, make sure to be comfortable managing issues and pull requests in a GitHub repository.

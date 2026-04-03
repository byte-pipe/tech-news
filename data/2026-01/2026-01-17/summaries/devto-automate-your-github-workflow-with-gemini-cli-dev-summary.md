---
title: Automate Your GitHub Workflow with Gemini CLI - DEV Community
url: https://dev.to/gde/automate-your-github-workflow-with-gemini-cli-4p4e
date: 2026-01-11
site: devto
model: llama3.2:1b
summarized_at: 2026-01-17T11:13:54.354200
screenshot: devto-automate-your-github-workflow-with-gemini-cli-dev.png
---

# Automate Your GitHub Workflow with Gemini CLI - DEV Community

**Automate Your GitHub Workflow with Gemini CLI: A New AI Coding Partner**

### Introduction

Google introduced a new AI coding teammate called Gemini CLI GitHub Action, which can automate tasks such as issue triage, bug fixes, and pull request reviews directly in your GitHub repository.

### What Does it Do?

1. **Issue Triage**: Automatically labels issues (bug, feature) and assigns them to developers.
2. **Code Fixes**: Analyzes issues and writes code to solve them.
3. **Pull Request Reviews**: Provide automated code reviews with suggestions for improvement.

### Setup Guide

To set up the Gemini CLI GitHub Action:

1. **Install and Update Gemini CLI**: Ensure you have the latest version of Gemini CLI installed and updated.
2. **Set Up the GitHub Action**: Run `gemini setup github` in your project directory, enter fullscreen mode and exit it afterwards.
3. **Commit and Push**: Commit all files and push them to GitHub.
4. **Add Gemini API Key**: Go to your repository settings, add a new secret called `GEMINI_API_KEY`, get the value from Google AI Studio.

### Example Usage

Walk through a basic example of using the Gemini CLI GitHub Action on a personal Flutter project:

* Create the necessary files and push changes to the repository.
* Run `gemini setup github` in your project directory and enter fullscreen mode.
* Exits fullscreen mode, resulting in new issues being automatically labeled as "bug," "feature," or other relevant categories.

By following these steps and tips, you can experience the benefits of automating routine GitHub tasks with Gemini CLI GitHub Action.

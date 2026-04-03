# Automating GitHub Workflow with Gemini CLI

## Introduction
Gemini CLI GitHub Action is an AI-powered coding teammate designed to operate directly within your GitHub repository. Built by Google and now shared with the community, it automates routine tasks to enhance development efficiency.

## Key Features
The tool provides three core automation capabilities:

| Feature                | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| Issue Triage           | Automatically labels issues (e.g., `bug`, `feature`)                       |
| Code Fixes             | Analyzes issues and generates code fixes                                    |
| Pull Request Reviews   | Provides automated code reviews with actionable suggestions                 |

## Requirements
Before implementation, ensure familiarity with:
- GitHub repository creation and management
- Basic command line operations
- Git repository configuration

## Setup Guide

### Step 1: Install Gemini CLI
Ensure the latest Gemini CLI version is installed in your environment.

### Step 2: Configure GitHub Action
1. Navigate to your project directory
2. Execute: `gemini setup github`
3. Enter fullscreen mode and exit

### Step 3: Commit and Push Changes
- Commit all generated files
- Push to your GitHub repository

### Step 4: Add API Key
1. Go to repository **Settings > Security > Secrets and Variables > Actions**
2. Create new secret:
   - Name: `GEMINI_API_KEY`
   - Value: Your Google AI Studio API key

## Expected Outcome
The Gemini CLI GitHub Action will:
- Operate 24/7 as your dedicated AI coding assistant
- Automate routine tasks without manual intervention
- Maintain consistent assistance across all repository operations

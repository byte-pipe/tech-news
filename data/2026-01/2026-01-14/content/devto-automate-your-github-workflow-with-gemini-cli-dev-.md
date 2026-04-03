---
title: Automate Your GitHub Workflow with Gemini CLI - DEV Community
url: https://dev.to/gde/automate-your-github-workflow-with-gemini-cli-4p4e
site_name: devto
fetched_at: '2026-01-14T11:08:03.353112'
original_url: https://dev.to/gde/automate-your-github-workflow-with-gemini-cli-4p4e
author: Daniel Gwerzman
date: '2026-01-11'
description: 'Automate Your GitHub Workflow: Meet Your New AI Coding Partner Google dropped something... Tagged with ai, geminicli, git, gemini.'
tags: '#ai, #geminicli, #git, #gemini'
---

### Automate Your GitHub Workflow: Meet Your New AI Coding Partner

Google dropped something that caught my attention back at Cloud Next 25 Tokyo: a new AI coding teammate that lives directly in your GitHub repository. It’s called the Gemini CLI GitHub Action, and it can automatically triage issues, fix bugs, and even review your pull requests.

The best part? The Google team built this tool for themselves to handle the flood of requests on their own Gemini CLI repository, and now they’re sharing it with the rest of us. I spent some time testing it on my personal Flutter project, and I want to walk you through exactly how to set it up and what you can expect.

### What Exactly Does This Tool Do?

Before we dive into setup, let’s clarify what we’re working with. The Gemini CLI GitHub Action gives you three main capabilities:

* Issue Triage: It reads new issues and automatically labels them (bug, feature, etc.)
* Code Fixes: It can analyze issues and write code to solve them
* Pull Request Reviews: It provides automated code reviews with suggestions

Think of it as having an AI developer on your team that works 24/7, never gets tired, and can handle the routine tasks that eat up your time.

Full review on Youtube

### Prerequisites: What You Need to Know

This guide assumes you have basic familiarity with:

* GitHub repositories (creating repos, issues, and pull requests)
* Command line basics
* Having a project you can test with

If you’re new to GitHub, spend some time with theirgetting started guidefirst. You’ll need to be comfortable creating issues and managing repositories.

### Step-by-Step Setup Guide

### Step 1: Install and Update Gemini CLI

First, make sure you have the Gemini CLI installed and updated to the latest version. If you don’t have it yet, check theofficial installation guide.

Once installed, verify you’re on the latest version — this is crucial for the GitHub integration to work properly.

### Step 2: Set Up the GitHub Action

Navigate to your project directory and run:

gemini setup github

Enter fullscreen mode

Exit fullscreen mode

This command takes just a few seconds and adds the necessary GitHub Action files to your repository. You’ll see new files in the.github/workflowsdirectory that define how the AI teammate will respond to different events.

### Step 3: Commit and Push

Don’t forget this crucial step! Commit all the new files and push them to GitHub. The actions won’t work until they’re actually in your repository.

git add .
git commit -m "Add Gemini CLI GitHub Actions"
git push

Enter fullscreen mode

Exit fullscreen mode

### Step 4: Add Your Gemini API Key

Here’s the step that’s not immediately obvious from the documentation but is absolutely essential:

1. Go to your GitHub repository
2. Click*Settings*
3. Navigate to*Security* →Secrets and Variables→Actions
4. Click*New repository secret*
5. Name itGEMINI_API_KEY
6. For the value, you’ll need to get your API key from Google AI Studio

To get your API key:

* Openai.devin a new tab
* This takes you to Google AI Studio
* Click*Get API key*
* Select*Create new API key*
* Copy the generated string and paste it as your secret value

### Testing Your New AI Teammate

Now for the fun part! Let’s see what this thing can actually do.

### Testing Issue Triage

I started by creating a new issue in my Flutter shopping list project. Here’s what I wrote:

“When a user hit enter on edit mode of an item, the system will end the edit mode and update as usual. and open a new empty item under the edited item that is focus and ready to be edit.”

Admittedly, this is a pretty vague description , normally I’d provide much more detail when working with AI tools. But I wanted to see how well it handled unclear requirements.

To trigger the triage, I added this comment to the issue:

@gemini-cli triage this issue

Enter fullscreen mode

Exit fullscreen mode

Within a few minutes, the action ran and automatically labeled my issue as a “bug.” Looking at the action logs, I could see exactly how it made this decision — it analyzed the issue description and determined this was describing missing functionality rather than a new feature request.

### Testing Code Fixes

Next came the real test. I commented:

@gemini-cli fix this issue

Enter fullscreen mode

Exit fullscreen mode

This is where things got interesting. The AI spent several minutes analyzing my code, creating a detailed plan with checkboxes, and then implementing the changes. Unlike my usual coding workflow where I see every change being made, this felt completely autonomous. I just watched it work and waited for the results.

The process looked like this:

1. Read and analyze the issue
2. Examine the existing codebase
3. Create a detailed implementation plan
4. Execute the plan step by step
5. Create a new branch with the changes

When it finished, I had a new branch called something like “fix-enter-key-functionality” with actual working code.

### Testing Pull Request Review

The final piece was testing the automated code review. I manually created a pull request from the branch the AI had created (it couldn’t create the PR automatically for some reason).

Almost immediately, another action triggered: the pull request review. After about three minutes, I had a comprehensive code review with:

* A summary of the changes
* Specific feedback on potential issues
* Security and performance considerations
* An overall assessment (in my case, it was marked as low-to-medium risk)

### What Actually Worked (And What Didn’t)

Let’s be honest about the results. The good news: the code actually worked! When I tested my Flutter app, pressing enter while editing an item did indeed update the item and create a new one. The functionality was implemented correctly despite my vague description.

However, there were some limitations:

* The AI had trouble with Flutter/Dart compared to what I’d expect with JavaScript projects (there’s simply more training data available for web technologies)
* It took longer to debug and correct Flutter-specific issues
* The autonomous nature felt strange compared to tools like Cursor where I can approve changes line by line
* It made some unwanted changes to my configuration files
* The pull request creation failed, requiring manual intervention

### Pro Tips for Better Results

Based on my testing, here are some recommendations:

Write Better Issue Descriptions: Even though my vague description worked, you’ll get much better results with detailed requirements, acceptance criteria, and context about your project. And always break it down into small pieces.

Use Different AI Tools for Different Tasks: I recommend using different AI tools for writing code versus reviewing it. For example, if Claude writes the code, use Gemini or another tool for the review. This provides a fresh perspective and catches issues the original tool might miss.

Review the Prompts: One of the best features is that all the prompts are visible and customizable. Check out the.github/workflowsfiles to see exactly what instructions the AI is following, and modify them to match your team's standards.

Start Small: Test this on smaller, non-critical repositories first. Get comfortable with how it works before deploying it on your main projects.

### The Bottom Line: Should You Try It?

Absolutely. Even with its limitations, this tool represents a significant step forward in AI-assisted development. It’s particularly valuable for:

* Solo developers who want help with routine tasks
* Open source maintainers dealing with lots of issues and PRs
* Teams looking to standardize their review process
* Anyone curious about autonomous AI coding

The setup is straightforward, it’s free to use (you just pay for Gemini API usage), and the prompts are completely customizable. Even if you don’t use it as-is, studying the prompts and workflow structure provides excellent insights into effective AI automation.

### Ready to Get Started?

Here’s your action plan:

1. Pick a test repository (not your main project!)
2. Follow the setup steps above
3. Create a simple issue to test triage functionality
4. Try the fix command on something small
5. Experiment with customizing the prompts to match your workflow

Remember, this is still early-stage technology. Approach it with curiosity rather than expecting perfection, and you’ll likely find some genuinely useful automation for your development workflow.

The future of coding is increasingly collaborative between humans and AI. Tools like this give us a glimpse of what that partnership might look like — and honestly, it’s pretty exciting.

Have you tried the Gemini CLI GitHub Action? I’d love to hear about your experience and any creative ways you’ve customized it for your projects.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse

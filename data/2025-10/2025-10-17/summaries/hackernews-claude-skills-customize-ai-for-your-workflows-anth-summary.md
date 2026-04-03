---
title: Claude Skills: Customize AI for your workflows \ Anthropic
url: https://www.anthropic.com/news/skills
date: 2025-10-17
site: hackernews
model: llama3.2:1b
summarized_at: 2025-10-17T11:20:57.205796
screenshot: hackernews-claude-skills-customize-ai-for-your-workflows-anth.png
---

# Claude Skills: Customize AI for your workflows \ Anthropic

# Introducing Agent Skills

## What are Agent Skills?

* **Skills** are folders that include instructions, scripts, and resources to improve specific tasks.
* They allow you to customize AI performance with tailored workflows.

## How Agent Skills Work

1. Claude scans for relevant skills matching your task.
2. When a skill matches, it loads minimal information and files needed while keeping the interface fast.
3. **Skills** are:
	* Composable: stackable
	* Portable: format-dependent
	* Efficient: only loaded what's necessary
	* Powerful: executable code for complex tasks

## Skills Across Multiple Claude Products

### Available to:

* Pro
* Max
* Team and Enterprise users

## Creating Skills

Claude apps and the Developer Platform (API) enable you to create custom skills.

### Skill-Creator Skill

1. Generate folder structure
2. Format SKILL.md file
3. Bundle resources
4. Automatically invoked based on your task

Enabling Skills in Settings is required for Team and Enterprise users.

## Utilizing Agent Skills with Anthropic-Created Skills

* Enable the Code Execution Tool (beta) to run custom agent skills.
* Use new/v1/skillsendpoint to access Skills programmatically.
* Develop custom Skill versions using the API and the Code Execution Tool.

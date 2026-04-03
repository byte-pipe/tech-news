---
title: 'Claude Skills: Customize AI for your workflows \ Anthropic'
url: https://www.anthropic.com/news/skills
site_name: hackernews_api
fetched_at: '2025-10-17T19:08:39.790378'
original_url: https://www.anthropic.com/news/skills
author: meetpateltech
date: '2025-10-16'
description: Build custom Skills to teach Claude specialized tasks. Create once, use everywhere—from spreadsheets to coding. Available across Claude.ai, API, and Code.
tags:
- hackernews
- trending
---

Product

# Introducing Agent Skills

Oct 16, 2025
●
3 min
 read

Claude can now useSkillsto improve how it performs specific tasks. Skills are folders that include instructions, scripts, and resources that Claude can load when needed.

Claude will only access a skill when it's relevant to the task at hand. When used, skills make Claude better at specialized tasks like working with Excel or following your organization's brand guidelines.

You've already seen Skills at work in Claude apps, where Claude uses them to create files like spreadsheets and presentations. Now, you can build your own skills and use them across Claude apps, Claude Code, and our API.

## How Skills work

While working on tasks, Claude scans available skills to find relevant matches. When one matches, it loads only the minimal information and files needed—keeping Claude fast while accessing specialized expertise.

Skills are:

* Composable: Skills stack together. Claude automatically identifies which skills are needed and coordinates their use.
* Portable: Skills use the same format everywhere. Build once, use across Claude apps, Claude Code, and API.
* Efficient: Only loads what's needed, when it's needed.
* Powerful: Skills can include executable code for tasks where traditional programming is more reliable than token generation.

Think of Skills as custom onboarding materials that let you package expertise, making Claude a specialist on what matters most to you. For a technical deep-dive on the Agent Skills design pattern, architecture, and development best practices, read ourengineering blog.

## Skills work with every Claude product

### Claude apps

Skills are available to Pro, Max, Team and Enterprise users. We provide skills for common tasks like document creation, examples you can customize, and the ability to create your own custom skills.

Claude automatically invokes relevant skills based on your task—no manual selection needed. You'll even see skills in Claude's chain of thought as it works.Creating skills is simple. The "skill-creator" skill provides interactive guidance: Claude asks about your workflow, generates the folder structure, formats the SKILL.md file, and bundles the resources you need. No manual file editing required.

Enable Skills inSettings. For Team and Enterprise users, admins must first enable Skills organization-wide.

### Claude Developer Platform (API)

Agent Skills, which we often refer to simply as Skills, can now be added to Messages API requests and the new/v1/skillsendpoint gives developers programmatic control over custom skill versioning and management. Skills require theCode Execution Toolbeta, which provides the secure environment they need to run.

Use Anthropic-created skills to have Claude read and generate professional Excel spreadsheets with formulas, PowerPoint presentations, Word documents, and fillable PDFs. Developers can create custom Skills to extend Claude's capabilities for their specific use cases.

Developers can also easily create, view, and upgrade skill versions through the Claude Console.

Explore thedocumentationorAnthropic Academyto learn more.

“
Skills teaches Claude how to work with Box content. Users can transform stored files into PowerPoint presentations, Excel spreadsheets, and Word documents that follow their organization's standards—saving hours of effort.
“
With Skills, Claude works seamlessly with Notion - taking users from questions to action faster. Less prompt wrangling on complex tasks, more predictable results.
“
Canva plans to leverage Skills to customize agents and expand what they can do. This unlocks new ways to bring Canva deeper into agentic workflows—helping teams capture their unique context and create stunning, high-quality designs effortlessly.
“
Skills streamline our management accounting and finance workflows. Claude processes multiple spreadsheets, catches critical anomalies, and generates reports using our procedures. What once took a day, we can now accomplish in an hour.

### Claude Code

Skills extend Claude Code with your team's expertise and workflows. Install skills via plugins from the anthropics/skills marketplace. Claude loads them automatically when relevant. Share skills through version control with your team. You can also manually install skills by adding them to~/.claude/skills. The Claude Agent SDK provides the same Agent Skills support for building custom agents.

## Getting started

* Claude apps:User Guide&Help Center
* API developers:Documentation
* Claude Code:Documentation
* Example Skills to customize:GitHub repository

## What's next

We're working toward simplified skill creation workflows and enterprise-wide deployment capabilities, making it easier for organizations to distribute skills across teams.

Keep in mind, this feature gives Claude access to execute code. While powerful, it means being mindful about which skills you use—stick to trusted sources to keep your data safe.Learn more.

News

### Claude and your productivity platforms

Oct 16, 2025

News

### Introducing Claude Haiku 4.5

Oct 15, 2025

News

### Anthropic and Salesforce expand partnership to bring Claude to regulated industries

Oct 14, 2025

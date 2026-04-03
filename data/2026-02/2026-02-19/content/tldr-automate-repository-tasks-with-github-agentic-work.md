---
title: Automate repository tasks with GitHub Agentic Workflows - The GitHub Blog
url: https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/
site_name: tldr
content_file: tldr-automate-repository-tasks-with-github-agentic-work
fetched_at: '2026-02-19T19:25:07.754841'
original_url: https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/
author: Don Syme, Peli de Halleux
date: '2026-02-19'
published_date: '2026-02-13T14:00:00+00:00'
description: Build automations using coding agents in GitHub Actions to handle triage, documentation, code quality, and more.
tags:
- tldr
---

Don Syme
 &
Peli de Halleux


			February 13, 2026

|

				8 minutes

* Share:

Imagine visiting your repository in the morning and feeling calm because you see:

* Issues triaged and labelled
* CI failures investigated with proposed fixes
* Documentation has been updated to reflect recent code changes.
* Two new pull requests that improve testing await your review.

All of it visible, inspectable, and operating within the boundaries you’ve defined.

That’s the future powered byGitHub Agentic Workflows: automated, intent-driven repository workflows that run in GitHub Actions, authored in plain Markdown and executed with coding agents. They’re designed for people working in GitHub, from individuals automating a single repo to teams operating at enterprise or open-source scale.

At GitHub Next, we began GitHub Agentic Workflows as an investigation into a simple question: what does repository automation with strong guardrails look like in the era of AI coding agents? A natural place to start was GitHub Actions, the heart of scalable repository automation on GitHub. By bringing automated coding agents into actions, we can enable their use across millions of repositories, while keeping decisions about when and where to use them in your hands.

GitHub Agentic Workflows are now available intechnical preview. In this post, we’ll explain what they are and how they work. We invite you to put them to the test, to explore where repository-level AI automation delivers the most value.

## AI repository automation: A revolution through simplicity

The concept behind GitHub Agentic Workflows is straightforward: you describe the outcomes you want in plain Markdown, add this as an automated workflow to your repository, and it executes using a coding agent in GitHub Actions.

This brings the power of coding agents into the heart of repository automation. Agentic workflows run as standard GitHub Actions workflows, with added guardrails for sandboxing, permissions, control, and review. When they execute, they can use different coding agent engines—such as Copilot CLI, Claude Code, or OpenAI Codex—depending on your configuration.

The use of GitHub Agentic Workflows makes entirely new categories of repository automation and software engineering possible, in a way that fits naturally with how developer teams already work on GitHub. All of them would be difficult or impossible to accomplish traditional YAML workflows alone:

1. Continuous triage: automaticallysummarize, label, and route new issues.
2. Continuous documentation: keepREADMEs and documentation aligned with code changes.
3. Continuous code simplification:repeatedly identify code improvementsand open pull requests for them.
4. Continuous test improvement:assess test coverage and add high-value tests.
5. Continuous quality hygiene: proactivelyinvestigate CI failures and propose targeted fixes.
6. Continuous reporting:create regular reports on repository health, activity, and trends.

These are just a few examples of repository automations that showcase the power of GitHub Agentic Workflows. We call thisContinuous AI: the integration of AI into the SDLC, enhancing automation and collaboration similar to continuous integration and continuous deployment (CI/CD) practices.

GitHub Agentic Workflows and Continuous AI are designed to augment existing CI/CD rather than replace it. They do not replace build, test, or release pipelines, and their use cases largely do not overlap with deterministic CI/CD workflows. Agentic workflows run on GitHub Actions because that is where GitHub provides the necessary infrastructure for permissions, logging, auditing, sandboxed execution, and rich repository context.

In our own usage at GitHub Next, we’re finding new uses for agentic workflows nearly every day. Throughout GitHub, teams have been using agentic workflows to create custom tools for themselves in minutes, replacing chores with intelligence or paving the way for humans to get work done by assembling the right information, in the right place, at the right time. A new world of possibilities is opening for teams and enterprises to keep their repositories healthy, navigable, and high-quality.

## Let’s talk guardrails and control

Designing for safety and control is non-negotiable. GitHub Agentic Workflows implements a defense-in-depth security architecture that protects against unintended behaviors and prompt-injection attacks.

Workflows run with read-only permissions by default. Write operations require explicit approval throughsafe outputs, which map to pre-approved, reviewable GitHub operations such as creating a pull request or adding a comment to an issue. Sandboxed execution, tool allowlisting, and network isolation help ensure that coding agents operate within controlled boundaries.

Guardrails like these make it practical to run agents continuously, not just as one-off experiments. See oursecurity architecturefor more details.

One alternative approach to agentic repository automation is to run coding agent CLIs, such as Copilot or Claude, directly inside a standard GitHub Actions YAML workflow. This approach often grants these agents more permission than is required for a specific task. In contrast, GitHub Agentic Workflows run coding agents with read-only access by default and rely on safe outputs for GitHub operations, providing tighter constraints, clearer review points, and stronger overall control.

## A simple example: A daily repo report

Let’s look at an agentic workflow which creates a daily status report for repository maintainers.

In practice, you will usually use AI assistance tocreate your workflows. The easiest way to do this is with an interactive coding agent. For example, with your favorite coding agent, you can enter this prompt:

Generate a workflow that creates a daily repo status report for a maintainer. Use the instructions at https://github.com/github/gh-aw/blob/main/create.md

The coding agent will interact with you to confirm your specific needs and intent, write the Markdown file, and check its validity. You can then review, refine, and validate the workflow before adding it to your repository.

This will create two files in.github/workflows:

* daily-repo-status.md(the agentic workflow)
* daily-repo-status.lock.yml(the corresponding agentic workflow lock file, which is executed by GitHub Actions)

The filedaily-repo-status.mdwill look like this:

---
on:
 schedule: daily

permissions:
 contents: read
 issues: read
 pull-requests: read

safe-outputs:
 create-issue:
 title-prefix: "[repo status] "
 labels: [report]

tools:
 github:
---

# Daily Repo Status Report

Create a daily status report for maintainers.

Include
- Recent repository activity (issues, PRs, discussions, releases, code changes)
- Progress tracking, goal reminders and highlights
- Project status and recommendations
- Actionable next steps for maintainers

Keep it concise and link to the relevant issues/PRs.

This file has two parts:

1. Frontmatter(YAML between---markers) for configuration
2. Markdown instructionsthat describe the job in natural language in natural language

The Markdown is the intent, but the trigger, permissions, tools, and allowed outputs are spelled out up front.

If you prefer, you can add the workflow to your repository manually:

1. Create the workflow: Adddaily-repo-status.mdwith the frontmatter and instructions.
2. Create the lock file:* gh extension install github/gh-aw
* gh aw compile
3. Commit and push: Commit and push files to your repository.
4. Add any required secrets: For example,add a token or API key for your coding agent.

Once you add this workflow to your repository, it will run automatically or you can trigger it manually using GitHub Actions. When the workflow runs, it creates a status report issue like this:

## What you can build with GitHub Agentic Workflows

If you’re looking for further inspirationPeli’s Agent Factoryis a guided tour through a wide range of workflows, with practical patterns you can adapt, remix, and standardize across repos.

A useful mental model: if repetitive work in a repository can be described in words, it might be a good fit for an agentic workflow.

If you’re looking for design patterns, check outChatOps,DailyOps,DataOps,IssueOps,ProjectOps,MultiRepoOps,andOrchestration.

Uses for agent-assisted repository automation often depend on particular repos and development priorities. Your team’s approach to software development will differ from those of other teams. It pays to be imaginative about how you can use agentic automation to augmentyourteam foryourrepositories foryourgoals.

## Practical guidance for teams

Agentic workflows bring a shift in thinking. They work best when you focus on goals and desired outputs rather than perfect prompts. You provide clarity on what success looks like, and allow the workflow to explore how to achieve it. Some boundaries are built into agentic workflows by default, and others are ones you explicitly define. This means the agent can explore and reason, but its conclusions always stay within safe, intentional limits.

You will find that your workflows can range from very general (“Improve the software”) to very specific (“Check that all technical documentation and error messages for this educational software are written in a style suitable for an audience of age 10 or above”). You can choose the level of specificity that’s appropriate for your team.

GitHub Agentic Workflows use coding agents at runtime, which incur billing costs. When using Copilot with default settings, each workflow run typically incurs twopremium requests: one for the agentic work and one for a guardrail check through safe outputs. The models used can be configured to help manage these costs. Today, automated uses of Copilot are associated with a user account. For other coding agents, refer to ourdocumentationfor details. Here are a few more tips to help teams get value quickly:

* Start withlow-risk outputssuch as comments, drafts, or reports before enabling pull request creation.
* For coding, start withgoal-oriented improvementssuch as routine refactoring, test coverage, or code simplification rather than feature work.
* For reports, use instructions that arespecific about what “good” looks like, including format, tone, links, and when to stop.
* Agentic workflows create an agent-only, sub-loop that’s able to be autonomous because agents are acting under defined terms. But it’s important thathumans stay in the broader loopof forward progress in the repository, through reports, issues, and pull requests. With GitHub Agentic Workflows,pull requests are never merged automatically, and humans must always review and approve.
* Treat the workflow Markdown as code. Review changes, keep it small, and evolve it intentionally.

Continuous AI works best if you use it in conjunction with CI/CD. Don’t use agentic workflows as a replacement for GitHub Actions YAML workflows for CI/CD. This approach extends continuous automation to more subjective, repetitive tasks that traditional CI/CD struggle to express.

## Build the future of automation with us

GitHub Agentic Workflows are available now in technical preview and are a collaboration between GitHub, Microsoft Research, and Azure Core Upstream. We invite you to try them out and help us shape the future of repository automation.

* Documentation
* How they work
* Quick start guide
* Workflow gallery

We’d love for you to be involved!Share your thoughts in the Community discussion, or join us (and tons of other awesome makers) in the #agentic-workflows channel of theGitHub Next Discord. We look forward to seeing what you build with GitHub Agentic Workflows. Happy automating!

Try GitHub Agentic Workflows in a repo today! Installgh-aw, add a starter workflow or create one using AI, and run it. Then,share what you build (and what you want next).

## Tags:

* agentic workflows
* AI agents
* automation
* continuous integration
* developer productivity
* DevOps
* GitHub Actions
* GitHub Copilot
* GitHub Next

## Written by

Principal Researcher, GitHub Next. Agentic software engineering, Copilot, C#, F#, async/await and more.

Principal Research Software Design Engineer at Microsoft Research. Creator of MakeCode, GenAIScript and more.

## Related posts



AI & ML


### How AI is reshaping developer choice (and Octoverse data proves it)

AI is rewiring developer preferences through convenience loops. Octoverse 2025 reveals how AI compatibility is becoming the new standard for technology choice.



AI & ML


### Continuous AI in practice: What developers can automate today with agentic CI

Think of Continuous AI as background agents that operate in your repository for tasks that require reasoning.



AI & ML


### How to maximize GitHub Copilot’s agentic capabilities

A senior engineer’s guide to architecting and extending Copilot’s real-world applications.

## We do newsletters, too

Discover tips, technical guides, and best practices in our biweekly newsletter just for devs.



Your email address

*

Your email address

Subscribe

							Yes please, I’d like GitHub and affiliates to use my information for personalized communications, targeted advertising and campaign effectiveness. See the
GitHub Privacy Statement
 for more details.

Subscribe

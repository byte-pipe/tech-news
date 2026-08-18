---
title: 'GitHub - vercel-labs/eve-software-factory-template: Meet Foreman, an eve Software Factory. · GitHub'
url: https://github.com/vercel-labs/eve-software-factory-template
site_name: tldr
content_file: tldr-github-vercel-labseve-software-factory-template-me
fetched_at: '2026-08-18T11:23:13.906352'
original_url: https://github.com/vercel-labs/eve-software-factory-template
date: '2026-08-18'
description: Meet Foreman, an eve Software Factory. Contribute to vercel-labs/eve-software-factory-template development by creating an account on GitHub.
tags:
- tldr
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 vercel-labs

 

/

eve-software-factory-template

Public template

* NotificationsYou must be signed in to change notification settings
* Fork58
* Star891

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

7 Commits
7 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
agent
agent
 
 
evals
evals
 
 
.env.example
.env.example
 
 
.gitignore
.gitignore
 
 
.vercelignore
.vercelignore
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
biome.jsonc
biome.jsonc
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
tsconfig.json
tsconfig.json
 
 
View all files

## Repository files navigation

# eve Software Factory Template

MeetForeman, an eve software factory that puts AI agents on every stage of the development loop and keeps people on the judgment calls.

Foreman takes tasks from GitHub and Linear, moves each one through four stations, and delivers a reviewed draft pull request on your repository. You review, mark ready, and merge.

## How it works

* Classifiertriages the task: type, priority, complexity, actionable or not. When the task isn't actionable, Foreman asks the requester instead of building the wrong thing.
* Analystturns it into a plan with acceptance criteria, working from a live checkout of your repository.
* Implementerexecutes the plan in its own sandbox, verifies with your repo's own checks, and pushes a branch.
* Reviewerindependently judges everything against the real diff, with evidence for each verdict.

Each station is its own agent with its own instructions, sandbox, and tools. The Reviewer sees only the pushed branch, never the Implementer's reasoning. Between runs, Foreman keeps afactory brain: notes about your repository that every run starts from. Seethe pipelineandfactory memoryfor the full picture.

## How work arrives

* Label an issuefactory.The pipeline runs on its own, posts progress as stations complete, and ends with a draft PR linked to the issue.
* @mention it on an issue or PR.Mentions from repo owners, members, and collaborators start an interactive session.
* Delegate in Linear.Linear Agent Sessions run the same pipeline and report progress back in Linear.
* The dev TUI.Hand it a task locally. Changes to GitHub wait for your approval.
* Red CI on a factory PR.Foreman diagnoses the failure and pushes a fix to its own branches, never yours.
* Someone opens a pull request.Foreman posts one orienting comment for reviewers: a summary, not a review.

## Deploy

The Vercel deploy flow sets up everything: theGitHubconnector,Linearconnector,Vercel Blobstore, and a prompt for theFACTORY_REPOandFACTORY_LABELenvironment variables.

Configuration (see.env.example):

Variable

Required

Default

What it does

FACTORY_REPO

Yes

—

The 
owner/repo
 the factory works on (the build fails without it)

FACTORY_SETUP_COMMAND

No

—

Runs once inside the sandbox checkout at build time (e.g. 
pnpm install
), so every run starts with dependencies already installed

FACTORY_LABEL

No

factory

The issue label that hands an issue to the factory

FACTORY_BRANCH_PREFIX

No

factory/

Branch prefix marking the factory's own PRs, which are the only branches automated CI fixes touch

FACTORY_BOT_NAME

No

the GitHub App's slug

The 
@mention
 name, resolved from the connector automatically when unset

GITHUB_CONNECTOR
 / 
LINEAR_CONNECTOR

Yes

—

Set automatically from Vercel Connect connector UIDs

## Local development

Link the project you deployed (or a fresh one), pull its environment, and start the TUI:

vercel link
vercel env pull
pnpm dev

Hand the agent a task ("users report the password reset email arrives twice, fix it") and watch the four stations fire in order, ending in a draft PR onFACTORY_REPO. Local runs are treated as untrusted, so changes to GitHub wait for your approval in the TUI.

## Resources

* Foreman Docs
* Vercel Connect
* eve Documentation
* GitHub Tools eve Extension

## Explore more templates

* eve Marketing Team
* eve Personal Agent
* eve Sanity Copilot
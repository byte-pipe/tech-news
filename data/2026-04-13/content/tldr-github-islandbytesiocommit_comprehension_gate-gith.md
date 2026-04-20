---
title: GitHub - islandbytesio/commit_comprehension_gate · GitHub
url: https://github.com/islandbytesio/commit_comprehension_gate
site_name: tldr
content_file: tldr-github-islandbytesiocommit_comprehension_gate-gith
fetched_at: '2026-04-13T06:00:32.996596'
original_url: https://github.com/islandbytesio/commit_comprehension_gate
date: '2026-04-13'
description: Contribute to islandbytesio/commit_comprehension_gate development by creating an account on GitHub.
tags:
- tldr
---

islandbytesio



/

commit_comprehension_gate

Public

* NotificationsYou must be signed in to change notification settings
* Fork0
* Star9




 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

4 Commits
4 Commits
.github/
workflows
.github/
workflows
 
 
scripts
scripts
 
 
.gitignore
.gitignore
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
View all files

## Repository files navigation

# Comprehension Gate

Developers are merging AI-generated code they've never read. Comprehension Gate blocks the merge until they can prove they understand what they're shipping.

A GitHub Action workflow that uses Claude to generate multiple-choice questions whenever a developer opens or updates a pull request. The PR author must answer all 3 questions correctly before the branch can merge.

No database, no external storage. Questions are embedded directly in the PR comment.

## How it works

1. A PR is opened (or updated) targetingmain
2. The workflow fetches the diff and sends it to Claude, which generates 3 multiple-choice questions about the actual logic and design decisions in the changes
3. The questions are posted as a PR comment and the commit status is set topending
4. The PR author replies with their answers in the comment thread
5. The answer-checker workflow runs instantly (no API call) and sets the commit status tosuccessorfailure

The PR author can retry as many times as needed. Pushing new commits regenerates fresh questions.

## Demo

[Video coming soon]

## Setup

### 1. Copy the files

Copy these into your repository:

scripts/comprehension_gate.py
.github/workflows/comprehension-gate-pr.yml
.github/workflows/comprehension-check.yml

### 2. Add the API key secret

In your repository:Settings → Secrets and variables → Actions → New repository secret

Name

Value

ANTHROPIC_API_KEY

Your Anthropic API key

### 3. (Optional) Change which branch is gated

By default, PRs targetingmainare gated. To change this, editcomprehension-gate-pr.yml:

on
:

pull_request
:

branches
:
 -
main
#
 ← change this

## Blocking merges (required status check)

Without this step the gate is informational only — the PR can still merge while the status is pending or failed.

To enforce the gate:

1. Go toSettings → Branches
2. ClickAdd branch ruleset(or edit an existing protection rule formain)
3. UnderRequire status checks to pass, add:Comprehension GateThe name must match exactly — it is case-sensitive.
4. EnableRequire branches to be up to date before merging(recommended)
5. Save the ruleset

Once configured, GitHub will block the merge button until the commit status forComprehension Gateissuccess.

## Developer experience

When a PR is opened, the bot posts a comment like:

Q1.What does this change do when the input is empty?

* A)Returns an empty list
* B)Raises a ValueError
* C)Returns None
* D)Falls through to the default handler

The author replies with their answers:

1. B
2. A
3. C

The bot then immediately replies with a pass/fail breakdown and updates the commit status.

## Skipping the gate

Draft PRs are skipped automatically. If you need to bypass the gate for a specific PR, a maintainer can manually set the commit status tosuccessvia the GitHub API or CLI:

gh api repos/{owner}/{repo}/statuses/{sha} \
 -f state=success \
 -f context=
"
Comprehension Gate
"
 \
 -f description=
"
Manually approved
"

## API cost

Claude is calledonce per PR open or pushto generate questions. Answer checking makes no API call.

The gate usesclaude-opus-4-6. Diffs are capped at 12,000 characters before being sent.

Diff size

Approx. input tokens

Estimated cost

Small (< 2 KB)

~800

~$0.01

Medium (2–6 KB)

~2,000

~$0.04

Large (6–12 KB, truncated)

~3,500

~$0.07

Output (3 questions + choices) adds roughly500 tokens ($0.04) regardless of diff size.

Typical cost: $0.05–$0.10 per PR.At current Anthropic pricing ($15/M input tokens, $75/M output tokens for Opus).

## Requirements

* Python 3.12+ (provided by the Actions runner)
* anthropicPython package (installed automatically by the workflow)
* AnAnthropic API key

## License

MIT License — see LICENSE file for details.
Patent Pending — IslandBytes LLC

## Contributing

Issues and PRs welcome.
See CONTRIBUTING.md for guidelines.

## About

 No description, website, or topics provided.


### Resources

 Readme



### License

 MIT license


### Contributing

 Contributing


### Uh oh!

There was an error while loading.Please reload this page.





Activity


### Stars

9

 stars


### Watchers

0

 watching


### Forks

0

 forks


 Report repository



## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





## Contributors1

* islandbytesioIslandBytes LLC

## Languages

* Python100.0%

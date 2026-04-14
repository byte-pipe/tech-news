---
title: GitHub Stacked PRs | GitHub Stacked PRs
url: https://github.github.com/gh-stack/
site_name: hackernews_api
content_file: hackernews_api-github-stacked-prs-github-stacked-prs
fetched_at: '2026-04-14T11:57:16.329514'
original_url: https://github.github.com/gh-stack/
author: ezekg
date: '2026-04-13'
description: Break large changes into small, reviewable, stacked pull requests with first-class GitHub support.
tags:
- hackernews
- trending
---

Stacked PRs is currently in private preview. 
Sign up for the waitlist →
 
 
 
 
 
 

# GitHub Stacked PRs

 
Break large changes into small, reviewable pull requests that build on each other — with native GitHub support and the 
gh stack
 CLI.
 
 
 
 Quick Start 
 
 Overview 
 
 
 
 
 
 
 

Stacked PRs, Native in GitHub

 

Arrange pull requests in an ordered stack and merge them all in one click. Each PR represents one focused layer of your change, reviewed independently and landed together.

 
 

Simplified Stack Management

 

Navigate between PRs in your stack from the GitHub UI, check the status of every layer at a glance, and trigger a cascading rebase across the entire stack with one click.

 
 

Powerful CLI

 

Thegh stackCLI makes it easy to create stacks, perform cascading rebases, push branches and create PRs, and navigate between layers — all from your terminal.

 
 

AI Agent Integration

 

Runnpx skills add github/gh-stackto teach your AI coding agents how to work with stacks. Break up a large diff into a stack or develop with stacks from the start.

 

## Why Stacked PRs?

Section titled “Why Stacked PRs?”

Large pull requests are hard to review, slow to merge, and prone to conflicts. Reviewers lose context, feedback quality drops, and the whole team slows down. Stacked PRs solve this by breaking big changes into a chain of small, focused pull requests that build on each other — each one independently reviewable.

## Arranging PRs in a Stack

Section titled “Arranging PRs in a Stack”

Astackis a series of pull requests in the same repository where each PR targets the branch of the PR below it, forming an ordered chain that ultimately lands on your main branch.

GitHub understands stacks end-to-end: the pull request UI shows astack mapso reviewers can navigate between layers, branch protection rules are enforced against thefinal target branch(not just the direct base), and CI runs for every PR in the stack as if they were targeting the final branch.

## How It Works

Section titled “How It Works”

Thegh stackCLI handles the local workflow: creating branches, managing rebases, pushing to GitHub, and creating PRs with the correct base branches. On GitHub, the PR UI gives reviewers the context they need — a stack map for navigation, focused diffs for each layer, and proper rules enforcement.

When you’re ready to merge, you can merge all or a part of the stack. Each PR can be merged directly or through the merge queue. After a merge, the remaining PRs in the stack are automatically rebased so the lowest unmerged PR targets the base branch.

## Get Started

Section titled “Get Started”

Terminal window
# Install the CLI extension
gh
 
extension
 
install
 
github/gh-stack

# Alias `gh stack` as `gs` for easier use (optional)
gh
 
stack
 
alias

# Start a stack (creates and checks out the first branch)
gs
 
init
 
auth-layer
# ... make commits ...

# Create new layers in the stack (creates and checks out each new branch)
gs
 
add
 
api-routes
# ... make commits ...
gs
 
add
 
frontend
# ... make commits ...

# Push all branches
gs
 
push

# Open a stack of PRs
gs
 
submit

Ready to dive in? Start with theQuick Start guideor read thefull overview.
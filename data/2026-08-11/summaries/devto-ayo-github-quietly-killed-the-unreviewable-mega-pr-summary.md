---
title: Ayo GitHub Quietly Killed the Unreviewable Mega-PR - DEV Community
url: https://dev.to/lovestaco/ayo-github-quietly-killed-the-unreviewable-mega-pr-3868
date: 2026-08-10
site: devto
model: llama3.2:1b
summarized_at: 2026-08-11T11:54:11.516615
---

# Ayo GitHub Quietly Killed the Unreviewable Mega-PR - DEV Community

# GitHub's Stacked Pull Requests Solution
=====================================================

## Overview of the Problem
-------------------------

The article discusses a problem faced by developers when working on large projects with multiple stakeholders. The issue was that good reviews went unrecognized due to a lengthy diff and insufficient code review process.

## Solution Overview
----------------------

GitHub introduced a solution called "stacked pull requests," which is a new way of reviewing changes as they are made to the project's history, rather than all at once. This approach breaks down large changes into smaller, manageable chunks, allowing for better reviews and more efficient use of reviewer time.

## Key Concepts
----------------

*   Stacked Pull Requests: GitHub's solution involves manually organizing different parts of a codebase into separate pull requests.
*   Base Branching: The top two branches in the repository serve as a reference point for each subsequent branch, allowing reviews to focus on the new changes introduced by each pull request.

## Practical Example
--------------------

### Step 1: Establish Stacking

The author manually stacks different parts of their codebase by creating separate pull requests and linking them together.

### Step 2: Create Base Branches

Base branches (e.g., `main` branch) serve as references for subsequent branches. The "stack" is created using the `gh stack --help` command, which requires a CLI extension or a newer version of GitHub Desktop.

### Step 3: Push Stacked Pull Requests

Each stacked pull request, including `setup-database`, `api-endpoints`, and `frontend` branches, is pushed to the repository with its corresponding base branch (`stack/01-setup-database`) set as the upstream tracking branch.

## Case Study
-------------

The article includes a detailed example of how GitHub's solution works for one of the author's repositories. The stack begins with two initial pull requests (`stack/01-setup-database` and `stack/02-api-endpoints`). By pushing these stackable pull requests into the repository, the author can then open additional pull requests to review changes without needing a long diff in the master branch.

The solution's key benefits are:

*   **Better Code Review:** Stacked pull requests help reviewers focus on specific parts of the codebase.
*   **Efficiency:** Reviews become more efficient as smaller, targeted updates are made.
*   **Reduced Burnout:** With fewer longer diffs to review, reviewers stay focused and energized.
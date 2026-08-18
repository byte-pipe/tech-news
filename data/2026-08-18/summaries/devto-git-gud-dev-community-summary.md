---
title: Git Gud! - DEV Community
url: https://dev.to/francistrdev/git-gud-4e6g
date: 2026-08-17
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-08-18T12:13:47.228077
---

# Git Gud! - DEV Community

# Transitioning from GitHub Desktop to CLI commands

## Introduction
- I have been using GitHub Desktop for its friendly UI, but list “Git” on my résumé feels inaccurate without CLI experience.  
- Learning Git via the command line helps bridge the gap between UI and terminal workflows.  
- This article shares the essential Git commands I use after moving away from GitHub Desktop, with analogies to *Hollow Knight: Silksong* for visual learners.  

## Core commands

### 1. `git init`
- Initializes a new Git repository in a fresh project folder.  
- Equivalent to starting a new game; you gain access to Git features.  
- **Note:** Skip this step when cloning an already‑initialized repository.

### 2. `git clone <url>`
- Copies an existing remote repository to your local machine.  
- Example: `git clone https://github.com/forem/forem.git`  
- Think of it as opening an existing save file.  
- **Tip:** Run the command in an empty directory.

### 3. `git add <file‑path>` (or `git add .`)
- Stages changes before committing.  
- Use `.` to add all modified files, or specify a path for a single file (e.g., `git add /app/tests.js`).  
- **Extra:** `git restore <file‑path>` undoes an accidental add, similar to unequipping a charm in the game.

### 4. `git commit -m "message"`
- Records a snapshot of the staged changes; acts like a checkpoint or save point.  
- Write clear, descriptive messages (e.g., “Fix a rerouting bug”).  
- To revert to a previous commit, find its hash with `git log` and run `git revert <hash>`.

### 5. `git push origin main`
- Sends local commits to the remote repository.  
- Best practice: fetch and integrate remote changes first:  
  - `git fetch origin main`  
  - `git pull origin main` (if the remote is ahead).  
- Analogy: fetching updates the game version before saving.

### 6. Branch management
- Create a branch: `git branch <branch-name>`  
- Switch to a branch: `git checkout <branch-name>`  
- Combine creation and checkout: `git checkout -b <branch-name>` (discovered from a comment).  

### 7. `git status`
- Shows which files are tracked, untracked, staged, or modified.  
- Helps you see what will be included in the next commit.

## Additional notes
- The list is not exhaustive; commands like `git merge` are omitted for simplicity.  
- Official documentation is available at <https://git-scm.com/docs>.  

## Call to action
- If you know other useful commands, leave a comment with the Hornet “Git Gud!” image as requested.  

---  
*End of summary.*
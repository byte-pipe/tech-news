---
title: Rebasing in Magit
url: https://entropicthoughts.com/rebasing-in-magit
date: 2026-03-10
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-03-11T13:14:48.221834
---

# Rebasing in Magit

# Rebasing in Magit – Summary

## Command centre: the git log
- Open the log with `l L`; `l` is the prefix for log commands and `L` shows all local and remote branches.
- Magit displays non‑intrusive hints for every option, so you never have to memorize the exact flags.
- Examples of on‑the‑fly options:
  - `-A` → choose an author from a fuzzy‑matched list.
  - `=u` → pick a date range via a calendar or manual entry.
  - `-s` → show file diffstats.
  - `-- tests` → limit the view to a specific subdirectory.
- After selecting options, press `b` to include all branches.
- The full key sequence for a complex log view is:
  `l -A kqr ␍ =u 2025-06-01 ␍ -s -- tests ␍ b`
- Magit shows the equivalent shell command, e.g.:
  `git log --branches --remote --author=kqr --until=2025-06-01 --graph --color --decorate --no-merges --stat -- tests`
- This transparency helps users understand the underlying git commands instead of hiding them.

## Rebasing from the log
- Identify the branch to rebase (e.g., `profiling-of-test-suite`) and checkout it with `b b ␍`.
- Move the cursor to the target base branch (e.g., `optimise-company-name-generation`) and press `r e ␍` to start a rebase onto that commit.
- Adding `-i` after `r` opens an interactive rebase where you can edit the commit list, using hotkeys such as:
  - `k` – discard a commit
  - `f` – fixup
  - `w` – reword
  - `s` – squash
- The log updates instantly to reflect the new branch hierarchy.

## What did it just do?
- Press `$` to view Magit’s command log, which shows the exact git commands executed, e.g.:
  ```
  git checkout profiling-of-test-suite
  git rebase --autostash optimise-company-name-generation
  ```
- `--autostash` is enabled by default: it creates a temporary stash before the rebase and reapplies it afterward, allowing rebases on a dirty worktree while warning about possible conflicts.
- Magit also promotes safer practices such as using `--force-with-lease` instead of plain `--force`.

## Other git interfaces
- The same rebase could be performed directly on the command line with the two commands shown above, but the interactive log view gives better intuition about what changes are happening.
- Graphical git tools can perform the rebase but usually hide the underlying commands, offering less learning opportunity.
- Magit occupies a sweet spot: it is a thin, transparent wrapper around git while adding interactivity, discoverability, and efficiency that many other tools lack.
- Beyond rebasing, Magit also excels at staging, unstaging, reverting, and resetting files or hunks interactively.

## Takeaway
- Magit’s log view is a powerful, discoverable interface that teaches git concepts while remaining fast and transparent.
- Interactive rebasing from the log simplifies complex workflows and makes the underlying git operations visible, helping users become more confident with both Magit and the command line.

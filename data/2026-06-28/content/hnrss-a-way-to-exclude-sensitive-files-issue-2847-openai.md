---
title: 'A way to exclude sensitive files · Issue #2847 · openai/codex · GitHub'
url: https://github.com/openai/codex/issues/2847
site_name: hnrss
content_file: hnrss-a-way-to-exclude-sensitive-files-issue-2847-openai
fetched_at: '2026-06-28T19:34:58.534722'
original_url: https://github.com/openai/codex/issues/2847
date: '2026-06-28'
description: 'What feature would you like to see? A mechanism to explicitly mark files/paths that the agent must not read or send to the model, at both repository and global levels (e.g., a repo-local .codexignore plus a global ignore file). Example: ...'
tags:
- hackernews
- hnrss
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 openai

 

/

codex

Public

* NotificationsYou must be signed in to change notification settings
* Fork14k
* Star94.2k

# A way to exclude sensitive files#2847

Open
Open
A way to exclude sensitive files
#2847
Labels
enhancement
New feature or request
New feature or request
sandbox
Issues related to permissions or sandboxing
Issues related to permissions or sandboxing

## Description

mkusaka
opened 
on Aug 28, 2025
Issue body actions

### What feature would you like to see?

* A mechanism to explicitly mark files/paths that the agent must not read or send to the model, at both repository and global levels (e.g., a repo-local .codexignore plus a global ignore file).
* Example: keep node_modules/ searchable for implementation checks, but never read or send .env, .env.*,.pem, id_, .aws/, .ssh/.
* The configuration should be deterministic and shareable across the team/repo, and also support user defaults, rather than relying on project documentation or conventions.

### Are you interested in implementing this feature?

* Yes — I can contribute and tests.

### Additional information

Related:#205. That issue surfaced two primary use cases: preventing sensitive data from being sent to the model and excluding large/irrelevant files. The issue was closed in favor of a Rust (codex-rs) implementation, but as of 2025-08-28 a comparable feature does not appear to exist in codex-rs. I’d like to restart the discussion and converge on a design.

Reactions are currently unavailable

## Metadata

## Metadata
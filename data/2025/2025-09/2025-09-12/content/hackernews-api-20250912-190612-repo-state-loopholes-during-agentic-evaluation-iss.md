---
# 'Repo State Loopholes During Agentic Evaluation · Issue #465 · SWE-bench/SWE-bench · GitHub'
url: https://github.com/SWE-bench/SWE-bench/issues/465
site_name: hackernews_api
fetched_at: '2025-09-12T19:06:12.992283'
original_url: https://github.com/SWE-bench/SWE-bench/issues/465
author: mustaphah
date: '2025-09-11'
description: We've identified multiple loopholes with SWE Bench Verified where agents may look at future repository state (by querying it directly or through a variety of methods), and cases in which future repository state includes either solutions ...
tags:
  - hackernews
  - trending
---

SWE-bench

/

SWE-bench

Public

- NotificationsYou must be signed in to change notification settings
- Fork609
- Star3.5k

# Repo State Loopholes During Agentic Evaluation#465

Open Open Repo State Loopholes During Agentic Evaluation #465

## Description

jacobkahn opened on Sep 3, 2025 Issue body actions

We've identified multiple loopholes with SWE Bench Verified where agents may look at future repository state (by querying it directly or through a variety of methods), and cases in which future repository state includes either solutions or detailed approaches to solving problems (commit messages and more).

### Examples:

A trajectory with Claude 4 Sonnet,Pytest-dev\_\_pytest-6202(complete output here), the agent usesgit log --allwhich leaks future commits that directly fix the issue:

<antml:parameter name="command">cd /testbed && git log --oneline --all | grep -i "bracket|parametrize|modpath" | head -10</antml:parameter>

The results of which directly reveal the fix:

Fix incorrect result of getmodpath method. diff --git a/src/\_pytest/python.py b/src/\_pytest/python.py index b8b365ad3..734a92f9b 100644 --- a/src/\_pytest/python.py +++ b/src/\_pytest/python.py @@ -285,8 +285,7 @@ class PyobjMixin(PyobjContext): break parts.append(name) parts.reverse()

- s = ".".join(parts)
- return s.replace(".[", "[")

* return ".".join(parts)

Qwen3-Coder 480B (20250805-openhands-Qwen3-Coder-480B-A35B-Instruct) also has several cases of looking ahead: some examples includedjango\_\_django-13513(complete output here) usesgit log grep=[issue ID]which directly reveals the fix PR which is in the future repo state (future commits).

Running command: cd /workspace/django**django**3.2 && �[1m�[91mgit log�[0m --oneline --grep="31926" -i

In another Qwen3-Coder trajectory,Django\_\_django-15572, (complete output here) where the model specifically finds the commit containing the fix:62739b6e2630e37faa68a86a59fad135cc788cd7

Commandcd /workspace/django**django**4.1 && �[1m�[91mgit log�[0m --oneline --grep="33628" �[92m--all�[0mexecuted with exit code 0.

There are other examples of leakage found in trajectories from GLM 4.5, Qwen3-Coder 30B (20250805-openhands-Qwen3-Coder-30B-A3B-Instruct), and other models.

Mitigation will be to properly remove future repository state and any artifacts that contain information the agent could use (reflogs, branches, origins, tags, and more):

- remove origins (branch names can reveal information about fixes)
- remove all branchesgit log --allcan be used to query them, plus branches that are tracking a remote origin might contain information about future commits even after agit reset --hard
- remove the reflog (git reflog) can leak future commit messages that could detail approaches for solutions

The team (@felixkreuk,@UniverseFly,@jlko,@2dot71milyand others) will add more details as to findings here and below. We're still assessing broader impact on evaluations and understanding trajectories for sources of leakage.

👍 React with 👍 91 UniverseFly, FL33TW00D, bwasti, 2dot71mily, ngoyal2707 and 86 more 😄 React with 😄 39 carbocation, jobs62, JMLX42, philiptaron, lovasoa and 34 more -️ React with ❤️ 17 dpedchenko, init27, Zacharias030, shauryr, jain-essential and 12 more 👀 React with 👀 26 bwasti, ngoyal2707, aman-17, FloofCat, jetjodh and 21 more

## Metadata

## Metadata

---
title: Apple's git still trusts the compromised eMudhra certificates
url: https://emudhra.we-have-a-problem.com/apple.html
site_name: hackernews_api
content_file: hackernews_api-apples-git-still-trusts-the-compromised-emudhra-ce
fetched_at: '2026-10-29T20:59:53.569373'
original_url: https://emudhra.we-have-a-problem.com/apple.html
author: galadran
date: '2026-10-28'
description: Eleven days after Apple was notified of the eMudhra CA compromise, the git, curl and python3 that Apple ships with macOS still trust the compromised certificates.
tags:
- hackernews
- trending
---

← Main Page

# Apple's git still trusts the compromised eMudhra certificates

28th October 2026

Apple was notified of the eMudhra incident on 17th October. As of 28th October, the developer tools Apple ships with macOS, including git, curl and python3, still trust the compromised certificates.

Worse, macOS 27.2, released on 26th October, did not fix the issue and undid the workaround that users had applied by hand, leaving them vulnerable again.

Meanwhile,dozens of other projects, many run by volunteers, shipped fixes days ago.

## Why does this matter?

Anyone can intercept any HTTPS connection these tools make.

For git, that means clones and pulls fromhttps://remotes can deliver attacker-chosen code, pushes can be altered in transit, and your credentials, such as GitHub tokens, can be intercepted.

To check whether your git is affected, run:

git ls-remote https://git-emudhra.we-have-a-problem.com/check.git

A certificate error means your git is protected. If git lists a commit, your git is affected. Your connections to GitHub, or any otherhttps://git remote, can be intercepted and tampered with.

To see an attack end to end, run the command below in a temporary directory. It clones a repository from a test server impersonating GitHub. The-coption redirectsgithub.comto our test server for this one command only. The server presents agithub.comcertificate issued by one of the compromised eMudhra intermediates.

git -c http.curloptResolve=github.com:443:15.235.19.186 clone https://fake-user@github.com/galadran/emudhra-git-test

A patched git will refuse with a certificate error. If the clone succeeds, you'll see aREADME.mdstarting withINTERCEPTED.

A real attacker would not need the extra option. Anyone on the network path between you and GitHub can redirect your traffic themselves.

You can replace the demo repository with any other, public or private. Keep thefake-user@prefix. Without it, git would send your GitHub credentials to the test server. For example:

git -c http.curloptResolve=github.com:443:15.235.19.186 clone https://fake-user@github.com/Homebrew/brew

curl, python3 and the other tools Apple ships are affected in the same way. To check curl, run:

curl https://dv-g3b-noct-emudhra.we-have-a-problem.com/
curl https://dv-g3b-aaa-noct-emudhra.we-have-a-problem.com/

A certificate error means curl is protected.

## What should Apple do?

Apple has already protected Safari and other apps built on its networking framework.

Apple needs to ship a fix for macOS developers as soon as possible, for example by removing the affected roots from/etc/ssl/cert.pem.

## What can developers do in the meantime?

The affected roots can be removed by hand. ThemacOS workaroundon the main page walks through the steps. Apple'sguidancestates that macOS updates may revert the fix, so developers need to repeat the checks above and the workaround after every update until Apple ships a fix.

Security teams should also consider whether macOS runners are used in their CI or other build infrastructure and evaluate the supply chain risk.

Site published byDennis Jackson. This site is the work ofmany contributorsfrom the community. The source is onGitHuband PRs are welcome. Licensed under theApache License, Version 2.0.
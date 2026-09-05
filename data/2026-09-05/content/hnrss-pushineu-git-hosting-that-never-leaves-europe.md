---
title: Pushin.eu — Git hosting that never leaves Europe
url: https://pushin.eu
site_name: hnrss
content_file: hnrss-pushineu-git-hosting-that-never-leaves-europe
fetched_at: '2026-09-05T13:42:05.426800'
original_url: https://pushin.eu
date: '2026-09-05'
description: Sovereign, GDPR-native git hosting — code, issues, and CI, all on European soil.
tags:
- hackernews
- hnrss
---

European Git hosting

# Git hosting that never leaves Europe.

Public and private Git repos, hosted 100% in the EU, on a platform built for humans, not AI. We block slop, never use your code to train models, and focus on availability, not shiny AI features.

 Start pushing — free 

 

 Explore repos
 

## Five values we build by

We're not just a Git hosting platform. We're the Git hosting platform with a backbone. These are the values that guide us.

 01
 

### No US kill-switch. Just European law.

Your repos never leave the EU. That means noCLOUD Actsubpoenas, no foreign platform politics, and no vendor an ocean away who can lock you out overnight — only GDPR and a privacy-first approach.

 02
 

### Bots are welcome. Slop gets blocked.

Maintainers are drowning.Reputation hunters spray low-effort contributions across popular packages just to get their name on the list. We block the slop instead of enabling it, so maintainers don't burn out.

 03
 

### Built for humans.

We build for developers, not bots. No AI buttons bolted onto every surface. We obsess about DX while others chase shiny AI features but can't keep the servers online.

 04
 

### Always online.

When your Git host is down, so is your team. We put availability front and centre and engineer for it relentlessly, because you should be able to ship at any hour.

 05
 

### We don't train a model with your code.

We don't use your code to train models, and we don't let partners either
 — no exceptions, no fine print, no quiet opt-out buried in the terms.

 

 Code View
 
 

 
 
 

 Pull requests
 

 8
 

 

 Issues
 

 4
 

 CI Runners
 
 

 
 

 
 

 

 

 
 
 

 
 

main

Preview

Code

K

 ‹
 

 ›
 

 Aa
 

 ab
 

 .*
 

 

 Light theme
 

 Dark theme
 

 
 

 Clone
 

 

 Close
 

 

Is this real?

 
 Yes, it is! I'm 
Peter Ullrich
, and I'm building Pushin.eu with my Labrador, Bella. I've worked as a software developer for almost 10 years and live in Leiden, the Netherlands. You can also find many of my talks on YouTube. I've built other projects, including
 
Letter to Yourself

 and 
Indie Courses
.

 I started building Pushin.eu in April 2026, and it will become generally available in early 2027. I'm building it for the long term, with the hope that it will help Europe become more independent.
 
 

How do you make money?

 
 We're currently in invite-only beta and focused on polishing the product. Once Pushin.eu is generally available, we'll offer individual and team subscriptions at prices comparable to GitHub and GitLab.
 
 

How do you block slop?

 
 We plan to reduce low-quality contributions through several features, some already in place and others still to come. Invite-only registration helps us filter out low-quality accounts and confirm that new members are real people. Next, we plan to introduce a vouching system, similar to Tangled's, that lets contributors build a reputation.

 We'll combine that reputation with other signals to assess new pull requests and issues. Contributions that appear low quality will be clearly marked and de-emphasized, while maintainers will make the final decision. We also plan to introduce sane limits to contributions, like how many pull requests and issues a new contributor can open in repositories they don't own. This will be an ongoing effort, but the goal is clear.
 
 

How do I move a repository over from GitHub?

 
 Install the 
pun

 CLI and run 
pun import
. With no arguments, it lists your GitHub repositories so you can choose the ones you want. A GitHub import brings over the full Git history, labels, issues, and closed and merged pull requests with their comments. Original numbers, timestamps, and author attribution all remain intact. The import runs on your own machine, so your GitHub token stays with you. Any other Git remote works too, but those arrive as Git-only imports because there is no API for reading the surrounding metadata.
 
 

Can I try it without leaving GitHub?

 
 Mirror instead of importing. A mirror is a one-way sync from a GitHub repository into Pushin.eu: GitHub stays your source of truth, and the mirror follows along. Mirrored repositories are read-only to direct pushes, so the two stay in step. You can sync on demand, pause the mirror, or remove it whenever you like — nothing about it is a commitment.
 
 

Does it work with the tools I already use?

 
 Push and pull over SSH or over HTTPS with a personal access token, exactly as you do today. There's a REST API at
 
/api/v1

 with GitHub-compatible request and response shapes, so most scripts written for GitHub need nothing more than a new base URL. It covers a large part of GitHub's API, but not all of it, so review the available endpoints before porting a large integration. The
 
pun

 CLI manages repositories, pull requests, reviews, and comments from the terminal. You can secure your account with TOTP or a passkey.
 
 

How do I get an account?

 
 Registration is invite-only. Every member gets a limited number of invitation codes to share, so you'll need one from someone who is already here. You don't need an account to read code, though — Explore lists every public repository on the platform.
 
 

Where is my code actually hosted?

 
 On bare-metal servers that we operate in Scaleway's Paris datacenters. Scaleway is a French company, and nothing fails over to a US region, so there's no CLOUD Act surface. Your code remains in France, under European jurisdiction.
 
 

How do I get my data back out?

git clone

 gives you a complete copy of each repository, including its full history. It's ordinary Git, so the tools you already use will work. Issues, pull requests, and their comments are available through the REST API. There is no one-click export archive yet, but it's planned. Leaving should be as easy as arriving.
 
 

## Move your repos to Europe.

Host your code on a platform that keeps it in the EU, blocks the slop, and never trains on it.

 Start pushing — free 

 Explore repos
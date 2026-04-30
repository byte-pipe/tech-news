---
title: 'GitHub - browserbase/skills: Claude Agent SDK with a web browsing tool · GitHub'
url: https://github.com/browserbase/skills
site_name: github
content_file: github-github-browserbaseskills-claude-agent-sdk-with-a-w
fetched_at: '2026-04-30T12:14:31.958460'
original_url: https://github.com/browserbase/skills
author: browserbase
description: Claude Agent SDK with a web browsing tool. Contribute to browserbase/skills development by creating an account on GitHub.
---

browserbase

 

/

skills

Public

* NotificationsYou must be signed in to change notification settings
* Fork54
* Star667

 
 
 
 
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

44 Commits
44 Commits
.claude-plugin
.claude-plugin
 
 
agent
agent
 
 
skills
skills
 
 
.gitignore
.gitignore
 
 
README.md
README.md
 
 
package.json
package.json
 
 
tsconfig.json
tsconfig.json
 
 
View all files

## Repository files navigation

# Browserbase Skills

A set of skills for enablingClaude Codeto work with Browserbase through browser automation and the officialbbCLI.

## Skills

This plugin includes the following skills (seeskills/for details):

Skill

Description

browser

Automate web browser interactions via CLI commands — supports remote Browserbase sessions with anti-bot stealth, CAPTCHA solving, and residential proxies

browserbase-cli

Use the official 
bb
 CLI for Browserbase Functions and platform API workflows including sessions, projects, contexts, extensions, fetch, and dashboard

functions

Deploy serverless browser automation to Browserbase cloud using the 
bb
 CLI

site-debugger

Diagnose and fix failing browser automations — analyzes bot detection, selectors, timing, auth, and captchas, then generates a tested site playbook

browser-trace

Capture a full DevTools-protocol trace (CDP firehose, screenshots, DOM dumps) alongside any browser automation, then bisect the stream into per-page searchable buckets

bb-usage

Show Browserbase usage stats, session analytics, and cost forecasts in a terminal dashboard

cookie-sync

Sync cookies from local Chrome to a Browserbase persistent context so the browse CLI can access authenticated sites

fetch

Fetch HTML or JSON from static pages without a browser session — inspect status codes, headers, follow redirects

search

Search the web and return structured results (titles, URLs, metadata) without a browser session

ui-test

AI-powered adversarial UI testing — analyzes git diffs to test changes, or explores the full app to find bugs

## Installation

To install the skill to popular coding agents:

$ npx skills add browserbase/skills

### Claude Code

On Claude Code, to add the marketplace, simply run:

/plugin marketplace add browserbase/skills

Then install the plugin:

/plugin install browse@browserbase

If you prefer the manual interface:

1. On Claude Code, type/plugin
2. Select option3. Add marketplace
3. Enter the marketplace source:browserbase/skills
4. Press enter to select thebrowseplugin
5. Hit enter again toInstall now
6. Restart Claude Codefor changes to take effect

## Usage

Once installed, you can ask Claude to browse or use the Browserbase CLI:

* "Go to Hacker News, get the top post comments, and summarize them "
* "QA testhttp://localhost:3000and fix any bugs you encounter"
* "Order me a pizza, you're already signed in on Doordash"
* "Usebbto list my Browserbase projects and show the output as JSON"
* "Initialize a new Browserbase Function withbb functions initand explain the next commands"

Claude will handle the rest.

For local and localhost work,browse env localnow starts a clean isolated browser by default. Usebrowse env local --auto-connectwhen the agent should reuse your existing local Chrome session, cookies, or login state.

## Troubleshooting

### Chrome not found

Install Chrome for your platform:

* macOSorWindows:https://www.google.com/chrome/
* Linux:sudo apt install google-chrome-stable

### Profile refresh

To refresh cookies from your main Chrome profile:

rm -rf .chrome-profile

## Resources

* Stagehand Documentation
* Claude Code Skills

## About

Claude Agent SDK with a web browsing tool

### Resources

 Readme

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

667

 stars
 

### Watchers

4

 watching
 

### Forks

54

 forks
 

 Report repository

 

## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* JavaScript85.1%
* HTML14.9%
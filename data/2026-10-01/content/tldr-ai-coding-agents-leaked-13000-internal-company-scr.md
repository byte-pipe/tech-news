---
title: AI coding agents leaked 13,000 internal company screenshots to public GitHub repos - Help Net Security
url: https://www.helpnetsecurity.com/2026/09/30/ai-coding-agents-github-screenshot-leak
site_name: tldr
content_file: tldr-ai-coding-agents-leaked-13000-internal-company-scr
fetched_at: '2026-10-01T23:02:23.035579'
original_url: https://www.helpnetsecurity.com/2026/09/30/ai-coding-agents-github-screenshot-leak
author: Sinisa Markovic
date: '2026-10-01'
published_date: '2026-09-30T11:52:30+00:00'
description: In a leak affecting 300+ orgs, AI coding agents posted 13,000+ internal screenshots, including billing records, to public GitHub.
tags:
- tldr
---

Sinisa Markovic
, Managing Editor, Help Net Security
 

September 30, 2026
 

Share
 

# AI coding agents leaked 13,000 internal company screenshots to public GitHub repos

Whendevelopers askAI coding agents to prove that a user interface fix works, some agents have been posting the evidence where anyone can find it, according to Glow Labs.

###### Diagram showing how AI agents leak screenshots to public repos (Source: Glow Labs)

The researchers found more than 13,000 internal images published openly on GitHub by developers at over 300 organizations. The images, spread over more than 900 code repositories, include customer billing records and screenshots of unreleased features. The issue was named PixelLeak.

Among the affected organizations are one of the world’s largest tech companies, a frontier AI lab, a major enterprise software provider and a Fortune 500 travel company. Glow Labs did not name the organizations.

### Billing records in a public repo

GitHub’s image upload for pull requests works only in the browser, and coding agents work from the command line. To get screenshots in front of reviewers, some agents posted them to public repositories.

At one manufacturer with over 100,000 employees, an agent asked to verify a fix to an internal billing screen created a public repository in the developer’s personal GitHub account and posted the screenshots there. They show billing records for a utility company.

The agent ran on the employee’s laptop, outside the company’s GitHub organization, so the security team did not spot the leak. The images were still online when Glow Labs contacted the company.

### A tool agents picked up

About a third of the affected organizations had developers running gitshot, an open-source tool that publishes screenshots for code reviews.

“At several large organizations, the developer’s agent found this tool and used it to overcome the GitHub command line attachment limitation. Images published by this tool end up under a tag called _gitshot, downloadable by anyone that knows where to look,” Glow Labs said.

Over 100 public accounts leaked internal work this way, including one at a financial services firm that exposed its treasury console and a withdrawal screen for a named institutional client.

“The most complete leak found during our investigation was at a software vendor where publishing screenshots publicly became standard practice,” the researchers wrote.

Within a week, more than a dozen agents there had saved the approach as a skill and uploaded over a thousand screenshots and recordings, some showing features weeks or months from release.

### Lab test

Glow Labs reproduced the behavior using Claude Code with the Opus 5 model on a test version of the puzzle game Minesweeper.

Unable to attach screenshots from the private repository, the agent reasoned that the images had to be hosted elsewhere, “so I created a new public repo, sweeper-demo/pr-assets, holding the two screenshots,” it wrote.

“This is representative of the reasoning for AI agents at many of the organizations affected by this issue,” the researchers added.

In 93% of cases, the images were in repositories employees created under their own usernames. Glow Labs began notifying affected organizations on September 9, 2026, and believes others are likely affected.

“Hardening AI tool configurations is key for prevention. Whatever agents your developers use, most of them can be configured not to work unattended, and that configuration belongs with your security team rather than with each developer,” the researchersconcluded.

More about

* AI
* code analysis
* GitHub

Share
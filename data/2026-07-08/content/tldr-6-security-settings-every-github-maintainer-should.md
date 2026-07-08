---
title: 6 security settings every GitHub maintainer should enable this week - The GitHub Blog
url: https://github.blog/security/6-security-settings-every-github-maintainer-should-enable-this-week/
site_name: tldr
content_file: tldr-6-security-settings-every-github-maintainer-should
fetched_at: '2026-07-08T19:33:38.522176'
original_url: https://github.blog/security/6-security-settings-every-github-maintainer-should-enable-this-week/
author: Joseph Katsioloudes
date: '2026-07-08'
published_date: '2026-07-01T15:59:29+00:00'
description: These six free settings will not make your project unhackable. Nothing will. What they will do is close the easy doors.
tags:
- tldr
---

Joseph Katsioloudes
·
@jkcso
 

			July 1, 2026		

|

				6 minutes			

* Share:

At GitHub Security Lab, we spend a lot of our week talking to maintainers. Some find the settings page dense and the docs sprawl. Most maintainers we talk to weren’t hired to be security engineers. While this is true, ignoring a project’s security settings completely will lead into leaving a lot in the table in terms of automation and scalability, leading into a poor security posture, and before you realize it to vulnerabilities that pile up, exposing your users.

Here’s the short version. Six settings, free to use, updated in less than half an hour. We’ve bundled them into a guided flow calledProtect Your Projectso you can do them in one pass, and we walk through each tool you’ll use below.

## 1. Add a SECURITY.md file

This is the lightest-lift setting on the list and the one that makes everything else easier.

ASECURITY.mdfile tells the people who find bugs in your project where to send them. Without one, your options for a well-meaning reporter are a public issue (now a public exploit) or your personal email (if they can find it).

You don’t need to write much. We suggest adding a communication mean such as an email so that those reporting vulnerabilities can reach you directly without posting about them publicly. Then, you can state what bugs are in scope, alongside anything else a reporter should have in mind when contacting you. For reference, we point maintainers to the thesystemd project’s security policythat we consider a complete example. It sets clear expectations about reproducers and doesn’t assume you have a 24/7 response team when you don’t. Borrow the structure, change the contact details, commit it.

Ten minutes, tops.

## 2. Turn on private vulnerability reporting

SECURITY.mdtells reporters where to go. Private vulnerability reporting (PVR) gives them a private place to make their report.

Once enabled, a researcher can file a confidential advisory on your repo. You triage it out of the public eye and disclose on your timeline. The setup is one checkbox in Settings → Security.

If you only do one thing tonight, do these first two together. They are free, and are the fastest signal to your community that you take this seriously.

## 3. Turn on secret scanning, with push protection

This is the one with the most embarrassing failure mode.

GitGuardian’sState of Secrets Sprawl 2026found 28.65 million new secrets leaked on public GitHub in 2025, a 34% jump over the prior year and the largest single-year increase on record. AI-assisted commits are leaking secrets at roughly twice the baseline rate. The average cost of a data breach now sits at $4.44 million globally ($10.22 million in the US) perIBM’s 2025 Cost of a Data Breach Report.

Secret scanning catches keys and tokens that slip into your repo by blocking them locally before they’re pushed to your repository. It doesn’t matter if your repo is public or private, because once secrets leave your local development, then they are available to anyone with access to your repo.

## 4. Turn on Dependabot and dependency review

Your project isn’t just your code. It’s the dozens (often hundreds) of packages your code pulls in.

Looking at WordPress, for example:this search for reviewed, critical-severity advisories mentioning WordPressreturns a long list of plugins with known vulnerabilities. If you’re running a WordPress site, Dependabot helps ensure none of these plugins are sitting in your dependencies.

Dependabot alerts you when a package you depend on has a known vulnerability. Dependency review shows you, inside a pull request, exactly what’s being added or upgraded and whether any of it has an open advisory. Together they turn an opaquepackage.jsondiff into a two-minute review.

## 5. Turn on code scanning

Code scanning runs static analysis on your repo and flags the patterns that lead to real bugs. SQL injection. Command injection. Dangerous deserialization. The usual cast.

Code scanning with CodeQL can detect unsafe GitHub Actions workflows. CodeQL is the engine, and we built code scanning. We made it free for open source in 2019, and it now ships as a one-click default setup in your Security and Quality tab.

This is the setting most maintainers skip because it sounds like it needs configuration. It doesn’t. Default setup picks the right query pack for your language and runs on every pull request.

## 6. Turn on branch protection on your default branch

This is the simplest, least-flashy setting, but it will yield the biggest impact starting as soon as you turn it on. This is about requiring a pull request before merging tomainwith minimum one approval.

This catches the worst-case scenario: a compromised credential, a confused contributor, or a tired version of you pushing straight to production. It’s also what makes the other five settings actually bite, because now Dependabot alerts and code scanning findings block a merge instead of sitting in a tab you never open.

## In conclusion

These six settings will not make your project unhackable. Nothing will.

What they will do is close the easy doors, the ones being walked through right now by people scripting through public repos at scale.

Turn these on, and your project will be meaningfully harder to attack than it was this morning. So will every project that depends on it.

## Tags:

* GHAS
* GitHub Security Lab
* open source
* open source security

## Written by

Joseph is a leading voice in cybersecurity and AI, developing software and content that shape how developers build securely. His open source game gh.io/scg has helped over 10,000 developers gain future-proof security skills. His videos, with 2.8M+ views, simplify complex security topics and deliver actionable tips to a global audience. As a speaker, Joseph has delivered 79 talks across 25 countries over the past four years, captivating audiences with his insights and energetic stage presence.

## Related posts

 

Application security
 

### How GitHub used secret scanning to reach inbox zero

GitHub had 20,000+ secret scanning alerts across 15,000 repositories. Here’s how we separated signal from noise, built remediation workflows, and reached inbox zero in nine months.

 

Governance & compliance
 

### How GitHub maintains compliance for open source dependencies

Explore how the Open Source Program Office uses GitHub’s new license compliance product to manage open source dependencies at scale.

 

Git
 

### Highlights from Git 2.55

The open source Git project just released Git 2.55. Here is GitHub’s look at some of the most interesting features and changes introduced since last time.

## We do newsletters, too

Discover tips, technical guides, and best practices in our biweekly newsletter just for devs.

 

Your email address

*

Your email address

Subscribe

							Yes please, I’d like GitHub and affiliates to use my information for personalized communications, targeted advertising and campaign effectiveness. See the 
GitHub Privacy Statement
 for more details.						

Subscribe
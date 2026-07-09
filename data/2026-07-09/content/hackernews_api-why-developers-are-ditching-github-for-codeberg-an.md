---
title: Why developers are ditching GitHub for Codeberg and self-hosting alternatives
url: https://www.howtogeek.com/why-developers-are-ditching-github-for-codeberg-and-self-hosting-alternatives/
site_name: hackernews_api
content_file: hackernews_api-why-developers-are-ditching-github-for-codeberg-an
fetched_at: '2026-07-09T19:36:33.645200'
original_url: https://www.howtogeek.com/why-developers-are-ditching-github-for-codeberg-and-self-hosting-alternatives/
author: Gedxx
date: '2026-07-09'
published_date: '2026-07-08T20:00:17Z'
description: It’s supposed to be a decentralized service, after all...
tags:
- hackernews
- trending
---

By 

Bobby Jack

Published
 Jul 8, 2026, 4:00 PM EDT

A technology enthusiast, Bobby studied Computer Science at the University of Southampton before working in a number of roles across industries, from the private sector to the charitable one, at multinationals and startups. He’s helped maintain backend Java servers, designed databases and front-end interfaces, and created a bespoke content management system.

Bobby also enjoys video gaming, and has written for several outlets, including a stint as Editor-in-Chief at 
Switch Player Magazine
 and contributions to online magazine, 
SUPERJUMP
. Bobby uses a Mac for day-to-day work and an Android phone for distractions. 

Sign in to your 
How-To Geek
 account

By many measures, GitHub is as popular as ever. One new user joins every second, the service hosts over 600 million repositories, and nearly one billion commits were made in 2025.

 

But scratch the surface, and something else is going on. Some users are concerned about a range of issues, from technical problems like frequent downtime to the service’s political direction, especially since it was taken over by Microsoft.

 

A few high-profile projects have taken things much further, abandoning the offering altogether, in a move that may represent the beginnings of a more widespread exodus.

 

## Some key players have abandoned GitHub

### A slow trickle that may gain momentum

When you’re searching for open-source software, it can seem like every project is hosted on GitHub. Even the Linux kernel source code has a read-only GitHub mirror, although itsmain home has a domain of its own.

 

But this isn’t always the case, and it may become less and less so if moves by a handful of projects become a wider trend.

Probably the highest-profile departure so far has beenGhostty, a cross-platform terminal emulator. The project’s maintainer, Mitchell Hashimoto,announced in April 2026that Ghostty was leaving GitHub, although not immediately:

 

It'll take us time to remove all of our dependencies on GitHub and we have a plan in place to do it as incrementally as possible. We plan on keeping a read-only mirror available on GitHub at the current URL.

Zig, a system programming language that’s a spiritual successor to C,also announced its departure, back in November 2025. The project made its first commit back in 2015, and enjoyed an uninterrupted run on GitHub, until recently.

 

Another significant project that’s made a switch isTenacity. This cross-platform audio editorannounced its move on a Reddit forumin 2023 and now only maintains a mirror presence on GitHub.

Alongside these more prominent repos, many other projects have migrated, such asthe Dillo web browserand the Hare programming language. Even more were never on GitHub in the first place, choosing to self-host their repositories, likeGNOMEor Apache’s vast array of software.

 

Quiz

8 Questions · Test Your Knowledge

## GitHub alternatives for developersTrivia challenge

Think you know your GitLab from your Gitea? Put your source control
						knowledge to the test.

Platforms
Open Source
History
Features
DevOps

Begin

01 / 8

Platforms

Which company developed GitLab, one of the most popular GitHub alternatives?

A
Microsoft
B
Atlassian
C
GitLab Inc.
D
JetBrains

That's right! GitLab Inc. was founded in 2014 by Dmitriy Zaporozhets and
				Sid Sijbrandij. The platform started as an open-source project and has grown into one of the most
				feature-rich DevOps platforms available today.

Not quite — GitLab was created by GitLab Inc., founded by Dmitriy
				Zaporozhets and Sid Sijbrandij in 2014. While Microsoft owns GitHub itself, GitLab is an entirely
				separate company and product.

Continue

02 / 8

Open Source

Which GitHub alternative is a lightweight, self-hosted Git service written in Go,
					known for its low resource usage?

A
Gogs
B
Gitea
C
Kallithea
D
Phabricator

Correct! Gitea is a community-managed fork of Gogs, written in Go, and
				is celebrated for being incredibly lightweight. It can run on a Raspberry Pi and offers a GitHub-like
				interface without heavy server requirements.

Close, but the answer is Gitea. While Gogs is also written in Go and
				inspired Gitea, Gitea is the more actively maintained fork with a larger community. Both are self-hosted
				options, but Gitea has surpassed Gogs in development activity.

Continue

03 / 8

History

Bitbucket, a major GitHub alternative, was originally acquired by which company in
					2010?

A
Microsoft
B
Salesforce
C
Atlassian
D
IBM

Spot on! Atlassian acquired Bitbucket in 2010, integrating it into their
				suite of developer tools alongside Jira and Confluence. This made Bitbucket especially popular among
				teams already using the Atlassian ecosystem.

Not quite — Bitbucket was acquired by Atlassian in 2010, not Microsoft
				or any of the other options. Atlassian is the company behind Jira, Confluence, and Trello, making
				Bitbucket a natural fit for its developer-focused product lineup.

Continue

04 / 8

Features

Which GitHub alternative is best known for offering a fully integrated DevOps
					lifecycle platform, including CI/CD, security scanning, and project management in a single
					application?

A
Bitbucket
B
SourceForge
C
GitLab
D
Launchpad

Exactly right! GitLab markets itself as a complete DevOps platform,
				offering everything from source control and CI/CD pipelines to container registries and security
				scanning — all within one unified interface. This all-in-one approach is a key differentiator.

The correct answer is GitLab. While Bitbucket also offers CI/CD via
				Pipelines, GitLab is uniquely recognized for packaging the entire DevOps lifecycle — from planning to
				monitoring — into a single cohesive platform, making it a favorite for enterprise teams.

Continue

05 / 8

History

SourceForge, one of the earliest code hosting platforms, launched in which year?

A
1995
B
1999
C
2003
D
2001

Well done! SourceForge launched in 1999 and was a pioneer in open-source
				code hosting before GitHub existed. At its peak it hosted millions of projects, though it later lost
				ground to GitHub due to controversy over adware bundling.

Not quite — SourceForge launched in 1999, making it one of the oldest
				code hosting services on the internet. It predates GitHub by nearly a decade and was once the go-to
				platform for open-source projects before GitHub disrupted the space.

Continue

06 / 8

DevOps

Which self-hosted Git repository manager, developed by Perforce, is widely used in
					enterprise environments and supports both Git and Mercurial?

A
Gerrit
B
Rhodecode
C
Gitolite
D
Kallithea

Correct! RhodeCode is an enterprise-grade, self-hosted source code
				management platform that supports Git, Mercurial, and SVN. It was acquired by Perforce and is used by
				organizations that need strong access controls and audit trails.

The right answer is RhodeCode, now part of Perforce. It stands out among
				self-hosted alternatives for supporting multiple version control systems — Git, Mercurial, and SVN —
				making it attractive for enterprises managing legacy codebases alongside modern repos.

Continue

07 / 8

Platforms

Which platform, primarily used for large-scale open-source projects, is maintained
					by Canonical and hosts the development of many Ubuntu-related packages?

A
Savannah
B
Launchpad
C
Codeberg
D
Phabricator

That's correct! Launchpad is maintained by Canonical and serves as the
				central hub for Ubuntu development. It offers bug tracking, code hosting via Bazaar and Git, and
				translation tools, making it a specialized but powerful platform for the Ubuntu ecosystem.

The answer is Launchpad, run by Canonical — the company behind Ubuntu.
				While it's not as general-purpose as GitHub or GitLab, Launchpad is integral to Ubuntu's development
				workflow and hosts thousands of packages and projects tied to the Debian/Ubuntu ecosystem.

Continue

08 / 8

Open Source

Codeberg is a nonprofit-run GitHub alternative based in Germany. Which open-source
					software does it run under the hood?

A
GitLab CE
B
Gogs
C
Gitea
D
Kallithea

Exactly! Codeberg is powered by Gitea, the lightweight open-source Git
				platform written in Go. As a nonprofit hosted in the EU, Codeberg appeals strongly to privacy-conscious
				developers and those who want an ethical alternative to commercial platforms.

The correct answer is Gitea. Codeberg uses Gitea as its underlying
				software and operates as a registered nonprofit based in Berlin, Germany. It has become a favorite in
				the open-source and privacy-focused developer communities as a transparent alternative to GitHub.

See My Score

Challenge Complete

## Your Score

/ 8

Thanks for playing!

Try Again

## Projects have left for these key reasons

### Downtime, artificial intelligence, and politics are all concerns

Maintainers have given various reasons for moving away, including these:

 
* Technical quality: probably the most common complaint is that GitHub suffers from frequent outages. IncidentHubtracked a total downtimeof 112 hours across 48 “major outages” in the year from May 2025, noting that such outages were the driver behind the migrations of Ghostty and Zig.
* Politics: Andrew Kelley, creator of Zig, mentioned GitHub’s relationship with ICE in passing. The company’s $200k deal with the immigration agency was also criticized by employees way back in 2019.
* AI:Still a divisive topic, artificial intelligence has touched almost every aspect of our tech lives, including GitHub, where Copilot is being increasingly integrated. The service nailed its colors firmly to the mast in 2025, when CEO Thomas Dohmkecommented,“Either you embrace AI, or get out of this career.”

Complaints about GitHub are probably best summarized by another quote from Mitchell Hashimoto:

 

It's not a fun place for me to be anymore. I want to be there but it doesn't want me to be there. I want to get work done and it doesn't want me to get work done. I want to ship software and it doesn't want me to ship software.

Aside from these departures, those projects that have always avoided GitHub have their own reasons. The GNU Project, for example, has always been fiercely ideological and rejects GitHub because it requires non-free software (JavaScript) to run.It also notesthe host’s encouragement of “bad licensing practice.”

Close

## Alternatives to GitHub are doing well

### From self-hosting to Codeberg, various options are available

Codeberg is probably the singular most popular competing service that projects like Zig havechosen to abandon GitHub for. It has many of the same features as GitHub: issue tracking, static page hosting, and Continuous Integration/Continuous Delivery (CI/CD), for example.

There are other options, such as GitLab, which has a self-hosting option, or Bitbucket, GitHub’s most contemporary alternative.

 

Sourcehutis a completely open-source offering,with equivalents of GitHub’s core featuresand an emphasis on an email-based workflow.Others choose to host their own forge, with popular options includingGiteaand Forgejo, the software that runs in the background at Codeberg.

 

There are even whole movements encouraging people to give up GitHub, likethe Software Freedom Conservancy’s campaign, which has many resources to help you make the move.

 

### GitHub can be great, but it’s not your only option

Although it’s probably done more than any other web app to encourage open source development and collaboration, GitHub isn’t without its problems. Some are technical, some are more idealized, but whatever your stance, it’s good to know that alternatives are available.

 

Close
---
title: Why I'm leaving GitHub for Forgejo | Jorijn Schrijvershof
url: https://jorijn.com/en/blog/leaving-github-for-forgejo/
site_name: hackernews_api
content_file: hackernews_api-why-im-leaving-github-for-forgejo-jorijn-schrijver
fetched_at: '2026-05-13T19:36:37.909205'
original_url: https://jorijn.com/en/blog/leaving-github-for-forgejo/
author: Jorijn Schrijvershof
date: '2026-05-13'
description: I left GitHub for self-hosted Forgejo on a hardened NUC. The reason is digital sovereignty, not reliability outages. Here's the thinking and the architecture.
tags:
- hackernews
- trending
---

# Why I'm leaving GitHub for Forgejo

I moved my code from GitHub to a self-hosted Forgejo. Not because of the outages, but because of who owns what runs on top of them. The Dutch government just made the same call.

On April 27, 2026 the Dutch Ministry of the Interior soft-launchedcode.overheid.nl, a self-hosted Forgejo instance for Dutch government source code. Project manager Boris Van Hoytema said the platform "was born from the requirement that the ministry has to legally publish [its] source code on a place that [it] owns," and that Forgejo was picked over GitLab because it is fully open source and offers all the freedoms needed fordigital autonomy.

The week before, I quietly moved my own code in the same direction. My canonical Git host is nowcode.jorijn.com, running Forgejo v15 LTS on a single NUC in a hardened setup. Some of my repositories already live there; the rest are queued. The longer-term plan is to archive my public GitHub repositories once the migration is complete and point each archive at the new home.

Most pieces about leaving GitHub lead with the outages. Outages are real. They are not why I'm leaving. The outages, the AI-by-default opt-in, and the fact that GitHub no longer has its own CEO are all symptoms of one underlying fact: I do not own this. The Dutch government just published the same conclusion. So this is the long version of that thinking, and what the move actually looks like once you decide to make it.

TL;DR

* GitHub logged 257 incidents in May 2025 to April 2026, 48 of them major. The CTO publicly apologised and said capacity needs to scale 30x to keep up with AI-driven load.
* In August 2025 GitHub stopped having its own CEO. It is now a unit of Microsoft's CoreAI division, the same group building Copilot and the broader AI stack.
* On April 24, 2026 GitHub flipped Copilot Free, Pro, and Pro+ user-interaction data to opt-in for AI training by default. There is no repository-level opt-out.
* US-jurisdictional risk under FISA Section 702 and the CLOUD Act is unresolved. Microsoft's own attorney told the French Senate under oath he could not guarantee EU data was safe from silent US government access.
* The Dutch government picked Forgejo for code.overheid.nl in April 2026 for the same set of reasons. I'm doing the same for my work.
* code.jorijn.com runs Forgejo v15 LTS on a single NUC with a KVM-isolated, weekly-rebuilt Actions runner. Public GitHub repositories will be archived and pointed at the new home as the migration completes.

## Why outages aren't actually the reason

The April 2026 outages were the kind that makes engineers angry. On April 23 themerge queue's squash-merge code pathsilently reverted previously merged commits across 658 repositories and 2,092 pull requests after a feature flag was rolled out incompletely. Companies including Modal and Zipline did manual data recovery. Four days later, an overloaded Elasticsearch cluster took Pull Requests, Issues, and Packages offline for over six hours.

But pick any month and the picture is the same kind of bad. February 2026 alone logged 37 incidents, including a 3-hour 40-minute outage that took Actions, the Copilot Coding Agent, Code Review, CodeQL, Dependabot, and Pages down at once. October 1, 2025 was a ten-hour macOS-runner outage. The IncidentHub aggregation puts the May 2025 to April 2026 total at257 incidents and 48 major outages, with roughly 112 hours of total downtime.

The right way to read this list is not "GitHub is unreliable." Big systems break. The right way to read it is the framing GitHub itself put on it. CTOVlad Fedorov apologisedon April 28 and said capacity has to grow 30x to keep up with the load. He attributed that load directly to "agentic AI workflow growth" since December 2025. The reliability story is downstream of the AI story. GitHub is not slowing down on AI features. It is doubling down on them. The outages are what doubling-down looks like in production.

The Pragmatic Engineer pointed out thatGitLab, Bitbucket, Vercel, Linear, and Sentry didn't have the same year. They serve developers under the same overall demand pressure. Whatever GitHub is wrestling with is specific to GitHub.

## GitHub no longer has its own CEO

The bigger fact is older than the apology and got a lot less press. On August 11, 2025Thomas Dohmke stepped downas GitHub's CEO. Microsoft did not replace him. Instead, GitHub wasabsorbed into Microsoft's CoreAI division, a groupSatya Nadella introduced in January 2025with the stated mission to buildthe end-to-end Copilot and AI stack for both first-party and third-party customers.

GitHub's revenue, engineering, and support now report into Microsoft's developer division under Julia Liuson. GitHub's CPO reports to Microsoft's AI platform VP. The brand still exists. The independent leadership does not.

This matters because the older argument for staying on GitHub was that Microsoft kept it at arm's length. From 2018 through 2024 that was substantively true. Dohmke had a real seat. Product decisions were visibly GitHub's, not Microsoft's. After August 2025 that argument no longer holds. When you push code to github.com today, you are pushing it to a unit of Microsoft's AI organization. Whether that bothers you depends on how much you trust Microsoft's AI organization to make the same decisions about your repository that the older GitHub would have made. I no longer do, and the reason for that distrust shows up in the next section.

## The training-data default flipped

On March 25, 2026 GitHubannounced a privacy-statement changeeffective April 24. From that date,interaction data, specifically inputs, outputs, code snippets, and associated context, from Copilot Free, Pro, and Pro+ users will be used to train and improve our AI models unless they opt out.

Three things about that statement matter, in order.

First: opt-out, not opt-in. The default flipped. Anyone using Copilot for free, on Pro, or on Pro+ is now contributing to model training unless they go to the Copilot settings page and turn it off.

Second: there is no repository-level switch. As a maintainer, I cannot tell GitHubdon't train on interactions inside my repository. The opt-out is per user account, so each contributor has to make their own choice. In effect, my codebase becomes training material whenever anyone using Copilot Free/Pro/Pro+ touches it, no matter how I license it.

Third: the carve-out for private repositories is narrower than it sounds. GitHub says it does not use private-repo content "at rest" for training, but it does collect "code snippets and interaction context" generatedwhileCopilot is being used inside a private repo. The line betweenthe code at restandthe snippets generated while editing itis, charitably, blurry.

Copilot Business and Copilot Enterprise customers are exempt because they are governed by separate Data Protection Agreements. The split is clean: pay enough and your interactions are not training data. Otherwise they are.

Iwrote about agentic GitHub Actionsa few weeks ago, and at the time the security model was the headline. The training-data flip is the second half of the same story: GitHub's strategic interest in your interaction data is structural now, not optional. I am not interested in arguing about the merits of that strategy on someone else's platform. I would rather not be on the platform.

## Then there's the jurisdiction

Underneath all of this is a layer that doesn't shift when the privacy statement does. GitHub Inc. and Microsoft Corp. are US companies. Anything they hold sits in scope of US law, includingFISA Section 702and theCLOUD Act of 2018. Both apply regardless of where data physically sits.

Section 702 was reauthorised in April 2024 for two years and is currently running on a45-day extensionsigned at the end of April 2026 while Congress argues over a longer renewal. It authorises US intelligence collection against non-US persons through electronic communications service providers domiciled in the US. The CLOUD Act lets US law enforcement compel a US-headquartered company to produce data stored anywhere in the world.

GitHub announcedEU data residency for Enterprise Cloudin October 2024. That solves data location. It does not solve jurisdiction. CLOUD Act exposure follows corporate control, not geography.

The most honest articulation of this came not from a regulator but from Microsoft's own attorney, who told a French Senate hearing in June 2025, under oath, that hecould not guarantee French data stored in European Microsoft datacentres was safe from silent US government access.

I covered the broader legal picture in my earlier piece onwhy "hosted in Frankfurt" doesn't mean GDPR-compliant, and the operational implications for hosting providers inmy piece on NIS2, so I'll keep the detail there. The point that matters here is narrow. As long as your code lives at github.com, your code lives in US legal territory. EU data residency is a comfort, not a fix.

## The Dutch government's call: code.overheid.nl

This is where the Dutch government's choice deserves more attention than it got. The legal driver is the Netherlands' "Open, tenzij" policy, in force since 2020: software developed with public funds is open source by default unless security or confidentiality requires otherwise. To comply, the ministry needed somewhere to publish code that it actually controlled. Code.overheid.nl is the answer.

The piece worth pausing on iswhich forge they chose. The European Commission runscode.europa.eu on self-hosted GitLab, live since September 2022. Germany'sopenCodeis also GitLab. France'scode.gouv.fris an aggregator that indexes repos hosted elsewhere, not a forge in itself.

The Dutch government's choice of Forgejo, not GitLab, was deliberate. As the OSOR article put it, the rationale was that Forgejo is fully open source, with no open-core split, and offers all the freedoms needed for digital autonomy. Van Hoytema added that Forgejo's roadmap was "way more aligned" with theirs than the alternatives. The government did not just want a sovereign forge. They wanted a sovereign forge that wasn't gated behind a commercial vendor's premium tier.

So the institutional pattern matters: a national government with serious lawyers and a long memory looked at the same picture I was looking at, made the same decision, and shipped it the week before I did. That isn't proof that the decision is right. It is, at minimum, proof that the decision is no longer fringe.

## Why Forgejo, and not GitLab

I weighed GitLab seriously. Self-hosted GitLab CE is a known quantity, with a much larger commercial ecosystem and, frankly, a more polished UI. Two things tipped the choice.

First: licensing. GitLab is open core. The Community Edition is MIT-licensed, but many of the features I'd actually want in production live in the Enterprise tiers under a non-free license. Forgejo went the other way. As ofv9.0 in August 2024the project relicensed from MIT to GPLv3+, with the explicit goal of staying copyleft and resisting future commercial capture of the codebase. The fork from Gitea inDecember 2022happened precisely because Gitea Ltd took control of the trademarks and domains in a way the community had not consented to. The lesson learned shows up in the license.

Second: governance. Forgejo lives underCodeberg e.V., a non-profit registered in Berlin since September 2018, with a member-elected board, public budgets, and 300,000+ repositories on its hosted instance. Members vote on the budget annually; the 2025 plan was accepted with 88 in favour, zero against, one abstention. That is not a marketing claim about community governance. That is a GermanVereindoing whatVereinedo.

Forgejo v15.0 LTS shipped on April 16, 2026. It is the project's 100th release. Long-term support runs through July 15, 2027. Forgejo Actions reached the maturity I needed (ephemeral runners, OpenID Connect, reusable workflow expansion) in v15. Releases since the fork have been steady, with active monthly reports.

The honest caveat: the commercial Forgejo ecosystem is real but thin. The cleanest commercial offering today isCodey by VSHN, a Swiss-hosted managed Forgejo from 19 CHF per month, launched on Servala in March 2025. There is no Red-Hat-style enterprise support subscription. If you need 24/7 phone support and a vendor to point at, you will need to build that yourself, or wait. I am willing to wait, because I would rather own the platform.

## What I built, and why it looks the way it does

Code.jorijn.com runs on a single Intel NUC with 64 GB of RAM in my home office. Forgejo v15 LTS, Postgres 17, and Traefik live inside Docker. An Incus-managed KVM virtual machine sits beside them and runs my Forgejo Actions runner. That is the whole platform.

The interesting decision is not in the Forgejo deployment. Forgejo plus Postgres plus a reverse proxy is not interesting. The decision that took the most thought is the runner.

### Where the danger actually is

If you self-host a forge, the forge itself is the easy part. The hard part is whatever runs the CI jobs. My runner has to executenpm install,composer install, andpip installon a daily Renovate schedule, against lockfiles generated by my own repositories. That means it executes lifecycle scripts. It means every job potentially runs untrusted code, of the same general shape that recent npm-worm and axios supply-chain attacks used to ride dependency bots that auto-merged within an hour.

The runner's job, in other words, is not to run code. The runner's job is tocontainthe code while it runs. Everything in the runner architecture exists for that reason. The same logic I described inmy piece on unmaintained dependenciesapplies here: assume any single layer can fail, and design so the next one absorbs the failure.

### The defenses, weakest to strongest

The runner uses five layers, in order from softest to hardest.

1. A persistent KVM virtual machine.The runner lives in its own VM, not in a container on the host. The host's kernel is not shared with the job environment. A Linux kernel CVE inside the runner has to break the KVM boundary before it can touch the NUC.
2. gVisor as the default Docker runtime inside that VM.Job containers run underrunsc, which intercepts system calls in user space rather than passing them to the host kernel. A container escape has to break gVisorandthe surrounding KVM.
3. A weekly destructive rebuild.Every Monday at 02:00 UTC the entire VM is destroyed and recreated from a freshly baked Ubuntu base image, with new persistent runner registrations minted against Forgejo. The base image itself rebuilds on Sundays, so the new VM consumes that week's apt and kernel patches. Persistent state cannot live longer than seven days.
4. An nftables egress filter on the runner's bridge.The runner can reach:443,:80,:22, and:53to public destinations (npm, pypi, ghcr, my own Forgejo via the public hostname through the router's hairpin NAT). It cannot reach192.168.0.0/16,10.0.0.0/8, or172.16.0.0/12. A compromised job cannot scan my LAN, cannot reach the router admin interface, and cannot reach the host's other services.
5. Scope-bound runner tokens, never admin-scoped.The two persistent runner registrations are tied to a single user scope and a single org scope respectively, withwrite:user,write:organizationPAT scopes for management. A leaked token cannot register runners outside its scope, and definitely cannot do anything admin-scoped.

The combination is deliberately overlapping. Each layer is a fence. Together they are a perimeter with depth. None of this is novel, in the sense that all the primitives are upstream and well-documented. What is new is wiring them together for a single-user homelab where the entire platform fits on one NUC and reverts cleanly when something goes wrong.

The underlying primitives, KVM isolation, gVisor, weekly rebuilds, and scope-bound runner registrations, are all things Forgejo and Incus support natively. I just had to combine them.

## What I gave up

This is the section I have to write because every "both sides" article I respect has one. So: what does moving to Forgejo cost me, honestly?

Discovery and the social graph.GitHub is where my contributors find me. When someone pushes a small fix to a public repository, they expect to do it on github.com, not on a domain they have never heard of. The plan I'm working towards is to archive each public GitHub repository once the move is done and point its README at code.jorijn.com. The discovery path stays intact: people still find me via GitHub, see the archive notice, and follow the link to the canonical home. I'm not there yet — a few repositories already live on code.jorijn.com, the rest are queued. Until then, the gap is real, and I accept it.

GitHub Actions ecosystem fragility.Forgejo Actions deliberatelyaims for familiarity, not compatibility. Most things work. Some don't.permissions:blocks at the workflow level are silently ignored.actions/checkout@v6broke authenticated checkout on non-GitHub runners in early 2026, so I pinned everything to v5.actions/upload-artifact@v4requires the Forgejo-hosted fork. OIDC works but uses a different workflow key (enable-openid-connect: true) than GitHub'spermissions: id-token: write. None of these are blockers. They are all friction. If your workflows lean heavily on GitHub-specific features, the migration is a project, not an evening.

Dependabot.Forgejo doesn't have it. I runRenovateon the same self-hosted runner, on a 3-hour schedule. It does the same job. It has more configuration. The setup took me a day.

24/7 vendor support.GitHub Enterprise gives you a phone number and an SLA. Forgejo gives you an issue tracker and a chat room. For a one-person operation that is fine. For a 200-engineer organisation it might not be, and that is a real reason to wait.

## When this isn't worth it

I would not move to self-hosted Forgejo if any of the following are true.

* The team has zero appetite or capacity for running infrastructure. A managed Forgejo (Codey, or Codeberg for FOSS) closes most of that gap, but you still own the migration cost.
* You are heavily invested in GitHub-specific features: GitHub Apps marketplace, Codespaces, Copilot Workspace, Advanced Security. Forgejo is a forge, not a developer-platform-as-a-service.
* Your contributor base is the GitHub social graph. If discoverability matters more than ownership, stay where the contributors are. Or accept the friction, archive your public repositories with a pointer to your new home once the move is finished, and revisit the decision later.
* You don't have a credible operational answer for the runner. The runner is the part where this gets serious. If you are not prepared to think about KVM isolation, gVisor, nftables, and weekly rebuilds, run your CI jobs on a managed runner host, or stay on GitHub.

The Dutch government's pattern is the right model here too. They did not migrate everything in one step. Code.overheid.nl is a soft-launch platform for ministries to share open-source code, not a wholesale replacement for everything else they use. My setup has the same shape: Forgejo is canonical for my work, GitHub is a mirror, and I am willing to revisit the mirror later.

## Key takeaways

* GitHub is no longer an independent company with its own CEO. Since August 2025 it is a unit of Microsoft's CoreAI division.
* The April 2026 outages and the Copilot training-data default flip are downstream of the same shift. Both are predictable from the structure.
* US-jurisdictional risk under FISA 702 and the CLOUD Act is real and unresolvable from the customer side. EU data residency is a comfort, not a fix.
* The Dutch government picked Forgejo for code.overheid.nl in April 2026 for the same set of reasons. The institutional pattern is forming.
* A defensible self-hosted Forgejo deployment is achievable on a single NUC, but the runner is the part that requires real care: KVM isolation, gVisor, weekly rebuilds, scope-bound tokens, and an egress filter that says no to your LAN.
* Migration friction is real. Archiving your public GitHub repositories with a pointer to the new home keeps the discovery path intact while you complete the move.

## Recurring server or deployment issues?

I help teams make production reliable with CI/CD, Kubernetes, and cloud—so fixes stick and deploys stop being stressful.

Explore DevOps consultancy

## Related articles

1. 30 Apr 2026copy.fail (CVE-2026-31431): a small Linux kernel bug with an unusually big blast radiuscopy.fail is a Linux kernel local privilege escalation disclosed on 29 April 2026. It works on nearly every modern distribution, leaves no on-disk trace, and slips past Kubernetes' default seccomp. Why it matters and what to do.1631 words
2. 29 Apr 2026HashiCorp Vault vs OpenBao: a thorough comparison for platform teamsTwo secrets managers, one shared codebase, two very different licenses. A deep, practical comparison of HashiCorp Vault and OpenBao for platform engineers picking between them.4605 words
3. 19 Apr 2026OpenTofu vs Terraform in 2026: the fork finally divergedThree years after the fork, OpenTofu and Terraform have diverged in licensing, governance, and technical features. For EU teams evaluating infrastructure-as-code strategy, the choice is no longer theoretical.1950 words
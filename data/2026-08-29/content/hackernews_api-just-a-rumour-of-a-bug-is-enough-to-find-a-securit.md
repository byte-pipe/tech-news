---
title: Just a rumour of a bug is enough to find a security exploit these days | Anil Madhavapeddy
url: https://anil.recoil.org/notes/rumour-is-the-exploit
site_name: hackernews_api
content_file: hackernews_api-just-a-rumour-of-a-bug-is-enough-to-find-a-securit
fetched_at: '2026-08-29T15:28:55.942629'
original_url: https://anil.recoil.org/notes/rumour-is-the-exploit
author: Anil Madhavapeddy
date: '2026-08-28'
published_date: '2026-08-22'
description: Thinking through how the conventional OSS security embargoes no longer buy us time, and what open source maintainers might do instead to respond
tags:
- hackernews
- trending
---

Anil Madhavapeddy

I released a security fix for OCaml'scohttp 6.3.0today, fixing apath traversal issue.
The patch itself was straightforward and in normal times, the security procedure would have been to fix it privately, inform affected users, and then issue a public advisory. This time around though, I noticed probes in my live webserver logs with the exact bug pattern just minutes after opening thePR to fix the issue.

What's worse, I found I could use my own agents to find the exploitjust by knowing roughly what it was aboutand so could have been exploiting it well before the public patch was available!
Given that just therumourof a security issue seems enough to give attackers enough info to find new exploits, we're going to need to change the way we deal with security responses in open source.

## 1The rumour of a bug is all new agentic exploit systems need

This particular report arrived privately on a Slack channel via Jane Street last week, and was itself found via Claude Fable. That compresses all timelines considerably...

### 1.1The timeline of a modern security report

Before examining the patch in detail, I pointed my own Claude at the affected code to see what else was lurking (asking it to investigate path normalisation issues). Fable frustratingly refused outright due to its security block since Idon't have access to Glasswing, butDeepSeek V4 Proobliged me and independently turned up several related issues. My agent also trivially created an exploit to probe a local live server in under a minute.

After some back and forth with the bug reporter about possible fixes, I quietly openedcohttp#1145publicly toget more eyeson it. This normally takes a few days and a release within a week or two is reasonable. Within about ten minutes (!) this website was fielding probes for percent-encoded traversal sequences, indicating that automated watchers are keeping an eye on public repositories.

If it took me just a minute to create my own exploit locally, thenten minutes actually seems quite longfor an automated attack window to start! A determined attacker who is monitoring package repositories could easily be exploiting them within seconds.

### 1.2Security embargoes are no longer effective

Conventional security process involvesembargoingthe bug, and assumes that secrecy of the details protects users. However, all an agent needs today is a broad direction to search in, and it can do its own research.Fang et al.found that when given a CVE description, their GPT-4 agentexploited 87%of a 15-vulnerability benchmark, and without the description, just 7%.

Two years on, themean time to exploitis -7 days. In other words, exploitation now precedes the patch! That same metric looks to be around 63 days in 2018-19, and crossed zero in 2024. A quick search finds lots of other similar cases these days... marimo'sCVE-2026-39987went from advisory to first exploitation attempt in 9 hours, even with no public proof-of-concept in existence. Langflow'sCVE-2026-33017took 20 hours. We seem to have crossed the rubicon for automated exploit generation...

The state of LLM exploitation in 2026 (source: Vulncheck)

## 2Are the bugonomics against OSS maintainers now?

It looks to me like our security processes need to invert somewhat, since just one
person searching for the issue class (this could be a mailing list question, an odd
commit in an orphan branch, or a context leak) is sufficient to alert someone
else's agent and let them get exploit code. This is wild.

A May 2026 paper coined the term "bugonomics"
and argues that the bottleneck has moved to "defender remediation throughput". LLMs are merrily
generating exploits, but our ability to defend against them isn't necessarily
improving as maintainer validation, triage and release rates stay flat. This unfortunately
matches the view from my OSS maintainer's chair:

The question is not whether frontier models, open-weight models, or program
analysis "win". The question is how to orchestrate them so that scarce
validation, prioritization, and release capacity goes toward durable fixes
rather than mechanical search and report drafting. A central defender
opportunity is technical debt remediation: semantics-grounded, tool-verified,
model-assisted workflows that help maintainers find, validate, prioritize,
and fix security-relevant defects before they become tomorrow’s exploited
vulnerabilities.--Demystifying the Mythos or Disrupting Bugonomics?, Pesoli et al, 2026

And why are maintainer capabilities staying flat? Well, not having access
to frontier agents like Mythos is an obvious one, but also that the engineering of a
security patch that doesn't cause any regressions is just fundamentally more work.

## 3So what the hell can we do about this?

We clearly need to adapt fairly quickly. I don't think the current manual
triage process should disappear, but I have seen an unsustainable surge of activity since Fable
came out. We are only just beginning to get a handle on how much of the
incoming firehose is machine-generated, but it's obviously a lot.

The big engineering shops (like Google) have been buildingmicroupdates directly into
their softwareto
ensure that fixes directly reach users as a priority over (e.g.) being fixed in the
Chrome code repository. We don't really have that kind of luxury in
Docker or OCaml, as we don't control the endpoints our software is used in.
Aside fromDocker Desktop, downstream distributions quite
rightly repackage OSS on their own timescales and terms.

For smaller projects like OCaml, just gaining access to the frontier models is a struggle. The Western models have security guards in place which mean that we can't use the commercially available ones.Project Glasswinghasexpandedto 150 organisations across 15 countries including critical infrastructure operators, cloud and financial providers, the Linux Foundation, but 'mom and pop' maintainers still don't have access. I was ambivalentback in Aprilwhether this is harmful, but it's pretty obvious today that it's turning out pretty terribly.

### 3.1Super sekrit private patch development

The first remediation is to develop the fixes somewhere really private out of the reach of AI. GitHub'stemporary private forksnominally do this, but it doesn't work hugely well for us.

First, GitHub restricts it"to keep information about vulnerabilities secure, integrations, including CI, cannot access temporary private forks"which immediately disconnects the maintainer from the lifeblood of our CI results. Secondly, only a single PR can merge into the fork, which doesn't work well for issues that often span a few repositories. Reviewers also have to be enrolled one at a time by an admin, and in open-source land reviewers are kind of drive-by depending on who is available (especially in August!).

More broadly though, this plugs the wrong leak. The patch staying secret isn't
nearly as important as ensuring the description about the issue reaches
exactly the right people with no leakage to attackers.

We don't have robustdiscussioninfrastructure available within OSS as it's
spread through various end-to-end encrypted ones (we use Matrix) but also shared
infrastructure like Discord or Slack which are extremely leaky. We do need
some sort ofweb-of-trustto distinguish the
good guys from the bad in a particular project context.

### 3.2No embargoes, just ship continuously

Another thing we could do is to rapidly fix issues in public, ship
continuously, and improve the release path via better automation.

Bigger projects like Chrome show this is possible viaweekly security updates, two releases per week (!), anddynamic patchingthat swaps background processes for updated binaries without a restart. This isn't entirely new technology; I looked into integratinglive ksplice Linux patching with Xen15+ years ago. The Linux kernel also ships fixes as soon as possible, deferring at mostseven daysand exceptionally fourteen.

However, software packaging is our primary obstacle. Chrome has a relatively easy job of shipping one binary artefact, but OSS is often a bunch of libraries that are thenembeddedin a variety of downstream products.
So to do this, we'll need:

* much bettercross-ecosystem package managementto discover where disparate libraries are eventually embedded.Ryan Gibbwill talk about this at ICFP next week!
* better scanning tools to help with triage; Andrew Nesbitt has been doing just this withScrutineerover the past few months.Thomas Gazagnaireand I have been discussing trying this out for our OCaml code, subject to getting access to a reasonable frontier model without security blocks.
* more robust quality control infra without any false positives that works across the spectrum of supported platforms. While it's relatively easy to run CI on Linux, it's a different story onOpenBSD,FreeBSD,macOS, and some architectures likeRISC-V

### 3.3Proactive protection at the protocol layer

I've also been having more radical thoughts about how we could slam in protections dynamically to protect endpoints using our libraries.
If we just accept that upstream patch fixes will always trail an exploit, then wemustput something faster to get ahead.

For example, this cohttp bug fixed today has a simple mitigation: just normalise percent-encoded path separators in the request URL. This rule was implementable the minute the report arrived, and also deployable while the full fix went through review, testing and packaging. Virtual patching is routine on cloud infrastructure these days; Cloudflare deployedmanaged rulesto plug Log4shell back in 2021.

But open source lacks a distribution mechanism for such rules outside of a commercial CDN. That's what theantibotty networkidea from ourinternet ecology paperis trying to plug viamore software diversityaround the global Internet. How can we have local, fast-propagating defences that hear about a vulnerability and act on their immediate infrastructure within seconds?

 
 

## 4Some research followups

I think we'll need some combination of all three options in the short-term. A lightweight web-of-trust for OSS contributors (like the venerableAdvogato used to be), as well as more focus on OSS packaging and continuous rollout and triage mechanisms that don't overwhelm our precious human contributors.

I've also posted a couple of new MPhil research ideas for anyone incoming to Cambridge next month and is looking for a project.

* "An antibotty defensive testbed to protect network services" puts a MirageOS gateway in front of a home network, and investigates whether a set of mitigation rules can be made trustworthy enough to deploy automatically. There's a fun capture-the-flag game we could play by giving the same rumour to an attacking agent and a defending one and seeing
which one gets there first.
* "Compiling Lean specifications into OxCaml enforcement automata" defines what a library is permitted to do across filesystem, parser and network layers usingDijkstra monads. This would compiles that Lean specification into an OxCaml automaton that enforces it at runtime. It's a modern spin on thestatecall automataI built during my PhD.

And if anyone from Project Glasswing is listening, team OCaml could use access now :-)

(The cohttp fix was not a solo effort. Sapphire Livingstone found and reported the issue, guided the fix and co-developed the remediation;Michael Dales,Török EdwinandPatrick Ferrisreviewed the patch;Hannes Mehnertcoordinated the advisory; andThomas Gazagnairehas been thinking through the wider triage problem. Thank you all! The bugonomics may be against us, but we will crest this hump.)

### References

[1]
Madhavapeddy et al (2025). Functional Networking for Millions of Docker Desktops. 
10.1145/3747525
[2]
Madhavapeddy (2026). Language integrated LLMs as an OCaml function. 
10.59350/61cdd-r5a25
[3]
Madhavapeddy et al (2025). Steps towards an Ecology for the Internet. Association for Computing Machinery. 
10.1145/3744169.3744180
[4]
Madhavapeddy et al (2026). A Decade of Docker Containers. 
10.1145/3761803
[5]
Madhavapeddy (2026). Rewilding the Web: my workshop report from Edinburgh. 
10.59350/g40yy-ks003
[6]
Madhavapeddy (2026). The Internet needs an antibotty immune system, stat. 
10.59350/snnnf-asc02
[7]
Madhavapeddy (2009). Combining Static Model Checking with Dynamic Enforcement Using the Statecall Policy Language. Springer. 
10.1007/978-3-642-10373-5_23
[8]
Gibb et al (2026). Package Managers à la Carte: A Formal Model of Dependency Resolution. arXiv. 
10.48550/arXiv.2602.18602
[9]
Fang et al (2024). LLM Agents can Autonomously Exploit One-day Vulnerabilities. arXiv. 
10.48550/arXiv.2404.08144
[10]
Pesoli et al (2026). Demystifying the Mythos or Disrupting Bugonomics? From Zero-Day Asymmetry to Defender Remediation Throughput. arXiv. 
10.48550/arXiv.2605.24632

### Related

.plan-26-34: Am I human or am I antibotty
Aug 2026
TESSERA v2 beta embeddings are in the TZE explorer, security embargoes being outrun by agents, opam packages now need humans behind them, prometheus and eio releases
.plan-26-33: Zarro rides out and evidence papers pour in
Aug 2026
TESSERA 1.0 is now fully available as Zarr with global RGB previews, a weather downscaling preprint, and Evidence TAP gets a public website with progress on the downloader and parser.
An antibotty defensive testbed to protect network services
Aug 2026
Available · MPhil
Compiling Lean specifications into OxCaml enforcement automata
Aug 2026
Available · MPhil
Package Managers à la Carte: A Formal Model of Dependency Resolution
Jul 2026
Ryan Gibb, Patrick Ferris et al.
Corrupt copies on the OpenBSD CI worker
Jun 2026
Mark Elvers
. Last week I updated the OpenBSD workers to OCaml 5.5.0 and took that opportunity to deploy OpenBSD 7.8. Shortly after, issue#1061 was opened as jobs randomly failed with an opam parse error.
FreeBSD git-daemon leak
Jun 2026
Mark Elvers
. The FreeBSD CI workers get slower over time. Is this a build-up on ZFS snapshots or something else?
Language integrated LLMs as an OCaml function
Jun 2026
Using a local DeepSeek model as an ordinary OCaml library and building sandboxed agents from simple primitives
Emulating RISC-V workers when the hardware goes away
Jun 2026
Mark Elvers
. Scaleway provide the RISC-V workers for OCaml CI, and they have been down for about a week with no real evidence that they’ll be back anytime soon. I can’t provision any new ones as they are “temporarily out of stock”.
Rewilding the Web: my workshop report from Edinburgh
May 2026
Notes from a wonderfully interdisciplinary Edinburgh workshop on 'Rewilding the Web', ranging coopetition and biological variety through the philosophy of self-organisation, polycrisis governance, protopian science fiction, and moderation seen through the lens of artisanal cheese.
Voluntary AI disclosure proposal for OCaml: update 1
May 2026
An update on the voluntary AI disclosure proposal, digesting the security, quality and legal feedback, and some concrete next steps around maintenance intent, multi-repository tooling, and reputation.
The Internet needs an antibotty immune system, stat
Apr 2026
Anthropic's Mythos makes autonomous vulnerability chaining across devices a sudden reality, so I've been thinking about how digital 'antibotty' inoculation networks may be needed far sooner than I expected.
A Decade of Docker Containers
Mar 2026
Anil Madhavapeddy, David J. Scott et al. — Communications of the ACM
Attempting overlayfs with macFuse
Oct 2025
Mark Elvers
. It would be great if overlayFS or unionFS worked on macOS! Initially, I attempted to use DYLD_INTERPOSE, but I wasn’t able to intercept enough system calls to get it to work. However, macFuse provides a way to implement our own userspace file systems. Patrick previously wrote obuilder-fs, which im…
Functional Networking for Millions of Docker Desktops
Aug 2025
Anil Madhavapeddy, David J. Scott et al. — Proceedings of ACM Programming Languages
Steps towards an Ecology for the Internet
Aug 2025
Anil Madhavapeddy, Sam Reynolds et al. — Proceedings of the sixth decennial Aarhus conference: Computing X Crisis
Modularizing Reasoning about AI Capabilities via Abstract Dijkstra Monads
Sep 2024
Cyrus Omar, Patrick Ferris et al. — the 12th ACM SIGPLAN Workshop on Higher-Order Programming with Effects (HOPE)
Combining Static Model Checking with Dynamic Enforcement Using the Statecall Policy Language
Nov 2009
Anil Madhavapeddy — Formal Methods and Software Engineering
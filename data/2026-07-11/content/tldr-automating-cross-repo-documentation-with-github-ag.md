---
title: Automating cross-repo documentation with GitHub Agentic Workflows - The GitHub Blog
url: https://github.blog/ai-and-ml/github-copilot/automating-cross-repo-documentation-with-github-agentic-workflows/
site_name: tldr
content_file: tldr-automating-cross-repo-documentation-with-github-ag
fetched_at: '2026-07-11T19:27:31.014070'
original_url: https://github.blog/ai-and-ml/github-copilot/automating-cross-repo-documentation-with-github-agentic-workflows/
author: David Pine, Peli de Halleux
date: '2026-07-11'
published_date: '2026-07-08T21:11:56+00:00'
description: How the Aspire team turns merged product changes into SME-reviewed docs pull requests, closing the gap between release and documentation.
tags:
- tldr
---

David Pine
 & 
Peli de Halleux
 

			July 8, 2026		

|

				9 minutes			

* Share:

“Where are the docs?” It’s a question nobody on a product team enjoys answering. The honest reply is usually some variant of “behind.” A writer is staring at a closed pull request, trying to reverse-engineer what changed. The pull request’s author has already moved on. By the time the doc actually publishes, the feature has shipped, sometimes more than once.

That used to be us on theAspireteam (we’re a small team of 10 building dev tools for distributed apps). A few months back, we were trying to figure out how to safely bring AI into automations we already trusted. That’s when we discovered GitHub Agentic Workflows. I started bolting prototypes intomicrosoft/aspire.

Here’s what that bought us, in numbers pulled straight out of GitHub: for Aspire 13.3 and 13.4,82 feature-docs pull requests merged at a median of 44.8 hours after the product pull request, every one of them reviewed by the engineer who shipped the feature. No new headcount. No process retraining. Just a different way of asking “who writes this?”

## 🔒 The constraint: cross-repo automation is the hard part

Our product lives inmicrosoft/aspireand our docs site lives inmicrosoft/aspire.dev—different repo, deploy target, and review chain. Most teams figure out same-repo automation pretty quickly; cross-repo automation is where things get sharp. Broad repo-scoped tokens belong in a museum, and any responsible security posture (ours included) restricts them accordingly. That’s a good thing. It’s also a real bottleneck if the place where you write the docs isn’t the place where you write the code.

The default workflow for years was:

1. Engineer ships a feature inmicrosoft/aspire.
2. Docs writer notices weeks later.
3. Docs writer opens the pull request, reads the diff, and pings the engineer to clarify what changed.
4. Engineer is on the next feature, vaguely remembers, replies with half the picture.
5. Docs draft ships, sometimes against a release that’s already out.

This is the reverse-engineering tax. We needed automation that crossed repos without handing an agent a write-everywhere token. GitHub Agentic Workflows turned out to be the answer.

## 🤖 Why GitHub Agentic Workflows

GitHub Agentic Workflows is a project from the GitHub Next team that I keep describing to people as “GitHub Actions, but with a model as the work-item processor and guard rails that satisfy security review.” That’s reductive, but it’s close.

The shape of it:

* You author a workflow as asingle markdown file(.github/workflows/my-thing.md). YAML-style frontmatter on top, an English-language prompt underneath.
* You run GitHub Agentic Workflows compile, and it generates a sibling.lock.yml(a normal GitHub Actions workflow) that you commit alongside.
* At runtime, the workflow runs an agent against your prompt with a constrained toolset.
* Critically,the agent doesn’t write to GitHub directly. It emits intent (a JSON blob describing the pull requests, issues, and comments it wants to create), and a separate, narrowly scoped job (thesafe-outputs handler) materializes that intent against a per-workflow GitHub app.

That last bullet is the unlock. The agent gets read access and a prompt. Writes go through a tiny verifiable pipeline with explicit allow-lists. Security review nods. We ship.

## 💚 A small aside: kindred stacks

I love when the tools you’re using to build are built with the same tools you’re using to build with. TheGitHub Agentic Workflows docsare built with Astro and Starlight. So is aspire.dev—Astro with Starlight, dressed up with the wider Starlight plugin ecosystem (astro-mermaid, starlight-llms-txt, starlight-sidebar-topics, starlight-image-zoom, the gorgeous @catppuccin/starlight theme, and more. Shout-out to Chris Swithinbank and the Starlight maintainers, the entire ecosystem feels designed by people who genuinely care).

There’s a real kinship there. The tool we use to automate docs and the docs site we automate into share the same foundation. Convenient, because the Mermaid sequence diagram in the next section renders the exact same way in both worlds.

## The end-to-end pipeline

Here’s the flow we landed on. The protagonist is a workflow calledpr-docs-check.mdliving inmicrosoft/aspire.

A run starts onpull_request: closedagainstmainorrelease/*, gated bymerged == true. From there, the workflow first runs a deterministic target branch resolver in plain bash before the agent ever wakes up:

1. Pull request milestone title (e.g. 13.4 → release/13.4 onaspire.dev).
2. Linked-issue milestone title (parse Fixes/Closes/Resolves #N from the body, fetch each issue, take the first non-empty milestone).
3. Pull request base ref, if it matches release/X.Y[.Z].
4. Fall back to main.

This is the linchpin.Milestones in the product repo map cleanly to release branches in the docsrepo. When the agent finally runs, it knows exactly where the docs should land without any creative writing about target branches or guessing.

The agent reads the diff, scans linked issues, and decides: does this need docs? If yes, it drafts the actual content in a checked-outmicrosoft/aspire.devworkspace, following our existing doc-writer skill (voice, MDX conventions, Starlight components). It then emits acreate_pull_requestsafe-output and hands off.

The safe-outputs handler takes over:

* Title prefix: [docs]
* Label: docs-from-code
* draft: true (we never auto-merge)
* Base branch: agent-supplied, restricted tomainorrelease/*
* Target repo:microsoft/aspire.dev
* Reviewer: theSME identified from the source pull request’s reviews—i.e., whoever the product team trusted to approve the feature, now gets asked to approve the doc for that feature.

A companion job posts a marker comment back on the source pull request with the docs pull request link and minimizes any olderpr-docs-checkcomments on re-run. The engineer who just hitMergegets a notification within a few minutes: “Here’s the docs draft. Look it over?”

## 🔐 The safe-outputs contract

The whole security story comes down to a small, boring stretch of frontmatter:

tools: 
 github: 
 toolsets: [repos, issues, pull_requests] 
 min-integrity: approved # only run pinned, integrity-checked actions 
 allowed-repos: 
 - microsoft/* 
 github-app: 
 app-id: ${{ secrets.ASPIRE_BOT_APP_ID }} 
 private-key: ${{ secrets.ASPIRE_BOT_PRIVATE_KEY }} 
 owner: "microsoft" 
 repositories: ["aspire.dev", "aspire"] 

safe-outputs: 
 create-pull-request: 
 title-prefix: "[docs] " 
 labels: [docs-from-code] 
 draft: true # human-in-the-loop, always 
 base-branch: main 
 allowed-base-branches: [main, release/*] 
 target-repo: "microsoft/aspire.dev" 
 protected-files: blocked # AGENTS.md, manifests, security config: hands off 
 fallback-as-issue: true 

That’s the deal in plain text. The agent gets a GitHub App token whose installation is scoped toexactly two repositories—the product repo and the docs repo—and nothing else in the org is reachable. It can only land pull requests againstmainorrelease/*.AGENTS.mdand dependency manifests are off-limits by policy. If the pull request creation fails (network blip, conflict, anything), the framework falls back to filing an issue, so nothing is silently dropped.

This is the part security review actually liked. The agent’s reasoning is fuzzy. The action surface is not.

## 📊 By the numbers

Here are the stats from a rolling 30-day window (May 3 – June 2, 2026) spanning the back end of the Aspire 13.3 release and the run-up to 13.4:

Metric
 
Value
 
Product pull requests merged in microsoft/aspire 
396 (338 main / 50 release/13.3 / 8 release/13.2) 
pr-docs-check workflow runs 
396 
Draft docs pull requests created on microsoft/aspire.dev 
82 
  – Merged 
82 (100%) 
  – Closed without merge 
0 
  – Still open 
0 
Docs pull requests target branches 
52 → release/13.3, 27 → release/13.4, 3 → main 
Median time-to-merge (docs) 
44.8 hours 
Merged within 24 h / 7 days 
38% / 96% 

Note:Numbers captured at the time of writing; the workflows keep running, so the totals only go up.

A few of those numbers deserve a second look:

* 396 runs→ 82 pull requests is not a defect. The workflow runs on every merged pull request; most of them are internal refactors, test fixes, or dependency bumps with no user-facing surface. The agent saying “no docs needed” 300+ times is a feature.
* 100% merge ratesays the agent’s docs picks are right. The tighter prompt we shipped after the v1 false-positive phase is paying off.

## ✅ What worked,❌what didn’t

What worked

* ✅Milestone→ release-branch mapping. This was the single highest-leverage choice we made. Engineers already set milestones on pull requests and issues; we got accurate target-branch routing for free.
* ✅Draft-only, SME-as-reviewer. The agent never merges. The engineer who shipped the feature is the one who confirms the docs are right. We’ve stopped reverse-engineering features at the doc layer. The engineer just tells the docs draft what to say, in the place where they already are.
* ✅Scoped GitHub app per workflow. Each workflow gets its own app token with explicit repo and permission scopes. Security review approved. We approved too; the first time we needed to rotate keys.
* ✅protected-files: blocked. The agent cannot touchAGENTS.md, package manifests, or repo security config. Period.

What didn’t (at first)

* ❌ The agent’s “is this docs-worthy?” gate was too generous in the first version. It drafted pull requests for changes that were genuinely internal, such as a CI tweak or a logging refactor. The result: 9 closures of 69 pull requests (≈13%), so we tightened the prompt’s user-facing-change definition and added explicit negative examples (CI, internal helpers, tests-only). Now, the rate is trending down.
* ❌ Cross-repo pull request creation needed amirrored checkout patternthat wasn’t obvious from the docs. The agent works in one repo; safe-outputs needs to find the target repo to push a branch. We solved it by checking outmicrosoft/aspire.devtwice—once as the current workspace, onceunder _repos/aspire.dev—so the safe-outputs handler can rediscover it deterministically.
* ❌ Big diffs blow prompt budgets. We pre-extract pull request metadata (linked issues, milestone, base ref) in pre-agent-steps bash, so the agent gets a small, structured summary instead of a giant payload. This is GitHub Agentic Workflow’s designed-in pattern, and it works.

## Wrapping up

The changes we made shifted our thinking. A feature wasn’t considered done until the docs were. Docs no longer trail along behind it like a tin can on a string. The engineer’s review is the gate; the bot does the typing.

Critically,this doesn’t replace docs writers; it un-burdens them. Our writers used to spend most of their time reverse-engineering features. Now they spend their time on the things only a human can do well: narrative pages, sample programs, conceptual walkthroughs, the parts of the docs that don’t fall out of a diff. The bot handles the mechanical “this new option was added; here’s the reference page update” work that was never enjoyable for anyone.

Huge thanks to the GitHub Next team for GitHub Agentic Workflows (and for making the safe-outputs primitive a first-class part of the design), and to Chris Swithinbank and the Starlight maintainers for the docs platform we automate into. A genuine thank-you, too, to the security folks whose guardrails forced us to design this the right way the first time. The boring secret of good automation is that strong security constraints make the system more trustworthy and more correct.

If you build a product in one repo and ship docs in another—and especially if you have to do it inside any nontrivial security boundary—GitHub Agentic Workflows is worth a serious look. Start with one workflow, such aspr-docs-check, and watch what happens to your median time-to-docs.

## 🔗 The other workflows

pr-docs-checkis the one I wrote this post about, but it’s not running alone. If you’re curious about the rest, the source is public:

* milestone-changelog.md: runs every two hours, picks up newly merged pull requests in the active milestone, and maintains a 13.x-Change-log wiki page (new features, improvements, notable bug fixes) with a companion editorial-feedback issue.346 runs.
* release-update-support-mdx.md: on a stable Aspire release, drafts a [support] pull request onaspire.devthat updates the support policy page (promotes the new version, demotes the previous one, refreshes the “Last updated” badge).
* update-integration-data.md: lives in the docs repo; runs pnpm update:all daily, refreshes NuGet metadata + GitHub stats + sample data, and opens a chore: Update integration data PR with supersede-and-close logic for stale runs.27 runs, eight merged pull requests.
* repo-pulse.md: a rolling three-day repo dashboard pinned to a single issue and updated in place: recent merges, pull requests awaiting review, new issues, discussion activity. One issue, always fresh.

Happy automating, friends! 🤖🚀

## Tags:

* agentic workflows
* automation
* DevOps
* GitHub Agentic Workflows

## Written by

Senior Software Engineer, Building aspire.dev at Microsoft

Principal Research Software Design Engineer at Microsoft Research. Creator of MakeCode, GenAIScript and more.

## Related posts

 

AI & ML
 

### Better tools made Copilot code review worse. Here’s how we actually improved it.

How migrating Copilot code review to shared Unix-style code exploration tools reduced review cost by reshaping agent workflows around pull request evidence.

 

AI & ML
 

### How GitHub Copilot enables zero DNS configuration for GitHub Pages

Go from an empty repository to a live custom domain with HTTPS in about 14 minutes, without manually editing a single DNS record.

 

AI & ML
 

### Evaluating performance and efficiency of the GitHub Copilot agentic harness across models and tasks

Explore how the GitHub Copilot agentic harness delivers strong results across multiple benchmarks and leading token efficiency, while maintaining flexibility to choose among more than 20 models.

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
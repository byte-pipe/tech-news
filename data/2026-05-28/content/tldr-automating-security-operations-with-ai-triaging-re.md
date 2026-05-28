---
title: 'Automating Security Operations with AI: Triaging Renovate PRs | Marco Lancini''s Blog'
url: https://blog.marcolancini.it/2026/blog-automating-security-operations-with-ai-triage-renovate/
site_name: tldr
content_file: tldr-automating-security-operations-with-ai-triaging-re
fetched_at: '2026-05-28T12:11:41.752570'
original_url: https://blog.marcolancini.it/2026/blog-automating-security-operations-with-ai-triage-renovate/
author: Marco Lancini
date: '2026-05-28'
published_date: 2026-05-21 00:00:00 +0100
description: A Claude Code Routine that triages every Renovate PR by risk, flags dead deps, and catches deprecated framework configs before I touch the diff.
tags:
- tldr
---

Reading time ~19 minutes

# Automating Security Operations with AI:Triaging Renovate PRs

* The Renovate Setup
* The Claude Skill
* The Claude Code Routine
* Putting It to Work
* Conclusions

If you followed the wave of supply-chain attacks from the first half of 2026,
you’ve probably realised that continuously patching and upgrading your dependencies is no longer optional.

For me,Renovatehandles the patching part well.
Most bumps are safe, but majors,0.xjumps, dead dependencies, and quietly deprecated framework configs are hard to spot from a CI test.
Manually reviewing every PR with the same rigor also doesn’t scale, and is a waste of time, to be honest.

So here I want to show youhow I combined Renovate with AI(Claude Code Routines in particular)to automatically verify the proposed changes do not introduce breaking changes.

The end-to-end pipeline looks like this:

flowchart LR
 subgraph GH["GitHub"]
 direction TB
 Renovate["Renovate<br/>(GitHub Actions, monthly)"]
 PR["[RENOVATE] PR"]
 Comment(["Auto-review<br/>comment"])
 Renovate -->|opens| PR
 PR -.- Comment
 end

 subgraph Claude["Claude Code (cloud)"]
 direction TB
 Routine["Routine<br/>trigger: PR_open"]
 Skill["renovate-review<br/>Skill"]
 Routine -->|invokes| Skill
 end

 PR -->|PR_open event| Routine
 Skill -->|reads PR + repo<br/>via gh api| PR
 Routine -->|posts comment<br/>via gh pr comment| Comment

Renovate runs inside GitHub Actions on a monthly cron and opens[RENOVATE]-prefixed PRs.
Each new PR fires aPR_openevent that triggers the Routine in Claude Code,
which in turn invokes therenovate-reviewSkill.
The Skill pulls the PR diff and the repo overgh api, builds a risk matrix, and then the Routine posts it straight back onto the PR as a comment.

The rest of the post walks each box in that diagram, in order.

# The Renovate Setup

Let’s start with the traditional (a.k.a. boring) part:Renovate.

If you are not familiar, Renovate is anautomated dependency update tool.
It helps update dependencies in your code without you needing to do it manually.
When Renovate runs on your repo, it looks for references to dependencies (both public and private) and, if newer versions are available, opens pull requests to update them automatically.

In my monorepo, I’ve a global.github/renovate.json5where I specify the upgrade behaviour I want to see:

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59

{
 // Docs: https://docs.renovatebot.com/configuration-options/
 $schema: "https://docs.renovatebot.com/renovate-schema.json",

 // ---------------------------------------------------------------------------
 // GENERAL CONFIG
 // ---------------------------------------------------------------------------
 baseBranchPatterns: ["main"],
 schedule: ["at any time"], // Workflow controls when it runs
 timezone: "UTC",

 // PR settings
 prConcurrentLimit: 10,
 prHourlyLimit: 0,
 prCreation: "immediate",
 automerge: false,
 labels: ["dependencies"],
 separateMajorMinor: false,

 // Minimum release age (supply chain protection)
 minimumReleaseAge: "14 days",
 internalChecksFilter: "strict",

 // ---------------------------------------------------------------------------
 // INCLUDES
 // ---------------------------------------------------------------------------
 // Include package files only within these defined paths
 includePaths: [
 ".github/**",
 "infrastructure/docker/cloudseclist/**",
 ],

 // Package rules for different dependency types
 packageRules: [
 // -------------------------------------------------------------------------
 // GitHub Actions
 // -------------------------------------------------------------------------
 {
 matchManagers: ["github-actions"],
 groupName: "github-actions",
 commitMessagePrefix: "[RENOVATE] [CI] [DEPS]:",
 commitMessageTopic: "GitHub Actions"
 },
 // -------------------------------------------------------------------------
 // CLOUDSECLIST APP
 // -------------------------------------------------------------------------
 // Docker - Backend
 {
 matchFileNames: [
 "infrastructure/docker/cloudseclist/backend/docker/Dockerfile.prod"
 ],
 matchManagers: ["dockerfile"],
 groupName: "dockerfile-backend",
 commitMessagePrefix: "[RENOVATE] [CLOUDSECLIST] [DEPS]:",
 commitMessageTopic: "Docker backend image"
 },
	...
 ]
}

* Lines8-10: general configuration for setting the base branch (main) and the schedule (left it open since Renovate will run from GitHub Actions).
* Lines13-18: some PR-related settings. For example, I do not want more than10PRs opened at once from a single Renovate run, I do not want separate PRs for minor and major upgrades, but I want every PR opened by Renovate to carry thedependencieslabel.
* Lines21-22: a couple of configs toprevent supply chain attacks.minimumReleaseAgewill prevent Renovate from suggesting packages published within the past 14 days (which alone would have blocked 90+% of the 2026 waves of attacks), whileinternalChecksFilterset tostrictwill skip pending releases. New typosquats and yanked versions don’t make it past those filters.
* Lines28-31: I tell Renovate which parts of the monorepo to keep updated regularly. Here you can see I started rolling out Renovate only to GitHub Actions and CloudSecList, while some legacy apps and static websites are not covered.
* Lines34-58:packageRulesthen group bumps by stack (GitHub Actions, Docker, Python, JavaScript) and give each group a deterministic PR title prefix. That’s actually important because they’re what the routine parses later to detect the stack and the project automatically.

The config is then driven by a thin GitHub Actions workflow.
It runs on a monthly schedule, can be triggered manually withworkflow_dispatch, and runs Renovate under a dedicatedRENOVATE_TOKEN(rather than the defaultGITHUB_TOKEN).
Monthly is a deliberate cadence: it batches the noise so I can dedicate one focused review window, instead of getting pinged every few days.

name
:
 
'
[ADMIN]
 
Renovate'

on
:

 
# Run every 2nd of the month at 05:00am UTC

 
schedule
:

 
-
 
cron
:
 
'
0
 
5
 
2
 
*
 
*'

 
# Allow manual triggers

 
workflow_dispatch
:

 
inputs
:

 
logLevel
:

 
description
:
 
'
Log
 
level'

 
required
:
 
false

 
default
:
 
'
debug'

 
type
:
 
choice

 
options
:

 
-
 
debug

 
-
 
info

 
-
 
warn

 
-
 
error

jobs
:

 
renovate
:

 
runs-on
:
 
ubuntu-latest

 
permissions
:

 
id-token
:
 
write

 
contents
:
 
write

 
pull-requests
:
 
write

 
steps
:

 
-
 
name
:
 
Checkout repository

 
uses
:
 
actions/checkout@v6

 
-
 
name
:
 
Run Renovate

 
uses
:
 
renovatebot/
[email protected]

 
with
:

 
configurationFile
:
 
.github/renovate.json5

 
token
:
 
$

 
env
:

 
RENOVATE_REPOSITORIES
:
 
${ { github.repository } }

 
LOG_LEVEL
:
 
${ { inputs.logLevel || 'info' } }

# The Claude Skill

That setup produces clean, predictable PRs. The next problem is making them actually reviewable.

A single PR can touch ten or more packages, and most monthly cycles look almost identical to the previous one.
Sothe review is time consuming, but not mechanical.
You still need to ask “does the codebase even use this package?” and “did the framework just deprecate something I rely on?”. That’s what burns the time, and that’s exactly the kind of thing I want captured as a skill rather than carried around in my head.

SoI crated a Claude skill which turns the review into a fixed workflow.
Once invoked, this skill:

1. Detects the stack and the project from the PR title and changed files.
2. Parses every bump out of the dep manifest.
3. Classifies each one intoHigh,Medium, orLowrisk based on what the package does and its track record, not just the version-number distance.
4. Greps the source for actual imports of everyHighrisk bump.
5. QueriesContext7for documented breaking changes on framework bumps.
6. Scans the project’s config files for known deprecated patterns (e.g., Next.jsmiddleware.ts).
7. Emits a single risk matrix at the end.

It’s important to call out two design choices I made:

1. Read-only by default.The skill investigates and outputs a risk matrix, then stops and waits. It does not run anything that could have side effects (neither edits nor commits). This is what makes it safe to run autonomously from the cloud later.
2. Project-agnostic.The same skill handles JS/TS and Python, regardless of the actual project (e.g., CloudSecList or something else). The project detection is driven entirely by the labeler config, not hardcoded paths.

Here is a dump of the actual skill (committed to the monorepo as well under.claude/skills/renovate-review/SKILL.md):

---

name
:
 
renovate-review

description
:
 
Use when reviewing a Renovate dependency-bump PR to investigate breaking changes, dead dependencies, and deprecated configs before merge

allowed-tools
:
 
Bash(gh api:*), Bash(gh pr view:*), Bash(gh auth status:*), Bash(ls:*), Bash(cat:*), Read, Grep, Glob, Edit

version
:
 
1.0.0

---

# Renovate PR Review

Investigate a Renovate-generated dependency-bump PR for real breaking changes, flag dead dependencies that can be removed, and scan for deprecated config patterns introduced by framework bumps. Project-agnostic: works for any app in the monorepo (CloudSecList, future apps).

## Core Principle

A Renovate PR is a proposal, not a ground truth. Most bumps are safe, but majors and 0.x bumps need evidence-based verification: does the codebase actually use the package? Did the framework deprecate something the project still relies on? This skill formalizes that investigation so it's reproducible instead of tribal knowledge.

## Constraints

-
 
**Read-only until approval.**
 Investigate first, propose fixes with diffs, wait for the user to say "apply" before editing anything.

-
 
**Never commit, never push, never run builds.**
 Follow CLAUDE.md: suggest verification commands, do not execute them. The only exception is 
`gh api`
 read calls and 
`cat`
 on local files.

-
 
**Never modify `yarn.lock`/`uv.lock`/`poetry.lock` manually.**
 If deps change, the user re-runs the appropriate install via 
`lcli`
.

-
 
**Never modify `renovate.json`.**
 Marco prefers single-PR upgrades; do not suggest grouping changes.

## Workflow

### Step 1: Fetch the PR

Accept a PR number or URL as argument. If the user passed a full GitHub URL, extract the number.

```
bash

gh auth status

```

If not authenticated, tell the user to authenticate first and stop.

Fetch PR metadata and changed files:

```
bash

gh api <your-repo>/pulls/<PR> 
--jq
 
'{title, state, base: .base.ref, head: .head.ref, body}'

gh api <your-repo>/pulls/<PR>/files 
--jq
 
'.[] | {filename, additions, deletions, patch}'

```

**If the PR body is truncated**
 (Renovate often hits GitHub's limit — look for 
`"This PR body was truncated"`
), rely on the 
`patch`
 field of the dep manifest file for the authoritative diff. Do not trust the PR body summary.

### Step 2: Detect Stack and Project

**Stack detection**
 — regex the PR title:

| Title pattern | Stack flow |
| --------------------- | ----------------------------------------------------------------------------------------------- |
| 
`JavaScript frontend`
 | JS/TS flow |
| 
`Python backend`
 | Python flow |
| Neither | Inspect changed filenames: 
`package.json`
 → JS/TS, 
`pyproject.toml`
/
`requirements.txt`
 → Python |

**Project detection**
 — read 
`.github/labeler.yml`
 and match the changed file paths against the glob patterns to identify the 
`component-*`
 label. Extract the app path.

If multiple 
**project-component**
 labels are matched, stop and ask the user which one to analyze — Renovate shouldn't cross project boundaries, so it's a signal something is off. Non-component labels like 
`ci/cd`
 or 
`documentation`
 touched alongside a component label are fine and don't count as "multiple projects".

### Step 3: Parse Bumps and Classify by Risk

From the dep manifest 
`patch`
, extract every 
`"<pkg>": "<old>" → "<pkg>": "<new>"`
 line. Build a structured list: 
`{name, old, new, dev}`
.

**Risk tiers:**

| Tier | Criteria |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 
**High**
 | Major semver bump (
`1.x → 2.x`
), any 
`0.x → 0.y`
 bump, framework packages (TypeScript, Next.js, React, React-DOM, ESLint, FastAPI, SQLAlchemy, Pydantic, Django) |
| 
**Medium**
 | Minor bumps on packages with a documented history of breakage on minors (Radix UI, Supabase SSR, lucide-react pre-1.0) |
| 
**Low**
 | Patch bumps, dev-only tooling, 
`@types/*`
 type-only packages, ordinary minor bumps |

**Do not**
 mechanically escalate based on raw version-number distance. A 
`12.27 → 12.38`
 jump on a well-behaved package is still a minor bump and belongs in Low tier. Risk comes from what the package 
*does*
 and its track record, not from the integer gap.

A bump in 
`devDependencies`
 is still High-risk if it's a major version jump on a framework-adjacent tool (tsc, eslint, tailwind). Don't mechanically downgrade tier just because it's a devDep.

### Step 4: Verify Usage

**For every High-risk bump:**

1.
 
**Grep source for imports.**
 Use the stack-specific patterns below. Read every match to understand 
*how*
 the package is used (one import at a file top vs a core integration matters).

2.
 
**If zero results:**
 flag as 
**dead dep**
. This is a fix candidate.

3.
 
**If used:**
 check the resolved installed version in 
`node_modules`
 (JS) or the lockfile (Python). Renovate bumps the ceiling, but 
`yarn install`
 may have already pulled a newer patch — 
`^1.0.0`
 might actually be 
`1.8.0`
. This matters because docs lookups should target the 
*installed*
 version, not the ceiling.

4.
 
**Query Context7**
 for documented breaking changes. Do this only for framework bumps and 0.x bumps — it's not worth the token cost for minor lucide-react.

**For every Medium-risk bump:**

-
 Grep only. Flag if dead. Skip Context7.

**For every Low-risk bump:**

-
 Skip investigation entirely. Group them in a one-line "safe bumps" footer.

#### JS/TS grep patterns

```

from ['\"]<pkg>['\"] # ES imports
require\(['\"]<pkg>['\"]\) # CommonJS

```

Use 
`Grep`
 tool with 
`path`
 set to the app root. Exclude 
`node_modules`
, 
`.next`
, 
`yarn.lock`
.

Installed version check:

```
bash

cat
 <app-root>/node_modules/<pkg>/package.json

```

Look for 
`"version"`
 field. If the file doesn't exist, the package isn't installed — very strong signal it's dead.

#### Python grep patterns

```

^import <pkg> # top-level import
^from <pkg>[. ] # from x import y / from x.submod import y

```

Note that 
**PyPI names and import names often differ**
. Keep this mapping in mind:

| PyPI name | Python import |
| ----------------- | ------------- |
| 
`python-dotenv`
 | 
`dotenv`
 |
| 
`pynamodb`
 | 
`pynamodb`
 |
| 
`beautifulsoup4`
 | 
`bs4`
 |
| 
`pillow`
 | 
`PIL`
 |
| 
`pyyaml`
 | 
`yaml`
 |
| 
`psycopg2-binary`
 | 
`psycopg2`
 |
| 
`sqlalchemy`
 | 
`sqlalchemy`
 |

When in doubt, check the package's PyPI page or 
`pyproject.toml`
 entry-points. If unclear, fall back to grepping both the PyPI name and plausible import names.

Resolved version check: parse 
`uv.lock`
 or 
`poetry.lock`
 in the app root for the exact installed version.

### Step 5: Deprecated-Config Scan

When a framework bump is present, check for known deprecation patterns in the project's config files. These are the patterns discovered in production; extend this list as new ones are found.

#### TypeScript 6.x

-
 
**`baseUrl` in `tsconfig.json`**
 — deprecated, will stop working in TS 7. Fix: remove it. 
`paths`
 now resolves relative to 
`tsconfig.json`
 itself.

```
bash

# Check:

grep
 
-n
 
'"baseUrl"'
 <app-root>/tsconfig.json

```

#### Next.js 16.x

-
 
**`middleware.ts`**
 — renamed to 
`proxy.ts`
 in Next.js 16. Presence of 
`middleware.ts`
 means the rename hasn't been applied yet.

-
 
**Sync `cookies()` / `headers()` calls**
 — must be 
`await`
-ed in Next.js 16. Grep for 
`cookies()`
 and 
`headers()`
 without 
`await`
.

-
 
**`params` typed as non-Promise**
 — dynamic route pages must type 
`params: Promise<{...}>`
 and 
`await`
 them.

-
 
**Cross-origin dev resources blocked**
 — if dev happens on a non-localhost hostname (e.g., 
`sf.local`
, 
`po.local`
), 
`next.config.ts`
 must include 
`allowedDevOrigins: ["<hostname>"]`
.

```
bash

# Checks:

ls
 <app-root>/middleware.ts 2>/dev/null 
# should not exist

grep
 
-rn
 
"cookies()"
 <app-root>/app 
--include
=
"*.ts*"
 | 
grep
 
-v
 
"await cookies()"

```

#### Python framework bumps

Not yet characterized — add specific rules here as they're encountered. For now, on FastAPI/Pydantic/SQLAlchemy majors, emit a "manual migration guide required" note in the report and link to the framework's upgrade docs via Context7.

### Step 6: Emit Risk Matrix

Output a structured report in the chat. Use this format exactly — it's been tuned to be scannable:

```
markdown

## PR #<num> — <title>

**Stack:**
 
<JS
/
TS
 
|
 
Python
>
 · 
**Project:**
 
<component-name>
 · 
**App root:**
 
`<path>`
 · 
**Status:**
 
<open
 
|
 
merged
 
|
 
closed
>

### High-risk bumps

| Package | Change | Installed | Verdict | Evidence |
| ------------------------ | ------------- | --------- | ---------- | ------------------------------------------------------------------------------------ |
| 
`typescript`
 | 
`5.9 → 6.0`
 | 
`6.0.2`
 | 
`[VERIFY]`
 | 
`tsconfig.json`
 uses deprecated 
`baseUrl`
 (see Step 5) |
| 
`lucide-react`
 | 
`0.562 → 1.7`
 | 
`1.8.0`
 | 
`[SAFE]`
 | 
`icons`
 export still present in 
`node_modules/lucide-react/dist/esm/lucide-react.js`
 |
| 
`eslint`
 | 
`9 → 10`
 | — | 
`[DEAD]`
 | No 
`eslint.config.*`
, 
`next lint`
 removed in Next.js 16 — tool was non-functional |
| 
`react-resizable-panels`
 | 
`4.4 → 4.7`
 | — | 
`[DEAD]`
 | No imports in source |
| 
`shiki`
 | 
`3 → 4`
 | — | 
`[DEAD]`
 | Listed as direct dep in 
`package.json`
 but zero source imports |

### Medium-risk bumps

| Package | Change | Verdict | Evidence |
| --------------- | ----------- | -------- | ------------------------------------------------- |
| 
`@supabase/ssr`
 | 
`0.8 → 0.9`
 | 
`[SAFE]`
 | 
`cookies.getAll/setAll`
 pattern matches v0.9 docs |

### Low-risk bumps (not investigated)

`prettier 3.8.0→3.8.1`
, 
`zod 4.3.5→4.3.6`
, 
`zustand 5.0.10→5.0.12`
, 
<
...
>

### Deprecated-config findings

-
 
`tsconfig.json:20`
 — 
`baseUrl: "."`
 is deprecated in TS 6. Remove it; 
`paths`
 still works.

-
 
`package.json:9`
 — 
`"lint": "next lint"`
 is dead (next lint removed in Next.js 16, no eslint.config present).

### Proposed fixes (awaiting approval)

[show diffs here — see Step 7]

**Verdict legend:**

-
 
`[SAFE]`
 — investigated, no action needed

-
 
`[VERIFY]`
 — can't be determined statically, run the verification command

-
 
`[DEAD]`
 — unused dep, safe to remove

-
 
`[MIGRATE]`
 — breaking change in active use; user must manually update code

-
 
`[RESOLVED]`
 — the issue was valid but is already fixed in the working tree (committed or uncommitted)

-
 
`[UNKNOWN]`
 — investigation inconclusive, user should review manually

Use bracketed text labels rather than emoji — CLAUDE.md's communication style rule forbids emoji in output.

### Step 7: Propose Fixes and Verification

**Propose fix diffs**
 for everything mechanical. Show them in the chat as code blocks labeled with the target file. Do NOT call 
`Edit`
 yet.

Categories of mechanical fixes:

1.
 
**Dead deps**
 — remove lines from 
`package.json`
 
`dependencies`
/
`devDependencies`
 or 
`pyproject.toml`
 
`[dependencies]`

2.
 
**Deprecated config options**
 — remove 
`baseUrl`
 from tsconfig, rename 
`middleware.ts`
 to 
`proxy.ts`
, etc.

3.
 
**Non-functional scripts**
 — remove 
`"lint": "next lint"`
 when ESLint is gone

4.
 
**Missing dev-host allowlist**
 — add 
`allowedDevOrigins`
 to 
`next.config.ts`
 when dev runs on a non-localhost hostname

For each proposed fix, write a clear "before / after" in the chat. Then stop and say:

> "Ready to apply these fixes? Reply `apply` to write them, or tell me which ones to skip."

**Only after explicit approval**
, use 
`Edit`
 to apply them. Apply in a batch. Do not call 
`git add`
 or 
`git commit`
.

## Output

The skill's final output in the chat is:

1.
 The risk matrix (Step 6)

2.
 The deprecated-config findings (Step 5, inline in the matrix)

3.
 The proposed fix diffs (Step 7)

4.
 The approval prompt

That's it. No narrative summary, no "I found N issues", no hedging.

## Edge Cases

**PR body is truncated by GitHub.**
 Renovate PRs routinely hit the 65K character limit. Always parse the 
`patch`
 field of the dep manifest file — do not rely on the PR body.

**Multiple projects touched.**
 Renovate shouldn't cross boundaries, but if the PR touches multiple projects, stop and ask the user which one to analyze. Do not try to analyze both in one report.

**PR already merged.**
 Warn the user and ask if they still want the report (useful for retroactive dead-dep cleanup). If they proceed, set 
`Status: merged`
 in the report header and use the 
`[RESOLVED]`
 verdict for any finding that was valid against the PR but is already fixed in the current working tree.

**`gh` not available.**
 Emit a message asking the user to run 
`gh auth status`
 manually. Do not try to install or configure 
`gh`
. Fall back: offer to analyze if the user pastes the 
`package.json`
 diff manually.

**No dep manifest in the diff.**
 This isn't a Renovate dep PR. Stop and tell the user the skill doesn't apply.

**Pre-1.0 Python package with a minor bump.**
 Treat as High-risk. Python libs routinely break on minor bumps when 
`0.x`
.

**Transitive-only package.**
 If a package appears in the diff but has no source imports AND no entry in 
`package.json`
/
`pyproject.toml`
, it's transitive. Ignore it — Renovate shouldn't include it, but if it does, it's not actionable.

## What This Skill Does NOT Do

-
 Does not run builds, typecheckers, tests, or container actions (CLAUDE.md: suggest, don't execute)

-
 Does not batch-review multiple PRs in one call — one PR per invocation

-
 Does not touch 
`renovate.json`
 or suggest grouping changes

-
 Does not commit, push, or create follow-up PRs

- Does not install or upgrade packages directly — only edits manifest files on approval

# The Claude Code Routine

The skill alone is half the story.
Invoking it manually from my terminal every time Renovate opens a PR is still a chore I’d skip on a busy week, and the whole point of the setup is consistency.

This is whereClaude Code Routinescome in.
A Routine isa Claude Code session that runs in the cloud, pointed at a repo and triggered by either a schedule or a GitHub event.
Configure it once and it fires without me.

In my case, every new Renovate PR should kick off a session that runs the skill against it, before I’ve even seen the PR notification on my phone.
So here is a step by step on how to create it.

First, link Claude to your GitHub account (if you haven’t already), then pick the repo the routine will run in:

Point the routine to your repo.

Next, select the GitHub event that triggers the routine (PR openedin this case),
add a title filter so it doesn’t fire on every PR.
Only PRs whose title starts with[RENOVATE]should match.
This is exactly why the package rules earlier all emit deterministic title prefixes: the routine needs a cheap, reliable way to decide whether to fire.

Picking a trigger, and setting a filter.

Connectors come next.
Aside from GitHub (to read PR metadata and post the comment), no other external service is needed.
Same goes for permissions: nothing special.

No connectors nor permissions needed.

Next, we only need to pick a title (something likeRenovate Review) and a prompt.
This is the actual interesting part.

Rather than reimplementing the review logic, it justinvokes the same skill I use locallyand applies a handful of overrides on top:

You are reviewing a Renovate-generated dependency-bump PR that just opened on 
<your
 
repo
>
.
Invoke the 
`renovate-review`
 skill at 
`.claude/skills/renovate-review/SKILL.md`
 and run it end-to-end against this PR.

Identify the PR number from the GitHub event context that triggered this session.
If the event context is not directly surfaced, fall back to:

```

gh pr list --repo <your-repo> --state open --search '"[RENOVATE]" in:title' --limit 1 --json number,title

```

and use the most recent match.

This run is fully autonomous.
The following overrides apply to the skill's default behavior:

-
 Do NOT ask for approval. Do NOT wait for any user reply. Skip the skill's Step 7 approval prompt entirely.

-
 Do NOT apply any fixes. Do NOT call Edit. Do NOT modify any files in the working tree. Do NOT commit, push, or open follow-up PRs.

-
 This cloud environment has no node_modules, no lockfiles resolved. Render the "Installed" column in the risk matrix as is.

Output channel: post the completed report as a single comment on the PR using:

```

gh pr comment <pr-number> --repo <your-repo> --body-file -

```

The report body must contain, in order:

1.
 A one-line header: 
`**Automated Renovate review**`
 (so it's clearly distinguishable from human comments).

2.
 The risk matrix from the skill's Step 6 (High / Medium / Low tables).

3.
 The deprecated-config findings from Step 5 (inline, as the skill already specifies).

No chat narrative, no separate files, no "I found N issues" summary. End the session as soon as the comment is posted successfully.

If the skill determines it does not apply (the PR touches no dependency manifest, or the stack/project cannot be detected unambiguously), post a single short comment explaining why and stop.
Do not invent findings to fill the report.

Title and prompt.

And the final shape of the routine:

The routine, ready to ship.

# Putting It to Work

The routine is event-driven, so the test isn’t to click “Run”. It’s either to wait for the monthly Renovate cron, or to kick off the GitHub workflow manually withworkflow_dispatch. Either way, a batch of Renovate PRs will appear.

Manually dispatching the Renovate workflow.

Once a PR opens, GitHub fires thePR_openevent and the routine wakes up.
A new Claude Code session spins up in the cloud, pulls the PR metadata, invokes the skill, and starts working through the risk matrix.

The routine picks up the PRs.

Once done, the routine will append a comment with its analysis.
It looks like this:

The auto-review comment posted on the Renovate PR.

# Conclusions

Overall, Renovate keeps the dependencies fresh, the minimumReleaseAge filter keeps the freshly-poisoned ones out, and the Routine keeps the review consistent.

I hope you found this post valuable and interesting,
and I’m keen to get feedback on it!
If you find the information shared helpful, if something is missing,
or if you have ideas on improving it,
please let me know on🐣 Twitteror at📢 feedback.marcolancini.it.

Thank you! 🙇‍♂️

CloudSecList

### Subscribe to CloudSecList

If you found this article interesting, you can join thousands of security professionals getting curated
 security-related news focused on the cloud native landscape by subscribing toCloudSecList.com.Subscribe

 About the Author
 

### Marco Lancini

				Hi, I'm 
Marco Lancini
. I'm a Director of Security, C|CISO, and author of "
The CloudSec Engineer
", writing about security strategy, technical leadership, and cloud security.
				

 [read more] 

Read More

#### Redesigning CloudSecList with Claude Design

Published on April 29, 2026
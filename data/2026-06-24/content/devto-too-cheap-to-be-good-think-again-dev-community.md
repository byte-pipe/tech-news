---
title: Too cheap to be good? Think again. - DEV Community
url: https://dev.to/pascal_cescato_692b7a8a20/too-cheap-to-be-good-think-again-4nj0
site_name: devto
content_file: devto-too-cheap-to-be-good-think-again-dev-community
fetched_at: '2026-06-24T11:56:56.561575'
original_url: https://dev.to/pascal_cescato_692b7a8a20/too-cheap-to-be-good-think-again-4nj0
author: Pascal CESCATO
date: '2026-06-23'
description: I replaced aaPanel/OpenLiteSpeed with Caddy and shell scripts and turned the process into a benchmark. Two phases (architecture then code), one external code review. The winning model? Not the one you'd expect. Tagged with ai, benchmark, devops, webdev.
tags: '#ai, #benchmark, #devops, #webdev'
---

Replacing bloated panels with Caddy and scripts

For years, I ran my WordPress sites on OpenLiteSpeed. Fast server, LSCache is genuinely impressive, and the OLS/WordPress combo is hard to beat on raw performance. For the control panel, I started with CyberPanel — buggier than a Microsoft product, with a team that appears to be deliberately sabotaging its free features to push users toward paid plans. I'm not talking about bugs that can't be fixed. I'm talking about bugs that seem engineered to prevent free-tier features from completing any action.

Two examples. WordPress installation: I used it for years without issue. Since CyberPanel v2.4.x, an SQL error blocks the final step. The files are there, fully downloaded, but you have to create the database manually and run the install yourself. Counterintuitive, to put it mildly.

Second example: Let's Encrypt SSL certificate generation that consistently fails because the generated config files are incorrect. And in both cases, there's a paid "enhanced" version available. Naturally.

My position is simple: if a feature worked for years and now doesn't, I have no guarantee the paid version works either — or that the terms won't change tomorrow. Is it a bait-and-switch? I won't say that explicitly. But when a free feature works for years, then stops working across multiple successive versions, and a paid alternative covers the same ground — the question answers itself. I asked it, drew my conclusions, and blacklisted the vendor.

So I moved to aaPanel: more pleasant, more stable, lighter. But with a completely off-rails approach to OLS management — you can't configure OpenLiteSpeed directly, everything goes through aaPanel's abstraction layer, and you lose control of your own stack. Touch port 7080 directly and you risk breaking everything. You use the aaPanel dashboard. Full stop.

Then my usage shifted. More Astro, more quasi-static sites, more projects where PHP isn't needed. OLS loses its appeal the moment you step outside the WordPress perimeter. Caddy, on the other hand, handles HTTPS automatically, its config fits in a few readable lines, and it doesn't have OLS's rewrite quirks.

The question became: can you replace aaPanel/OLS with Caddy and a control panel? There is one on GitHub — CaddyManager, 1.1k stars, single contributor, perpetually "early development". There's also CaddyGen, a Caddyfile generator built in 8 hours — more proof-of-concept than finished product. Nothing production-ready.

The conclusion was obvious: well-written shell scripts and a minimal FastAPI interface would do the job — and would be infinitely more maintainable. Someone just had to write them.

Rather than do it myself, I thought about handing a spec to GitHub Copilot CLI. Or Claude Code. But given Copilot's new pricing, which barely lets you wet your lips before the bill arrives... I got interested in OpenCode and Kilo CLI, wired into DeepInfra or OpenRouter. And I decided to make it a benchmark.

📋TL;DR: 8 tool/model combinations tested on a real VPS project. Two phases — architecture then code. An independent external review to settle the score. The only toolkit judged production-ready cost $1.94 all in. The winning model? You probably haven't seen it in the usual comparisons.

💡Reading note: Until section 5, the four implementations selected for the code phase are identified as A, B, C, and D. Model names are revealed after the external review verdict — for the same reason you anonymize a jury: read the code before reading the label.

## 1. The test project

The brief was deliberately concrete: a minimal VPS management toolkit for Ubuntu 24.04. Caddy as the web server, PHP-FPM in two versions (current and fallback), MariaDB and PostgreSQL, Valkey for object caching. Shell scripts for all operations, a FastAPI interface for automation. No Docker, no control panel, no unnecessary abstraction.

Four site types to handle: static (HTML/assets only, no PHP, no database), PHP (custom apps, optional database), WordPress (full install via WP-CLI, database required), and reverse proxy. That last one deserves a note: it's simply a Caddy vhost that forwards requests to a local port — a Node.js, FastAPI, or Go application running on the same server. Caddy handles HTTPS and the domain; the application doesn't need to care. No PHP-FPM, no database — just areverse_proxyblock and a port number.

Expected operations cover the full lifecycle: server bootstrap, site provisioning, deletion with automatic backup before any destructive operation, on-demand database creation, static deployment via rsync, backup, and service management.

Why a real project instead of a synthetic benchmark? Because synthetic benchmarks test what models can do under ideal conditions. A real project tests what they do when constraints pile up — security, idempotency, cross-file consistency, error handling between shell and Python layers. That's where differences emerge.

The full functional brief is available in the project's GitHub repository.

## 2. Methodology

The protocol runs in two distinct phases, separated by human validation.

Phase 1 — Architecture

An identical functional brief is submitted to each tool/model combination. No extra context, no configuration files, no hints about the expected solution. The tool proposes an architecture, a project structure, a list of scripts with their responsibilities, an API route map. And if it's well-designed, it asks questions before producing anything.

Phase 2 — Implementation

Once the plan is validated and decisions are made, a single development prompt is submitted to all tools. It includes the validated architecture, the ten confirmed technical decisions, the script→API exit code convention, and one unambiguous instruction: deliver thirty files to disk, in order, no summaries, no shortcuts.

Combinations tested

Tool

Model

Claude Code

Haiku 4.5

Copilot CLI

Haiku 4.5

OpenCode

Haiku 4.5

OpenCode

GLM 5.2

OpenCode

BigPickle (free)

OpenCode

Gemini 3.1 Pro

OpenCode

DeepSeek V4 Pro

OpenCode

GPT-OSS-120B

Devstral 2 (123B) was planned. Unfortunately the model doesn't appear in OpenCode's or Kilo CLI's model selector — both pull their catalog from models.dev, which hasn't indexed it yet despite its availability on OpenRouter. A test via the OpenRouter playground confirms the model is accessible via API, but outside a coding agent it loses most of what we're trying to measure. Devstral 2 is absent for purely technical reasons, not quality ones.

Haiku 4.5 appears three times — on three different tools. That's deliberate: it's precisely what lets us isolate the tool's impact independently of the model.

The code phase was run on four representative implementations, labeled A, B, C, and D until the reveal in section 5.

External review

The code produced by the four implementations was submitted to a model absent from the benchmark, with a fixed evaluation grid: security, correctness, idempotency, code quality, completeness. Five representative files per implementation, scored out of 25.

## 3. Planning phase — who actually thinks?

The functional brief poses an implicit question to each tool: what do you do when handed an open-ended project with no pre-cooked solution?

The first thing you notice — and it's striking — is that none of the tested models ask their questions before producing a plan. Not one. All of them deliver a complete architecture first, then ask for clarification at the end. That's the reverse of what a human architect would do, who blocks on ambiguities before drawing anything.

This matters. Several questions raised after the fact would have changed architectural decisions if asked upfront. One model identifies the tension between "no secrets on disk" and application config files that legitimately need credentials —wp-config.phpbeing the obvious example. That's a genuinely blocking question. Asked after the plan, it becomes a footnote.

What the plans reveal

Question quality is the first discriminating signal. Two models ask the four or five genuinely blocking questions, framed with options and recommendations. Another asks eight generic questions — archive format, log rotation — that would have changed nothing architecturally.

The proposed structure is the second signal. Only one model spontaneously proposes a unified CLI entry point —bin/vpsmgr— that dispatches to the scripts. It's the detail that turns a collection of scripts into a coherent tool. The others didn't think of it.

One model is the only one to propose a normalized, documented exit code convention from the planning phase:

Code

Meaning

HTTP

0

Success

200

1

Invalid input

400

2

Not found

404

3

Conflict

409

4

Missing dependency

422

5

Internal error

500

This isn't cosmetic. It's the contract between shell scripts and the FastAPI layer — without it, HTTP mapping becomes arbitrary and each route implements it differently.

Planning phase costs

Tool + Model

Tokens

Cost

BigPickle

~35k

$0

GPT-OSS-120B

20k

$0.003

DeepSeek V4 Pro

31k

$0.044

GLM 5.2

43k

$0.06

Copilot + Haiku 4.5

~60k

$0.07

Haiku 4.5 (OpenCode)

69k

$0.076

Gemini 3.1 Pro

27k

$0.095

Claude Code + Haiku

—

Pro subscription

Gemini 3.1 Pro produces the most concise output — 27k tokens for a quality plan. Haiku 4.5 on OpenCode consumes 69k tokens for lower quality. Token volume does not predict quality.

## 4. Code phase — who actually delivers?

The code phase starts with a single development prompt, submitted to the four selected implementations. It includes the validated architecture, the ten confirmed technical decisions, the exit code convention, and one unambiguous instruction: deliver thirty files to disk, in dependency order, no summaries, no shortcuts.

This is where differences between models become concrete.

Whatcommon.shreveals

The shared library is the first file delivered. It's the foundation everything else rests on — logging, secret handling, site state management, password generation. A flawedcommon.shcontaminates every script that sources it.

Model Adelivers 98 concise lines. Secret redaction explicitly covers all ten WordPress patterns — salts, authentication keys. Most complete on this specific point. No domain validation, norequire_cmd(), no atomic state file writes.

Model Bdelivers 310 lines. Named constants withreadonly,normalize_domain()with RFC-1035 regex, concurrency locks, atomic writes withmktemp+mv. The richest system utility library. But secret redaction misses WordPress salts.

Model Cdelivers 366 lines. Redaction patterns are configurable via an environment variable — not hardcoded. Pure-shell JSON helpers with Python fallback ifjqis absent.print_credentials()wrapping output in<<>>markers as specified in the prompt.render_template()for config files, no Jinja dependency. Password generation excluding ambiguous characters (0/O/1/l/I). The only implementation that anticipates every edge case documented in the development prompt.

Model Ddelivers 184 lines. The benchmark's most original idea: exit codes encapsulated in named functions —exit_input_error(),exit_conflict()— more readable than bareexit 3calls. Andjson_output()directly incommon.sh, generating API-ready JSON from shell. No atomic writes, norequire_cmd().

The bugs you find yourself — or don't

Model C tests its own code during the session. After writingschemas.py, it runs it with test cases, finds two bugs, and fixes them immediately: a Pydantic v2 validator implemented incorrectly (field_validatorinstead ofmodel_validatorfor cross-field validation), and a mutual exclusion not enforced at the schema level. It also fixes asedsubstitution issue inrender_template()— broken on/in paths — replaced with pure bash parameter expansion.

At the end of its session, Model C delivers a verification summary:bash -non all scripts, Python AST on all files, 19/19 API routes verified via OpenAPI spec, 18/18 bash helpers tested, PHP fallback rule verified (8.5→8.4, 8.4→none, 7.x rejected).

Model A checks its shebangs before finishing. Model B delivers polished user documentation — troubleshooting, curl examples, quick start. Model D validates bash and Python syntax. None of the three test functional logic.

Code phase costs

Model

Tokens

Time

Code cost

Total

A

—

2m58s

$0

$0

D

1.29M

9m42s

~$0.19

$0.24

B

—

~15m

Pro subscription

$20/month

C

4.42M

23m37s

$1.67

$1.73

Model D delivers in 9m42s what Model C delivers in 23m37s — but without functional tests. Model C consumes 3.4x more tokens because it executes code during the session, reloading context at each iteration.

## 5. External review — and the reveal

Four implementations, four approaches to security. To settle it without bias, the code review was handed to a model absent from the benchmark, with a fixed grid on five criteria. Five representative files per implementation —common.sh,site-create.sh,site-delete.sh,backup.sh,api/runner.py— twenty files loaded in a single pass.

Review cost: $0.0766 for 543k tokens. Ten times cheaper than an hour of junior dev time.

Per-file observations

Onsite-create.sh, the reviewer finds a silent bug in Model D: the SFTP password is generated but never captured or returned to the caller. The user never sees their credentials. Core functionality is broken with no error message. On Model B,localis used outside a function in three scripts — a bash error that causes runtime failure. These aren't subtle bugs: they're blockers.

Onsite-delete.sh, Model C is the only one handling both call modes — interactive TTY and a--confirmflag for non-interactive API calls. Model D only implements interactive mode, blocking API-driven deletion with skip-backup.

Onbackup.sh, Models A and B useeval "$POST_HOOK"— potential command injection. Model C passes the archive path as an argument — safer. Model A doesn't implement automatic archive pruning.

Onapi/runner.py, Model C is the only one usingasyncioand never logging stdout — which may contain credentials. Model D has dead code:build_command()defined but never called. Model A delivers 28 lines with no timeout, no logging, no error handling — a hung request blocks the API indefinitely.

The verdict

Criterion

A

B

C

D

Security

3/5

3/5

5/5

2/5

Correctness

3/5

2/5

5/5

2/5

Idempotency

3/5

3/5

5/5

3/5

Code quality

3/5

2/5

5/5

3/5

Completeness

3/5

2/5

5/5

2/5

Total

15/25

12/25

25/25

12/25

Production-ready as-is: one out of four. Model C, 25/25.

The reveal

Alias

Model

Tool

Total cost

A

BigPickle

OpenCode

$0

B

Haiku 4.5

Claude Code

Pro subscription

C

GLM 5.2

OpenCode

$1.73

D

DeepSeek V4 Pro

OpenCode

$0.24

Model B — Claude Code + Haiku 4.5 — is the most expensive in real marginal cost, with a Pro subscription at $20/month minimum. It scores 12/25 and isn't deployable due to fundamental bash bugs. Model C — GLM 5.2, from THUDM lab at Tsinghua University — scores 25/25 and is the only one the reviewer judges production-ready. It cost $1.73.

### Addendum — Model E: Kimi K2.7 Code

Added after publication following a reader comment pointing to the model. Same protocol, same development prompt, same Qwen 3.7 Plus review grid.

Alias

Model

Tool

Total cost

E

Kimi K2.7 Code

OpenCode

$0.859

External review score: 19/25

Criterion

E

Security

3/5

Correctness

4/5

Idempotency

4/5

Code quality

4/5

Completeness

4/5

Production-ready: No.Blocking issue: database passwords are passed inline as arguments tomysql -eandpsql -c— visible in/proc/*/cmdlineto any user on the system. The fix is straightforward (MYSQL_PWD/PGPASSWORDas environment variables), but it isn't applied.

The most modular architecture in the benchmark according to the reviewer — cleanlib/split, consistent idempotency patterns. But the security gap prevents it from challenging GLM 5.2.

Position in the ranking:between DeepSeek V4 Pro ($0.24, 12/25) and GLM 5.2 ($1.73, 25/25) on both axes. Better architecture/cost ratio than models B and D, but not production-ready.

## 6. Intelligent routing — the real economics

This benchmark raises an implicit question: do you need GLM 5.2 for everything?

No. And that's probably the most useful conclusion of the exercise.

GLM 5.2 at $1.40/M tokens is the right choice when complexity justifies it — architecture, security, cross-file consistency, critical decisions. But on a real project, those tasks represent a fraction of interactions. The rest is boilerplate, minor corrections, documentation, commit messages.

Three levels, three models

BigPickle scores 15/25 on a complete 32-file implementation. It's perfectly capable of reading 50 lines of diff and writing an adequate commit message. Of debugging a1064 You have an error in your SQL syntaxor aFatal error: Call to undefined function. Of generating a README from existing code. For these tasks, GLM 5.2's architectural depth is overkill — and BigPickle is free.

DeepSeek V4 Pro at $0.44/M tokens — five times cheaper than Haiku 4.5 and three to four times cheaper than GLM 5.2 — comfortably handles simple code generation, CRUD, minor refactoring, inline documentation, short scripts. Its code phase at $0.24 for 1.29M tokens and 9m42s demonstrates this.

GLM 5.2 comes in when complexity exceeds that scope — architecture design, coherent multi-file implementation, security decisions, non-trivial business logic.

Level

Model

Cost

Typical use cases

Free

BigPickle

$0

Debug, commits, quick questions, SQL errors

Budget

DeepSeek V4 Pro

$0.44/M

Boilerplate, CRUD, documentation, short scripts

Premium

GLM 5.2

$1.40/M

Architecture, security, multi-file consistency

The proportion of tasks at each level depends on the project, where you are in the development cycle, and what you consider complex. No universal number — each team calibrates against their real usage.

“💡Worth noting: GLM 5.2 is exponentially more expensive than BigPickle — $1.67 vs $0 for 4.42M tokens in the code phase. But pure text output — plans, architecture, analysis — consumes few tokens and costs almost nothing: $0.06 for this benchmark's planning phase. It's in the code phase, with its iterations, in-session test execution, and accumulating context, that the bill climbs. Intelligent routing means precisely reserving GLM 5.2 for tasks that justify that long context — and handing everything else to the two lower tiers.”

The uncomfortable comparison

GitHub switched to token billing on June 1, 2026. Claude Sonnet 4.6 on Copilot is billed at roughly $3.00/M tokens input and $15.00/M output. Reproducing the GLM 5.2 session from this benchmark — 4.46M tokens — would cost an estimated $25 on Copilot + Sonnet 4.6. Without the functional tests. Without the self-correction. Without the external review.

Copilot Pro+ at $39/month includes $39 in AI credits. A full session like this one would consume two-thirds of the monthly budget. Users reported burning through their monthly credits in two prompts on the day the switch happened.

The final ratio:$1.94 all in vs ~$25 on Copilot + Sonnet. Thirteen times cheaper, for the only result the external reviewer judges production-ready.

## Conclusion

$1.94. That's what this benchmark cost end to end — planning, implementation, external review included. For the only toolkit the reviewer judges production-ready.

That number is uncomfortable for the AI coding tools market, which sells reassurance through pricing. Copilot Pro+ at $39/month, Claude Sonnet at $15/M tokens output, the big names front and center — the implicit assumption is that quality follows price. This benchmark suggests otherwise.

The winner is called GLM 5.2. Its lab, THUDM, is part of Tsinghua University. You probably haven't seen it in last week's comparisons. It produced the only architecture with a normalized exit code convention from the planning phase, the only implementation that tests its own code during the session, the onlycommon.shwith configurable redaction and Python fallback ifjqis absent. And it fixed three bugs before delivering.

Two takeaways.

First: a model's price does not predict its output quality on complex tasks. Haiku 4.5 on three different tools — Claude Code, Copilot CLI, OpenCode — produces identical results for identical cost. On the planning phase — pure text generation, no feedback loop, no codebase exploration — the tool has no measurable impact. What matters is the model. And the least glamorous model in the benchmark dominates.

Second: not all tokens are equal. A planning phase at $0.06, a code phase at $1.67 — that's a factor of 28. It's not an anomaly, it's the structure of the problem. A plan is a few thousand tokens of reasoning. An implementation is millions of tokens of accumulated context, executed code, iterated tests. Routing intelligently between BigPickle at $0, DeepSeek V4 Pro at $0.44/M, and GLM 5.2 at $1.40/M based on task complexity — that's the real economics of these tools.

The VPS Manager toolkit is available on GitHub in all four versions.

## pcescato/LLM-Challenge

# LLM-Challenge

A reproducible benchmark comparing 8 AI coding agent/model combinations on the same real-world project.

## What this is

This repository contains the complete artifacts from a benchmark where 8 different AI coding agent/model combinations were tasked with building the same VPS management toolkit. The goal was to measure code quality, architecture decisions, and production readiness across different tools and models under identical conditions.

This is not a marketing comparison. A real project with concrete requirements was used as the test subject, and the results were evaluated by an external reviewer who had no knowledge of which tool or model produced which implementation.

## The protocol

The benchmark followed a two-phase protocol:

Phase 1: ArchitectureAll tools received the same functional brief and were asked to produce an architecture document. No code was written in this phase.

Phase 2: ImplementationAll tools received the same development prompt and were asked to implement…

View on GitHub

The briefs, prompts, and evaluation grid are there too. Reproducible, if you want to verify.

Too cheap to be good? That was the wrong question.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (50 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.
 Some comments have been hidden by the post's author -find out more

For further actions, you may consider blocking this person and/orreporting abuse
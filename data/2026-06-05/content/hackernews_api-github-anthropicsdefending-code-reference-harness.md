---
title: 'GitHub - anthropics/defending-code-reference-harness: Skills for threat modeling, scanning, triage, patching, plus an autonomous scanning harness you can /customize · GitHub'
url: https://github.com/anthropics/defending-code-reference-harness
site_name: hackernews_api
content_file: hackernews_api-github-anthropicsdefending-code-reference-harness
fetched_at: '2026-06-05T12:03:56.003295'
original_url: https://github.com/anthropics/defending-code-reference-harness
author: binyu
date: '2026-06-04'
description: Skills for threat modeling, scanning, triage, patching, plus an autonomous scanning harness you can /customize - anthropics/defending-code-reference-harness
tags:
- hackernews
- trending
---

anthropics

 

/

defending-code-reference-harness

Public

* NotificationsYou must be signed in to change notification settings
* Fork149
* Star1.9k

 
 
 
 
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

6 Commits
6 Commits
.claude/
skills
.claude/
skills
 
 
bin
bin
 
 
docs
docs
 
 
harness
harness
 
 
scripts
scripts
 
 
static
static
 
 
targets
targets
 
 
tests
tests
 
 
.gitignore
.gitignore
 
 
CLAUDE.md
CLAUDE.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
pyproject.toml
pyproject.toml
 
 
View all files

## Repository files navigation

# Defending Code Reference Harness

A reference implementation for autonomous vulnerability discovery and
remediation with Claude, based on our learnings frompartnering with security
teams at several organizationssince launching Claude Mythos Preview. For a write up of these learnings along with
best practices, see theaccompanying blog post(also available inblog-post.md). For a lightweight SDK-only
walkthrough of the same recon → find → triage → report → patch loop, see thecompanion cookbook.

This repo is not maintained and is not accepting contributions.

🔒Want a managed option?Anthropic offersClaude Security, a hosted product
that finds and fixes vulnerabilities in your source code across multiple
projects. Claude Security scans your repository for vulnerabilities,
applies a multi-stage verification pipeline to reduce false positives, and
lets you manage findings through their lifecycle: triage, fix validation,
and rapid fix generation.

This repository is an open-source reference implementation based on general
best practices for finding vulnerabilities using Claude. You can use it to
build your own vulnerability finding pipeline, customize the logic, and it
can be used with whatever access you have to Claude APIs (including
Bedrock, Vertex, or Azure).

## Contents

* Claude Code skills:/quickstart,/threat-model,/vuln-scan,/triage,/patch,/customize: interactive scoping, scanning, triage,
and patching. Open this repo in Claude Code and run/quickstartto get
oriented.
* harness/: the autonomous reference pipeline (recon → find → verify
→ report → patch), configured for finding C/C++ memory vulnerabilities
using Docker and ASAN. This harness is areference, not a product.
The general shape, prompts, and sandboxing are reusable, but the harness
will not work on every codebase out of the box. Run/customizeto port it
to your language, detector, or vuln class.

⚠️Security:/quickstart,/threat-model,/vuln-scan, and/triageonly read and write files. Running/patchon static findings (TRIAGE.jsonorVULN-FINDINGS.json) is likewise read- and write-only./customizeedits
the harness code and runs validation commands. Any of these skills are safe to
run unsandboxed, as long as you review and approve each tool use in Claude Code.
The autonomous reference pipeline (including/patchon pipeline results)executes target code, so it refuses to run outside of a gVisor sandbox
unless explicitly overridden. To get set up, runscripts/setup_sandbox.shonce,
then invoke the pipeline viabin/vp-sandboxed. Seedocs/security.mdanddocs/agent-sandbox.mdfor more details.

## Getting Started

git clone https://github.com/anthropics/defending-code-reference-harness

cd
 defending-code-reference-harness
claude

#
 30-sec intro + guided first run on the canary target

>
 /quickstart

>
 /quickstart how 
do
 I port the pipeline to Java
?

>
 /quickstart how 
do
 I triage all these bugs
?

## Further Reading

* Blog Post· The accompanying blog post with learnings + best practices
* Pipeline· How it works: diagram, stages, CLI flags
* Security· Sandboxing, what not to mount
* Agent sandbox· gVisor isolation + egress allowlist for every agent
* Customize· Port to my stack; which files change and why
* Patching· Generate and verify fixes for verified crashes
* Troubleshooting· Duplicates, rate limits, subagent model pinning
* Safeguards· Block for dangerous cyber work

## Ramp Up

The most successful security teams we've partnered with are those
that have gotten hands-on the fastest. Though it's tempting to
spend months designing the perfect pipeline, we recommend starting
small on Day 1 and building from there as learnings come. The
steps below follow that pattern and set an ambitious (but reasonable)
pace based on what we've seen.

Step 1

Day 1

Build a threat model and run your first static scan + triage

Step 2

Day 2

Run the reference pipeline on a C/C++ library

Step 3

Days 3-5

Customize the pipeline for your target

Step 4

Week 2

Start autonomous scanning, triage, and patching

### Step 1 (Day 1): Build a threat model and run your first static scan + triage

Day 1 is focused on seeing the whole loop end-to-end. Using only the
interactive skills, you'll build a threat model, run a static scan scoped
by it, triage what comes back, and draft candidate fixes. You'll finish
the day with a threat model, a ranked list of static findings, and candidate
patches.

The relevant skillsonly read and write filesin your repo. As long as you
run Claude Code interactively and approve each tool use, no sandbox is needed.

#
 Pin every subagent to the model you want

export
 CLAUDE_CODE_SUBAGENT_MODEL=
<
model-id
>

claude

#
 0. intro + guided first run

>
 /quickstart

#
 1. Build a threat model (aim before you shoot)

>
 /threat-model bootstrap targets/canary

#
 2. Run a static scan, scoped by that threat model

>
 /vuln-scan targets/canary

#
 3. Verify, dedupe, and rank what came back

>
 /triage targets/canary/VULN-FINDINGS.json

#
 4. Generate candidate fixes for the verified findings

>
 /patch ./TRIAGE.json --repo targets/canary

This flow producesTHREAT_MODEL.md,VULN-FINDINGS.{json,md},TRIAGE.{json,md}, andPATCHES/.

The vulnerability candidates produced in Step 1 come from Claude's static
review of the source (nothing is built or run), so expect more false positives on
any non-canary targets. In Step 2, you'll produceexecution-verifiedfindings.

Note:on the canary target,/triagemay dismiss the scan's findings
as false positives.entry.cannounces itself as deliberately vulnerable
demo code, and/triagecorrectly excludes bugs in test / fixture code.
To see the full confirm / dedupe / false positive flow, run it on the
curated fixture instead (/triage .claude/skills/triage/fixtures/canary-findings.json --repo targets/canary) or point the Step 1 skills at your own code.

### Step 2 (Day 2): Run the reference pipeline on a C/C++ library

On Day 2, you'll move from interactive skills to your first autonomous
run using the reference pipeline. You'll run the full recon → find →
verify → report loop in your environment on a known-vulnerable open-source
library, then generate a candidate patch for what it finds. You'll finish
with a set of reproducible crashes, exploitability reports, and candidate patches,
along with a feel for how the pipeline works.

Running the pipeline is simple:

#
 One-time setup

python3 -m venv .venv 
&&
 .venv/bin/pip install -e 
.

./scripts/setup_sandbox.sh 
#
 installs gVisor, builds the agent images, and verifies isolation; note: requires Docker

export
 ANTHROPIC_API_KEY=sk-ant-... 
#
 or CLAUDE_CODE_OAUTH_TOKEN; the pipeline requires one in env

#
 Run the recon → find → verify → report loop

bin/vp-sandboxed run drlibs --model 
<
model-id
>
 --runs 3 --parallel --stream --auto-focus

#
 Generate a candidate patch for each finding

bin/vp-sandboxed patch results/drlibs/
<
timestamp
>
/ --model 
<
model-id
>

#
 Or, ask Claude Code to launch the pipeline and watch the run for you

claude

>
 run the pipeline on drlibs and explain findings as they come

Results from the loop land in aresults/drlibs/<timestamp>/directory. With
the--streamflag, the first report will appear in minutes underreports/bug_NN/.

⚠️runspawns autonomous agents.The pipeline runs each agent
inside a gVisor container with egress restricted to the Claude API.
Agent-spawning subcommands refuse to start outside it unless explicitly
overridden. For more information, seedocs/security.mdanddocs/agent-sandbox.md.

Under the hood, the pipeline walks through seven stages:

1. Build: Compiles the target into a Docker image with ASAN (the memory
error detector for C and C++). The pipeline builds this image automatically
on first run using the target'sDockerfile.
2. Recon: A lightweight agent reads the source inside a network-isolated
container and proposes a partition, i.e.,"here are N distinct input-parsing
subsystems worth attacking separately", so that parallel find agents explore
different areas instead of converging on the same bug. Without the--auto-focusflag, the pipeline uses thefocus_areaslist from the target'sconfig.yaml.
3. Find: N agents run in parallel, each in its own isolated container.
Each agent reads the source, crafts malformed inputs, and runs the ASAN
binary until a given input produces a crash 3 out of 3 times.
4. Verify: A separate grader agent reproduces each crash in a fresh
container that the find agent hasn't touched. The only thing that crosses over
from the find agent to the grader is the proof of concept it produced.
5. Dedupe: A judge agent compares verified crashes against bugs already
reported and decides whether each is a new bug, a better example of a known
bug, or a duplicate to skip.
6. Report: A report agent writes a structured exploitability analysis per
unique bug, including details on primitive class, reachability, escalation
path, and severity.
7. Patch(the separate patch command above): A patch agent writes a proposed
fix, and a grader agent confirms that the new code builds, that the original
proof of concept input no longer crashes, that the target's test suite still
passes, and that a fresh find agent can't find a way around the fix.

For more details, seedocs/pipeline.md.

### Step 3 (Days 3-5): Customize the pipeline for your target

On Days 3-5, you'll customize the harness for your own target. First, you'll
point the Step 1 skills at your code, then you'll use/customizeto port the
pipeline to your stack. By the end of the week, you'll have atargets/<your-service>/directory that the pipeline can run against, validated with a single smoke run
of the pipeline, and ready to scale up in Step 4.

While the reference pipeline is designed for finding memory vulnerabilities in C and C++
code, its shape is generic. Porting it to a new vuln class or language just means
answering the following questions for your target stack:

Question

C/C++ Reference

Your target (examples)

What signals a finding?

ASAN crash signature

exception / canary file / DNS callback

What does a proof of concept look like?

crashing input file

HTTP request sequence / tx list / test harness

How is the target built and run?

Dockerfile
 (using clang + ASAN)

your language's build in a container

Before customizing, point the Step 1 skills at your own code. As a reminder,
they're read- and write-only, so they can run unsandboxed.

claude

>
 /quickstart how 
do
 I customize this 
for
 
~
/code/my-service
?

>
 /threat-model bootstrap-then-interview 
~
/code/my-service

>
 /vuln-scan 
~
/code/my-service

>
 /triage 
~
/code/my-service/VULN-FINDINGS.json --repo 
~
/code/my-service

Then, use the artifacts produced by those skills in the/customizeskill,
which modifies the harness for your codebase.

>
 /customize use 
~
/code/my-service/{THREAT_MODEL.md,VULN-FINDINGS.json} and ./TRIAGE.md

When/customizeis done, you'll have atargets/my-service/directory
set up. Validate it with a smoke run of the pipeline before scaling up.

bin/vp-sandboxed run my-service --model 
<
model-id
>
 --runs 1

For more details, seedocs/customizing.md.

### Step 4 (Week 2): Start autonomous scanning, triage, and patching

In Week 2, you'll use the pipeline you customized in Step 3 on your own
targets, adding anouterloop to the inner pipeline loop - run multiple
pipeline scans, triage the findings from across those runs, patch based
on prioritization, and repeat.

#
 Scan - run a wave of parallel runs against your target

bin/vp-sandboxed run my-service --model 
<
model-id
>
 --runs 5 --parallel --stream --auto-focus

#
 Triage - dedupe and rank every finding across all waves using your threat model

>
 /triage results/my-service/ --repo 
~
/code/my-service --auto --votes 5

#
 Patch - generate and validate fixes, starting with what triage ranked the highest

>
 /patch results/my-service/
<
timestamp
>
/ --model 
<
model-id
>

⚠️Follow the same sandboxing guidelines as inStep 2

A given pipeline run already verifies and deduplicates its own findings./triageworks across many pipeline runs. When pointed at theresults/directory, it collapses duplicates across all runs (and any static findings
from/vuln-scanif present), recalibrates severity ratings against your
threat model, and attempts to route every finding to the component owner.

When possible, patching findings quickly helps keep the outer loop as
productive as possible. When findings are fixed, the model can't re-find
them, and instead will surface net new, typically deeper issues. As you run
more pipeline waves, the number of findings will likely go down, but the
complexity will likely also go up. If quick patching isn't possible, even
just recording prior findings in the target'sknown_bugscan help steer
future runs toward newer bugs.

Autonomous triage and patching are still open issues, and this reference
harness doesn't fully solve them. The verification strategies in/patchhelp raise the bar, but severity and prioritization are ultimately
judgments about your environment, and verified patches are not always
upstreamable. Many partners have reported these steps as their current
bottlenecks, and you should budget real engineering time for them.

For more details, seedocs/triage.mdanddocs/patching.md.

## Looking Forward

After the initial ramp up, the teams we've worked with have tended to invest in a
few directions:

1. Reviewing all their internal repos and key open-source dependencies,
ranking which are the most important to scan (e.g., based on their exposure,
history of CVEs, business-criticality), then working through scanning the
list in priority order.
2. Setting up bespoke infrastructure for scanning to move scans off of laptops
or one-off VMs. The most successful teams resist the urge to build the perfect
scanning platform before scaling up.
3. Incorporating scans into their SDLC. Some teams have set up recurring scans
(e.g., daily, weekly) or have added scanning into their CI pipelines.
4. Testing and experimenting with the models to find what works best for them.

## About

Skills for threat modeling, scanning, triage, patching, plus an autonomous scanning harness you can /customize

claude.com/blog/using-llms-to-secure-source-code

### Topics

 security

### Resources

 Readme

 

### License

 View license
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

1.9k

 stars
 

### Watchers

8

 watching
 

### Forks

149

 forks
 

 Report repository

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python92.7%
* Shell3.5%
* C2.5%
* Dockerfile1.3%
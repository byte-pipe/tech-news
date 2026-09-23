---
title: Claude Code reads AGENTS.md only when telemetry is on · blog.szypowi.cz
url: https://blog.szypowi.cz/p/claude-code-reads-agents.md-only-when-telemetry-is-on/
site_name: hackernews_api
content_file: hackernews_api-claude-code-reads-agentsmd-only-when-telemetry-is
fetched_at: '2026-09-23T15:19:23.193273'
original_url: https://blog.szypowi.cz/p/claude-code-reads-agents.md-only-when-telemetry-is-on/
author: pszypowicz
date: '2026-09-23'
published_date: '2026-09-23T12:00:00+02:00'
description: Claude Code 2.1.277 added AGENTS.md support, but the loader sits behind a remote feature flag. With telemetry or nonessential traffic turned off, a local AGENTS.md is skipped without a warning. This is what I measured and the one-line CLAUDE.md I use instead.
tags:
- hackernews
- trending
---

Claude Code 2.1.277 announced support forAGENTS.md. In a project with noCLAUDE.md, it is supposed to readAGENTS.mdinstead. I keep telemetry off in my shell, and in my repos the file never loaded.Issue #95690explains why, and I addedmy own measurementsto it. This post collects them in one place.

## Where the gate is

The loader ships as a built-in plugin calledagents-md. Its registration in the 2.1.280 bundle looks like this:

var
 
W
 
=
 
!
1
;

var
 
B
 
=
 
()
 
=>
 
Oa
(
"tengu_agents_md_mod"
,
 
W
);

var
 
H
 
=

 
"AGENTS.md as project instructions: by default loaded where the project has no CLAUDE.md; ..."
;

Wis the plugin’sisOnByDefaultvalue and it isfalse.BisisAvailable, and it asks a remote feature flag calledtengu_agents_md_mod, withfalseas the fallback. When Claude Code cannot fetch the flag, the plugin is unavailable, and the local file is never read. Reading a markdown file from the working directory needs no network at all, but here it waits on a server-side switch.

## How I tested it

I made an empty directory that holds only anAGENTS.mdwith a canary word in it, and askedclaude -pfor the word. Each setup ran in two sessions, because the first session in a new configuration only fetches the flag and the second one uses it.

echo
 
'The canary word is PERIWINKLE.'
 > AGENTS.md

claude -p 
'What is the canary word from the project instructions? Answer NONE if you have none. Do not read files.'

## What I measured

* CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1blocks the feature, as the issue says.
* DISABLE_TELEMETRY=1blocks it too. With either variable set,AGENTS.mdnever loaded, so I had to clear both.
* Setting either variable to0does not help. The block stays in place. The environment variable docs say that any value counts, but that is easy to miss when you try to turn a feature on.
* Anenvblock in the project’s.claude/settings.jsonthat clears both variables has no effect. There is no way to turn the feature on for a single repo.
* A session-level override does work from the second session on:
claude --settings 
'{"env":{"DISABLE_TELEMETRY":"","CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC":""}}'

None of these cases print a warning. The session starts, the model answers without the project instructions, and nothing tells you that a file was skipped. The issue also points out that third-party gateways, Bedrock and Vertex have the same problem, because the flag cannot resolve to true there either.

## The workaround

CLAUDE.mdsupports@pathimports, and those do not depend on the flag. A one-lineCLAUDE.mdnext to theAGENTS.mdloads it with telemetry off:

echo
 
'@AGENTS.md'
 > CLAUDE.md

With that file in place, the same canary test returns the word withCLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1still set. The cost is one extra file per repo, which is what theAGENTS.mdsupport was supposed to remove.

## Why I think this is unacceptable

I turned telemetry off on purpose, and I expect that choice to cost me some diagnostics and nothing else. Here it silently costs me a feature that reads a file from my own disk. A remote flag can make sense for a feature that talks to a server, but the only input this one needs is already in the working directory.

The gate also hits the people who are most likely to care aboutAGENTS.md. Someone who keeps one instruction file for several agents is usually careful about what each tool sends home, and teams on Bedrock, Vertex or a gateway often disable nonessential traffic by policy. They all get a feature that is announced as available and then does nothing.

The silence is the worst part. I confirmed the cause with a canary word and a string search through the binary, and most people will not do that. They will conclude that the model ignores their instructions, and they will spend time on prompts when the file never reached the model in the first place.

A privacy setting should never quietly switch off unrelated local behavior. If Anthropic wants a staged rollout, the fallback for a flag that cannot be fetched should be the documented behavior, or at least a visible message that says what was skipped and why.

## What I would like to see

* Reading a local file should not depend on telemetry. If the gate has to stay for a gradual rollout, a startup warning when anAGENTS.mdis present and skipped would save people the time I spent on a canary test.
* A globalAGENTS.md. The plugin looks forAGENTS.mdand.claude/AGENTS.mdin project directories only, and there is no user-level file next to the userCLAUDE.md. Codex reads a global~/.codex/AGENTS.md, and the/importcommand in Claude Code can copy it into the userCLAUDE.md, but the copy does not follow later edits. If you keep one set of personal instructions for several agents, you still need an@import in the userCLAUDE.mdthat points at the shared file.
* Native support for shared agent skills. Codex reads skills from.agents/skillsin the project and from~/.agents/skillsin the home directory. Claude Code 2.1.280 knows those paths only in/import, which copies the skills into.claude/skills. I put a canary skill in.agents/skillsand Claude Code did not list it, but it listed the same skill from.claude/skillsin the same repo. A copy drifts from the source, so I link.claude/skillsto../.agents/skillsinstead, and Claude Code follows that symlink.

Until then, I use the one-lineCLAUDE.mdfor instructions and a symlink for skills.
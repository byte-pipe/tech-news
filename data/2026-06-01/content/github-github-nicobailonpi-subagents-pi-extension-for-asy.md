---
title: 'GitHub - nicobailon/pi-subagents: Pi extension for async subagent delegation with truncation, artifacts, and session sharing · GitHub'
url: https://github.com/nicobailon/pi-subagents
site_name: github
content_file: github-github-nicobailonpi-subagents-pi-extension-for-asy
fetched_at: '2026-06-01T04:17:16.567759'
original_url: https://github.com/nicobailon/pi-subagents
author: nicobailon
description: Pi extension for async subagent delegation with truncation, artifacts, and session sharing - nicobailon/pi-subagents
---

nicobailon

 

/

pi-subagents

Public

* NotificationsYou must be signed in to change notification settings
* Fork253
* Star1.8k

 
 
 
 
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

257 Commits
257 Commits
.github/
workflows
.github/
workflows
 
 
agents
agents
 
 
prompts
prompts
 
 
skills/
pi-subagents
skills/
pi-subagents
 
 
src
src
 
 
test
test
 
 
.gitignore
.gitignore
 
 
CHANGELOG.md
CHANGELOG.md
 
 
README.md
README.md
 
 
banner.png
banner.png
 
 
install.mjs
install.mjs
 
 
package.json
package.json
 
 
View all files

## Repository files navigation

# pi-subagents

pi-subagentslets Pi delegate work to focused child agents. Use it for code review, scouting, implementation, parallel audits, saved workflows, background jobs, and anything else that benefits from a second or third set of model eyes.

pi-subagents-chain.mp4

## Installation

pi install npm:pi-subagents

That is the only required step. You can add optional pieces later.

## Try this first

You do not need to create agents, write config, or learn slash commands. After installing, ask Pi for delegation in plain language:

Use reviewer to review this diff.

Ask oracle for a second opinion on my current plan.

Use scout to understand this code based on our discussion then ask me clarification questions.

Run parallel reviewers: one for correctness, one for tests, and one for unnecessary complexity.

That is enough to start.

## What happens

Pi is the parent session. A subagent is a focused child Pi session with its own job.

When you ask for a subagent, Pi starts the child, gives it the task, and brings the result back. Foreground runs stream in the conversation. Background runs keep working and can be checked later.

Installing the extension does not start an automatic reviewer in the background. It gives Pi a delegation tool. If you want every implementation reviewed, say that in your prompt or put it in your project instructions:

When you finish implementing, run a reviewer subagent before summarizing.

## Good first prompts

These cover most day-to-day use:

Ask oracle for a second opinion on my current plan. Challenge assumptions and tell me what I might be missing.

Use oracle to help solve this hard bug. Have it inspect the code and propose the best next move before we edit anything.

Run parallel reviewers on this diff. I want one focused on correctness, one on tests, and one on unnecessary complexity.

Have worker implement this approved plan. Afterward, run parallel reviewers, summarize their feedback, and apply the fixes that make sense.

Run a review loop on this change until reviewers stop finding fixes worth doing, with a max of 3 rounds.

Use scout to understand the auth flow, then have planner turn that into an implementation plan.

Those are ordinary Pi requests. Pi decides whether to callsubagent, which agent to use, and whether a chain or parallel run makes sense.

## Common workflows

Want

Ask naturally

Get a second opinion

“Ask oracle to review this plan and challenge assumptions.”

Solve a hard problem

“Use oracle to investigate this bug before we edit.”

Review a diff

“Use reviewer to review this diff.”

Run parallel reviewers

“Run reviewers for correctness, tests, and cleanup.”

Implement then review

“Implement this, then review it.”

Review until clean

“Run a review loop on this change with a max of 3 rounds.”

Execute a plan carefully

“Have worker implement this approved plan, then run reviewers and apply the feedback.”

Scout before planning

“Use scout to inspect the auth flow before planning.”

Run in the background

“Run this in the background.”

Browse agents

“Show me the available subagents.”

Use a saved workflow

“Run the review chain on this branch.”

See running work

“Show active async runs.”

Check setup

“Check whether subagents are configured correctly.”

The extension ships with builtin agents you can use immediately.

## Builtin agents in plain English

Agent

Use it when you want...

scout

Fast local codebase recon: relevant files, entry points, data flow, risks, and where another agent should start.

researcher

Web/docs research with sources: official docs, specs, benchmarks, recent changes, and a concise research brief.

planner

A concrete implementation plan from existing context. It should read and plan, not edit code.

worker

Implementation work, including approved oracle handoffs. It edits files, validates, and escalates unapproved decisions instead of guessing.

reviewer

Code review and small fixes. It checks the implementation against the task/plan, tests, edge cases, and simplicity.

context-builder

A stronger setup pass before planning: gathers code context and writes handoff material such as 
context.md
 and 
meta-prompt.md
.

oracle

A second opinion before acting. It challenges assumptions, catches drift, and recommends the safest next move without editing.

delegate

A lightweight general delegate when you want a child agent that behaves close to the parent session.

A simple rule of thumb: usescoutbefore you understand the code,researcherbefore you trust external facts,plannerbefore a bigger change,workerto implement,reviewerto check, andoraclewhen the decision itself feels risky.

## Changing a builtin agent's model

Builtin agents inherit your current Pi default model by default. This keeps new installs from depending on a provider you may not have configured. If you want a role to use a specific model, set an override instead of copying the bundled agent file.

For one run, put the override in the command:

/run reviewer[model=anthropic/claude-sonnet-4:high] "Review this diff"

For a persistent override, edit settings. This example pins the reviewer everywhere, adds a backup model for provider failures, and keeps the other builtins on your normal default model:

{
 
"subagents"
: {
 
"agentOverrides"
: {
 
"reviewer"
: {
 
"model"
: 
"
anthropic/claude-sonnet-4
"
,
 
"thinking"
: 
"
high
"
,
 
"fallbackModels"
: [
"
openai/gpt-5-mini
"
]
 }
 }
 }
}

Use~/.pi/agent/settings.jsonfor a user override or.pi/settings.jsonfor a project override. The sameagentOverridesblock can changetools,skills, inherited context, prompt text, or disable a builtin. If you want a totally different agent, create a user or project agent with the same name; for normal tweaks, prefer overrides.

## Where running subagents show up

Foreground runs stream progress in the conversation while they run.

Background runs keep working after control returns to you. Inspect active runs withsubagent({ action: "status" }), or a specific run withsubagent({ action: "status", id: "..." }).

They also show a compact async widget and send completion notifications. Parallel background runs show per-agent progress instead of fake chain steps. Chains with parallel groups keep their grouped shape in progress and results, so failed or paused agents stay visible next to completed ones. When a child is explicitly allowed to fan out withtools: subagent, its nested runs appear under that parent child in the main status tree instead of being hidden inside the child process.

You can also ask naturally:

Show me the current async runs.

If something feels misconfigured, run:

/subagents-doctor

or ask:

Check whether subagents and intercom are set up correctly.

## Recommended orchestration pattern (scaffolding)

Use orchestration as parent-agent guidance, not as a runtime workflow mode. For implementation work, the recommended loop is:

clarify → planner → worker → fresh reviewers → worker

Use the optional prompt shortcuts below when you want the pattern to be repeatable.

Packagedplanner,worker, andoracledefault to forked context when a launch omitscontext; passcontext: "fresh"when you intentionally want a fresh child run.

Child-safety boundaries are enforced at runtime. Spawned child sessions do not receive the bundledpi-subagentsskill, and forked child context filtering removes parent-only subagent artifacts (including old hidden orchestration-instruction messages, slash/status/control messages, and prior parentsubagenttool-call/tool-result history) while preserving ordinary prose and unrelated tool calls/results. By default, children do not register thesubagenttool and receive boundary instructions that they are not the parent orchestrator and must not propose or run subagents. The explicit exception is an agent whose resolved builtintoolsincludessubagent; that child gets a child-safesubagenttool for the fanout work the parent assigned, still bounded bymaxSubagentDepth.

## Optional shortcuts

The package includes reusable prompt templates for common workflows. You do not need them, but they are handy when you want the same shape every time:

Prompt

Use it for

/parallel-review

Launch fresh-context reviewers with distinct angles, then synthesize what to fix.

/review-loop

Run parent-controlled worker, reviewer, and fix-worker cycles until clean or capped.

/parallel-research

Combine 
researcher
 and 
scout
 for external evidence, local code context, and practical tradeoffs.

/parallel-context-build

Run 
context-builder
 agents in parallel to produce planning handoff context and meta-prompts.

/parallel-handoff-plan

Combine external research and 
context-builder
 passes into an implementation handoff plan and meta-prompt.

/gather-context-and-clarify

Scout/research first, then ask the user the clarification questions that matter.

/parallel-cleanup

Run review-only cleanup passes after implementation.

Addautofixto/parallel-reviewor/parallel-cleanupto apply only the synthesized fixes worth doing now after reviewers return.

## Optional pi-intercom companion

pi-subagentsworks withoutpi-intercom. Installpi-intercomonly if you want child agents to talk back to the parent Pi session while they are running.

pi install npm:pi-intercom

Most users do not callintercomdirectly. Afterpi-intercomis installed,pi-subagentscan automatically give child agents a private coordination channel back to the parent session. The bridge recognizes the normalpi install npm:pi-intercompackage install as well as legacy local extension checkouts.

Use it for work where the child might need a decision instead of guessing:

Run this implementation in the background. If the worker gets blocked or needs a product decision, have it ask me through intercom.

Ask oracle to review this plan. If it sees a decision I need to make, have it ask me instead of assuming.

The child can use one dedicated coordination tool:

* contact_supervisor: the child contacts the parent/supervisor session that delegated the task. Usereason: "need_decision"for blocking decisions or clarification, andreason: "progress_update"for short non-blocking updates when a discovery changes the plan. Do not ask for clarification when the only conflict is review-only/no-edit versus progress-writing or artifact-writing instructions; no-edit wins.

Child-side routine completion handoffs are still not expected. With the intercom bridge active, parent-sidepi-subagentssends grouped completion results throughpi-intercom: one grouped message per foreground parentsubagentrun and one per completed async result file. Acknowledged foreground delivery returns a compact receipt with artifact/session paths; if unacknowledged, the normal full output is preserved. Grouped messages include child intercom targets, full child summaries, and compact nested child summaries under the parent child that launched them.

If a child appears stalled, needs-attention notices can show up in the parent session with useful next actions, such as checkingsubagent({ action: "status" }), interrupting the run, or nudging the child.

If messages do not show up, run:

/subagents-doctor

For normal use, you do not need to configure anything. Advanced users can tune the bridge withintercomBridgein the configuration section below.

At this point, you know enough to use the plugin. The rest of this README is reference material for exact command syntax, custom agents, saved chains, worktrees, and configuration.

## Direct commands

Skip this section until you want exact syntax.

Command

Description

/run <agent> [task]

Run one agent; omit the task for self-contained agents

/chain agent1 "task1" -> agent2 "task2"

Run agents in sequence

/parallel agent1 "task1" -> agent2 "task2"

Run agents in parallel

/run-chain <chainName> -- <task>

Launch a saved 
.chain.md
 or 
.chain.json
 workflow

/subagents-doctor

Show read-only setup diagnostics

Commands validate agent names locally, support tab completion, and send results back into the conversation.

### Per-step tasks

Use->to separate steps and give each step its own task:

/chain scout "scan the codebase" -> planner "create an implementation plan"
/parallel scanner "find security issues" -> reviewer "check code style"

Both double and single quotes work. You can also use--as a delimiter:

/chain scout -- scan code -> planner -- analyze auth

Steps without a task inherit behavior from the execution mode. Chain steps get{previous}, the prior step’s output. Parallel steps use the first available task as a fallback.

/chain scout "analyze auth" -> planner -> worker
# scout gets "analyze auth"; planner gets scout output; worker gets planner output

For a shared task, list agents and place one--before the task:

/chain scout planner -- analyze the auth system
/parallel scout reviewer -- check for security issues

### Inline per-step config

Append[key=value,...]to an agent name to override defaults for that step:

/chain scout[output=context.md] "scan code" -> planner[reads=context.md] "analyze auth"
/run scout[model=anthropic/claude-sonnet-4] summarize this codebase
/parallel reviewer[skills=code-review+security] "review backend" -> reviewer[model=openai/gpt-5-mini] "review frontend"

Key

Example

Description

output

output=context.md

Write results to a file. For 
/chain
 and 
/parallel
, relative paths live under the chain directory; for 
/run
, relative paths resolve against cwd.

outputMode

outputMode=file-only

Return only a concise file reference for saved output instead of the full saved content. Requires 
output
; default is 
inline
.

reads

reads=a.md+b.md

Read files before executing. 
+
 separates multiple paths.

model

model=anthropic/claude-sonnet-4

Override model for this step.

skills

skills=planning+review

Override injected skills. 
+
 separates multiple skills.

progress

progress

Enable progress tracking.

Setoutput=false,reads=false, orskills=falseto disable that behavior explicitly. Do not useoutput=falsefor file-only returns; useoutputMode=file-onlywith anoutputpath.

### Background and forked runs

Add--bgto run in the background:

/run scout "audit the codebase" --bg
/chain scout "analyze auth" -> planner "design refactor" -> worker --bg
/parallel scout "scan frontend" -> scout "scan backend" --bg

Add--forkto start each child from a real branched session created from the parent’s current leaf:

/run reviewer "review this diff" --fork
/chain scout "analyze this branch" -> planner "plan next steps" --fork
/parallel scout "audit frontend" -> reviewer "audit backend" --fork

You can combine them in either order:

/run reviewer "review this diff" --fork --bg
/run reviewer "review this diff" --bg --fork

Background runs are detached. If the parent agent has other independent work, it should keep working. If it has nothing useful to do until the background result arrives, it should end the turn instead of running sleep or status-polling loops. Pi will deliver the completion when the run finishes.

Theoracleandworkerbuiltins are designed for an explicit decision loop. A typical pattern is to askoraclefor diagnosis and a recommended execution prompt, then only runworkerafter the main agent approves that direction.

## Clarify and launch UI

Chains open a clarify UI by default so you can preview and edit the workflow before it runs. Single and parallel tool calls can opt into the same flow withclarify: true; slash commands launch directly.

Common clarify keys:

* Enterruns in the foreground, or in the background if background is toggled on
* Esccancels or backs out
* ↑↓moves between steps or tasks
* eedits the task/template
* mselects a model
* tselects thinking level
* sselects skills
* btoggles background execution
* wedits output/write behavior where supported
* redits reads where supported
* ptoggles progress tracking where supported
Picker screens use↑↓,Enter,Esc, and type-to-filter. The full-screen editor supports word wrapping, paste,Escto save, andCtrl+Cto discard.

## Agents and chains

Agents are markdown files with YAML frontmatter and a system prompt body. They define the specialist that will run in the child Pi process.

Agent locations, lowest to highest priority:

Scope

Path

Builtin

~/.pi/agent/extensions/subagent/agents/

User

~/.pi/agent/agents/**/*.md

Project

.pi/agents/**/*.md

Project discovery also reads legacy.agents/**/*.mdfiles. Nested subdirectories are discovered recursively..chain.mdfiles do not define agents. If both.agents/and.pi/agents/define the same parsed runtime agent name,.pi/agents/wins. UseagentScope: "user" | "project" | "both"to control discovery;bothis the default and project definitions win runtime-name collisions.

Builtin agents load at the lowest priority, so a user or project agent with the same name overrides them. They do not pin a provider model; they inherit your current Pi default model unless you setsubagents.agentOverrides.<name>.model.oracleis an advisory reviewer that critiques direction and proposes an execution prompt without editing files.workeris the implementation agent for normal tasks and approved oracle handoffs.

Theresearcherbuiltin usesweb_search,fetch_content, andget_search_content; those requirepi-web-access:

pi install npm:pi-web-access

### Builtin overrides

You can override selected builtin fields without copying the whole agent. Overrides live in settings:

* User:~/.pi/agent/settings.json
* Project:.pi/settings.json

Example:

{
 
"subagents"
: {
 
"agentOverrides"
: {
 
"reviewer"
: {
 
"inheritProjectContext"
: 
false

 }
 }
 }
}

Supported override fields aremodel,fallbackModels,thinking,systemPromptMode,inheritProjectContext,inheritSkills,defaultContext,disabled,skills,tools, andsystemPrompt. UsedefaultContext: falsein builtin overrides to clear an inherited context default. Project overrides beat user overrides.

Setdisabled: trueto hide a builtin from runtime discovery and agent-facingsubagent({ action: "list" })output. For bulk control, setsubagents.disableBuiltins: truein settings.

### Prompt assembly

Subagents are designed to be narrow by default. Custom agents start with a clean system prompt and only the context you intentionally give them. They do not automatically inherit Pi’s whole base prompt, project instruction files, or discovered skills catalog.

Use these fields when an agent should see more:

Field

Effect

systemPromptMode: append

Append the agent prompt to Pi’s normal base prompt.

inheritProjectContext: true

Keep inherited project instructions from files like 
AGENTS.md
 and 
CLAUDE.md
.

inheritSkills: true

Let the child see Pi’s discovered skills catalog.

defaultContext: fork

Use forked session context when a launch omits 
context
; explicit 
context: "fresh"
 still wins.

Builtin agents opt into project instruction inheritance by default so they follow repo-specific rules out of the box.delegatealso uses append mode because its job is orchestration inside the parent workflow.

### Agent frontmatter

A typical agent looks like this:

---

name
: 
scout

#
 Optional: registers this as code-analysis.scout while preserving name: scout

package
: 
code-analysis

description
: 
Fast codebase recon

tools
: 
read, grep, find, ls, bash, mcp:chrome-devtools

extensions
:

model
: 
claude-haiku-4-5

fallbackModels
: 
openai/gpt-5-mini, anthropic/claude-sonnet-4

thinking
: 
high

systemPromptMode
: 
replace

inheritProjectContext
: 
false

inheritSkills
: 
false

skills
: 
safe-bash, chrome-devtools

output
: 
context.md

defaultReads
: 
context.md

defaultProgress
: 
true

completionGuard
: 
false

interactive
: 
true

maxSubagentDepth
: 
1

---

Your system prompt goes here.

Important fields:

Field

Notes

package

Optional package identifier. A file with 
name: scout
 and 
package: code-analysis
 registers as 
code-analysis.scout
; serialization keeps 
name
 and 
package
 separate.

tools

Builtin tool allowlist. 
mcp:
 entries select direct MCP tools when 
pi-mcp-adapter
 is installed.

extensions

Omitted means normal extensions; empty means no extensions; comma-separated values allowlist specific extensions.

model

Default model. Bare ids prefer the current provider when possible, then unique registry matches.

fallbackModels

Ordered backup models for provider/model failures such as quota, auth, timeout, or unavailable model. Ordinary task failures do not trigger fallback.

thinking

Appended as a 
:level
 suffix at runtime unless a suffix is already present.

systemPromptMode

replace
 by default; 
append
 keeps Pi’s base prompt.

inheritProjectContext

Keeps or strips inherited project instruction blocks.

inheritSkills

Keeps or strips Pi’s discovered skills catalog.

defaultContext

Optional 
fresh
 or 
fork
 launch context default for this agent.

skills

Injects specific skills directly, regardless of 
inheritSkills
.

output

Default single-agent output file.

defaultReads

Files to read before running in chain/parallel behavior.

defaultProgress

Maintain 
progress.md
.

completionGuard

Set 
false
 only for non-implementation agents that may mention implementation words while using mutation-capable tools such as 
bash
.

interactive

Parsed for compatibility but not enforced in v1.

maxSubagentDepth

Tightens nested delegation for this agent’s children.

### Tool and extension selection

Iftoolsis omitted,pi-subagentsdoes not pass--tools, so the child gets Pi’s normal builtin tools. Iftoolsis present, regular tool names become an explicit allowlist.mcp:entries are split out and forwarded as direct MCP selections. Path-liketoolsentries, such as extension paths or.ts/.jsfiles, are treated as tool-extension paths rather than builtin tool names. Agents that declare only known read-only builtin tools skip the implementation completion guard, butbash, unknown tools, and MCP tools stay mutation-capable. UsecompletionGuard: falsefor bash-enabled validators or advisors that should never be judged as implementation agents.

Examples:

* toolsomitted andextensionsomitted: normal builtins and normal extensions.
* tools: mcp:chrome-devtools: normal builtins plus direct Chrome DevTools MCP tools.
* tools: read, bash, mcp:chrome-devtools: onlyreadandbashas builtins, plus direct Chrome DevTools MCP tools.
* tools: subagent, read: a child-safesubagenttool is available inside that child so it can run explicitly assigned nested fanout.

Direct MCP tools requirepi-mcp-adapter. Subagents only receive direct MCP tools whenmcp:entries are listed in their frontmatter; globaldirectTools: trueinmcp.jsonis not enough by itself. The genericmcpproxy tool can still be used for discovery when available. The adapter caches tool metadata at startup, so after connecting a new MCP server for the first time, restart Pi before relying on direct tools. Anmcp:entry namedsubagentdoes not authorize nested fanout; only the builtinsubagenttool name does.

extensionscontrols child extension loading:

#
 Omitted: all normal extensions load

#
 Empty: no extensions

extensions
:

#
 Allowlist

extensions
: 
/abs/path/to/ext-a.ts, /abs/path/to/ext-b.ts

Whenextensionsis present, it takes precedence over extension paths implied bytoolsentries.

## Chain files

Chains are reusable workflows stored separately from agent files. Use.chain.mdfor simple sequential saved chains. Use.chain.jsonwhen a chain needs dynamic fanout.

Scope

Path

User

~/.pi/agent/chains/**/*.chain.md
, 
~/.pi/agent/chains/**/*.chain.json

Project

.pi/chains/**/*.chain.md
, 
.pi/chains/**/*.chain.json

Nested subdirectories are discovered recursively. If both.chain.mdand.chain.jsondefine the same parsed runtime chain name in the same scope,.chain.jsonwins. If user and project scopes define the same parsed runtime chain name, the project chain wins. Chains support the same optionalpackagefrontmatter as agents;name: review-flowpluspackage: code-analysisruns ascode-analysis.review-flow.

Example:

---

name
: 
scout-planner

description
: 
Gather context then plan implementation

---

## 
scout

phase: Context
label: Map auth flow
as: context
output: context.md

Analyze the codebase for {task}

## 
planner

phase: Planning
label: Implementation plan
reads: context.md
model: anthropic/claude-sonnet-4-5
:
high

progress: true

Create an implementation plan based on {outputs.context}

Each.chain.md## agent-namesection is a step. Config lines such asphase,label,as,outputSchema,output,outputMode,reads,model,skills, andprogressgo immediately after the header. A blank line separates config from task text. In saved.chain.mdfiles,outputSchemais a path to a JSON Schema file; direct tool calls and.chain.jsonfiles can pass the schema object inline.

Foroutput,reads,skills, andprogress, chain behavior is three-state: omitted inherits from the agent, a value overrides, andfalsedisables.

Usephaseto group related work in status output,labelfor a readable step name, andasto store a successful step or parallel task result for later{outputs.name}references. Duplicateasnames, invalid identifiers, and unknown output references fail before child execution.

Dynamic fanout is available only through directsubagent({ chain: [...] })JSON or saved.chain.jsonfiles. It expands an array from a prior structured named output, runs one child template per item, and stores the ordered collection undercollect.as. The source must be structured output; prose is never parsed.expand.maxItemsis required, over-limit arrays fail, nested fanout and arbitrary expressions are not supported, and.chain.mdhas no dynamic syntax in this release.

{
 
"name"
: 
"
dynamic-review
"
,
 
"description"
: 
"
Find review targets, fan out reviewers, then synthesize.
"
,
 
"chain"
: [
 {
 
"agent"
: 
"
scout
"
,
 
"task"
: 
"
Return {
\"
items
\"
:[{
\"
path
\"
:
\"
...
\"
,
\"
reason
\"
:
\"
...
\"
}]} via structured_output.
"
,
 
"as"
: 
"
targets
"
,
 
"outputSchema"
: { 
"type"
: 
"
object
"
 }
 },
 {
 
"expand"
: {
 
"from"
: { 
"output"
: 
"
targets
"
, 
"path"
: 
"
/items
"
 },
 
"item"
: 
"
target
"
,
 
"key"
: 
"
/path
"
,
 
"maxItems"
: 
12

 },
 
"parallel"
: {
 
"agent"
: 
"
reviewer
"
,
 
"label"
: 
"
Review {target.path}
"
,
 
"task"
: 
"
Review {target.path}. Reason: {target.reason}
"
,
 
"outputSchema"
: { 
"type"
: 
"
object
"
 }
 },
 
"collect"
: { 
"as"
: 
"
reviews
"
 },
 
"concurrency"
: 
4

 },
 {
 
"agent"
: 
"
worker
"
,
 
"task"
: 
"
Synthesize fixes from {outputs.reviews}
"

 }
 ]
}

Create simple.chain.mdchains by writing files directly or with thesubagent({ action: "create", config: ... })management action. Create dynamic.chain.jsonchains by writing the JSON file directly. Run saved chains with natural language or:

/run-chain scout-planner -- refactor authentication

## Chain variables

Task templates support:

Variable

Description

{task}

Original task from the first step.

{previous}

Output from the prior step, or aggregated output from a parallel step.

{chain_dir}

Path to the chain artifact directory.

{outputs.name}

Text value from a prior step or completed parallel task with 
as: "name"
.

Parallel outputs are aggregated with clear separators before being passed to the next step:

=== Parallel Task 1 (worker) ===
...

=== Parallel Task 2 (worker) ===
...

## Skills

Skills areSKILL.mdfiles injected into an agent’s system prompt.

Discovery uses project-first precedence:

1. .pi/skills/{name}/SKILL.md
2. Project packages and project settings packages viapackage.json -> pi.skills
3. Current task cwd package viapackage.json -> pi.skills
4. .pi/settings.json -> skills
5. ~/.pi/agent/skills/{name}/SKILL.md
6. User packages and user settings packages viapackage.json -> pi.skills
7. ~/.pi/agent/settings.json -> skills

Use agent defaults, override them at runtime, or disable them:

{
 
agent
: 
"scout"
,
 
task
: 
"..."
 
}

{
 
agent
: 
"scout"
,
 
task
: 
"..."
,
 
skill
: 
"tmux, safe-bash"
 
}

{
 
agent
: 
"scout"
,
 
task
: 
"..."
,
 
skill
: 
false
 
}

For chains,skillat the top level is additive. A step-levelskilloverrides that step;falsedisables skills for that step.

Injected skills use this shape:

<
skill
 
name
=
"
safe-bash
"
>
[skill content from SKILL.md, frontmatter stripped]
</
skill
>

Missing skills do not fail execution. The result summary shows a warning.

### Bundled skill

The package bundles api-subagentsskill that is automatically available to the parent agent when the extension is installed. It is for the orchestrating parent only: child subagents never receive it, and their context is explicitly filtered to strip parent-only orchestration instructions.

What the bundled skill covers:

* Delegation patterns: when to launch which agent, whether to use single, parallel, chain, or async mode, and whether to use fresh or forked context
* Prompt workflow recipes: how to apply the packaged techniques directly withsubagent(...)when the user describes the workflow in natural language instead of invoking a slash command. This includes parallel review, review-loop, parallel research, parallel context-build, parallel handoff-plan, gather-context-and-clarify, and parallel cleanup
* Role-agent prompting guidance: compact contract prompts instead of long scripts, what to include in role-specific meta prompts, and retrieval budgets for researchers
* Safety boundaries: child agents must not run subagents unless their resolved builtin tools explicitly includesubagent, must not invent intercom targets, and must escalate unapproved decisions
* Intercom conventions: when to ask vs send, and how parent-side result delivery works withpi-intercom
* Control and diagnostics: attention signals, soft interrupts, status, and thedoctoraction

If you are writing an agent that orchestrates subagents, the bundled skill helps it behave correctly without guessing the patterns. If you are a human user, you do not need to read it directly; the README and prompt shortcuts encode the same workflows in user-facing form.

## Programmatic tool usage

These are the parameters the LLM passes when it calls thesubagenttool. Most users ask naturally or use slash commands instead.

### Execution examples

// Single agent

{
 
agent
: 
"worker"
,
 
task
: 
"refactor auth"
 
}

{
 
agent
: 
"scout"
,
 
task
: 
"find todos"
,
 
maxOutput
: 
{
 
lines
: 
1000
 
}
 
}

{
 
agent
: 
"scout"
,
 
task
: 
"investigate"
,
 
output
: 
false
 
}

{
 
agent
: 
"scout"
,
 
task
: 
"write a large report"
,
 
output
: 
"reports/scout.md"
,
 
outputMode
: 
"file-only"
 
}

// Forked context

{
 
agent
: 
"worker"
,
 
task
: 
"continue this thread"
,
 
context
: 
"fork"
 
}

// Parallel

{
 
tasks
: 
[
{
 
agent
: 
"scout"
,
 
task
: 
"a"
 
}
,
 
{
 
agent
: 
"reviewer"
,
 
task
: 
"b"
 
}
]
 
}

{
 
tasks
: 
[
{
 
agent
: 
"scout"
,
 
task
: 
"audit auth"
,
 
count
: 
3
 
}
]
 
}

{
 
tasks
: 
[
{
 
agent
: 
"scout"
,
 
task
: 
"audit frontend"
 
}
,
 
{
 
agent
: 
"reviewer"
,
 
task
: 
"audit backend"
 
}
]
,
 
context
: 
"fork"
 
}

// Chain

{
 
chain
: 
[

 
{
 
agent
: 
"scout"
,
 
task
: 
"Gather context for auth refactor"
 
}
,

 
{
 
agent
: 
"planner"
 
}
,

 
{
 
agent
: 
"worker"
 
}
,

 
{
 
agent
: 
"reviewer"
 
}

]
}

// Chain in the background, suitable for unblocking the main chat

{
 
chain
: 
[
...
]
,
 
async
: 
true
 
}

// Chain with fan-out/fan-in

{
 
chain
: 
[

 
{
 
agent
: 
"scout"
,
 
task
: 
"Gather context"
,
 
phase
: 
"Context"
,
 
label
: 
"Map code"
,
 
as
: 
"context"
 
}
,

 
{
 
parallel
: 
[

 
{
 
agent
: 
"worker"
,
 
task
: 
"Implement feature A from {outputs.context}"
,
 
label
: 
"Feature A"
,
 
as
: 
"featureA"
 
}
,

 
{
 
agent
: 
"worker"
,
 
task
: 
"Implement feature B from {outputs.context}"
,
 
label
: 
"Feature B"
,
 
as
: 
"featureB"
 
}

 
]
,
 
concurrency
: 
2
,
 
failFast
: 
true
 
}
,

 
{
 
agent
: 
"reviewer"
,
 
task
: 
"Review {outputs.featureA} and {outputs.featureB}"
 
}

]
}

// Dynamic fanout from structured output

{
 
chain
: 
[

 
{

 
agent
: 
"scout"
,

 
task
: 
"Return review targets as structured_output: { items: [{ path, reason }] }"
,

 
as
: 
"targets"
,

 
outputSchema
: 
{
 
type
: 
"object"
 
}

 
}
,

 
{

 
expand
: 
{
 
from
: 
{
 
output
: 
"targets"
,
 
path
: 
"/items"
 
}
,
 
item
: 
"target"
,
 
key
: 
"/path"
,
 
maxItems
: 
12
 
}
,

 
parallel
: 
{
 
agent
: 
"reviewer"
,
 
task
: 
"Review {target.path}. Reason: {target.reason}"
,
 
outputSchema
: 
{
 
type
: 
"object"
 
}
 
}
,

 
collect
: 
{
 
as
: 
"reviews"
 
}
,

 
concurrency
: 
4

 
}
,

 
{
 
agent
: 
"worker"
,
 
task
: 
"Synthesize fixes from {outputs.reviews}"
 
}

]
 
}

// Strict structured output for reliable handoff data

{
 
chain
: 
[

 
{

 
agent
: 
"scout"
,

 
task
: 
"Return the key files and risks for {task}"
,

 
as
: 
"scan"
,

 
outputSchema
: 
{

 
type
: 
"object"
,

 
required
: 
[
"files"
,
 
"risks"
]
,

 
properties
: 
{

 
files
: 
{
 
type
: 
"array"
,
 
items
: 
{
 
type
: 
"string"
 
}
 
}
,

 
risks
: 
{
 
type
: 
"array"
,
 
items
: 
{
 
type
: 
"string"
 
}
 
}

 
}

 
}

 
}
,

 
{
 
agent
: 
"planner"
,
 
task
: 
"Plan from this scan: {outputs.scan}"
 
}

]
 
}

// Worktree isolation

{
 
tasks
: 
[

 
{
 
agent
: 
"worker"
,
 
task
: 
"Implement auth"
 
}
,

 
{
 
agent
: 
"worker"
,
 
task
: 
"Implement API"
 
}

]
,
 
worktree
: 
true
 
}

### Management actions

Agent definitions are not loaded into context by default. Management actions let the LLM discover, inspect, create, update, and delete agents and chains at runtime.

{
 
action
: 
"list"
 
}

{
 
action
: 
"list"
,
 
agentScope
: 
"project"
 
}

{
 
action
: 
"get"
,
 
agent
: 
"scout"
 
}

{
 
action
: 
"get"
,
 
agent
: 
"code-analysis.scout"
 
}

{
 
action
: 
"get"
,
 
chainName
: 
"review-pipeline"
 
}

{
 
action
: 
"create"
,
 
config
: 
{

 
name
: 
"Code Scout"
,

 
package
: 
"code-analysis"
,

 
description
: 
"Scans codebases for patterns and issues"
,

 
scope
: 
"user"
,

 
systemPrompt
: 
"You are a code scout..."
,

 
systemPromptMode
: 
"replace"
,

 
inheritProjectContext
: 
false
,

 
inheritSkills
: 
false
,

 
model
: 
"anthropic/claude-sonnet-4"
,

 
fallbackModels
: 
[
"openai/gpt-5-mini"
,
 
"anthropic/claude-haiku-4-5"
]
,

 
tools
: 
"read, bash, mcp:github/search_repositories"
,

 
extensions
: 
""
,

 
skills
: 
"parallel-scout"
,

 
thinking
: 
"high"
,

 
output
: 
"context.md"
,

 
reads
: 
"shared-context.md"
,

 
progress
: 
true

}
}

{
 
action
: 
"create"
,
 
config
: 
{

 
name
: 
"review-pipeline"
,

 
description
: 
"Scout then review"
,

 
scope
: 
"project"
,

 
steps
: 
[

 
{
 
agent
: 
"scout"
,
 
task
: 
"Scan {task}"
,
 
output
: 
"context.md"
 
}
,

 
{
 
agent
: 
"reviewer"
,
 
task
: 
"Review {previous}"
,
 
reads
: 
[
"context.md"
]
 
}

 
]

}
}

{
 
action
: 
"update"
,
 
agent
: 
"code-analysis.scout"
,
 
config
: 
{
 
model
: 
"openai/gpt-4o"
 
}
 
}

{
 
action
: 
"update"
,
 
chainName
: 
"review-pipeline"
,
 
config
: 
{
 
steps
: 
[
...
]
 
}
 
}

{
 
action
: 
"delete"
,
 
agent
: 
"scout"
 
}

{
 
action
: 
"delete"
,
 
chainName
: 
"review-pipeline"
 
}

createusesconfig.scope, notagentScope.config.nameis the local frontmatter name; optionalconfig.packageregisters the runtime name as{package}.{name}and is saved as separatenameandpackagefrontmatter.updateanddeleteuse the runtime name andagentScopeonly when the same runtime name exists in multiple scopes. To clear optional string fields, includingpackage, set them tofalseor"".

### Parameter reference

Param

Type

Default

Description

agent

string

-

Agent name for single mode, or target for management actions.

task

string

-

Task string for single mode.

action

string

-

list
, 
get
, 
create
, 
update
, 
delete
, 
status
, 
interrupt
, 
resume
, or 
doctor
.

chainName

string

-

Chain name for management actions.

config

object/string

-

Agent or chain config for create/update.

output

string | false

agent default

Override single-agent output file.

outputMode

"inline" | "file-only"

inline

Return saved output inline or as a concise saved-file reference. 
file-only
 requires an 
output
 path.

skill

string | string[] | false

agent default

Override skills or disable all.

model

string

agent default

Override model.

tasks

array

-

Top-level parallel tasks. Supports 
agent
, 
task
, 
cwd
, 
count
, 
output
, 
outputMode
, 
reads
, 
progress
, 
skill
, 
model
, and 
acceptance
.

concurrency

number

config or 
4

Top-level parallel concurrency.

worktree

boolean

false

Create isolated git worktrees for parallel tasks.

chain

array

-

Sequential, static parallel, and dynamic fanout chain steps. Steps and chain parallel tasks support 
phase
, 
label
, 
as
, 
outputSchema
, and 
acceptance
 in addition to the usual execution fields. Dynamic fanout uses 
expand
, one child 
parallel
 template, and 
collect
.

context

fresh | fork

agent default or 
fresh

fork
 creates real branched sessions from the parent leaf. Packaged 
planner
, 
worker
, and 
oracle
 default to 
fork
.

chainDir

string

temp chain dir

Persistent directory for chain artifacts.

clarify

boolean

true for chains

Show TUI preview/edit flow.

agentScope

user | project | both

both

Agent discovery scope. Project wins on collisions.

async

boolean

false

Background execution. For chains, 
clarify: true
 explicitly keeps the run foreground for the clarify UI.

cwd

string

runtime cwd

Override working directory.

maxOutput

object

200KB, 5000 lines

Final output truncation limits.

artifacts

boolean

true

Write debug artifacts.

includeProgress

boolean

false

Include full progress in result.

share

boolean

false

Upload session export to GitHub Gist.

sessionDir

string

derived

Override session log directory.

acceptance

string/object/false

inferred

Override the run's inferred acceptance gates. Use 
"auto"
, 
"attested"
, 
"checked"
, 
"verified"
, 
"reviewed"
, or 
{ level: "none", reason: "..." }
.

context: "fork"fails fast when the parent session is not persisted, the current leaf is missing, or the branched child session cannot be created. It never silently downgrades tofresh. In multi-agent runs, if any requested agent hasdefaultContext: forkand the launch omitscontext, the whole invocation uses forked context; passcontext: "fresh"when you intentionally want a fresh run.

UseoutputMode: "file-only"when a saved output may be large and the parent only needs a pointer. The returned text is a compact reference likeOutput saved to: /abs/report.md (48.2 KB, 2847 lines). Read this file if needed.Failed runs and save errors still return normal inline output for debugging. In chains, later{previous}steps receive the same compact reference when the prior step used file-only mode.

Sequential and parallel chain tasks acceptagent,task,phase,label,as,outputSchema,cwd,output,outputMode,reads,progress,skill, andmodel. Parallel tasks also acceptcount. Parallel step groups acceptparallel,concurrency,failFast, andworktree. IfoutputSchemais present, the child must callstructured_outputwith schema-valid JSON; prose-only completion or invalid JSON fails the step. Validated structured values are preserved on the step result, andasalso exposes a compact text representation through{outputs.name}.

Status and control actions:

subagent
(
{
 
action
: 
"status"
 
}
)

subagent
(
{
 
action
: 
"status"
,
 
id
: 
"<run-id>"
 
}
)

subagent
(
{
 
action
: 
"status"
,
 
id
: 
"<nested-run-id>"
 
}
)

subagent
(
{
 
action
: 
"interrupt"
,
 
id
: 
"<run-id>"
 
}
)

subagent
(
{
 
action
: 
"interrupt"
,
 
id
: 
"<nested-run-id>"
 
}
)

subagent
(
{
 
action
: 
"resume"
,
 
id
: 
"<run-id>"
,
 
message
: 
"follow-up question"
 
}
)

subagent
(
{
 
action
: 
"resume"
,
 
id
: 
"<run-id>"
,
 
index
: 
1
,
 
message
: 
"follow-up for child 2"
 
}
)

subagent
(
{
 
action
: 
"resume"
,
 
id
: 
"<nested-run-id>"
,
 
message
: 
"follow-up for a nested child"
 
}
)

subagent
(
{
 
action
: 
"doctor"
 
}
)

statusresolves exact foreground ids, top-level async ids, and nested run ids before falling back to prefix matching. Nested status shows the root/parent path, nested children, session/artifact paths when known, and nested control commands. Inside child-safe fanout mode, barestatusrequires an id when no local foreground run is active, so children cannot enumerate unrelated top-level async runs. Bareinterruptstill targets only the visible top-level run; interrupting a nested run requires its explicit nested id.

resumesends the follow-up directly when an async child is still reachable over intercom. After completion, it revives the child by starting a new async child from the stored child session file. Multi-child async runs and remembered foreground single, parallel, or chain runs can be revived by passingindexto choose the child. Nested runs can be resumed by nested id when their live route or persisted session metadata is available. Revive starts a new child process from the old session context; it does not restart the same OS process, and it requires the chosen child to have a persisted.jsonlsession file.

## Worktree isolation

Parallel agents can clobber each other if they edit the same checkout.worktree: truegives each parallel child its own git worktree branched fromHEAD.

{
 
tasks
: 
[

 
{
 
agent
: 
"worker"
,
 
task
: 
"Implement auth"
,
 
count
: 
2
 
}
,

 
{
 
agent
: 
"worker"
,
 
task
: 
"Implement API"
 
}

]
,
 
worktree
: 
true
 
}

{
 
chain
: 
[

 
{
 
agent
: 
"scout"
,
 
task
: 
"Gather context"
 
}
,

 
{
 
parallel
: 
[

 
{
 
agent
: 
"worker"
,
 
task
: 
"Implement feature A from {previous}"
 
}
,

 
{
 
agent
: 
"worker"
,
 
task
: 
"Implement feature B from {previous}"
 
}

 
]
,
 
worktree
: 
true
 
}
,

 
{
 
agent
: 
"reviewer"
,
 
task
: 
"Review all changes from {previous}"
 
}

]
}

Requirements:

* run inside a git repo
* working tree must be clean
* node_modules/is symlinked into each worktree when present
* task-levelcwdoverrides must be omitted or match the shared cwd
* configuredworktreeSetupHookmust return valid JSON before timeout

After a worktree parallel step completes, per-agent diff stats are appended to the output and full patch files are written to artifacts. Worktrees and temp branches are cleaned up infinallyblocks.

## Configuration

pi-subagentsreads optional JSON config from~/.pi/agent/extensions/subagent/config.json.

### asyncByDefault

{ 
"asyncByDefault"
: 
true
 }

Makes top-level calls use background execution when the request does not explicitly setasync. Callers can still force foreground withasync: falseunlessforceTopLevelAsyncis enabled.

### forceTopLevelAsync

{ 
"forceTopLevelAsync"
: 
true
 }

Forces depth-0 single, parallel, and chain runs into background mode and bypasses clarify UI by forcingclarify: false. Nested calls keep their own inherited settings.

### parallel

{
 
"parallel"
: {
 
"maxTasks"
: 
12
,
 
"concurrency"
: 
6

 }
}

maxTasksdefaults to8;concurrencydefaults to4. Per-callconcurrencytakes precedence.

### defaultSessionDir

{ 
"defaultSessionDir"
: 
"
~/.pi/agent/sessions/subagent/
"
 }

Session directory precedence is:params.sessionDir, thenconfig.defaultSessionDir, then a directory derived from the parent session. Sessions are always enabled.

### maxSubagentDepth

{ 
"maxSubagentDepth"
: 
1
 }

Controls nested delegation when no inheritedPI_SUBAGENT_MAX_DEPTHis already in effect. Per-agentmaxSubagentDepthcan tighten the limit for that agent’s child runs, but cannot relax an inherited stricter limit. This applies even to children that explicitly declaretools: subagent; at the cap, execution fanout is blocked instead of silently hiding nested work.

### intercomBridge

{
 
"intercomBridge"
: {
 
"mode"
: 
"
always
"
,
 
"instructionFile"
: 
"
./intercom-bridge.md
"

 }
}

Controls whether subagents receive runtime intercom coordination instructions and whetherintercomandcontact_supervisorare auto-added to their tool allowlist when needed.

Fields:

* mode: defaultalways; usefork-onlyto inject only for forked runs, oroffto disable the bridge.
* instructionFile: optional Markdown template replacing the default bridge instructions.{orchestratorTarget}is interpolated. Relative paths resolve from~/.pi/agent/extensions/subagent/.

Bridge activation also requirespi-intercomto be installed and enabled throughpi install npm:pi-intercomor a legacy local extension checkout, a targetable current session name or fallback alias, andpi-intercomin any explicit agentextensionsallowlist.

The default injected guidance tells children to usecontact_supervisorwithreason: "need_decision"when blocked or needing a decision,reason: "progress_update"only for meaningful blocked/progress updates, genericintercomas fallback plumbing, and avoid routine completion handoffs.

### worktreeSetupHook

{
 
"worktreeSetupHook"
: 
"
./scripts/setup-worktree.mjs
"
,
 
"worktreeSetupHookTimeoutMs"
: 
45000

}

The hook runs once per created worktree. Paths must be absolute,~/..., or repo-relative; bare command names are rejected.

stdin is a JSON object withrepoRoot,worktreePath,agentCwd,branch,index,runId, andbaseCommit. stdout must be one JSON object, for example:

{ 
"syntheticPaths"
: [
"
.venv
"
, 
"
.env.local
"
] }

syntheticPathsmust be relative to the worktree root. They are removed before diff capture so helper files do not pollute patches. Tracked files are never excluded; marking a tracked path as synthetic fails setup. Default timeout is30000ms.

## Files, logs, and observability

Each chain run creates a user-scoped temp directory like:

<tmpdir>/pi-subagents-<scope>/chain-runs/{runId}/

It may contain files such ascontext.md,plan.md,progress.md, andparallel-{stepIndex}/.../output.md. Directories older than 24 hours are cleaned up on extension startup.

Debug artifacts live under{sessionDir}/subagent-artifacts/or a user-scoped temp artifact directory. Per task you may see:

* {runId}_{agent}_input.md
* {runId}_{agent}_output.md
* {runId}_{agent}.jsonl
* {runId}_{agent}_meta.json

Metadata records timing, usage, exit code, final model, attempted models, and fallback attempt outcomes.

Session files are stored under a per-run session directory. Withcontext: "fork", each child starts with--session <branched-session-file>produced from the parent’s current leaf. That is a real session fork, not an injected summary.

Async completions notify only the originating session. The result watcher emitssubagent:async-complete, and the extension consumes that event to render completion notifications.

Async runs write:

<tmpdir>/pi-subagents-<scope>/async-subagent-runs/<id>/
 status.json
 events.jsonl
 output-<n>.log
 subagent-log-<id>.md

status.jsonpowers the widget andsubagent({ action: "status" })output.events.jsonlcontains wrapper events plus child Pi JSON events annotated with run and step metadata. Nested fanout status is stored as compact sidecar event/registry metadata and merged into parent status views and result/intercom payloads; full recursive status snapshots are not embedded in parent result files.output-<n>.logis a live human-readable tail. Fallback information is persisted so background runs are debuggable after completion.

## Acceptance Gates

Every run resolves an effective acceptance policy. Callers may omitacceptancefor the inferred default, or set it on single runs, top-level parallel task items, chain steps, static parallel tasks, and dynamic fanout templates.

{

 
agent
: 
"worker"
,

 
task
: 
"Implement the fix"
,

 
acceptance
: 
{

 
level
: 
"verified"
,

 
criteria
: 
[
"Patch the bug without widening scope"
]
,

 
evidence
: 
[
"changed-files"
,
 
"tests-added"
,
 
"commands-run"
,
 
"residual-risks"
,
 
"no-staged-files"
]
,

 
verify
: 
[
{
 
id
: 
"focused"
,
 
command
: 
"npm test"
,
 
timeoutMs
: 
120000
 
}
]

 
}

}

Accepted levels areauto,none,attested,checked,verified, andreviewed.acceptance: "auto"is the default. Read-only reviewer/scout tasks infer lightweight attestation, normal writer tasks infer checked evidence, and async/risky/dynamic writer contexts infer a reviewed gate. To disable gates, prefer{ level: "none", reason: "..." }.

Acceptance provenance is stored separately from child prose:

* claimed: child finished but did not provide structured evidence.
* attested: child returned a structured acceptance report.
* checked: runtime structural checks passed, such as required evidence and no staged files.
* verified: configured runtime verification commands passed. Child-reported command success does not count.
* reviewed: an independent reviewer result is present.
* rejected: attestation, structural checks, verification, or review failed.

Forattestedor stricter levels, the child prompt includes a standardized acceptance section and asks for a fencedacceptance-reportJSON block. Explicit failed gates fail the run. Inferred gates are persisted for observability without breaking older calls that omitacceptance.

## Live progress

Foreground runs show compact live progress for single, chain, and parallel modes: current tool, recent output, token counts, duration, activity freshness, current-tool duration, and chain graph metadata when available.

PressCtrl+Oto expand the full streaming view with complete output per step.

Sequential chains show a flow line likedone scout → running planner. Chains with parallel steps show per-step cards instead. Chain status useslabelandphasemetadata when present, while falling back to agent names for older chains.

## Session sharing

Passshare: trueto export a full session to HTML, upload it to a secret GitHub Gist through yourghcredentials, and return ahttps://shittycodingagent.ai/session/?<gistId>URL.

{
 
agent
: 
"scout"
,
 
task
: 
"..."
,
 
share
: 
true
 
}

This is disabled by default. Session data may contain source code, paths, environment variables, credentials, or other sensitive output. You needghinstalled and authenticated.

## Recursion guard

Subagents can callsubagentonly when their resolved builtin tools explicitly includesubagent. That is meant for delegated fanout agents, not ordinary worker/reviewer children. A depth guard prevents unbounded nesting.

By default, nesting is limited to two levels: main session → subagent → sub-subagent. Deeper calls are blocked with guidance to complete the current task directly. Nested runs appear in the parent status widget andstatusoutput as a tree, andstatus,interrupt, andresumecan target a nested run by its id.

Configure the limit with:

1. PI_SUBAGENT_MAX_DEPTHbefore starting Pi
2. config.maxSubagentDepth
3. maxSubagentDepthin agent frontmatter, which can only tighten the inherited limit

export
 PI_SUBAGENT_MAX_DEPTH=3

export
 PI_SUBAGENT_MAX_DEPTH=1

export
 PI_SUBAGENT_MAX_DEPTH=0

PI_SUBAGENT_DEPTHis internal and propagated automatically. Do not set it manually.

## Events

Async events:

* subagent:async-started
* subagent:async-complete

Intercom delivery events:

* subagent:control-intercom
* subagent:result-intercom

The result watcher emitssubagent:async-complete;src/extension/index.tsregisters the notification handler that consumes it. Control/attention events are surfaced as visible parent notices and persisted for async runs. Withpi-intercom, needs-attention notices and grouped parent-side subagent result deliveries can reach the orchestrator over intercom.

## Prompt-template integration

pi-subagentsworks standalone through natural language, thesubagenttool, slash commands, and the packaged prompt shortcuts listed near the top of this README. If you usepi-prompt-template-model, you can also wrap subagent delegation in your own reusable prompt templates.

Example:

---

description
: 
Take a screenshot

model
: 
claude-sonnet-4-20250514

subagent
: 
browser-screenshoter

cwd
: 
/tmp/screenshots

---

Use url in the prompt to take screenshot: $@

Then/take-screenshot https://example.comswitches to Sonnet, delegates tobrowser-screenshoterwith/tmp/screenshotsas cwd, and restores your model when done. Runtime overrides like--cwd=<path>and--subagent=<name>work too.

For more reusable workflows on top of subagents, including/chain-promptsand compare-style prompts such as/best-of-n, installpi-prompt-template-modelseparately and copy the examples you want into~/.pi/agent/prompts/.

## Runtime files

The main runtime files are:

File

Purpose

src/extension/index.ts

Extension registration, tool registration, message/render wiring.

src/agents/agents.ts

Agent and chain discovery, frontmatter parsing.

src/runs/foreground/subagent-executor.ts

Main execution routing for single, parallel, chain, management, status, interrupt, and doctor actions.

src/runs/foreground/execution.ts

Core foreground 
runSync
 handling.

src/runs/background/subagent-runner.ts

Detached async runner.

src/runs/background/async-execution.ts

Background launch support.

src/runs/background/async-status.ts

Status discovery and formatting for async runs.

src/runs/foreground/chain-execution.ts
 / 
src/agents/chain-serializer.ts

Chain orchestration and 
.chain.md
 parsing.

src/shared/settings.ts

Chain behavior, instructions, and config helpers.

src/runs/shared/worktree.ts

Git worktree isolation.

src/intercom/intercom-bridge.ts

Runtime intercom bridge instructions and diagnostics.

src/extension/schemas.ts
 / 
src/shared/types.ts

Tool schemas, shared types, and event constants.

test/unit/
 / 
test/integration/

Unit and loader-based integration tests.

## About

Pi extension for async subagent delegation with truncation, artifacts, and session sharing

### Resources

 Readme

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

1.8k

 stars
 

### Watchers

5

 watching
 

### Forks

253

 forks
 

 Report repository

 

## Releases78

v0.27.0

 Latest

 

May 30, 2026

 

+ 77 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript99.3%
* JavaScript0.7%
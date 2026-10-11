---
title: 'GitHub - danyuchn/asd-ste100-skill: ASD-STE100 Simplified Technical English rules, repurposed as a Claude Code skill for rewriting ambiguous agent-facing English. · GitHub'
url: https://github.com/danyuchn/asd-ste100-skill
site_name: github
content_file: github-github-danyuchnasd-ste100-skill-asd-ste100-simplif
fetched_at: '2026-10-11T16:32:47.936508'
original_url: https://github.com/danyuchn/asd-ste100-skill
author: danyuchn
description: ASD-STE100 Simplified Technical English rules, repurposed as a Claude Code skill for rewriting ambiguous agent-facing English. - danyuchn/asd-ste100-skill
---

master
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

26 Commits
26 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
examples
examples
 
 
references
references
 
 
scripts
scripts
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SKILL.md
SKILL.md
 
 
View all files

## Repository files navigation

# ASD-STE100 Skill — Simplified Technical English for Agent Output

A Claude Code skill that rewrites dense, ambiguous English intoASD-STE100 Simplified Technical English(STE) — the controlled-language standard the aerospace and defense industry built so aircraft maintenance instructions cannot be misread.

This skill repurposes that same discipline for a different reader: anAI agentparsing another agent's output, a tool description, an error message, or an inter-agent instruction, with no human in the loop to resolve ambiguity.

## Why STE, and Why for Agents

STE exists because a misread instruction on an aircraft can kill people, and the intended readers were often not native English speakers with no author to call for clarification. The standard's fix: one meaning per word, active voice, simple tenses, one instruction per sentence, short sentences, no dropped words.

An LLM agent parsing another agent's output is in a strikingly similar position — no back-channel, no way to ask "did you mean X or Y?" The same rules that keep a mechanic from misreading a torque spec keep a downstream agent from misreading a tool description or an inter-agent message.

## Before / After

Before

After

"This tool will attempt to synchronize state across the various backends that have been configured, and if a conflict is detected it may resolve it automatically depending on the strategy that has been set, or otherwise it will surface the conflict for manual review."

"The tool tries to synchronize state across the configured backends. If it finds a conflict, it reads the configured strategy. If the strategy allows automatic resolution, the tool may resolve the conflict without a user. If the tool does not resolve the conflict, it reports the conflict for manual review."

"An error may have occurred while processing your request due to a possible mismatch in the expected data format, which could be caused by an outdated client version."

"Your request may have failed. The cause may be a data format that does not match what the server expects. An outdated client can cause this mismatch. Check your client version."

More examples, including illustrations of the official STE rules themselves, inexamples/before-after.md.

## What This Skill Does

1. Picks a mode.Strictcovers procedures, error messages, and tool descriptions.STE-flavoredcovers READMEs, PR descriptions, and explanatory prose. STE-flavored keeps the sentence discipline but not the fixed-vocabulary lockdown.
2. Reads the input English text for meaning.
3. Flags every rule violation sentence-by-sentence: ambiguous word choice, present-perfect/complex tense, passive voice with an unclear actor, multi-instruction sentences, oversized noun clusters, dropped words, sentences over length, phrasal verbs, nominalized actions, semicolons, hedge stacks, and marketing adjectives.
4. Rewrites each flagged sentence — without dropping any fact, condition, or scope qualifier from the original. If a shorter phrasing would lose required precision, it keeps the longer phrasing and flags the trade-off instead of silently simplifying.
5. Outputs the rewritten text on its own — no preamble, no mode announcement, no change summary — plus a one-lineKept as-is:note when it deliberately left something unsimplified.

Ask for the reasoning ("show the diff", "which rules did it break") and it outputs a before/after table naming each rule instead.

The structural rules it checks are mechanical — you can point at the word or punctuation mark that breaks each one. The rules that depend on ASD's dictionary are flagged as advisory rather than enforced, and the rules that need taste are left to you.

The linter checks structural patterns only. It does not compare an original text with a rewrite, verify that requirement strength stayed the same, or prove that the rewrite preserved meaning. A zero-violation result means that the configured structural checks found no problems.

The deterministic linter checks semicolons, a short list of soft phrasal verbs (spin up, reach out, dive into, kick off, circle back, touch base), nominalizations, marketing adjectives, passive voice, present-perfect forms (including irregular participles such as "has run"), long sentences, synonym rotation, and dangling conjunctions in supported list items. It does not check noun-cluster length (that needs part-of-speech tagging) and it does not know phrasal verbs outside its list, so "take off the panel" passes. It never flags hedges or modality.

The repo's own prose does not lint clean: the rule tables quote the patterns they forbid, and some sentences run long. Lint it withpython scripts/ste-lint.py --baseline 41 SKILL.mdand read the findings as examples, not defects.

The dangling-conjunction rule checks list markers at the start of a line with zero to three leading spaces and ASCII spaces after the marker. It supports unordered markers-,*, and+, and ordered numeric markers that end in.or), such as1.or1). It checks indented continuation lines up to the final meaningful line. It does not parse list syntax inside blockquotes, lazy continuation, or full nested-list semantics. A standalone line with four or more leading spaces is not treated as a list marker. Within an active list item, indentation at the computed content column is treated as continuation text. Fence detection follows the linter's existing simple rule: a stripped line beginning with three backticks or three tildes toggles the fence state.

The intentionally invalid examples/linter-edge-cases.md file demonstrates incomplete Markdown list items. Run python scripts/ste-lint.py examples/linter-edge-cases.md to confirm that the linter reports the two expected findings. The file is a test fixture and should not be used as compliant STE prose.

It doesnotreproduce ASD's official ~900-word approved dictionary. The standard is free to obtain but not free to redistribute: Issue 9 permits reproduction only with ASD's written authority, or by eight listed categories of organisation that this project does not belong to. This skill applies the underlyingprinciple(plainest available word, used the same way every time) rather than checking against a fixed word list. For certified STE-compliant documentation, use the real standard.

Full rule summary and citations:references/writing-rules.md.

## Installation

### Quick Install (npx skills)

The fastest way to install this skill is theskills CLI— no clone, no path setup. Run it from your project root:

npx skills add danyuchn/asd-ste100-skill

This pulls the skill from the GitHub repo and installs it for the current project. The CLI sends anonymous install telemetry (skill name and timestamp, no personal or device information) to help rank skills on the skills.sh leaderboard. SetDISABLE_TELEMETRY=1to opt out.

Update later withnpx skills update.

### Clone

git clone https://github.com/danyuchn/asd-ste100-skill 
~
/.claude/skills/asd-ste100

This clones the repo into~/.claude/skills/, making the skill available in every Claude Code project. Best for contributors and anyone who wants a live checkout that updates withgit pull.

## Usage

Trigger with a request to simplify or clarify English text:

Disambiguate this tool description
Rewrite this error message so an agent can't misparse it
Apply ASD-STE100 to this instruction

Or paste text and ask Claude to "disambiguate this" / "apply STE100 to this" / "reduce ambiguity in this output."

You get the rewritten text back and nothing else. To see which rules were applied, add "show the diff" or "explain the changes" to the request.

## Scope

Built for: agent-to-agent messages, tool/function descriptions, error messages, system prompts, inter-agent instructions — any English text a machine or non-native reader has to parse without a human to ask.

Not built for: creative writing, marketing copy, or anything where voice and nuance are the point — STE is deliberately flat and literal by design.

One limit worth stating up front: this fixes the form of a text, not its substance. A paragraph with nothing to say comes out short, clean, and still empty.

## Sources

* ASD-STE100 official site
* ASD-STE100 — About STE
* ASD Europe — Simplified Technical English
* Simplified Technical English — Wikipedia
* TechScribe — ASD-STE100 Simplified Technical English

## License

MIT — seeLICENSE.
---
title: Encoding Team Standards
url: https://martinfowler.com/articles/reduce-friction-ai/encoding-team-standards.html
site_name: tldr
content_file: tldr-encoding-team-standards
fetched_at: '2026-04-05T11:12:37.331688'
original_url: https://martinfowler.com/articles/reduce-friction-ai/encoding-team-standards.html
date: '2026-04-05'
description: Encoding Team Standards (8 minute read)
tags:
- tldr
---

# Encoding Team Standards

AI coding assistants respond to whoever is prompting, and the
 quality of what they produce depends on how well the prompter articulates team
 standards. I propose treating the instructions that govern AI interactions
 (generation, refactoring, security, review) as infrastructure: versioned,
 reviewed, and shared artifacts that encode tacit team knowledge into
 executable instructions, making quality consistent regardless of who is at the
 keyboard.

31 March 2026

Rahul Garg

Rahul is a Principal Engineer at Thoughtworks, based in Gurgaon, India.
 He is passionate about the craft of building maintainable software through DDD and Clean Architecture,
 and explores how AI can help teams achieve engineering excellence.

generative AI

This article is part of a series:

Patterns for Reducing Friction in AI-Assisted Development

## Contents

* The Consistency Problem
* Executable Governance
* What This Looks Like
* Surfacing the tacit knowledge.
* Where Standards Meet the Workflow
* Standards as Shared Infrastructure
* Calibration
* Conclusion

When a team has worked together long enough, certain practices become
 invisible. The senior engineer who rejects a pull request does not consult a
 checklist; she recognizes, almost instantly, that the error handling is
 incomplete, that the abstraction is premature, that the naming does not
 follow the team's conventions. The same instincts shape how she prompts an
 AI to generate code, how she frames a refactoring request, what she asks the
 AI to check before she considers a piece of work complete. Ask her to
 explain and she can, but in the moment it is pattern recognition built from
 years of reviews, production incidents, and architectural discussions. This
 tacit knowledge (what to generate, what to check, what to flag, what to
 reject) is the team's most valuable and most fragile asset. It lives in
 people's heads, transfers slowly through pairing and code review, and walks
 out the door when someone leaves.

In earlier work I have described techniques that improve how an
 individual developer collaborates with AI: sharing curated project context,
 structuring design conversations, externalizing decisions into living
 documents. Each helps one person get better results. None of them solve a
 different problem: two developers on the same team, using the same tool,
 same codebase, same project context, producing materially different results.
 The gap is not in what the AI knows about the project. It is in what the AI
 is told todowith that knowledge. The instructions vary by person, and
 they vary across every kind of interaction, not just code review.

The standards that shape how an AI generates code, refactors existing
 systems, checks for security vulnerabilities, or reviews a pull request
 should not be tips shared on Slack or tribal knowledge carried in a senior's
 head. They should be versioned artifacts that encode “how we do things here”
 into a form that executes consistently for everyone.

## The Consistency Problem

When AI-assisted development depends on who is prompting, seniors
 become bottlenecks, not because they write the code, but because they are
 the only ones who know what to ask for.

I have observed this pattern repeatedly. A senior engineer, when asking
 the AI to generate a new service, instinctively specifies: follow our
 functional style, use the existing error-handling middleware, place it inlib/services/, make types explicit, use our logging utility rather thanconsole.log. When asking the AI to refactor, she specifies: preserve the
 public contract, avoid premature abstraction, keep functions small and
 single-purpose. When asking it to check security, she knows to specify:
 check for SQL injection, verify authorization on every endpoint, ensure
 secrets are not hardcoded.

A less experienced developer, faced with the same tasks, asks the AI to
 “create a notification service” or “clean up this code” or “check if this
 is secure.” Same codebase. Same AI. Completely different quality gates,
 across every interaction, not just review.

This is not the junior developer's fault; they have not yet developed
 the instincts. But the inconsistency is expensive. AI-generated code
 drifts from team conventions when one developer prompts and aligns when
 another does. Refactoring quality varies by who requests it. Security
 checks catch different things depending on who frames the question.
 Technical debt accumulates unevenly.

The instinct is to treat this as a skills problem: train the juniors,
 write better documentation, do more pairing. These all help, but they are
 slow and they do not scale. The knowledge exists on the team; it simply
 has no vehicle for consistent distribution. What is needed is a way to
 take what the senior applies instinctively and make it available to
 everyone, not as advice to remember, but as instructions that execute.

This is a systems problem, not a skills problem. And it requires a
 systems solution.

The earlier techniques in this series address what the AIknows.Knowledge
 Priminggives the AI the project's conventions.Design-First
 collaborationbuilds alignment on architecture.Context
 Anchoringmakes that alignment durable across sessions. This article is about
 something different: making the AI apply the team'sjudgment,
 consistently, regardless of who is prompting, across every meaningful
 interaction.

## Executable Governance

Teams have always tried to codify their standards. The challenge has
 always been the gap between documentation and practice. A checklist on a
 wiki depends on someone reading it, remembering it, and applying it
 consistently under time pressure. In my experience, that gap is where most
 codification efforts quietly fail.

AI instructions change this dynamic in an interesting way. A team
 standard encoded as an AI instruction does not depend on someone
 remembering to apply it. The instructionisthe application. When a
 developer generates code using an instruction that embeds the team's
 architectural patterns, or runs a security check that encodes the team's
 threat model, the standards are applied as a side effect of the workflow,
 not as a separate step that requires discipline. The governance is the
 workflow.

I find it useful to think of this as two moves:

From tacit to explicit.The first move is the familiar one: taking
 what the senior knows instinctively and writing it down. The difference is
 that the target format is not a wiki page or a checklist, but a structured
 instruction set that an AI can execute. The act of writing it surfaces
 assumptions that were never articulated. Whatexactlymakes a security
 issue critical versus merely important? These distinctions, often
 intuitive for the senior, must become precise for the AI.

From documentation to execution.The second move is the one that
 matters. Linting rules are versioned config files, not personal
 preferences. CI/CD pipelines are executable definitions, not wiki pages
 describing deployment steps. AI instructions belong in the same category:
 configuration that executes, not documentation that informs. When these
 instructions live in the repository, reviewed through pull requests,
 shared by default, they have the same status as any other piece of team
 infrastructure. The developer does not need to carry the team's full set
 of standards in their head. They invoke an instruction. The team's
 judgment is applied consistently — not because the developer memorized it,
 but because the infrastructure encodes it.

## What This Looks Like

A well-structured executable instruction has a recognizable anatomy:
 four elements, each doing distinct work. This anatomy applies regardless
 of the instruction's purpose.

* Role definition. Not because the AI needs a persona, but because
 the role sets the expertise level and perspective. “Role: senior engineer
 implementing a new service following the team's architectural patterns”
 establishes a different baseline than a generic prompt. The role is the
 lens through which every subsequent instruction is applied.
* Context requirements. What the instruction needs before it can
 operate: the relevant code, access to the project's architectural context,
 any applicable constraints. This makes dependencies explicit rather than
 hoping the developer remembers to provide them.
* Categorized standards. The categories matter more than the
 individual items. For a generation instruction, the categories might be:
 architectural compliance (must follow), convention adherence (should
 follow), and style preferences (nice to have). For a security instruction:
 critical vulnerabilities (blockers), important concerns (must address
 before merge), and advisories (track and evaluate). For a review
 instruction: breaking issues, important findings, and suggestions. This
 priority structure encodes the team'sjudgment, not just their
 knowledge. It tells the AI, and through the AI, the developer, what
 matters most.
* Output format. A structured response with a summary, categorized
 findings, and clear next steps. The format ensures that output from the
 instruction is comparable across runs and across developers, a property
 that matters once multiple people are using the same instructions
 regularly. For generation instructions, this shapes the completeness and
 structure of the code produced — not a findings report, but the
 conventions of the output itself.

The principle applies across the full range of AI interactions. For
 example:

* Generation: encodes how the team builds new code (architecture patterns,
 naming, error-handling, testing expectations) so output aligns from the first
 pass.
* Refactoring: encodes how the team improves existing code (preserve
 contracts, avoid premature abstraction, propose incremental change).
* Security: encodes the team's threat model (what to check and how to
 grade severity) so checks are team-specific rather than generic.
* Review: encodes what the team checks in review (architecture alignment,
 error handling, type safety, conventions) with a consistent severity
 structure.

Keep instructions small and single-purpose. Smaller instructions
 maintain focus, are easier to maintain, and compose flexibly.

## Surfacing the tacit knowledge.

The most interesting part of
 creating these instructions is the extraction process. It amounts to an
 interview with the team's senior engineers, structured around pointed
 questions that span the full development workflow: What architectural
 decisions should never be left to individual judgment? Which conventions
 are corrected most often in generated code? Which security checks are
 applied instinctively? What triggers an immediate rejection in review?
 What separates a clean refactoring from an over-engineered one?

The answers map directly to instruction structures. Non-negotiable
 architectural patterns become generation constraints. Frequent corrections
 become convention checks. Security instincts become threat-model items.
 Review rejections become critical checks. Recurring mistakes become
 anti-patterns to flag. The interviews essentially write the instructions;
 the act of creation is the act of organizing tacit knowledge into
 explicit, prioritized checks.

I have found that this process has value even beyond the resulting
 instructions. On one project, the extraction conversation revealed that
 two senior engineers had quietly different thresholds for what counted as
 a “critical” security concern versus an “important” one, a
 disagreement that had never surfaced because each reviewed different pull
 requests. The act of writing a shared instruction forced the distinction
 to be made explicit. Once a less experienced developer on the team began
 using the resulting instructions, the effect was immediate: their first
 review flagged a missing authorization check on a newly added endpoint,
 exactly the kind of issue that had previously only been caught when a
 senior happened to be the reviewer. The instructions did not make the
 developer more experienced. They made their inexperience less costly.

## Where Standards Meet the Workflow

These instructions are not a single-purpose tool. They apply at
 different points in the development workflow, and the point of application
 shapes their value.

At generation-time, when a developer asks the AI to create a new
 service, implement a feature, or write tests, a generation instruction
 ensures the output follows team conventions from the start. This is where
 encoded standards have the most leverage: they prevent misalignment rather
 than catching it after the fact.

During development, a refactoring instruction keeps improvements
 aligned with team norms, and a security instruction applies the team's
 threat model rather than a generic checklist. The standards are present
 throughout the development process, not bolted on at the end.

At review-time, when a developer finishes a piece of work (whether
 AI-generated or manually written), a review instruction applies the team's
 quality gate. But review-time is thelastopportunity to catch
 misalignment — the earlier in the workflow standards are applied, the
 fewer issues that reach it.

Optionally in CI, some teams extend these instructions into their
 continuous integration pipeline as an automated consistency check.
 CI-level instructions must be fast enough not to slow the pipeline,
 predictable enough to avoid noisy false positives, and maintained with the
 same discipline as any other CI gate.

## Standards as Shared Infrastructure

A prompt on an individual machine is a personal productivity hack. The
 same prompt in the team's repository is infrastructure. The distinction is
 the difference between a personal preference and a team practice.

When it lives in the repository, it inherits the properties of any
 versioned artifact: changes tracked, standards owned collectively, every
 developer working from the same version. Different tools implement this
 differently — custom commands, skills, rules files, project instructions —
 but the underlying property is the same: a versioned, shared artifact that
 the AI executes consistently.

This is how the team comes together to make the standards better. A
 developer who notices that the generation instruction does not specify the
 team's new error-handling pattern submits a PR to update it. A security
 incident reveals a gap in the security instruction; the fix is a commit,
 reviewed and merged like any other infrastructure change. The standards
 are not static rules handed down by a senior and frozen in place. They are
 living artifacts that the whole team maintains, sharpened by practice, and
 improved through the same pull request workflow the team already uses for
 code.

In an earlier article, I described the key shift in context management
 as treating context as infrastructure rather than habit. The same
 principle extends here: the priming document tells the AI how the project
 works; the executable instruction tells the AI how the team works.

There is a real risk that these instructions become another
 documentation graveyard, created with enthusiasm and abandoned within
 months. Repository placement and pull request review mitigate this. An
 instruction that lives in the repo is visible. It appears in diffs. It can
 be referenced in pull request templates. When it drifts from actual
 practice, the drift is visible in the same way that a stale test is
 visible, not because someone audits it, but because it is encountered in
 the normal course of work. The closer the artifact is to the workflow, the
 more likely it is to be maintained.

## Calibration

This approach is most valuable when a team is large enough that
 consistency cannot be maintained through conversation alone. A useful
 heuristic: if AI-assisted output visibly varies in quality depending on
 who is prompting, or if generation and review work is routing through a
 handful of people because they are the only ones who know how to prompt
 effectively, the inconsistency is the signal. Teams of five may not need
 this. Teams of fifteen almost certainly do.

The costs are real. Creating good instructions requires effort — the
 extraction interviews, the drafting, the iteration. Overly prescriptive
 instructions become brittle; they produce false positives on edge cases or
 fight against legitimate variations in approach. There is a maintenance
 burden as standards evolve. And there is a risk of over-engineering: not
 every interaction with AI needs a dedicated instruction.

The right starting point, in my experience, is one instruction. A
 generation or review instruction is usually the highest-value choice; it
 addresses the most common workflow, the widest quality gap, and the most
 visible inconsistency. Additional instructions should follow adoption, not
 precede it.

## Conclusion

This is, at its core, a shift from judgment that lives in people's
 heads to judgment that executes as shared infrastructure. The senior
 engineer's instincts (the patterns she checks, the conventions she
 enforces, the risks she flags) do not have to remain personal and
 unscalable. They can be extracted, encoded into versioned instructions,
 and applied consistently across every developer and every interaction with
 AI.

The mechanism is not new. Teams already do this with linting rules, CI
 pipelines, and infrastructure-as-code. What changes with AI is thescopeof what can be encoded. Linting catches syntax and style. Executable team
 standards can encode architectural judgment, security awareness,
 refactoring philosophy, and review rigor, the kind of knowledge that
 previously transferred only through pairing, mentorship, and years of
 shared experience.

The most interesting property of these standards is that they are
 team-owned. They live in the repository. They evolve through pull
 requests. They improve when practice reveals gaps. Every instruction that
 misses something is an instruction waiting to be updated, and the update
 is a commit that the whole team reviews. The standards are not just the
 output of team knowledge; they are the mechanism through which team
 knowledge gets codified, shared, and refined.

Significant Revisions

31 March 2026:first published

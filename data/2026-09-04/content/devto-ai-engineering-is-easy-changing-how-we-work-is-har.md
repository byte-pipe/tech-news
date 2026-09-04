---
title: AI Engineering Is Easy. Changing How We Work Is Hard - DEV Community
url: https://dev.to/ujja/ai-engineering-is-easy-changing-how-we-work-is-hard-39j4
site_name: devto
content_file: devto-ai-engineering-is-easy-changing-how-we-work-is-har
fetched_at: '2026-09-04T21:14:44.150657'
original_url: https://dev.to/ujja/ai-engineering-is-easy-changing-how-we-work-is-hard-39j4
author: ujja
date: '2026-09-04'
description: 'AI engineering sounds fancy. New terms are everywhere: agentic development, AI-native engineering,... Tagged with ai, agents, softwaredevelopment, architecture.'
tags: '#ai, #agents, #softwaredevelopment, #architecture'
---

Exposes existing software bottlenecks

AI engineering sounds fancy. New terms are everywhere: agentic development, AI-native engineering, spec-driven development, and now AI harness engineering. Underneath all the terminology, though, something genuinely useful is happening. AI can now help with requirements, challenge aPRD, explore UX ideas, reason about architecture, create implementation plans, write code and validate the result.

The obvious question is what AI can do. The more interesting question is whether the way we build software is ready for it.

## The workflow is changing

A workflow we've been exploring breaks development into five stages:requirements, refinement, planning, build and validation. The stages themselves aren't new, but AI can now participate in each one. It can take existing product inputs, help clarify the problem, question assumptions, identify gaps in a PRD and then turn a well-defined requirement into a plan and eventually implementation tasks.

This puts more emphasis on the quality of the requirements. A human involved in a project might understand what “improve the experience” means because they've had several conversations about it. An agent doesn't have that shared history. It needs the problem, scope, constraints, edge cases and expected outcome to be explicit. That doesn't mean writing enormous specifications; it means using AI to help make the requirements precise before we start building.

AI can actually be a useful, slightly annoying reviewer here, asking what happens when something fails, whether a requirement is testable, whether two parts of the document contradict each other and what we haven't considered yet. It can also help compare different versions of a PRD or have one model review another's output, making gaps easier to spot. The important part is that AI is helping us uncover ambiguity, not making the decisions for us.

## Maybe coding isn't the bottleneck

This becomes more interesting when we look at where teams actually spend their time. Complex work can involve several rounds between product, UX, requirements and engineering before development can properly begin. That's often necessary, but it can also create significant bottlenecks. If an AI agent can produce a working implementation quickly, waiting two weeks for a requirement to be clarified becomes a much bigger problem than it used to be.

This suggests that engineers need to be involved earlier rather than receiving requirements only once they're considered finished. UX needs to be part of the conversation early too. A rough prototype or wireframe can expose gaps in a requirement much faster than another round of discussion, and AI makes creating those lightweight prototypes much cheaper. Requirements, UX and technical design can become an iterative loop rather than a series of handoffs.

## More documentation isn't always better

The instinct with AI is often to give it more documentation: more PRDs, more architecture diagrams, more wiki pages and more context. But if several documents describe the same capability differently, we're not really giving the agent better context; we're giving it more ways to get confused.

What the agent needs is a way to navigate the system. A clear project structure, focused documentation, useful agent instructions, architecture decisions that explain why something exists and a well-organised codebase can be far more useful than one giant specification. The goal isn't to give AI everything we know. It is to make it easy for AI to find what it needs when it needs it.

## The ticket might be the problem

AI also makes me question how we slice work. A ticket that takes weeks or months is difficult for an agent to reason about, and arguably isn't a particularly useful unit of work for humans either. “Build authentication” is very different from breaking the problem into password reset, token validation, password updates and the associated tests.

That doesn't mean turning every feature into dozens of tiny tickets. We just need work that has a clear purpose, manageable scope and a definition of done. If something takes months, it might be a project hiding in a Jira costume.

At the same time, not everything needs the full AI lifecycle. A large feature may benefit from structured requirements, refinement, planning and validation, while a small BAU change might only need a prompt and a developer. If we apply the same process to everything, we risk replacing one form of bureaucracy with another. The workflow should match the complexity of the work.

## The agent needs to see the real system

There is also a fairly fundamental requirement:the agent needs to understand the real system. Giving it a PRD without access to the relevant codebase means it is still making assumptions. With the code, it can find existing patterns, understand constraints, reuse functionality and spot when a proposed solution doesn't fit.

Of course, giving AI access to source code introduces security, licensing, privacy and organisational considerations, so AI adoption isn't simply a matter of choosing the right model. Some of the biggest barriers have nothing to do with the model at all.

And once multiple developers and agents are working in parallel, things get even more interesting. Each agent has its own context and can make decisions based on what it currently sees. One agent can change something another doesn't know about, or two agents can make perfectly reasonable decisions that don't work well together. This makes good engineering practices even more important: small changes, clear boundaries, good tests, frequent reviews and consistent project rules.

## So, are we ready?

Probably not completely, and that's fine. We don't need to jump straight into autonomous software development. We can take real pieces of work, try these workflows, see where they break and improve the process as we go.

Because AI isn't just changing how quickly we write code. It is exposing everything around the code that slows us down: unclear requirements, oversized tickets, late UX involvement, documentation drift, handoffs, access restrictions and decisions that take days to make.

That's why I think the idea of anAI harnessis bigger than prompts and agent configuration. The harness is the environment we create around the AI: how we define work, how product, UX and engineering collaborate, how knowledge is structured, how repositories are organised, how work is validated and what access the agent has.

The AI might be the new part, but the way we work around it is what will determine whether it actually makes us faster.

AI engineering is easy. Changing how we work is hard.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (13 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse
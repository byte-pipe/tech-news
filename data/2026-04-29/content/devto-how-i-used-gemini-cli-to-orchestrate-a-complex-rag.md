---
title: How I used Gemini CLI to orchestrate a complex RAG migration - DEV Community
url: https://dev.to/googleai/how-i-used-gemini-cli-to-orchestrate-a-complex-rag-migration-43ga
site_name: devto
content_file: devto-how-i-used-gemini-cli-to-orchestrate-a-complex-rag
fetched_at: '2026-04-29T12:16:38.373160'
original_url: https://dev.to/googleai/how-i-used-gemini-cli-to-orchestrate-a-complex-rag-migration-43ga
author: Remigiusz Samborski
date: '2026-04-28'
description: Building a complex, multi-phase cloud project like a RAG migration is as much about orchestration as... Tagged with gemini, agents, programming, ai.
tags: '#gemini, #agents, #programming, #ai'
---

Building a complex, multi-phase cloud project like a RAG migration is as much about orchestration as it is about code. You have to manage infrastructure (Terraform), backend services (Python), frontend UI (Next.js), data pipelines (BigQuery/AlloyDB), and documentation - all while maintaining a consistent technical strategy.

Standard IDE completions are great for snippets, but they lack the system-level context needed for this kind of engineering. To build this reference architecture, I didn't just use an AI to write code. I used an AI toorchestrate the entire project.

In this final post (see previouspart 1andpart 2), I'll share a behind-the-scenes look at usingGemini CLIwith theConductor extensionto orchestrate this migration.

In this post, you will learn:

* How to leverage terminal-first AI assistants for system-level engineering
* How to implement spec-driven development withthe Conductor extension
* How to use AI-driven Test-Driven Development (TDD) for reliable code generation
* How to collaborate with AI agents using the "Human-in-the-Loop" model

Before we dive into the workflow, let's briefly discuss why orchestration is the next logical step for AI-assisted development.

## The Developer Experience

Let's walk through my development process step-by-step. The entire specification, plan, and implementation logic is available intheconductordirectoryof therag-migrationrepository.

### Spec-driven development with Conductor

Central to my workflow, is the Conductor extension. It's built on the principle ofspec-driven development. Instead of jumping straight into code, we define the "source of truth" in Markdown files.

* Product Definition (product.md):What are we building?
* Tech Stack (tech-stack.md):What tools are we using?
* Tracks Registry (tracks.md):What are the major milestones?
* Implementation Plans (plan.mdfor each of the tracks):What are the step-by-step tasks?
* Workflow (workflow.md):How are we building the solution?

By having these documents in the codebase, the AI agent (Gemini CLI) always has the high-level context it needs to make smart decisions. It's also a good practice to share those with your team so everyone (including AI agents) is on the same page about the project's direction.

### Conductor initialization

The first step for the project initialization is to create product definition and tech stack files. This is handled by running:

/conductor:setup

Enter fullscreen mode

Exit fullscreen mode

Gemini CLI will ask you a series of questions to help you define your project, including:

* What is the name of your product?
* Who are the primary users?
* What is the tech stack you are using?
* What are the major features you want to implement?
* What is the workflow you want to use?

It will then create the initial project structure in theconductordirectory, including theproduct.mdandtech-stack.mdfiles.

### The lifecycle of a track

Each major feature in this project was implemented as a "Track". A typical track lifecycle consists of:

1. Track Initialization (/conductor:newTrack):* The agent creates aspec.mdfile that describes the goals of the track
* The agent maps the existing codebase and validates assumptions
* The agent creates aplan.mdfile that describes the steps needed to achieve the goals
2. Track Execution (/conductor:implement):* The agent iterates through tasks using aPlan -> Act -> Validatecycle
3. Track Completion:* The agent verifies the changes made during the track
* The agent ask for user feedback on the implementation
4. Track Archivization:* Once a track is completed, Gemini CLI archives the track in theconductor/archivedirectory

For example, when I started the initial embeddings track, I initialized it with:

/conductor:newTrack

Enter fullscreen mode

Exit fullscreen mode

Gemini CLI researches the codebase, asks clarifying questions and creates aspec.mdandplan.mdfiles. Only after I review and approve them, the actual implementation starts.

### Terraform for Infrastructure as Code

Myproduct.mdfile instructs Gemini CLI to write Terraform code for all the resources created during the project. This works really well as all the resources are consistently managed by source code and it's easy to spin up a new environment when needed.

You can see all the Terraform files and infrastructure scripts used in the first track in theinfradirectory.

Moreover, in the course of the project creation I instructed Gemini CLI to always runterraform planbeforeterraform apply. Keeping this information in theworkflow.mdfile ensures that such an approach is applied to all tracks.

### TDD with an AI agent

One of the most powerful aspects of this workflow is AI-driven Test-Driven Development (TDD). I didn't just ask the agent to "write the code". It followed a strict protocol:

* Write Failing Tests:The agent defines the expected behavior in a new test file
* Red Phase:It runs the tests and confirms they fail
* Green Phase:It writes the minimum code needed to pass the tests
* Refactor:It refactors the implementation code and the test code to improve clarity, remove duplication, and enhance performance without changing the external behavior.
* Verify Coverage:It verifies that the test coverage meets the project requirements (target: >80% coverage for new code).
* Commit Code Changes:The agent commits code changes related to the task.

This ensures that the AI-generated code isn't just "syntactically correct" but functionally verified against my requirements. This workflow is described in theworkflow.mdfile.

### Checkpoints and quality gates

At the end of every phase, Gemini CLI runs a "Checkpoint" protocol. This includes:

* Automated Verification:Running the full test suite.
* Manual Verification:Providing the user with step-by-step instructions to verify the changes.
* Auditable Records:Attaching a verification report to the git commit usinggit notesand updateplan.mdwith the new commit hash.

Conductor commits demonstrating the checkpoint protocol.

### Effective Human-in-the-Loop

To achieve an effective AI agent-human development synergy I heavily depended on following solutions:

* Gemini CLI in a sandbox with Yolo mode enabled - seemy past articlefor more about it.
* Custom sandbox notifier scriptthat runs in another terminal.

This approach provided safe guardrails and allowed me to jump into work on other projects while the AI was working on this one. I was always able to jump back quickly thanks to timely notifications. Moreover the checkpointing mechanism of Conductor allowed me to always have a possibility to revert unnecessary changes or to restart from a known working state.

I also usedAntigravityto polish the generated code and the documentation. It was particularly helpful for minor tweaks or refactoring of the code that was generated by Gemini CLI.

### Token usage

Throughout the project I used several models (Gemini 3 Pro, Gemini 3 Flash and Gemini 2.5 Flash Lite). The total token consumption was:

* Input tokens: ~19M
* Cached input tokens: ~66M
* Output tokens: ~400k

Notice the high number of cached input tokens, which significantly impacts the spend. The total Vertex AI token cost wasaround $30. Not bad for several days of AI assisted work.

See thepricing pagefor more details and please mind that your mileage may vary.

## Summary

Software engineering is evolving from writing code to orchestrating agentic workflows. By using tools like Gemini CLI and frameworks like Conductor, you can scale your impact as an architect while ensuring consistent, high-quality implementation.

Ready to build your own AI-assisted development projects?

* Check out Gemini CLI
* Explore the Conductor extension
* Try Antigravity
* Check out the full RAG Migration repository

## Thanks for reading

If you found this article helpful, please consider adding 50 claps to this post by pressing and holding the clap button 👏 This will help others find it. You can also share it with your friends on socials.

I'm always eager to share my learnings or chat with fellow developers and AI enthusiasts, so feel free to follow me onLinkedIn,XorBluesky.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
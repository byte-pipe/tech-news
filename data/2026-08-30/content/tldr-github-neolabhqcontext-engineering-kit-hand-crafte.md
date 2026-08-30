---
title: 'GitHub - NeoLabHQ/context-engineering-kit: Hand-crafted Claude Code Skills focused on improving agent results quality. Compatible with OpenCode, Cursor, Antigravity, Gemini CLI, and others. Includes CodeRabbit open-source alternative. · GitHub'
url: https://github.com/NeoLabHQ/context-engineering-kit
site_name: tldr
content_file: tldr-github-neolabhqcontext-engineering-kit-hand-crafte
fetched_at: '2026-08-30T15:12:05.605107'
original_url: https://github.com/NeoLabHQ/context-engineering-kit
date: '2026-08-30'
description: Hand-crafted Claude Code Skills focused on improving agent results quality. Compatible with OpenCode, Cursor, Antigravity, Gemini CLI, and others. Includes CodeRabbit open-source alternative. - NeoLabHQ/context-engineering-kit
tags:
- tldr
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 NeoLabHQ

 

/

context-engineering-kit

Public

* NotificationsYou must be signed in to change notification settings
* Fork153
* Star1.5k

 
 
 
master
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

410 Commits
410 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.claude-plugin
.claude-plugin
 
 
.claude
.claude
 
 
.cursor
.cursor
 
 
.devcontainer
.devcontainer
 
 
.github/
workflows
.github/
workflows
 
 
.specs
.specs
 
 
agents
agents
 
 
antigravity
antigravity
 
 
docs
docs
 
 
plugins
plugins
 
 
scripts
scripts
 
 
skills
skills
 
 
.gitbook.yaml
.gitbook.yaml
 
 
.gitignore
.gitignore
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
gemini-extension.json
gemini-extension.json
 
 
justfile
justfile
 
 
plugin.json
plugin.json
 
 
View all files

## Repository files navigation

Advanced context engineering techniques and patterns for Claude Code, OpenCode, Cursor, Antigravity and more.

Quick Start·Plugins·Github Action·Reference·Docs

# Context Engineering Kit

A hand-crafted collection of advanced context engineering techniques and patterns with minimal token footprint, focused on improving agent result quality and predictability.

The marketplace is based on prompts our company's developers have used daily for a long time, supplemented by plugins from benchmarked papers and high-quality projects.

## Key Features

* Simple to Use- Easy to install and use without any dependencies. Contains automatically used skills and self-explanatory commands.
* Token-Efficient- Carefully crafted prompts and architecture, preferring command-oriented skills with sub-agents over general information skills when possible, to minimize populating context with unnecessary information.
* Quality-Focused- Each plugin is focused on meaningfully improving agent results in a specific area.
* Granular- Install only the plugins you need. Each plugin loads only its specific agents, commands, and skills, without overlap or redundant skills.
* Scientifically proven- Plugins are based on proven techniques and patterns validated by reputable benchmarks and studies.
* Open-Standards- Skills are based onagentskills.iospecification. TheSDDplugin is based on theArc42specification standard for software development documentation.

## News

Updates from key releases:

* v3.1.0:ImprovedSpec-Driven Development plugingenerated code quality by embedding DDD/SOLID rules in the developer agent and adding a dedicated code-reviewer agent that applies functional and OOP best-practices rules together with Muda waste analysis to reduce code complexity and duplication.
* v3.0.0:Added support for AMP and Hermes agents.Tech Stack pluginnow automatically injects typescript best practices when agent reads or writes TypeScript files.
* v2.2.0:Subagent-Driven Development pluginnow works as a distilled version ofSDD pluginusing meta-judge and judge sub-agents for specification generation on the fly and in parallel to implementation.DDD pluginnow includes Clean Architecture, DDD, SOLID, Functional Programming, and other pattern examples as rules that are automatically added to the context during code writing.
* v2.1.0:Spec-Driven Development pluginagents include high-level code quality guidelines fromDDD plugin.
* v2.0.0:Spec-Driven Development pluginwas rewritten from scratch. It is now able to produce working code in 99% of cases on real-life production projects!

## Quick Start

### Step 1: Install Marketplace and Plugins

Claude Code

Open Claude Code and add the Context Engineering Kit marketplace:

/plugin marketplace add NeoLabHQ/context-engineering-kit

This makes all plugins available for installation, but does not load any agents or skills into your context.

Install any plugin — for example, reflexion:

/plugin install reflexion@NeoLabHQ/context-engineering-kit

Each installed plugin loads only its specific agents, commands, and skills into Claude's context.

Gemini CLI

Install the extension directly from the repository:

gemini extensions install https://github.com/NeoLabHQ/context-engineering-kit

Note:This installs every plugin's skills and agents as a single bundle — there's no per-plugin selection like Claude Code's. Unfortunately, Gemini CLI does not support per-plugin selection. But you can delete skills and agents that you don't need, after installation.

Antigravity CLI

Install the plugin directly from the repository'santigravity/folder — Gemini CLI is not required:

agy plugin install https://github.com/NeoLabHQ/context-engineering-kit/antigravity

Note:This installs every plugin's skills and agents as a single bundle — there's no per-plugin selection like Claude Code's. Unfortunately, Antigravity CLI does not support per-plugin selection. But you can delete skills and agents that you don't need, after installation.

Cursor, Codex, OpenCode and others

Run thevercel-labs/skillscommand in your terminal:

npx skills add NeoLabHQ/context-engineering-kit

You can pick which skills to install.

Note:Each provider uses its own agent format andnpx skillsdoes not support subagents, so this installation method won't provide the full experience.

Alternative installation methods

You can useOpenSkillsto install skills by running the following commands:

npx openskills install NeoLabHQ/context-engineering-kit
npx openskills sync

### Step 2: Use Plugin

>
 claude 
"
implement user authentication
"

#
 Claude implements user authentication, then you can ask it to reflect on implementation

>
 /reflect

#
 It analyses results and suggests improvements

#
 If issues are obvious, it will fix them immediately

#
 If they are minor, it will suggest improvements that you can respond to

>
 fix the issues

#
 If you would like to prevent issues found during reflection from appearing again,

#
 ask Claude to extract resolution strategies and save the insights to project memory

>
 /memorize

Alternatively, you can use thereflectword in the initial prompt:

>
 claude 
"
implement user authentication, then reflect
"

#
 Claude implements user authentication,

#
 then hook automatically runs /reflect

In order to use this hook, you need to havebuninstalled. However, it is not required for the overall command.

## Documentation

You can find the complete Context Engineering Kit documentationhere.

However, the main plugins we recommend starting with areSubagent-Driven DevelopmentandSpec-Driven Development.

### Agent Reliability Engineering

The three plugins in this marketplace are designed to improve how accurately and consistently the agent follows provided instructions and to reduce hallucinations and bias toward incorrect solutions. They are not competitors but rather complementary to each other, because they allow you to balance reliability vs. token cost. Here is a high-level comparison of different agent usage approaches and the probability of receiving results that are fully accurate and include zero hallucinations, based on task complexity:

Approach

Probability of receiving fully accurate results for the following number of changed files (p)

Tokens Overhead

What does this mean in practice

1-3

4-10

10-20

20+

One-shot prompt

60%-80%

30%-50%

5%-30%

1%-20%

0

Accuracy depends on model, but with context growth LLM quality degrades exponentially

/reflect

68%-91%

49%-71%

13%-41%

1%-30%

1k-3k

Agent finds and fixes missed requirements on its own

/reflect
 + 
/memorize

79%-87%

60%-79%

34%-42%

5%-30%

2k-5k

Agent extracts repeatable mistakes and avoids them during new tasks

/do-and-judge

90%

83%

60%

30%

1.5x-3x

Mitigates context rot, bias, hallucinations and missed requirements using Judge sub-agent

/do-in-steps

92%

90%

71%

50%

3x-5x

Resolves all issues similar to /do-and-judge, but separately per file group

/plan-task + /implement-task

94%

93%

85%

70%

5x-20x

Performs the /do-in-steps flow, but the specification mitigates issues caused by inconsistent architecture and codebase size

/brainstorm
 + 
/plan-task
 + 
/implement-task

95%

95%

90%

80%

5x-20x

Brainstorming decreases the number of incorrect decisions and missed requirements

/plan-task
 + human review + 
/implement-task

99%

99%

99%

95%

5x-35x

Human review mitigates misunderstanding of requirements by LLM

Reliability metrics are based on more than year of real development usage on production projects.

## Plugins List

To view all available plugins:

/plugin

* Reflexion- Feedback and refinement loops to improve output quality.
* Spec-Driven Development- Commands for specification-driven development, based on Continuous Learning + LLM-as-Judge + Agent Swarm. Achievesdevelopment as compilationthrough reliable code generation.
* Review- Open-source and higher quality version of CodeRabbit. Includes code and PR review commands and skills using multiple specialized agents with impact/confidence filtering.Free Github Actions integration available
* Git- Commands for commit and PR creation.
* Test-Driven Development- Commands for test-driven development and common anti-patterns, plus skills for testing using subagents.
* Subagent-Driven Development- Skills for subagent-driven development, which dispatches a fresh subagent for each task with code review between tasks, enabling fast iteration with quality gates.
* Domain-Driven Development- Commands to update CLAUDE.md with best practices for domain-driven development, focused on code quality, and includes Clean Architecture, SOLID principles, and other design patterns.
* FPF - First Principles Framework- Structured reasoning using ADI cycle (Abduction-Deduction-Induction) with knowledge layer progression. Uses workflow command pattern with fpf-agent for hypothesis generation, verification, and auditable decision-making.
* Kaizen- Inspired by Japanese continuous improvement philosophy, Agile and Lean development practices. Commands for analysis of root causes of issues and problems, including 5 Whys, Cause and Effect Analysis, and other techniques.
* Customaize Agent- Commands and skills for writing and refining commands, hooks, and skills for Claude Code. Includes Anthropic Best Practices andAgent Persuasion Principlesthat can be useful for sub-agent workflows.
* Docs- Commands for analyzing projects, writing and refining documentation.
* Tech Stack- Rules for language-specific best practices, automatically applied when working on matching file types.
* MCP- Commands for setting up well-known MCP server integrations when needed and updating the CLAUDE.md file with requirements to use MCP servers in the current project.

## Works Great With

We developed the following projects to speed up development further and improve code quality:

* Agent Sandbox- Development sandbox image for agents, based on the official devcontainers images from Microsoft. Works out of the box with most languages and agents.
* Agent Eslint Config- An overly opinionated ESLint config for AI agents. Forces them to write low-complexity, highly readable code. Includes SonarJS, Unicorn, and 100+ rules focused on security and cognitive complexity.

Both are tested and combine well with theSADD/SDDplugins, but also work great independently of Context Engineering Kit.

## Stay ahead

Star Context Engineering Kit on GitHub to support its development and get notified about new features and updates.

### Reflexion

Collection of commands that force the LLM to reflect on the previous response and output. Includesautomatic reflection hooksthat trigger when you include "reflect" in your prompt.

How to install

/plugin install reflexion@NeoLabHQ/context-engineering-kit

Commands

* /reflect- Reflect on the previous response and output based on the self-refinement framework for iterative improvement with complexity triage and verification
* /memorize- Curate insights from reflections and critiques into CLAUDE.md using Agentic Context Engineering
* /critique- Comprehensive multi-perspective review using specialized judges with debate and consensus building

Hooks

* Automatic Reflection Hook- Triggers/reflectautomatically when "reflect" appears in your prompt

Theoretical Foundation

The plugin is based on papers likeSelf-RefineandReflexion. These techniques improve the output of large language models by introducing feedback and refinement loops.

They are proven toincrease output quality by 8–21%based on both automatic metrics and human preferences across seven diverse tasks, including dialogue generation, coding, and mathematical reasoning, when compared to standard one-step model outputs.

On top of that, the plugin is based on theAgentic Context Engineeringpaper, which uses memory updates after reflection andconsistently outperforms strong baselines by 10.6%in agent applications.

### Review

Comprehensive code and PR review commands that use multiple specialized agents for thorough code quality evaluation with impact/confidence filtering.

How to install

/plugin install review@NeoLabHQ/context-engineering-kit

Commands

* /review-local-changes- Comprehensive review of local uncommitted changes using specialized agents with code improvement suggestions
* /review-pr- Comprehensive pull request review using specialized agents
* /traiage-review- Pick the top most important files from huge changeset for human reviewer, to decrease amount of files that need to review before approving it.

Agents

This plugin uses multiple specialized agents for comprehensive code quality analysis:

* bug-hunter- Identifies potential bugs, edge cases, and error-prone patterns
* code-quality-reviewer- Evaluates code structure, readability, and maintainability
* contracts-reviewer- Reviews interfaces, API contracts, and data models
* historical-context-reviewer- Analyzes changes in relation to codebase history and patterns
* security-auditor- Identifies security vulnerabilities and potential attack vectors
* test-coverage-reviewer- Evaluates test coverage and suggests missing test cases

Thetraiage-reviewskill additionally uses four change-triage agents:

* **change-story-agent
* change-impact-agent
* change-failure-agent
* change-expectation-agent

You can use this plugin to review code in GitHub Actions; to do so, followthis guide.

### Git

Commands and skills for streamlined Git operations including commits, pull request creation, and advanced workflow patterns.

How to install

/plugin install git@NeoLabHQ/context-engineering-kit

Commands

* /commit- Create well-formatted commits with conventional commit messages and emoji
* /create-pr- Create pull requests using GitHub CLI with proper templates and formatting
* /analyze-issue- Analyze a GitHub issue and create a detailed technical specification
* /load-issues- Load all open issues from GitHub and save them as markdown files
* /load-pr-comments- Load open/unresolved PR review comments and group them as tasks for parallel agents to fix.
* /worktree- Create, compare, and merge git worktrees for parallel development with automatic dependency installation

Skills

* git-notes- Skill for using git notes to add metadata to commits without changing history.
* resolve-fixed-pr-comments- Verify what PR review comments have been addressed and resolve that are genuinely fixed or no longer relevant.

### Test-Driven Development

Commands and skills for test-driven development with anti-pattern detection.

How to install

/plugin install tdd@NeoLabHQ/context-engineering-kit

Commands

* /write-tests- Systematically add test coverage for local code changes using specialized review and development agents
* /fix-tests- Fix failing tests after business logic changes or refactoring using orchestrated agents

Skills

* test-driven-development- Introduces TDD methodology, best practices, and skills for testing using subagents
* design-testing-strategy- Manual guide to design a plan for the best way to cover a given artifact with tests while minimizing effort and maximizing coverage.
* test-coverage- Manual for choosing, applying, different types of coverage analysis (structural, mutation, requirements, API/integration) on an existing test suite.

### Subagent-Driven Development

Execution framework for competitive generation, multi-agent evaluation, and subagent-driven development with quality gates.

How to install

/plugin install sadd@NeoLabHQ/context-engineering-kit

Commands

* /launch-sub-agent- Launch focused sub-agents with intelligent model selection, Zero-shot CoT reasoning, and self-critique verification
* /do-and-judge- Execute a single task with implementation sub-agent, independent judge verification, and automatic retry loop until passing
* /do-in-parallel- Execute the same task across multiple independent targets in parallel with context isolation
* /do-in-steps- Execute complex tasks through sequential sub-agent orchestration with automatic decomposition and context passing
* /do-competitively- Execute tasks through competitive generation, multi-judge evaluation, and evidence-based synthesis to produce superior results
* /tree-of-thoughts- Execute complex reasoning through systematic exploration of solution space, pruning unpromising branches, and synthesizing the best solution
* /judge-with-debate- Evaluate solutions through iterative multi-judge debate with consensus building or disagreement reporting
* /judge- Evaluate completed work using LLM-as-Judge with structured rubrics and evidence-based scoring

Skills

* subagent-driven-development- Dispatches a fresh subagent for each task with code review between tasks, enabling fast iteration with quality gates
* multi-agent-patterns- Design multi-agent architectures (supervisor, peer-to-peer, hierarchical) for complex tasks exceeding single-agent context limits

### Spec-Driven Development

Comprehensive specification-driven development workflow plugin that transforms prompts into production-ready implementations through structured planning, architecture design, and quality-gated execution.

This plugin is designed to consistently produce working code. It was tested on real-life production projects by our team, and in 100% of cases, it generated working code aligned with the initial prompt. If you find a use case it cannot handle, please report it as an issue.

#### Key Features

* Development as compilation— The plugin works like a "compilation" or "nightly build" for your development process:task specs → run /implement-task → working code. After writing your prompt, you can launch the plugin and expect a working result when you come back. The time it takes depends on task complexity — simple tasks may finish in 30 minutes, while complex ones can take a few days.
* Benchmark-level quality in real life— Model benchmarks improve with each release, yet real-world results usually stay the same. That's because benchmarks reflect the best possible output a model can achieve, whereas in practice LLMs tend to drift toward sub-optimal solutions that can be wrong or non-functional. This plugin uses a variety of patterns to keep the model working at its peak performance.
* Customizable— Balance result quality and process speed by adjusting command parameters. Learn more in theCustomizationsection.
* Time-efficient for developers— The overall process is designed to minimize developer time and reduce the number of interactions, while still producing results better than what a model can generate from scratch. However, overall quality is highly proportional to the time you invest in iterating and refining the specification.
* Industry-standard— The plugin's specification template is based on the arc42 standard, adjusted for LLM capabilities. Arc42 is a widely adopted, high-quality standard for software development documentation used by many companies and organizations.
* Works best in complex or large codebases— While most other frameworks work best for new projects and greenfield development, this plugin is designed to perform better the more existing code and well-structured architecture you have. At each planning phase, it includes acodebase impact analysisstep that evaluates which files may be affected and which patterns to follow to achieve the desired result.
* Simple— This plugin avoids unnecessary complexity and mainly uses just 3 commands, offloading process complexity to the model via multi-agent orchestration./implement-taskis a single command that produces working code from a task specification. To create that specification, you run/sdd:add-taskand/plan-task, which analyze your prompt and iteratively refine the specification until it meets the required quality.

#### Quick Start

/plugin install sdd@NeoLabHQ/context-engineering-kit

Then run the following commands:

#
 create .specs/tasks/draft/design-auth-middleware.feature.md file with initial prompt

/add-task 
"
Design and implement authentication middleware with JWT support
"

#
 write detailed specification for the task

/plan-task .specs/tasks/draft/design-auth-middleware.feature.md

#
 will move task to .specs/tasks/todo/ folder

Restart the Claude Code session to clear context and start fresh. Then run the following command:

#
 implement the task

/implement-task @.specs/tasks/todo/design-auth-middleware.feature.md

#
 produces working implementation and moves the task to .specs/tasks/done/ folder

* Detailed guide
* Usage Examples

Commands

* /add-task- Create task template file with initial prompt
* /plan-task- Analyze prompt, generate required skills and refine task specification
* /implement-task- Produce a working implementation of the task and verify it

Additional commands useful before creating a task:

* /create-ideas- Generate diverse ideas on a given topic using creative sampling techniques
* /brainstorm- Refine vague ideas into fully-formed designs through collaborative dialogue

Agents

Agent

Description

Used By

researcher

Technology research, dependency analysis, best practices; creates a reusable skill file

/plan-task
 (Phase 2a)

code-explorer

Codebase analysis, pattern identification, architecture mapping

/plan-task
 (Phase 2b)

business-analyst

Requirements discovery, scope and user scenarios, and the whole 
## Acceptance Criteria
 section — checklist, regular checks, rubric, score definitions, test strategy and definition of done

/plan-task
 (Phase 2c)

software-architect

Architecture design, component design, solution strategy and expected changes

/plan-task
 (Phase 3)

tech-lead

Decomposition into per-step sub-task files, dependency mapping, parallelization, risk analysis, and grouping steps into independently verifiable phases with a reviewer model each

/plan-task
 (Phase 4)

developer

Implements exactly one step, from its own sub-task file, and leaves the tree building and green

/implement-task
 (per step)

code-reviewer

Reviews a whole implementation phase against the acceptance criteria that phase lists as due, plus code quality, Muda waste analysis and test coverage

/implement-task
 (end of each phase)

tech-writer

Technical documentation writing, API guides, usage examples, architecture updates

/implement-task

#### Patterns

Key patterns implemented in this plugin:

* Structured reasoning templates— includes Zero-shot and Few-shot Chain of Thought, Tree of Thoughts, Problem Decomposition, and Self-Critique. Each is tailored to a specific agent and task, enabling sufficiently detailed decomposition so that isolated sub-agents can implement each step independently.
* Multi-agent orchestration for context management— Context isolation of independent agents prevents the context rot problem, essentially keeping LLMs at optimal performance at each step of the process. The main agent acts as an orchestrator that launches sub-agents and controls their work.
* Quality gates based on LLM-as-Judge— Evaluate the quality of each planning and implementation step using evidence-based scoring and predefined verification rubrics. This fully eliminates cases where an agent produces non-working or incorrect solutions.
* Continuous learning— Builds skills that the agent needs to implement a specific task, which it would otherwise not be able to perform from scratch.
* Spec-driven development pattern— Based on the arc42 specification standard, adjusted for LLM capabilities, to eliminate parts of the specification that add no value to implementation quality or that could degrade it.
* MAKER— An agent reliability pattern introduced inSolving a Million-Step LLM Task with Zero Errors. It removes agent mistakes caused by accumulated context and hallucinations by utilizing clean-state agent launches and filesystem-based memory storage.

#### Vibe Coding vs. Specification-Driven Development

This plugin is not a "vibe coding" solution, but out of the box, it works like one. By default, it is designed to work from a single prompt through to the end of the task, making reasonable assumptions and evidence-based decisions instead of constantly asking for clarification. This is because developer time is more valuable than model time. As a result, the plugin is designed to allow the developer to decide how much time the task is worth. The plugin will always produce working results, but quality will be sub-optimal if no human feedback is provided.

To improve quality, after generating a specification you can correct it or leave comments using//, then run the/plan-taskcommand again with the--refineflag. You can also verify each planning and implementation phase by adding the--human-in-the-loopflag. According to most known research, human feedback is the most effective way to improve results.

Our tests showed that even when the initially generated specification was incorrect due to lack of information or task complexity, the agent was still able to self-correct until it reached a working solution. However, it usually takes much longer and results in the agent spending time on wrong paths and stopping more frequently. To avoid this, we strongly advise decomposing tasks into smaller separate tasks with dependencies and reviewing the specification for each one independently. You can add dependencies between tasks as arguments to the/add-taskcommand, and the agent will link them together by adding adepends_onsection to the task file frontmatter.

Even if you don't want to spend much time on this process, you can still use the plugin for complex tasks without decomposition or human verification — but you will likely need tools like ralph-loop to keep the agent running for longer.

Learn more about available customization options inCustomization.

### Domain-Driven Development

Code quality framework with rules for Clean Architecture, SOLID principles, and Domain-Driven Design patterns.

How to install

/plugin install ddd@NeoLabHQ/context-engineering-kit

Rules

* 15 composable rules covering Clean Architecture, SOLID principles, Command-Query Separation, Functional Core/Imperative Shell, Explicit Control Flow, Domain-Specific Naming, and more. Seerules reference

### FPF - First Principles Framework

A structured reasoning plugin that implements theFirst Principles Framework (FPF)by Anatoly Levenchuk — a methodology for rigorous, auditable reasoning. The killer feature is turning the black box of AI reasoning into a transparent, evidence-backed audit trail. The plugin makes AI decision-making transparent and auditable. Instead of jumping to solutions, FPF enforces generating competing hypotheses, checking them logically, testing against evidence, then letting developers choose.

Key principles:

* Transparent reasoning- Full audit trail from hypothesis to decision
* Hypothesis-driven- Generate 3-5 competing alternatives before evaluating
* Evidence-based- Computed trust scores, not estimates
* Human-in-the-loop- AI generates options; humans decide (Transformer Mandate)

The core cycle follows three modes of inference:

1. Abduction— Generate competing hypotheses (don't anchor on the first idea).
2. Deduction— Verify logic and constraints (does the idea make sense?).
3. Induction— Gather evidence through tests or research (does the idea work in reality?).

Then, audit for bias, decide, and document the rationale in a durable record.

Warning:This plugin loads the core FPF specification into context, which is large (~600k tokens). As a result, it is loaded into a subagent with the Sonnet[1m] model. However, such an agent can consume your token limit quickly.

How to install

/plugin install fpf@NeoLabHQ/context-engineering-kit

#### Usage workflow

#
 Execute complete FPF cycle from hypothesis to decision

/propose-hypotheses What caching strategy should we use
?

#
 The workflow will:

#
 1. Initialize context and .fpf/ directory

#
 2. Generate competing hypotheses

#
 3. Allow you to add your own alternatives

#
 4. Verify each against project constraints (parallel)

#
 5. Validate with evidence (parallel)

#
 6. Compute trust scores (parallel)

#
 7. Present comparison for your decision

Commands

* /propose-hypotheses- Execute complete FPF cycle from hypothesis to decision (main workflow)
* /status- Show current FPF phase and hypothesis counts
* /query- Search knowledge base with assurance info
* /decay- Manage evidence freshness (refresh/deprecate/waive)
* /actualize- Reconcile knowledge with codebase changes
* /reset- Archive session and return to IDLE

Agent

* fpf-agent- FPF reasoning specialist for hypothesis generation, verification, validation, and trust calculus using ADI cycle and knowledge layer progression

### Kaizen

Continuous improvement methodology inspired by Japanese philosophy and Agile practices.

How to install

/plugin install kaizen@NeoLabHQ/context-engineering-kit

Commands

* /analyse- Auto-selects best Kaizen method (Gemba Walk, Value Stream, or Muda) for target analysis
* /analyse-problem- Comprehensive A3 one-page problem analysis with root cause and action plan
* /why- Iterative Five Whys root cause analysis drilling from symptoms to fundamentals
* /root-cause-tracing- Systematically traces bugs backward through call stack to identify source of invalid data or incorrect behavior
* /cause-and-effect- Systematic Fishbone analysis exploring problem causes across six categories
* /plan-do-check-act- Iterative PDCA cycle for systematic experimentation and continuous improvement

Skills

* kaizen- Continuous improvement methodology with multiple analysis techniques

### Customaize Agent

Commands and skills for creating and refining Claude Code extensions.

How to install

/plugin install customaize-agent@NeoLabHQ/context-engineering-kit

Commands

* /create-agent- Comprehensive guide for creating Claude Code agents with proper structure, triggering conditions, system prompts, and validation
* /create-command- Interactive assistant for creating new Claude commands with proper structure and patterns
* /create-workflow-command- Create workflow commands that orchestrate multi-step execution through sub-agents with file-based task prompts
* /create-skill- Guide for creating effective skills with test-driven approach
* /create-hook- Create and configure git hooks with intelligent project analysis and automated testing
* /test-skill- Verify skills work under pressure and resist rationalization using RED-GREEN-REFACTOR cycle
* /test-prompt- Test any prompt (commands, hooks, skills, subagent instructions) using RED-GREEN-REFACTOR cycle with subagents
* /apply-anthropic-skill-best-practices- Comprehensive guide for skill development based on Anthropic's official best practices

Skills

* prompt-engineering- Well-known prompt engineering techniques and patterns, includes Anthropic Best Practices and Agent Persuasion Principles
* context-engineering- Deep understanding of context mechanics: attention budget, progressive disclosure, lost-in-middle effect, and practical optimization patterns
* agent-evaluation- Evaluation frameworks for agent systems: LLM-as-Judge, multi-dimensional rubrics, bias mitigation, and the 95% performance finding

### Docs

Commands for project analysis and documentation management based on proven writing principles.

How to install

/plugin install docs@NeoLabHQ/context-engineering-kit

Commands

* /update-docs- Update implementation documentation after completing development phases
* /write-concisely- ApplyThe Elements of Styleprinciples to make documentation clearer and more professional

### Tech Stack

Rules for language and framework-specific best practices, automatically applied when the agent works on matching file types.

How to install

/plugin install tech-stack@NeoLabHQ/context-engineering-kit

Rules

* TypeScript Best Practices - Type system guidelines, code style, async patterns, and code quality standards, automatically loaded when the agent reads or writes.tsfiles

### MCP

Commands for integrating Model Context Protocol servers with your project. Each setup command supports configuration at multiple levels:

* Project level (shared)- Configuration tracked in git, shared with team via./CLAUDE.md
* Project level (personal)- Local configuration in./CLAUDE.local.md, not tracked in git
* User level (global)- Configuration in~/.claude/CLAUDE.md, applies to all projects

How to install

/plugin install mcp@NeoLabHQ/context-engineering-kit

Commands

* /setup-context7-mcp- Guide for setting up Context7 MCP server to load documentation for specific technologies
* /setup-serena-mcp- Guide for setting up Serena MCP server for semantic code retrieval and editing capabilities
* /setup-codemap-cli- Guide for setting up Codemap CLI for intelligent codebase visualization and navigation
* /setup-arxiv-mcp- Guide for setting up arXiv/Paper Search MCP server via Docker MCP for academic paper search and retrieval from multiple sources
* /build-mcp- Guide for creating high-quality MCP servers that enable LLMs to interact with external services

## Theoretical Foundation

This project is based on research and papers from the following sources:

* Self-Refine- Core refinement loop
* Reflexion- Memory integration
* Constitutional AI- Principle-based critique
* LLM-as-a-Judge- Evaluation patterns
* Multi-Agent Debate- Multiple perspectives
* Agentic Context Engineering- Memory curation
* Chain-of-Verification- Hallucination reduction
* Tree of Thoughts- Structured exploration
* Process Reward Models- Step-by-step evaluation
* Verbalized Sampling- Diverse idea generation with 2-3x improvement
* Process Reward Models- Step verification
* Chain of Thought Prompting- Step-by-step reasoning
* Inference-Time Scaling of Verification- Rubric-guided verification

More details about the theoretical foundation can be found on theresourcespage.
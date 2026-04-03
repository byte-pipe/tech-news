---
title: 'Agentic Engineering: Lessons Learned Vol. 1 - DEV Community'
url: https://dev.to/duske/agentic-engineering-lessons-learned-vol-1-jbj
site_name: devto
fetched_at: '2025-09-29T19:07:19.449376'
original_url: https://dev.to/duske/agentic-engineering-lessons-learned-vol-1-jbj
author: Dustin
date: '2025-09-29'
description: 'The buzz around agentic engineering is deafening, and for good reason: it promises to be a massive... Tagged with llm, agentic, contextengineering.'
tags: '#llm, #agentic, #contextengineering'
---

The buzz around agentic engineering is deafening, and for good reason: it promises to be a massive lever for software development. But as we've integrated these agents into our workflow, we've discovered that harnessing their power isn't as simple as writing a good prompt. True success comes from mastering a deeper, more dynamic skill: context engineering.

This post is a dispatch from the front lines. We're cutting through the noise to share our lessons on managing an agent's context. We'll cover what worked, what failed, and provide practical strategies you can use today, drawn from our experience with tools like Claude Code.Note that many of these strategies are not new and have been discussed in various forms by experts (1,2,3,4,5) in the field. However, we've found that consolidating these insights into actionable lessons has been invaluable for our team.

Note:This space is moving atfast. Take these recommendations with a grain of salt and always validate them for your own use case. Our findings are as of September 2025.

## Context Engineering 101

ℹ️ We assume that you are already familiar with the basics of LLMs, prompt engineering, and agentic engineering. If not, check out the resources section at the end of this post.

When thinking about agentic engineering, context engineering is one of the most important aspects to get right.

### Mental model

Since LLMs are stateless, the context is the only way to provide them with the necessary information to perform a task.When working on a codebase, you can think of this model as a function:

type

Context

=

Instructions

|

Knowledge

|

Tools

agent
:

(
context
)

->

output

Enter fullscreen mode

Exit fullscreen mode

So if the context is your entire input to the model, it is crucial to get it right. While in the early ages of LLMs, prompt engineering was the main focus, context engineering encompasses more than just the prompt:

* Instructions: besides the prompt or even an entire spec, this could be examples (few-shot), constraints, or other memories like agents.md/claude.md
* Knowledge: documentation, facts/memories,
* Tools: regular tool calls like grep, read file, write file but also MCPS, subagents, etc.

Note that there is not a clear boundary between those categories. For example, a spec could be seen as instructions or knowledge, while documentation could be read with a MCP server like context7. The important part is to understand that the context is more than just the prompt and that all those aspects need to be considered when working with agents.

So when so many things could be the context, how to get it right? Luckily, there are smart people that already figured outcommon issues that you will face. We can highly recommendthis article by Drew Breunigfor more details, but let's get right into the main points:

### Common pitfalls with long contexts

as coined byDrew Breunig

* Context Poisoning: When an error or hallucination enters the context and gets repeatedly referenced, corrupting subsequent responses. For example, if your code assistant hallucinates a non-existent API method early in a debugging session, it may keep trying to use that fictional method throughout the conversation, building increasingly nonsensical solutions around it.
* Context Distraction: As context grows beyond certain thresholds, models start over-relying on their accumulated history rather than their training. A coding assistant might fixate on repeating past debugging attempts from its context instead of synthesizing new approaches, even when those old strategies clearly aren't working.
* Context Confusion: Irrelevant information in the context interferes with response quality. Loading a coding assistant with 40+ tool definitions when you only need 3-4 causes the model to make inappropriate tool calls or get distracted by unrelated capabilities, like trying to use a database migration tool when you asked for string manipulation (Tool loadout).
* Context Clash: When information gathered incrementally contains contradictions, models struggle to recover. If your coding assistant makes incorrect assumptions about your codebase architecture early on, those wrong assumptions remain in context and influence later responses—even after you provide corrections. The model gets "lost" and cannot recover from early missteps.

Crucial skill:Think about your first interaction with a LLM that used to be a few messages back and forth. Now with ever-growing turns the agents willtake to fulfill your task, the context will necessarily grow and be expanded with information over time. Keeping this context relevant and focused is a crucial skill to master.

### Context window management strategies

How to manage the context window effectively?Lance Martin wrote an exceptional article aboutcontext engineering strategiesand describes four main techniques to do so:

* ✏️ Writing context means saving it outside the context window to help an agent perform a task.
* 🔎 Selecting context means pulling it into the context window to help an agent perform a task.
* 🗜️ Compressing context involves retaining only the tokens required to perform a task.
* ✂️ Isolating context involves splitting it up to help an agent perform a task.

Each strategy is categorized by an emoji that we will use throughout this post to highlight which strategy we think is employed.

## Lessons learned

Equipped with that knowledge, let's dive into the lessons learned from our journey with agentic engineering:

### 🔎 Don't set yourself up for failure

If your initial setup is already bad, you will have a hard time achieving good results with coding agents. This often happens when it is not tuned to your specific environment or tries to do too many things at once:

* Provide afocusedClaude.md/agents.mdfile. It should be kept compact and relevant for all use cases, thus task specific instructions should be provided in the prompt/spec,/<command>or subagent.
* MaintainyourClaude.md/agents.mdfile. Outdated or conflicting information will poison the context. In our case, we forgot to update how we ran tests after a migration, which made the agent ever-rediscovering how to actually run tests wasting tokens.
* Only keep mcp servers that youreallyneed. Having conflicting tool information or overlapping mcp definitions will lead to context consfusion and clash. It should beversionedand reviewed by the team. Usecontextto identify what is actually used.

### 🔎 Codebase is context too (or make your codebase agent friendly)

While you can put a lot of work into optimizing the your prompts and context files like documentation, it will only get you so far if you do not make the codebase itself agent friendly.

Code architecture/patterns:

Not only the prompt/spec is context, the codebase itself is context too. Since the model cannot "guess" your codebase, it will scan and crawl through to find files, analyze coding patterns, and understand the architecture. Thus, it is crucial to have a clean and consistent codebase to get good results.If the codebase has lots of inconsistencies, bad patterns, or is just plain messy, the agent will struggle to understand it and will even use it as reference for generating and aligning new code.Then you have the good oldgarbage in -> garbage outproblem: Since the LLM will only predict the next most likely token, if the code is bad, the output will likely be bad too.

To overcome this, you need to do the stuff most of us should do anyway: Refactor, clean up, and improve the codebase. For example by having uniform structure, implement well-known patterns and keep complex abstractions at bay. Ironically, by making the codebase agent friendly, your fellow humans will also benefit from it 🤡.

Agent friendly tooling:

You can also make your codebase more agent friendly by using well-known tools and precise scripts, that will not stress your context window that much. For example, you can:

* centralize your logginginto a single place with service prefixes. E.g. route your backend, DB andfrontend logsto one central log file. Now the Agent cangrep/tailfor the service and find all relevant logs in one place every time.
* Fix noisy toolslike test runners or linters that might produce a lot of output with verbose data.
* Createhelper scriptsthat will do the heavy lifting for the agent. If you have existing scripts, ensure that they are easy to use and that configuration is documented. This could be api generators, build scripts, or even tools that get you thenext task like this example.

### 🔎/🗜️ Watch the context window size

As a general rule of thumb, keep the context window usage below 60%. This will ensure that the model has enough "space" to reason and generate output. If you go above that, you often start to see issues like context distraction and confusion.When starting a task that will likely exceed the context window, plan ahead and clear or summarize the context deliberately. This can be done by:

* clearing the context with/clearor starting a new session. Ensure you have a working todo-list ortodo.mdfile to keep track of what needs to be done.
* summarizing the context with/summarizeand provide the summary back to the agent. Be careful with this, as the summary might miss important details. So far, we found this to be less effective than expected.
* use the/contextcommand that will provide you a good overview of the current context window usage and what is taking up the most space.

### 🔎 Paradigm shift: Read the spec!

For most non-trivial tasks, it really pays of to spend some time to create and evaluate an implementation plan together with the agent (duh!). This will help to get a common understanding of the task and will also help to keep the context focused.While you don't have to go all-in into spec driven development, simply leveraging Claude's plan mode or generating a markdown file with spec and task breakdown can often be sufficient for smaller tasks.

But if you choose to go down that path, make sure to keep to actually read the the specthoroughly. You might feel amazed by the agent's well structured output, but it might not align with your expectations or simply is contradictory to the codebase at hand.This can lead to context poisoning and distraction, as the agent will keep referencing the spec and try to align with it.It may sounds trivial, but being hyped often leads to skimming through the spec and missing important details.

Behind this there actually a bigger paradigm shift that is approaching fast: The role of the developer is shifting from spending big chunks of time writing code to spending more time on planning, specifying, and validating. For many usecases, the actual coding part is becoming less important, as the agent can take over a lot of that work.Stillfeeling productive while writing less codeand reading through generated specs is a skill that needs to be learned and practiced.

### ✏️ Outsource context via filesystem

One nice way of outsourcing context is to leverage the filesystem. Since the filesystem is not limited by the context window, you can use it to store large amounts of data that the agent can reference when needed.By providing tools like bash scripts or subagents (see below) that write to disk but return a summary/crucial info, you keep the context window small and focused while giving the agent the choice to access more information when needed.

### ✏️ Directives: Hansel and Gretel

Instead of writing elaborate prompts and precisely embed example or crucial files for the task, you can also use comment directives as breadcrumbs 🍞 to guide the agent.Giuseppe Gurgone wrote a great article aboutcomment directivesand how to use them effectively.Basically, you scatter certain type of comments across your codebase with some extra information on top. Then, when firing up the agent,instruct it to look for those comments and use them as context. This way, you can provide a lot of relevant information very locally without bloating the context window upfront.

For example, you when you want to finish a PR and know that in a follow-up PR you want address certain aspects, you can add a comment directive like this:

/* @Implement
 * Replace with generated api-client
 * timeouts should be configurable
 * no retries
 * /
async fetchUserData(userId: string): Promise<UserData> {
/...
}

Enter fullscreen mode

Exit fullscreen mode

### ✂️/🗜️ Subagents: Researchers, not implementers

Subagents are a great way ofisolating context, parallelizing tasks and specializing on certain aspects. But they are not a silver bullet and anthropomorphizing them into human roles did not play well for us.The main lesson learned here is that subagents currently work best as researchers, not implementers. This means that they can be used nicely to gather information, explore possibilities, and provide insights that the main agent can then use to make decisions.

Unsupervised Subagents "fixing" code in parallel

If you use subagents as implementers, you often run into issues like context clash and confusion, as the subagent might take actions that are notaligned with the main agent's goal. Also, spawning subagents in parallel could lead to conflicting writes that the main agent then needs to resolve.Instead, by using them for aggregating and collecting data, you can leverage their strengths without running into those issues. Plus, read-only tasks can usually be parallelized without any headaches.We used subagents for tasks like:

* finding/traversing codebase for certain patterns
* analyzing logs/code for certain errors
* checking deployment status/issues of platforms like Kubernetes by providing read-only access tokubectlor cloud CLIs

Test runner and build scriptsOkay, we lied. There are special use case for subagents as implementers we found useful: running tests.Our tests were quite verbose (see making codebase agent friendly 🫠) and often produced a lot of output (roughly 40k tokens!).By using a subagent to run the tests, we could isolate the context and only provide the relevant summarized output back to the main agent. This way, the main agent could focus on the task at hand without being distracted by the noise of the test output.The same goes for build scripts likenpm buildordocker build. They often produce a lot of output that is not relevant for the main task but were sometimes used to verify if the code can be built successfully, but ymmv.

For example, this could be baked into your subagent definition:

1. Execute tests efficiently across all services in the monorepo
2. Interpret test results and provide actionable feedback
3. Identify the most appropriate test commands based on user context
4. Provide clear summaries of test outcomes with specific error details when failures occur
5. You do not modify source code or fix bugs; your role is strictly to run tests and report results. You can suggest next steps but do not implement them.

Enter fullscreen mode

Exit fullscreen mode

## Outlook: Spec driven development 📝

While the lessons learned so far are quite generic and can be applied to most agentic engineering setups, there is one aspect that is worth mentioning in more detail: Spec driven development.With tools likeKiroorSpec Kitgaining traction quickly, spec driven development is becoming more and more popular.This is an entire topic for itself, so we will cover it in more detail in the next volume of this series - so stay tuned.

Context engineering will still apply, as this is just a more formalized, thorough and elaborate way of providing the right context well aligned with your goals.As with anything in the agentic engineering space, it is still early days and we are just scratching the surface of what is possible. Take it with a grain of salt and enjoy the ride!

## Resources

* https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html
* https://www.dbreunig.com/2025/06/26/how-to-fix-your-context.html
* https://rlancemartin.github.io/2025/06/23/context_engineering/
* https://steipete.me/posts/2025/essential-reading
* https://lucumr.pocoo.org/2025/7/30/things-that-didnt-work/
* https://giuseppegurgone.com/comment-directives-claude-code
* https://cognition.ai/blog/dont-build-multi-agents
* https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-03-own-your-context-window.md
* https://www.nathanonn.com/how-a-read-only-sub-agent-saved-my-context-window-and-fixed-my-wordpress-theme/

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse

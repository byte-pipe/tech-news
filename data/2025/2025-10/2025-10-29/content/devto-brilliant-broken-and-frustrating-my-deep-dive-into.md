---
title: 'Brilliant, Broken, and Frustrating: My Deep Dive into Amazon’s Kiro AI IDE, the Flawed Junior Developer - DEV Community'
url: https://dev.to/aws-builders/brilliant-broken-and-frustrating-my-deep-dive-into-amazons-kiro-ai-ide-the-flawed-junior-gn5
site_name: devto
fetched_at: '2025-10-29T19:10:34.783804'
original_url: https://dev.to/aws-builders/brilliant-broken-and-frustrating-my-deep-dive-into-amazons-kiro-ai-ide-the-flawed-junior-gn5
author: Francois Dexemple
date: '2025-10-24'
description: We’ve all been there. You throw a few prompts at an AI coding tool, and like magic, a functional app... Tagged with ai, aws, kiro, code.
tags: '#ai, #aws, #kiro, #code'
---

We’ve all been there. You throw a few prompts at an AI coding tool, and like magic, a functional app appears. It’s the peak of “vibe coding” — fast, exciting, and instantly gratifying. But then comes the hangover, and, oh boy, I havepersonallyhit this wall hard. The requirements were fuzzy. The design decisions were undocumented.Does the output even solve the problem?What was once a fun prototype quicklybecomesa maintenance nightmare; without clear design documentation, future changes are just guesswork. This is why so many AI-built prototypes hit a wall.

Enter Kiro, a new agentic IDE from AWS that takes a completely different path. It promises to tame the chaos by injecting a dose of engineering discipline into AI-assisted development. Instead of unstructured chats, it champions a structured, spec-driven workflow. After a deep dive into how Kiro works in its current preview state, a few realities stood out — some powerful, some frustrating, and all of them surprising. Here are the five surprising and often contradictory realities of using the tool that wants to wage war on vibe coding.

## 1. Its core mission is the opposite of “Vibe Coding”

Kiro’s entire philosophy is built on spec-driven development. This is a deliberate, structured, three-phase workflow that moves from a high-level prompt to a series of formal engineering artifacts:requirements.md,design.md, andtasks.md. The AI doesn’t just generate code; it first generates a detailed plan, user stories, architectural diagrams using Mermaid.js, and a sequenced task list.

This is the polar opposite of the unstructured “prompt-and-pray” chaos of vibe coding. The process forces you to plan and clarify your intent upfront, ensuring that what gets built aligns with actual requirements. It’s a trade-off: you get the rigor of traditional software engineering, but it can feel like a slower, more rigid “waterfall approach” compared to the quick dopamine hits of seeing code appear instantly. While this structure provides discipline, early user feedback highlights a critical flaw: its rigidity can kill momentum. One user described it as a “waterfall approach” where “requirements and design artifacts don’t auto-update,” causing the implementation and specs to drift apart and breaking the iterative flow developers rely on.

## 2. It’s an AWS product that tries hard not to be one

Here’s one of the biggest strategic surprises: Kiro is developed by Amazon Web Services, but it’s not branded as an “AWS” or “Amazon” product. This is AWS’s most significant strategic gamble in the developer tool space in years, a deliberate attempt to shed its “walled garden” reputation to win a war for developer mindshare that it has, until now, been losing.

It lives on its own website (kiro.dev), and you don’t even need an AWS account to use it, supporting logins via common providers like Google and GitHub, side-stepping the usual requirement for an AWS account (though AWS Builder ID and IAM roles are also supported for deeper integration). By shedding the AWS branding, Kiro aims to be a tool for all developers, not just those building on Amazon’s cloud.

## 3. The hype collided with a wall of errors and limits

The launch of Kiro was met with what the company called “unprecedented demand,” and the preview experience reflects a system struggling under the load. The ambitious vision of a seamless, AI-driven workflow has, for many users, been replaced by a reality of constant friction and failure.

The user-reported issues have been widespread and consistent:

* Initial Waitlists:At first, new users were often waitlisted before they could even download the IDE. Thankfully, the waitlist is now removed.
* Daily Usage Limits:Early users were hitting daily limits that halted their projects, with no option to pay for more capacity. This also seems to be resolved.
* Frequent Errors:Messages like “The model you’ve selected is experiencing a high volume of traffic. Try changing the model and re-running your prompt” and “An unexpected error occurred, please retry” are common. Personally, I still get these 1–2 times a week, though it’s much better than the daily errors at the start.
* Stuck Tasks:Tasks frequently get stuck, fail, and require numerous manual retries. I ran into a lot of problems with my terminal that was configured with many plugins; the issue and solution are on GitHub:https://github.com/kirodotdev/Kiro/issues/53The frustration is compounded by the fact that a failed task often loses all context, forcing developers to restart the entire process from scratch and burning through their daily usage limits on unsuccessful attempts. This gap between the product’s promise and its current usability has been a major source of frustration, perfectly captured by my own user’s experience:

I’ve been retrying 50+ times over the last 10+ hours and still get: “The model you’ve selected is experiencing a high volume of traffic. Try changing the model and re-running your prompt.” But with the paid plan, that’s over. I do not get this anymore.

## 4. Its real power isn’t just generating code, it’s automating the entire project

Beyond generating code from specs, Kiro’s true potential lies in two powerful automation features that represent its core argument for how AI development should work: not as a chatty assistant, but as an embedded, reactive system that automates the tedious rituals of software engineering.

Agent Steering: Solving the AI Memory Problem

Agent Steering is Kiro’s solution to the notorious short-term memory of AI assistants. It gives the AI persistent knowledge about your project’s conventions — tech stack, file structure, coding patterns — through a series of markdown files in a.kiro/steering/directory. Kiro consults these files to ensure it generates code that consistently follows your team's established standards, without you having to repeat the rules in every prompt.

Agent Hooks: Automating the Engineering Rituals

Agent Hooks are event-driven automations that trigger AI agents to perform tasks in the background. For example, a hook can automatically update test files whenever a component is saved, refresh documentation when an API endpoint changes, or scan for security leaks before a commit. However, the feature is limited in its preview state; only one hook can execute per file save, and there is no way to orchestrate a sequence of hooks.

It’s like having a very attentive pair programmer who takes care of the tedious stuff without interrupting your flow.

## 5. The AI is still a flawed (and overeager) Junior Dev

Despite its sophisticated planning and structured approach, Kiro’s AI is far from infallible. In practice, it often behaves like an overeager junior developer who, while well-intentioned, can make fundamental mistakes and overcomplicate simple problems.

Here are a few documented examples of its flaws:

* Code Bloat:I asked Kiro to create a simple app that will display my Strava data. The result was an “absolute mess” of approximately 20 files and over 1,500 lines of convoluted code riddled with “console.log gibberish” for a task that a human could solve in under 200 lines. It seems Kiro defaults to an “industrial, military-grade” product, so you have to review the tasks.
* Debugging Loops: The AI has been observed falling into a circular debugging loop, where it identifies a problem and applies the same incorrect fix over and over again.
* Infinite Optimizations:A user discovered they could repeatedly trigger a “code smell” hook on the same file. Each time, Kiro would find new “optimizations,” continuing until the code was “arguably worse than when we started.”
* Losing Context:In one project, Kiro correctly implemented DynamoDB caching logic but then unexpectedly mixed it with secrets management code from a completely different, earlier task, demonstrating a breakdown in context retention.

This reveals the central paradox of Kiro today: it builds an elaborate scaffolding of engineering discipline to constrain the AI, yet the AI inside still behaves like an unpredictable junior developer, requiring constant senior-level oversight to prevent it from over-engineering itself into a corner.

## Conclusion

Kiro’s vision is undeniably the future for any team that cares about building durable, enterprise-grade software with AI. It is a brilliant and necessary correction to the chaotic, short-term thinking of “vibe coding.” The constant errors, limits, and AI quirks make it clear that while the destination is exciting, the journey there is still incredibly bumpy. This leaves us with a critical question:

Is the engineering discipline Kiro enforces worth the current struggle, or will the instant gratification of “vibe coding” win out?

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse

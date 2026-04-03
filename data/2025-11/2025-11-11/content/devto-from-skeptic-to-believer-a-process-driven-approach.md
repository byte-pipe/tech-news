---
title: 'From Skeptic to Believer: A Process-Driven Approach to Vibe Coding - DEV Community'
url: https://dev.to/googleai/a-skeptics-guide-to-vibe-coding-213p
site_name: devto
fetched_at: '2025-11-11T11:07:31.483876'
original_url: https://dev.to/googleai/a-skeptics-guide-to-vibe-coding-213p
author: Mollie Pettit
date: '2025-11-05'
description: I’ll admit, I've in the past had a negative reaction to the term vibe coding. (And in some... Tagged with geminicli, vibecoding, agents, ai.
tags: '#geminicli, #vibecoding, #agents, #ai'
---

I’ll admit, I've in the past had a negative reaction to the termvibe coding. (And in some circumstances, I still do.) It often brought to mind an engineer carelessly committing code that’s buggy or inefficient without proper checks.

My perspective changed after our conversation with Keith Ballinger, VP and General Manager atGoogle Cloudonepisode 6of theAgent Factor podcast. He showed us that his approach to vibe coding isn't about chaos; it's about a surprisinglystructured templatethat turns a vague 'vibe' into a concrete plan.

Demo: Vibe coding a command line Markdown viewer with the Gemini CLI

My biggest takeaway is that vibe coding is more nuanced than I first thought. I now see its value on a spectrum: it's apowerful tool for exploration when you're in unfamiliar territory, and atool for acceleration when you're an expert in your domain. It's a workflow for both creative ideation and efficient execution.

## The Template: a structured workflow for AI-assisted development

On the show, Keith suggested on a whim that we vibe-code a command-line markdown viewer from scratch using theGemini CLI. This turned out to be my favorite moment of the show. What stuck out most to me was his methodical approach (which I am totally stealing, btw).

Here’s a breakdown of the template he used:

### Step 1: start with the user, not the code

Before writing a single line of code, Keith’s first move was to define the user experience. He prompted theGemini CLIto create aUserGuide.md.Timestamp: [01:49]

The demo prompt:

I want to build a command line markdown viewer. It should paginate long markdown files, have some syntax highlighting, and does not include any editing features. Write me a user guide and save it to UserGuide.md. Wait for my review, don't write any code yet.

Why I like it:Doing this as a first step forces clarity on the project's goals from the end-user's perspective. It establishes a clear definition of "done" before delving into technical details. It also ensures the LLM proceeds incrementally and doesn't jump ahead.

### Step 2: get a programming language suggestion

Next, Keith requested advice on what programming language to use for this project.Timestamp: [03:51]

The demo prompt:

Let's build a technical design for mdview. What language do you suggest we use? Give me three options and your final recommendation. And after I tell you, we'll write the technical design.

Why I like it:It can be tempting to default to familiar tools. However, this approach can sometimes lead to using the wrong tool for the job. This step serves as a helpful reminder to consider alternatives, whether by asking the LLM or evaluating options yourself. When the best approach involves an unfamiliar tool, it presents an opportunity to acquire a new skill!

### Step 3: create a technical blueprint

Once the user guide was approved, he had the agent act as a junior architect, suggesting technologies and outlining a technical design in anArch.mdfile.Timestamp: [05:00]

The demo prompt:

Let's author a technical design and save it to Arch.md. Be very detailed. Wait for my review before coding.

Why I like it:This separates the high-level design from the implementation. It creates a natural checkpoint for human review, allowing for changes and approval of the technical direction before committing to code.

### Step 4: generate a detailed, check-list style plan

This was the core of the template. Keith asked the agent to break down the entire project into a series of discrete, numbered tasks in aplan.mdfile.Timestamp: [07:00]

The demo prompt:

Now let's create a detailed task plan and save it to plan.md. Include in the plan.md some general workflow

Why I like it:This is the step that turns a fuzzy idea into an actionable project plan. It creates a clear roadmap for both the developer and the AI, preventing the agent from going off-track or attempting to build everything simultaneously.

### Step 5: give the AI meta-instructions on how to work

I found this to be a subtle but powerful part of the process. In addition to asking the AI to execute the plan, this prompt told ithow to use the plan.

The demo prompt:

Update plan.md when each task is completed with implementation notes. Update arch.md with any design changes. I will review, and then we'll start.

Why I like it:By instructing the agent to update theplan.mdfile with checkboxes and implementation notes after each step, he created a self-documenting workflow. This is valuable because it preserves the session's state, making it easy to review progress, debug, or even step away and resume the project another day. It also keeps other documents up to date with changes.

### Bonus step: add personality! 🤪

The part of this demo that tickled me most is when Keith decided to inject some personality into the interaction. This was a fun reminder that we can adjust how the AI interacts with us to enhance our experience.Timestamp: [09:23]

The demo prompt:

From here on out, address me as K-bro. And use puns liberally.

The AI immediately obliged, quipping things like, "Alright, K-bro, consider it done!" and "It's time to make this code look rich" (punning on the use of therich library).

Why I like it:Adding these kinds of personality adjustments could add intermittent giggles and delight into the driest of projects. (Listen and you'll hear me laughing in the background at this part. :p) Why not make the entire development process more enjoyable, creative, and feel less like working with a sterile machine?

❓Question for you:What ideas do you have for injecting personality into your workflow? I'd love to see your examples!

Beyond the fun, the demo left me with a few key takeaways about how I'll approach AI-assisted development from now on.

## My takeaways

### It's about exploration and acceleration

Keith’s workflow helped me reframe vibe coding. Instead of seeing it as just a tool for prototyping, I now see its value on a spectrum that goes from pure exploration to powerful acceleration.

For work you're not familiar with, like learning a new language or system, it’s a tool forexploration. The ability to experiment and iterate at a speed that was never before possible is a massive advantage. Projects you might have put aside because the learning curve was too steep are now accessible.

For work you already know inside and out, it's a tool foracceleration. As Keith's demo showed, the most productive AI users are experts in their domain. They can offload the mundane parts of their job—like writing boilerplate code or hundreds of tests—making them faster and, frankly, happier.

This interview made me want to go out and build more things. To experiment more, prototype more, and see what I can quickly whip together to solve problems in my own work and life. I hope it inspires you as well. (Get started withGemini CLI.)

### I love process

This is something I already knew about myself. I've always appreciated the value of process, not for its own sake, but for its ability to improve collaboration and efficiency. When I identify areas where a little structure could greatly enhance how people work together, I am driven to implement it, regardless of my official role or priority.

I don't think I realized how much this type of structure was missing from my own iterative LLM workflow. And not just for development, but for any task I'm trying to complete with an AI.

## What else?

There are many effective ways to structure an iterative LLM /vibe codingworkflow. I am curious about what other approaches people have found effective.

❓Question for you:What other workflows have you found effective?

For our complete conversation, watchAgent Factory S1E6or check out theEpisode Recap Blog Postfor an overview of episode segments with links and timestamps.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse

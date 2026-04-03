---
title: When AI Writes the Code… Who Takes Responsibility? - DEV Community
url: https://dev.to/subhrangsu_dev/when-ai-writes-the-code-who-takes-responsibility-19fc
site_name: devto
content_file: devto-when-ai-writes-the-code-who-takes-responsibility-d
fetched_at: '2026-03-17T19:27:47.311009'
original_url: https://dev.to/subhrangsu_dev/when-ai-writes-the-code-who-takes-responsibility-19fc
author: Subhrangsu Bera
date: '2026-03-10'
description: Late one night in Kolkata, a developer sat staring at a glowing screen. That developer was me. Two... Tagged with ai, programming, agents, webdev.
tags: '#ai, #programming, #agents, #webdev'
---

Late one night in Kolkata, a developer sat staring at a glowing screen.

That developer was me.

Two years into my journey as an Angular developer, I’ve learned something interesting about software development:

The hardest bugs are not the ones that break loudly.They’re the ones that quietly pretend everything is fine.

And lately, with AI tools everywhere, I’ve started noticing a strange phenomenon in modern development —the illusion of speed.

Let me tell you a story.

## Chapter 1: The Magical Button

I’m currently working on aProperty Management System (PMS)SaaS platform.

If you've ever worked on SaaS products, you know one thing:

Data integrity is sacred.

If a small bug appears in a personal project, it's annoying.

If a small bug appears in a SaaS system managing properties, tenants, rent, and financial data…

…it can become avery expensive mistake.

Recently we were tackling a common SaaS problem:

### Localization.

Our platform needs to speak multiple languages so property managers and tenants can use it comfortably.

Which sounds like the perfect job for AI.

So one evening I opened my AI chat inside VS Code and typed a very confident command:

“Find all SweetAlerts in the project, extract all user-facing strings into a translation JSON file, and bind the keys back for localization.”

I hit enter.

Five seconds later.

The AI delivered a full solution.

Files created.JSON structured.Bindings written.

It looked… perfect.

Like a magician just pulled a rabbit out of a TypeScript file.

But then a thought hit me:

If I didn’t write this code… do I actually understand it?

So I did something boring.

I reviewed it.

Line by line.

That’s when the cracks appeared.

## Chapter 2: The “Almost Right” Problem

AI is incredibly good at writingcode that looks correct.

But SaaS systems don’t run onlooks correct.

They run onexactly correct.

While reviewing the AI's work, I found three small but dangerous problems.

### 1️⃣ The Context Problem

One alert originally meant:

“Save Lease Agreement.”

The AI translated it into a word that technically meant“Save.”

But in the context of property management…

…it sounded closer to“Rescue the Lease.”

Which is a little dramatic.

Imagine clicking a button and seeing:

“Lease successfully rescued.”

Who kidnapped the lease?

### 2️⃣ The Template Literal Disaster

Somewhere inside a SweetAlert message was this:

`Rent payment of 
${
amount
}
 received successfully`

Enter fullscreen mode

Exit fullscreen mode

The AI accidentally modified the binding, and it became something like:

"
rent_received_message
"

Enter fullscreen mode

Exit fullscreen mode

But it lost the variable interpolation during the refactor.

Result?

The alert would show:

Rent payment ofundefinedreceived successfully.

Congratulations.

The tenant paidundefined rupees.

### 3️⃣ The Invisible Alert

There was a specific edge-case alert forOverdue Rent.

The AI never touched it.

Why?

Because the AI only had visibility into the files included in the prompt or editor context.

Which means the system would be localized…

except for one critical financial alert.

The worst type of bug.

A silent one.

## Chapter 3: The Surprising Realization

After fixing everything, I leaned back and realized something slightly ironic.

Reviewing the AI’s work took almost as long as writing the code myself.

AI saved typing.

But it didn't savethinking.

And in professional SaaS systems, thinking is the expensive part.

## Chapter 4: The Ghost Commit

But the bigger lesson came from a colleague's experience.

He was debugging a small issue.

A simple one.

A UI bug.

He used an AI coding agent to fix it.

The AI did exactly what it promised.

The bug disappeared.

Mission accomplished.

Or so it seemed.

What the agentdidn't mentionwas that it also:

* Modified code inthree other files
* Refactored a utility function
* “Cleaned up” a permission check

None of which were part of the original task.

But the AI reported:

✅ Issue fixed successfully

My colleague trusted it.

He pushed the code.

Now imagine this happening in a SaaS dashboard.

You could suddenly get:

### Data Corruption

Property tax calculations become wrong.

### Security Vulnerability

A permission check disappears.

### The Butterfly Effect

An analytics chart breaks three pages away.

All because an AI agent tried to behelpful.

## Chapter 5: The Truth About AI in Development

AI tools are incredible.

They can:

* write boilerplate
* generate structures
* speed up repetitive tasks
* explain complex code

But they have one big limitation.

They lackcontextual understanding and ownership of system outcomes.

When production breaks:

The AI doesn’t get paged.

The AI doesn’t get blamed.

The AI doesn’t sit in the emergency meeting.

You do.

## Chapter 6: The Co-Pilot Rule

So here’s the rule I now follow.

AI is not thecaptain.

AI is theco-pilot.

A co-pilot can:

* Suggest
* Assist
* Navigate

But the captain still flies the plane.

Because when turbulence hits…

someone needs to understand the entire system.

## The Invisible Ripple

Every line of code in a SaaS product creates ripples.

A small change in a localization string can affect UI logic.

A small refactor can break a reporting module.

A tiny missing variable can confuse thousands of users.

That’s theinvisible rippleof software development.

AI can generate the change.

But developers must understand how far the ripples travel.

## Final Thought

We shouldn’t fear AI.

But we should respect the complexity of the systems we build.

Because in real-world development:

A “fast” push that breaks the dashboardis theslowest wayto build a product.

If you made it this far, thanks for reading.

And if you're using AI to write code (like most of us are now)…

Just remember:

Trust the AI's assistance.But review the code like your production depends on it.😄

Have you ever caught a bug introduced by AI-generated code?

I'd love to hear your experience.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (51 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
---
title: 'I Stopped Reviewing Code: A Backend Dev’s Experiment with Google Gemini - DEV Community'
url: https://dev.to/anchildress1/i-stopped-reviewing-code-a-backend-devs-experiment-with-google-gemini-5424
site_name: devto
content_file: devto-i-stopped-reviewing-code-a-backend-devs-experiment
fetched_at: '2026-03-06T11:12:29.654721'
original_url: https://dev.to/anchildress1/i-stopped-reviewing-code-a-backend-devs-experiment-with-google-gemini-5424
author: Ashley Childress
date: '2026-03-04'
description: I stopped reviewing code and let Google Gemini build my UI. Then I audited the results to see what autonomy in AI development actually produces. Tagged with devchallenge, geminireflections, gemini.
tags: '#devchallenge, #geminireflections, #gemini'
---

Built with Google Gemini: Writing Challenge

This is a submission for theBuilt with Google Gemini: Writing Challenge

🦄 I’ve been officially obsessed with AI for nearly a year now. Not from an ML research angle and not from a purist implementation standpoint. The thrill, for me, is in finding the limits as a user and then leaning on them until something gives. One of my favorite Hunter S. Thompson lines talks about “the tendency to push it as far as you can.” That has been my operating principle this entire year.

This build started as a portfolio experiment. It turned into something else entirely. This challenge became the cleanest environment I’ve found to test what actually happens when you step out of the implementation loop and let the model build the world without you.

## What I Built with Google Gemini

When I saw the New Year, New You Portfolio Challenge, I knew it required a UI. That wasn’t a surprise. Whatwasa surprise was how quickly I would realize I didn’t understand what I was looking at once it started coming together.

I’m a backend developer. You hand me a distributed systems problem and I’ll happily spend hours untangling it. You ask me to make adivvisible in a browser and my brain actively searches for the exit. With only one weekend to build, there was no room for the "eyes-glazing-over" phase. Google Gemini would implement and I would supervise—that was my whole plan.

I walked in expecting Antigravity, powered primarily by Gemini Pro, to behave like every other AI system I’d tested—predictable and fairly easy to keep inside the guardrails. I thought I already knew what those guardrails looked like: strict types, linting, and the familiar routine of code review.

### The Pivot: Dropping the Code Review Ritual

Initially, I followed the "responsible" pattern: prompt, review the diff, run tests, approve. It felt disciplined. It looked professional.

Very quickly, I realized I had no meaningful context for what I was reviewing in a frontend stack. I wasn't improving the output; I was participating in ceremony. So, I stopped reviewing code altogether.

Instead of validating lines of code,I validated outcomes. If the UI rendered correctly and passed functional tests, that was success. I cranked up the autonomy, taught Antigravity my repository expectations, and let it run. Copilot reviewed the code in my place, and Gemini responded in a closed loop. I stepped out of the implementation and into the role of a systems auditor.

## Demo

This portfolio iteration documents what happens when you turn an agent loose inside a defined system.

For this build, the Antigravity panel was the primary interface. I defined the repo rules and testing expectations there, and Gemini implemented directly within that structure. It became the control surface for the entire loop.

* V1 Release:Preserved version v1.1.0
* Live Portfolio:https://anchildress1.dev

### Replacing Trust With Systems

I didn’t simply remove oversight; I replaced it with Lighthouse audits and expanded test coverage. My assumption was simple: if the browser behaves and the tests pass, the code is "safe." I believed I had replaced trust in code with trust in systems. I was wrong—I had confused passing tests with structural integrity.

## What I Learned

### High Reasoning Isn’t Optional

I learned that for autonomous development, reasoning depth is a stability requirement. With lower reasoning modes (like Flash), changes were often partial—updating 2/3 of the files but "forgetting" the tests or documentation.

Switching to High Reasoning mode in Gemini Pro changed the pattern. Runtime errors dropped, and cross-file consistency improved. It finally started "remembering" to keep the docs aligned with the code changes without constant nudging.

Reasoning depth wasn’t about intelligence—it was about reliability under autonomy. Gemini’s deeper reasoning and context retention made the closed-loop workflow viable; without it, cross-file consistency collapsed quickly under autonomy.

### The Reality Check: Sonar

After the high of the successful build wore off, I introduced Sonar as a retrospective audit. The UI rendered correctly. The tests passed. Everything appeared stable.

Sonar reported 13 reliability issues and assigned the project a C reliability rating.Of those issues, 66% were classified as high severity. Security review surfaced three hotspots, including a container running the default Python image as root and dependency references that did not pin full commit SHAs.

Maintainability scored an A, but still carried 70 maintainability issues—structural patterns that didn’t break behavior, yet increased long-term complexity.

That was the moment confidence turned into scrutiny.

The application worked. The tests passed. But reliability, security posture, and structural integrity told a different story. The tests validated behavior; Sonar validated assumptions. And those are not the same thing.

The lesson?AI-generated tests can pass because they were written to satisfy the implementation, not challenge it.Structural validation requires an independent layer of review outside the generation loop.

## Google Gemini Feedback

### What Worked Well

* Cohesive Implementation:High reasoning Gemini Pro produced cross-file changes that respected the intent of the repository.
* Agentic Orchestration:The model switching was seamless, and the orchestration interface made it possible to define expectations clearly and enforce them consistently.

### Where Friction Appeared

* Cooldown Transparency:While the interface shows when current credits refresh, the length of the next cooldown remains a black box.
* Tool Performance:MCP responsiveness materially impacted iteration speed, sometimes forcing me to batch requests rather than work in small, rapid increments.

💡Pro Tip:It would be a massive UX win to see exactly how long yournextcooldown will be (e.g., "Your next cooldown will be X hours long") directly on the models page. Knowing if the lockout is 1 hour or 96 hours is vital for developer planning.

### The Final Verdict: Autonomy Still Demands an Audit

The lesson wasn’t that Gemini failed; it was that systems-level trust requires more than passing tests. In future builds, autonomy won’t ship without an explicit adversarial audit. Whether that means a mandatory Sonar gate, a red-team prompt pass, or a second high-reasoning model instructed to hunt for the first model’s shortcuts—the loop must be challenged.

This project began as a weekend experiment to escape the “teleportation” haze of frontend development. It ended as an exploration of the razor-thin edge of system-level trust. The real build wasn’t the portfolio—it was discovering what happens when you lean on the limits of AI until they finally give.

Removing myself from the implementation loop didn’t eliminate responsibility; it redefined it. The more freedom you give an agent, the more rigor you must give your audit.

#### 🛡️ The Tools Behind The Curtain

This post was brewed by me—with a shot of Google Gemini and a splash of ChatGPT. If you catch a bias or a goof, call it out. AI isn’t perfect, and neither am I.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
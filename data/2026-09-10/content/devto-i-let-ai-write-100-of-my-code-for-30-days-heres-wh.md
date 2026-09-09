---
title: I let AI write 100% of my code for 30 days. Here's what broke. - DEV Community
url: https://dev.to/infoinlet1/i-let-ai-write-100-of-my-code-for-30-days-heres-what-broke-1aa0
site_name: devto
content_file: devto-i-let-ai-write-100-of-my-code-for-30-days-heres-wh
fetched_at: '2026-09-10T07:20:47.832615'
original_url: https://dev.to/infoinlet1/i-let-ai-write-100-of-my-code-for-30-days-heres-what-broke-1aa0
author: Info Inlet
date: '2026-09-09'
description: 'Not "AI-assisted." Not "copilot suggestions I edited." I mean I made a rule: for 30 days, I don''t... Tagged with ai, webdev, programming, career.'
tags: '#ai, #webdev, #programming, #career'
---

Not "AI-assisted." Not "copilot suggestions I edited." I mean I made a rule:for 30 days, I don't type application code. The AI does. My job is to describe, review, and approve.

I shipped a real product this way — a small SaaS with auth, Stripe billing, a dashboard, and a public API. It works. It's in production. And along the way I found out exactly where the "AI writes everything now" dream holds up and where it quietly falls apart.

This isn't a hype post and it isn't a doom post. It's a field report.

## The rules

To keep myself honest:

1. I don't write application logic by hand. I prompt, the AI writes.
2. Icanread every line, reject it, and ask again — but I can't fix it myself in the editor.
3. Config, secrets, and "click the button in the dashboard" steps are mine (the AI can't do those anyway).
4. If I get truly stuck for more than an hour, I log it as a "break" and write the code myself.

By the end I had9 logged breaks.Those breaks are the interesting part.

## What worked shockingly well

Let me be fair to the machine first, because a lot of this genuinely surprised me.

Greenfield scaffolding is basically solved."Set up a Next.js app with Postgres, Drizzle, and auth" — done, correctly, in one shot. The first 40% of the project flew by faster than I've ever built anything.

Boilerplate it never gets wrong.CRUD endpoints, form validation, Zod schemas, a table component with sorting and pagination. This is the stuff I hate writing and it produced it perfectly, every time, no notes.

It's a phenomenal rubber duck."Why is this query slow?" got me a better answer than I'd have reasoned to alone — it spotted a missing index and an N+1 in the same breath.

For the first week I genuinely thought I'd write the "developers are obsolete" post. Then week two happened.

## What broke — the 9 breaks, honestly

### Break 1–3: It can't hold thewhole systemin its head

The AI is brilliant at the file in front of it and blind to the one three folders over. It happily wrote a secondformatCurrencyhelper because it didn't know the first one existed. It re-implemented my auth check inline instead of using the middleware I already had. It introduced a subtly differentUsertype in a new module.

None of these are "bugs" — everything compiled, everything passed. They'rearchitecture drift.And architecture drift is invisible until the day it costs you a week.

The AI optimizes locally. Coherence across a system is still a human job.

### Break 4–5: It confidently writes plausible, wrong code

The scariest failures weren't crashes. They were code thatlookedright and ran fine on the happy path.

The billing webhook handler it wrote acknowledged Stripe events before persisting them. Works perfectly in testing. In production, a DB blip = a paid customer with no access and no record. I only caught it because I've been burned by exactly this before.A junior copying this AI's output would not have caught it.That's the part that keeps me up.

### Break 6: Debugging its own code is a loop of despair

When something broke that the AI couldn't see, asking it to fix it producedchanges, notfixes. It would confidently rewrite the function, swear the bug was gone, and reintroduce it two prompts later. Without the ability to drop into the debuggermyselfand actually understand the state, we'd have spun forever. This was the single biggest time sink of the month.

### Break 7–8: Taste, and saying "no, less"

Asked for a settings page, it gave me 14 options no user asked for. Asked for error handling, it wrapped everything in try/catch and swallowed the errors. The AI's instinct is toadd. Knowing what to leave out — the actual product-design part of engineering — it has none of.

### Break 9: The last 10% is still 90% of the work

Getting to "demo works" took a week. Getting to "handles a real user doing something weird at 2am" took the other three. Edge cases, race conditions, the empty state, the error state, the "what if they double-click" state — the AI does none of this unless youknow to ask, and knowing to askis the job.

## The uncomfortable synthesis

Here's what I actually believe after 30 days:

AI didn't replace me. It replaced the *tasks I used to give juniors.* The scaffolding, the boilerplate, the first draft — that's exactly the work a junior learns on. And that's the real problem nobody's pricing in: if the AI does all the entry-level work,where does the next senior come from?You can't skip the 10,000 hours; you can only move where they're spent.

The skill that mattered every single day wasn't writing code. It was:

* Knowing the code it gave me was subtly wrong.
* Knowing what tonotbuild.
* Holding the whole system in my head so I could catch the drift.

Those are allseniorskills. Which means AI didn't flatten the hierarchy — it made the top of it more valuable and kicked away the ladder to get there.

## What I actually changed

I didn't stop using AI — I use it for 100% of thetypingnow and always will. I changed the guardrails around it, and every one of them maps to a break above:

* The thing that writes the code isneverthe thing that reviews it. A separate reviewer, prompted torefutethe diff, catches the plausible-but-wrong code the author will always wave through.
* Nothing merges without a human who can see the blast radius the model can't.
* "It compiles and the tests pass" is thestartof review, not the end — because the model will write tests that agree with its own wrong mental model.

That separation — author here, skeptic there, human on the merge button — is the whole reason I could hand the typing to a machine and still sleep. It's also, not coincidentally, exactly how we buildxenition: agents that do the work, a different agent that tries to tear it down, and a person who owns the decision. Dogfooding that on a real 30-day build is the only benchmark I trust.

## Would I do it again?

For a prototype? In a heartbeat — I'd never scaffold by hand again.

For production? I'll use AI for 100% of thetypingand 0% of thethinking. The typing was never the hard part. It just felt like it was.

So, honest question for the comments:if AI is doing the junior work, how does your team plan to grow the next generation of seniors? Because I don't think "they'll figure it out" is an answer anymore. 👇

(If this was worth your time, a ❤️ and a 🔖 help — and tell me your worst "the AI wrote something that looked totally fine" story below.)

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
---
title: The future belongs to those who can refute AI, not just generate with AI - DEV Community
url: https://dev.to/shrsv/the-future-belongs-to-those-who-can-refute-ai-not-just-generate-with-ai-28i0
site_name: devto
content_file: devto-the-future-belongs-to-those-who-can-refute-ai-not
fetched_at: '2026-02-25T19:26:46.813661'
original_url: https://dev.to/shrsv/the-future-belongs-to-those-who-can-refute-ai-not-just-generate-with-ai-28i0
author: Shrijith Venkatramana
date: '2026-02-19'
description: The assumption in software engineering circles has been that if AI lets us write code faster, we will... Tagged with career, ai, discuss, programming.
tags: '#discuss, #career, #ai, #programming'
---

The assumption in software engineering circles has been that if AI lets us write code faster, we will build more things and move faster.

That assumption misses a step.

Writing code is not the same as integrating it, maintaining it, or trusting it.

We are starting to discover that verification does not scale the way generation does.

I argue that the engineer who thrives in this environment willnotbe the one who can prompt the largest code output. It will be the one who can look at what comes out and reliably decide what survives.

This post is aboutwhy that skill — of refutation — is about to become central,and what it means for how we build software.

## 1. Volume is no longer a signal of value.

We are in the middle of a real GenAI explosion.

Code, images, video, documents — all of it can now be generated at a cost that is rapidly approaching zero compared to the historical human-labor baseline.

In software engineering especially, the ability to write a lot of code has traditionally been associated with productivity and even creativity.

That association is now breaking down.

We can generate more than ever before, faster than ever before.

Volume by itself has lost meaning.

## 2. Knowledge is what survives attack.

To understand what is changing, it helps to step back and borrow from epistemology.

Epistemology is the branch of philosophy that separates knowledge from what is not knowledge.

Merely having experience with something is not knowledge.

Repeating what supposed authorities have propounded is not knowledge.

Making statements based on experience is not knowledge either.

Statements become candidates for knowledge only when they are internally consistent, publicly testable, and able to survive adversarial scrutiny.

## 3. Value is revealed under attack, not in the design lab

A useful analogy is military hardware.

The worth of a battle tank is not established in the design lab or by marketing brochures.

Its worth is demonstrated by how it withstands attack in actual battle.Until it has faced stress, resistance, and hostile conditions, we cannot make serious claims about its efficacy.

The same applies to ideas, designs, and code. Their value is revealed under attack.

## 4. The source of an idea does not matter; only its survival matters.

Karl Popper made this explicit: the source cannot be trusted.

It does not matter whether a claim comes from a famous scientist, a senior engineer, or a large language model.

What matters is whether the claim survives attempts to falsify it.

Knowledge grows through conjecture and refutation, not through confident assertion.

Popper was writing about the demarcation of science from non-science, but the pattern applies more broadly: without the possibility of being shown wrong, we cannot claim to have learned anything.

## 5. GenAI is a conjecture engine; everything it produces is provisional.

GenAI, at its core, is a conjecture engine.

Every piece of generated code is a proposed theory about how a system should behave.

Every generated explanation is a proposed interpretation.

All of it must be treated as provisional.

Everything AI generates should be considered a proposed theory and then subjected to severe testing and criticism to see if it survives.

## 6. We already had systems for adversarial scrutiny (CI/CD, code review).

This was already true in the pre-AI world.

That is why we invented code review, linters, and continuous integration in the first place. We recognized that humans make mistakes, that first drafts are often wrong, and that structured criticism improves outcomes.

CI/CD pipelines, unit tests, and integration tests are all mechanisms for subjecting code to adversarial scrutiny.

In that sense, applied Popperian epistemology has been embedded in our workflows for years.

## 7. Historical software growth: about 20% per year.

What changes now is scale.

In 2016, Professor Hatton and his team publishedThe Long-Term Growth Rate of Evolving Software.

They studied how software codebases grew over time, long before GenAI was in the picture.

Their finding was strikingly consistent: historically, software projects grew at about a 20% compound annual growth rate (CAGR).

At that rate, a codebase roughly doubles in size in about four years.

It is important to note that this paper describes how codebases actually grew, not a theoretical maximum. It is a historical baseline, not a physical law.

## 8. Monster codebases are a plausible outcome of AI-driven productivity.

Now consider what happens if AI meaningfully boosts developer productivity.

If productivity doubles and CAGR moves toward 40%, doubling time shrinks to roughly two years.

If productivity increases fivefold and we approach 100% CAGR, a codebase doubles every year.

Over a decade, that compounding is explosive. A 5× productivity boost sustained over ten years could translate into a roughly 165× increase in code volume.

A medium-sized 100,000 LOC codebase could plausibly turn into 100 million LOC.

For context, the Linux kernel reached around 40 million LOC after three decades of evolution.

We are potentially heading toward “monster codebases.”

## 9. But isn’t growth bounded by complexity? Yes, but significant growth is still likely

This projection invites immediate objections.

First, the 20% CAGR comes from a pre-LLM world; using it to predict a post-LLM world is logically tension-ridden.

The historical trend gives us a baseline against which to measure disruption.

If the trend holds, nothing changes.

If it breaks, we need to understand the new environment.

Second, software growth is bounded by complexity, not just typing speed.

A 100 million LOC codebase might be unbuildable or unmaintainable regardless of how fast we can write code, because integration complexity grows faster than linearly.

If we generate code faster than we can manage its integration complexity, we build systems that collapse under their own weight.

The question is whether our verification systems scale with it.

## 10. The old equilibrium between writing and reviewing code breaks at scale.

Historically, review processes could grow alongside codebases.

If code grew 20% per year, human review capacity could roughly keep pace.

But if code volume grows by multiples, not percentages, the old equilibrium breaks.

We move from incremental growth to bulk production of code.

How will refutation grow with generation?

## 11. AI must help with verification, or human review collapses.

At that point, attention becomes the scarce resource.

As generated output increases, value shifts from production to selection.

The key problem becomes: how do we direct limited human attention to the most important risks inside an ocean of machine-generated diffs?

How do we build higher-level representations that compress massive change into manageable insight?

There is no realistic path forward without using AI to verify as well.

Human-only review cannot keep up with machine-scale generation.

AI must help draw attention to useful things, highlight potential constraint violations, detect behavioral drift, and reduce the burden of review.

Verification must become partially automated, or it simply collapses.

## 12. But if AI is flawed, can AI review be trusted? (The infinite regress problem).

This is where the most obvious objection arises: if the AI that generates code is flawed and produces hallucinations, why would an AI that reviews code be any less flawed?

Would this not simply compound errors rather than catch them? This is sometimes called the infinite regress problem — if we need an AI to check the AI, who checks the checker?

## 13. Specialized review AI is different from general generation AI.

The answer lies in specialization.

A review AI does not need to be a general intelligence.

It needs to be a focused tool for checking specific properties: type correctness, conformance to project style, violation of defined architectural boundaries, or behavioral drift captured by property-based tests.

The model used for review can be different from the one used for generation — smaller, more conservative.

Review AI is not asked to have an opinion about whether code is “good.”

It is asked to surface anomalies to a human.

It acts as a tireless, fast, but ultimately fallible junior reviewer whose job is to flag anything unusual and let the senior engineer make the final call.

The goal is not to eliminate human judgment, but to focus it.

## 14. Guardrails belong in verification, not just generation.

This is also where guardrails belong.

Guardrails should primarily sit on the verification layer, not the generation layer.

Trying to constrain generation alone is like trying to prevent all bad tank designs at the drawing board.

A more robust approach is to subject every design to rigorous criticism and stress testing.

Instead of focusing on censoring models as the main control mechanism, we should upgrade our verification methods.

There is room for debate here: some harms occur at the moment of generation, not execution, and generation-layer guardrails address those.

But for engineering reliability, verification is where the leverage lies.

## 15. Perhaps we’ll write less, more leveraged code. But verification shifts, it doesn’t disappear.

A different kind of objection comes from economics.

Perhaps the future is not monster codebases but minimal, highly leveraged ones.

If code becomes cheap, the incentive to write efficient, reusable abstractions increases.

Why generate a thousand lines of boilerplate when a ten-line configuration file powered by AI does the same thing?

This is possible.

But even minimal codebases require verification of their minimal parts, and the leverage increases the blast radius of any mistake.

Whether code volume expands or contracts, the verification load shifts rather than disappears.

The scarce resource remains human attention directed at the right places.

If GenAI scales conjecture, ReviewAI must scale refutation.

## 16. Market saturation might limit growth, but problem space is far from exhausted.

Another objection is that growth in code volume will eventually hit market saturation.

We do not have an infinite number of meaningful problems to solve. After a point, generating more code just creates noise and technical debt.

But this assumes that the problem surface is close to saturated. It is not.

Consider countries like India. Large-scale infrastructure gaps, pollution management, logistics inefficiencies, healthcare access, education quality, urban planning, agricultural optimization — these are not marginal problems.

They are system-level challenges that require coordination, monitoring, simulation, automation, and optimization at scale. All of these increasingly rely on software.

Even in developed economies, software penetration into physical systems is still incomplete: energy grids, water systems, public transport, manufacturing, climate modeling, robotics, biotech.

As capability expands, software does not merely fill existing markets; it enables new domains of intervention.

Historically, when production capacity increases, demand tends to expand into areas previously considered infeasible.

The limiting factor has rarely been a shortage of problems. It has been cost and coordination.

## 17. Engineering must adapt, because norms evolve too slowly.

Engineering as a field needs to internalize this shift.

The discipline has always depended on separating what works from what merely appears to work.

Having experience building something does not make it reliable.

Having it survive adversarial testing does.

With code volume potentially compounding at unprecedented rates, we do not have the luxury of slowly evolving norms.

We need accessible, cost-effective verification tools that integrate directly into development workflows.

## 18. A concrete direction: automated review on every git commit.

Inmy own work on AI-assisted code review, I have been building tooling that triggers review automatically when diffs are committed to git repositories.

The idea is straightforward: treat every change as a hypothesis and subject it to systematic attack.

In a sense, this is applied Popperian epistemology embedded in CI/CD. The goal is not to slow down generation, but to make criticism abundant.

I do not claim this solves every problem.

The tools are early, the approaches are experimental, and the infinite regress concern is real.

But it’s time we started taking our ReviewAI stack more seriously.

## 19. The future belongs to those who can refute, not just generate.

GenAI has made conjecture cheap.

The risks of compounding error are real.

If we do not make refutation equally powerful and widely available, we risk drowning in our own output.

The future of engineering in the AI era will not be decided by how much we can generate, but by how rigorously we decide what survives.

And that decision of what survives, in the end, remains a human responsibility.

And I for one hope that Refutation as an idea gets taken as seriously as the idea of generation in the industry.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse

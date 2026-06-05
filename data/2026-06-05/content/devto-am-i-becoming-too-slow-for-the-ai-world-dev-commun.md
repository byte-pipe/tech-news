---
title: Am I Becoming Too Slow for the AI World? - DEV Community
url: https://dev.to/marcosomma/am-i-becoming-too-slow-for-the-ai-world-1904
site_name: devto
content_file: devto-am-i-becoming-too-slow-for-the-ai-world-dev-commun
fetched_at: '2026-06-05T12:03:58.360631'
original_url: https://dev.to/marcosomma/am-i-becoming-too-slow-for-the-ai-world-1904
author: marcosomma
date: '2026-06-03'
description: The AI world is full of old infrastructure with stochastic organs. That sentence probably explains... Tagged with ai, programming, productivity, career.
tags: '#ai, #programming, #productivity, #career'
---

Verification as the new engineering bottleneck

The AI world is full of old infrastructure with stochastic organs.

That sentence probably explains better than anything why I feel slow lately. Not because I stopped caring about AI. Not because I cannot build anymore. Not because the tools moved beyond me. If anything, the tools moved in the opposite direction: they make me faster at generating code, faster at prototyping, faster at touching layers I would normally approach one by one.

And still, inside the work, I feel slower.

This is the uncomfortable part. AI gives me the sensation that everything should move faster, but the more I use it seriously, the more I end up spending time in the parts that do not accelerate cleanly. The code appears quickly. The draft appears quickly. The workflow appears quickly. But then I need to understand what it actually does. I need to test the boundary between components. I need to verify that the result is not just plausible, but correct enough to survive contact with reality.

Maybe this is the first real trap of AI development:

Creation became cheap. Verification did not.

That sounds simple, almost too obvious, but I think it is the reason many of us feel this strange mismatch between speed and exhaustion. We can now produce more surface area than we can comfortably inspect. A feature that would have taken days to sketch can appear in hours. A backend route, a frontend component, a prompt chain, a test, a deployment script, a workflow diagram: all of it can be generated quickly enough to create the illusion that the whole process compressed.

But the whole process did not compress.

The expensive part moved.

You still have to understand the system. You still have to validate the assumptions. You still have to test the end-to-end behavior. You still have to ask whether the thing is stable, maintainable, safe, observable, and aligned with the original intention. AI made the first draft cheaper, but it also made it easier to produce first drafts across more layers at once. So the final burden often becomes larger, not smaller.

Before AI, there was a natural friction in development. You wrote more slowly, so production and understanding were closer together. Now production can sprint ahead of understanding. You can build faster than you can digest. And once that happens, the bottleneck becomes obvious.

It is not typing.

It is not even coding.

It is judgment.

This is where my feeling of slowness begins. I am not slow in the part that AI is good at accelerating. I am slow in the part that matters after acceleration. I am slow when I need to decide whether a generated thing deserves to exist inside a system. I am slow when I need to move from “this works once” to “this is trustworthy enough to become infrastructure.”

That kind of slowness does not look good in a noisy field.

The AI world rewards motion. It rewards people who react quickly, rename quickly, package quickly, comment quickly, and post before the concept has cooled down. Every week there is a new model, a new benchmark, a new agent framework, a new “this changes everything” moment, a new tool that is apparently going to replace half the industry and then disappear into a GitHub archive two weeks later.

At some point, I became tired of chasing it.

Not completely. I still follow the field. I still care about what matters. But I no longer have the energy to treat every release, every demo, every thread, and every AI product with a gradient background as if it deserves my full attention. A proof of concept is not a product. A prompt chain is not cognition. A wrapper is not infrastructure. A dashboard is not an operating system for intelligence just because someone wrote “agentic” in the hero section.

After a while, the noise becomes expensive.

And when I stopped chasing every update, something strange happened. I did not become less interested in AI. I became more interested in older things.

Distributed systems. Permissions. Control loops. Network optimization. Separation of concerns. Routing. Handshakes. Feedback. Biological systems. Ant colonies. Viruses. Evolution. Complex adaptive systems.

The more I look at AI, the more I see old problems returning in a new substrate. Not copied perfectly. Not solved automatically. But returning. The same families of problems keep appearing under newer language. How do parts coordinate? Who is allowed to access what? Where does a decision happen? What happens when a component fails silently? How do you stop local uncertainty from becoming global corruption? How do you keep a system observable when some of its organs speak in probabilities?

That is why I keep saying that AI infrastructure often feels like old infrastructure with stochastic organs. The body is familiar. The organs behave differently.

And this is where I need to be more precise, because vague depth is too easy. Saying “old principles return” is not enough. It risks becoming another elegant sentence that avoids doing the actual work.

Take orchestration.

A lot of what people now call AI orchestration is not conceptually new. We already had coordination, routing, permissions, queues, retries, fallbacks, handshakes, separation of concerns, and validation boundaries. None of those appeared because LLMs arrived. They were already part of software, distributed systems, automation, and infrastructure engineering.

But the component changed.

A deterministic service fails in ways we can often reason about. A request times out. A schema breaks. A permission check rejects access. A queue stalls. A dependency returns an error. The failure may be painful, but at least it often announces itself.

A generative component can fail while sounding successful.

It can return a clean boolean and still be wrong. It can pass a check while carrying uncertainty underneath the return type. It can produce a fluent answer that looks like completion but is actually drift. It can say “yes” with confidence because the prompt, the model, and the input distribution all lined up toward the same blind spot.

That is the part that changes the orchestration problem.

The old principle still matters: boundaries are useful. Checks are useful. Separation of concerns is useful. Permissions are useful. But the error model under the boundary is different. A handshake with a stochastic component is not the same as a handshake with a deterministic one. The interface may look clean, but the uncertainty has not disappeared. It has been compressed.

This is why I do not think the right adaptation is simply “use AI, then check AI.” That is too soft. It sounds responsible, but it hides the important question: what kind of check, under what error model, with what independence assumptions?

Imagine a pipeline like this:

A > B > C > final check

If the final check passes, the system continues. If it fails, the system routes somewhere else. This is simple. It is also risky, because an early hallucination can travel through the whole chain before being inspected.

So we make the process more granular:

A > check > B > check > C > check > evaluate checks

That feels better, and in many cases it is better. Granularity gives the system a higher sampling rate. It interrupts compounding. It catches problems earlier. It lowers the impact of one local failure because the system becomes observable and interruptible at more points.

But it does not magically lower the uncertainty of the model.

It lowers propagated uncertainty. It lowers blast radius. It lowers the chance that one bad step contaminates everything downstream. Those are real gains.

But the atomic uncertainty remains.

And here is the part I think matters more than the usual AI safety slogan: more checks do not help much if all the checks share the same blind spot.

Classical retry logic quietly assumes some degree of independence. If a service call fails because of a transient network problem, trying again may work. If a worker crashes because of temporary load, retrying elsewhere may work. The same idea often gets imported into AI workflows without being inspected: ask again, check again, validate again, add another gate.

But generative errors are often correlated.

The same model, with the same prompt family, reading the same kind of input, can reproduce the same wrong conclusion several times. A pipeline can collect many green checkmarks that all share the same flaw. At that point, granularity does not create safety. It creates high-resolution false confidence.

That is the difference between variance and bias.

Granular checks help with variance. They catch random, local, one-off deviations. They make the system less fragile against isolated mistakes.

They do not fix bias. If the checker is systematically wrong, adding more instances of the same checker mostly multiplies the wrongness. It creates a beautiful row of confirmations over the same error.

This is where the old infrastructure metaphor starts breaking, and where another metaphor becomes useful.

The repair is not just retry.

The repair is decorrelation.

Different models. Different prompts. Different evaluation angles. Different representations of the same task. Different failure assumptions. Sometimes even different modalities of checking, where one component evaluates structure, another checks factual grounding, another verifies constraints, and another looks for contradiction.

That is not classical retry anymore.

That is closer to speciation.

You do not make the system robust by repeating the same organism. You make it robust by introducing enough variation that one blind spot does not become a colony-wide disease. The same way biological systems survive not because every unit is perfect, but because diversity changes how failure propagates.

This is the bridge I keep finding between old engineering and the older biological material I have been reading for years.

I spent almost three years readingAnt Encounters. Not because the book was impossible to read faster, but because every page kept connecting to something else. A small observation about ants was not just about ants anymore. It became a question about local decisions, global behavior, task allocation, distributed coordination, and how a system can stabilize without one central source of truth owning every decision.

Now I am reading about viruses as complex adaptive systems, and the same thing happens. One page becomes a week of thinking. Adaptation, persistence, mutation, failure, survival under pressure, local variation, global behavior. Suddenly this is not only biology. It becomes a way to think about AI systems that cannot rely on perfect deterministic components but still need to produce reliable behavior.

Compared with the rhythm of the AI world, this looks absurdly slow.

People publish five takes about five new tools before lunch, and I am still stuck on one biological analogy from a book that is not even about AI.

But maybe “stuck” is the wrong word.

Maybe this is not reading. Maybe this is compilation.

The page is not being consumed. It is being linked. It enters a context made of old work, unfinished ideas, technical scars, software architecture, biological curiosity, and frustration with shallow AI products. The result is not speed. The result is compression. A small input creates a large internal reorganization.

That is valuable, but it has a serious problem.

It is invisible.

And maybe this is the real fear behind the question “am I slow?” Not that I am actually slow. Not exactly. The fear is that while I am connecting dots, the field will move on without seeing any of it. The fear is that depth without visible output becomes indistinguishable from absence. The fear is that the AI world is so loud, so accelerated, and so addicted to fresh vocabulary that if I do not constantly produce something visible, I will disappear inside the buzz.

That fear is not irrational.

The field rewards fluency in the language of the week. If the word is “agents,” everyone builds agents. If the word is “reasoning,” everything becomes reasoning. If the word is “memory,” every cache becomes memory. If the word is “workflow,” every sequence of API calls becomes a platform.

I understand why this happens. Attention is scarce. Timing matters. If you arrive too late, the conversation has already moved somewhere else.

But there is a cost to always moving at that rhythm. You risk becoming synchronized with noise. You start optimizing for being current instead of being correct. You learn how to speak the new vocabulary faster than you understand the old problem underneath it. You become responsive, but not necessarily thoughtful.

And I do not want that.

At the same time, I cannot use depth as an excuse forever.

This is the uncomfortable part, and I should not escape it with a nice sentence.

Sometimes I am not slow. I am filtering. Sometimes I am not slow. I am connecting. Sometimes I am not slow. I am refusing to spend cognitive energy on hype that will disappear in two weeks.

But sometimes I am hiding behind depth.

Not theoretically. Not as a universal writer problem. Me, now, in this exact pattern.

I can feel it when a connection stays private longer than it should. I can feel it when a thought keeps becoming more complex in my head because publishing it would make it smaller, exposed, and easier to criticize. I can feel it when “I am still thinking about it” starts as discipline and slowly becomes shelter.

That is the failure mode I need to catch.

Because slow thinking is valuable only if it eventually becomes visible, testable, shareable, or executable. Otherwise it is just private complexity. It may feel profound internally, but from the outside it has no weight.

This does not mean every thought needs to become a polished theory. That would create another paralysis. But the intermediate steps need to leave traces. The note after reading one page matters. The connection between ant encounters and AI routing matters. The observation that a model check is a handshake with uncertainty hidden under the return type matters. The idea that decorrelated evaluators are closer to speciation than retry matters.

Not because each fragment is complete.

Because the fragments show the work.

That is probably the artifact I keep underestimating: the process of connecting old principles to new systems while the connection is still messy.

The current AI discourse is full of people saying “look at this new thing.” Maybe there is space for someone saying “look at this old principle returning in a strange form, and look carefully at where the analogy breaks.”

That is not slower.

It is a different rhythm.

A rhythm that does not compete well with hype in the short term, but maybe ages better.

And maybe that is what I actually want. I do not want to win the weekly AI vocabulary race. I do not want to rebuild my thinking every time the market chooses a new word. I do not want to become another person who confuses speed with direction.

I want to understand what remains true after the buzzword moves away.

That kind of work is slower by nature. You cannot connect biology, distributed systems, software architecture, and AI orchestration at the speed of a product launch thread. You cannot build a durable mental model by reacting to every notification. You cannot understand a field only by consuming its newest claims.

But you can disappear while doing deep work silently.

That is the warning I take seriously.

Not “you are too slow.”

More like:

Your slowness needs output.

Slow and invisible is dangerous. Slow and traceable is different. Slow and executable is different. Slow and published is different. Slow and connected to experiments, code, diagrams, arguments, failures, and public reasoning becomes a body of work.

So maybe the answer is yes, I am slow.

But I am not slow because I am lost.

I am slow because I am trying to understand the machinery instead of just repainting the dashboard. I am slow because every new AI idea seems to drag behind it a much older question. I am slow because I do not trust speed when speed is mostly social pressure. I am slow because I keep finding useful ghosts from older fields inside the newest buzzwords.

The risk is not being slow.

The risk is letting the work stay trapped inside my head until the world has no way to distinguish depth from silence.

So I probably do not need to chase more.

I need to expose more.

I need to turn the reading into notes, the notes into arguments, the arguments into experiments, and the experiments into artifacts. Not perfectly. Not only when the whole theory is clean. Earlier. Messier. More honestly.

Because maybe, in this AI world, reacting to every buzzword is not the same thing as adapting.

Maybe the harder part is still being able to think when the buzzword is gone.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (28 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
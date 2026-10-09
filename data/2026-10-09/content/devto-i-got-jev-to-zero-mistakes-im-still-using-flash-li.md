---
title: I got Jev to zero mistakes. I'm still using Flash-Lite. - DEV Community
url: https://dev.to/theycallmeswift/i-got-jev-to-zero-mistakes-im-still-using-flash-lite-2mo7
site_name: devto
content_file: devto-i-got-jev-to-zero-mistakes-im-still-using-flash-li
fetched_at: '2026-10-09T17:19:20.906981'
original_url: https://dev.to/theycallmeswift/i-got-jev-to-zero-mistakes-im-still-using-flash-lite-2mo7
author: Swift
date: '2026-10-08'
description: Jev is a brilliant decision model. Gemini Flash-Lite is the model nobody talks about, and it’s fast,... Tagged with ai, gemini, testing, jev.
tags: '#ai, #gemini, #testing, #jev'
---

Jev is a brilliant decision model. Gemini Flash-Lite is the model nobody talks about, and it’s fast, accurate, and nearly free. Here's what we measured picking between them, and why the pair is the cheapest setup of all.

Jev is the most hyped model right now. TypeSafe's decision model doesn't chat and doesn't write. It reads some text and a list of options and returns calibrated probabilities over those options. A few hundred milliseconds, for almost nothing. Every feed I read has a post about it.

We had a real job for exactly that kind of model, already running in production on something much less fashionable. So instead of reading about Jev, we put it on our own data, ran both models a few thousand times, and kept score.

I love Jev. I'm still using Gemini Flash-Lite. Here's why.

This is the long version of a lightning talk I gave at AI Tinkerers NYC on October 7, 2026. The slides are onSpeaker Deck.

## The setup

A test that passes when the code is broken is worse than no test. With no test, you know you don't know. With a false green, you ship.

At Major League Hacking (MLH), we grade AI coding agents withbenchspec, an open-source eval runner we built for the job. You write what an agent should have done as plain-English checks in a markdown file. benchspec runs the agent in a sandbox and grades every check, with and without the skill under test, so the difference is what the skill actually teaches. After a run, the checks look like this:

- ./.meta/index.md exists
- Exactly six files match ./.meta/templates/*.md
- The summary faithfully reflects the three key facts from the source

Enter fullscreen mode

Exit fullscreen mode

Each check gets verified one of two ways.Cheap code: does this path exist, how many files match this glob, does this file have a line matching a pattern. Free, instant, exact. Or anLLM judgereads the content for meaning. That costs money every run.

A classifier, the router, reads each check and picks a checker (file_exists,glob_count,regex, a few more) or defers to the judge.

The router's job: one check in, one checker out, or a deferral.

The router's two mistakes aren't equal:

* Send something to the judge that code could have handled:you lose a few cents.
* Send something to code that code can't actually verify: a broken result reports green and nobody finds out. The person who trusted that green ships on it.We lose a user's trust.Cents come back. Trust doesn't.

So: when in doubt, defer.

## The secret

The router I actually run isGemini Flash-Lite, the smallest of Google's three Gemini tiers. Pro is the frontier model. Flash is the everyday one. Flash-Lite is the one Google itself describes as built for "high-volume, latency-sensitive tasks like translation and classification".

Flash-Lite has the same million-token context window as its bigger siblings, an answer in well under a second, and $0.30 per million input tokens. The current version, 3.5, shipped in July. It got a line in the release notes and no keynote. Nobody hypes it, but they should be.

99% of my monthly LLM calls go to Flash-Lite. That number comes from my own AI Studio usage page, across every project I have. Pro got nothing. Flash, almost nothing. And the calls are long in, short out: the shape of classification work.

Then Jev showed up. Text in, probabilities over a fixed set of options out, nothing written, by design. $0.042 per million input tokens, output free, a few hundred milliseconds. For a router, that's a perfect pitch.

## Round 1: the mistake you can't afford

The experiment is simple. Our router is a single call with one job: read a check, pick a checker or defer. We swapped Flash-Lite out of that slot, put Jev in, and ran the same checks through both. Each model got its own prompt and nothing else changed.

Here are eight real ones. ✓ is safe, ~ is over-cautious (deferred when code could have done it), ✗ is dangerous:

Jev made three dangerous(false positive)calls. Two checks need the content read for meaning, and Jev sent them toregex. A regex can find asource:line. It can't tell you whether that line names the right move. The third: "no.DS_Storeanywhere" is about the whole tree, and Jev picked a checker that looks at one path. It passes on a repo full of.DS_Storefiles.

Flash-Lite: zero false positives. Over-cautious twice, which costs cents(not trust!).

## Make No Mistakes

Jev reads literally. TypeSafe's own docs say it answers the question you wrote, not the one you meant. So I rewrote the question. I expected worked examples to do the heavy lifting, because that's what works for chat models. They didn't. What worked was one sentence:

Read quickly, it's the equivalent of writing "make no mistakes" when prompt-engineering. Here's why it isn't that, and why it worked on Jev specifically.

It's a test, not a plea."Be careful" gives the model nothing to do. "Imagine this checker passed. Could the check still be false?" is a procedure it can run once per option. Take "the log entry has asource:line naming the move". Imagineregexpasses. Asource:line exists. Could it still name the wrong move? Yes. Soregexis out. Take "no.DS_Storeanywhere". Imaginenot_file_existspasses on./.DS_Store. Could there still be one in a subfolder? Yes. Out. Every checker gets a mechanical answer, and the mechanical answer is the routing decision.

It asks about the checker's blind spot, not the check's shape.The original prompt asked "can this be verified mechanically?" That's a question about the check, andregexlooks mechanical. The rewrite asks "what does this checker fail to see?" That's a question about the tool. Same information, opposite direction. Jev answers exactly what you ask, so it gives a different answer.

The criteria changed to match.The old criteria described what a check should look like:regexis for "a named file has a line matching a stated pattern." The new ones describe what the checkermechanically does and cannot see:

Checker

Before

After

regex

The assertion says a named file has a line matching a stated pattern or literal prefix.

Tests whether one named file has a line matching a pattern. 
It cannot tell what the matched text means or refers to.

not_file_exists

The assertion says a single path is gone or never existed.

Tests one exact path for non-existence. 
It looks at that path and nowhere else.

skill_invoked

A bare activation line: skill X was invoked.

Tests whether the named skill was invoked. 
It sees nothing about what the skill did.

Examples made it worse.I folded our worked examples into Jev's original prompt and its dangerous checks doubled. Examples teach pattern-matching: "a line that says X" looks like theregexexamples, soregexit is. The test teaches the failure mode instead.

Checks that must go to the judge but were sent to code. Flash-Lite got to zero on Jev's weak prompt too.

With the rewrite, Jev went to zero on the eight, and on every check we have. Zero dangerous, zero wrong checkers, run after run. Tuned on half, zero on the half it never saw.

The one sentence fixed Jev. It didn't fix Flash-Lite. We wrote a fresh batch of whole-tree checks neither model had seen, like "nothing named draft.md exists in any subfolder".

Both models made false positive calls on them. With the rewrite, Jev went from 35 false positive runs to 0. Flash-Lite barely moved. The difference is how each one failed. Jev got the same checks wrong run after run: a blind spot. Flash-Lite got a check wrong about one run in five and right the other four: a flip. Jev obeys a precise criterion literally, so a better criterion fixes it. Flash-Lite forgives a sloppy criterion but doesn't fully obey a precise one. A blind spot is a prompt bug you fix. A flip is sampling noise you measure for.

## Does a smarter model mask a weak prompt?

If the prompt is the biggest variable, does a better model make it stop mattering? Same phrasings, Jev's bare prompt, three models.

Yes. Flash-Lite was still wrong about one run in five. Gemini 3.8 Flash and Opus 5.5 were never wrong. A stronger model masks a weaker prompt.

It doesn't make the prompt stop mattering. The same prompt change that fixed Jev pushed both bigger models toward deferring. It cut Opus's right answers by more than half and 3.8 Flash's to none. The prompt is still the single largest variable; the model decides how expensive your mistakes are. And the mask costs an order of magnitude more in both price and latency.

## Beyond our data

Our checks come from one project. So we ran the same experiment on a slice of theBerkeley Function Calling Leaderboard. The task: pick the right function and write its arguments, or say none fits. "None fits" is that benchmark's version of defer. Calling a function that doesn't fit is the dangerous direction.

The first thing we learned had nothing to do with either model. Flash-Lite kept calling a function on items the answer key said had none, and every time I marked it wrong.

After the fourth or fifth failure, I read the item. "Who won the World Series in 2020?" with one candidate function,get_champion(event, year). The function answers the question. The key said it didn't. So I checked every "none fits" item in our sample. Seven items matched. Flash-Lite had flagged all seven by disagreeing with the key. We score without them and list them in the repo. A cheap model with a real job found a bug in a public benchmark.

Jev's false-positive rate is at a 0.8 probability bar: call the function only if Jev is at least 80% sure.

Neither model is at zero. With its top label, Jev called a function on about one in thirteen items where nothing fit. Flash-Lite, about one in twenty-five. But Jev has a knob. Raise the bar to 0.8 and its false positives drop to 1%, at the price of deferring twice as often. Flash-Lite has no knob, but it writes the arguments, and gets them fully right over nine times in ten.

The third card, Jev + Flash-Lite, gets Jev's false-positive rate and Flash-Lite's arguments for well under half the one-call price. That combination is where this ends up, so the rest of the post is about it.

## The call you don't need

Take the_Last updatedcheck. Jev returnsregexwith a probability distribution. And stops. Which file? What pattern? That takes a second model. Flash-Lite, one call, returns the label, the arguments, and a reason, because it can write.

Measured, billed through OpenRouter. Time is mean milliseconds; cost is per 1,000 checks.

Now look at the fourth row:Jev → Flash-Lite, $0.10.Cheaper than Flash-Lite on its own, at $0.52. How does adding a model make it five times cheaper?

## How Jev + Flash-Lite saves the money

Nothing clever. Two multipliers, both on Flash-Lite's bill.

1. The second call only runs when there's something to write.A check that goes to the judge has no arguments. Jev defers it and Flash-Lite never sees it. On our full set that's most checks: fewer than four in ten have anything for Flash-Lite to do.

2. The second call uses a shorter prompt.The one-call prompt is long, with worked examples, because that's what keeps Flash-Lite safe on the routing decision. And it goes out on every check. In the pair, Jev has already made the routing decision. The second prompt only has to say: here's the check, here's the checker that was chosen, write its arguments. That's about a seventh of the tokens.

An eval assertion has already been routed to a deterministic checker. Write that checker's arguments.

Assertion: {check}
Checker already chosen: {label}

Arguments needed per checker:
- file_exists / not_file_exists: "path"
- glob_count: "glob" and "count"
- regex: "path" and "pattern"
...
Reply with one JSON object holding only the arguments and nothing else.

Enter fullscreen mode

Exit fullscreen mode

Jev itself costs about three cents per thousand checks. Rounding error.

Blue is Flash-Lite input, yellow is Flash-Lite output, coral is Jev.

Put the multipliers together: a call on about half the checks, with a prompt a seventh the size, plus a near-free first hop. Measured, $0.52 becomes $0.10 per 1,000. On the production mix it'd be lower still.

The same thing happens on public data. On BFCL the pair costs less than half of one Flash-Lite call. The second hop runs on about half the items and reads one function's schema instead of every candidate's.

What you pay for it: one more round trip, about a quarter of a second on average. And you inherit Jev's routing, not Flash-Lite's. On BFCL that means Jev's false-positive rate and Jev's knob.

## The takeaways

1. Flash-Lite is Google's best-kept secret.For most classification work it's the right balance of fast and cheap. It's smart enough to forgive a sloppy prompt and to generate. It gave us zero dangerous calls on Jev's bare prompt and wrote the label and the arguments in one call.
2. Prompts are your single biggest variable.One sentence took Jev from 35 dangerous runs to 0, and examples made it worse. Smarter models soften the problem. They don't remove it: the same prompt change still pushed Opus from mostly answering to mostly deferring.
3. Private evals separate real from hype.We didn't have to take anyone's word for Jev, including TypeSafe's. We had real checks from a real product. So we ran the hyped model against the one we already use and found out. What's true: fast, cheap, zero once you ask the right question. What isn't: examples help, a smarter model makes prompting irrelevant. What nobody was saying: the cheapest setup is both of them.

To go deeper, start with thepractical getting-started guide to Jev. Google'sGemini 3.6 Flash & 3.5 Flash-Lite developer guidecovers the model.

Happy Hacking!

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
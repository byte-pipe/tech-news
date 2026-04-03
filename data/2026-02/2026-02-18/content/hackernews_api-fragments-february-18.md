---
title: 'Fragments: February 18'
url: https://martinfowler.com/fragments/2026-02-18.html
site_name: hackernews_api
content_file: hackernews_api-fragments-february-18
fetched_at: '2026-02-18T19:23:45.138963'
original_url: https://martinfowler.com/fragments/2026-02-18.html
author: nthypes
date: '2026-02-18'
description: The Future of AI Software Development
tags:
- hackernews
- trending
---

# Fragments: February 18

Martin Fowler: 18 Feb 2026

I’ll start with some more tidbits from theThoughtworks Future of Software Development Retreat

❄                ❄

We were tired after the event, but our marketing folks forced Rachel Laycock and I to do a quick video. We’re often asked if this event was about creating some kind of new manifesto for AI-enabled development, akin to the Agile Manifesto (which is now 25 years old). In short, our answer is “no”, but for the full answer,watch our video

❄                ❄

My colleagues put together adetailed summary of thoughtsfrom the event, in a 17 page PDF. It breaks the discussion down into eight major themes, including “Where does the rigor go?”, “The middle loop: a new category of work”, “Technical foundations: languages, semantics and
operating systems”, and “The human side: roles, skills and experience”.

The retreat surfaced a consistent pattern: the practices, tools and organizational structures built for human-only software development are breaking in predictable ways under the weight of AI-assisted work. The replacements are forming, but they are not yet mature.

The ideas ready for broader industry conversation include the supervisory engineering middle loop, risk tiering as the new core engineering discipline, TDD as the strongest form of prompt engineering and the agent experience reframe for developer experience investment.

❄                ❄

Annie Vellaposted her take-awaysfrom the event

I walked into that room expecting to learn from people who were further ahead. People who’d cracked the code on how to adopt AI at scale, how to restructure teams around it, how to make it work. Some of the sharpest minds in the software industry were sitting around those tables.

And nobody has it all figured out.

There is more uncertainty than certainty. About how to use AI well, what it’s really doing to productivity, how roles are shifting, what the impact will be, how things will evolve. Everyone is working it out as they go.

I actually found that to be quite comforting, in many ways. Yes, we walked away with more questions than answers, but at least we now have a shared understanding of the sorts of questions we should be asking. That might be the most valuable outcome of all.

❄                ❄

Rachel Laycock wasinterviewed in The New Stack(by Jennifer Riggins) about her recollections from the retreat.

AI may be dubbed the great disruptor, but it’s really just an accelerator of whatever you already have. The 2025 DORA report places AI’s primary role in software development as that of an amplifier — a funhouse mirror that reflects back the good, bad, and ugly of your whole pipeline. AI is proven to be impactful on the individual developer’s work and on the speed of writing code. But, since writing code was never the bottleneck, if traditional software delivery best practices aren’t already in place, this velocity multiplier becomes a debt accelerator.

❄                ❄

LLMs are eating specialty skills. There will be less use of specialist front-end and back-end developers as the LLM-driving skills become more important than the details of platform usage. Will this lead to a greater recognition of the role ofExpert Generalists? Or will the ability of LLMs to write lots of code mean they code around the silos rather than eliminating them? Will LLMs be able to ingest the code from many silos to understand how work crosses the boundaries?

❄                ❄

Will LLMs be cheaper than humans once the subsidies for tokens go away? At this point we have little visibility to what the true cost of tokens is now, let alone what it will be in a few years time. It could be so cheap that we don’t care how many tokens we send to LLMs, or it could be high enough that we have to be very careful.

❄                ❄

Will the rise of specifications bring us back towaterfall-style development? The natural impulse of many business folks is “don’t bother me until it’s finished”. Does the process of evolutionary design get helped or hindered by LLMs?

My instinctive reaction is that all depends on our workflow. I don’t think LLMs change the value of rapidly building and releasing small slices of capability. The promise of LLMs is to increase the frequency of that cycle, and doing more in each release.

❄                ❄

Sadly the session on security had a small turnout.

One large enterprise employee commented that they were deliberately slow with AI tech, keeping about a quarter behind the leading edge. “We’re not in the business of avoiding all risks, but we do need to manage them”.

Security is tedious, people naturally want to first make things work, then make them reliable, and only then make them secure. Platforms play an important role here, make it easy to deploy AI with good security. Are the AI vendors being irresponsible by not taking this seriously enough? I think of how other engineering disciplines bake a significant safety factor into their designs. Are we doing that, and if not will our failure lead to more damage than a falling bridge?

There was a general feeling that platform thinking is essential here. Platform teams need to create a fast but safe path - “bullet trains” for those using AI in applications building.

❄                ❄

One of my favorite things about the event was some meta-stuff. While many of the participants were very familiar with theOpen Spaceformat, it was the first time for a few. It’s always fun to see how people quickly realize how this style of (un)conference leads to wide-ranging yet deep discussions. I hope we made a few more open space fans.

One participant commented how they really appreciated how the sessions had so much deep and respectful dialog. There wasn’t the interruptions and a few people gobbling up airtime that they’d seen around so much of the tech world. Another attendee, commented “it was great that while I was here I didn’t have to feel I was a woman, I could just be one of the participants”. One of the lovely things about Thoughtworks is that I’ve got used to that sense of camaraderie, and it can be a sad shock when I go outside the bubble.

❄                ❄                ❄                ❄                ❄

I’ve learned much over the years from Stephen O’Grady’s analysis of the software industry. He’s written about how much of the profession feelsbesiegedby AI.

these tools are, or can be, powerful accelerants and enablers for people that dramatically lower the barriers to software development. They have the ability to democratize access to skills that used to be very difficult, or even possible for some, to acquire. Even a legend of the industry like Grady Booch, who has been appropriately dismissive of AGI claims and is actively disdainful of AI slop posted recently that he was “gobsmacked” by Claude’s abilities. Booch’s advice to developers alarmed by AI on Oxide’s podcast last week? “Be calm” and “take a deep breath.” From his perspective, having watched and shaped the evolution of the technology first hand over a period of decades, AI is just another step in the industry’s long history of abstractions, and one that will open new doors for the industry.

…whether one wants those doors opened or not ultimately is irrelevant. AI isn’t going away any more than the automated loom, steam engines or nuclear reactors did. For better or for worse, the technology is here for good. What’s left to decide is how we best maximize its benefits while mitigating its costs.

❄                ❄                ❄                ❄                ❄

Adam Tornhill shares some more of his company’s research on code health and its impact on agentic development.

The study Code for Machines, Not Just Humans defines “AI-friendliness” as the probability that AI-generated refactorings preserve behavior and improve maintainability. It’s a large-scale study of 5,000 real programs using six different LLMs to refactor code while keeping all tests passing.

They found that LLMs performed consistently better in healthy code bases. The risk of defects was 30% higher in less-healthy code. And a limitation of the study was that the less-healthy code wasn’t anywhere near as bad as much legacy code is.

What would the AI error rate be on such code? Based on patterns observed across all Code Health research, the relationship is almost certainly non-linear.

❄                ❄                ❄                ❄                ❄

In a conversation with one heavy user of LLM coding agents:

Thank you for all your advocacy of TDD (Test-Driven Development). TDD has been essential for us to use LLMs effectively

I worry about confirmation bias here, but I am hearing from folks on the leading edge of LLM usage about the value of clear tests, and the TDD cycle. It certainly strikes me as a key tool in driving LLMs effectively.

---
title: Everybody's Lost Their Minds
url: https://www.netmeister.org/blog/everybodys-lost-their-minds.html
site_name: hackernews_api
content_file: hackernews_api-everybodys-lost-their-minds
fetched_at: '2026-09-17T21:56:20.698412'
original_url: https://www.netmeister.org/blog/everybodys-lost-their-minds.html
author: ibobev
date: '2026-09-17'
tags:
- hackernews
- trending
---

# Signs of Triviality

Opinions, mostly my own, on the importance of being and other things.

 [
homepage
] 
 [
blog
] 
 [
jschauma@netmeister.org
] 
 [
@jschauma
] 
 [
RSS
]
 

## Everybody's Lost Their Minds

September 16th, 2026

Men. Some would rather vomit up a rambling blog post
 wall of text that nobody's going to read than go to
 therapy. So here we are.

I've seen my share of stupid over the years, but now
 people with no engineering background have started
 pitching "industry changing" solutions they cooked up
 in their agent infested homelab; people's emails
 read like bozotic LinkedIn-fluencer posts with punchy
 "it's not this, it's that" single-sentence
 paragraphs; online articles suffer a similar fate in
 their own convergence on Meh; and half of the people
 you interact with have turned intomeat proxies.

Spending upwards of 75% of my time directly or
 indirectly dealing with AI every day has absolutely
 robbed me of most of my enjoyment of my work. Most
 days feel like that Twilight Zone where you wake up
 and you're the same, but everyone else is different.
 (They were all
 like that.)

### "Ethics aside..."

The cyber hype train has been going "choo choo" for a
 while, with the main AI companies trying to one-up
 each othercommitting
 crimesand somehow we let them; the conscious
 choice of anthropomorphic language by the companies is
 adapted unquestioned by the media, thereby absolving
 AI companies of their incompetence to secure their
 programs.

Built on unapologetic exploitation of intellectual
 property and concentrating power in the hands of a
 very small number of US companies and oligarchs, these
 AI models not only lend themselves togeneration
 of Child Sexual Abuse Material—a productfeatureforlogged-in
 users—1but our continued use of
 them also directly supports their role in, e.g.,
 military target selection, such aselementary
 schools.

Meanwhile, every single company is happy to "ethics
 aside..." all of that and spend unimaginable amounts
 of "tokens"—a made-up currency following the
 casino model2—while staring at you
 blankly when you ask whether anybody has bothered to
 check if that support chatbot you vibe coded and which
 you fed all of your very mediocre at best
 "documentation" hasanyROI.3

### Project Sisyphus

"Frontier Models" and AI-assisted vulnerability
 research is another topic with questionable results.
 Anthropic and OpenAI tried to one-up each other with
 how dangerous their models are and everybody who
 considers themselves an industry leader is now part of
 some mysteriously named "project" (likeGlasswingandDaybreak, orAthenaandAkrites) or
 co-signed various open letters (likethisorthis)
 to signal just how much they're totally not left out.

Every participant in these project has thrown
 absolutely incredible amounts of engineering resources
 at the FOMO-induced, time-limited, "the first one's
 free" offer from Anthropic and OpenAI. Dozens of
 highly-paid security engineers had all of their
 priorities shifted and spentall of their
 timeon this; the cost of the engineering hours
 spent on developing and adjusting AI vulnerability
 discovery harnesses, building new processes and
 pipelines to shoehorn thousands of findings into their
 vulnerability management processes, and of course
 working with the product owners on assessing and
 fixing the findings... all that must run in the many,
 many millions of dollars for each organization.

And yet, despite having found literallythousandsof new vulnerabilities (onlya
 fraction of which were reported to Open Source
 projects, by the way), I don't think that we're
 any safer than before. That's becausefindingvulnerabilities has never been the
 bottleneck in information security. The bottleneck
 isn't evenverifyinga vulnerability report
 and validating its severity, as time consuming as that
 is. The bottleneck isn't determining the fix,
 creating the patch, or publishing a new release. The
 bottleneck is still, as ever before,getting the
 goddamn packages updated. Patching is stillhard.

Now imagine that we had spent all these resources on
 doing the basics: ensuring your organization has an
 up-to-date and comprehensive asset inventory with
 fine-grained package listings; building infrastructure
 that supports regular, frequent, and automated OS and
 applіcation updates; automatically rebooting systems
 when they hit, say, 30 days of uptime to ensure these
 updates are picked up; establishing comprehensive
 attack surface enumeration across all your IP spaceas well asall your cloud providers (what a
 concept!); the list of basic, fundamental defenses
 that nobody seems to actually do well goes on. Having
 a few dozen senior engineers dedicated for 6 months to
 overhauling all that, focusing on makingpatchingeasier, would, in my book, have been
 a much better investment, but that's just not very
 cyber at all.

No matter what AI promises, human resources are still
 a zero-sum game, and every individual feeling super
 busy in their agentic silo doing a thousand things at
 once does not, in the end, help solve the kinds of
 projects that require cross-functional collaboration
 and team work.

### A strange game

At the same time, AI companies are falling over
 themselves once again facetiously calling for their
 own regulation because, you know, they could
 accidentally end all mankind.

If you actually thought your product will kill all
 humans, then you could, you know, like, just stop
 building the torment nexus. All by yourself, no
 government regulations required. Nobody's forcing you
 to play "Theaterwide Biotoxic and Chemical Warfare" or
 "Global Thermonuclear War". I mean, except your
 future shareholders and your greed. Alas, that
 wouldn't cockblock your competition...

But you don't need to imagine AI destroying all
 humankind within the next few years via some sort of
 Skynet or Paperclip Maximizer scenario when in reality
 AI has of course already been hard
 at work here. The environmental impact of these
 companies isstaggering.
 The AI race demands more and more water wasting, air
 polluting, fossil fuel powered data centers that
 absolutely nobody wants to live close to, and
 governments lift any and all environmental regulations
 for these companies who not too long ago at leastpretendedto have even the feeblest
 greenwashing commitments to carbon neutrality or
 renewable energy sources.

But "the
 world looks different now", to which I can only say
 "No fucking shit, Sherlock.IT'S
 ON FUCKING FIRE.Because ofyou."

### Superhuman Intelligence

You know there are two ways for AI to achieve
 superhuman intelligence, right? One (theoretical) way
 is the mystical "recursive self-improvement" by AI.
 The other one is the path we're very clearly on: The
 agentic brain worms have been spreading, and it looks
 increasingly like everybody's lost their goddamn minds
 already. AI is the tool that dulls its users; it
 incrementally replacesunderstandingwith a
 new dependency and addiction as you actively de-skill
 yourself.

AI helps people find more vulnerabilities in existing
 code. To address those vulnerabilities, people use AI
 to generate patches. The resulting pull requests are
 then "reviewed" by AI. That is, the more AI is in the
 loop, the less we understand the code base. The
 mystical "human in the loop" often is nothing more
 than arubber
 stamp.

So what happens when things go bump? Complex systems
 fail in complex ways, and debugging code is an order
 of magnitudeharder
 than writing code. Debugging somebody else's code
 is harder still. Trying to debug large, complex,
 distributed systems consisting of components that are
 effectively opaque to your entire organization is
 going to be impossible.

So no, I'm not going to set ethics aside and then
 actively offer myself up as tribute to self-amputate
 my brain. I'm sorry if everybody else can't get rid
 of the brain slugs, but at this point I'm just looking
 to get off this ride.

September 16th, 2026

P.S.: And no, Claude isnot
 conscious. J-Space my ass.

Footnotes:

[1] Damn straight I use an emdash. Fuck
 you for devaluing it.↩

[2] "Results showed that participants
 gambled significantly more with chips than with real
 cash." [citation provided]↩

[3] It doesnt: LLMs are Garbage-In/Garbage-Out—if
 you have shitty docs, the AI can at best polish that
 turd and still only spit out nothing of use.↩

Links:

* Patching is hard. Knowing what to patch is harder still
* Discussion on HackerNews(dupe)
* Discussion on Lobsters

 ← [
Sites using PQC (September 2026)
]

 [
homepage
] 
 [
blog
] 
 [
jschauma@netmeister.org
] 
 [
@jschauma
] 
 [
RSS
]
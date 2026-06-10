---
title: Anthropic says these topics are too dangerous to let its Fable 5 model talk about - Ars Technica
url: https://arstechnica.com/ai/2026/06/anthropic-says-these-topics-are-too-dangerous-to-let-its-fable-5-model-talk-about/
site_name: newsfeed
content_file: newsfeed-anthropic-says-these-topics-are-too-dangerous-to-l
fetched_at: '2026-06-11T06:00:40.502384'
original_url: https://arstechnica.com/ai/2026/06/anthropic-says-these-topics-are-too-dangerous-to-let-its-fable-5-model-talk-about/
date: '2026-06-09'
published_date: '2026-06-09T19:20:25+00:00'
description: New frontier model refuses cybersecurity, biology, and chemistry queries.
tags:
- ars-technica
- ai
- anthropic
- fable
---

Text
 settings

Anthropic Tuesdaypublicly released Claude Fable 5, its first “Mythos-class” model that it says surpasses its previous frontier Opus models in overall capabilities. But the model’s launch today comes with safeguards designed to prevent it from answering queries on topics like cybersecurity, biology, and chemistry, where the company haspublicly worried about its potential impactto “uplift” malicious actors.

Anthropic says Fable 5 operates on the “same underlying model” as Mythos 5, which is coming out ofits monthslong “Mythos Preview” periodtoday, but only for “a small group of cyberdefenders” judged trustworthy through theexisting Project Glasswing. Unlike Mythos 5, though, the publicly accessible Fable 5 is designed to funnel queries on certain sensitive topics to the earlier Claude Opus 4.8 model and to warn the user when this is happening.

 Among the many claimed benchmark improvements for Fable 5, the one related to cybersecurity was a particularly large jump.
 

 Credit:
 
Anthropic

 Among the many claimed benchmark improvements for Fable 5, the one related to cybersecurity was a particularly large jump.

 

 Credit:

 

 
 Anthropic

 

Anthropic said it has tuned these safeguards to be “stricter than ideal,” meaning the system may occasionally refuse “harmless requests” in a way that it acknowledges may be frustrating for regular users. But Anthropic says such false positives come up in less than five percent of all sessions in testing, and were worth it to avoid situations where Mythos could give malicious actors assistance in “causing serious harm that they couldn’t have received from other sources.”

## I can’t let you do that, Dave

Fable 5’s topic-based safeguards are built arounda system of classifiersdesigned to broadly detect banned prompt subjects as well as any potential jailbreak attempts. In over 1,000 hours of red-team testing with a bug bounty program, Anthropic says external teams failed to find any universal jailbreaks for Fable 5. The new model also resisted automated jailbreak attempts to a much larger degree than previous Claude Opus models, Anthropic said.

The company said it is particularly worried about Mythos 5’s ability to perform “agentic hacking,” executing multi-part cyberattacks with much more facility than earlier models. But testing from the UK’s AI Security Institute in recent months found that Mythos Previewperformed similarly to OpenAI’s GPT-5.5on a suite of Capture the Flag challenges, suggesting Mythos’ performance is not “a breakthrough specific to one model.”

 Anthropic says Fable 5 has much more robust defenses against automated and red-teamed jailbreak tests.
 

 Credit:
 
Anthropic

 Anthropic says Fable 5 has much more robust defenses against automated and red-teamed jailbreak tests.

 

 Credit:

 

 
 Anthropic

 

Among the usual raft of fair-to-middling benchmark test improvements that Anthropic reports for Mythos 5 over previous frontier models, the company claims a significant jump in the model’s capabilities onthe cybersecurity-focused ExploitBench test. Mythos 5 scored a 78 percent on the benchmark’s tests of vulnerable code exploits, a significant increase from the 40 percent score from Opus 4.8, and even the 69 percent score achieved by Mythos Preview.

While earlier Anthropic models blocked bioweapons-related queries, that classifier now applies toallchemistry and biology-related queries in Fable 5. The company says it worries that “well-resourced malicious actors” could use even seemingly benign queries on these subjects to assist with “highly risky biological research” in a much more effective way than with previous models.

## Who can you trust?

Anthropic seems to understand that making certain topics off-limits for Fable 5 is something of a double-edged sword. The company writes that “the same queries that are beneficial in the hands of cybersecurity professionals and biology researchers could be dangerous if available to malicious actors.”

That puts Anthropic in the somewhat awkward position of having to judge who is and is not trustworthy enough to have access to a model that it says has potentially dangerous capabilities. The company says it will be periodically expanding its existing Project Glasswing program “in consultation with the US government” to let in more cybersecurity professionals. That expansion will also include a new trusted access program for life sciences organizations that removes Fable 5’s biology/chemistry safeguards while keeping cybersecurity safeguards in place.

API and Enterprise users will be able to access the Fable 5 model at a cost of $10-per-million input tokens and $50-per-million output tokens starting today. Those prices are 67 to 100 percent higher thanthose for OpenAI’s recent GPT-5.5, a difference that could be significant at a time when many users arebalking at the high cost of frontier models.

Anthropic’s existing subscription plans will include access to Fable 5 through June 22, after which users will need to purchase “usage credits” to access the new model. Anthropic says it eventually hopes to restore Fable 5 access as a standard part of subscription plans once it has “sufficient capacity” to do so.

 Kyle Orland
 

Senior Gaming Editor

 Kyle Orland
 

Senior Gaming Editor

 Kyle Orland has been the Senior Gaming Editor at Ars Technica since 2012, writing primarily about the business, tech, and culture behind video games. He has journalism and computer science degrees from University of Maryland. He once 
wrote a whole book about 
Minesweeper
.
 

1. 1.Starlink charges $10 monthly hardware fee in move away from one-time purchases
2. 2.First Drive: The 2027 Rivian R2 entirely changes the EV game
3. 3.Commonwealth Fusion makes the physics case for its 400 MW reactor
4. 4.US military claims first drone boat rescue of downed helicopter crew
5. 5.High-severity vulnerability in Linux caused by a single faulty character

Customize
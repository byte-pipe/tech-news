---
title: GPT-5 Thinking in ChatGPT (aka Research Goblin) is shockingly good at search
url: https://simonwillison.net/2025/Sep/6/research-goblin/
site_name: hackernews
fetched_at: '2025-09-08T11:06:04.614998'
original_url: https://simonwillison.net/2025/Sep/6/research-goblin/
author: Simon Willison
date: '2025-09-08'
---

# Simon Willison’s Weblog

Subscribe

## GPT-5 Thinking in ChatGPT (aka Research Goblin) is shockingly good at search

6th September 2025

“Don’t use chatbots as search engines” was great advice for several years... until it wasn’t.

I wrote about how good OpenAI’s o3 was at using its Bing-backed search toolback in April. GPT-5 feels even better.

I’ve started calling it myResearch Goblin. I can assign a task to it, no matter how trivial or complex, and it will do an often unreasonable amount of work to search the internet and figure out an answer.

This is excellent for satisfying curiosity, and occasionally useful for more important endeavors as well.

I always run my searches by selecting the “GPT-5 Thinking” model from the model picker—in my experience this leads to far more comprehensive (albeit much slower) results.

Here are some examples from just the last couple of days. Every single one of them was run on my phone, usually while I was doing something else. Most of them were dictated using the iPhone voice keyboard, which I find faster than typing. Plus, it’s fun to talk to my Research Goblin.

* Bouncy travelators
* Identify this building
* Starbucks UK cake pops
* Britannica to seed Wikipedia
* Official name for the University of Cambridge
* History of the caverns in Exeter quay
* Aldi vs Lidl
* AI labs scanning books for training data
* GPT-5 for search feels competent
* Tips for using search in ChatGPT

#### Bouncy travelators

They used to be rubber bouncy travelators at Heathrow and they were really fun, have all been replaced by metal ones now and if so, when did that happen?

I was traveling through Heathrow airport pondering what had happened to the fun bouncy rubber travelators.

Here’s what I got. Research Goblin narrowed it down to some time between 2014-2018 but, more importantly, found me thisdelightful 2024 articleby Peter Hartlaub in the San Francisco Chronicle with a history of the SFO bouncy walkways, now also sadly retired.

#### Identify this building

Identify this building in reading

This is a photo I snapped out of the window on the train. Itthought for 1m4sand correctly identified it asThe Blade.

## Starbucks UK cake pops

Starbucks in the UK don’t sell cake pops! Do a deep investigative dive

The Starbucks in Exeter railway station didn’t have cake pops, and the lady I asked didn’t know what they were.

Here’s the result. It turns out Starbucks did launch cake pops in the UKin September 2023but they aren’t available at all outlets, in particular the licensed travel locations such as the one at Exeter St Davids station.

I particularly enjoyed how it established definitive proof by consultingthe nutrition and allergen guide PDFon starbucks.co.uk, which does indeed list both the Birthday Cake Pop (my favourite) and the Cookies and Cream one (apparently discontinued in the USA, at leastaccording to r/starbucks).

#### Britannica to seed Wikipedia

Someone on hacker News said:

> I was looking at another thread about how Wikipedia was the best thing on the internet. But they only got the head start by taking copy of Encyclopedia Britannica and everything else

Find what they meant by that

The result. It turns out Wikipedia did seed itself with content from the out-of-copyright 1911 Encyclopædia Britannica... but that project took place in 2006, five years after Wikipedia first launched in 2001.

I asked:

What is the single best article I can link somebody to that explains the 1911 Britannica thing

And it pointed me toWikipedia:WikiProject Encyclopaedia Britannicawhich includes a detailed explanation and a link tothe 13,000 pagesstill tagged with the template from that project. I posted what I foundin a comment.

Notably (for me anyway) I didn’t feel the need to disclose my use of ChatGPT in finding that information—at this point that feels a little like disclosing that I ran a Google search.

#### Official name for the University of Cambridge

What is the official legal name of the university of Cambridge?

Here’s the context for that one. It thought for 19 seconds—the thinking trace reveals it knew the answer but wanted to confirm it.It answered:

“The Chancellor, Masters, and Scholars of the University of Cambridge.”University of Cambridge,Cambridge University Press & Assessment

That first link gave me the citation I needed in order to be sure this was right.

Since this is my shortest example, here’s a screenshot of the expanded “Thought for 19s” panel. Ialwaysexpand the thoughts—seeing how it pulled together its answer is crucial for evaluating if the answer is likely to be useful or not.

#### History of the caverns in Exeter quay

Research On the waterfront restaurant in Exeter, is it dug into the cliffs somehow? History of the building, who built it, why and how

We were out to dinnerhereand noticed that the interior of the restaurant appeared to be a space dug into the cliff, which piqued my interest.

This wasthe ChatGPT sessionthat inspired the Research Goblin nickname. It just kept on digging!

The first reply took 2m40s and confirmed that yes, these quay buildings were carved into the red sandstone cliffin the 1820s-1830s.

ChatGPT with GPT-5 really likes to suggest additional steps it can take. In this case:

If you’d like, I can dig up the exact Historic England entry that covers the “Southern Warehouse” address and overlay it on a map of the vaults.

I often say “yes” purely out of curiosity to see what it will do next, and the offer to “overlay it on a map” was irresistible, like how would it even do that?

It did atonof extra searches, found latitude and longitude coordinates for the restaurant (from Wikimedia Commons) and the warehouse buildings (from National Heritage List for England via Wikipedia), showed me that data in a table and then used Python to render this image:

Yeah, so that one is a bit of a miss!

But... the underlying research chain, as always, provided fascinating. I noticed that at one point it had searched for “Exeter Quay vaults map PDF”, which inspired my next question:

Did you find any PDF diagrams, showing the tunnels into the cliff

2m20s later it had founda planning documentanda letting brochure, both PDFs, but noted that neither of them had the diagram I wanted. Evidently it actually “reads” the PDFs it finds as part of its activities, since it appears to have knowledge of the images contained within them as well as the text.

It concluded with this intriguing note:

There’s strong evidence that a detailed plan/sectiondoesexist in the Exeter Archaeology report often cited by planners—“Archaeological, Historical and Conservation Study of the Exeter Canal Basin” (Exeter Archaeology Report 00.18, 2000)—but it isn’t online; it’s just cited in planning documents. You’d likely need to request it via the Devon Heritage Centre/Historic Environment Record.

If you want, I can keep hunting specialist archives for a digitized copy or a different report that includes the vault layouts.

Obviously I said “Yes do that” and 2m24s later it chucked out a whole host of extra links, an apology that it still hadn’t found a detailed plan diagram and, under the section heading “What I recommend next (actionable + exact ask)”:

If you’re happy, I can draft an email you can paste to the right archivists. [...]

Subject: Exeter Quayside cliff vaults – request for plan/section drawings
Hello,

I’m researching the cliff-cut vaults behind The Quay (On The Waterfront / Kings Wharf).
Could you supply scans or copies of anyplans/sections/diagramsof these vaults—especially those inExeter Archaeology Report 00.18 (2000)(Archaeological, Historical and Conservation Study of the Exeter Canal Basin) and anyEMAFU/Exeter Archaeology drawingsfor “The Quay” showing thevault/tunnel layouts cut into the red sandstone cliff?

For reference: NHLE list entries1223045 (1–4 Warehouse Vaults), 1223046 (6–11 Warehouse Vaults), and1223114 (14–25 Vaults).

Many thanks!

It’s a good thing my Research Goblin doesn’t have the ability to send email (which we already know isvery risky business) or at this point I wouldn’t be surprised if it started autonomously bothering archivists on my behalf!

#### Aldi vs Lidl

In UK supermarket terms compare lidl and aldi

I saw an Aldi and a Lidl next to each other in Exeter and was curious as to how they compare. In this case my Research Goblin wentwaydeeper than I had intended, thinking for 1m25s about market share and price surveys and loyalty schemes andansweringwith ten paragraphs of detailed analysis.

I replied:

Yeah, I just wanted the basic vibes like is one fancier than the other?

It thought for 6 seconds, didn’t run any additional searches and replied:

Short version: neither is “fancy” — both are no-frills discounters — butLidl often feels a touch more polished, whileAldi feels a touch more bare-bones. [...]

Since I was now enjoying having my Goblin express judgement over British supermarket chains I said:

How do they rate in fancinews compared to all of the other major UK supermarket chains?

(That was a typo for “fanciness” which it figured out.)

It thought for another 1m1s, ran 7 searches, consulted 27 URLs and gave me back a ranking that looked about right to me.

#### AI labs scanning books for training data

Anthropic bought lots of physical books and cut them up and scan them for training data. Do any other AI labs do the same thing?

Relevant totoday’s big story. Research Goblin wasunable to findany news stories or other evidence that any labs other than Anthropic are engaged in large scale book scanning for training data. That’s not to say it isn’t happening, but it’s happening very quietly if that’s the case.

#### GPT-5 for search feels competent

The word that best describes how I feel about GPT-5 search is that it feelscompetent.

I’ve thrown all sorts of things at it over the last few weeks and it rarely disappoints me. It almost always does better than if I were to dedicate the same amount of time to manually searching myself, mainly because it’s much faster at running searches and evaluating the results than I am.

I particularly love that it works so well on mobile. I used to reserve my deeper research sessions to a laptop where I could open up dozens of tabs. I’ll still do that for higher stakes activities but I’m finding the scope of curiosity satisfaction I can perform on the go with just my phone has increased quite dramatically.

I’ve mostly stopped using OpenAI’s Deep Research feature, because ChatGPT search now gives me the results I’m interested in far more quickly for most queries.

As a developer who builds software on LLMs I see ChatGPT search as the gold standard for what can be achieved using tool calling combined with chain-of-thought. Techniques like RAG aremassivelymore effective if you can reframe them as several levels of tool calling with a carefully selected set of powerful search tools.

The way that search tool integrates with reasoning is key, because it allows GPT-5 to execute a search, reason about the results and then execute follow-up searches—all as part of that initial “thinking” process.

Anthropic call this abilityinterleaved thinkingand it’s alsosupported by the OpenAI Responses API.

#### Tips for using search in ChatGPT

As with all things AI, GPT-5 search rewards intuition gathered through experience. Any time a curious thought pops into my head I try to catch it and throw it at my Research Goblin. If it’s something I’m certain it won’t be able to handle then even better! I can learn from watching it fail.

I’ve been trying out hints like “go deep” which seem to trigger a more thorough research job. I enjoy throwing those at shallow and unimportant questions like the UK Starbucks cake pops one just to see what happens!

You can throw questions at it which have a single, unambiguous answer—but I think questions which are broader and don’t have a “correct” answer can be a lot more fun. The UK supermarket rankings above are a great example of that.

Since I love a questionable analogy for LLMs Research Goblin is... well, it’s a goblin. It’s very industrious, not quite human and not entirely trustworthy. You have to be able to outwit it if you want to keep it gainfully employed.

Posted
6th September 2025
 at 7:31 pm · Follow me on
Mastodon
,
Bluesky
,
Twitter
 or
subscribe to my newsletter

## More recent articles

* V&A East Storehouse and Operation Mincemeat in London- 27th August 2025
* The Summer of Johann: prompt injections as far as the eye can see- 15th August 2025



This isGPT-5 Thinking in ChatGPT (aka Research Goblin) is shockingly good at searchby Simon Willison, posted on6th September 2025.

Part of seriesGPT-5

1. GPT-5: Key characteristics, pricing and model card- Aug. 7, 2025, 5:36 p.m.
2. The surprise deprecation of GPT-4o for ChatGPT consumers- Aug. 8, 2025, 5:52 p.m.
3. GPT-5 Thinking in ChatGPT (aka Research Goblin) is shockingly good at search- Sept. 6, 2025, 7:31 p.m.

 bing

29

 search

93

 ai

1550

 openai

342

 generative-ai

1359

 llms

1330

 llm-tool-use

56

 llm-reasoning

70

 ai-assisted-search

31

 gpt-5

12

Previous:V&A East Storehouse and Operation Mincemeat in London

### Monthly briefing

Sponsor me for$10/monthand get a curated email digest of the month's most important LLM developments.

Pay me to send you less!

 Sponsor & subscribe






* Colophon
* ©
* 2002
* 2003
* 2004
* 2005
* 2006
* 2007
* 2008
* 2009
* 2010
* 2011
* 2012
* 2013
* 2014
* 2015
* 2016
* 2017
* 2018
* 2019
* 2020
* 2021
* 2022
* 2023
* 2024
* 2025

---
title: Gemini 3.0 Spotted in the Wild Through A/B Testing | Rick Lamers' blog
url: https://ricklamers.io/posts/gemini-3-spotted-in-the-wild/
site_name: hackernews
fetched_at: '2025-10-17T11:08:16.680096'
original_url: https://ricklamers.io/posts/gemini-3-spotted-in-the-wild/
author: Rick Lamers
date: '2025-10-17'
published_date: '2025-10-16T12:00:00+02:00'
description: Testing Google's highly anticipated Gemini 3.0 through AI Studio's A/B feature using SVG generation as a quality proxy
---

Table of Contents

So I kept reading rumors that Gemini 3.0 is accessible through Google AI Studio through A/B testing and the SVGs folks were posting (of Xbox controllers in particular) made me think that they might be right.

Gemini 3.0 is one of the most anticipated releases in AI at the moment because of the expected advances in coding performance.

Evaluating models is a difficult task, but surprisingly the SVG generation task seems to be a very efficient proxy for gauging model quality as@simonwhas shown us using his “pelican riding a bicycle” test.

Lo and behold, after trying a couple of times I got the A/B screen and got an SVG image of an Xbox 360 controller that looked VERY impressive compared to the rest of the frontier.

The exact prompt I used:

Create an SVG image of an Xbox 360 controller. Output it in a Markdown multi-line code block.
Like this:
```svg
...
```

For what it’s worth the model ID for “Gemini 3.0” wasecpt50a2y6mpgkcnwhich doesn’t really help understand which version of the model it is. Perhaps since I user selected Gemini 2.5 Pro it is actually Gemini 3.0 Pro that it is pitted against, as comparing Gemini 3.0 Flash to Gemini 2.5 Pro in an A/B test makes less sense to me. Also, it had about 24s higher TTFT and output length was about 40% longer (this includes reasoning tokens AFAICT), but that doesn’t say much other than it’s likely not a “GPT-5 Pro” type answer that uses significant test time compute.

## Appendix#

“Gemini 3.0” A/B result versus the Gemini 2.5 Pro model:

---
title: Anthropic explains how Claude’s invisible text watermarks will work | The Verge
url: https://www.theverge.com/ai-artificial-intelligence/980869/anthropic-claude-watermarks-synthid-text-system
site_name: newsfeed
content_file: newsfeed-anthropic-explains-how-claudes-invisible-text-wate
fetched_at: '2026-08-17T11:22:27.920663'
original_url: https://www.theverge.com/ai-artificial-intelligence/980869/anthropic-claude-watermarks-synthid-text-system
author: Jess Weatherbed
date: '2026-08-17'
published_date: '2026-08-17T10:57:13+00:00'
description: Anthropic has clarified how it’s planning to apply invisible watermarks to Claude-generated text in order to comply with Europe’s AI transparency rules.
tags:
- the-verge
- ai
- anthropic
- news
---

* AI
* News
* Tech

# Anthropic explains how Claude’s invisible text watermarks will work

﻿It’s using ‘a version’ of the open-source SynthID-Text system Google developed.

﻿It’s using ‘a version’ of the open-source SynthID-Text system Google developed.

by
 
 
Jess Weatherbed
Aug 17, 2026, 10:57 AM UTC
* Link
* Share
* Gift
Image: Cath Virginia / The Verge, Getty Images
Jess Weatherbed
 
is a news writer focused on creative industries, computing, and internet culture. Jess started her career at TechRadar, covering news and hardware reviews.

Anthropic has clarified how it’s planning to apply invisible watermarks to Claude-generated text in order to comply with Europe’s AI transparency rules. On Friday,Anthropic announcedthat Claude’s text marking system is “a version of the SynthID-Text approach” — an open-source watermarking technologydeveloped by Google DeepMindthat creates detectable patterns using wording probabilities.

This watermarking feature,alongside C2PA supportfor Claude-processed images, is being introduced to meet Anthropic’s obligations under theEuropean Union’s AI Act, which requires synthetic audio, image, video, and text to include machine-readable marks that enable the content to be detected as artificially generated or manipulated. Anthropic says the text watermarks won’t make Claude more expensive for users, or “have any practical impact on the quality or content of Claude’s outputs.” Here’s Anthropic’s explanation for how it works:

Take the sentence “The weather today was cold and…”. The next word is very unlikely to be “sugary.” But it is quite likely to be “overcast” or “grey.” Under most circumstances, it doesn’t matter much to the reader which of these latter two words the model ultimately chooses—the meaning of the sentence is largely the same either way. In cases like this, the choice is settled by a random number.

Watermarking uses low-stakes choices like these—which occur many times over a piece of generated text—to leave a pattern in Claude’s responses. That pattern is undetectable to the reader, but is detectable to anyone who has a key that encodes it. When watermarking is used, choices are still made at random, but the source of the randomness is different. Instead of using an arbitrary random number generator to pick the next word, watermarking uses the key and a few words that come before to settle what word the model should pick.

As Anthropic notes, the EU’s AI transparency requirements also impact other major AI developers, so Claude won’t be the only model introducing text watermarks. Google’s Gemini chatbot has supported theSynthID Text solution since 2024, and while OpenAI hasn’t detailed anytext watermarking plansfor ChatGPT in itsAI Act compliance roadmap, it will also be subject to the law’s requirements.

Follow topics and authors
 from this story to see more like this in your personalized homepage feed and to receive email updates.
* Jess Weatherbed
* AI
* Anthropic
* News
* Tech

## Most Popular

Most Popular
1. Flock CEO: ‘We got this one wrong’
2. I finally found a magnetic phone grip I never want to remove
3. ChatGPT’s Computer History tracks your clicks and keystrokes
4. OpenAI reportedly disbanded its preparedness team
5. Marvel reveals the new X-Men cast, including Inde Navarrette and Adam Driver

## The Verge Daily

A free daily digest of the news that matters most.

Email (required)
Sign Up
By submitting your email, you agree to our
 
Terms
 and 
Privacy Notice
. 
This site is protected by reCAPTCHA and the Google
 
Privacy Policy
 
and
 
Terms of Service
 
apply.
Advertiser Content From

This is the title for the native ad

## More inAI

ChatGPT’s Computer History tracks your clicks and keystrokes
Rogue AI aren’t science fiction anymore
Have a laugh at AI’s expense by roleplaying as a chatbot
Mark Zuckerberg has an Instagzam
You can now turn off Google Gemini’s visible watermarks
Apple trained its own AI model for China with help from Alibaba
ChatGPT’s Computer History tracks your clicks and keystrokes
Terrence O'Brien
Aug 16
Rogue AI aren’t science fiction anymore
Robert Hart
Aug 16
Have a laugh at AI’s expense by roleplaying as a chatbot
Terrence O'Brien
Aug 15
Mark Zuckerberg has an Instagzam
David Pierce
Aug 14
You can now turn off Google Gemini’s visible watermarks
Emma Roth
Aug 14
Apple trained its own AI model for China with help from Alibaba
Robert Hart
Aug 14
Advertiser Content From

This is the title for the native ad

## Top Stories

13 minutes ago
Whisker’s AI-powered litter robot thinks my cats swapped bodies
7:00 AM UTC
I’m hooked on Peak Design’s new City bags
Aug 16
Rogue AI aren’t science fiction anymore
13 minutes ago
How to take better photos of your pets
Aug 15
We’re reaching peak camera with the Sony A7R VI
---
title: Apple Exploring Ways to Run Much Larger AI Models Directly on iPhones - MacRumors
url: https://www.macrumors.com/2026/07/09/apple-prismml-larger-on-device-ai-models/
site_name: tldr
content_file: tldr-apple-exploring-ways-to-run-much-larger-ai-models
fetched_at: '2026-07-11T01:37:14.069887'
original_url: https://www.macrumors.com/2026/07/09/apple-prismml-larger-on-device-ai-models/
date: '2026-07-11'
description: Apple has held meetings with PrismML about ways it could use the startup's technology to run much larger AI models directly on iPhones, according to The Information. The report said PrismML has managed to shrink down Alibaba's open-source large language model Qwen 3.6 to run entirely on an iPhone 17 Pro. The model has 27 billion parameters, which is larger than Apple's on-device AFM 3 Core Advanced model with 20 billion parameters.
tags:
- tldr
---

# Apple Exploring Ways to Run Much Larger AI Models Directly on iPhones

Thursday July 9, 2026 9:24 am PDT
 by 
Joe Rossignol

Apple has held meetings with PrismML about ways it could use the startup's technology to run much larger AI models directly on iPhones,according toThe Information.

The report said PrismML has managed to shrink down Alibaba's open-source large language model Qwen 3.6 to run entirely on an iPhone 17 Pro. The model has 27 billion parameters, which is larger than Apple's on-device AFM 3 Core Advanced model with 20 billion parameters. Apple's model powers iOS 27 enhancements such as Siri AI's more expressive voices and improved systemwide dictation on iPhone 17 Pro and iPhone Air models.

Unlike with AFM 3 Core Advanced, all of Qwen 3.6's parameters can be active at the same time.

"One new on-device Apple model has 20 billion parameters but uses a so-called sparse architecture, in which only 1 billion to 4 billion parameters are active at a time," the report said, in reference to AFM 3 Core Advanced. "In the case of PrismML's on-device model, all 27 billion parameters are active at the same time."

Larger models running directly on iPhones would allow for more Apple Intelligence features to run on device instead of on Apple's Private Cloud Compute servers, which could reduce Apple's costs and further enhance user privacy.

Tags: 
Apple Intelligence Guide
, 
The Information
[ 
103 comments
 ]

Get weekly top MacRumors stories in your inbox.

Leave this field empty

## Popular Stories

### The MacRumors Show: Siri AI, Apple Intelligence in Apps, and More at WWDC 2026

Wednesday June 10, 2026 9:41 am PDT by 
Hartley Charlton
On this week's special episode of The MacRumors Show, we talk through all of the major announcements Apple unveiled at WWDC 2026, including Siri AI, new Apple Intelligence features in apps, and system-wide performance and design improvements.Subscribe to The MacRumors Show YouTube channel for more videos Apple framed the keynote around three areas: platform improvements, Trust and Safety,...

### Advanced AI Dictation Not Enabled by Default in iOS 27 Beta

Monday June 22, 2026 8:44 am PDT by 
Hartley Charlton
Apple's next-generation AI dictation feature for the iPhone 17 Pro and iPhone Air is not turned on by default in the first developer beta of iOS 27.Apple says the new AI-powered dictation system delivers "a major boost in accuracy," with more reliable on-the-fly capitalization and punctuation than the existing dictation system. The feature runs on Apple's new AFM 3 Core Advanced model,...

### Apple Intelligence Home Features Require 2TB iCloud+ Plan in iOS 27

Monday July 6, 2026 2:13 pm PDT by 
Juli Clover
Using Apple Intelligence camera features in the Home app will require an iCloud+ plan starting at 2TB, according to Apple. Apple shared the detail in its notes for the third macOS Golden Gate beta that was released today.In iOS 27, iPadOS 27, and macOS 27 Golden Gate, the Home app is able to generate written summaries for motion alerts from HomeKit Secure Video cameras. It's also able to...

## Top Rated Comments

Taq'aix
23 hours ago at 09:37 am
The AI bubble can’t burst soon enough.
Score:
 23 Votes (
Like
 | 
Disagree
)
DanteHicks79
23 hours ago at 09:31 am
👏 NOBODY 👏 WANTS 👏 THIS 👏 AI 👏 GARBAGE 👏
Score:
 21 Votes (
Like
 | 
Disagree
)
smeagol
23 hours ago at 09:35 am
Ultimately, Apple shot themselves in the foot by either being stingy with RAM across all devices for decades, or by upgrading to higher capacity memory prohibitively expensive in the name of profits, saying nonsense like 8GB on an Apple device is like 16GB for everyone else. AI came along and told the truth, 8GB is 8GB.
Score:
 20 Votes (
Like
 | 
Disagree
)
C
ChrisA
22 hours ago at 10:06 am
The report said PrismML has managed to shrink down Alibaba's open-source large language model Qwen 3.6 to run entirely on an iPhone 17 Pro. The model has 27 billion parameters,
There are many comments here, and not one about PrismML's new technology.
What they have done is invent a new way to compress a neural network to one bit per parameter. This means each parameter is just a one or a zero. Not only does this save space, it saves a LOT of space. Now Apple's 10B-parameter on-device model will fit in just over 1GB of RAM and hence comfortably into a 6 GB iPhone. (The iPhone 15 has only 6GB of RAM.)
Not only does it save space, but it also runs with less energy because it is very easy to multiply by 1 or by 0. Most of us can do that kind of math in our heads.
How does it work exactly? I don't know yet. I assume it is not so easy as simply normalizing all values to the 0...1 range and thresholding at 0.5. I suspect that replicating the "important" parameters is involved, but I don't know how you would find them.
PrismML says they are not done yet. Of course, a width of 1 is the shortest possible, but maybe they are reducing the number of parameters without doing much harm?
PrismML says the work is based on mathematics. They don't claim AI breakthroughs or better code. This might mean they have some Linear Algebra experts.
Maybe someone here has some better insight?
Score:
 16 Votes (
Like
 | 
Disagree
)
N
neuropsychguy
23 hours ago at 09:38 am
This is the future. If we can have current model performance on-device, that will help solve a lot of the energy problems. It's likely years away (if it ever gets there), but it should be one of the goals.
Score:
 16 Votes (
Like
 | 
Disagree
)
turbineseaplane
23 hours ago at 09:40 am
Speak for yourself. If nobody wanted it, it wouldn’t exist.
AI does not exist right now, in its current form, because of demand for it.
Score:
 14 Votes (
Like
 | 
Disagree
)
Read All Comments
---
title: Build with Veo 3, now available in the Gemini API - DEV Community
url: https://dev.to/googleai/build-with-veo-3-now-available-in-the-gemini-api-1klk
site_name: devto
fetched_at: '2025-07-27T01:04:59.342682'
original_url: https://dev.to/googleai/build-with-veo-3-now-available-in-the-gemini-api-1klk
author: Alisa Fortin
date: '2025-07-23'
description: We're bringing Veo 3 to developers in paid preview via the Gemini API and Vertex AI. First... Tagged with gemini, veo, api, webdev.
tags: '#gemini, #veo, #api, #webdev'
---

## We're bringing Veo 3 to developers in paid preview via theGemini APIandVertex AI.

First unveiled atGoogle I/O 2025, people around the world have already generated tens of millions of high-quality videos withVeo 3(along with some new fun and interesting video trends). It is our first video model to incorporate high-fidelity video outputs and native audio, first with text-to-video and soon with image-to-video.

Developers are already experimenting with Veo 3, discovering how the model can help them brainstorm content, rapidly iterate, and be more efficient.

* Cartwheeldeveloped a system that can take 2D videos of humans and translate it into fully production ready 3D animation on rigged characters. Cartwheel uses Veo 3 togenerate realistic, fluid human actionsthat Cartwheel can then turn into 3D animations for customers.
* Volleyuses Veo 3 to produce in-game video cut-scenes that advance the story. With Veo 3, Volley designers can rapidly iterate on the game to deliver the best possible output for an upcoming RPG game calledWit's End.

## Veo 3 capabilities

Veo 3 is designed to handle a range of video generation tasks, from cinematic narratives to dynamic character animations. With Veo 3, you can create more immersive experiences by not only generating stunning visuals, but also audio like dialogue and sound effects.

* Synchronized Sound:Natively generates rich audio—dialogue, effects, and music—and synchronizes it with video in a single pass.
* Cinematic Quality:Produces stunning, high-definition video that captures creative nuances in your prompt, from intricate textures to subtle lighting effects.
* Realistic Physics:Simulates real-world physics for authentic motion, from natural character movement to the accurate flow of water and casting of shadows.

Let’s take a look at some examples.

Prompt: Fluffy Characters Stop Motion: Inside a brightly colored, cozy kitchen made of felt and yarn. Professor Nibbles, a plump, fluffy hamster with oversized glasses, nervously stirs a bubbling pot on a miniature stove, muttering, "Just a little more... 'essence of savory,' as the recipe calls for." The camera is a mid-shot, capturing his frantic stirring. Suddenly, the pot emits a loud "POP!" followed by a comical "whoosh" sound, and a geyser of iridescent green slime erupts, covering the entire kitchen. Professor Nibbles shrieks, "Oh, dear! Not again!" and scurries away, leaving a trail of tiny, panicked squeaks.

Prompt: The sequence begins with an extreme close-up of a single gear, slowly turning and reflecting harsh sunlight. The camera gradually pulls back in a continuous movement, revealing this is but one component of a colossal, mechanical heart half-buried in a desolate, rust-colored desert. A sweeping aerial shot establishes its enormous scale and isolation in the barren landscape. The camera descends to capture pipes hissing steam and the rhythmic thumping that echoes across the empty plains. A subtle shake effect synchronizes with each massive heartbeat. A lateral tracking shot discovers tiny, robed figures scurrying across the metallic surface. The camera follows one such figure in a detailed tracking shot as they perform meticulous maintenance, polishing brass valves and tightening immense bolts. A complex movement circles the entire structure, capturing different maintenance teams working in precarious positions across its rusted exterior. The final shot begins tight on the meticulous work of one tiny figure before executing a dramatic pull-out that reveals the true scale of the heart and the minuscule size of its caretakers, tending to the vital organ of an unseen, sleeping giant that extends beyond the frame.

Explore these examples and more withVeo 3 in Google AI Studio, available as an SDK template and interactive Starter App to remix, copy and extend. The Starter App and its sample code offer a convenient way for Paid Tier users to rapidly prototype with Veo 3 and more on the Gemini API, directly from Google AI Studio.

Click the Key button in the top right of the AI Studio Build interface to select a Google Cloud Project with billing enabled to use the Paid Tier in AI Studio apps. See theFAQsfor more.

## Get started with Veo 3 in the Gemini API

Veo 3 will bepricedat $0.75 per second for video and audio output. Additionally, Veo 3 Fast will be available soon, offering a faster and more cost-effective option for video creation.

Here’s a basic Python example to create a video:

import

time

from

google

import

genai

from

google.genai

import

types

client

=

genai
.
Client
()

operation

=

client
.
models
.
generate_videos
(


model
=
"
veo-3.0-generate-preview
"
,


prompt
=
"
a close-up shot of a golden retriever playing in a field of sunflowers
"
,


config
=
types
.
GenerateVideosConfig
(


negative_prompt
=
"
barking, woofing
"
,


),

)

# Waiting for the video(s) to be generated

while

not

operation
.
done
:


time
.
sleep
(
20
)


operation

=

client
.
operations
.
get
(
operation
)

generated_video

=

operation
.
result
.
generated_videos
[
0
]

client
.
files
.
download
(
file
=
generated_video
.
video
)

generated_video
.
video
.
save
(
"
veo3_video.mp4
"
)

Enter fullscreen mode

Exit fullscreen mode

## Building responsibly with Veo 3 in the Gemini API

All videos generated by Veo 3 models will continue to include a digitalSynthIDwatermark. To get started, check out the documentation, cookbook, and a Veo 3 starter app in Google AI Studio:

* Read the documentation
* Veo cookbook
* Try the Veo 3 starter app(paid tier only)
In addition to being available via the Gemini API in Google AI Studio, Veo 3 is also available toGoogle AI subscribersin theGemini appandFlow, and to enterprise customers viaVertex AI.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse

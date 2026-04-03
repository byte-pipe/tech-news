---
title: Get started with me & Kestra.io - DEV Community
url: https://dev.to/missamarakay/get-started-with-me-kestraio-b94
site_name: devto
fetched_at: '2026-01-02T11:07:36.262122'
original_url: https://dev.to/missamarakay/get-started-with-me-kestraio-b94
author: Amara Graham
date: '2025-12-26'
description: New job (!!!), so let's learn orchestration with Kestra.io together. Tagged with orchestration, automation, gettingstarted, opensource.
tags: '#orchestration, #automation, #gettingstarted, #opensource'
---

Guess who got a new job and is going to take you along the onboarding and learning journey? ME! 🤗

I decided to go back to the core of my DevRel roots and joinKestra.ioas a developer advocate to help expand into the US market. I'm pretty excited to get back to learning and doing in public, and of course seeing all your wonderful faces in person at events. I've really missed the direct connection to the developer community. It's good to be back.

## What is Kestra?

Kestra is a declarative workflow orchestration platform that really leans into the everything-as-code construct, but also has a pretty good experience for the config only no-coders out there too.

Since I enjoy walking the line between coding and no-coding experiences out of pure laziness, the editor experience really sold it for me. I can see the YAML (code), no-code (that immediately modifies the YAML), and an editable topology all in the same editing experience in side-by-side panels. The YAML is readable, and the diagram gives me a great visual of what I'm building, and I can edit wherever I want.

This really lights up all the areas in my brain in ways other platforms just haven't done. Leaning too hard into no-code and config only experiences made me frustrated that I couldn'tjust write code, while sometimes I'd love to have someone else wrap the values I need for my solution in the boilerplate necessary tojust make them work. Callback to the next Hannah Montana gif because I do, in fact, like the flexibility that comes with the best of both worlds.

## Using and evaluating Kestra

Kestra has two editions - OSS and Enterprise - although it's three if you count Cloud. For the purposes of this blog, Cloud is just a different administered experience, a different flavor of Enterprise if you will. If you are looking for an OSS project to contribute to in the new year, we got that too! But I digress.

Kestra OSS will be great for single user use cases, but also more than enough for doing a general evaluation of the flow building experience. Kestra Enterprise does unlock some pretty cool enterprise-y features, but digging into building your first flow is where things will click. At least that's where they did for me.

I recommend following thequickstartand spinning up Kestra OSS with Docker compose. Just make sure you have Docker setup and, unless you are old like me, you probably already know Docker compose ships with Docker. What a time to be alive!

Pop this into your terminal, then head tohttp://localhost:8080:

docker run --pull=always --rm -it -p 8080:8080 --user=root -v /var/run/docker.sock:/var/run/docker.sock -v /tmp:/tmp kestra/kestra:latest server local

Enter fullscreen mode

Exit fullscreen mode

Pay attention to the note in the docs about whether you need a persistent database backend or not. For my first few flows and executions this wasn't necessary and, to be honest, I just left it running in the background because I wasn't doing anything else that was compute heavy or intensive. Your mileage may vary!

I then recommend heading straight to theBlueprintsafter running a tutorial or two. Once you execute a few flows to get some data in your dashboards you can dig in to building your own flow with the tons of available communityplugins.

I'm still working on a flow that prompts me to wrap up my day or week by pulling together what I did in different places so I can accurately summarize what Iactuallydid. Maybe remind me to do a blog on this later. Keen eyes may notice my WIP in the flow editor screenshot. 👀

## But wait, what's an orchestrator even for?

I have this hypothesis that "orchestration" doesn't resonate with everyone in tech. At least not yet.

I think many of us have a general understanding that we have many disparate systems with dataeverywhereand if we could just use all of that together, we couldmaybesolve some really cool and interesting problems. That's where the orchestration piece comes in - getting these different systems to talk to each other to accomplish a unified goal or a task.

The folks in DevOps seem to get it, along with the folks in AI, probably because they are already working with so many different pieces and pulling things together, whether it's 5 different platforms and projects to standup a cluster or merging datasets from several different sources to provide the best answer.

I'm sure I'll have another blog on this topic in the future, but I'm interested to hear what your definition of an orchestrator or orchestration is, when you learned about it, and how you use it, or maybe even how you know when to use an orchestrator. Leave me a comment and let's talk!

Join me as I dig in more and let me know what you are building. Like I said, it's good to be back. 💜

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse

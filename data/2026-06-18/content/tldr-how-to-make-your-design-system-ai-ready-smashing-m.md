---
title: How To Make Your Design System AI-Ready — Smashing Magazine
url: https://www.smashingmagazine.com/2026/06/how-make-design-system-ai-ready/
site_name: tldr
content_file: tldr-how-to-make-your-design-system-ai-ready-smashing-m
fetched_at: '2026-06-18T12:19:33.542775'
original_url: https://www.smashingmagazine.com/2026/06/how-make-design-system-ai-ready/
date: '2026-06-18'
published_date: 2026-06-03 13:00:00 +0000 UTC
description: Practical guide on how to reduce drifts, minimize mistakes, maintain context, and improve the quality of AI-generated prototypes. Brought to you by Design Patterns For AI Interfaces, **friendly video course on UX** and design patterns by Vitaly.
tags:
- tldr
---

* 4 min read
* Design,AI,Design Patterns,UX
* Share onTwitter,LinkedIn

#### About The Author

Vitaly Friedman loves beautiful content and doesn’t like to give in easily. When he is not writing, he’s most probably runningfront-end & UX …More about
Vitaly ↬

#### Email Newsletter

Your (smashing) email

Weekly tips on front-end & UX.Trusted by 182,000+ folks.

Practical guide on how to reduce drifts, minimize mistakes, maintain context, and improve the quality of AI-generated prototypes. Brought to you by 
Design Patterns For AI Interfaces
, 
friendly video course on UX
 and design patterns by Vitaly.

AI-generated prototypesoften don’t deliver consistently decent results because of tiny inconsistencies scattered all across a design system. I’s decisions made but not documented, hard-coded values never cleaned up, orrelying too much on AImaking sense of mock-ups or design flows on its own.

Yesterday I stumbled upon auseful practical guideby Hardik Pandya from Atlassian — onhow to reduce drifts, minimize mistakes, maintain context, and improve the quality of AI-generated prototypes. Let’s see how it works.

To get better results, AI needs better guidance that minimizes assumptions and reduces ambiguity. Guide by 
Hardik Pandya
. (
Large preview
)

## 1. Design Decisions Are Infrastructure

Unsurprisingly, better AI prototypescome from better data— but also from better human guidance. We shouldn’t assume that AI knows how to choose the right component and how to design with accessibility in mind. It needs priorities, a clear path on how we make decisions, design principles, examples, do’s and don’ts.

In fact, we should treat design decisions asinfrastructure. That means that every time we make a decision — not just a design decision, but even a decision on how to actually prioritize our work and how we make decisions around here — it must find a path into the spec file that is then consumed by AI.

## 2. Auditing: FigmaLint

One of the useful tools to audit the quality of the design system isFigmaLint. It’s a usefulfree Figma pluginfor auditing tokens, states, accessibility, binding tokens, renaming layers, detecting detached instances, missing interactive states and hard-coded values — and preparing the design documentation.

Neat little helper to streamline auditing: 
FigmaLint
. (
Large preview
)

If you often have to work withvendors and third partieswho supply you with their design systems and component libraries, that’s a great helper to have by your side — especially if you want to improve the quality of prototypes, AI-generated code, and AI-written documentation.

## 3. Three Layers: Spec Files + Token Layer + Auditing

To ensure quality, we establish design principles, guidelines, and rules in the form of “spec files”. It’s structured Markdown files that include spacing rules, color choices, component usage guidelines, priorities, etc. AI is going to read and reuse that spec file every time it’s going to generate a prototype.

An example of a folder that organizes spec files to be AI-friendly. 
Jump to full example
. (
Large preview
)

Because the spec files are text files, it’s much morecost-effectivebut also much more accurate, just because we don’t rely on AI recognizing or decoding patterns from mock-ups but get specific guidelines instead. In fact, extending code is often a more effective way than generating code from mock-ups.

Thetoken layerlists and keeps updated all tokens used throughout the design system. AI always chooses from a closed set of named variables instead of inventing plausible values ad hoc.

Context engineering is everything. Five levels of context engineering: 
a practical overview
, by Matthew Alverson, via Addy Osmani. (
Large preview
)

Anaudit scriptcatches what AI gets wrong. It scans the prototype and flags every hard-coded value and flags it if necessary. It can be a regular software doing that, with AI waiting for its feedback to come back.

Finally, when a design systemships updates, a sync routine flags which spec files need updating. The goal is to make sure that AI always reads up-to-date, current specs, not the ones written against an outdated version.

## 4. Examples of AI-Ready Design Systems

* Atlassian
* Carbon
* CMS Design System
* Nordhealth

## Wrapping Up

Ultimately, AIcannot magically resolvetechnical debt or design debt without proper guidance. It relies heavily on clear decisions, established priorities, and well-defined principles.

The moredeliberate and precisedesigners are in guiding AI, the better the overall outcomes will be. This requires not just cleaning up and improving design systems but also maintaining them over time as decisions need to trickle down into Markdown files. We’ll be busy for years to come.

## Meet “Design Patterns For AI Interfaces”

MeetDesign Patterns For AI Interfaces, Vitaly’s newvideo coursewith 100s of real-life examples and UX guidelines to design AI features that people actually use — with alive UX traininglater this year.Jump to a free preview.

MeetDesign Patterns For AI Interfaces, Vitaly’s video course on interface design & UX.### Video + UX Training$450.00$799.00Get Video + UX Training30 video lessons (10h) +Live UX Training.100 days money-back-guarantee.### Video only$275.00$395.00Get the video course30 video lessons (10h). Updated yearly.Also available as aUX Bundle with 3 video courses.

## Useful Resources

* FigmaLint, by TJ Pitre
* Atlassian AI-Ready Design System Example, by Atlassian
* Carbon AI-Ready Design System Example, by IBM
* CMS Design System AI-Ready Example, by Centers for Medicare & Medicaid Services
* Nordhealth AI-Ready Design System Example, by Nordhealth

(yk)
Explore more on
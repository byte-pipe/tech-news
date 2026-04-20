---
title: Jargon Doesn't Make You Senior - DEV Community
url: https://dev.to/jonoherrington/jargon-doesnt-make-you-senior-50fd
site_name: devto
content_file: devto-jargon-doesnt-make-you-senior-dev-community
fetched_at: '2026-03-26T11:22:38.336834'
original_url: https://dev.to/jonoherrington/jargon-doesnt-make-you-senior-50fd
author: Jono Herrington
date: '2026-03-23'
description: I asked one of my tech leads to demo the latest work to a cross-functional group. Business... Tagged with webdev, leadership, discuss.
tags: '#discuss, #webdev, #leadership'
---

I asked one of my tech leads to demo the latest work to a cross-functional group. Business stakeholders. UX. Product. Engineering.

The work deserved the room's attention. His team had built out a component library using Storybook to streamline the design-to-development workflow. Designers could see exactly what engineers had built. Engineers could build exactly what designers intended. Handoff time dropped. Misinterpretations between the two disciplines that used to create entire cycles of rework were gone.

But he told the story in engineering. He kept referencing technical implementation details that sounded impressive from a developer's perspective but meant nothing to half the room. Contracts. CI/CD pipelines. Caching layers. Things that mattered deeply to how the work was built. Things that had zero relevance to why it was built or what it meant for the business.

The business side nodded politely. UX checked out. Product was trying to translate in real time. And the actual impact of the work got buried under terminology that only a third of the audience could parse.

If he'd stripped the jargon out, the demo would have landed. The work spoke for itself. The technical details were getting in the way of the story, not supporting it.

## The Reddit Post Nobody Could Help With

I saw a post on Reddit where a dev was venting about their manager's manager going through every PR and demanding more productivity while adding more meetings. Used terms like "o3" for one-on-one, "N+1" for their manager, and "N+2" for the skip-level. The top comment with 44 upvotes was "Speak English brother."

Almost nobody addressed the actual problem.

Because nobody could understand the post.

Not because the problem was complex. Because the language was. The person asking for help had accidentally built a wall between themselves and the people who could help them. The jargon that made them feel precise was the thing that made them invisible.

This happens in engineering orgs every day. And it's not limited to Reddit.

## Where Jargon Hides

The obvious version is the one everyone jokes about. Leaders who say "let's leverage our synergies to optimize velocity" when they mean "let's work together to ship faster." That's easy to spot and easy to mock.

The harder version is the one my tech lead did in that demo. The jargon wasn't corporate fluff. It was technically accurate. He wasn't wrong about anything he said. He was just saying it to the wrong audience. And the gap between technically accurate and actually understood is where communication goes to die.

The gap between technically accurate and actually understood is where communication goes to die.

I see it in docs that only the author can parse. In Slack messages that require three follow-up questions before anyone knows what's being asked. In meeting agendas written in shorthand that assumes everyone in the room has the same context. In architecture reviews where the presenter uses acronyms they invented for their own team and never defines them.

None of this is malicious. Most of it isn't even conscious. Engineers optimize for precision. Precision in language means using the most specific term available. The problem is that the most specific term is often the least accessible one. And accessibility is the whole point of communication.

## Why It's Hard to Stop

Early in my career I used jargon because I thought it proved I belonged. I'd walk into a meeting with stakeholders and talk about "decoupled architectures" and "event-driven patterns" when what I meant was "we built it so changes in one place don't break everything else." I thought precision made me credible. What it actually did was make me forgettable. The stakeholders remembered the engineer who said the clear thing. Not the one who said the technically correct thing.

Jargon feels like competence. When you use the precise technical term, you signal depth. You signal that you've been in the room long enough to speak the language. That's not a small thing in an industry that respects technical credibility above almost everything else.

Stripping the jargon out feels like dumbing it down. And nobody wants to feel like they're dumbing things down. Especially not in front of stakeholders they're trying to impress.

But the most respected engineers I've worked with communicate like they're explaining to a smart friend.

The most respected engineers communicate like they're explaining to a smart friend. Not dumbing it down. Stripping it clean.

Not dumbing it down. Stripping it clean. They assume intelligence in the listener and take responsibility for making the complex thing simple.

## The Distributed Problem

This gets worse when your team spans continents.

I lead engineering across North America, Europe, and Asia. English is the working language but it's not everyone's first language. And jargon that's already confusing to a native English speaker becomes completely opaque to someone parsing it in their second or third language.

An engineer in Serbia doesn't need you to dumb things down. They need you to say what you mean in words that translate cleanly. "We need to decouple the service mesh from the deployment pipeline" means something very specific to the person who wrote it. To someone reading it across eight time zones in a language they learned in school, every word in that sentence is doing double duty and half of them might not land.

I've watched async communication break down entirely because a Slack message used four acronyms that only one team understood. The follow-up questions took longer than the original conversation would have taken if it had been written in plain language from the start. And by the time the clarification arrived, the engineer in the other time zone had already moved on to something else. The window for collaboration closed because the message wasn't clear enough to act on. Multiply that across a distributed org and jargon isn't just a communication problem. It's a productivity tax.

## What I Told My Tech Lead

After that demo, we had a conversation. Not a correction. A reframe.

The work was excellent. The delivery obscured it. And that's the worst outcome for an engineer. Not that the work was bad. That the work was good and nobody in the room could see it because the language got in the way.

I asked him one question. "If you were explaining this to your wife, what would you say?"

He laughed. Then he said it in two sentences. Clear. Specific. No jargon. The impact was obvious. The value was immediate.

That's the version the room needed. And it was already in his head. He just needed permission to use plain language in a professional setting. Because somewhere along the way, engineering culture taught him that simple language means simple thinking. It doesn't. Simple language means you've done the hard work of understanding something well enough to explain it without the crutch of terminology.

The conversation wasn't about his technical skill. That was never in question. It was about reading the room. A demo to engineers should sound like engineering. A demo to a cross-functional group should sound like a story about what changed for the customer, the business, or the product. The technical depth lives underneath. It comes out when someone asks a question. Not before.

I've watched this pattern play out across every org I've been part of. The engineers who get promoted fastest aren't always the strongest technically. They're the ones who can walk into any room and adjust. They give the CTO the architecture. They give the VP of Product the customer impact. They give the designer the user experience implications. Same work. Different lens. The substance doesn't change. The translation does.

That's the skill most engineers never get coached on. Not what to say. Who they're saying it to. And adjusting the message without losing the substance.

Not what to say. Who they're saying it to.

## The Real Test

If your message needs a glossary, rewrite it. If a new hire couldn't understand your meeting agenda, simplify it. If someone outside your team couldn't follow your Slack message, it's not clear enough.

That's not about lowering the bar. That's about raising your ability to communicate across the bar. The engineer who can explain a complex system to a product manager in plain language understands that system better than the engineer who can only explain it in technical terms. Because they've done the extra work of translation. And translation requires deeper understanding, not shallower.

My tech lead got this. The next demo he gave was the same level of technical depth underneath but the presentation was stripped clean. Business stakeholders asked questions. UX engaged. Product connected the work to the roadmap. The room was alive instead of politely confused.

Same engineer. Same quality of work. Different level of communication. And suddenly the work got the recognition it deserved.

Jargon doesn't make you senior. Clarity does.

I write daily about engineering leadership atjonoherrington.com.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (16 comments)


For further actions, you may consider blocking this person and/orreporting abuse

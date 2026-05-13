---
title: Two DEV Users. Two Countries. One Weird Little Avatar Project. - DEV Community
url: https://dev.to/itsugo/two-dev-users-two-countries-one-weird-little-avatar-project-3gd3
site_name: devto
content_file: devto-two-dev-users-two-countries-one-weird-little-avata
fetched_at: '2026-05-13T19:36:41.079773'
original_url: https://dev.to/itsugo/two-dev-users-two-countries-one-weird-little-avatar-project-3gd3
author: Aryan Choudhary
date: '2026-05-13'
description: We Gave Our DEV Avatar Project a V2… and It Escalated Quickly A few months ago,... Tagged with webdev, nextjs, sideprojects, react.
tags: '#webdev, #nextjs, #sideprojects, #react'
---

Technical hurdles and VRM animation bugs

### We Gave Our DEV Avatar Project aV2… and It Escalated Quickly

A few months ago,@webdeveloperhyperand I made a small side project where two VRM avatars talked to each other in a 3D scene.

At the time, it was just meant to be something fun. Two developers from different countries making weird little animated characters interact over the internet because… honestly, why not?

If you missed the first post, here it is:

How a DEV Friend and I Brought Two Avatars to Life

Back then, the project was much simpler. A conversation system, some VRM animations, a few gestures, and a surprising amount of time spent trying to stop avatars from snapping into cursed poses mid-animation.

We thought we were mostly done with it.

We were very wrong.

### Somewhere along the way, the project became… alive

The funny thing about side projects is that they rarely stay contained.

You fix one thing, get one new idea, add one “small feature,” and suddenly a weekend experiment starts behaving like an actual system.

That’s pretty much what happened here.

While I was busy juggling office life, Japanese, engineering work, interviews, marketing side quests, and trying to survive adulthood without my brain overheating… WDH was quietly evolving the project in the background like some kind of sleep-deprived VRM wizard.

And every few days I’d wake up to messages like:

“Added music and music button. Then pushed."

or

“fix mobile speech bubble layout and responsive avatar positioning”

or sometimes just:

“fixed and pushed.”

And somehow the project kept getting cooler.

### The avatars stopped feeling scripted

One of the biggest changes in v2 was that the characters stopped feeling like objects that simply played animations on command.

Now they actually react.

They blink naturally. Follow movement. Shift attention while listening. React while the other character is speaking. Small details, but weirdly important ones.

It turns out humans are very sensitive to tiny signs of life.

A static model feels dead immediately.

But add:

1. eye tracking
2. idle movement
3. small delays
4. slight reactions
5. facial expressions
…and suddenly your brain starts treating it like a character instead of geometry.

That transition fascinated me way more than I expected.

At one point we spent an unreasonable amount of time adjusting tiny gesture timings that most users probably won’t consciously notice.

But that’s kind of the magic of interactive systems.

The invisible details are usually doing the heavy lifting.

### The architecture quietly became more interesting too

The first version was mostly about “getting it to work.”

The second version became more about orchestration.

Now the scene handles:

1. dialogue sequencing
2. animation coordination
3. background switching
4. music control
5. expression timing
6. responsive layouts
7. costume switching
8. branching interactions

And because of that, hardcoding behavior stopped making sense very quickly.

So instead of writing giant chains of conditions everywhere, the conversation itself became structured data.

Each dialogue entry knows:

* who is speaking
* what animation plays
* what expression appears
* how timing should behave

Which made the system dramatically easier to extend without everything collapsing into spaghetti.

Ironically, the more playful the project became, the more important clean systems thinking became too.

### The funniest bugs were always animation-related

There is probably a law somewhere stating that if you work with avatars long enough, something horrifying will eventually happen. And if not it should be.

At various points:

* arms rotated into dimensions unknown to mankind
* blinking broke and created sleep paralysis avatars
* gesture transitions snapped violently
* one animation froze mid-pose and looked like the character had emotionally given up on life
* Classic side project experience honestly.

But weirdly enough, those moments ended up becoming some of the most memorable parts of the project.

Because every fix made the avatars feel a little more believable.

### While all this was happening,@webdeveloperhyperwas building something much bigger

And this is honestly the part I respect the most.

While we were experimenting with our collaboration project, WDH was also building something called AI Avatar — a VS Code and Chrome extension where VRM avatars react to AI activity, animate while you work, track your cursor, trigger expressions, speak through speech bubbles, and basically exist beside you like a tiny chaotic coding companion.

The interesting thing is that it never felt like one of those overly corporate “AI productivity” tools trying to optimize your soul.

It felt playful.

Like something made by someone who genuinely likes interactive characters and wants technology to feel a little more alive and personal.

And I think that mindset naturally spilled back into our collab project too.

A lot of the small interaction details, responsiveness ideas, animation handling improvements, and experimentation mentality came from constantly exploring these systems further.

Which honestly reminded me why collaborations matter so much.

You don’t just share workload.

You share ways of thinking.

### The project accidentally became a tiny engine

That’s probably the strangest realization from all this.

At some point we stopped thinking:

“we’re making two avatars talk”

And started realizing:

“wait… this is basically becoming a reusable interaction system.”

Now there’s:

* branching dialogue
* modular animation logic
* reusable scene orchestration
* dynamic reactions
* configurable backgrounds
* audio systems
* responsive UI behavior
And suddenly your silly little side project starts looking suspiciously scalable.

That’s always the dangerous phase.

### But honestly, the best part was still the process

The actual code matters, obviously.But what I’ll probably remember most is:

* random weekend debugging
* async conversations across timezones
* sending screenshots back and forth
* testing weird ideas just because they sounded funny
* slowly watching something gain personality
* That feeling is hard to replicate in structured environments.

No roadmap pressure. No stakeholder meetings. No “business value alignment.”

Just curiosity carrying the project forward.

And honestly?That’s probably why side projects stay fun.

### Where this goes next

Right now, v2 still feels like the beginning.

There are already ideas floating around for:

* interactive storytelling
* user-triggered reactions
* branching scenes
* mini-games
* dynamic conversations
* more expressive characters
* Or maybe something completely different.
At this point, I’ve stopped trying to predict where these projects go.

The fun part is discovering it while building.

### For the people interested in trying it themselves

WDH made a public version available here:

Vercel Demo (with VRMA + MP3)

GitHub Repo (without VRMA + MP3)

And honestly, if you build something weird with it, let us know.

Those are usually the best ideas anyway.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
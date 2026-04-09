---
title: Are We Losing Our Manners in Software Development? - DEV Community
url: https://dev.to/adiozdaniel/are-we-losing-our-manners-in-software-development-1c55
site_name: devto
fetched_at: '2025-12-24T11:08:02.551974'
original_url: https://dev.to/adiozdaniel/are-we-losing-our-manners-in-software-development-1c55
author: adiozdaniel
date: '2025-12-18'
description: The longer I write software, the more my sense of “impressive” changes. What actually amazes me these... Tagged with discuss, performance, softwaredevelopment.
tags: '#discuss, #performance, #softwaredevelopment'
---

The longer I write software, the more my sense of “impressive” changes. What actually amazes me these days isn’t modern technology, but older systems — and the people who built them.Take Windows 95. A full operating system from almost 30 years ago. GUI, drivers, multitasking, multimedia, process and thread management. All of it lived in roughly 50 MB on disk and ran on 4–8 MB of RAM.

Now compare that to today. The browser tab I’m using to type this text currently takes over 1 GB of memory. I’m not compiling anything. I’m not rendering video. I’m just editing text.That number alone would horrify engineers from the 1980s — people who ran full multi-user Unix environments on machines with 2 MB of RAM and 20 MB hard drives. Entire development workflows — editors, compilers, networking, users — fit inside constraints that feel impossible now.

Even small things today feel heavy. A simple “Hello, World” after activating a virtual environment can easily pull in tens of megabytes of libraries before any real logic runs. Not because the problem is complex, but because the ecosystem around it is.

The Disappearing Discipline

What surprises me isn’t that hardware became faster. That was inevitable. What surprises me is how abundance changed our behavior. We lost our software manners.

The constraint of scarcity once enforced an unwritten code of conduct:

* Memory was precious — you cleaned up after yourself
* Every cycle counted — you thought before you looped
* Dependencies were earned — you didn’t pull in libraries for trivial tasks
* Abstractions were understood — you knew what happened under the hood

Old systems weren’t magical. They were constrained — and that constraint forced discipline. We’ve traded that discipline for convenience.

The Professional Paradox

Here’s where it gets professionally painful: The system now rewards waste.

If you don’t use the tonne of libraries, cloud SDKs, and abstraction layers that consume resources (and cash) at runtime, you risk being passed over for Developer B who doesn’t care. Developer B is the “deliverer” — they ship fast, consequences be damned!

The metrics are stacked against careful craftsmanship:

* Velocity > Efficiency
* Features shipped > Resources consumed
* Time to market > Technical debt considered
* Framework familiarity > Understanding fundamentals
We’ve created a world where the most “productive” developer is often the one who piles abstraction upon abstraction, dependency upon dependency, until the entire structure becomes so bloated that it requires hardware upgrades just to maintain parity; and inflates cloud costs.

The Cost of Bad Manners

This isn’t just about nostalgia. The consequences are real:

1. Environmental impact: We’re burning megawatts to run inefficient software that does simple tasks
2. Accessibility erosion: Software that requires the latest hardware excludes users with older devices
3. Security fragility: Layers of dependencies create attack surfaces we don’t understand
4. Innovation stagnation: When all our energy goes into maintaining bloat, we have little left for genuine breakthroughs.
The engineers who built C++ on a 2 MB PDP-11 weren’t just clever — they were considerate. They considered the hardware, the next programmer, the user’s resources. That consideration was their professional ethic.

Relearning Our Manners

So yes, we’re losing our manners. But manners can be relearned. It starts with small acts of consideration:

* Question dependencies: “Do I really need this 50 MB library for a simple task?”
* Profile relentlessly: Know what your code actually does, not what you think it does
* Understand one layer down: Know what happens beneath your abstraction
* Advocate for efficiency: Make performance a feature, not an afterthought
The most impressive software isn’t what uses the most resources — it’s what accomplishes the most with the least. That discipline, that consideration, that professional courtesy toward the machine and the user — that’s what we need to reclaim.

Because in the end, software development isn’t just about making computers do things. It’s about how we choose to exist in a world of limited resources. And good manners, it turns out, are just as important in code as they are in life.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (17 comments)


Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse

---
title: Who Here Has Worked with Legacy? The Longer You Wait, the Worse It Gets - DEV Community
url: https://dev.to/sylwia-lask/who-here-has-worked-with-legacy-the-longer-you-wait-the-worse-it-gets-58bk
site_name: devto
content_file: devto-who-here-has-worked-with-legacy-the-longer-you-wai
fetched_at: '2026-06-18T12:19:27.127557'
original_url: https://dev.to/sylwia-lask/who-here-has-worked-with-legacy-the-longer-you-wait-the-worse-it-gets-58bk
author: Sylwia Laskowska
date: '2026-06-18'
description: I promised myself that starting this week I'd switch to lighter topics. But on Monday, my JSNation... Tagged with javascript, webdev, programming, architecture.
tags: '#javascript, #webdev, #programming, #architecture'
---

Safe framework migration tips from JSNation

I promised myself that starting this week I'd switch to lighter topics. But on Monday, my JSNation adventure officially came to an end, and I realized I hadn't written a single article about my talk yet. Since everything is still fresh in my mind, here we go!

As for JSNation itself, I have mixed feelings. I was selected for the online track and, despite the organizers' incredible professionalism, it just wasn't the same as being there in person. You know, I could have been in Amsterdam drinking beer with Wes Bos, but instead I was watching my own talk from the kitchen while replying to Teams messages. 😄 Still, it was a great experience. And who knows? Maybe my expertise, or my level of celebrity status 😅 will grow enough that one day I'll get to speak in Amsterdam in person.

That said, I might visit that beautiful city later this year anyway, but let's not get ahead of ourselves. 😉

Back to the topic. My talk was called"Rewrite or Refactor? How to Safely Move Legacy Apps to Modern Frameworks."I believe I'm the right person to talk about this. Why? Because I've migrated a lot of frontend apps throughout my career, in all kinds of configurations: old Angular to modern Angular, ASP.NET MVC 5 to Vue, React with class components to modern React, and so on.

The reason is simple. If a company desperately needs a migration and suddenly receives a CV from someone who's already done one, they're usually very happy to hire that person—even for a slightly above-market rate. 😄 That's basically how I became a frontend migration expert, and I definitely have a few things to say about it.

## But why migrate at all?

Before discussing strategies, we need to answer a more fundamental question: why migrate in the first place?

I've heard this question many times from stakeholders, especially non-technical product owners. If the application works, why touch it? Developers are just chasing hype and trying to put shiny technologies on their CVs, right?

My answer is usually very simple and honest.

You know me well. I'm not a fanboy of any particular framework. To me, they're just tools. Like hammers. But when I'm building something, I'd rather use a solid, reliable hammer than a rusty one with missing parts. 😉🔨⛏️🪓🔧🪛

But migration isn't just about developer experience. In reality, it's about the survival of your product. Especially today, when technology evolves faster than ever and AI is accelerating everything even further.

Take security, for example. When a library becomes obsolete and nobody maintains it anymore, security patches stop coming. Vulnerability reports start turning red. No product owner in history has ever said, "Sure, let's sacrifice security for a few extra features!" At least I hope so 😅

And let's not forget modern tooling. Vite builds alone can make a huge difference. Modern applications are simply faster, and faster applications are better applications.

There are many more reasons, but the most important thing to remember is this:

The longer you postpone a migration, the harder and more expensive it becomes.

## Okay, okay, I want to migrate. But how?

Interestingly, the arrival of LLMs hasn't fundamentally changed migration strategies. They're basically the same as before AI became mainstream. Sometimes the work is faster, sometimes it isn't, but the underlying approaches remain unchanged.

There are probably as many migration strategies as there are senior engineers, but in practice they fall into two categories:

### Rewrite (Big Bang Strategy)

Rewrite the entire application — or, as often happens on the frontend, upgrade an ancient stack directly to the latest version of the framework.

### Refactor (Strangler Pattern)

Rewrite the application piece by piece while continuing to deliver features.

So, which approach is better?

Honestly, there's no point starting a holy war over this. In most cases, the realities of your project decide for you.

If your application is relatively small, your team is experienced, your documentation is decent, and you can afford to pause feature development for a few weeks or months, a rewrite may be a perfectly reasonable choice.

On the other hand, if you're working on a huge project with lots of junior developers or people unfamiliar with the technology, and the documentation is practically nonexistent — an incremental refactor is probably your only realistic option.

Of course, there are many other factors to consider. Here's a quick summary:

Factor

Rewrite (Big Bang)

Refactor (Strangler)

Application size

Small or medium

Large

Feature development

Can be paused

Must continue

Documentation

Good

Poor

Team experience

High

Mixed

Risk tolerance

Higher

Lower

Time to first results

Short

Long

Complexity during migration

Lower

Higher

Risk of endless migration

Low

High

## Big Bang – Not as scary as it sounds

Let me briefly describe both approaches, starting with Big Bang.

I have to admit — I like this strategy. Sure, books and articles often describe it as risky, sometimes even as an anti-pattern. And they're right — if we're talking about a twenty-year-old Java monolith that nobody dares to touch.

But many frontend applications are relatively young and relatively small. In those situations, a Big Bang approach can simply be faster and cheaper.

Full rewrites are relatively rare these days. However, large upgrades are quite common: for example, moving from Angular 7 to modern Angular with Signals, or from old React with class components to modern React with hooks.

These projects still require a lot of work and a lot of digging through old code, but you'll reach the finish line much faster than with a Strangler migration.

I'm not going to describe planning phases, migration scripts, codemods, or the specific tools I've used. Those details vary from project to project and don't make much sense in a general article.

However, there are certain things that show up with surprising consistency in almost every migration. 😉

## Real-Life Example: Big Bang migration from Angular 7 to latest Angular

Here's an interesting example. Sometimes we wonder how a team could possibly let an application go years without upgrades. In reality, it's surprisingly easy, especially when nobody is actively working on it because the product is in maintenance mode and hasn't changed significantly in years.

That was exactly the case here.

Then one day, the stakeholders decided to expand the application significantly and add several new features. I convinced them to upgrade to the latest Angular version, mainly for security reasons — the system stored critical data.

Long story short, four developers upgraded it to the latest version in four months. And it turned out to be much harder than I expected.

First of all, it's easy to underestimate the scope of the problem. From the outside, it looks simple: "Just upgrade Angular."

But the framework itself is rarely the real problem. The ecosystem around it is.

For example, our primary component library introduced major syntax changes somewhere between versions 12 and 13. Imagine how many places needed to be updated! Sure, AI can help, but if an ambitious UI engineer decides to rename CSS classes and change component structures, AI won't save you — you'll end up fixing things manually.

Some third-party libraries had long been abandoned. And here's something worth remembering:

If you have a library that hasn't been updated in years, whose author has apparently forgotten it exists, and it doesn't even compile on Node 18 anymore, that's not "working code." That's a time bomb.

And yes, we had plenty of end-to-end tests. Many of them exploded because of changes in the component library. 😄 So even automated tests won't always save you.

Another important lesson: always have a solid branching strategy for hotfixes. Assume something will go wrong. Because eventually, something probably will.

Fortunately, the migration was a success.

Build times improved dramatically. The bundle size shrank significantly. The new layout looked much better than the old one, so even the most technology-resistant stakeholders were impressed.

And perhaps most importantly, the application became ready for future upgrades. Even the QA team—which initially hated us, eventually admitted that upgrading regularly is much better than doing it once every seven years 🤣

## Incremental migration – having your cake and eating it too

Sometimes, though, your application is simply too large for a Big Bang approach, or you can't afford to stop delivering features. In that case, incremental migration becomes the only realistic option.

This type of step-by-step refactoring is usually implemented using theStrangler Pattern. There are other approaches, of course, but I personally like this one because it's elegant, relatively simple, and battle-tested by some of the largest tech companies in the world.

So what exactly is the Strangler Pattern?

Take a look at the beautiful diagram below, handcrafted by yours truly in draw.io. 😄

As you can see, you start with your legacy application. You build a new application alongside it. Then you place a reverse proxy in front, which decides which routes go to which application.

From there, you migrate screen by screen, route by route. Over time, the legacy application becomes smaller and smaller until, hopefully, all that's left is the new one, and you can finally get rid of both the old app and the reverse proxy.

In this scenario, both applications should share authentication and the backend, but not frontend code.

And if you absolutely must make the two applications communicate, I'd strongly recommend using something simple like custom DOM events instead of so-called "temporary" adapters.

Because we all know what "temporary" means in software engineering.Forever. 😅 And before you know it, those adapters become a brand-new piece of legacy.

## Real-life example: Migrating from Backbone to Vue with the Strangler Pattern

This was an old application written in Backbone—and I have to admit, it was actually very well written. Still, it was Backbone. 😄

The application wasn't huge, so a Big Bang migration was theoretically possible. But we were a startup, and one day we heard these famous words:"Guys, we just sold a feature that doesn't exist yet. You have three months to deliver it. Have fun!"

My immediate reaction was:"Hahaha. Very funny. There's no way I'm building that in Backbone."Luckily, our stakeholders were smart and agreed to a Strangler migration.

My team consisted of me and... two junior Java developers who, I swear, heard the word "TypeScript" for the first time in their lives.

Fortunately, they were ambitious and learned quickly. Well, they didn't really have much choice. 😄 And that's another advantage of this strategy: junior developers can learn meanwhile.

I created a new Vue application on the side. A lot of people in the company already knew Vue, so the choice was obvious.

First, I migrated the login screen as a proof of concept. Then we moved on to the shiny new feature the client had already paid for. 😉

For the next year, we migrated the application screen by screen.

Eventually, Backbone disappeared completely. And throughout the entire process, we had zero downtime. Customers didn't even notice that a migration was happening.

Just like in the previous example, the bundle became significantly smaller, and build times improved dramatically.

However, the Strangler approach isn't all sunshine and rainbows.

First of all, there's the time factor. The migration process takes a long time. In our case, with a relatively small application, it still took an entire year.

There's also the danger of thenever-ending migration. You probably know what I mean. Deadlines pile up. Features keep coming. And after a while, you find yourself almost begging your product owner to spare a few story points for migration work.

And unfortunately, there's no way to avoid touching legacy code. Zero chance. And believe me, developers hate it. I've heard things like:"Sylwia, why are you making everything so complicated? Now we have to know two technology stacks!"

So no matter which strategy you choose, you'll probably become the team's scapegoat. At least while the migration is in progress.

But once it's over, the bundle size has been cut in half, vulnerability reports stop glowing red, and customers stop complaining, you'll suddenly become the company's hero. 😄

## A Few Final Words

Migrating legacy applications is a lot like buying an old house. It's not your fault that it's falling apart, but it is your responsibility to bring it back into shape. You can take a few weeks off and renovate everything at once, or you can move in and tackle one room at a time.

The only truly bad strategy is doing nothing. Sooner or later, you'll have to migrate anyway — except you'll be doing it because of a production incident. 😉

So, what's your approach to renovating your legacy applications?

### Disclaimer

None of the stories described above actually happened. Or maybe they did? 😉

As both a professional and someone bound by NDAs, I deliberately created a blend of several migration stories to make sure no company or project could be identified. That wasn't particularly difficult, because after a while all migrations start to look surprisingly similar. 😄

If you like my articles, you can also follow me onLinkedIn.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (12 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse
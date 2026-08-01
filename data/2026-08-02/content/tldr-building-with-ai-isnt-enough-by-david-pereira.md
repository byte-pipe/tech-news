---
title: Building with AI Isn't Enough. - by David Pereira
url: https://dpereira.substack.com/p/building-with-ai-isnt-enough
site_name: tldr
content_file: tldr-building-with-ai-isnt-enough-by-david-pereira
fetched_at: '2026-08-02T06:00:30.669585'
original_url: https://dpereira.substack.com/p/building-with-ai-isnt-enough
author: David Pereira
date: '2026-08-02'
description: What you need to remain authentic beyond AI
tags:
- tldr
---

# Building with AI Isn't Enough.

### What you need to remain authentic beyond AI

David Pereira
Jul 30, 2026
7
Share

By now you have many tools that enable you to build an application and put it live in a fraction of time. Claude, Lovable, Bolt, Replit, and many others. They’re terrific, and yet not enough.

Lately I’m stumbling upon more of the same designs and products everywhere. And I almost contributed to that with my new website.

I want to share a full story with you on how you can build with AI with taste and judgement from end to end. This is an honest story, not a tutorial, though you can repeat everything on your own. I will share what worked well, what didn’t, and common mistakes I made, and what to do instead.

## Know why you’re building

It sounds obvious, but whenever you start building something, you should have clarity on what you’re doing that for. Starting points would be:

* Your audience
* What’s in it for them
* What’s your value proposition
* What you know
* What you don’t know

The last two parts are vital, and often ignored. We often know less than we assume, which means we should confront our ideas against reality as fast as possible. Then, decide based on evidence, not opinions.

Back to my example. My website seemed dated, a bit messed up with templates from Kajabi (where I host my trainings), Canva banners, and my copy. It was functional, but lacked authenticity. I wanted a personal website that reflected who I am, and what I stand for. I’m a thought-provoker, who’s optimistic, and hopeful. My energy rises when I help people level up their potential. Within that, I could start.

## Designing

I needed to migrate my website, preserve the content, but transform the experience. But I’m not a designer. Could AI design it for me?

As with product, the website didn’t seem the right place to start, so I decided to start as small as possible. I built a set of infographics with Claude Sonnet 4.6, and I hated everything about it. They didn’t look like me, but looked like most of the LinkedIn posts I see. Then, I switched to Opus, that’s when I got to something I liked.

First, I wanted to diverge and explore multiple options, collect feedback, and see what resonated before iterating. I knew the design wasn’t what I wanted, but hiding it from people wouldn’t help me iterate it.

I shared them to collect impressions and resonance.Here are some samples of how it looked at a high level:

The fourth option landed better with me and my audience, but something still felt off. I was seeing too much dark background with orange font already. I chose not to solve it at that moment, and went on exploring my website design. For that, I used Claude Design with Opus 4.8. I first designed the home page, and then iterated from there. This part is important, start small, don’t go for everything immediately.

As I got the first design ready, it looked cool, but it felt off. The words were mine, but the design not.

Here’s how it looked.

Even though I wasn’t convinced, I shared it with a few people. I got comments like:

“Wow. This is awesome. The words, the design, and the style.”

“Nice, but missing YOUR brand.”

“Cool. But kind of missing a soul.”

“Beautifully structured and polished.”

The last one got me thoughtful because it was too polished, too standard, and missing the hands-craft. I knew AI wouldn’t do that for me unless I’d step into it.

It was time for me to reflect on how to make it authentic, and not look like somebody else’s website. As a person, I’m structured and messy at the same time. Breaking things is necessary to bring the right foundations. As I stepped back and reflected on things that are my brand, clarity arose. Thought-provoking, personal touch, simplicity, and audacity. But how could I add that?

Writing is my thing, I get joy from that. And people love when I “cut the crap” and make the important things clear. In workshops I do that with simple handwriting. That’s when things clicked, I had to tweak it to my style so it reflected me.

Within that, I went back to Claude Design and tried to iterate. I must confess that I almost freaked out with the first weird designs I got, but after several iterations, I got to something that related to me.

This version enticed me, and got stronger resonance from my audience.

“That’s you. The hand-written touch is great.”

“Yes. I love the authenticity and sometimes unstructured sections.”

“It shows me you’re human and approachable.”

From that, I was ready to start building, and I wish I had done that better. Let me tell you how I screw up before I got it right.

Key lesson:The first design options will look ordinary. You have to know what you stand for to make it stand out. Diverge, and converge until you get what speaks to you and your audience.

## Building

I’ve been reading about specs driven development, which I don’t agree with, but decided to give it a try to see the results. The idea, is that you share what your application should do, and then write the “PRD” with AI. Then, AI agents will code for you based on the specs.

As Claude Design crafted the visuals for me, it seemed like a natural step to use Claude Cowork for the specs. I prompted, Claude asked a few questions, and voilà, the document was ready, and honestly quite solid. At this moment, I had a deja-vu feeling because earlier in my career I wrote such documents, and the results weren’t the best. Anyway I continued the experiment.

I first created my repository in GitHub, then an application on Google Firebase, followed by a storage and database (I like having everything in one place). Within that, I started VS Code with Claude extension, uploaded the specs, and prompted to create a plan. For that, I used Sonnet 4.6, and again, the plan was sound, so I approved to execute with automatic updates.

As it included the CMS, design system, several pages, and functions, it took around half an hour or so to conclude. Now, what do you think happened?

Maybe you’ve seen that already. Expectations and reality went in completely different directions. The built website had little to do with the design, and the interactions were rough and anything but nice. I clearly did something wrong. After, I talked to my brother, who had just built a whole end to end application, I got valuable insights.

1. Forget about specs, go bit by bit.
2. Use stronger models for architecture, and weaker ones for execution.
3. Instead of implementing the website, ask Claude Code to evaluate the output from Claude Design, create the design system and components.
4. With the design system ready, implement one single page.
5. Iterate the page components until it matches what you expect.

These five steps transformed everything. I needed a reset the application because the first attempt just burned tokens and created crap. You’ve got to go bit by bit. It’s kind of using software engineering practices for that. The bigger the scope of your prompt, the more surprising your output can be. I cleared the repository and started over.

Such iterations take some time, I did try building first with Claude Pro because I had an assumption that could be enough for most PMs. I hit the wall every hour and had to wait for my next window. This broke my flow, but I had other things to do so I switched. Eventually, I got disturbed and upgraded to Claude Max, and concluded the website implementation in about a day. Yes, it wasn’t hours because I found many glitches and wanted to fix the iterations before testing with more people.

Key lesson:First the foundations of your application, then the rest. This way you can keep it consistent.

## Shipping (And Breaking Stuff)

After getting the core pages finalised, I wanted to release the website to a few people. It still missed the blog, contact form, and some other parts, but I had enough to show. By this time, I had already collected loads of feedback and iterated, so it was more like a confirmation.

As I presented to people, it landed well. The new design, and website immersive experience worked nicely. The hammer came with speed and some flickering menu on iOS, which I could iterate and fix it.

The great thing about Claude Design and Claude Code is that you can quickly iterate, and ship live fast. This is something I appreciate about it.

And then an unpleasant surprise came. “David, your app secrets are exposed.” A software engineer sent this message to me. Which was true, my application security was rather weak, which I rushed to fix.

First, I used Sonnet 4.6 to fix the security vulnerabilities, which it did, but then it crashed other things. My lead magnets stopped working, and the CMS broke. When that happens, it’s better to start a new chat and use a stronger model, which I did with Opus 4.8 (high effort selected), and the results were great. Everything fixed, but I pressed one “Yes” without reading it properly, and I hated myself after that because it re-seeded the content, and everything I adapted was gone.

There I was staring at an outdated version of my new website. At some point, I learned that as adults we can be pissed off, but not for long. So I picked my guitar for a bit, and played Symphony of Destruction by Megadeth, 5 minutes after, I was chilled and fixed my own mess.

## Iterating (And breaking More Stuff)

After I cleaned up my mess, I wrapped up for the day, and decided to continue the next day. I still had my blog to put there, contact form, and 100XPM page, application, and quiz. I kept the lesson in my mind, step by step. Slow is fast.

I had a few rounds of:

1. Claude Design until I like what I see.
2. Claude Code, first components, then feature.
3. Claude Code, ships to dev, I test, and iterate.
4. Merge to master, and Firebase deploy live.

And then, guess what happened?

My e-mail stopped working. Yes, contact@d-pereira.com stopped receiving e-mails. And I realized that just 15 minutes before a pregnancy photo shooting with my wife. I had to breathe 10x to calm down because I knew I’d be out for the next four hours, and the photo shooting mattered more than fixing my e-mails.

I won’t deny that I thought a few times about what I’ve done. Probably I messed up with the DNS with Claude Cowork, or something like that. I did worry about not receiving a few key e-mails from companies I was negotiating with. But, I convinced myself to worry about it later.

After the photo shooting, I was starving, and eager to go back to my computer. I chose to feed my wife and myself. As hunger got out of the way, I checked out what I messed up with. Obviously Claude Cowork and I removed a DNS entry we shouldn’t have. It was an easy fix, and a few minutes later, several e-mails kicked in. Phew, relieved.

The website is now live and doing its work. You can check the current versionhere. The old version is dead for good, you cannot see it anymore :)

## Measuring

The website is live for a few weeks now, and it’s not just a more beautiful design, it’s a more effective platform. I knew the metrics I wanted to improve, and it’s already happening.

Since last year, I’m on my own, figuring out my path forward. I do that with advisory, workshops, keynotes, and the 100XPM. And I can only make it work once I get requests, people apply for my mastermind and so on.

I assumed that a stronger message, and solid content would create more leads, more applications, and then it’d be my job to make the conversion.

The numbers improved more than I expected. Apparently my old website was playing against me, not in my favor. I continuously measure the metrics that matter to me, and then I strive to understand what’s going on before just building stuff. And that’s the job of any product person. Judgement, taste, and making the hard decisions.

## Lessons

My real journey doesn’t make a nice LinkedIn post. I cannot write - This is how I transformed my pipeline in a few minutes with AI. That’s not what happened.

From the moment I decided to build to the real go-live, it took almost four weeks. Yes, you can call me slow, or whatever you choose. I’m still classic. I first iterated my infographics, tested them with real people, made a few posts on LinkedIn and learned what landed and what flopped. Then, I iterate. And something takes a few days to get signs beyond noise.

Designing requires your taste more than anything. I had finished my website quickly, but I felt blocked to put it live because it didn’t feel like me at all. Figure out what you stand for, what’s your product about, and then progress. Take your time because this part matters.

Building should be step by step. The specs driven stuff didn’t work for me. Maybe I did it incorrectly, but I don’t care. I don’t like long documents and I don’t believe in them. The collaborative and interactive approach ended up in a better result.

You will break things in weird moments. Maybe out of tokens, or in a moment you have other commitments. Know what matters most for you. I follow the principle of happy wife, happy life to the bones. Fixing stuff requires focus and 100% of your attention, not just prompting wildly while doing five other things.

After this small experiment with my website (not the first thing I built with AI, but the first I had a strong connection with), I realized that PMs are heavily needed. But the PMs that are the most needed aren’t the ones that master AI, but the ones that master product management itself.

The tools themselves you’ll learn quickly. They’re easy, no big deal honestly. You’re smart, you will get it well enough within days or weeks. Yet, the craft of product management takes more time to sharpen it, and that still matters most.

That’s it for this episode. I hope you got insights to apply to your station.

See you next week.

## Are you the PM the market needs, or the one that gets ignored?

Many PMs today are uncertain about what matters, and then try becoming the AI PM, yet to be ignored. AI may help you, but not alone. The PMs that get paid 6-figures are the ones with a solid operating system combined with a powerful mindset. And that’s something you can learn.

I was the ignored product person for a while. After learning what clicks with the market, I grew in my career a lot. From PM to CEO in five years. This is what I teach in my mastermind, the100XPM. We’ll open enrolment next Monday.

Apply now if you want to become the PM the market needs.

Let’s untrap the product world together.

Talk soon,

David Pereira100XPM Coach

7
Share
Previous
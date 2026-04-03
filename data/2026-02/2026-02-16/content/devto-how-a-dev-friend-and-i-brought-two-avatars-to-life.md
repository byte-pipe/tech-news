---
title: How a DEV Friend and I Brought Two Avatars to Life - DEV Community
url: https://dev.to/itsugo/how-a-dev-friend-and-i-brought-two-avatars-to-life-chp
site_name: devto
content_file: devto-how-a-dev-friend-and-i-brought-two-avatars-to-life
fetched_at: '2026-02-16T19:17:45.037858'
original_url: https://dev.to/itsugo/how-a-dev-friend-and-i-brought-two-avatars-to-life-chp
author: Aryan Choudhary
date: '2026-02-16'
description: I met @webdeveloperhyper on the DEV Community, and like most good internet collaborations, it started... Tagged with webdev, sideprojects, animation, react.
tags: '#webdev, #sideprojects, #animation, #react'
---

I met@webdeveloperhyperon the DEV Community, and like most good internet collaborations, it started casually.

A few messages. Some feedback. Valuable guidance.

Then at some point, the conversation shifted from “this looks cool” to “let’s make something fun together.”

We didn’t over-plan it. We just started building.

They were in Japan. I was in India. Which meant most of this project happened in small pockets of time. Late nights. Random 20-minute windows during the day. Messages sent hours apart. Progress that didn’t look dramatic, but quietly accumulated.

Somehow, it worked.

## From basic shapes to actual avatars

The projectdidn’t begin with polished characters. It began with simple shapes in a scene, just placeholders to test positioning, camera, and basic interaction.

The idea was simple. Two characters. A short conversation. Some animation.

Simple ideas tend to hide interesting problems.

My first real task was creating the avatar itself using VRoid Studio. That alone was a learning curve. Once imported, the avatar didn’t behave like a character. It behaved like a static object.

The default pose was a T-pose. Arms stretched out. Completely lifeless. Fixing that was thefirst small victory. Getting the avatar into a neutral stance, hands down, just standing naturally.

It sounds minor. But that was the moment it stopped looking like a model and started looking like a character.

From there, we began layering gestures.

Hello animations. Goodbye animations. Small movements during conversation. Even a sigh animation that became one of my favorite details.

There was also a failed attempt at overriding default gestures directly, which taught me very quickly that animation systems have their own rules.

## Writing the conversation was harder than expected

Surprisingly, one of the hardest parts wasn’t technical. It was writing the conversation itself.

Short. Natural. Slightly funny. Not robotic.

When dialogue is too long, it feels forced. Too short, it feels empty. Too serious, it loses charm. Too silly, it loses believability.

Finding that balance took more iterations than expected.

I still think the punchline could be better. But maybe that’s a good thing, leaves room for evolution.

## When rendering avatars becomes a systems problem

Rendering avatars is straightforward with modern tools. The real challenge was orchestrating behavior.

We needed the scene to manage:

• who speaks• what animation plays• when it starts• when it ends• when the next character takes over

So instead of hardcoding behavior, we defined dialogue as structured data:

const

DIALOGUE

=

[


{


speaker
:

"
A
"
,


text
:

"
I'm Web Developer Hyper. I like to make fun things.
"
,


animation
:

"
VRMA_03_peace_sign.vrma
"
,


},


{


speaker
:

"
B
"
,


text
:

"
Hello! I'm Itsugo. And I like turning ideas into something real.
"
,


animation
:

"
VRMA_04_shoot.vrma
"
,


}

];

Enter fullscreen mode

Exit fullscreen mode

The scene simply interprets this sequence. This separation made the system easier to control, extend, and reason about.Instead of forcing behavior, we orchestrated it.

## The coordination problem

Animations don’t naturally tell your application when they finish.

But timing matters. The next line shouldn’t interrupt too early. And the system shouldn’t freeze if something goes wrong.

So the dialogue system waits for either:

• animation completion• or a safe timeout fallback

Whichever happens first.

This tiny decision made the system resilient.

Small systems thinking like this often matters more than large features.

## You can check it out here!

## The invisible part of collaboration

What made this project meaningful wasn’t just the final result. It was the process.

Fixing animation timing. Cleaning unnecessary code. Improving readability. Adjusting gesture intensity. Adding beginner-friendly comments.

And doing it across timezones.

Huge thanks to@webdeveloperhyperfor setting up the foundation, pushing the project forward, and tolerating my questionable Japanese during our conversations.(ˉ▽ˉ；)...

This project exists because of that shared effort and patience.

## Where this could go next

Right now, it’s just two avatars having a conversation.But it already feels like the beginning of something larger.

Interactive characters. Story systems. Dynamic dialogue. Maybe something we haven’t even thought of yet.

And that brings us to the real question.

How should we take this forward?

We have some ideas where this could go next, but we want to hear from our awesome followers.

How would you have fun with this project?No matter how unrealistic it might sound.Let’s have some fun with this side project.

## Closing

This started as a small experiment between two developers who met online.It became a reminder of why side projects matter.Not because they are perfect.But because they are alive.

And sometimes, that’s enough to start something meaningful.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (28 comments)


For further actions, you may consider blocking this person and/orreporting abuse

---
title: Anki On My Wrist - DEV Community
url: https://dev.to/matheusmaldaner/anki-on-my-wrist-3gi6
site_name: devto
content_file: devto-anki-on-my-wrist-dev-community
fetched_at: '2026-03-20T19:19:35.874353'
original_url: https://dev.to/matheusmaldaner/anki-on-my-wrist-3gi6
author: Matheus Kunzler Maldaner
date: '2026-03-18'
description: I've long been interested in "learning how to learn" and have long been annoyed by how I have grown... Tagged with learning, productivity, showdev, ai.
tags: '#showdev, #learning, #productivity, #ai'
---

I've long been interested in "learning how to learn" and have long been annoyed by how I have grown to forget things -- which is not a great sign for a 24-year-old. That, combined with how I, and several of my friends, have grown dependent on our phones over the years, has led me to create a system to better learn, memorize and remember things long term without necessarily needing your phone.

## Flashcards

I remember using Quizlet extensively throughout high school since it was pseudo-required for many subjects, but that practice did not follow in college where most classes in my Data Science program required either coding or math, neither of which you would immediately connect to flashcards or memorization at first glance. I noticed throughout the years that it would be hard to recollect certain memories, whether that be with names of people, facts about certain subjects, or simply things I had definitely learned but could no longer recall.

So as one does, I made my own app with their native programming language called MonkeyC.

## The Prototype

Garmin VivoActive 6 with Anki Prototype

When I won first place at UF AI Days Hackathon, we were given the choice of a $300 tech-related item. I got a Garmin VivoActive 6 despite not running that much, as I was kind of obsessed with my sleep and staying off my phone at that time, and that seemed like a good choice -- plus I could leave my phone outside of my room and set alarms on my watch.

Going back to the flashcards, I was also excited to install Anki on my brand new Garmin and review my flashcards on my wrist whenever I was walking or showering or doing just about anything else.

## Anki on My Wrist

Well, that was short lived. I did not find a downloadable Anki app for Garmin, or any public implementation of how to get Anki on your Garmin. So as one does, I made my own app with their native programming language called MonkeyC, installed the AnkiConnect add-on to enable programmatic HTTP calls, exposed my computer via an ngrok tunnel, realized Garmin expects API calls to be HTTPS, recreated their API system with FastAPI and a Cloudflare tunnel, and went through many iterations by refusing to use Windows' native Garmin plugin and using WSL2 instead. Once done, my watch could fetch, review and sync cards both ways with my Anki account.

## Is Your Laptop On 24/7?

As you may have picked up, this setup does require my laptop to be turned on for the tunnel to be exposed, and when I do want to use my watch's app I am typically walking with my laptop happily closed and/or without wifi in my backpack. This was recently solved by getting one of the free Oracle VMs and moving all of my workflow to be inside the VM.

This VM does not have that much RAM -- well there is one better Oracle free VM, but that is typically always taken. I wrote a script to keep trying to select the better free version once it became available across all 3 available regions, and the script ran for 2 days with no luck.

### System Architecture

## More Issues

A Garmin, not surprisingly, does not have that much memory dedicated to third-party apps, so once my decks grew in size -- or the one time I forgot to review cards by being too busy making the workflow instead of reviewing them -- pressing sync overloaded the watch and crashed the app. The fix was paginated sync: fetching 10 cards at a time instead of the full deck, and eliminating intermediate data copies that tripled memory usage.

## Even More Extensions

A separate issue I had was with note taking. I've used NotePad, Obsidian, OneNote, even a server with myself on Discord or a groupchat by myself on WhatsApp. I really liked Obsidian and used it for quite some time, but something that always annoyed me was having to alt-tab between whatever I was doing or relying on a separate monitor. This led me to create a super simple, lightweight AutoHotKey script that spawns a toggleable overlay.

I quickly expanded this small tool, adding a pomodoro timer, a feature that locks your screen in the current tab since I tend to sidetrack and do many things at once, an article clipper as I read many articles and lose track of what I read or where I found certain info later, and finally compatibility with my flashcards since I had already defined the API endpoints.

I integrated Claude into it by adding a notes-to-flashcards button (you can choose which cards you approve), and also this fun functionality where it proposes bridges between certain cards -- for example, you could have the cards "Neural Networks" and "Symbolic Programming" and the bridge system may propose "Neurosymbolic AI" as a bridge term that connects them.

Once again, once you have the API endpoints, you can integrate this into almost anything. I used ChatGPT Actions to create an "AnkiGPT," allowing me to review my cards via ChatGPT -- which also works with voice mode, letting me do my flashcards while driving on the highway.

## Project Timeline

* Nov 2025-- v1: basic Garmin watch app with sample cards, tap/swipe UI
* Dec 2025-- FastAPI bridge with deck listing, card fetching, review submission
* Dec 2025-- Cloudflare tunnel deployment -- anki.matheus.wiki goes live
* Dec 2025-- AnkiGraph: LLM analysis, knowledge graphs, Obsidian export
* Jan 2026-- Landing page with drag-and-drop multi-format card import
* Mar 2026-- 24/7 Oracle Cloud VM deployment with headless Anki

## Overreliance

As with all things, balance is important. Memorization without understanding, especially in a field like Machine Learning, may harm you as you may be unable to form new connections or generalize to new terms. The system I've built is a tool, not a replacement for deep thinking. But when you need to remember that one professor's name, or the year a paper was published, or the flags for a CLI tool you use twice a month -- having it on your wrist is genuinely useful.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
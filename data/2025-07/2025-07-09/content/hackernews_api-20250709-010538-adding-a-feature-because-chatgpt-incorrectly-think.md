---
title: Adding a feature because ChatGPT incorrectly thinks it exists | Holovaty.com
url: https://www.holovaty.com/writing/chatgpt-fake-feature/
site_name: hackernews_api
fetched_at: '2025-07-09T01:05:38.430889'
original_url: https://www.holovaty.com/writing/chatgpt-fake-feature/
author: adrianh
date: '2025-07-08'
description: Adding a feature because ChatGPT incorrectly thinks it exists
tags:
- hackernews
- trending
---

# Adding a feature because ChatGPT incorrectly thinks it exists

Written byAdrian Holovatyon July 7, 2025

Well, here’s a weird one.

At Soundslice, oursheet music scannerdigitizes music from photographs, so you can listen, edit and practice. We continually improve the system, and I keep an eye on the error logs to see which images are getting poor results.

In the last few months, I started noticing an odd type of upload in our error logs. Instead of images like this...

...we were starting to see images like this:

Um, that’s just a screenshot of a ChatGPT session...! WTF? Obviously that’s not music notation. It’sASCII tablature, a rather barebones way of notating music for guitar.

Our scanning system wasn’t intended to support this style of notation. Why, then, were we being bombarded with so many ASCII tab ChatGPT screenshots? I was mystified for weeks — until I messed around with ChatGPT myself and got this:

Turns out ChatGPT is telling people to go to Soundslice, create an account and import ASCII tab in order to hear the audio playback. So that explains it!

Problem is, we didn’t actually have that feature. We’ve never supported ASCII tab; ChatGPT was outright lying to people. And making us look bad in the process, setting false expectations about our service.

So that raised an interesting product question. What should we do? We’ve got a steady stream of new users who’ve been told incorrect facts about our offering. Do we slap disclaimers all over our product, saying “Ignore what ChatGPT is saying about ASCII tab support”?

We ended up deciding: what the heck, we might as well meet the market demand. So we put together a bespokeASCII tab importer(which was near the bottom of my “Software I expected to write in 2025” list). And we changed the UI copy in our scanning system to tell people about that feature.

To my knowledge, this is the first case of a company developing a feature because ChatGPT is incorrectly telling people it exists. (Yay?) I’m sharing the story because I think it’s somewhat interesting.

My feelings on this are conflicted. I’m happy to add a tool that helps people. But I feel like our hand was forced in a weird way. Should we really be developing features in response to misinformation?

---
title: Someone hacked the freezers at 400 French supermarkets - DEV Community
url: https://dev.to/peter/someone-hacked-the-freezers-at-400-french-supermarkets-5flm
site_name: devto
content_file: devto-someone-hacked-the-freezers-at-400-french-supermar
fetched_at: '2026-10-16T15:12:16.717792'
original_url: https://dev.to/peter/someone-hacked-the-freezers-at-400-french-supermarkets-5flm
author: Peter Kim Frank
date: '2026-10-13'
description: 'Friends ask me some version of this a lot: how would a bad actor with super powerful AI actually hurt... Tagged with news, security, ai.'
tags: '#news, #security, #ai'
---

Outdated industrial software risks physical chaos

Friends ask me some version of this a lot:how would a bad actor with super powerful AI actually hurt anyone in the real world?

It usually comes with some skepticism. The All-In Podcast guys have talked about this and tend to wave it off as a straw man, like everyone concerned is picturing the Terminator.

So here is a much more mundane example from this week.

## What happened

The New York Times reportsthat a cyberattack hit the refrigeration systems of more than 400 supermarkets in France. That is about 300 Intermarché and Netto shops, 80 from Coopérative U, and 30 from Monoprix.

The attackers went after the software that lets refrigeration companies control the fridges remotely. Some shops had to throw out all of their fresh and frozen food. The head of Coopérative U said a failed system can cost a small supermarket tens of thousands of dollars, and a hypermarket roughly $220,000.

Nobody has claimed responsibility. Danfoss, one of the companies that makes these systems, said the affected ones were often outdated and no longer received security updates.

## This is definitely not the first time

Software has been breaking physical things for a while now:

* Stuxnet, discovered in 2010, destroyed roughly a thousand uranium centrifuges in Iran.
* InDecember 2015, attackers cut the power to about 230,000 people in Ukraine.
* In 2021, ransomware hit the business systems atColonial Pipeline. The company shut the pipeline down, and gas stations across the US Southeast ran dry.

## Why this one sticks with me

Stuxnet took a nation-state budget and years of work. The freezers took an old controller that was reachable from the internet.

To be clear, nothing reported so far says AI had any part in this attack. It didn't need one, and that is why it is a useful example.

An attack like this is mostly patient, tedious work. Someone has to find the exposed devices, read through old firmware, and work out which setting does the damage. Today the limit on attacks like this is how many skilled people want to do it, and how much time they have. Patient, tedious work across a long list of targets is exactly what AI models are getting good at.

And the world is full of freezers. Building HVAC, water pumps, parking gates, the fridge at your pharmacy. Nobody thinks of these as targets, so they run old software with remote access switched on.

So when a friend asks what a bad actor with powerful AI could do, my answer has no robots in it. It looks a lot like this week in France, at more places, more often, and from people who couldn't have pulled it off on their own before.

What is the most boring internet-connected thing at your work that would cause real trouble if someone turned it off?

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
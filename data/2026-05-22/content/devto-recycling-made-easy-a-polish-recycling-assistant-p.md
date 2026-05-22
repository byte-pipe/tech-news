---
title: 'Recycling made easy: a Polish recycling assistant powered by Gemma 4 - DEV Community'
url: https://dev.to/klaudiagrz/recycling-made-easy-a-polish-recycling-assistant-powered-by-gemma-4-j0a
site_name: devto
content_file: devto-recycling-made-easy-a-polish-recycling-assistant-p
fetched_at: '2026-05-22T11:58:12.095287'
original_url: https://dev.to/klaudiagrz/recycling-made-easy-a-polish-recycling-assistant-powered-by-gemma-4-j0a
author: Klaudia Grzondziel
date: '2026-05-21'
description: 'This is a submission for the Gemma 4 Challenge: Build with Gemma 4 I clearly remember this scene: my... Tagged with devchallenge, gemmachallenge, gemma, webdev.'
tags: '#devchallenge, #gemmachallenge, #gemma, #webdev'
---

Gemma 4 Challenge: Build With Gemma 4 Submission

This is a submission for theGemma 4 Challenge: Build with Gemma 4

I clearly remember this scene: my mom and I are dyeing our hair together. I'm holding a small plastic bottle that still has some dye inside, and I'm asking myself: where the hell do I throw this? I ask my mom – she has no idea either. Plastic bin, even though the bottle is contaminated with dye? Or is it mixed waste now?

Sorting waste in Poland has improved a lot over the last few years. The system is based on six colourful bins that you'll see in any backyard:

Bin

Color

What goes in

PLASTIC/METAL

🟡 (yellow)

plastic bottles, cans

PAPER

🔵 (blue)

paper, cardboard

GLASS

🟢 (green)

glass jars, bottles

BIO

🟤 (brown)

food scraps, garden waste

MIXED

⚫ (black/grey)

mixed waste: contaminated or composite items

TEXTILE

🟣 (violet)

clothes, shoes (separate collection mandatory since Jan 2026)

Obvious stuff like cardboard or an old pair of socks is easy. But there are traps – you can't throw an old mug or a broken mirror into the glass bin, even though it seems to be the right choice. And then there's the hair dye bottle with dye still inside. The pizza box with grease on the bottom. The blister pack from your pills.

Real debates are happening on the Polish internet about this stuff. Type "gdzie wyrzucić..." into Google and you'll see how much people struggle. I once watched two friends argue about where a used coffee cup goes — one swore it was paper, the other said mixed waste because of the plastic lining.

Confusing? Hell yeah, it is! 😩

## What I Built

That's why I built a web app calledGdzie to wyrzucić?[ENG: Where to throw it?]. It's a Polish recycling assistant – you take a photo of an item with your camera and send it to a Gemma 4-backed AI assistant. As a response, it tells you which bin the waste goes in.

The photos are not stored anywhere – they are processed in-memory by the API route, sent to Gemma 4 for analysis, and discarded immediately after the response is returned.

The recycling rules live in a ~200-linesystem prompt. What you see now is v4 – there were a lot of iterations and a lot of live testing along the way. At this point, my entire phone gallery has turned into one big collection of trash photos 🙈 And my neighbours probably think I've gone nuts, because I keep photographing "interesting" items from the backyard bin to see how Gemma will handle them 😅

The app is Polish-only by design – Polish recycling rules apply to people in Poland, and the system prompt is built around Polish categories. I'm planning to add English and Ukrainian translations, though, because there are minorities living in Poland who could really use this, too. Until then, I hope the app is intuitive enough for a non-Polish speaker.

## Demo

To test the project, go toGdzie to wyrzucić?. The walkthrough is as follows:

1. Take a photo of the wasted item or choose one from your gallery. Press theAparatorGaleriabutton, respectively.
2. ClickAnalizujand wait ~15-30 seconds to get the sorting result. Alternatively, clickZrób ponownieif you are not satisfied with the photo and want to retake it.
3. The app returns the answer to which bin you should throw your waste, together with the explanation and some additional remarks (if any).
4. If you want to try another waste item, pressSprawdź inny przedmiot.

For the English-speakingdev.tousers, I prepared a walkthrough video with some explanation:

## Code

All the code lives in therecycling-apprepository on GitHub.

At this point, let me be honest with you – I vibe-coded this. I am a Technical Writer, not a Developer, and even though I have experience with git and done some small code updates in the past, this is the first bigger project I've built myself.

It was a multi-agent work. I used Claude Code for the boilerplate code and for turning business logic into reality. I used Gemini's deep search to dig up current recycling rules from Polish government sources and eco-experts. I was the brain behind everything else – the idea, the business logic, the testing, the improvements, leading each next step, holding it all together. And Gemma is the heart of the project 💛

## How I Used Gemma 4

The app sends the photo to Gemma 4 with adetailed system promptthat encodes the current Polish recycling rules. Gemma looks at the image and returns a structured JSON: which bin, how to prepare the item, an explanation, and an extra note if relevant. The frontend turns that into a result card in the right bin colour.

I went withGemma 4 26B Mixture-of-Experts(gemma-4-26b-a4b-it) via Google AI Studio's free tier. The MoE architecture only activates around 4B parameters per token out of ~26B total. It's efficient enough to run on the free tier and smart enough to handle the actually hard cases.

The free tier means the demo runs 24/7 without costs. And because Gemma is open-weights, the same app could one day ship with Gemma 4 E2B or E4B running directly on the user's device. That's a path I'd like to explore.

## Known limitations

Thetest phaserevealed that some photos trigger an immediate error before Gemma is even reached. The failing photos share the same characteristics: detailed scenes, multiple objects, busy compositions, and possibly larger file sizes than simple isolated-item photos. I think that the issue is about image size or encoding, but I need to confirm it yet.

Also, analysis takes 10–15 seconds. Free-tier cloud inference is slow. It is acceptable for the initial phase and the challenge, but I'd need to think about some other options in the future.

## What's Next

The roadmap is in theissue tracker. A few highlights:

* Multilingual support for English and Ukrainian – many Ukrainians have moved to Poland in recent years, and there are also exchange students and expats living in Poland who would find an English translation handy.
* Interactive clarification – when Gemma isn't sure what's in the photo, let it ask the user a yes/no question instead of guessing.
* Suggesting reuse before recycling for books, clean clothes, working electronics, old furniture, and so on. Recycling is good. Reusing is better.

## Closing sentence

If you're in Poland, try outGdzie to wyrzucić?. If you spot a misclassification or a rule the app gets wrong, please open an issue – I'd love to keep improving it.

Thanks to thedev.tochallenge for the deadline, to my colleagues and friends who tested the app, and to Gemma 4 for actually making it all happen 💛

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (28 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse
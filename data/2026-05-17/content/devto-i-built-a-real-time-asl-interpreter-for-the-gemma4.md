---
title: I built a real-time ASL interpreter for the Gemma4 challenge, no cloud needed - DEV Community
url: https://dev.to/cbms26/i-built-a-real-time-asl-interpreter-for-the-gemma4-challenge-no-cloud-needed-5gdj
site_name: devto
content_file: devto-i-built-a-real-time-asl-interpreter-for-the-gemma4
fetched_at: '2026-05-17T19:29:32.642473'
original_url: https://dev.to/cbms26/i-built-a-real-time-asl-interpreter-for-the-gemma4-challenge-no-cloud-needed-5gdj
author: Ngawang Tenzin
date: '2026-05-17'
description: 'This is a submission for the Gemma 4 Challenge: Build with Gemma 4 What I Built A... Tagged with devchallenge, gemmachallenge, gemma, opensource.'
tags: '#devchallenge, #gemmachallenge, #gemma, #opensource'
---

Gemma 4 Challenge: Build With Gemma 4 Submission

This is a submission for theGemma 4 Challenge: Build with Gemma 4

## What I Built

A real-timeAmerican Sign Language (ASL) alphabet interpreterthat runs 100% on your own machine - no api key, no cloud, no subscription. Hold up your hand showing a sign-lan in front of your webcam, hit capture, and Gemma4 tells you which letter it thinks it sees, how confident it is, and what it notice about your hand position.

The pipeline design is:Webcam -> MediaPipe (hand detection + cropping only) -> Gemma4 does the hard work (i.e., ASL recognition) -> Result

Repo + setup:[https://github.com/cbms26/asl-interpreter]

## Why this, and why Gemma4:e4b

Most ASL recognition tools out there either need a cloud API or have rely on a dedicated sign-language model pre-trained specifically on ASL datasets. Both approaches have real trade-offs; one cloud APIs mean your hand gestures are going to some server, and secondly, a purpose-built model means you're stuck with whatever letters it was trained on.I wanted to see how well a general purpose vision model like Gemma4 couldhandle ASL recognition just by being given a good specific-description of what each letter looks like. No fine-tuning, no dataset, just programmatic prompting. And everything had to run locally because privacy matters (esp. when your webcam is in use).

I went withgemma4:e4bspecifically. E2B was too small to handle thesubtle differences between similar letters. The 31B Dense model is greatbut won't run on most people's laptops. E4B hit the sweet spot — capableenough to reason about fine hand shapes, light enough to run locally.

## The one design decision worth explaining

The obvious approach is sending the raw webcam frame to Gemma 4 and askingit to identify the sign. That works, but accuracy is noticeably worsebecause the model splits its attention between the hand, the background,the face, the lighting, and everything else in frame.

The fix was addingMediaPipeas a pre-processing step. It runs in thebrowser at ~15fps, detects the hand, and crops a tight (512×512) squarearound it. That cropped image, hand only, nothing else - is what Gemma4actually sees.MediaPipe handleswhere the hand is. Gemma 4 handleswhat letter it is. Separating those two jobs made the biggest accuracy difference of anything I tried.

## Prompt engineering did real work here

Gemma 4 had no ASL training. To make up for that, I wrote precise specific-descriptions of all 26 letters and explicit disambiguation rules for the pairs the model kept getting confused:

"A vs S: In A the thumb is BESIDE the index finger. In S the thumb isfolded OVER the knuckles.""M vs N vs T: All involve fingers folded over the thumb.M = 3 fingers, N = 2 fingers, T = thumb between index and middle."

Writing those out forced me to actually understand the signs properly.And it worked - the confused-pair accuracy improved significantly oncethe model had explicit rules to fall back on. No fine-tuning needed.

## How I measured it (not just vibes)

I didn't just demo the app and call it done. I built a proper evaluationpipeline:

1. Extract frames from an ASL tutorial video
2. Let Gemma 4 auto-sort them intotest_signs/<LETTER>/folders
3. Runbatch_tester.pyto measure per-letter accuracy with ground truth

Every interaction — webcam captures, batch runs, model sorts — getsappended to a timestamped CSV log. The webcam UI also has a thumbs-up/thumbs-down feedback button. If the model is wrong, you pick the correct letter from an A-Z picker so the log captureswhatit got wrong, not justthatit got it wrong.

Results so far:folder 1 got created due to model thinking letter D sign as 1 - interesting

Summary report:

* Total images: 66
* Overall: 59.1%
* Best letters: B, D, E, F, G, H, K, R, T, U, X, Y, Z -> 100%
* Worst letters: I (0%), O (0%), P (0%), V (22%)

During live webcam testing, the built-in feedback captured 15 sessions - 3 correct (thumbs up) and 12 incorrect (thumbs down with the actual letter logged). Common webcam misidentifications included O predicted instead of A, C, or E, and blank/low-confidence responses on letters like D and F.

## What surprised me

The hardest letters aren't the ones I expected. J and Z both involvemotion in real ASL - J traces an arc, Z traces a Z shape in the air.In a still image they look almost identical to I and A. Gemma 4 actuallyhandles this well by flagging them aslowconfidence rather thanguessing confidently wrong. That's the honest answer.Clean input also mattered more than prompt length. The biggest accuracy jump came from cropping with MediaPipe and clear background, not from making the prompt more detailed.

## Demo

Short demo walkthrough -Goes to YouTube

It was really fun to take on this challenge.Thank you DEV community!

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
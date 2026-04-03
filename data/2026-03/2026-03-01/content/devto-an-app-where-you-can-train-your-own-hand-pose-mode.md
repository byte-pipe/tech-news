---
title: An App where you can Train your Own Hand Pose Model for your Project! 🤌 - DEV Community
url: https://dev.to/francistrdev/an-app-where-you-can-train-your-own-hand-pose-model-for-your-project-58ib
site_name: devto
content_file: devto-an-app-where-you-can-train-your-own-hand-pose-mode
fetched_at: '2026-03-01T10:15:38.638131'
original_url: https://dev.to/francistrdev/an-app-where-you-can-train-your-own-hand-pose-model-for-your-project-58ib
author: 👾 FrancisTRᴅᴇᴠ 👾
date: '2026-02-28'
description: 'This is a submission for the DEV Weekend Challenge: Community The Community This targets... Tagged with devchallenge, weekendchallenge, showdev, javascript.'
tags: '#showdev, #devchallenge, #weekendchallenge, #javascript'
---

DEV Weekend Challenge: Community

This is a submission for theDEV Weekend Challenge: Community

## The Community

This targets the AI/ML community in general, especially those who want to get their feet wet into creating their own model. I notice when I start learning AI, there aren’t a lot of resources (to my knowledge) that allow you to create your own model and have the freedom to download the files to import it to your project without having to sign up and possibly pay to use their services (I might be wrong but that’s based on my experience). The lack of free tools pretty much restricted me since it is not accessible and I do not enjoy signing up and paying for their services just to train my model. Even if it is free, it is quite limited in some way.

Additionally, when I use Pre-Trained models, sometimes it is not as accurate as I needed it to and sometimes it goes back to the same problem: Signing up, either pay or not, and use their API key (which is good in some cases, but when it comes to creating a Chrome Extension for example, it’s hard to hide).

## What I Built

I remember creating the ASL project that Ishared on Dev.towhere I mentioned I created another project that is dedicated to creating my own model using Hand Pose. I thought it would be convenient to create a free tool that allows you to train your own model, download it, and use it to your project.

I created a website called “HandTracker” where you can create your own model using the ml5.js Hand Pose feature. This allows you to create any gestures you want and classify them to your liking. For example, you can create a hand gesture that means “Hello” or create the Gojo’s signature gesture forDomain Expansion: Infinite Void.

## Demo

✨ Live Demo:https://francistralt.github.io/HandTracker/

#### This is what the website looks like when you first visit:

Note:Make sure to enable your camera on. Otherwise, it would not work!

   

#### These are the settings:

1. Define Classes:You can create class that will correlate with the gesture you made. For example, if it is for ASL, you can do the “A” gesture, and it will output the class “A”.
2. Collection:You can modify how many data samples you would like to capture for each class. It is recommended that for all classes, it needs to be the same amount.
3. Training Parameters:You can modify the training parameters for your liking depending on the sampling size you decide to train.
4. Once you train all the classes and modify your training parameters, then you can click“Begin Training”and let the magic happens!

Note:During training, the training is collecting data if the hand is visible. If the hand is not visible, it pauses.

   

#### After you train the model, you can test out the features as shown here:

   

#### You also have the ability to download the model as a zip folder. The contents in that folder includes

Model.json
Model.weights.bin
Model_meta.json

Enter fullscreen mode

Exit fullscreen mode

## How I Built It

This is built using Vanilla HTML, CSS, and JS. Additionally, I uses ml5.js to perform Machine Learning related stuff and p5.js library. This is fully built using Google Gemini and thecode is 100% coded by Gemini.

## Code

Feel free to see the code here:https://github.com/FrancisTRAlt/HandTracker

If you are interested in contributing, feel free! The whole goal is making this tool free to use and I want to expand features where it is not just the Hand Pose. Imagine using it to train models that does Image Classification, Text generation, etc!

Any questions/comments? I would love to hear from you!

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
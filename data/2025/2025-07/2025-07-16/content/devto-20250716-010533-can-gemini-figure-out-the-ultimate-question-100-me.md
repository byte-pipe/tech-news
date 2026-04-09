---
title: 'Can Gemini Figure Out the Ultimate Question: 100 Men Versus a Gorilla — Who Would Win? - DEV Community'
url: https://dev.to/ansellmaximilian/can-gemini-figure-out-the-ultimate-question-100-men-versus-a-gorilla-who-would-win-475h
site_name: devto
fetched_at: '2025-07-16T01:05:33.259208'
original_url: https://dev.to/ansellmaximilian/can-gemini-figure-out-the-ultimate-question-100-men-versus-a-gorilla-who-would-win-475h
author: Ansell Maximilian
date: '2025-07-09'
description: 'This post is my submission for DEV Education Track: Build Apps with Google AI Studio. Spoiler: I... Tagged with deved, learngoogleaistudio, ai, gemini.'
tags: '#deved, #learngoogleaistudio, #ai, #gemini'
---

Education Track: Build Apps with Google AI Studio

This post is my submission forDEV Education Track: Build Apps with Google AI Studio.

Spoiler: I absolutely love this new feature in Gemini. It works awesome. I've tried many different prompts for many different app ideas, and in the end I always end up with a working app that looks great, handles errors, is well-organized, and does exactly what I want.

You can test out the final apphere.

## What I Built

It was super big a while ago over on X/Twitter: "Can 100 men beat one gorilla?"

Most of the participants in this discussion didn't have any expertise to answer one or the other AND explain it accurately.

That's how I got the idea for this app. Why not let AI decide. It's got all the information and is really good at reasoning.

The basic premise of the app is to simulate a battle between two teams scientifically. So users will be able to pit two teams comprising of one or more characters (real or fictional) and see who the AI thinks would win, based on real world metrics.

Though any characters is valid, the driving motivation to create this app is to finally and reliably answer that question: 100 men vs one gorilla — who would win?

### The Main Prompt

I started with the main prompt to get the basic features:

* user inputs what the two teams are
* AI simulates the result
* display the result

Besides describing the main features, I also sprinkled in some commands for Gemini to include some support features and specific styling:

* Error handling: I asked it to elegantly handle any errors and distinguish between all types of possible errors
* Science based description: I asked it to analyze the battle scientifically and apply real-world metrics likekm/h,tons,voltage, etc.
* Styling: I asked it to theme the application around the concept of "Red vs Blue".

Here was the full prompt:

Create an app called "Who Would Win".

It takes two teams (each comprising of a character OR groups of characters) by two fields: name and description.

Then use Gemini to simulate a realistic battle to the end and generate the result.

The result should describe the battle in scientific terms.

You should map supernatural/fictional powers as close to real world metrics as you can. For example: if a character in lore somehow shoots lasers out of their eyes; explain how much heat it generates, how destructive it is, etc.

Theme the whole app around red vs. blue.

If a character is non-existent and the description is too vague or also doesn't exist, display an error. For a battle to be valid, the teams need to comprise of either recognizable characters OR created characters with enough description.

Make sure to differentiate between Gemini API error and invalid teams error.

Enter fullscreen mode

Exit fullscreen mode

You'll see the result in more detail below, but a quick review:

Gemini absolutely crushed it — as expected after testing it out a bunch. The main features were implemented beautifully in a responsive UI. The support features and styling requests were also interpreted and implemented correctly. The "Red vs. Blue" style was done elegantly without making the app look corny.

### Enhancements/Adjustments with Gemini

After a satisfying initial prompting, I decided to test its adjustment/enhancements capabilities. Because generating a project and enhancing/adjusting it, to me, seems intuitively different enough that I needed to test it.

The first prompt didn't include image generation. Let's try adding that. Here is the prompt I entered into the code assistant panel:

Aside from text result, also use Imagen to generate an image of the battle result

Enter fullscreen mode

Exit fullscreen mode

Again, the result will be shown in more detail below. But to summarize: it worked really great. I expected an adjustment process like this to mess up existing code or at least change it very noticeably. But to my surprise, the UI and the previous features stayed largely the same.

It added the new requested feature very seamlessly and correctly.

## Demo

Here's a video clip of my whole process of developing this whole app. Generating the initial project took about ~2.5 minutes, while the adjustments took about ~1.5 minutes.

The video doesn't contain any editing in an attempt to show you in real time the whole process of creating this app. Feel free to skip around:

Here's what the final app looks like:

## My Experience

Here's a detailed chronology of my experience using Gemini's build feature, from beginning to end:

### First Prompt

Pretty straightforward process. Please note that this was my first iteration of the prompt. I didn't enhance it using another AI or anything. I wanted to push Gemini to see if how much prompt engineering skills you need to produce satisfying results.

### Result of First Prompt

Turns out you don't! Obviously, you can't just write gibberish and expect it to understand. But this shows that Gemini was able to interpret what I wanted from a simple and human prompt.

Everything I described in the prompt was implemented correctly and more.

#### Error handling

Error is handled very beautifully.

### Testing Out the App

### Created Files

Here's the current version of the app. I finally got to simulate the battle between 100 men and a gorilla. 100 men won!

I was super happy with the result, as I was always team "100 men".

As you can see, there is detailed, grounded, and scientific explanation of the fight with real-world metrics like strength measured inN, velocity, etc.

### Enhancement and Adjustment

This is where I tested Gemini's adjustment/enhancement capabilities. Currently the app doesn't generate the image representing the battle. So I went over to the code assistant panel and added a new prompt, requesting it to add — on top of the existing features — an in image generation feature using Imagen.

It worked really well. What's amazing is that the previous code not relevant to the new feature stayed very largely the same.

### Adjustment Result

Here is the resulting app after the enhancement. As you can see, the styling stayed the same, but now there's an image there.

### Final Result

Here's the app in full screen. Looks great!

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse

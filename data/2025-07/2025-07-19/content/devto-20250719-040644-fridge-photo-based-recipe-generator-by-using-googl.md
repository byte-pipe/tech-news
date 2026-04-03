---
title: Fridge-photo based recipe generator by using Google AI Studio - DEV Community
url: https://dev.to/samee-ullah/fridge-photo-based-recipe-generator-by-using-google-ai-studi-28k5
site_name: devto
fetched_at: '2025-07-19T04:06:44.654831'
original_url: https://dev.to/samee-ullah/fridge-photo-based-recipe-generator-by-using-google-ai-studi-28k5
author: Samee Ullah
date: '2025-07-11'
description: 'This post is my submission for DEV Education Track: Build Apps with Google AI Studio. What... Tagged with deved, learngoogleaistudio, ai, gemini.'
tags: '#deved, #learngoogleaistudio, #ai, #gemini'
---

Education Track: Build Apps with Google AI Studio

This post is my submission forDEV Education Track: Build Apps with Google AI Studio.

## What I Built

I built a simple app that gives recipe ideas using a photo of your fridge. The user uploads a fridge photo, and the app finds the ingredients and shows easy recipes.I used Google AI Studio with the Vision model. My prompt tells Gemini to detect ingredients and suggest simple recipes from what it sees.

This is the prompt that I used:

You are a helpful cooking assistant.

The user will upload a photo of the inside of their fridge. First, >analyze the image and identify only the visible food ingredients (e.g. >eggs, milk, vegetables, sauces, fruits, leftovers, etc.). Ignore non->food items like containers, packaging, bottles, or background objects.

Then, based on the identified ingredients, suggest 1 or 2 simple >recipes that can be made using only those ingredients.

Each recipe should include:

* Recipe name
* List of required ingredients (from the image)
* Easy step-by-step instructions (maximum 4 steps)

If you cannot find enough ingredients, reply politely:"I couldn't find enough ingredients to suggest a recipe. Please try a clearer photo."

Keep your response short, friendly, and beginner-friendly.

## Demo

Link to my app (Google AI Studio App)Live Demo

## My Experience

I really enjoyed building this app. It was easy to use Google AI Studio and create something useful with just a prompt.

I learned how to write a good prompt for image input and how AI can turn images into smart responses. I plan to add more features to this app later!

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse

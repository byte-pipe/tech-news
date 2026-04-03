---
title: What’s the Worst Advice AI Has Given You? Here’s Mine. - DEV Community
url: https://dev.to/gramli/whats-the-worst-advice-ai-has-given-you-heres-mine-58j4
site_name: devto
content_file: devto-whats-the-worst-advice-ai-has-given-you-heres-mine
fetched_at: '2026-03-05T11:16:06.805219'
original_url: https://dev.to/gramli/whats-the-worst-advice-ai-has-given-you-heres-mine-58j4
author: Daniel Balcarek
date: '2026-03-04'
description: I recently saw a meme about terrible legacy code on platform X and it gave me an idea for a... Tagged with discuss, ai, chatgpt, security.
tags: '#discuss, #ai, #chatgpt, #security'
---

I recently saw a meme about terrible legacy code on platform X and it gave me an idea for a discussion topic.

A year ago, the classic developer question was:

“What’s the worst code you’ve ever seen?”

But our day-to-day work has changed. Maybe the real question now is:

“What is the worst suggestion AI has ever given you?”

I’ll start.

I’ve happily survived plenty of questionable code: from “fast hotfixes” that didn’t even touch the root cause, to refactorings that added more complexity than my 15-years-younger self on OOP steroids.

But this happened about a year ago and it still sticks in my mind:

## API key in a public Docker image

I was working on a GitHub Action that builds a Docker image from my .NET REST API, pushes it to Docker Hub as a public image and then deploys it to Azure. Pretty straightforward, right?

There was one small catch: the API uses a private API key to communicate with a third-party service.

So I asked ChatGPT for advice.

Its suggestion:

“You can store this API key as an environment variable in your Docker image.”

Wait… what?

Put a private API key inside a public Docker image?

To be clear, environment variables themselves are fine.The problem was baking the secret into the image during build time, which would expose it to anyone pulling or inspecting the public image.

I explained this to ChatGPT.

It responded with the classic:

“You are right!”

…and suggested storing it securely in Azure.

End of the story?

Of course not.

Just a few messages later, in the same context window, ChatGPT again suggested putting the private API key into the public Docker image as an environment variable.

That was the moment I realized:

AI isn’t production-ready yet, at least for security advice. 😄

## The interesting shift

We used to review junior developers’ code carefully.

Now we also need to review code written by something that sounds like a senior engineer but occasionally behaves like an intern on their first day.

## Discussion

* What’s the most ridiculous suggestion AI or ChatGPT has ever given you?
* Do you review AI-generated code differently than human-written code?

I’d love to hear real examples from the community.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (20 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse
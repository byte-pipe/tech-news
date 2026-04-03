---
title: 'Vibe-coding in Google AI Studio: my tips to prompt better and create amazing apps - DEV Community'
url: https://dev.to/googleai/vibe-coding-in-google-ai-studio-my-tips-to-prompt-better-and-create-amazing-apps-3kcp
site_name: devto
content_file: devto-vibe-coding-in-google-ai-studio-my-tips-to-prompt
fetched_at: '2026-03-20T11:14:40.098809'
original_url: https://dev.to/googleai/vibe-coding-in-google-ai-studio-my-tips-to-prompt-better-and-create-amazing-apps-3kcp
author: Guillaume Vernade
date: '2026-03-19'
description: You might already know Google AI Studio as a sandbox to play with the Deepmind models and tinker with... Tagged with ai, vibecoding, gemini, promptengineering.
tags: '#ai, #vibecoding, #gemini, #promptengineering'
---

You might already knowGoogle AI Studioas a sandbox to play with the Deepmind models and tinker with all their parameters. But did you know that you can also vibe-code webapps for free and publish them in a few clicks?

ItsBuildsection is a game-changer for "vibe coding" and generating functional applications without writing a single line of code. It allows you to rapidly build and iterate on ideas using the power of Gemini models, moving from simple concepts to fully deployed prototypes in minutes.

Following my own experiments with the platform over the last year, this guide covers the core capabilities of AI Studio, how it compares to other tools, and how to prompt it effectively to build your apps.

Here's what you'll find in this article:

* 0.Why use AI Studio?
* 1.The App Gallery & Remixing
* 2.Get started with Vibe Coding
* 3.Create apps with databases
* 4.My tips to better Vibe Code
* 5.Publish your app
* 6.AI Studio vs. Antigravity: When to use which?
* 7.My favorite creations

# 0. Why use AI Studio? (Native Gemini and Privacy)

Before diving into the "how," let's address the most common question:Why use AI Studio over other popular AI app builders on the market?

The first reason is for AI Studio'snative Geminiusage. It can create apps that are using the Gemini models, in a way that (as long as you stay in AI Studio) you don't have anything to set up so you, and the folks you're sharing your app with, can use the free tier and enjoy Gemini-powered apps for free.

Note: Some advanced models require a paid API key, but there's always an alternative with a free tier.

But the main differentiator isPrivacy.

On the free tiers of many competing platforms, unless you're paying, all the applications you generate are public by default. Anyone can see what you are working on. On AI Studio, your apps remainstrictly private. This is a huge advantage when you are prototyping personal ideas, working on sensitive client projects, or just want to experiment freely without worrying about public visibility.

Sharing uses the same system as any Google Drive file, which makes sharing your apps easy and lets people try them without having to create a new account.

Pro tip:As with any Drive file, you can set your apps to be accessible to whoever has the link. That's what I do when I post on LinkedIn (cf. the last section of this post for examples).

In any case, even if you don't use AI Studio, my tip should still be relevant as most vibe coding agents are working similarly.

# 1. The App Gallery & Remixing

If you are new to vibe coding, the best way to understand how the code is generated is to explore theApp Gallerydirectly within AI Studio.

Best Practices:

* Explore:Check out the impressive examples already built by the AI Studio team. Two of my personal favorites are theSpatial understandingand theComic Book Creator(which need a paid API key to use Nano-banana Pro, but you can try remixing it to only use Nano-Banana's free tier).
* Check the code:For each app, you can click "code" in the top left corner to access all of the app's code and check how things are done (or more likely copy-paste it to an AI coding agent).
* Remix:When you like an app and just want to create your own flavor of it, click "remix" to create a copy of it that you'll own. It's an excellent way to start from an existing, working codebase and make it your own.

# 2. Get started with Vibe Coding

Ready to build your own? The principle is incredibly straightforward: open thebuildpage, write what you want the app to do in a prompt, hit enter, and watch the coding agent (similar to theAntigravityone) generate the UI and logic.

Note:the generation can take quite some time (about 5 mins on average), so go get a coffee or read a blog post and come back after the coding agent has finished its job.

When you get a working app, you can start adding new features by continuing to prompt in the code assistant chatbox on the left.

New:One of the cool new additions in the past weeks is that the code assistant now works server-side, which means you can close the tab or change devices and it will continue to work for you.

Depending on the case, you can also use those two buttons to provide visual clues to the model by drawing things on it, which is very convenient to give UI feedback.

Another option is to dictate what changes you need. It's very convenient when you want to add a new feature on-the-fly while on your phone, but I would not recommend it for very precise updates.

# 3. Create apps with databases

Sincethis week, you can also ask the coding agent to create apps that can save things between sessions or users. You just need to ask it to specifically use a database:(yes, I've been wanting to create my own grocery list app for a very long time)

Just click "Enable" when asked and the magic will happen.

What it will do behind the scenes is setting up the Firebase integration and a Firestore to store your data. It will also add authentication using a Google account to your app so it knows who's trying to access which data.

You don't need to know how your database is structured, the code agent will manage everything for you depending on what your app needs. You want each user to have their own grocery list? Boom, it's done! You now want them to be able to have shared lists, that's also done! Add labels to the items, easy peasy.

Your imagination is the limit!

# 4. My tips to better Vibe Code

Nowadays, "vibe coding" has become a reflex for me. It is the absolute best way to prototype a user experience before potentially moving to a complex IDE. But if you're not careful, you can easily end up losing a lot of time to make the agent work in an efficient way.

So here are my top tricks to get the most out of AI Studio (in no particular order).

### Design your app before building it

If you have opinions about what your app should look like (personally I usually don't, yolo), a good idea is to iterate on designs for it using something likeStitch(that is using Nano-Banana) and give the images to the coding agent so it knows what's expected.

### Save your progress so you can revert (and learn when to do it)

AI makes mistakes. It might misunderstand your prompt or write code that breaks a previously working app. When this happens, you can ask it to "fix the error" and most of the time it works, but sometimes it doesn't.

One very important skill to learn when vibe coding is when to try to fix things using AI, when to start anew, and when to go fix things yourself.

My personal advice is that if the agent can't figure out how to fix something after 2 rounds, stop insisting and go back to a previous version otherwise you might end up spending an hour arguing with the AI for nothing. And when you think you're spending as much time explaining what you want than to actually do it yourself (a good example is "change this time for another"), just do it yourself.

Thankfully AI Studio makes it easy for you to go back to a previous version:

#### Checkpoints

Checkpointsare the built-in version history to instantly revert to the last working state. They are the most convenient way to go back to a previous working version.

Warning:Just be careful of something: you can revert the code, but not the database changes, so don't load a checkpoint that was before a database update (what I would do is load the checkpoint, copy the code, load the more recent/broken code, ask the assistant to fix it based on how it was before).

#### Github

Githubis what I would recommend to save milestone versions. You should use it to save the state of your app when you reach a certain milestone, like when you finish adding a new feature. You can enable it in a few clicks:

And then it will just be about describing your new feature and committing it to GitHub.

One current limitation though is that the sync is one-way, so it's a good way to save your status in a place where you can easily reuse it, but you can't update your code in GitHub and sync it to AI Studio (yet).

### Use Multi-Modal Prompting

Stop relying purely on text. As I said before, AI studio gives you other options:

* Voice:Incredibly practical for iterating quickly, especially if you are tweaking an app from your phone.
* The "Annotate App" Tool:This is my absolute favorite feature for UI work. Take a screenshot of your app, draw directly on it ("Move this button here", "Remove this menu"), and send it.

Pro Tip:Always combine the annotated image with a clear text explanation to give the model maximum context.

### Split Your Files! (Avoid the Monolith)

As your app grows, the model might start to "hallucinate", forget earlier features, or tangle the logic. This is almost always a structural issue.

By default, the AI tends to cram everything into one massiveapp.tsxfile. Veto this immediately.

* Golden Rule:Tell the model from the very beginning to separate features into distinct files and components.
* Why?It drastically reduces errors and makes generation faster. It also allows you to instantly spot if the AI is messing up (e.g., If you ask for a UI color change and it starts rewritingauth-service.js, you know it lost the plot and you can stop it immediately). It will save you a lot of time when reviewing and at least gives you anat a glanceconfidence that the right part of the codebase was updated.

### Force the AI to Write Documentation

To also help the AI remembering what the app is meant to do, have it maintain as much documentation as possible (from micro to macro):

* Docstrings:Always forces the app to document all its functions, what they do, what the inputs and the outputs are.
* File documentation:Since you're creating a file per feature, tell the AI to maintain some documentation at the top of them to detail what the feature is about, what use cases should be covered, etc.
* Design.md:Finally, ask it to maintain a design doc of the whole app at the root of it.
* Why?By having the AI repeat everything multiple times you both help it (and potentially yourself) find where everything is being done and what is the expected behavior. Kind of like howerror correction codeswork, having something written multiple times reduces the chances that they will be deleted by mistake.

### Supercharge with System Instructions

After some time you'll realize that you're always giving the same instructions to the coding agent and will get tired of repeating yourself. That's why AI Studio allows you to customize the underlying "System Instructions." Don't leave this blank! You can define your preferred tech stack, frameworks, coding style, and of course everything I mentioned before!

Think of it as the onboarding package for your new junior developer, they need to know how you are expecting them to work, how to code, document, communicate, etc... You might not get it right the first time, but it's important to reflect on it and to keep on improving your package so that the next newcomers will be better onboarded and thus get productive faster.

Here's the ones I'm always using on top of more specialized instructions (like trusting me on model names and not changing them):

## Coding/documenting guidelines

*
 Create a file per feature or related features, split as much as possible in different files;

*
 add docstrings to all functions to explain what they do;

*
 start each file with a long comment explaining in detail what the feature is about and the different use cases;

*
 maintain a 
`Design.md`
 document at the root of the app that documents all the features of the app;

*
 log as info all function calls (with their parameters) and log all genai calls with all their parameters (model used, prompt, config) and their outputs, just strip inline data;

*
 group all configurable items (like model names) in a centralized file;

*
 always create a way to test the scripts without altering the data;

Enter fullscreen mode

Exit fullscreen mode

You'll see that I also added some instruction about logging (as it always help debugging) and dry run as these are both good practices, vibe coding or not.

Try them and tell me if that improved your vibe-coding experience!

# 5. Publish your app

You are now happy with your app and want to share it with the world (or maybe a subset of it), AI Studio offers you two ways of publishing your app:

### Share it in AI Studio

The easiest way is to just use AI Studio sharing capability.

You can either decide to share the app with specific people or to make it available to whoever has its link (that's what I use on LinkedIn for ex.).

One of the key benefits is that they will also get access to the code and be able to Remix it if they want. But you can also send a link that opens the app full screen and hides the code agent to your less technical friends.

Another nice benefit is that if your app is using Gemini, your friends will use their free tier when using the app (or their API key if using a paid model), which means it won't cost you anything.

### Publish the app on Cloud run

This is what you should do if you want to publish the app for real to actual users. In a few clicks it will create a cloud run container, publish the app online and give you a URL for anyone to access it.

You'll then be able to buy a domain and give it a proper URL, deploy in different regions, automatically scale, etc... But then you'll also be the one paying for usage as it's your own app now.

# 6. AI Studio vs. Antigravity: When to use which?

Since AI Studio uses a similar underlying coding agent as Google'sAntigravity, you might be wondering when to use which tool. Here is my rule of thumb:

Use AI Studio when:

* You are prototyping a front-end UI or a lightweight full-stack application.
* You want to genuinely "vibe code" using multimodal inputs (like drawing directly on the app's UI or using your voice).
* You want to instantly share a working prototype with stakeholders or friends via a simple link, without managing hosting.
* You want zero-setup, native access to the Gemini models to build AI features quickly.

Use Antigravity when:

* You are building a production-grade, complex application with deep backend infrastructure requirements.
* You need fine-grained control over your dependencies, complex build steps, and deployment pipelines.
* You are integrating the AI coding agent into anexisting, large-scale codebase rather than starting a project from a blank slate.

Think of AI Studio as your creative sketchbook for rapid iteration, and Antigravity as your full-fledged developer workshop.

# 7. My favorite creations

Now that you have mastered the basics of vibe coding, the best way to learn is by doing. I didn't follow all these rules perfectly when I started, but making mistakes is how you refine your workflow!

To show you what's possible, here are a few applications I vibe-coded entirely from scratch using most of those methods:

* [AI-powered resume]:An AI-powered resume. Don't just read it, but ask Gemini questions about me (it will know some anecdotes that are not written), tailor it according to the role you want to propose to me or even ask for an audio overview.Check it out here
* [Talk coach]:A coach for your talks. Give it a recording or youtube link and it will tell you how to get even better.Check it out here
* [FreshList]:A copy of the app I'm working on to simplify the groceriesCheck it out here

See other examples in therepoI created when I thought I will have the time to vibe code an app per week.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
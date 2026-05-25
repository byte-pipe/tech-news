---
title: Should you use Gemma 4 for your Development? A Multiversal Analysis to Determine if Gemma 4 is Right for You! - DEV Community
url: https://dev.to/devengers/should-you-use-gemma-4-for-your-development-a-multiversal-analysis-to-determine-if-gemma-4-is-2iol
site_name: devto
content_file: devto-should-you-use-gemma-4-for-your-development-a-mult
fetched_at: '2026-05-25T12:12:02.735313'
original_url: https://dev.to/devengers/should-you-use-gemma-4-for-your-development-a-multiversal-analysis-to-determine-if-gemma-4-is-2iol
author: FrancisTRᴅᴇᴠ (っ◔◡◔)っ
date: '2026-05-22'
description: 'This is a submission for the Gemma 4 Challenge: Write About Gemma 4 Disclaimer: This is an... Tagged with devchallenge, gemmachallenge, gemma, discuss.'
tags: '#discuss, #devchallenge, #gemmachallenge, #gemma'
---

Gemma 4 Challenge: Write about Gemma 4 Submission

This is a submission for theGemma 4 Challenge: Write About Gemma 4

Disclaimer:This is an individual submission for Francis Tran (@francistrdev). Everyone involved has their own accounts of using Gemma 4 and has been paraphrased in this post. See below for the list of people involved.

 

Author:Francis Tran (@francistrdev)Featuring:Elmar Chavez (@codingwithjiro), Konark Sharma (@konark_13), and Julien Avezou (@javz)

The cover image uses characters from various Anime chosen by the people who are featured in this post, put together in using Pixlr, and using AI to enhance the quality of the image. Some contents started off using AI and has been paraphrased by the author's own words.

# Table of Contents

* Introduction
* Setting up Gemma 4 using OllamaInstalling Ollama and Gemma 4Trying out Gemma 4Running Gemma 4 OfflineElmar's Verdict on Gemma 4
* Installing Ollama and Gemma 4
* Trying out Gemma 4
* Running Gemma 4 Offline
* Elmar's Verdict on Gemma 4
* Using Gemma 4 as a Confused DeveloperThe Strawberry TestThe Tic Tac Toe Rotation TestThe Broken Cup TestKonark's Verdict on Gemma 4
* The Strawberry Test
* The Tic Tac Toe Rotation Test
* The Broken Cup Test
* Konark's Verdict on Gemma 4
* Building a Prototype using Gemma 4Results of Gemma 4 Vs. GPT 5.4Technical DepthArchitecture & System ThinkingJulien's Verdict on Gemma 4
* Results of Gemma 4 Vs. GPT 5.4Technical DepthArchitecture & System Thinking
* Technical Depth
* Architecture & System Thinking
* Julien's Verdict on Gemma 4
* Using Gemma 4 as an AI-AgentGemma 4 is StrictPlease Google I need this. Gemma 4 is kind of Looping ItselfFrancis' Verdict on Gemma 4
* Gemma 4 is Strict
* Please Google I need this. Gemma 4 is kind of Looping Itself
* Francis' Verdict on Gemma 4
* Summary

Thank you for Reading!

# Introduction

In the age of AI, many developers are using AI in their workflows. This can range from AI assistants cleaning up a large code-base to developers vibe coding a prototype to showcase to others.

Regardless of your use of AI in your development, it is important to choose the model you want to work with. There are a lot of choices to choose from such as ChatGPT, Gemini, Copilot, etc.The one we are talking about today is Google's latest model: Gemma 4!

The goal of this article is to share our experiences using Gemma 4 in 4 different perspectives of Developmentstarting from setting up Gemma 4 using Ollama, testing the hallucination of Gemma 4, how Gemma 4 outputs, and using Gemma 4 as an AI-Agent.Additionally, I will share our discoveries and whether we recommend using Gemma 4 based on our experiences!We hope that our experience of using Gemma 4 will help you to decide if Gemma 4 is right for you in any skill level of your developer career!

With that said, we will now talk about the setup process. In any development, we all experience setting up our environment whether it is OpenClaw or a simpleNPMpackage! Having a local LLM is one of them. Here is Elmar's experience of setting up Gemma 4 using Ollama!

 

 

# Setting up Gemma 4 using Ollama

## Elmar ChavezFollow

Licensed civil engineer turned full stack developer building accessible, responsive web applications. I also review code in Frontend Mentor and participate in collaborative projects.

Elmar has been using ChatGPT for the past year where he mainly uses it as a mentor when doing projects. He was interested having a LLM locally. He believes that having an LLM locally is convenient for his case, due to power outages he has to faced in the Philippines. Having Gemma 4 locally will allow him to be productive when coding without the need to worry about connecting to the internet. With that said, he started to research about setting up Gemma 4 using Ollama.

 

### Installing Ollama and Gemma 4

Elmar started to search on the internet, looking for tutorials on getting started on Gemma 4.

One of the ways to get started is installing Ollama, which Elmar thought was a weird name until he realized the logo was an actual llama.

When downloading Ollama, the main issue is the storage, which was nearing 100% capacity and Ollama installer defaults to theC:\ drive.

After searching more about installing Ollama without installing on theC:\ drive, which led to this command he had to run on the terminal:

C
:\Users\ELMAR>cd 
Downloads

C
:\Users\ELMAR\Downloads>OllamaSetup.exe 
/DIR
=
"D:\Ollama"

Enter fullscreen mode

Exit fullscreen mode

Ultimately, it worked well. He had done other configurations such as redirecting the AI model installation in the same drive underD:\OllamaModels. He then downloaded thegemma4:e4b.

 

### Trying out Gemma 4

The first thing Elmar tried was"hi gemma4". Although the expected outcome is Gemma 4 saying hello back, it gave him this error:

Error
500 Internal Server Error: model requires more system memory (9.8 GiB) than is available (4.9 GiB)

Enter fullscreen mode

Exit fullscreen mode

 

For context, this is his device specifications:

His laptop is great for programming and other developments. The issue is that his laptop is only suitable for "lightweight models" when it comes to downloading LLMs locally.

 

Elmar discovered that local AI depends heavily on your own hardware, unlike browser-based AI tools like ChatGPT.

 

One of the things Elmar did was to run a smaller version of Gemma 4:

ollama run gemma4:e2b

Enter fullscreen mode

Exit fullscreen mode

It gave him a similar error as before:

Error
500 Internal Server Error: model requires more system memory (7.2 GiB) than is available (5.7 GiB)

Enter fullscreen mode

Exit fullscreen mode

 

After investigating a bit more, he closed other applications that were running on his computer and taking up space and it outputted!

 

The big thing about running it for the first time is that it took longer than he expected, but he mentioned that he had VSCode, Notepad, and 4 tabs currently opened in his Chrome Browser.

 

### Running Gemma 4 Offline

Elmar was curious about the result of using Gemma 4 without connecting to the internet.

It ran slower than usual, but it is still under a minute.

 

Elmar then tried to ask questions to Gemma 4 that he would normally ask to ChatGPT as part of his Development workflow.

In this case, he is currently building his website portfolio. Elmar asked a question along with attaching a screenshot to Gemma 4 and here is what it output:

Surprisingly, it took less time considering the fact that he inserted an image for this use case.

 

The wait time for the LLM to respond, which is around a minute, is reasonable for Elmar since he has a decent laptop. It is quite useful especially for countries that commonly have power outages or that have unreliable internet.

 

### Elmar's Verdict on Gemma 4

This is Elmar's Verdict of Gemma 4 in terms of setting up via Ollama and using it for the first time:

Web-based LLMs are great for convenience and device flexibility. While local LLMs are great for offline reliability and privacy, I'd say the experience of experimenting with Ollama + Gemma 4 only made my perspective with AI clearer.

It is not magic, it's just data combined with probability and rendering models that require large amounts of RAM for compute power.

This begs the question, if I have a higher end device, would I invest fully into local LLM's?

I would not sacrifice my own hardware for running AI computations just to get responses faster.

There are data centers that have the hardware especially built for AI. I would rather give the job to them.

Overall, ChatGPT is still far more practical for my current workflow so I will be sticking to it as my default. However, I would definitely use Ollama + Gemma 4 as a reliable alternative.

That is Elmar's Verdict on Gemma 4! In the early stage, it is fast to setup, but difficult to use when it comes to response time and the hardware needed, especially considering most users do not have a powerful laptop.

Now you know about the setup with Gemma 4! Starting off with Gemma 4 and seeing its outputs is a good sign that everything works! However, although Gemma 4 is a small and powerful model, how good is it at not being confused? We now transition to Konark where he tested Gemma 4 to the limit!

 

 

# Using Gemma 4 as a Confused Developer

## Konark SharmaFollow

I am software engineer who finds fun and creativity in Frontend. I would love to be a part of a team to help, develop and learn from new people and add my knowledge to the project.

Konark has been using Gemma 4 for some time and the one thing he wanted to know is to see if he canabuse Gemma 4 to its confusion.

We all have that one moment where we randomly test an AI just to see“How smart are you actually?"with questions like“How many r’s are there in strawberry?”.Konark did three tests such as theStrawberry test, the Tic Tac Toe Rotation test, and the Broken Cup Test.

 

### The Strawberry Test

Konark asked Gemma 4:“How many r’s are there in strawberry?”(The answer would be three). Initially, this type of question was commonly used to confuse many AI models.

Gemma 4 thought for a while and gave Konark three different interpretations regarding the number of "r’s" in strawberry.

 

Konark realized that sometimes AI over complicates simple questions and he would rather prefer simple answers. For example, if there are 10 apples in a basket and you asked Gemma 4: “How many apples are there?”.

 

Would you prefer this answer:

“This is my first time counting. Do you mean apples inside the basket or around the basket?”

 

Or would you simply perfer:

“There are 10 apples.”

 

Konark would prefer the second answer.

 

With these results, he was curious about how Gemini would answer to the strawberry test. As such, he asked Gemini and it simply replied:

3 r’s.

Enter fullscreen mode

Exit fullscreen mode

It is straightforward and it is always good to have a simple, non-complex answer.

 

### The Tic Tac Toe Rotation Test

Another fun question Konark asked Gemma 4 was:“How would rotating a tic tac toe board by 90 degrees change the rules of the game and its strategy?”

The whole goal is to see if Gemma 4 thinks it's still the same, expect the board is rotated.

However, Gemma 4 took quite some time to conclude this. It explained things properly and even walked through a rotated example.

Although it is a helpful response, it would be nice to get a more straightforward answer similarly to the Strawberry Test.

 

### The Broken Cup Test

This is Konark's favorite test, in which he asked Gemma 4:“I have a metal cup with the bottom missing and the top sealed. How can I use this cup?”

The simple answer would be"Rotate the cup. And suddenly, it becomes usable again.".

However, Gemma 4 did not really understand the trick. Instead, it started suggesting alternative ways to use the object.

Although it is creative, it is not entirely correct.

 

On the other hand, Gemini understood the trick faster and then even expanded on practical uses.

Overall, Gemma 4 still struggles with certain trick questions and edge-case reasoning.

 

### Konark's Verdict on Gemma 4

This is Konark's verdict of using Gemma 4.

After playing around with both models, I reached a simple conclusion.

#### Gemma 4 feels good for:

* learning
* content generation
* straightforward explanations
* slower, detailed responses

#### Gemini feels better for:

* trick questions
* quick reasoning
* direct answers
* faster conclusions

And honestly, both have their place.

Sometimes I want a detailed explanation.

Sometimes I just want:“Bro, just give me the answer.”

And that matters.

Because developers don’t always want essays. Sometimes we just want the bug fixed.

This is important to consider when you want to use Gemma 4. Sometimes, we just want a simple answer to the issue we are trying to solve. Of course, prompting varies and this is Konark's experience using Gemma 4 so it can be different from others.

Speaking of prompting, AI is used to prototype projects in development! We now transition to Julien's experience on using Gemma 4 when it comes to prototyping a project and how it compares to what he usually uses, which is Codex!

 

 

# Building a Prototype using Gemma 4

## Julien AvezouFollow

Builder | Software Engineer | Author of The Thinking Engineer Toolkit

Julien planned on using AI to create a fast prototype.

 

He was curious about how Gemma 4 performs compared to his usual setup,Codex (GPT 5.4).

For context, the project is a Chrome extension to help develop better use of LLMs.He will share more on his blog page in the future!

His goal is to compareGemma 4 Vs. GPT 5.4when it comes to prototyping. For this comparison, he will run tests across the following 2 categories using the same prompt as input and comparing the quality of the outputs:

1. Technical Depth:The factual accuracy, understanding of deep system mechanics and ability to compare non-trivial trade-offs.
2. Architecture & System Thinking:The ability to think at the macro level, identifying bottlenecks, scaling issues, and making justifiable "when/why" decisions.

 

### Results of Gemma 4 Vs. GPT 5.4

Here are the results for the cases ofTechnical Depth and Architecture & System Thinking!

 

#### Technical Depth

This is the prompt given to both LLMs:

I am building a Chrome extension which detects when a developer is using ChatGPT, Claude, or Gemini, shows a floating button, opens a side panel, lets the user describe their task, recommends one of five AI thinking modes, generates a better prompt, and lets the user copy it manually.

Modes:1. Explore — when I don’t fully understand the problem yet2. Challenge — when I have a plan, but it might be wrong3. Decide — when I need to choose between options4. Audit — when I need to verify quality or correctness5. Reflect — when I want to actually learn from what I did

MVP constraints:

* Chrome extension only
* no login
* no dashboard
* no automatic prompt insertion
* no usage tracking yet

Task:Give me a technically detailed implementation plan for the MVP.

 

Here is the results:

Model

Pros

Cons

Gemma 4

Clear high-level structure. Correctly identifies manifest, background script, content script, overlay UI, and template-based prompt generation. Easy to read. Good for a conceptual first pass.

Too generic. Does not mention Chrome Side Panel API. Blurs overlay and side panel. Drifts from your exact modes. Weak on privacy/security. Less actionable for immediate implementation.

GPT 5.4

Much more implementation-ready. Strong file structure. Useful code snippets. Correct Chrome APIs. Better MVP scoping. Better maintenance thinking. Exact mode alignment. Clear recommendation to avoid LLM/API in v1.

Still light on deeper security analysis. The manifest/build setup would need adjustment because TypeScript files are not directly used by Chrome without bundling. Could have compared local/API/hybrid tradeoffs more explicitly.

Overall,GPT 5.4 gives the stronger Technical Depth output since it is more accurate, more build-ready, and more specific.

 

#### Architecture & System Thinking

This is the prompt given to both LLMs:

I am building a Chrome extension that helps developers use AI more intentionally.

It sits on top of ChatGPT, Claude, and Gemini. The user describes their task, then it recommends one of five thinking modes and generates a better prompt to copy.

Modes:1. Explore — when I don’t fully understand the problem yet2. Challenge — when I have a plan, but it might be wrong3. Decide — when I need to choose between options4. Audit — when I need to verify quality or correctness5. Reflect — when I want to actually learn from what I did

MVP:

* detect supported AI chat pages
* show floating ModeCheck button
* open side panel
* recommend mode
* generate better prompt
* copy manually
* soft CTA to the Thinking Engineer Toolkit

Future:A SaaS dashboard may later track AI usage modes, cognitive cost, dependency patterns, and optional hard blocks.

Task:Think at the system architecture level.

Cover:

* best one-week MVP architecture
* what to build now vs postpone
* key system boundaries
* privacy/trust risks
* maintenance risks for a solo builder
* how to preserve future optionality for analytics/dashboard
* strongest argument for and against the browser extension approach
* recommended roadmap: week 1, month 1, month 3

Be concise but thoughtful. Focus on trade-offs and “when/why” decisions.

 

Here is the results:

Model

Pros

Cons

Gemma 4

Good strategic restraint. Correctly recommends client-side MVP, hardcoded templates, no backend, and no dashboard at first. Good emphasis on fast time-to-value. Useful suggestion to model prompts as structured objects/schema for future flexibility.

Less complete system thinking. Weak privacy/trust analysis. Weak argument for/against extension approach. Maintenance advice is shallow. Roadmap becomes generic around logging, API integration, billing. Does not fully address future cognitive-cost/hard-block architecture.

GPT 5.4

Stronger system boundaries. Better local-first architecture. Better privacy/trust framing. Better solo-builder maintenance analysis. Stronger roadmap. Better future optionality through event/data modeling without collecting data yet. Better distinction between host page, extension, and future backend.

Does not go very deep on future scaling bottlenecks or hard-block mechanics. Could have included Gemma’s useful prompt-schema idea. Slightly less focused on concrete “engine” abstraction for prompt assembly.

Overall, GPT 5.4 wins on Architecture & System Thinking. Gemma 4 provides a solid, restrained MVP strategy, but GPT 5.4 gives a more complete architectural view: system boundaries, trust, local-first design, future analytics optionality, solo-builder maintenance risk, and roadmap discipline.

 

### Julien's Verdict on Gemma 4

This is Julien's verdict on the use of Gemma 4:

GPT 5.4 seems to be the strongest at high-level reasoning and synthesis as you would expect from a recent frontier model.

However a good use case for Gemma 4 in terms of prototyping work would be for codebase analysis, running experiments through constraints and for privacy-sensitive workflows.

Being an open model which can be run locally has great specific and complementary use cases when prototyping developer tools.

I will consider this going forward.

Even though GPT is preferred when it comes to high-level reasoning and synthesis, there are other cases where Gemma 4 is useful for prototyping.

Speaking of prototyping, now we transition over to using Gemma 4 as an AI-Agent!

 

 

# Using Gemma 4 as an AI-Agent

## FrancisTRᴅᴇᴠ (っ◔◡◔)っFollow

📚 Full-Stack Developer 📚
"A Smooth Sea never made a Skilled Sailor" - Franklin D. Roosevelt

Whenever I am contributing to Open Source, it is quite useful to have an AI-Agent to work with you. My preference is to use an agent living in an application likeVisual Studio Code.

I have been using GitHub Copilot when it comes to contributing to Forem and it has been useful when it comes to navigating code bases, problem solving issues, etc.

When I heard about Gemma 4, I thought it would be a good idea to try out when using Gemma 4 as an AI-Agent. I specifically used the cloud version using Ollama since the hardware I have cannot handle LLM locally, even though I tried the smaller version of the model.

 

Setting up wasn't too difficult on my part. Since I tried Ollama to begin with before the release of Gemma 4, it was as easy as pulling the model using this command:

ollama pull gemma4:31b-cloud

Enter fullscreen mode

Exit fullscreen mode

 

After installing, I selected the model and was ready to go!

 

When using the model, I noticed there wasn't much of a big change compared to my initial workflow of using Copilot as my agent.

Both models asked me for permission when running commands, able to problem solve the issue I requested, etc. To be fair, I wasn't using "Continue" Visual Studio code extension since it is quite popular when using local LLMs. Also, Visual Studio code is flexible when it comes to adding your own model in addition to using Copilot, which I wasn't surprised that it behaves similarly when using Copilot.

However, there are a couple of things I noticed when using Gemma 4 that I believe are important to address based on my experience using Gemma 4.

 

### Gemma 4 is Strict

The main difference between Gemma 4 and Copilot was that it is quite firm on the tasks it is given to them. I notice that whenever I request a plan on tackling an issue, it provides a To-do list of the steps Gemma 4 is planning on doing to fix the issue.

 

For example, this is the prompt I gave to Gemma 4:

I have this issue. How do I approach this?

https://github.com/forem/forem/issues/23277

Enter fullscreen mode

Exit fullscreen mode

It will output their findings like any other LLM. However, it would not act right away and instead, listed out the next steps:

 

In cases like these, I just follow up the Agent"Go for it"or"Proceed".Sometimes it does everything in the to-do list in one go and in other cases it goes one by one where I have to tell the Agent to"Do all the tasks".Do note that I did not change any settings as I was setting up Gemma 4 since it was just pulling the model and selecting it in Visual Studio Code.

Compare that to Copilot, where regardless of the prompt, it would take action right away. There were cases where Iforgot to change the mode from "Agent" to "Chat" and I was specifically asking the AI about the plan to tackle the issue.Instead of listing out the steps,it did it right away which I did not want it to do.

In all fairness, Gemma 4 and Copilot are from different companies (Google and Microsoft) and since Copilot is built into Visual Studio Code, it is fair to assume thatits actions strictly follows based on the settings you have in Visual Studio Code for Copilot.

However, it is always nice to see Gemma 4 listing out the To-do list and asking the user to proceed. I believe it is good practice by default if you are a type of user that wants to get an AI's advice on what to do and doing it yourself from there.

 

### Please Google I need this. Gemma 4 is kind of Looping Itself

It is exactly what you are thinking. This is a common occurrence where Gemma 4 will read a file from top to bottom and reread it again. Here is an example that I encountered when using Gemma 4:

I am not sure what is causing this issue since this happens randomly.

 

The solution is stopping the Agent and sending the same prompt. This fixes the issue really well, though this bug remains a mystery to why it occurs in the first place.

 

### Francis' Verdict on Gemma 4

This is my verdict on the use of Gemma 4 as an AI-Agent:

I believe Gemma 4 works really well when being an open source developer. It can navigate large code-bases and being able to solve complex problems well for a model that is quite small.

Although there isn't a big difference between Gemma 4 and other models I have used, it is good to consider token usage. I would recommend Ollama when using Gemma 4. It is free to use the cloud version and the tokens reset weekly whereas Copilot resets monthly. If you are heavily relying on AI-Agents, I would recommend the Ollama solution since it is more flexible. Even if you reach the daily limit of tokens, it resets every few hours.

I would highly recommend Gemma 4 as a great starting point when it comes to using it as an Agent when you want to contribute to open source. Just remember to monitor the response time since there is a very good chance where it loops itself in which it would burn tokens in the process.

 

 

# Summary

Gemma 4 has been used in some aspects when it comes to setting up Ollama to use Gemma 4, testing out the response of the model, prototyping using Gemma 4, and the role as an Agent. Here are the main things to consider based on what I have shared above.

 

### 1. Convenience

Like any other local models, you have to consider not only if you are conformable downloading a model locally, but ensuring you have enough compute power to run an LLM. Although there are options to use LLM on the cloud(for Ollama at least), having a local LLM is very convenient for developers who want to run the model locally and not worry about:

* Use of Tokens limits and payed services.
* The environment when it comes to data centers in the age of AI.

 

### 2. Performance

Speaking of compute power, having a local LLM, even with smaller models of Gemma 4, still needs a lot of power. We saw that in Elmar's experience, it took a while for Gemma 4 to produce an output comparable to using any cloud model. If you are comfortable with the wait time of the model, then it shouldn't be a problem!

 

### 3. Context Output

Every model behaves differently whether cloud or local models. This is no different to Gemma 4. If you are using Gemma 4,you have to make sure the prompt is specific to your needs.This is best practice in prompts in general when it comes to requesting your needs and being as specific as possible.

 

### 4. Role as an AI-Agent

It is common for developers nowadays to use a local model to run as an Agent. Using Gemma 4 via Ollama has been a great experience for me. Do note that you may encounter issues when using Gemma 4. I would recommend monitoring Gemma 4's token usage in the event of Gemma 4 looping itself and burning unnecessary tokens.

 

Verdict:Overall, if you have enough power to run a local LLM and would like to have a model that is smaller but more powerful than other Flagship models to use in your development knowing the limitations of local LLMs in general, then I believe Gemma 4 is right for you!

 

I hope that this Multiversal Analysis has helped you to determine if Gemma 4 is right for you! If you like to learn more about Gemma 4 in detail, you can read here:https://deepmind.google/models/gemma/gemma-4/

Note:Gemma 4 has different model sizes and the conclusion based on the verdicts may not be accurate to your own personal experience.However, I believe these experiences capture the feeling on what to expect when using Gemma 4 and any local AI model in general.

Visit the Google Documentation to learn more:https://ai.google.dev/gemma/docs/core

 

 

# Thank you for Reading!

If you have made it this far, thank you for taking the time to read this article! I hope you have learned something based on our experiences using Gemma 4 in different areas of development.

I would like to give credit to theVirtual Coffee Groupwhere I used their"#co-working"room to meet with Elmar Chavez (@codingwithjiro), Konark Sharma (@konark_13), and Julien Avezou (@javz) for the first time outside of DEV and would love to work with them again in the future!

Check out Virtual Coffee below to see what they do!

## Virtual CoffeeFollow

 Virtual Coffee is a laid-back conversation with developers twice a week. It's the conversation that keeps going in slack. It's the online events that support developers at all stages of the journey.
 

 

Feel free to send us love by following us individually and our DEVenger org!

## The DEVengersFollow

 This is an organization where we assemble the greatest minds the community has ever known! The question isn't "How fast can I code?". The question is "What will I learn from the farthest below?".
 

## FrancisTRᴅᴇᴠ (っ◔◡◔)っFollow

📚 Full-Stack Developer 📚
"A Smooth Sea never made a Skilled Sailor" - Franklin D. Roosevelt

## Julien AvezouFollow

Builder | Software Engineer | Author of The Thinking Engineer Toolkit

## Konark SharmaFollow

I am software engineer who finds fun and creativity in Frontend. I would love to be a part of a team to help, develop and learn from new people and add my knowledge to the project.

## Elmar ChavezFollow

Licensed civil engineer turned full stack developer building accessible, responsive web applications. I also review code in Frontend Mentor and participate in collaborative projects.

 

Challenge #1:Did you find 4 hidden random videos in this article?

Challenge #2:How many"r's"are there in this post in total?

Challenge #3:Who are the anime characters in this article's cover image?

Challenge #4:Based on Challenge 3, who decide to choose those anime characters in this article respectfully?

Any questions/comments? Love to hear your thoughts on Gemma 4! What's your experience on using Gemma 4 and do you recommend it?

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (18 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse
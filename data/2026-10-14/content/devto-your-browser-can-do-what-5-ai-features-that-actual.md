---
title: Your Browser Can Do WHAT?! 5 AI Features That Actually Work - DEV Community
url: https://dev.to/sylwia-lask/your-browser-can-do-what-5-ai-features-that-actually-work-1blb
site_name: devto
content_file: devto-your-browser-can-do-what-5-ai-features-that-actual
fetched_at: '2026-10-14T15:44:23.472285'
original_url: https://dev.to/sylwia-lask/your-browser-can-do-what-5-ai-features-that-actually-work-1blb
author: Sylwia Laskowska
date: '2026-10-14'
description: Are AI models running directly in the browser finally good enough to use in production? Let's find... Tagged with ai, react, javascript, webdev.
tags: '#ai, #react, #javascript, #webdev'
---

Explores WebGPU and hardware limits

Are AI models running directly in the browser finally good enough to use in production? Let's find out! 😉

It's been a week since my talk at FrontKon in Prague. As I mentioned before, it was fantastic! I'm adding a few photos below, just to prove that I actually speak at conferences and don't just make these things up. 😀

My talk was titled"Your Browser Is a Compute Platform (And You're Using It for Forms)", and I showed how we can use WebAssembly and WebGPU to perform advanced computations directly in the browser. I was a little concerned to discover that, out of everyone in the audience, maybe three or four people had even heard of WebGPU! And that's a shame, because WebGPU can accelerate certain types of parallel computations by tens of times compared to CPU-based implementations.

But okay, at least the people at FrontKon know what WebGPU is now. 😁 And if you'd like a talk about this at your conference, feel free to reach out! Especially if your conference happens to take place in a particularly attractive tourist destination. 😀

## Why I'm Revisiting Browser AI

After a conference, I traditionally prepare a blog post related to my talk. However, since I've already written about WebAssembly and WebGPU many times, today I'd like to approach the topic from a different angle. Namely, let's take a look at the current state ofAI models running directly in the browser, which, of course, make extensive use of these technologies. 🙂

Browser-based AI models are a fascinating concept. No inference API calls. No network round trips to an AI backend. No worrying that your users will consume too many tokens, because you're not paying for them! But of course, local inference still takes time, and downloading the model in the first place can take a while.

Another advantage is that these models can work offline once they've been downloaded and cached by the browser, provided the application itself supports offline operation.

And that also brings a significant privacy benefit: inference happens directly on the user's device, so their data doesn't need to be sent to an external AI service.

However, as you can probably imagine, these are relatively small models. We're not going to run a massive frontier-scale model in a typical browser tab.

So the question is:how useful are these smaller models, really?

Some of you may remember that I experimented with browser-based AI models about a year ago. Back then, we were mostly laughing that they were a fun curiosity, but not much more than that.

But I've been following people from Hugging Face who work on Transformers.js on LinkedIn, and every now and then, their demos would appear in my feed. At first glance, some of them looked genuinely impressive. You know, practically spaceships running inside a browser. 😉

So before FrontKon, I decided to take another look at what they had to offer. And it turned out that after upgrading Transformers.js to version 4.3.1, which I used for these experiments, and trying some newer models, the results were genuinely impressive!

Of course, Transformers.js isn't the only option for running AI models in the browser. There are other libraries and runtimes, but I really like Transformers.js, and I think it's a pretty representative example of what this technology can achieve today.

At the same time, I don't work for Hugging Face, and nobody is paying me to sell you a spaceship in your browser. So I'll tell you what browser-based AI models can actually do today, what works well, and what still doesn't.

And even better,you can explore the code and try everything yourself!

GitHub:https://github.com/sylwia-lask/practical-browser-ai

Live demo:https://sylwia-lask.github.io/practical-browser-ai

If you like the project, please give it a star on GitHub. I'm collecting them! 😀

## Can We Actually Use This in Production?

For these demos, I wanted to focus on practical applications. More specifically, I wanted to find out how we could use browser-based AI today, right now, in real production applications.

So is this technology worth paying attention to?In my opinion, absolutely!

But!

I probably wouldn't build a mission-critical system that depends entirely on these models working perfectly. 😉 Instead, I'd treat them as interesting, optional enhancements to existing application features, especially in areas like e-commerce, accessibility, and customer support.

The application itself is nothing particularly exotic, by the way. It's a regularReact application written in TypeScript, usingWeb Workersto run model inference without blocking the main UI thread.

The models are loaded on demand, so you don't need to download all five of them just to open the application. The inference runs locally through Transformers.js, using WebGPU where supported and WebAssembly-based CPU execution where a fallback is available.

No AI backend involved!

Let's see what I managed to build. And at the end, I'll share my thoughts on the limitations of these models.

One more thing: these aren't browser-based AI agents yet. They're simply applications using local AI models for specific tasks. But give me a few more weeks, and you'll see agents running in the browser on my blog too!

## 1. Background Remover

One of the things I particularly appreciate about browser-based AI is that it's not limited to text generation. I love working with multimodal AI!

In this demo, a small model calledRMBG-1.4, with approximately 44 million parameters, does a really impressive job of separating an object from its background. 🙂 The model itself is only about 170 MB to download in the configuration I'm using.

As you can see, we can then save the result as a transparent PNG, and it works surprisingly well!

I can easily imagine this as an additional feature on auction websites or e-commerce platforms.

Imagine someone trying to sell a product but only having a photo like my example. Instead of requiring them to use an external image-editing service, we could simply offer a background removal button directly in the application.

And the photo doesn't even need to leave their device. Pretty cool, isn't it?

One practical note: RMBG-1.4 comes with licensing conditions that should be checked before commercial deployment. So while the technical concept is very promising for e-commerce, you should always verify the model's license before shipping it.

## 2. Alt Text Generator

I've always felt that AI could become another useful layer of accessibility, if we use it properly.

This demo usesFlorence-2-base-ft, a vision model with approximately 230 million parameters, to generate descriptions of images.

Imagine that you're uploading an image to DEV, for example. Instead of having to write an alt text description from scratch, you could use a model like this to generate a suggestion automatically. Especially when you really don't feel like describing what's in the picture!

Of course, the generated description should still be reviewed and edited by a human. Good alt text isn't just about identifying objects in an image. It also depends on the context and purpose of that image.

The model doesn't necessarily understand why you're using the picture, and it can occasionally miss or invent details. Still, as an accessibility assistant, I think this is a very promising approach.

There's also an option to provide additional context, but don't expect too much from it. In my implementation, the extra text is simply appended to the generated description rather than genuinely influencing what the model sees or understands. I'll explain why I wasn't satisfied with this approach later in the article.

For reference, the model download is roughly350–450 MB, depending on the precision supported by the device.

## 3. Smart Ticket Creator

Oh, this one is my dream feature! I describe what's wrong in completely natural, messy language, and the model turns it into a structured ticket that I can send to support. 😀

The model I ended up using isQwen2.5-0.5B-Instruct, a small language model with approximately 500 million parameters. In my configuration, its quantized weights require a download of around786 MB, plus tokenizer files.

And I have to admit something. When I started implementing this feature, I thought it would be the easiest one! Seriously. How difficult could it be for a language model to turn a complaint into a structured ticket?

Well... Apparently, quite difficult! I spent much more time than expected trying different models and getting them to produce the output I actually needed.

The main challenge wasn't just understanding the complaint. It was producing a consistent, structured response with the correct fields, without inventing information or returning malformed JSON. Eventually, I got it working using a carefully designed prompt, output parsing, and schema validation with Zod.

The generated ticket is editable, so the user can review everything before copying or submitting it. And I think that's exactly the kind of approach that makes sense for production: let the AI do the boring initial work, but keep the human in control.

## 4. Semantic Search

Now, this is where small models really shine! For this demo, I implemented semantic search over a collection of support tickets.

Instead of looking for matching keywords, the application searches for tickets with a similar meaning. And, of course, I also included a traditional keyword search so you can compare the results yourself.

I'm usingall-MiniLM-L6-v2, a small embedding model with approximately 22 million parameters. Depending on the backend, its model weights are only about23 MB for the quantized CPU versionor90 MB for the WebGPU version.

And it works really well! The model is fast, and the results are genuinely useful.

Under the hood, it converts the tickets and the search query into numerical vectors, then compares them using cosine similarity. No generative LLM is needed here.

In fact, that's one of the most interesting lessons from these experiments: sometimes a small, specialized model is a much better choice than a general-purpose language model. This is particularly good news for applications where privacy matters and you don't want to send potentially sensitive information to an external server.

For a small collection of documents, this approach is definitely worth testing. Of course, for larger datasets you'd need to think about indexing, storage, and performance. In my demo, the embeddings are kept in memory, which is perfectly sufficient for the example. But the basic idea works surprisingly well.

## 5. Pause & Ask

Okay, this one might be a little less practical, but it's definitely fancy! 😀 And I think it also has interesting accessibility potential. For this demo, I'm usingLFM2.5-VL-450M, a vision-language model with approximately 450 million parameters. The download is roughly350–400 MB, depending on the configuration.

There are actually two features here. The first islive visual description. I turn on my webcam, and the model periodically describes what it sees. Yes, that's me:

But then it gets even better! I can pause the camera on a particular frame and ask the model questions about what it sees.

And here's the example showing that the model isn't exactly perfect. 😅 Although, well, I'm certainly flattered!

I wouldn't treat this as a reliable accessibility tool just yet, but as an experiment in local visual question answering, it's genuinely fascinating.

And that's all five demos!

## So What's the Catch?

Now, as promised, let's talk about the disadvantages. Because, of course, there are quite a few!

### WebGPU Support and Hardware Limitations

First of all, these models run as well as they do largely thanks to WebGPU. This API allows applications to use GPU computing capabilities directly in the browser, which can make a huge difference for machine learning inference.

The problem is thatWebGPU availability and performance aren't the same on every device. Support has improved significantly across modern browsers, but availability still depends on the browser version, operating system, GPU, drivers, etc. And even if WebGPU is supported, that doesn't mean everyone has an equally powerful computer.

Mobile devices are a particularly interesting problem. Some mobile browsers and devices still lack usable WebGPU support for certain workloads. In those cases, some Transformers.js models can fall back to WebAssembly-based CPU inference, potentially using SIMD or multithreading depending on the environment and configuration.

Unfortunately, this can be significantly slower. On my phone, two of the examples from my demo didn't work at all because they timed out. And it's not like I'm using some ancient phone from a museum! It's a Samsung Galaxy S24 FE. Not the newest flagship anymore, but definitely not a dinosaur either.

So yes, WebGPU support is improving, and the models are getting better. But I want to talk about what we can actually useright now, not what might be possible in a few years.

### Model Downloads Aren't Exactly Tiny

There's also another important limitation: the models themselves have to be downloaded. And while some are relatively small, others can require hundreds of megabytes. As you've seen, the models in my demo range from around 23 MB for the quantized semantic search model to nearly 800 MB for the Smart Ticket Creator. That's quite a lot if you're visiting a website on a mobile connection!

Fortunately, browsers can cache the downloaded model files, so subsequent visits usually don't require downloading everything again. But the first load still matters, and browser storage isn't guaranteed to keep those files forever.

That's another reason why I'd treat these features as optional enhancements rather than something every user must load before they can use the application.

### Some Things Still Don't Work Well Enough

I also couldn't implement everything I originally wanted, even though some ideas seemed perfectly reasonable. For example, I tried adding text recognition from images. And despite experimenting with different models and configurations, I couldn't get results that were reliable enough for my demo. The approaches I tested didn't give me the quality I wanted, so I decided not to include that feature.

Another thing I wanted to improve was the contextual information in the alt text generator. Imagine uploading a photo of a dog and adding some additional context, such as: "This dog is available for adoption at a local animal shelter." Ideally, the model would take that information into account and generate a beautiful, context-aware description.

I tried using an additional local language model for this, hoping it could combine the visual description with the extra information. But no matter what I tried, the results were very unsatisfactory. So I ended up with the simpler approach I mentioned earlier, where the context is added separately rather than genuinely interpreted by the image-captioning model.

And that's another good example of why I wouldn't blindly trust these models in production.

### What About Voice Recognition?

On the other hand, I've heard that small browser-based models can be surprisingly good at speech recognition. Transformers.js supports audio-related tasks too, so that's definitely another interesting area to explore.

I didn't test it this time, though. Mostly because I was building these demos in the evenings, and my family would have killed me if I'd spent hours talking to my computer. 😂 Maybe next time!

## My Verdict: Is Browser AI Production-Ready?

So, to sum up:browser-based AI models are getting better, and I think it's already worth exploring how to use them in production applications.

Not necessarily as a replacement for every AI backend. And definitely not as a critical dependency without a fallback. But as optional features that improve the user experience? Absolutely.

What do you think? Have you already experimented with running AI models directly in the browser?

And if you enjoy reading my articles, feel free to follow me onLinkedIntoo! 🙂

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (28 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse
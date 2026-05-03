---
title: Mozilla pushes back against Google's Prompt API • The Register
url: https://www.theregister.com/2026/04/30/mozilla_pushes_back_against_googles/
site_name: tldr
content_file: tldr-mozilla-pushes-back-against-googles-prompt-api-the
fetched_at: '2026-05-03T19:54:57.144720'
original_url: https://www.theregister.com/2026/04/30/mozilla_pushes_back_against_googles/
date: '2026-05-03'
description: Firefox maker torches Google for building Prompt API into browser (7 minute read)
tags:
- tldr
---

#### AI + ML

# Firefox maker torches Google for building Prompt API into browser

 

## Mozilla fears wiring an AI API into Chrome will make the web less open

UpdatedMozilla has reiterated its opposition to Google's decision to build AI plumbing into its Chrome browser, though rather belatedly now that the technology, known as the Prompt API, is already being tested in Chrome and Microsoft Edge.

Jake Archibald, Mozilla web developer relations lead, articulated the org’s concerns ina GitHub discussionof the API, which provides a standard way to send and receive prompts and responses from a local machine learning model.

"We continue to oppose this API, and feel it has severe negative consequences to the interoperability, updatability, and neutrality of the web platform," said Archibald.

ThePrompt API, as Google describes it, "gives web pages the ability to directly prompt a browser-provided language model." It provides a way to send natural language instructions to Google's Gemini Nano model, which is small enough to be downloaded for local inference through Chrome.

It's not that small – Google recommends having 22 GB of space available, though the Nano (v3Nano) model for desktop use is ~4.27 GB.

Web developers already have a variety of ways to interact with AI models. They can use cloud service APIs to communicate with hosted models. Or they can access local models through technologies like JavaScript runtime frameworks, WASM, or WebGPU.

Various vendors like OpenAI and Perplexity have shipped browsers that embed access to remotely hosted AI models. Mozilla itself is testingan AI-based Smart Window in Firefoxand it's developingtools for AI model scaffolding.

The Prompt API aims to make it easier to run local inference in a way that takes advantage of browser security mechanisms, to produce faster response times, to allow offline usage, and to provide more cost effective ways to integrate AI services (e.g. providing a free AI fallback if users lack a paid AI API key).

Mozilla's concern, as articulated by Archibald, has to do with what the Prompt API means for the web, not to mention Google's justification for deployment.

First, he worries that Google's own Nano model will become the default and that developers will standardize on it in an effort to make the non-deterministic responses of an AI model more predictable. That tendency, he argues, will create pressure for Apple and Mozilla to license Nano, for the sake of a common user experience.

Perhaps more significantly, Archibald notes that using the Prompt API requires agreeing to Google'sGenerative AI Prohibited Uses Policy, which prohibits activities that are not necessarily illegal, like generating "disturbing" content.

"This seems like a bad direction for an API on the web platform, and sets a worrying precedent for more APIs that have [browser]-specific rules around usage," he said.

Finally, Archibald argues that Google misrepresented demand for the API by cherry-picking a few social media posts and calling that a groundswell of developer support.

"Theintent to ship on blink-devstates web developers as 'Strongly positive,' and links to the explainer for evidence," he wrote. "The evidence provided there does not seem to fit the claim."

* Hashicorp co-founder Mitchell Hashimoto says GitHub 'no longer a place for serious work'
* Google's fix for critical Gemini CLI bug might break your CI/CD pipelines
* AWS says acute server memory shortage is driving customers to the cloud
* Linux cryptographic code flaw offers fast route to root

In an email, Archibald toldThe Registerthat the question is whether the Prompt API is good for the web, and Mozilla doesn't believe that it is.

"The core problem is interoperability," he said. "Prompts are tightly coupled to models; developers will inevitably tune to the quirks and policies of whatever model they're building against.

"That's how you end up with model-specific code paths, which is the browser-compatibility problem all over again. The T&C issue is part of that: if using a web API means accepting a specific vendor's content policy (especially one that goes beyond law) you're not really building for an open platform anymore."

With regard to Google's exaggeration of developer enthusiasm, Archibald said there are definitely devs interested in AI capabilities but Google failed to provide evidence of that.

"The signal is polarised, not 'strongly positive,'" he explained. "Either way, developer demand alone doesn't meet the bar. The question is whether the API can work across implementations without tying the platform to one vendor's model."

Google did not immediately respond to a request for comment.

However, on Thursday, Rick Byers, the Google Chrome engineer responsible for shipping the Prompt API,chimed into the GitHub discussion to acknowledge the concerns articulated by Archibald.

"As one of the blink API owner approvers for shipping this in Chromium, I admit that I share the concerns here in Mozilla's standards position," he wrote. "Where I differ is in preferring paths that promote experimentation, learning from mistakes, and competition to those which err on the side of stalling innovation out of fear of whatmighthappen."

Byers asked the web community to help collect evidence of harm to advance the discussion. Pointing to the debate over other controversial web technologies likeEncrypted Media Extensions(EME), he suggested the outcome has not been as dire as predicted.

But focusing on data, so far, hasn't done much for Google's cause. According toa reportcreated in February that compares the performance of Chrome (Gemini Nano) and Edge (Phi-4 mini-instruct) using the Prompt API, these models just don't provide very good results.

"For generative tasks (composition, tag generation, etc), 24.29 percent of Edge's and 15.17 percent of Chrome's responses failed to complete the task," the report says, in reference to a rubric that defines failure as a score of 2 or less on a scale of 5. "For classification tasks, 29.58 percent of Edge's and 23.93 percent of Chrome's responses did not label or categorize the input correctly."

In terms of groundedness and accuracy, Edge failed ("hallucinated") 17 percent of the time while Chrome failed 6 percent of the time.

Is that good for the web? You could ask Chrome but you might not get a reliable answer. ®

Updated at 23:45 UTC April 30to add a comment from a Google spokesperson

After this story was filed, a Google spokesperson sentThe Registerthe following comment:

“Part of working in the open is encouraging debate and disagreement. We welcome Mozilla’s feedback and will continue to collaborate with them and the web community as we work to improve the API.”

 

Get our
 
Tech Resources

Share

#### More about

* AI
* Chrome
* Firefox

More like these

×

### More about

* AI
* Chrome
* Firefox
* Web Browser

### Narrower topics

* AIOps
* Brave
* cookies
* DeepSeek
* Gemini
* Google AI
* GPT-3
* GPT-4
* HTTP
* Internet Explorer
* Large Language Model
* Machine Learning
* MCubed
* Microsoft Edge
* Neural Networks
* NLP
* Opera
* Retrieval Augmented Generation
* Safari
* Star Wars
* Tensor Processing Unit
* TOPS
* Vivaldi

### Broader topics

* Chromium
* Google Cloud
* Mozilla Foundation
* Self-driving Car
* Software

#### More about

Share

#### More about

* AI
* Chrome
* Firefox

More like these

×

### More about

* AI
* Chrome
* Firefox
* Web Browser

### Narrower topics

* AIOps
* Brave
* cookies
* DeepSeek
* Gemini
* Google AI
* GPT-3
* GPT-4
* HTTP
* Internet Explorer
* Large Language Model
* Machine Learning
* MCubed
* Microsoft Edge
* Neural Networks
* NLP
* Opera
* Retrieval Augmented Generation
* Safari
* Star Wars
* Tensor Processing Unit
* TOPS
* Vivaldi

### Broader topics

* Chromium
* Google Cloud
* Mozilla Foundation
* Self-driving Car
* Software

#### TIP US OFF

Send us news
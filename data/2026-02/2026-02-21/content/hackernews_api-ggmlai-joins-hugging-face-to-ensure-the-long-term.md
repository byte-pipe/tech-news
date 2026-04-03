---
title: 'ggml.ai joins Hugging Face to ensure the long-term progress of Local AI · ggml-org llama.cpp · Discussion #19759 · GitHub'
url: https://github.com/ggml-org/llama.cpp/discussions/19759
site_name: hackernews_api
content_file: hackernews_api-ggmlai-joins-hugging-face-to-ensure-the-long-term
fetched_at: '2026-02-21T06:00:22.574049'
original_url: https://github.com/ggml-org/llama.cpp/discussions/19759
author: lairv
date: '2026-02-21'
description: ggml.ai joins Hugging Face to ensure the long-term progress of Local AI
tags:
- hackernews
- trending
---

ggml-org



/

llama.cpp

Public

* NotificationsYou must be signed in to change notification settings
* Fork15k
* Star95.5k

# ggml.ai joins Hugging Face to ensure the long-term progress of Local AI#19759

 ggerganov



 announced in

Announcements

 ggml.ai joins Hugging Face to ensure the long-term progress of Local AI


#19759

 ggerganov


Feb 20, 2026

·

 36 comments

·

 9 replies


Return to top



Discussion options



Quote reply



edited

## ggerganovFeb 20, 2026Maintainer



-

## Announcement

We are happy to announce thatggml.ai(the founding team ofllama.cpp) are joiningHugging Facein order to keep future AI truly open.

Georgi and team are joining HF with the goal of scaling and supporting theggml/llama.cppcommunity as Local AI continues to make exponential progress in the coming years.

### Summary / Key-points

* Theggml-orgprojects remain open and community driven as always
* The ggml team continues to lead, maintain and support full-time theggmlandllama.cpplibraries and related open-source projects
* The new partnership ensures long-term sustainability of the projects and will help foster new opportunities for users and contributors
* Additional focus will be dedicated on improving user experience and integration with the Hugging Facetransformerslibrary for improved model support

### Why this change?

Since its foundation in 2023, the core mission of ggml.ai has continuously been to support the development and the adoption of theggmlmachine learning library. Over the past 3 years, the small team behind the company has been doing its best to grow the open-source developer community and to help establishggmlas the definitive standard for efficient local AI inference. This was achieved through strong collaboration with individual contributors, as well as with partnerships with model providers and independent hardware vendors. As a result, todayllama.cpphas become the fundamental building block in countless projects and products, enabling private and easily-accessible AI on consumer hardware.

Throughout this development, Hugging Face stood out as the strongest and most supportive partner of this initiative. During the course of the last couple of years, HF engineers (notably@ngxsonand@allozaur) have:

* Contributed several core functionalities toggmlandllama.cpp
* Built a solid inference server with polished user interface
* Introduced multi-modal support tollama.cpp
* Integratedllama.cppinto the Hugging Face Inference Endpoints
* Improved compatibility of the GGUF file format with the Hugging Face platform
* Implemented multiple model architectures intollama.cpp
* Helpedggmlprojects with general maintenance, PR reviews and more

The teamwork between our teams has always been smooth and efficient. Both sides, as well as the community, have benefited from these joint efforts. It only makes sense to formalize this collaboration and make it stronger in the future.

### What will change forggml/llama.cpp, the open source project and the community?

Not much – Georgi and team will continue to dedicate 100% of their time maintainingggml/llama.cpp. The community will continue to operate fully autonomously and make technical and architectural decisions as usual. Hugging Face is providing the project with long-term sustainable resources, improving the chances of the project to grow and thrive. The project will continue to be 100% open-source and community driven as it is now. Expect your favorite quants to be supported even faster once a model is released.

### Technical focus

Going forward, our joint efforts will be geared towards the following objectives:

* Towards seamless “single-click” integration with thetransformerslibraryThetransformersframework has established itself as the ‘source of truth’ for AI model definitions. Improving the compatibility between the transformers and the ggml ecosystems is essential for wider model support and quality control.
* Better packaging and user experience of ggml-based softwareAs we enter the phase in which local inference becomes a meaningful and competitive alternative to cloud inference, it is crucial to improve and simplify the way in which casual users deploy and access local models. We will work towards making llama.cpp ubiquitous and readily available everywhere, and continue partnering with great downstream projects.

### Long term vision

Our shared goal is to provide the building blocks to make open-source superintelligence accessible to the world over the coming years. We will achieve this together with the growing Local AI community, as we continue to build the ultimate inference stack that runs as efficiently as possible on our devices.

BetaWas this translation helpful?Give feedback.



85


You must be logged in to vote


👍

78



🎉

202



❤️

153



🚀

107



👀

6





All reactions

## Replies:36 comments·9 replies



Comment options



Quote reply

### julien-cFeb 20, 2026



-

welcome@ggerganovand team!

we're happy to get the chance to continue supporting the awesome llama.cpp community 🔥

BetaWas this translation helpful?Give feedback.



24


You must be logged in to vote


❤️

77



🚀

3





All reactions

 7 replies






Show 2 previous replies



Comment options



Quote reply

#### ngxsonFeb 20, 2026Collaborator



-

Excited news for the Local AI community! Thanks for your support, I'm super happy to be part of this journey. Looking forward to shipping even more impactful models and features in a very near future 🚀

BetaWas this translation helpful?Give feedback.


❤️

4



🚀

5





All reactions



Comment options



Quote reply



edited

#### rabbidaveFeb 20, 2026



-

Appreciate y'all immensely; bringing hope and long-term vision for local-first technology to plebeians 👑

BetaWas this translation helpful?Give feedback.


👍

1





All reactions



Comment options



Quote reply

#### giladgdFeb 20, 2026



-

Wanted to use this opportunity to say that you guys rock!@ggerganov@ngxson@allozaur@pwilkin@CISC@0cc4m@JohannesGaessler@jeffbolznv@am17an@max-krasnyansky@slaren@ericcurtinThank you for all the great work you do pushing llama.cpp forward! ❤️

I don't usually mass tag like this (sorry if I forgot to tag someone), just wanted to show my appreciation for your hard work and dedication on this project that I personally noticed every other day for the past few years. Thank you!

BetaWas this translation helpful?Give feedback.


👍

1



❤️

3





All reactions



Comment options



Quote reply



edited

#### ericcurtinFeb 20, 2026Collaborator



-

Thank you@giladgdalthough I'm not going to take credit for this :)

These days my goal is to ensure Docker Model Runner never forks llama.cpp or related ggml projects (there was a minor fork which I pushed hard to abolish and succeeded, the final PR went in not that long agodocker/model-runner#541) and upstreams first when necessary, the golang layer is important for distributing models via OCI registries.

BetaWas this translation helpful?Give feedback.



All reactions



Comment options



Quote reply

#### SolidoFeb 20, 2026



-

sacré mov@julien-c!

BetaWas this translation helpful?Give feedback.



All reactions



Comment options



Quote reply

### allozaurFeb 20, 2026Collaborator



-

LEEET'S GOOOOOOOO!!!

It's been such an honour and privilege to work on llama.cpp and this is the best news for the truly open AI ecosystem and democratising local AI.

BetaWas this translation helpful?Give feedback.



3


You must be logged in to vote


👍

1



❤️

15





All reactions

 0 replies




Comment options



Quote reply

### pwilkinFeb 20, 2026Collaborator



-

That's really cool! Great news for@ggerganovand the team!

BetaWas this translation helpful?Give feedback.



4


You must be logged in to vote


👍

1



❤️

7





All reactions

 0 replies




Comment options



Quote reply

### hoverflowFeb 20, 2026



-

congrats!

BetaWas this translation helpful?Give feedback.



2


You must be logged in to vote


👍

4





All reactions

 0 replies




Comment options



Quote reply

### EAddarioFeb 20, 2026



-

Congratulations to the entireggml.aiteam and what a fantastic move by HF!

BetaWas this translation helpful?Give feedback.



1


You must be logged in to vote


👍

1



❤️

2





All reactions

 0 replies




Comment options



Quote reply

### ddh0Feb 20, 2026



-

Wahoo!

BetaWas this translation helpful?Give feedback.



2


You must be logged in to vote


❤️

2





All reactions

 0 replies




Comment options



Quote reply

### MihaiiiFeb 20, 2026



-

This is awesome! Congrats! 🇪🇺🇪🇺🇪🇺

BetaWas this translation helpful?Give feedback.



1


You must be logged in to vote



All reactions

 0 replies




Comment options



Quote reply

### steampunqueFeb 20, 2026



-

Great to hear this news, congrats all around to the entire team and thanks to everyone for all your dedicated efforts over the years!

BetaWas this translation helpful?Give feedback.



2


You must be logged in to vote



All reactions

 0 replies




Comment options



Quote reply

### JohannesGaesslerFeb 20, 2026Collaborator



-

Good to hear that you managed to secure a partnership for the sustainability of the project! Though I am not part of the formal ggml organization I will happily continue to cooperate on our shared goals.

BetaWas this translation helpful?Give feedback.



3


You must be logged in to vote


👍

6



❤️

2





All reactions

 1 reply




Comment options



Quote reply

#### ggerganovFeb 20, 2026MaintainerAuthor



-

Thank you, Johannes! I am grateful for your major contributions to the project and I enjoy our closer collaboration lately.

BetaWas this translation helpful?Give feedback.


❤️

3





All reactions



Comment options



Quote reply

### davanstrienFeb 20, 2026



-

Very excited about this!

BetaWas this translation helpful?Give feedback.



5


You must be logged in to vote



All reactions

 0 replies




Comment options



Quote reply

### ali0uneFeb 20, 2026



-

Congrats. All the best for this wonderful project. Keep up the good work!Love you guys ❤️

BetaWas this translation helpful?Give feedback.



2


You must be logged in to vote



All reactions

 0 replies




Comment options



Quote reply

### giladgdFeb 20, 2026



-

This is amazing news!HuggingFace seems like a natural fit for the projects and the community

BetaWas this translation helpful?Give feedback.



2


You must be logged in to vote



All reactions

 0 replies




Comment options



Quote reply

### danielhanchenFeb 20, 2026



-

Congrats Georgi, GGML team and Hugging Face! This is amazing news.

Llama.cpp is what made open-source local AI what it is today. Excited to see what's coming 🎉🦙

BetaWas this translation helpful?Give feedback.



6


You must be logged in to vote


🎉

2



❤️

10





All reactions

 0 replies




Comment options



Quote reply



edited

### ericcurtinFeb 20, 2026Collaborator



-

Congrats to all at GGML and Hugging Face. Excited to see all the GGML efforts move from strength to strength. Glad to see Hugging Face as the acquiring company, I trust the community will remain strong.

BetaWas this translation helpful?Give feedback.



3


You must be logged in to vote



All reactions

 1 reply




Comment options



Quote reply



edited

#### ericcurtinFeb 20, 2026Collaborator



-

I like the long term vision@ggerganovmakes in the announcement here. Future directions make a lot of sense.

BetaWas this translation helpful?Give feedback.


👍

1





All reactions



Comment options



Quote reply

### davidmezzettiFeb 20, 2026



-

Congratulations on this news! All the best.

It will be great to have strong Python support for llama.cpp. The current options are limited to either hosting via API (llama.cpp, vllm, ollama etc) or using the largely unmaintained llama-cpp-python library.

BetaWas this translation helpful?Give feedback.



1


You must be logged in to vote



All reactions

 0 replies


 6 hidden items


 Load more…




Comment options



Quote reply

### jedisct1Feb 20, 2026



-

Awesome news!

BetaWas this translation helpful?Give feedback.



1


You must be logged in to vote



All reactions

 0 replies




Comment options



Quote reply

### AIWintermuteAIFeb 20, 2026



-

Congrats, looks like a very good match! Happy it's not some other company with "Open" in the name ;)

BetaWas this translation helpful?Give feedback.



1


You must be logged in to vote



All reactions

 0 replies




Comment options



Quote reply

### jeremyfowersFeb 20, 2026



-

Congratulations!

Better packaging and user experience of ggml-based software

We've put a large amount of work this past year into packaging ggml-based software into the open sourceLemonade project, which now auto-configures llama.cpp, whisper.cpp, and stable-diffusion.cpp through a unified installer on Windows and Linux (macOS in beta).

Our mission has been to make it as easy as possible to get started with open software on AI PCs. Please let me know if there's any way Lemonade can be a part of the packaging and user-experience journey here.

BetaWas this translation helpful?Give feedback.



8


You must be logged in to vote


🎉

4





All reactions

 0 replies




Comment options



Quote reply

### MediaeaterFeb 20, 2026



-

congrats!

BetaWas this translation helpful?Give feedback.



1


You must be logged in to vote



All reactions

 0 replies




Comment options



Quote reply

### aldehirFeb 20, 2026Collaborator



-

Congratulations on the partnership!

BetaWas this translation helpful?Give feedback.



1


You must be logged in to vote



All reactions

 0 replies




Comment options



Quote reply

### YetheSamartakaFeb 20, 2026



-

Awesome, congrats 👍🏻

BetaWas this translation helpful?Give feedback.



1


You must be logged in to vote



All reactions

 0 replies




Comment options



Quote reply

### ckastnerFeb 20, 2026Collaborator



-

This is fantastic news, congratulations!

BetaWas this translation helpful?Give feedback.



1


You must be logged in to vote



All reactions

 0 replies




Comment options



Quote reply

### DeleMikeFeb 20, 2026



-

Let’s goo✨❤️

Really loved your work and I used in a project I calledScout

BetaWas this translation helpful?Give feedback.



1


You must be logged in to vote



All reactions

 0 replies




Comment options



Quote reply

### terribleplanFeb 20, 2026



-

Glad you got your bag, but please try not to get too distracted bytransformers. The state and direction of the traditional AI ecosystem is one of the reasons this project was so different and interesting.

BetaWas this translation helpful?Give feedback.



1


You must be logged in to vote



All reactions

 0 replies




Comment options



Quote reply

### mixer3dFeb 20, 2026



-

Congratulations! 🎉

BetaWas this translation helpful?Give feedback.



1


You must be logged in to vote



All reactions

 0 replies




Comment options



Quote reply

### kamendFeb 20, 2026



-

Great news, congratz! 🥳

BetaWas this translation helpful?Give feedback.



1


You must be logged in to vote



All reactions

 0 replies




Comment options



Quote reply

### raishishFeb 20, 2026



-

Great to see this, congratulations 🎉

BetaWas this translation helpful?Give feedback.



1


You must be logged in to vote



All reactions

 0 replies




Comment options



Quote reply

### dobriakFeb 20, 2026



-

Congratulations!Also, glad it wasn't someone more sinister to snag you

BetaWas this translation helpful?Give feedback.



1


You must be logged in to vote



All reactions

 0 replies




Comment options



Quote reply

### mcraveiroFeb 20, 2026



-

Amazing news, congrats guys, more than deserved. Thanks for all your hard work so far. One minor question though, I was a bit confused with this though to be fair I do not know too much about llama.cpp's internals:

Towards seamless “single-click” integration with thetransformerslibraryThe transformers framework has established itself as the ‘source of truth’ for AI model definitions. Improving the compatibility between the transformers and the ggml ecosystems is essential for wider model support and quality control.

Isn't this a python library? I thought llama.cpp aimed at remaining lean and mean c++ only.

Thanks for your time

BetaWas this translation helpful?Give feedback.



1


You must be logged in to vote



All reactions

 0 replies




Comment options



Quote reply

### MainframeworkFeb 20, 2026



-

Congratulations, you deserve it. Still can´t thank you enough for the great work and contributions.P.S: Huggingface just got lucky :)

BetaWas this translation helpful?Give feedback.



1


You must be logged in to vote



All reactions

 0 replies


Sign up for free

to join this conversation on GitHub
.
 Already have an account?

Sign in to comment

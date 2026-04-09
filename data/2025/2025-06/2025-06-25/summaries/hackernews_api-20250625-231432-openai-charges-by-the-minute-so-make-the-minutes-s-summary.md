---
title: OpenAI Charges by the Minute, So Make the Minutes Shorter • George Mandis
url: https://george.mand.is/2025/06/openai-charges-by-the-minute-so-make-the-minutes-shorter/
date: 2025-06-25
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-06-25T23:14:32.417558
---

# OpenAI Charges by the Minute, So Make the Minutes Shorter • George Mandis

**Analysis**

The author is looking to automate the process of getting video content transcribed into text using their existing solo developer skills in Python. They plan on implementing the following steps:

1. Extracting audio from the video using `yt-dlp` and creating a low-bitrate MP3 version at 3x speed
2. Sending the MP3 file to OpenAI for transcription
3. Using `llm` (LLaMA) to sum up the main points of the video

Several benefits are discussed, including:

* Faster and cheaper transcriptions with high quality
* Time-saving without sacrificing quality
* Increased productivity and efficiency
* No need for additional software or subscriptions

**Market Indicators**

* According to the article, OpenAI charges users by the minute
* The author mentions that video content can generate significant revenue through advertising (there is no specific revenue mention in the provided text)
* Growth metrics are not discussed, but a willingness to pay for high-quality transcriptions is implied
* Existing competition is mentioned with regards to automated transcription from YouTube

**Technical Feasibility**

* Creating an MP3 file at 3x speed: This can be done by using `ffmpeg` with optimized settings and multiple processing threads
* Transcribing the audio data into text using LLaMA: While not explicitly supported in the article, it's possible to use OpenAI Models, such as the 'gpt-4o-transcribe' model, to achieve high-quality transcriptions

**Business Viability Signals**

* Willingness to pay for high-quality transcriptions
* Existing competition (e.g. YouTube provides built-in automated transcription)
* Distribution channels (e.g. online stores or platforms hosting video files)

**Actionable Insights**

* To build a profitable solo developer business:
	+ Implement this script multiple times, testing different settings and configurations.
	+ Experiment with optimizing `ffmpeg` and LLaMA for faster and cheaper transcriptions.
	+ Consider offering additional services (e.g. audio-to-text transcription) to increase revenue.
	+ Research online stores or platforms hosting video files where your content can be distributed.

**Specific Numbers**

* YouTube provides built-in automated transcription, which may not be a viable option due to the author's concerns about accuracy and willingness to pay.
* The script costs $0.00 since it uses command-line tools (e.g. `yt-dlp`) that are free or low-cost.

**Quotes**

* "I just wanted the TL;DW (tease down) of an AI summary" - The author mentions their use case for dumping something into an LLM to get the gist of it and walk away.
* "If ever there were a use-case for dumping something into an LLM to get the gist of it..." - This sentence highlights the author's concerns about using OpenAI Models for general use cases.

**Tone and Style**

The tone is informal, conversational, and friendly. The style is clear and concise, with a focus on providing actionable insights for building a profitable solo developer business.

Overall, this article provides valuable information for aspiring solo developers interested in automating video content transcriptions using Python.

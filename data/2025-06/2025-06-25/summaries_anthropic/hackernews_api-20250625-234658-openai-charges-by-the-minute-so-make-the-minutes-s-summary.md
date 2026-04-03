---
title: OpenAI Charges by the Minute, So Make the Minutes Shorter • George Mandis
url: https://george.mand.is/2025/06/openai-charges-by-the-minute-so-make-the-minutes-shorter/
date: 2025-06-25
site: hackernews_api
model: anthropic/claude-3-haiku-20240307
summarized_at: 2025-06-25T23:46:58.000697
---

# OpenAI Charges by the Minute, So Make the Minutes Shorter • George Mandis

Here's a 3-4 paragraph analysis of the article from a solo developer business perspective:

The article discusses an interesting problem and opportunity for solo developers - how to make OpenAI transcriptions faster and cheaper. The key insight is that by simply speeding up the audio input before sending it to OpenAI's API, you can reduce the number of audio tokens and therefore the cost, with minimal impact on transcription quality.

The market indicators are quite promising. The author was able to achieve a 33% price reduction on input tokens by speeding up the audio 3x, which speaks to the willingness of users/businesses to pay for this optimization. Additionally, the fact that the output token count remained the same suggests the summarized transcription maintains its value. This points to a clear customer pain point around the cost and time of transcription services that a solo developer could potentially address.

From a technical feasibility standpoint, the solution outlined is relatively straightforward for a skilled solo developer. The script provided uses common tools like ffmpeg and yt-dlp, which a solo dev could likely implement and automate with some effort. The key skills required would be audio/video processing, API integration, and some scripting/automation. While not trivial, this seems within reach for many solo developers, especially those with experience in media processing and working with AI/ML services.

The business viability signals are also quite positive. The author notes that the bulk of the transcription costs come from the output tokens, which are priced at $10 per 1M tokens. This suggests there is room for a solo developer to offer a competitively priced service, especially if they can further optimize the transcription process. Additionally, the lack of obvious competition in this specific optimization area indicates there may be an opportunity for a solo dev to carve out a niche in this market.

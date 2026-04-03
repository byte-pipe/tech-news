---
title: 'Building my MVP: Glyph — Your AI-Powered Writing Assistant - DEV Community'
url: https://dev.to/isah_alamin_93d4e4d2ab01f/building-my-mvp-glyph-your-ai-powered-writing-assistant-3e83
site_name: devto
fetched_at: '2026-01-05T11:07:33.595916'
original_url: https://dev.to/isah_alamin_93d4e4d2ab01f/building-my-mvp-glyph-your-ai-powered-writing-assistant-3e83
author: Isah Alamin
date: '2026-01-04'
description: This is a submission for the DEV's Worldwide Show and Tell Challenge Presented by Mux What... Tagged with devchallenge, muxchallenge, showandtell, video.
tags: '#devchallenge, #muxchallenge, #showandtell, #video'
---

DEV's Worldwide Show and Tell Challenge Submission 🎥

This is a submission for theDEV's Worldwide Show and Tell Challenge Presented by Mux

## What I Built

I built the MVP of my startup called Glyph.

Glyph is a word editor with an AI assistant that can:

* Write for you from scratch
* Edit text however you like
* Answer questions about what you're writing
* Let you write yourself if you prefer

You can also upload videos (like meetings or lectures) and get a clean transcript right in the editor.

## My Pitch Video

## Demo

Live Demo:https://glyph-ochre.vercel.app

Test Credentials for Judges:

* Email:test@glyph.com
* Password:GlyphTest2026

📝 Important Demo Notes for Judges:

* For the best experience, please use adesktop or laptop browser.
* Thevideo-to-text featurerequires a direct, public URL to a video file (e.g.,.mp4,.mov).It does not support:YouTube links, private videos, or files behind authentication.
* It does not support:YouTube links, private videos, or files behind authentication.
* To make testing easy, here are a few sample video URLs you can use:http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/WeAreGoingOnBullrun.mp4https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/SubaruOutbackOnStreetAndDirt.mp4
* http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/WeAreGoingOnBullrun.mp4
* https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/SubaruOutbackOnStreetAndDirt.mp4

## The Story Behind It

As a student and developer, I constantly write blogs, emails, assignments, documentation. I also worked at a company where I dealt with a lot of typing, and I knew how stressful it was. I've felt the frustration of the blank page, the inefficiency of jumping between research tabs, and the time lost manually transcribing meeting notes.

You spend hours typing and thinking: "What word comes next? Where should this punctuation mark go?" It's hard figuring out what words come after the next word, where to put punctuation marks.

I've always wanted something to help something accessible I could use without installing, that was affordable and actually solved my problem. Many experiences like this led me to creating Glyph.

It is my solution to make writing faster, less stressful, and more focused on ideas rather than mechanics.

## Technical Highlights

Glyph is a full-stack web application built for clarity and speed.

* Frontend:A responsive interface built with vanilla HTML/CSS/JavaScript, usingTipTapas the core rich-text editor for a smooth, native writing feel.
* Backend:Django handles API logic, user session management, and orchestrates between services.
* AI Engine:For this MVP, I'm using the Groq API with the Llama 3 model. I prioritized cost efficiency by using a lightweight LLM that handles basic text operations well. This keeps the app free for users while we validate the concept. We can easily swap to GPT-4 or Claude for production if needed.
* Video Intelligence:This is whereMuxshines. The backend uses the Mux Video API and its AI-powered auto-captioning to asynchronously process uploaded videos, returning clean, structured transcripts directly into the Glyph editor.

The Vision:This MVP validates the core workflow. The roadmap includes more advanced AI models, real-time collaboration, image-to-text analysis, and deeper document management features.

### Use of Mux (Additional Prize Category Participants Only)

Mux was the MVP behind my MVP (pun intended 😄). I used it for the video-to-text feature — and this is definitely a feature I'm keeping.

How It Works:When you upload a video in Glyph, here's the code that makes it work:

# Create a Mux asset with auto-generated English captions

create_payload

=

{


"
input
"
:

[


{


"
url
"
:

video_url
,


"
generated_subtitles
"
:

[


{


"
language_code
"
:

"
en
"
,

# English captions


"
name
"
:

"
English CC
"


}


]


}


],


"
playback_policy
"
:

[
"
public
"
]

}

# POST to Mux API

create_response

=

requests
.
post
(


'
https://api.mux.com/video/v1/assets
'
,


headers
=
headers
,


json
=
create_payload

)

Enter fullscreen mode

Exit fullscreen mode

I integrated the Mux Video API to handle the entire "video-to-document" pipeline:

1. A user provides a public video URL in Glyph.
2. My Django backend creates a Mux Asset with a request for auto-generated captions (generated_subtitles).
3. I listen for thevideo.asset.track.readyfrom Mux to know when the transcript is ready.
4. Once ready, my backend fetches the plain-text transcript from Mux and injects it as a beautifully formatted draft into the user's Glyph editor.

Why This Matters:

This isn't just a transcript feature. Here's how it blends perfectly with Glyph's AI writing tools:

📝 Blog from Video:Record a product demo → Get transcript → Ask Glyph "Turn this into a blog post" → Publish in minutes.

🎓 Research Made Easy:Have a 2-hour lecture recording? Get the transcript → Ask "Summarize key points" → Use Glyph to expand into research notes.

💼 Meeting Magic:Team meeting recorded → Get action items → Use Glyph to draft follow-up emails and project plans.

✍️ Content Repurposing:Podcast episode → Transcript → Glyph helps turn it into tweets, LinkedIn posts, and newsletter content.

Why This Blends Perfectly with Glyph:

Most tools stop at transcription. Glyph makes the transcript actionable. You can:

Immediately edit it with AI commands

Ask questions about specific parts

Transform it into any format you need

All within the same clean interface

The Experience:

Building this was remarkably straightforward. Mux's documentation is clear, their APIs are intuitive, and it fits perfectly into a user-friendly flow. What could have been a complex, weeks-long integration was up and running in a matter of days, allowing me to focus on the unique user experience Glyph provides around that transcript. This feature is a core part of Glyph's value proposition and wouldn't be in this MVP without Mux.

Shoutout to Mux!

A Personal Note:If Glyph resonates with you, I'd be incredibly grateful if you joined the waitlist via the link on the login page. Your interest helps guide what I build next. Feel free to reach out here on DEV with any questions or feedback!

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse

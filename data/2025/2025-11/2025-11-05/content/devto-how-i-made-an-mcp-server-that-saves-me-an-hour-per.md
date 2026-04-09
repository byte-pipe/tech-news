---
title: How I Made an MCP Server That Saves Me an Hour per Week - DEV Community
url: https://dev.to/googleai/how-i-made-an-mcp-server-that-saves-me-an-hour-per-week-3k8k
site_name: devto
fetched_at: '2025-11-05T11:07:43.186426'
original_url: https://dev.to/googleai/how-i-made-an-mcp-server-that-saves-me-an-hour-per-week-3k8k
author: Kaslin Fields
date: '2025-10-29'
description: Recently, I’ve been travelling around the country to help engineers learn how to build MCP Servers... Tagged with ai, mcp, serverless, productivity.
tags: '#ai, #mcp, #serverless, #productivity'
---

Recently, I’ve been travelling around the country to help engineers learn how to build MCP Servers and AI Agents serverlessly on Cloud Run in ourAccelerate AI with Cloud Run workshops. Attendees often ask, how can I use what I learned inmyuse case? This blog tells the story of how I used thefirst hands-on lab from that workshopto build something that saves me time and effort in my real day-to-day work!

As a co-host of theKubernetes Podcast from Google, I love the conversations and learning about cool technology and use cases. But like with any content series, there’s so much time and effort that goes into running and publishing each episode. In this article, I explainhowandwhyI built an MCP server to simplify and speed up our publishing process. You can also try out my solution yourself by checking out thecode for my podcast-assistant-mcp server on GitHub!

## Making Podcast Publishing Faster and Easier

There are a lot of steps involved with running a podcast: picking guests and topics, scheduling interviews, editing episodes, etc, etc. You might think that publishing should be the fastest part of the process- you just click a button and it’s out, right?! Alas, dear reader, how I wish it were so quick and easy.

For every episode, our publishing workflow looks something like this:

1. Listen to the episode for quality and write show notes.(This step is perhaps the most time-consuming and high-active-effort step in the whole process, really).
2. Upload the final audio to our publishing platform and fill out all the metadata fields (show notes, tags, etc.)
3. Updatekubernetespodcast.comby opening a pull request in the repo (our site is built withHugo).
4. Promote the new episode on social media (X, LinkedIn, BlueSky, Reddit, etc.).

The sheer number of manual steps in our publishing process makes it a significant time sink. I needed a better way, and I saw an opportunity for AI to help.

### Step 1: An AI-Based Script

AI excels at summarizing and transforming content. Many of the most time-consuming aspects of our publishing workflow are essentially summarization tasks. This presented a clear opportunity to leverage AI for drafting publishing artifacts such as show notes and social media posts.

To test out my theory that AI could save me time with these summarization steps, I created a simple Python script that:

* Took an audio file as input.
* Used AI to convert the audio to a transcript.
* Used the transcript to generate drafts of show notes and social media posts

With just a quick Python script, I significantly reduced the time I was spending meticulously listening to episodes to write down show notes. While I still review and edit everything I publish, the AI-drafted show notes give me something to work off of, minimizing the need for frequent note-taking pauses while listening to the episode for quality. Additionally, the social media drafts streamlined the preparation of posts for publishing. I began using the script regularly in early 2025 and it consistently saved 1.5-2 hours per episode, becoming an integral part of my publishing process over the last several months.

But there was a problem. You see, I’m not the only host for the Kubernetes Podcast, and I’m not always the one doing the publishing. The issue with my wonderful time-saving script was:** I was the only one using it!** Sure, I shared the script with my co-hosts, but its lack of integration into their existing publishing workflow meant they weren't leveraging it to reclaim valuable publishing time.

### Step 2: From Local Script to Shareable MCP Server

With a new goal aimed at saving my co-hosts time, I started to explore ways to share my automation more effectively, and to expand the initial script to further optimize our publishing workflow.

Initially, I envisioned a comprehensive, wizard-style web application that would manage the entire process, incorporating a "human in the loop" review step. This approach would centralize our publishing tools and processes, streamlining onboarding for new hosts.

Then I had to deal with reality:

* I’m a Kubernetes/Cloud Infrastructure expert - I don't have the front-end skills to build a multi-step web app quickly!
* Many of the APIs required to publish to all our platforms are not readily available. 😞

Ultimately, I lacked the time to develop such a comprehensive solution. Thus, I came back to the age-old wisdom: prioritizing simplicity. To solve my problem, I really needed a system that my team could easily adopt to achieve immediate time savings. And thinking about the longer term, I sought an extensible architecture, something that would allow me to incrementally build out the ideal publishing process as time permits.

The Solution:Create an MCP (Model Context Protocol) server! This approach had several key benefits:

* It's a simple user interface, mostly implemented in backend code (no need to learn frontend languages or libraries).
* It integrates with theGemini CLI, which our team already uses. This meant no new tools for them to learn or add to their workflows!
* It's super extensible!I can add new tools (like generate_hugo_post or publish_to_platform_x) one by one, incrementally, when I have the time.
* Leveraged existing work: I utilized two existing pieces of content to build this MCP server fast:I was able to reuse the MCP Server design and deployment methodology from the first hands-on lab from ourAccelerate AI with Cloud Run workshop series, which demonstratesrunning a secure MCP server on Cloud Run.And to customize it to my use case, I converted the Python script I had already developed into an MCP server. The conversion was amazingly easy- I just integrated the FastMCP library and modified the output mechanism to ensure each function independently saved its output to a storage bucket.
* I was able to reuse the MCP Server design and deployment methodology from the first hands-on lab from ourAccelerate AI with Cloud Run workshop series, which demonstratesrunning a secure MCP server on Cloud Run.
* And to customize it to my use case, I converted the Python script I had already developed into an MCP server. The conversion was amazingly easy- I just integrated the FastMCP library and modified the output mechanism to ensure each function independently saved its output to a storage bucket.

## How the Podcast Assistant MCP Server Works

I built the server, which I call my podcast-assistant-mcp, using FastMCP and Google's GenAI libraries, all containerized via Docker and ready for deployment toCloud Run.

### The Stack

The project is straightforward. Just like inthe lab, I use thecommand line tool uvto manage my dependencies, which means I have apyproject.toml filethat defines the key dependencies:

* FastMCP: For creating the MCP server itself.
* google-genai: To interact with theGemini 2.5 Flash model on Vertex AI.
* google-cloud-storage: For reading audio files and writing the text outputs to a GoogleCloud Storage Bucket.

### The MCP Server Tools

When I created the code for this project as a Python script, it was designed to be sequential, where the output of one tool serves as input for the next. In an MCP server, each component can be called independently, which offers more flexibility. For instance, if we’ve already created a shownotes file manually (which we do occasionally), or if you already have a transcript and you want to use it to generate social media & blog posts (which we might do for old episodes), the AI Podcast Assistant is flexible enough to assist with any specific part of the publishing process it supports. It can also still do everything it has tools for, and knows how to do them in a sensible order! This flexibility will be even more useful as we develop more tools for the server.

This projectconsists of 3 main files, aserver.pythat defines the MCP server itself, and aDockerfileandpyproject.toml filefor deployment.

Theserver.py filedefines 4 main tools, and theREADMEincludes instructions to make them**accessible via theGemini CLI. As a rule, we ***treat all generated content as a first draft*- we make sure to carefully review and edit anything we’re going to publish.

#### Function 1. generate_transcript(audio_file_uri: str, episode_name: str) -> str

This is the starting point. It takes a GCS URI for an .mp3 or .wav file and uses a detailed prompt to transcribe it. The prompt is specific, asking for speaker labels and timestamps, which is crucial for making show notes that I can thenconfirm the quality of, either by hand, or with a quality evaluation tool. It then saves the transcript to GCS and returns the new URI.

#### Function 2. generate_shownotes(transcript_gcs_uri: str, episode_name: str) -> str

This tool takes the transcript's GCS URI. In our production server, it uses a prompt specifically tailored to our podcast's style, which means a shownotes file in markdown format, that essentially consists of a set of links to relevant additional materials for anyone who wants to learn more about the technologies mentioned in the episode.

For the GitHub repo, I used a slightly more generic take on the show notes concept that summarizes the episode. If you want to try using this for yourself, you can always edit the prompt to make it work differently! Whether in our production environment or if deployed from the repo, this function saves the markdown show notes file to GCS and returns that file's URI.

#### Function 3. generate_blog_post(transcript_gcs_uri: str, episode_name: str) -> str

The third function takes the transcript and generates a full, engaging blog post in Markdown format, saving the result to GCS. This is where that MCP server extensibility comes into play a little bit, because currently,kubernetespodcast.comdoes not host a blog. We want to implement one at some point in the future. The drafts generated by this tool should work as a handy starting point some day when we have that blog page ready. We’ll use this function’s outputs as a starting point so we can spend more time on ensuring accuracy, linking to relevant reference material, and making sure the main points in the episode come across in blog form.

#### Function 4. generate_social_media_posts(transcript_gcs_uri: str, episode_name: str) -> str

Finally, the fourth tool in this MCP server generates formatted drafts for X (under 280 characters) and LinkedIn, based on the transcript. And as with all the outputs from this MCP server, we review these and edit them before publishing.

### Deployment

The whole point of implementing this as an MCP server is to share it with my co-hosts, which means deploying it on Cloud Run with authentication required - which means anyone can use it- as long as we tell them how! This should also make onboarding new hosts easier, especially as we implement more pieces of our publishing process as tools. For deployment, we have a simple Dockerfile for containerization, and a pyproject.toml file for handling dependencies.

## Making It Right: Design Choices

There are several choices that I made intentionally when designing this project. If you’re considering building your own MCP server, you might want to keep these considerations in mind.

### Selecting the Right Model

My initial script utilized Gemini 2.5 Pro, a powerful model for content generation. However, I encountered an issue where the Gemini CLI would time out while awaiting the tool's output. After unsuccessful troubleshooting of potential timeout configuration changes, I switched to Gemini 2.5 Flash on Vertex AI. Flash proved sufficiently fast to complete generation and save-to-bucket operations within the client's timeout limit, enabling reliable workflow execution. While other models are viable, Gemini 2.5 Flash is currently my preferred choice for this application. \

### FastMCP Tools vs Prompts

As a key dependency, FastMCP offers a feature allowing developers to register a prompt instead of a full tool. For a workflow like this, where the primary action involves taking a single input (the transcript URI) and generating a single, non-chainable output (e.g., show notes, blog posts, social media updates), a configured prompt might appear to be an ideal solution. Given that these tools are already integrated with an AI Model, it would logically follow to leverage that AI for the desired content generation.

However, the primary objective of the Podcast Assistant extends beyond content generation to long-term content persistence in a storage bucket. The prompt feature is designed to output generated text directly to the user, typically via the Gemini CLI. For this server, generated text must be saved to a Google Cloud Storage (GCS) bucket, enabling its use in subsequent steps or easy download by co-hosts. Therefore, I opted to implement full tools—despite their increased complexity—as they provide the explicit control required for output storage and saving the GCS URI for the next step in the workflow.

### Security in the Form of Authentication via Cloud Run

The ability to share this MCP server with my co-hosts is what makes it a great solution - but I don’t want to pay the bill for everyone in the world to use it! That’s why I wanted to maintain the spirit of the original codelab, “How to deploy asecureMCP server on Cloud Run,” and require authentication to use my MCP server.

There are ways to set up Auth at the MCP Server level, but I’m lazy and that sounded like more code, so I wanted to make use of the authentication at the Cloud Run level, which I did by deploying with the gcloud cli flag of “--no-allow-unauthenticated.”

In the codelab, authentication is handled essentially on a per-session basis by having the end user configure an ID Token that expires after 1 hour. This is fine for my podcast use case too, since I can add the ID Token creation as part of our publishing workflow, and actually using the server’s tools shouldn’t take more than a few minutes. But I also wanted to explore options that would be smoother for my limited number of intended users.

Inthe README for my podcast-assistant-mcp server, I outline three different authentication options:

* Option 1: Using an authentication token with Gemini CLI:This method is quick to set up and is useful for temporary access to the MCP server. The token is valid for one hour.
* Option 2: Using a proxy with Gemini CLI:This method is more robust and is recommended for continuous development. The proxy automatically handles authentication and forwards requests to the MCP server.
* [Example] Option 3: Using a service account: Options 1 & 2 involve authenticating as a user via Gemini CLI. This method involves authenticating as a service or agent (rather than a user) via a service account. This project does not include such a service or agent, so this option is provided as an example for reference, and is not immediately usable just from deploying this project.

For my use case, either Option 1 or 2 will work fine. I might test out both with my co-hosts and see what they like better. Our preference and needs might also change as we continue to expand the MCP server’s capabilities.

## Conclusion: A Workflow That Works

While I still aspire to build a fully integrated, comprehensive solution, this MCP server is a practical tool thatworks,integrates into our team's usual workflow, and isextensible, allowing me or my co-hosts to add more functionality as needed, benefiting everyone.

This project has consistently saved significant time for me over the last several months. Now, my co-hosts can readily utilize it directly from their Gemini CLI, collectively saving valuable time that can be redirected to producing future episodes. Check out the straightforward, three-file implementation of this MCP server inthis GitHub repository, and get started building your own useful, time-saving MCP servers!

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse

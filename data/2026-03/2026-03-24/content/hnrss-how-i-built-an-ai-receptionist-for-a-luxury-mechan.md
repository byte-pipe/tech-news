---
title: How I Built an AI Receptionist for a Luxury Mechanic Shop - Part 1
url: https://www.itsthatlady.dev/blog/building-an-ai-receptionist-for-my-brother/
site_name: hnrss
content_file: hnrss-how-i-built-an-ai-receptionist-for-a-luxury-mechan
fetched_at: '2026-03-24T20:01:39.113516'
original_url: https://www.itsthatlady.dev/blog/building-an-ai-receptionist-for-my-brother/
date: '2026-03-23'
description: Learn how I built an ai receptionist for my brother's mechanic shop
tags:
- hackernews
- hnrss
---

# How I Built an AI Receptionist for a Luxury Mechanic Shop - Part 1

 

Learn how I built an ai receptionist for my brother's mechanic shop

 
 
 
 
 
 
 
 Mar 20, 2026 
 
 
 
 
 
 

#ai 

#coding 

#technical 

#tutorial 
 
 
 
 
 
 

My brother is a luxury mechanic shop owner, and he’s losing thousands of dollars per month because he misses hundreds of calls per week. He’s under the hood all day. The phone rings, he can’t answer, the customer hangs up and calls someone else. That’s a lost job — sometimes a $450 brake service, sometimes a $2,000 engine repair — just gone because no one picked up.

So I’m building him an AI receptionist. I named itAxle— like a car axle — because of course I did. 😏

This isn’t a generic chatbot. It’s a custom-built voice agent that answers his phone, knows his exact prices, his hours, his policies, and can collect a callback when it doesn’t know something. To get this right requires a custom build, so first I scraped his website data, created a product requirements document (PRD), and scoped the project into a 3-part build.

## Step 1: Building the Brain (RAG Pipeline)

The first step was making sure the AI could actually answer questions accurately — without hallucinating prices or making things up.

A raw LLM is dangerous here. If a customer asks “how much for brakes?” and the AI guesses $200 when the real answer is $450, that’s a broken expectation and a frustrated customer. The fix isRetrieval-Augmented Generation (RAG): instead of letting the model guess, you give it a knowledge base of real information and make it answer only from that.

Here’s what I did:

Scraped Dane’s website— I pulled his service pages and pricing into markdown files. From there I built a structured knowledge base covering 21+ documents: every service type, pricing, turnaround times, hours, payment methods, cancellation policies, warranty info, loaner vehicles, and what car makes he specializes in.

Embedded the knowledge base into MongoDB Atlas— Each document gets converted into a 1024-dimensional vector usingVoyage AI(voyage-3-large). These vectors capture thesemantic meaningof each document, not just the keywords. They’re stored in MongoDB Atlas alongside the raw text, with an Atlas Vector Search index on the embedding field.

Built the retrieval pipeline— When a customer asks a question, the query gets embedded using the same Voyage AI model and then run against the Atlas Vector Search index. It returns the top 3 most semantically similar documents — so “how much for a brake job?” correctly retrieves the brake service pricing doc even if those exact words don’t appear together.

Wired up Claude for response generation— The retrieved documents get passed as context toAnthropic Claude(claude-sonnet-4-6) along with a strict system prompt: answer only from the knowledge base, keep responses short and conversational, and if you don’t know — say so and offer to take a message. No hallucinations allowed.

By the end of Part 1, I could type a question in the terminal and get a grounded, accurate answer back. “How much is an oil change?” → “$45 for conventional, $75 for synthetic. Includes oil filter, fluid top-off, and tire pressure check. Takes about 30 minutes.”

💡 I’m learning as I go using theMongoDB AI Learning Hub— and you can too! Check it out to build your own AI Agents!

## Step 2: Connecting It to a Real Phone Number

Next I had to get this brain onto an actual phone line that customers could call.

I choseVapias the voice platform. It handles everything on the telephony side: purchasing a phone number, speech-to-text (via Deepgram), text-to-speech (via ElevenLabs), and real-time function calling back to my server. The whole voice infrastructure is handled — I just needed to build the webhook it calls.

Built a FastAPI webhook server— Every time a caller asks a question, Vapi sends atool-callsrequest to my/webhookendpoint with the caller’s query. The server routes that to the RAG pipeline, gets a response from Claude, and sends it back to Vapi, which reads it aloud to the caller. The whole round trip has to be fast enough to feel like a natural conversation.

Exposed it with Ngrok— During development, the server runs locally on port 8000. Ngrok punches a tunnel through to a public HTTPS URL, which I paste into the Vapi dashboard as the webhook endpoint. Vapi can now reach my local server in real time as calls come in. For production this would move to a cloud host, but for building and testing Ngrok gets the job done in two minutes.

Configured the Vapi assistant— In the Vapi dashboard I set up the assistant with a greeting (“Hi, thanks for calling Dane’s Motorsport, how can I help you today?”), wired up two tools (answerQuestionfor RAG-backed responses andsaveCallbackfor collecting a name and number when a question can’t be answered), and pointed both at the webhook URL.

Added conversation memory— Vapi sends the full conversation history with each request, so the RAG pipeline gets the prior turns as context. If a caller asks “what are your hours?” and then follows up with “and how much for a tire rotation?”, the AI handles both coherently.

Logged every call to MongoDB— Each interaction gets stored in acallscollection: the caller’s number, the query, the AI’s response, whether it escalated to a human, and the timestamp. Callback requests from unknown questions go into a separatecallbackscollection so Dane can follow up. This turns the phone system into a data asset — he can see what customers are asking most, when call volume spikes, and how often the AI hands off to a human.

## Step 3: Tuning for Voice

Then finally, the thing that took the most iteration: making it sound right.

Text responses and voice responses are completely different. A response that reads fine on screen — with bullet points, dollar signs formatted as “$45.00”, or a sentence that starts with “Certainly!” — sounds awful when spoken aloud. I had to tune the system prompt specifically for voice delivery.

Picked the right voice— Vapi integrates with ElevenLabs and gives you access to a huge library of AI voices. I went through about 20 of them, reading the same test script each time: a greeting, a price quote, an escalation. Most sounded either too robotic, too enthusiastic, or just wrong for a mechanic shop. I landed onChristopher— calm, natural, unhurried. The kind of voice that sounds like someone who actually knows cars. Getting this right mattered more than I expected; a great AI response delivered in the wrong voice still feels off.

Rewrote the system prompt for voice— Short sentences. No markdown. No filler phrases like “Great question!” or “Certainly!”. Prices spoken naturally (“forty-five dollars” instead of “$45”). Responses capped at 2–4 sentences max. The goal is to sound like a knowledgeable, friendly human — not a chatbot reading a webpage.

Tested the escalation flow— When a caller asks something that isn’t in the knowledge base, the AI doesn’t guess. It tells the caller it doesn’t have that information, asks for their name and a good callback number, and saves that to MongoDB. Dane gets a list of callbacks to return — no lost leads.

Wrote integration tests— I built a test suite covering the RAG pipeline, the webhook handler, and the full end-to-end flow. This was especially important for catching edge cases: what happens when Vapi sends a malformed request, what happens when the vector search returns no results above the confidence threshold, what happens when the caller doesn’t leave a callback number.

## The Stack

Here’s everything wired together:

* Vapi (with Deepgram & ElevenLabs integration)— phone number, speech-to-text, text-to-speech, tool calling
* Ngrok— local development tunnel (Vapi → localhost)
* FastAPI + Uvicorn— webhook server
* MongoDB Atlas— knowledge base storage, vector search, call logs, callback queue
* Voyage AI(voyage-3-large) — text embeddings for semantic retrieval
* Anthropic Claude(claude-sonnet-4-6) — response generation, grounded in the knowledge base
* Python— everything glued together withpymongo,voyageai,anthropic,fastapi
* Copilot CLI- for the actual build!

## What’s Next

Right now the AI answers questions and takes callbacks. The next phase has a few pieces: connecting it to a real calendar so it can book appointments directly during the call; adding text message notifications so Dane gets an instant SMS whenever a new callback comes in; building a simple dashboard so he can see and manage all his pending callbacks in one place; locking down the security for production robustness; deploying to Railway so it runs on a persistent public URL; and then handing it over for him to actually use with real customers.

Dane misses 100+ calls a week. Each missed call is a potential job. Some of those jobs are $50, some are $2,000. This system runs 24/7, never puts someone on hold, and knows every price and policy as well as he does.

The build took three focused sprints. The hardest part wasn’t the code — it was getting the voice tone right so it actually sounds like someone who works at a mechanic shop and not a Silicon Valley startup.

If you’re building something similar, the core insight is this:don’t use a raw LLM for a business-specific voice agent. Ground it in a real knowledge base, constrain it to only answer from that base, and design the fallback flow before anything else. The escalation path is not an edge case — it’s a core feature.

This post was written with the assistance of AI.

 
 
 
* #### 30 Security Tips Every Vibe Coder Needs to Know
* #### 10 Vibe Coding Apps You’ve Never Heard Of (But Need To Try!)
* #### 5 FREE AI Courses to Level Up Your Skills
 
 

Written by

 
 
 
 
 
 

### Kedasha Kerr

 

Software Developerin Chicago

 
 
 
 
 

Let's Connect:

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

## I write about building with AI.

 

Get the next post delivered to your inbox.

 
 
 

 
 
 
 
 
 
 
 
 
 
 
 
Subscribe
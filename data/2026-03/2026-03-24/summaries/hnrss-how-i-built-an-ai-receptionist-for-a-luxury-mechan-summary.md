---
title: How I Built an AI Receptionist for a Luxury Mechanic Shop - Part 1
url: https://www.itsthatlady.dev/blog/building-an-ai-receptionist-for-my-brother/
date: 2026-03-23
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-03-24T20:03:00.131766
---

# How I Built an AI Receptionist for a Luxury Mechanic Shop - Part 1

# How I Built an AI Receptionist for a Luxury Mechanic Shop – Part 1

## Overview
- The mechanic shop loses thousands of dollars each month because missed calls lead to lost jobs.
- I created a custom voice AI receptionist named **Axle** to answer calls, provide accurate pricing, hours, policies, and collect callbacks when needed.
- The project was divided into three main parts: a Retrieval‑Augmented Generation (RAG) brain, phone integration, and voice tuning.

## Step 1 – Building the Brain (RAG Pipeline)
- Scraped the shop’s website and converted service pages and pricing into markdown files (21+ documents).
- Created a knowledge base stored in MongoDB Atlas; each document is embedded into a 1024‑dimensional vector using Voyage AI (voyage‑3‑large).
- Set up Atlas Vector Search to retrieve the top‑3 semantically similar documents for any query.
- Integrated Anthropic Claude (claude‑sonnet‑4‑6) with a strict system prompt: answer only from the knowledge base, keep replies short and conversational, and ask for a callback if the answer is unknown.
- Result: terminal queries return accurate, grounded answers (e.g., oil‑change pricing).

## Step 2 – Connecting to a Real Phone Number
- Chose Vapi as the telephony platform (provides phone number, Deepgram STT, ElevenLabs TTS, and function calling).
- Built a FastAPI webhook that receives Vapi requests, forwards queries to the RAG pipeline, and returns Claude’s response.
- Used Ngrok during development to expose the local server to Vapi; production will move to a cloud host.
- Configured Vapi assistant with a greeting, two tools (answerQuestion and saveCallback), and the webhook URL.
- Added conversation memory so follow‑up questions are handled coherently.
- Logged every call in MongoDB (caller ID, query, response, escalation flag, timestamp) and stored callbacks in a separate collection for the shop owner to follow up.

## Step 3 – Tuning for Voice
- Tested ~20 ElevenLabs voices; selected “Christopher” for a calm, natural tone suitable for a mechanic shop.
- Rewrote the system prompt for voice output: short sentences, no markdown, no filler phrases, prices spoken as words.
- Implemented escalation flow: when the AI cannot answer, it asks for name and callback number and stores the request.
- Developed integration tests covering the RAG pipeline, webhook handling, and end‑to‑end call flow, handling malformed requests, low‑confidence retrieval, and missing callback numbers.

## Stack
- **Vapi** (Deepgram STT, ElevenLabs TTS, phone number, tool calling)
- **Ngrok** – local development tunnel
- **FastAPI + Uvicorn** – webhook server
- **MongoDB Atlas** – knowledge base, vector search, call logs, callbacks
- **Voyage AI (voyage‑3‑large)** – text embeddings
- **Anthropic Claude (claude‑sonnet‑4‑6)** – response generation

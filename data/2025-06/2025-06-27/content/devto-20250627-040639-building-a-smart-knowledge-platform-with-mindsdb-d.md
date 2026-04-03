---
title: Building a Smart Knowledge Platform with MindsDB - DEV Community
url: https://dev.to/k0msenapati/building-a-smart-knowledge-platform-with-mindsdb-5anb
site_name: devto
fetched_at: '2025-06-27T04:06:39.027664'
original_url: https://dev.to/k0msenapati/building-a-smart-knowledge-platform-with-mindsdb-5anb
author: K Om Senapati
date: '2025-06-22'
description: Working with structured data like CSVs or JSON often means writing queries, managing schemas, and... Tagged with ai, python, mindsdb, programming.
tags: '#ai, #python, #mindsdb, #programming'
---

Working with structured data like CSVs or JSON often means writing queries, managing schemas, and building pipelines just to answer simple questions. If you want to make that data interactive like asking natural language questions or building an AI agent on top of it, things get complicated fast. You usually need to write code, understand vector stores, manage embeddings, and stitch tools together.

That’s the problem I faced.

I wanted a simple way to:

* Upload structured data
* Turn it into something queryable with natural language
* Build an AI agent that could talk about that data

### The Solution: MindsDB

That’s where MindsDB came in.

MindsDB recently added support for Knowledge Bases (KBs). You can now ingest structured data into a KB, use an embedding model (cloud or local), and build multi-step workflows or AI agents on top of it without writing code.

This release immediately clicked with me. I had already used MindsDB’s AI Table feature to build a quiz app. It lets you interact LLMs so I was familiar with the platform and trusted its approach.

With this KBs + Agents integration, I no longer needed to code the whole pipeline. I just wrote a couple of SQL queries in the MindsDB GUI, and voilà — I had an AI agent ready to go.

### MindsDB Philosophy

What I especially liked is how MindsDB thinks about data and intelligence. Their philosophy is:

* Connect: Connect data from hundreds of data sources
* Unify: Unify data from multiple (structured and unstructured) data sources within MindsDB, enabling federated queries as if all data resides in a single database
* Respond: Use agents to give intelligent, context-aware responses from that unified data

Dive into MindsDB 👉MindsDB Docs

As a Python, and SQL guy, this felt like the right mix of practicality and power.

## About Agent Hub

Agent Hub works with structured data: CSV and JSON, Knowledge Bases, and AI Agents.

### Features:

1. User can upload structured data.
2. User can create a KB and ingest the data into it using any OpenAI-compatible API embedding model (cloud/local) or Ollama models.
3. User can query/summarize the KB and also evaluate it from test_data.
4. User can add JOBS to ingest data from a data source into the KB.
5. User can create AI Agents and chat with them.

For structured data, I needed a database. I found out that MindsDB has afilesdatabase, which is perfect for storing user-uploaded data files.

Then I created a miniMindsDB packageto encompass all the MindsDB logic using the MindsDB Python SDK and SQL queries to do all the operations:

* Create a project for each user
* Prefix files with the username
* Create KBs
* Ingest data into KBs
* Delete KBs
* Query and summarize the KB using AI Table
* Evalauate KBs
* Setup JOB for data ingestion
* Create and use AI Agents

Then I created a simple Flask app which used a SQLite database and SQLAlchemy as the ORM. I used HTML Jinja2 templates. Yeah, no frontend framework.Python is 💖.

## k0msenapati/agent-hub

### Agent Hub is an AI collaboration platform designed to transform your data into intelligent AI agents.

# 🤖 Agent Hub

Note

Agent Hub is an AI collaboration platform designed to transform your data into intelligent AI agents. With Agent Hub, you can unlock powerful insights and automate tasks effortlessly by creating tailored AI agents, building comprehensive knowledge bases, and managing your data files seamlessly.

## 🎬 Project Showcase

Demo Video

Blog Post

## 🌟 Features

Agent Hubfeatures intro:

* AI Agents– Create and manage AI agents tailored to your specific needs for intelligent responses.
* Knowledge Bases– Build comprehensive knowledge bases from your data for efficient querying and insights.
* File Management– Upload and organize your files to integrate seamlessly with AI processes.

## 💻 Installation

Follow these steps to set up and run Agent Hub:

1. Setup MindsDB and Ollama with Docker(docker-compose.yml is provided):docker-compose up -dEnter fullscreen modeExit fullscreen mode
2. Install nomic-embed-text in Ollama container:dockerexecollama ollama pull nomic-embed-textEnter fullscreen modeExit fullscreen mode
3. Create KB Summarizer Model and Connect Pgvector in MindsDB…

View on GitHub

## Challenges

1. I ran into an issue with MindsDB when performing operations on a KB using an embedding model from Ollama. It would throw an"Event Loop Closed"error on the first attempt. Strangely, repeating the same operation a second time worked just fine. So, I handled that in the app using a simpletry-catchwith a retry.
2. For the frontend, I kind of vibe-coded the Jinja2 templates. But hey, the idea is mine 😜

Building this was fairly easy as all the heavy lifting is done by MindsDB.I just had to trigger the right queries from the Flask backend.

## Use Cases

* Upload structured data like logs, reports, or exports
* Query or summarize data with natural language
* Create intelligent agents trained on your data

## Final Thoughts

This is just an MVP, but it opens up a lot of possibilities.

Right now, it works with structured data like CSV and JSON but it can easily be extended to handle other formats like web pages, PDFs, or Word docs. MindsDB’s Connect layer also makes it easy to bring in data from external databases and APIs, so the potential to scale and integrate is built-in.

What I’ve built is a starting point: a way to turn raw, structured data into something intelligent. It’s simple, but powerful. And with MindsDB handling the heavy lifting, it’s also surprisingly easy to build.

If you found this article useful, share it with your peers and community to spread the word about this.

Follow me for more content like this!

Twitter|GitHub|YouTube

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (16 comments)


Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse

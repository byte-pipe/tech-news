---
title: AlloyDB AI | Google Cloud
url: https://cloud.google.com/alloydb/ai
site_name: tldr
content_file: tldr-alloydb-ai-google-cloud
fetched_at: '2026-04-03T01:01:25.024472'
original_url: https://cloud.google.com/alloydb/ai
date: '2026-04-03'
description: Build generative AI applications with AlloyDB for PostgreSQL.
tags:
- tldr
---

Learn how AlloyDB AI drives innovation for application developers. Read the blog.

# AlloyDB AI

## Build AI agents and apps with AlloyDB

AlloyDB integrates vector embeddings, high-performance vector search, and natural language into a PostgreSQL-compatible database that runs anywhere.

Try AlloyDB free
Documentation

Get started with a30-day AlloyDB free trial instance.

### Product highlights

* High-performance, automated vector operations
* Access to any AI model with a simple SQL query
* Foundation for AI applications and agentic workflows
* Harness gen AI with Google Cloud databases5:02

Overview

### Fast, pgvector-compatible vector search

TheScaNN indexuses the same search algorithm as Google Search and is based on 12 years of Google research. It performs advanced semantic search with up to 10x faster index creation, up to 4x faster vector search queries, and up to 10x faster filtered vector search queries than the standard PostgreSQL HNSW index. AlloyDB AI offers additional enhancements, such as parallel index build, index auto-maintenance, and enterprise-grade observability for vector indexes.

Introducing ScaNN vector indexing in AlloyDB

### High-performance queries across SQL and vector data

AlloyDB AI’s ScaNN index is deeply integrated with the PostgreSQL query planner to enablesimple yet powerful queriesacross structured and unstructured data. You don’t need to deploy or learn a separate vector database, nor suffer the latency of trips across multiple systems.Adaptive filteringensures that filters, joins, and vector indexes deliver optimal performance when used together.

Deep dive into AlloyDB’s vector search

### Natural language interfaces in your apps

Use AlloyDB AI to provide users and agents with accurate responses to natural language questions. WithAlloyDB AI natural languageyou can overcome the ambiguity, flexibility, and security issues typically encountered in natural language interfaces. AlloyDB AI can disambiguate user questions and incorporate data from the schema, sample data, and other sources to increase accuracy. It also locks down access to unauthorized data.

Learn about natural language app interfaces

### Access models on any platform

Access Google’s Gemini models or other foundation models hosted onVertex AI, and usemodel endpoint managementto register model endpoints on any platform and call them from AlloyDB with a simple SQL function. Use retrieval augmented generation (RAG) to ground application responses in real-time context from the database without the need for complex glue code.

### Natural language in SQL queries

WithAlloyDB AI functions, you can use natural language in SQL queries to express filtering conditions and ranking criteria. The power of AI models brings reasoning and real-world knowledge to SQL queries, unlocking deep semantic insights from your enterprise data. You can generate vector embeddings, perform similarity searches, and invoke AI models within a single query.

Learn about natural language database queries

### Integration with the AI ecosystem

Modularize and simplify your code with popular orchestration frameworks such asAgent Development Kit(ADK),LangChain, andLlamaIndexthat make it easy to connect models, tools, and databases. Focus on your application's unique logic and let the framework manage common actions like loading a document, accessing a vector store, and reading chat history.

Build an LLM and RAG-based chat application
View more

How It Works

### AlloyDB AI processes vector and SQL queries within a single query engine inside the database. This eliminates data movement to separate systems. By calling AI models via a simple SQL function, you can build real-time, data-rich applications and agents with less latency and complexity.

Read whitepaper
Common Uses

### Hybrid text and semantic search

##### Search results that reflect user intent

For a good search experience, your website or app needs to understand the user’s intent, and can’t rely on exact keyword matches. AlloyDB’s hybrid search combines text search (“Pixel”) with semantic search (“I’m looking for that phone from Google”) to provide both precision and context. It applies powerful re-ranking and inline filtering directly on your live operational data, delivering accurate, relevant results and increasing click-through rates without you having to manage separate search systems.

Learn how to run a hybrid vector similarity search
* How Target supports millions of product searches with AlloyDB
* Documentation: How to perform hybrid searches with AlloyDB
* Sample code for hybrid search on an e-commerce site

#### How-tos

##### Search results that reflect user intent

For a good search experience, your website or app needs to understand the user’s intent, and can’t rely on exact keyword matches. AlloyDB’s hybrid search combines text search (“Pixel”) with semantic search (“I’m looking for that phone from Google”) to provide both precision and context. It applies powerful re-ranking and inline filtering directly on your live operational data, delivering accurate, relevant results and increasing click-through rates without you having to manage separate search systems.

Learn how to run a hybrid vector similarity search
* How Target supports millions of product searches with AlloyDB
* Documentation: How to perform hybrid searches with AlloyDB
* Sample code for hybrid search on an e-commerce site

### Multimodal search applications

##### High performance vector embedding generation

Searching on multimodal data (text, images, video, and other content types) requires a high-performance vector database that contains your freshest data. AlloyDB automatically generates vector embeddings directly within the database using the AI model of your choice, eliminating the need for complex pipelines into other systems. It also offers automatic indexing, so your applications can deal with rapidly-changing data as it's written or updated.

Learn about storing vector embeddings in AlloyDB
* Codelab: Get started with vector embeddings with AlloyDB AI
* Blog: Gemini CLI extension for PostgreSQL in action
* Blog: ScaNN for AlloyDB - from millions to billion of vectors

#### How-tos

##### High performance vector embedding generation

Searching on multimodal data (text, images, video, and other content types) requires a high-performance vector database that contains your freshest data. AlloyDB automatically generates vector embeddings directly within the database using the AI model of your choice, eliminating the need for complex pipelines into other systems. It also offers automatic indexing, so your applications can deal with rapidly-changing data as it's written or updated.

Learn about storing vector embeddings in AlloyDB
* Codelab: Get started with vector embeddings with AlloyDB AI
* Blog: Gemini CLI extension for PostgreSQL in action
* Blog: ScaNN for AlloyDB - from millions to billion of vectors

### Natural language interfaces

##### Context-aware natural language queries

Empower business users to get answers from your data by simply asking questions. AlloyDB’s natural language understanding accurately translates conversational queries into responses, even asking follow-up questions (“Did you mean departure or arrival time?”) if necessary. This democratizes data access, accelerates decision-making, and reduces the burden of incorporating natural language interfaces into applications and AI agents.

Learn how to build a natural language interface into your app
* Blog: Build gen AI apps with real-time data
* Codelab: Generate SQL using AlloyDB AI natural language

#### How-tos

##### Context-aware natural language queries

Empower business users to get answers from your data by simply asking questions. AlloyDB’s natural language understanding accurately translates conversational queries into responses, even asking follow-up questions (“Did you mean departure or arrival time?”) if necessary. This democratizes data access, accelerates decision-making, and reduces the burden of incorporating natural language interfaces into applications and AI agents.

Learn how to build a natural language interface into your app
* Blog: Build gen AI apps with real-time data
* Codelab: Generate SQL using AlloyDB AI natural language

### Agentic workflows

##### AI agents that know your data

Build and scale powerful agentic workflows with AlloyDB as the foundation. AlloyDB provides a scalable, high-availability architecture for an AI-ready, PostgreSQL-compatible relational database. Your agent can use Gemini to reason over your structured and unstructured enterprise data and use high-performance search, natural language processing, and pre-configured data integrations to create sophisticated AI-powered applications and conversational experiences.

Learn about building AI agents on AlloyDB
* Develop and deploy AI agents with Agent Development Kit
* Learn about MCP Toolbox for Databases
* Codelab: Build an agentic AI assistant with ADK, MCP Toolbox, and AlloyDB

#### How-tos

##### AI agents that know your data

Build and scale powerful agentic workflows with AlloyDB as the foundation. AlloyDB provides a scalable, high-availability architecture for an AI-ready, PostgreSQL-compatible relational database. Your agent can use Gemini to reason over your structured and unstructured enterprise data and use high-performance search, natural language processing, and pre-configured data integrations to create sophisticated AI-powered applications and conversational experiences.

Learn about building AI agents on AlloyDB
* Develop and deploy AI agents with Agent Development Kit
* Learn about MCP Toolbox for Databases
* Codelab: Build an agentic AI assistant with ADK, MCP Toolbox, and AlloyDB

### On-premises and edge AI

##### Secure AI on any platform

Deploy a complete AI stack on-premises, at air-gapped environments, at the edge such as a retail store, or as part of a multicloud deployment. AlloyDB Omni is a downloadable edition of AlloyDB that runs anywhere, so you can maintain full data sovereignty while pairing your database with local foundation models. Your most sensitive data never leaves your network, giving you the control to build highly resilient and compliant custom AI solutions.

Learn more about AlloyDB Omni
* How NeuroPace developed a highly secure AI application
* Register and call AI models in AlloyDB Omni
* Codelab: Set up AlloyDB Omni with a local AI model on Kubernetes

#### How-tos

##### Secure AI on any platform

Deploy a complete AI stack on-premises, at air-gapped environments, at the edge such as a retail store, or as part of a multicloud deployment. AlloyDB Omni is a downloadable edition of AlloyDB that runs anywhere, so you can maintain full data sovereignty while pairing your database with local foundation models. Your most sensitive data never leaves your network, giving you the control to build highly resilient and compliant custom AI solutions.

Learn more about AlloyDB Omni
* How NeuroPace developed a highly secure AI application
* Register and call AI models in AlloyDB Omni
* Codelab: Set up AlloyDB Omni with a local AI model on Kubernetes
Generate a solution
What problem are you trying to solve?
Generate solution
shuffle
Surprise me
What you'll get:
check_small
Step-by-step guide
check_small
Reference architecture
check_small
Available pre-built solutions
This service was built with 
Vertex AI
. You must be 18 or older to use it. Do not enter sensitive, confidential, or personal info.

### Get started with AlloyDB AI

### Learn about AI development with databases

Download whitepaper

### Get started with a codelab

Try the codelab

### AlloyDB AI drives innovation for developers

Read the blog

### ScaNN for AlloyDB: next generation vector search

Download whitepaper

### Build a sports shop agent AI assistant with AlloyDB AI

Try the codelab

Business Case

Search at Target is evolving into something far more dynamic – an intelligent, multimodal layer that helps guests connect with what they need, when and how they need it. With AlloyDB AI and Google Cloud’s rapidly evolving data and AI stack, we’re confident in our ability to stay ahead of guest expectations and deliver more personalized, delightful shopping moments every day.

Melissa Ludack, VP of Data Sciences, Target

Read customer story

### Related Content

* Nuro drives autonomous innovation with AlloyDB for PostgreSQLRead the blog
* NeuroPace enhances iEEG seizure identification and similarity searchRead the blog
* Real-world applications of gen AI and databases at EchoStarWatch video

Featured benefits

Accelerate generative AI development and time-to-market

Reduce your AI stack's cost and complexity

Build smarter, more responsive, and more relevant AI applications
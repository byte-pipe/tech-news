---
title: 'From zero to a RAG system: successes and failures | Andros Fenollosa'
url: https://en.andros.dev/blog/aa31d744/from-zero-to-a-rag-system-successes-and-failures/
site_name: hnrss
content_file: hnrss-from-zero-to-a-rag-system-successes-and-failures-a
fetched_at: '2026-03-26T19:29:06.041510'
original_url: https://en.andros.dev/blog/aa31d744/from-zero-to-a-rag-system-successes-and-failures/
date: '2026-03-24'
description: 'A few months ago I was tasked with creating an internal tool for the company''s engineers: a Chat that used a local LLM. Nothing extraordinary so far.'
tags:
- hackernews
- hnrss
---

A few months ago I was tasked with creating an internal tool for the company's engineers: a Chat that used a local LLM. Nothing extraordinary so far. Then the requirements came in: it had to have a fast response, I insist... fast!, and... it also had to provide answers about every project the company has done throughout its entire history (almost a decade). They didn't want a traditional search engine, but a tool where you could ask questions in natural language and get answers with references to the original documents. With emphasis on providing information from OrcaFlex files (a simulation software for floating body dynamics, cables, etc., widely used in the offshore industry). It already seemed complex, but it was confirmed when I was given access to 1 TB of projects, mixed with technical documentation, reports, analyses, regulations, CSVs, etc. The emotional roller coaster had begun.

I'll tell you upfront that it was neither a quick nor easy process, and that's why I'd like to share it. From the first attempts, mistakes, to the final architecture that ended up in production. I also want to highlight that I had never done anything similar before and didn't know how a RAG worked either.

We'll go problem by problem, and the solution I applied to each one.

## Problem 1: selecting the right technology

The first step was to define the stack.

I needed a local language model, without relying on external APIs, for confidentiality reasons. Ollama emerged as the most mature and easy-to-use option for running LLaMA models locally. I tried several embeddings, andnomic-embed-textoffered good performance and quality for technical documents.

Next was a RAG engine to orchestrate the document indexing process, embedding generation, vector database storage, and queries. Without it, no matter how fast the language model is, we couldn't retrieve relevant information from the documents. Think of it like a book's index: without it, you'd have to read the entire book to find the information you need. And with a good index, you can go straight to the right page. I'll call this process indexing for simplicity, although it's really a vectorization and indexing process.

After some research, I found a mature open source framework called LlamaIndex.

The language I'd use would be Python, I could list many reasons, but the most important one is that I feel comfortable and productive with it. Additionally, both Ollama and LlamaIndex have excellent Python SDKs.

I was ready to start building the software. I wrote my first scripts to run vector tests on the RAG system and do some query experiments. It worked really well with very little code. I thought it would be a project of a few weeks. I couldn't have been more wrong.

The next step was working with the actual documents. Hold on tight, it's going to be a bumpy ride!

## Problem 2: the document chaos

My file source was a folder on Azure with a massive amount of technical documents: hundreds of gigabytes, thousands of files, various formats, with no organization or structure beyond the folder hierarchy. Every data engineer's dream (note the irony).

I cracked my knuckles, set the RAG output to save to disk, and launched my first script. LlamaIndex ended up overflowing my laptop's RAM within minutes, choking my OS until everything froze. I tried many configurations, caching systems, and other strategies, but at some point my machine always died.

After debugging, I discovered it was processing huge files that contributed nothing: videos, simulations, backup files... Documents that added nothing to a RAG system, but that LlamaIndex tried to process as if they were text. If a file weighed several gigabytes, the system tried to load it entirely into memory for processing, which was suicide.

I added a filtering system to the pipeline that excluded files by extension and by name patterns (simulation files, numerical results, etc.).

Category

Excluded extensions

Video

mp4, avi, mov, mkv, wmv, flv, webm, m4v, mpg, mpeg, 3gp, mts...

Images

jpg, jpeg, png, gif, bmp, tiff, svg, ico, webp, heic, psd...

Executables

exe, dll, msi, bat, sh, app, dmg, so, jar...

Compressed

zip, rar, 7z, tar, gz, bz2, xz

Simulation

sim, dat

Temporary

tmp, temp, cache, log, swp, pyc, crdownload, partial...

Backups

bak, 3dmbak, dwgbak, dxfbak, pdfbak, stlbak, old, bkp, original...

Email

msg, pst, eml, oft

I also removed files that were expensive to process and didn't add value either, like CSVs, JSONs, among others. On the other hand, I converted PDF, DOCX, XLSX, PPTX, etc. files to plain text so LlamaIndex could process them without issues.

The result was a 54% reduction in the number of files to index. And of course, my RAM stopped exploding.

I could finally start indexing without fear.

## Problem 3: indexing 451GB of documents without dying in the attempt

A RAG involves creating a vector index file containing document embeddings. Vectors are numerical representations of documents that allow measuring their similarity. LlamaIndex has a simple system you can configure with a couple of lines. You just point it to the directory and it takes care of storing all the information inside in JSON format. It's really convenient, works well, unless you're dealing with hundreds of gigabytes of documents. The system became unmanageable: every time the service restarted, it had to reprocess all documents from scratch, which could take days. Also, the default format is not optimal for large searches (JSON).

I added a checkpoint system to save indexing progress. Every time a problem occurred, I wouldn't lose all progress, but could resume from the last processed file. However, data got corrupted, it was error-prone, and very slow. I was facing a bottleneck I couldn't overcome.

After many trials and errors, and reading more about it, I decided to make the leap to a dedicated vector database: ChromaDB. An open-source database (Apache-2.0 license) for storing and querying vectors. Not to be confused with the Chrome/Chromium browser. ChromaDB is an abstraction layer that stores on top of a traditional database, I configured SQLite, and offers specific functionalities like similarity searches, clustering, etc.

The change was radical and instant. Indexing went from being a monolithic process that loaded everything into memory to a batch pipeline that processed 150 files at a time, generated their embeddings, and stored them directly in ChromaDB. This allowed indexing the 451GB of documents across multiple sessions, with checkpoints, without losing progress on interruptions, without corrupted data. Additionally, it was really easy to back up and restore the index in case of failures (just copy the SQLite file).

The system was ready. With a quick benchmark, I discovered I would need several months to index all the content with my laptop. Now the bottleneck was neither the RAM, nor the indexing system, nor the files, but the GPU.

## Problem 4: my graphics card is not a rocket

My laptop has an integrated graphics card. Processing 500 MB of documents by CPU takes 4-5 hours, not good numbers. I absolutely needed a powerful GPU. In a follow-up meeting, it was decided to rent me a virtual machine with an NVIDIA RTX 4000 SFF Ada, which has 20GB of VRAM. These kinds of rentals are not exactly cheap. Now I was working under more pressure.

I modified my containers and the system was optimized to take advantage of the GPU. I launched my script. After several weeks, between 2 and 3, the indexing process finished without failures. 738,470 vectors, 54GB of index in ChromaDB, and a RAG system ready to answer questions. I copied the ChromaDB database, a SQLite file, to my local machine and that was it. To the relief of my Sysadmin and Project Manager, we could finally shut down the virtual machine. The cost was 184 euros on Hetzner, not cheap.

It was time to build the backend and frontend.

## Problem 5: the user experience

With Flask I built a simple API to access LlamaIndex, which in turn queried ChromaDB and Ollama.

I'm quite a fan of Streamlit for building internal projects of all kinds, so it would be my frontend (and I'd keep using Python). It also has a native widget for Q&A, in the style of any current chat for interacting with an AI.

In a couple of hours I had the entire visual part working. The rest were details to polish: showing the company logo, a spinner while the query processes, saving sessions, etc.

The diagram of how the different system components communicate is as follows:

flowchart TD
 U["👤 User"]:::user --> E["Streamlit (Web UI)"]:::web
 E <-->|HTTP| D["Flask API"]:::api
 D --> F["Python Backend"]:::backend
 F <--> C["Ollama (LLM + Embeddings)"]:::llm
 C <--> B["RAG (LlamaIndex)"]:::rag
 B <--> G["ChromaDB"]:::chroma

 classDef user fill:#37474F,stroke:#263238,stroke-width:2px,color:#fff
 classDef web fill:#8E24AA,stroke:#6A1B9A,stroke-width:2px,color:#fff
 classDef api fill:#D32F2F,stroke:#B71C1C,stroke-width:2px,color:#fff
 classDef backend fill:#00897B,stroke:#00695C,stroke-width:2px,color:#fff
 classDef rag fill:#7CB342,stroke:#558B2F,stroke-width:2px,color:#fff
 classDef chroma fill:#4CAF50,stroke:#388E3C,stroke-width:2px,color:#fff
 classDef llm fill:#FF6F00,stroke:#E65100,stroke-width:2px,color:#fff

I adjusted the template for how the LLM response should be formatted. For each response, the system must show the information sources, that is, the documents used to generate the answer.

Question: What wind farm projects have been done at the company?Answer: Several wind farm related projects have been carried out, including:- Project A: Feasibility analysis for an offshore wind farm. Reference: https://.../project_a_wind_farm_report.pdf- Project B: Wind turbine simulation using OrcaFlex. Reference: https://.../project_b_wind_farm_simulation.sim

But of course, I needed to store all the original data on disk, along with the vector database, the LLM, and the backend. And I didn't have the space for it. My production environment was a virtual machine very limited in resources, and even more so in disk (100 GB). I couldn't afford to have half a terabyte of documents on the server.

## Problem 6: serving documents without filling the disk

We must remember that having the vector database doesn't mean we can do without the original documents. However, I can have the vector index with document embeddings on one side, and the original documents elsewhere (whether physically on the same server or in the cloud).

The solution was to serve the original documents directly from Azure Blob Storage (it would have been possible with any other system). For each document cited in a response, the system generates a download link with a SAS token that allows the user to download it directly from the cloud.

%%{init: {'theme':'default'}}%%
flowchart LR
 U["👤 User"]:::user -->|Question| S["Server (VM)"]:::server
 S -->|Response + links| U
 U -->|Direct download with SAS token| A["Azure Blob Storage
(451 GB of documents)"]:::azure

 classDef user fill:#37474F,stroke:#263238,stroke-width:2px,color:#fff
 classDef server fill:#00897B,stroke:#00695C,stroke-width:2px,color:#fff
 classDef azure fill:#0078D4,stroke:#005A9E,stroke-width:2px,color:#fff

What absolutely needed disk space was the ChromaDB vector index, which at 54GB is perfectly manageable on a local disk, the LLM, which takes about 10GB, the backend (a few megabytes), and the frontend (another few megabytes). The rest of the documents stay in Azure, accessible on demand.

## Final architecture

The final system architecture looked like this:

flowchart LR
 A["Azure Blob Storage"]:::azure -- Documents --> B["RAG (LlamaIndex)"]:::rag
 B <--> G["ChromaDB"]:::chroma
 B <--> C["Ollama (LLM + Embeddings)"]:::llm
 D["Flask API"]:::api <-- HTTP --> E["Streamlit (Web UI)"]:::web
 C <--> F["Python Backend"]:::backend
 D -- Call --> F

 classDef azure fill:#0078D4,stroke:#005A9E,stroke-width:2px,color:#fff
 classDef rag fill:#7CB342,stroke:#558B2F,stroke-width:2px,color:#fff
 classDef chroma fill:#4CAF50,stroke:#388E3C,stroke-width:2px,color:#fff
 classDef llm fill:#FF6F00,stroke:#E65100,stroke-width:2px,color:#fff
 classDef api fill:#D32F2F,stroke:#B71C1C,stroke-width:2px,color:#fff
 classDef web fill:#8E24AA,stroke:#6A1B9A,stroke-width:2px,color:#fff
 classDef backend fill:#00897B,stroke:#00695C,stroke-width:2px,color:#fff

Layer

Technology

Purpose

LLM

Ollama + llama3.2:3b

Local response generation

Embeddings

nomic-embed-text

Document vectorization

Vector database

ChromaDB (HNSW)

Similarity storage and search

RAG Framework

LlamaIndex

RAG pipeline orchestration

API

Flask + Gunicorn

HTTP REST service

Web UI

Streamlit

Conversational interface

Containers

Docker Compose

Service orchestration

GPU

NVIDIA Container Toolkit

Hardware acceleration

Storage Service

Azure Blob Storage

Cloud persistence

## Lessons learned

* Manage memory: Loading all documents into memory and processing them at once is dangerous. Implement batch processing, I used 150 per iteration, with explicit garbage collector calls between batches. Each batch is processed, embedded, stored in ChromaDB, and memory is freed before continuing.
* Problematic files: Even after the filtering layers, some files got through but failed during parsing, like corrupt PDFs, Word documents with broken macros, spreadsheets with unexpected formats... The strategy was error tolerance. If a file fails, it's logged and we move on to the next one. A problematic file never stops an entire batch. Afterwards, I can manually review, download, or assign it to another batch.
* Checkpoints: Each batch can take hours, a power outage or restart can't mean starting from zero. Implement a checkpoint system that saves the last completed batch, total processed nodes, and a timestamp. On restart, indexing continues exactly where it left off.
* Monitoring: Add monitoring and information scripts for different states:index-progress,index-watch,index-speed,index-checkpoint,index-failed... When the RAG is working for hours, you need to know what's happening.

## Conclusion

It's not a perfect system, but it's sufficient. It would have been great if I could have launched an OrcaFlex instance so the LLM could run projects or perform its own simulations on demand. But that required more time and resources than could be provided. However, I'm very happy with the final result. The system is fast, reliable, and above all useful for my colleagues.

My humble advice, if you're considering building something similar: spend time building the best possible data. If the source is not relevant enough, the LLM won't be able to generate good answers.

* Problem 1: selecting the right technology
* Problem 2: the document chaos
* Problem 3: indexing 451GB of documents without dying in the attempt
* Problem 4: my graphics card is not a rocket
* Problem 5: the user experience
* Problem 6: serving documents without filling the disk
* Final architecture
* Lessons learned
* Conclusion

This work is under aAttribution-NonCommercial-NoDerivatives 4.0 International license.

## Will you buy me a coffee?

Support me on Ko-fi

## You may also like

* python
* django
* django channels
* django liveview
* liveview

## DOOM in Django: testing the limits of LiveView at 600.000 divs/seconds

* web
* python
* django
* django liveview

## My website is now ~2.8x faster after converting it to a Django LiveView SPA

* python
* django
* django liveview

## I created a game engine for Django?

## Visitors in real time

You are alone: 🐱

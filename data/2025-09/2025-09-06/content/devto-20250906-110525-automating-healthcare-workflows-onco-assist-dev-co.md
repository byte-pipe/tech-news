---
title: 'Automating Healthcare Workflows: Onco-Assist - DEV Community'
url: https://dev.to/hargun_kaur_d5af086aff62f/automating-healthcare-workflows-onco-assist-phe
site_name: devto
fetched_at: '2025-09-06T11:05:25.234924'
original_url: https://dev.to/hargun_kaur_d5af086aff62f/automating-healthcare-workflows-onco-assist-phe
author: Hargun Kaur
date: '2025-09-01'
description: This is a submission for the AI Agents Challenge powered by n8n and Bright Data What I... Tagged with devchallenge, n8nbrightdatachallenge, ai, webdev.
tags: '#devchallenge, #n8nbrightdatachallenge, #ai, #webdev'
---

n8n and Bright Challenge: Unstoppable Workflow

This is a submission for theAI Agents Challenge powered by n8n and Bright Data

## What I Built

When technology meets personal need, innovation becomes deeply meaningful. This project wasn’t just a hackathon build or an experiment in automation — it started from my own mother’s case. Managing her medical reports, prescriptions, test results, and hospital bills was overwhelming. Each piece of information lived in different silos — Gmail attachments, WhatsApp messages, portals — leaving us scrambling whenever a doctor asked for history. I wanted to solve this once and for all.

That’s when I turned to n8n, an open-source workflow automation tool, and started building an automated pipeline to collect, classify, process, and deliver her medical information in an organized way.

## Demo

https://drive.google.com/file/d/1e5ZRD-Kij_X26GvbFbSV6DXEGblp9JmU/view?usp=sharing

### n8n Workflow

https://github.com/hargunkaur286/onco-assist

## Technical Implementation

📨 Step 1: Gmail Integration — The Entry Point

Every journey starts with an email. Most of my mother’s medical information — PET/CT reports, blood tests, invoices, prescriptions — came into Gmail as attachments. I set up a Gmail Trigger node to fetch every new email with a medical-related attachment. This ensured nothing slipped through.

Why? Because manually downloading and renaming files was error-prone. Automating this saved us hours every week.

🧠 Step 2: Text Classifier — Sorting the Chaos

Once emails were captured, the next challenge was classification. A PET scan report looks very different from a pharmacy invoice, and handling them required different workflows.

I used n8n’s AI Text Classifier with an LLM backend. It looked at the subject line and email body to classify attachments into buckets:

* PET/CT/Histopathology Reports
* Blood Tests
* Medicines
* Bills/Invoices

Why? Doctors want quick access to specific information. If you mix blood tests with pharmacy bills, you create confusion. Classification gave structure.

📄 Step 3: Document Handling — Google Docs + Drive

For reports (PET/CT, Histopathology, Blood Tests), I set up a Google Docs creation and update flow:

Search Files & Folders Node → Look up if a document already exists for this category.

IF Node → If it exists → Update Document; else → Create New Document.

Why? Doctors often ask for longitudinal comparisons (e.g., “show me how her PET scans have evolved”). By updating existing documents instead of endlessly creating new ones, we built living documents with the full medical history.

💊 Step 4: Medicines Management — Structured Sheets

Medicine prices vary across pharmacies, and availability is tricky. Here I used:

Google Sheets → As a structured store for medicines.

Bright Data Scraper → To fetch real-time medicine prices and availability from GoodRx.

Custom Code Node → To dynamically generate drug URLs from sheet entries.

Why? When managing long-term prescriptions, cost matters. Automating price comparisons across pharmacies helped us save money and plan better.

📊 Step 5: Bills & Invoices — Organized Proofs

Bills and invoices were funneled into a Google Doc draft. Why a draft? Because sometimes these need manual edits before submission for insurance claims. By automating drafts, I reduced the grunt work while keeping flexibility.

🌐 Step 6: Bright Data + HTTP Requests — Real-Time Intelligence

Some data needed scraping beyond APIs. Initially, I struggled with datasets — I couldn’t find one directly in Bright Data’s dataset hub that fit my use case. After experimenting (and failing) to get prebuilt datasets working, I built a custom Bright Data collector with parser code. Then I connected it to n8n via the HTTP Request node to trigger scrapes dynamically and fetch results back into my workflow.

This was challenging but became the most powerful part of the system: real-time medicine price intelligence from the web. Also, the generate code feature was awesome and helped alot

📲 Step 7: Twilio Notifications — Closing the Loop

What good is all this if the caregiver (me) doesn’t know when new data arrives? I set up Twilio SMS/WhatsApp alerts at the end of each flow:

“New PET scan uploaded to Docs”

“Medicine price sheet updated”

“Invoice draft ready for insurance”

Why? Because healthcare is stressful enough. Getting real-time alerts meant I could focus on care, not file management.

### Bright Data Verified Node

I used the Bright Data Verified Node to scrape structured drug pricing and pharmacy details from GoodRx. It dynamically triggered collectors, fetched clean JSON, and integrated the results into Google Sheets and Docs. This allowed real-time tracking of medicine prices, availability, and related insights within my caregiver workflow.

## Journey

This project wasn’t about shiny tech — it was about reducing cognitive overload for caregivers. By chaining together Gmail, AI classifiers, Google Docs, Sheets, Bright Data scrapers, and Twilio alerts in n8n, I built my first AI agent and a personal healthcare automation system.

At first, it was frustrating to get Bright Data datasets connected — but that challenge pushed me to learn how to build my own collector and integrate it with HTTP nodes. That struggle turned into one of the most rewarding parts of this journey.

For my mother, it meant we always had answers when doctors asked for history. For me, it was a reminder that the best tech emerges when we solve problems close to home.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse

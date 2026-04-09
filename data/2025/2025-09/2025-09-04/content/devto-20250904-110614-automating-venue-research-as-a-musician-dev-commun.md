---
title: Automating Venue Research as a Musician - DEV Community
url: https://dev.to/yulia_dmitrievna_9724337b/automating-venue-research-as-a-musician-5f01
site_name: devto
fetched_at: '2025-09-04T11:06:14.252701'
original_url: https://dev.to/yulia_dmitrievna_9724337b/automating-venue-research-as-a-musician-5f01
author: Yulia Dmitrievna
date: '2025-09-01'
description: 🚀 What I Built As an independent musician, I spend a lot of time on manual search for... Tagged with devchallenge, n8nbrightdatachallenge, ai, webdev.
tags: '#devchallenge, #n8nbrightdatachallenge, #ai, #webdev'
---

n8n and Bright Challenge: Unstoppable Workflow

## 🚀 What I Built

As an independent musician, I spend a lot of time on manual search for venues. Scrolling through websites and looking for contact data takes a lot of time needed for creative work. I built an AI-powered venue discovery tool that analyses musician and venue websites and automatically finds performance opportunities.

✅ The demo video is availablehere.

✅ The n8n workflow JSON is publicly shared in aGitHub Gist.

✅ All data is tracked in thepublicly shared Airtable.

## ⚙️ What does it do?

The n8n music event aggregator is tool that:

• Scrapes concert pages from musician and venue websites using Bright Data• Uses n8n AI agent node to extract venue names, locations, dates, and contact information• Automatically discovers new musicians and venues from the extracted data• Builds a powerful database of performance opportunities• Removes duplicates through intelligent AI comparison• Runs continuously on scheduled triggers to keep the database fresh

*This tool aims to solve the core problem every independent musician faces: finding venues is time-consuming manual work that takes time away from creating music. *

## 🧱 Architecture

The workflow consists of three parts:

Core venue extraction pipeline

* Trigger: Manual start or run on schedule
* Data Source: Airtable databases for Musicians and Venues with "Pending" status
* Web Scraping: Bright Data extracts raw HTML from concert/event pages
* AI Processing: Claude 3.7 Sonnet analyzes content using structured output parsing
* Database Storage: Venue opportunities saved to "Extracted Events" table

Smart Deduplication System

* AI Comparison: LLM compares new discoveries against existing database
* Duplicate Detection: Handles variations in spelling, formatting, and venue names
* Auto-Creation: New musicians/venues automatically added with "New" status
* Status Tracking: Processed sources marked as "Completed" to prevent reprocessing

Source Discovery Automation

* Google Search Integration: SerpApi finds concert pages for new musicians/venues
* URL Collection: Event page URLs automatically added to database records
* Status Updates: Sources moved from "New" to "Pending" for processing
* Continuous Loop: System continuously discovers and processes new opportunities

## 📋 AI Model Configuration

• Model: Claude 3.7 Sonnet via OpenRouter• Temperature: 0.1 for• Output Format: Structured JSON schema with defined fields• System Instructions: Optimized for venue/contact information extraction

## 🎉 Bright Data Verified Node

Bright Data node handles web scraping of event webpages for further AI specific data extraction.

## 🌟 Inspiration

Like most independent musicians, I spend more time booking gigs than making music. Each venue requires individual research - finding their event calendar, understanding their booking process, identifying the right contact person.

This tool is aimed to solve my personal problem while potentially creating a pipeline that scales to help other independent musicians. Instead of spending weekends researching venues, artists would spend them writing songs. A database would constantly update performance opportunities.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse

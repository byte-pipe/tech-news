---
title: EduBox - AI Student Hub - DEV Community
url: https://dev.to/aryprogrammer/edubox-ai-student-hub-21il
site_name: devto
fetched_at: '2025-09-26T11:06:33.594886'
original_url: https://dev.to/aryprogrammer/edubox-ai-student-hub-21il
author: Arya Pratap Singh
date: '2025-09-22'
description: This is a submission for the KendoReact Free Components Challenge. TLDR; for working... Tagged with kendoreactchallenge, react, webdev, devchallenge.
tags: '#kendoreactchallenge, #react, #webdev, #devchallenge'
---

This is a submission for theKendoReact Free Components Challenge.

TLDR;for working professionals

Life gets messy: deadlines change, tasks pile up, and campus life adds variables you didn’t plan for. EduBox is about balance — keeping things manageable so you can do more, worry less. Whether you're a freshman overwhelmed by schedule, or a senior juggling multiple commitments, EduBox helps you stay on top without burning out.

## What I Built

I built EduBox because I was tired of juggling a million different apps and tools as a student. You know how it is - notes scattered across Google Drive, assignments tracked in some random spreadsheet, campus events you only hear about by chance, and that constant anxiety about missing deadlines. So I created this intelligent student hub that brings everything together in one place.

EduBox uses AI to help students stay organized and on top of their academic life. It has smart file management with semantic search (so you can actually find your notes when you need them), an intelligent planner that learns your patterns and helps you avoid those last-minute cram sessions, a campus life hub to keep you connected with clubs and events, and even an AI assistant that can answer questions about your own materials and can CREATE new assignments/study sessions etc - thx to tool calling. It's like having a personal academic organizer that actually understands what you're studying. AI Content Generation, Markdown Fast Editor (thx Kendo), Study Assistant, Huge Context Storage, Data Import/Export feature and your profile management space.

Tech Stack (High Level):

* Frontend: Next.js + TypeScript, styled with Tailwind for a responsive, accessible UI.
* Authentication: Clerk for secure user sign-in and profiles.
* Sync/Storage: Convex for real-time sync and simple serverless data operations.
* AI & Agents: Multi-agent orchestration built with CopilotKit, LLMs hosted via Vertex/ Gemini using Tools, and Kendo RAG (retrieval-augmented generation) to ground model answers in user notes and documents.
* UI/UX components: KendoUI - powered widgets to speed up development.
* Deployment: Frontend - Vercel setup, Backend - Render, Both having environment-driven configuration for keys and providers.

Need More? See the application - it definitely has more, I kept working at it endlessly :)

## Demo

The Demo is crazy, I had a feeling it would go wrong [but it didn't, glad]:Demo Video on Youtube

The application is live on vercel:Website

And the source code:Source Code

Note: Some features might have stopped working on the deployment due to currently being on trial plan. Try to use your .env and local environment in that case.

## Screenshots [Some were taken During Development]

### Landing Page

Beautiful landing page with threejs component

### Dashboard & Overview

Academic progress tracking and analytics

User profile and settings

### AI Assistant & Chat

AI assistant home interface

Conversation with AI assistant having Tools

AI-powered study assistance

AI content generation feature

### Search & RAG

Retrieval-augmented generation Usage

Knowledge base and document processing in NucliaDB

### Planner & Scheduling

Intelligent planning and schedule management

### File Management

File organization and management interface

Advanced file operations and search

Data import and export functionality

### Backend Service

Nuclia Document synchronization service

Convex Real-time database management

Schematic Billing and feature gating system

### Additional Features

Premium feature access control Component

## KendoReact Components Used

I really went all-in with KendoReact components for EduBox! Here's what I used:

* KendoReact Buttons- These gave all my UI buttons that professional, polished look with smooth ripple effects
* KendoReact Indicators- Perfect loaders that I sprinkled throughout the app for those "please wait" moments
* KendoReact PDF- Made it super easy to export analytics reports as PDFs
* KendoReact Progress Bars- Great for showing upload progress in the file management section
* KendoReact Ripple- Added those satisfying ripple effects to buttons, switches, dropdowns - makes everything feel more interactive
* KendoReact ScrollView- Made by Landing Page more beautiful by allowing me to add an endless scrolling screenshots section
* KendoReact Sortable- Implemented drag-and-drop functionality for organizing files
* KendoReact Taskboard- Built the entire planner interface around this
* KendoReact Upload- Handles all the file uploads
* KendoReact Editor- Rich text editing capabilities for when students need to format their notes
* Kendo Theme Default- Makes the component color scheme shifting too easy in both themes

These components saved me so much time and made the UI look way more professional than if I'd built everything from scratch.

## Coded Smarter using Kendo AI Coding Assistant

Oh man, Kendo AI Assistant was a game-changer for building EduBox! I used it as my AI coding assistant many times in the entire development process. It wasn't just about writing code - it became my coding buddy that helped me think through problems and implement solutions.

Here's how it helped me:

* Component Creation is Pure Insane: It can literally create a very very complex component within seconds. I was stuck on something - I had an idea that I can go the Highway and create the react component with a somewhat complex logic to create a UX that I imagined. Instead I asked Kendo AI and to my surprise the answer was simply called "Sortable". It is a component which I wanted to created, Kendo already has it but This AI Assistant made the Integration too easy. Saved me multiple times. It helped me build complex components and created TypeScript interfaces
* Debugging Partner: When I was stuck on integration issues in the frontend components and pages with various AI services and data fetching, it helped me identify and fix problems
* Architecture Advice: It gave me great suggestions for organizing the existing component structure and how to integrate all these different services with kendo components

The AI assistant was especially helpful for:

* Making complex components and handling proper data methods
* Modifying existing components to add UX
* Setting up the multi-service architecture
* Creating responsive UI components with proper TypeScript typing
* Optimizing component performance

Without Kendo AI Assistant, this project would have taken way longer and probably had a lot more bugs. Quick Challenge - Find as many Bugs you can and raiseissues

## Progress/Kendo NucliaDB RAG Integration

I integrated Nuclia RAG as the brains behind EduBox's search capabilities, and it completely transformed how students can interact with their academic materials. Instead of just keyword searching, students can now ask natural questions and get intelligent answers based on their own documents. You ask about your photos, your chats , your assignments, files, contents, schedule, dining, events - literally anything. You will get an answer + You will get the source + Everything is constantly updated via their sync APIS + Insane retrieval speed. Man, Kudos to them for creating such a useful service, though the live version might not be having it for more time - its on trial usage for now

The integration has two main parts:

Backend Service: I built a custom Node.js service that handles all the document processing. It automatically creates personalized knowledge bases for each user, runs background processing for file uploads, and provides clean API endpoints for the frontend to use. It SYNCS your userContext to the NucliaDB which is operatedonby them to vectorize find similarities etc etc., and we can query using their widgets and response generation is via ChatGpt + Azure model in my case - there are lots of options on their website. Super duper cool and easy.

Frontend Integration: Their is a nuclia popup rag component which is basically a search component (more of a widget) provided by Nuclia itself that queries Nuclia to search across all a user's documents semantically. When you upload a PDF or document, it gets indexed immediately so you can search it right away. The AI can pull relevant information from your materials to give contextually appropriate answers. The frontend triggers the backend request when hash of userContext changes. The backend then does the syncing via Nuclia API.

What makes this special is that students can ask questions like "What are the key points from my calculus notes?" or "Find information about the assignment due next week" and actually get accurate, helpful responses based on their own uploaded materials. It's like having an AI tutor that knows everything you've studied or wanted to :|

The whole setup ensures privacy too - each user gets their own Hash in the Nuclia KB, so their academic materials stay personal and secure.

## What's next for EduBox — AI Student Hub

* Improved onboarding and initial setup flow so new users quickly import notes from softwares like obsidian/notion/joplin, and see value.
* Connectors like Google Calendar, iCal, Canvas/Blackboard for two-way sync and grade/task ingestion. Zoom and Gmeet Integration, Youtube API Integration and GDrive store Integration.
* Mobile-first polish (PWA or native clients) and accessibility improvements.
* Plugin/connector system so third parties can add data sources or custom agent behaviors. Obviously less challenging and can be done now too but requires architectural changes to create maybe a gateway and interdependencies.

## Additional Info:

### Architectural Diagram [Very High Level]

### Project Structure [Pretty Simple]

EduBox/
├── frontend/
│ ├── app/
# App Router pages and API routes

│ ├── components/
│ │ ├── schematic/
# Schematic billing components

│ │ └── ui/
│ ├── convex/
# Convex database schema and functions

│ ├── lib/
# Utility libraries

│ ├── hooks/
# Custom React hooks

│ └── types/
# TypeScript type definitions

├── backend/
│ └── nuclia-sync/
# Nuclia document sync service

└── README.md

Enter fullscreen mode

Exit fullscreen mode

#### The Project also uses Schematic - which internally has stripe management to provide plan based usage. It has LIMITED-FREE/Starter/Pro Plans. Currently all users are defaulted to LIMITED-FREE plan to access all features. This is a working payment gateway solution which is efficiently managed by schematic.

Try asking:

“What’s due tomorrow?”

“Find me my biology notes from last week.”

“Do I have time to hit the gym before physics class?”

For Setup Details REFER README.md of GitHub

Very happy to create such anusefulandworkingproduct. It was so easy to read thedocumentation of Kendoand think about creating a full fledged application. I would recommend everyone to test the application at least once, I found my joy creating this.

Do checkoutKendo Docsfor more details andNuclia RAG DB. Incase of Issues you can always askKendo AI Assistant

Kendo UIProgress/Kendo RAG

That's it for now, Looking forward to crazy new possibilities with this - Now that I can manage my life better.

For queries/suggestions/doubts or maybe a bit chit-chatContact Me:arya.2023ug1104@iiitranchi.ac.in

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (20 comments)


For further actions, you may consider blocking this person and/orreporting abuse

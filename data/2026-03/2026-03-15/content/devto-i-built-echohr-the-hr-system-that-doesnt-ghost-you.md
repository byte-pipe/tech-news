---
title: 'I Built EchoHR: The HR System That Doesn’t Ghost You - DEV Community'
url: https://dev.to/ujja/i-built-echohr-the-hr-system-that-doesnt-ghost-you-1c2i
site_name: devto
content_file: devto-i-built-echohr-the-hr-system-that-doesnt-ghost-you
fetched_at: '2026-03-15T06:00:17.268423'
original_url: https://dev.to/ujja/i-built-echohr-the-hr-system-that-doesnt-ghost-you-1c2i
author: ujja
date: '2026-03-12'
description: This is a submission for the Notion MCP Challenge Rejections hurt. But ghosting hurts even... Tagged with devchallenge, notionchallenge, mcp, ai.
tags: '#devchallenge, #notionchallenge, #mcp, #ai'
---

Notion MCP Challenge Submission 🧠

This is a submission for theNotion MCP Challenge

Rejections hurt. But ghosting hurts even more.

EchoHR is aNotion-native employee lifecycle systemthat ensures candidates and employees always receive timely updates, feedback, and visibility across their entire journey.

The goal is simple:

No candidate or employee should ever feel ghosted.

## What I Built

EchoHR is a fully automated employee lifecycle management system built on top of Notion MCP.

It provisions an entire HR operating system inside Notion, including:

* 20+ interconnected lifecycle data sources
* versioned workspace hubs
* relations and rollups across the entire employee journey
* automation playbooks
* AI-ready fields for feedback and summaries
* startup-scale demo datasets

The system covers the complete lifecycle:

Candidates → Applications → Interviews → Offers → Onboarding → Check-ins → Goals → Achievements → Performance Reviews → Compensation → Offboarding → Alumni

All records are connected through Notion relations and rollups, enabling a complete view of every employee journey.

To make experimentation easy for hackathons and demos, EchoHR can provision the entire workspace with one command.

This instantly creates:

* lifecycle pipelines
* feedback workflows
* onboarding journeys
* review systems
* promotion tracking
* exit processes
* dashboards and demo data

## Video Demo

Suggested demo flow:

1. One-command provisioning of the EchoHR workspace
2. Hiring pipeline with candidate progress
3. Automated onboarding journeys
4. AI-generated interview summaries
5. Slack notification workflows
6. Lifecycle dashboards and reporting

## Show us the code

GitHub repository:

https://github.com/ujjavala/EchoHR

The repository includes everything needed to spin up a fully functional EchoHR workspace.

## How I Used Notion MCP

EchoHR uses Notion MCP as the operational layer for lifecycle management.

It enables AI agents, automation workflows, and integrations to operate directly on structured HR data.

### Notion MCP (hosted)

Notion MCP provides the primary CRUD and schema layer for lifecycle operations.

It is used for:

* provisioning databases
* creating lifecycle records
* updating candidate stages
* logging check-ins
* posting AI summaries

EchoHR includes a one-click workspace provisioning command:

npm run demo

These provisions:

* pages
* data sources
* relations
* rollups
* demo records
* automation playbooks

Agents can then operate on the workspace through MCP.

### Slack MCP

Slack MCP enables human-first notifications so important updates never stall.

Examples include:

* candidate update reminders
* onboarding alerts
* offer acceptance notifications
* overdue feedback pings

This ensures recruiters and managers stay responsive.

### Figma MCP

EchoHR integrates with design workflows through Figma MCP.

Example automation:

When a Figma frame is marked Ready for Review:

* A review task is created in Notion
* The task links to the relevant check-in
* A Slack notification is posted

This bridges the design → product → engineering workflow.

### Calendar MCP Pattern

EchoHR uses calendar MCP patterns to schedule lifecycle events.

Examples:

* interview loops
* onboarding meetings
* post-offer check-ins

Agents create tasks in Notion and schedule them via calendar integrations.

### OpenAI MCP (automation server)

EchoHR includes an automation server that processes lifecycle notes and generates structured summaries.

Example endpoint:

/webhooks/meeting-notes

This converts raw notes into:

* interview feedback summaries
* candidate-safe responses
* manager action items

The summaries are written back into Notion records automatically.

## Core Components

### Notion Workspace Seeder

The workspace seeder provisions the entire HR operating system.

It creates:

* lifecycle databases
* relations and rollups
* templates
* automation playbooks
* demo datasets

Running the setup creates a fully operational HR workspace inside Notion.

### Automation Server

EchoHR includes a lightweight automation server that connects Notion to external systems.

Endpoints include:

POST /webhooks/notion

POST /webhooks/figma

POST /webhooks/meeting-notes

POST /summaries/interview

POST /summaries/review

POST /summaries/exit

POST /slack/notify

GET /health

Enter fullscreen mode

Exit fullscreen mode

These endpoints power automated workflows across the employee lifecycle.

## Example Automations

### Candidate Workflow

When a new candidate is created in Notion:

* An application record is automatically created
* An SLA follow-up task is assigned to the recruiter

### Offer Workflow

When an offer status becomes Accepted:

* An onboarding journey is created
* The first three monthly check-ins are scheduled
* onboarding tasks are generated

### Design Workflow

When a Figma frame is marked Ready for Review:

* A review task is created in Notion
* The task attaches to the relevant check-in
* A Slack notification is posted

## AI-Powered Feedback

EchoHR integrates with OpenAI to generate summaries for:

* interview feedback
* performance reviews
* exit interviews

Example flow:

1. Interview notes are captured
2. /webhooks/meeting-notesprocesses them
3. AI generates candidate-safe summaries and manager action items
4. The results are written back into Notion
5. Slack notifications ensure feedback never stalls

## Demo Dataset

To make the system immediately usable, EchoHR seeds a realistic startup environment with:

* ~50 employees
* founders and executives
* HR and people operations
* managers and ICs
* open roles
* active hiring pipelines
* onboarding journeys
* performance reviews
* promotions and compensation events
* recognition and pulse surveys
* exit processes

This allows dashboards and workflows to be demonstrated instantly.

## One-Command Setup

Run:

npm run demo

This automatically:

* provisions the Notion workspace
* creates lifecycle databases
* seeds demo records
* configures relations and rollups

You can also create a fresh versioned workspace:

npm run demo \-- \--force-new

Each installation creates a new workspace version, such as:

* EchoHR HQ v1
* EchoHR HQ v2

This makes experimentation safe during hackathons.

## The Differentiator

Most HR software focuses on compliance and reporting.

EchoHR focuses on human experience.

It introduces the concept of:

## Zero-Ghosting Lifecycle Management

Candidates should never wonder:

"Did they forget about me?"

Employees should never wonder:

"Am I doing well here?"

EchoHR enforces transparency through automated lifecycle checkpoints:

* candidate update deadlines
* interview feedback reminders
* onboarding check-ins
* review timelines
* promotion visibility
* exit follow-ups

Everything is tracked through interconnected Notion data sources.

## Limitations (Current Notion Constraints)

Some capabilities are limited by the current Notion API.

### Database Views

The API cannot create board, timeline, or gallery views.

EchoHR automatically creates a page called:

Set up Views (5–10 min)

This guides users through configuring dashboards manually.

### Visual Styling

Notion does not support custom CSS through the API.

Visual structure uses:

* page covers
* emojis
* callouts
* curated views

### Charts

Notion charts depend on workspace features.

If unavailable, charts can be embedded from external sources such as:

* Google Sheets
* Datawrapper

### Formula Updates

Formula properties cannot currently be modified after creation through the API.

They must be defined during provisioning.

## Why This Matters

Hiring and employee management systems often fail at one simple thing:

communication.

Candidates get ghosted.Employees receive little feedback.Performance reviews disappear into silence.

EchoHR demonstrates how Notion + MCP + AI automation can create a transparent and human-first operating system for people operations.

Instead of spreadsheets and disconnected tools, teams get a single lifecycle workspace where every stage is visible and actionable.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (38 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
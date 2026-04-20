---
title: I Built EchoHR: The HR System That Doesn’t Ghost You - DEV Community
url: https://dev.to/ujja/i-built-echohr-the-hr-system-that-doesnt-ghost-you-1c2i
date: 2026-03-12
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-03-15T06:02:28.395703
---

# I Built EchoHR: The HR System That Doesn’t Ghost You - DEV Community

# Summary of EchoHR Submission

## Overview
- EchoHR is a Notion‑native employee lifecycle system designed to eliminate ghosting for candidates and employees.
- Built on Notion MCP, it provides end‑to‑end HR automation, visibility, and AI‑enhanced feedback.

## What I Built
- A fully automated HR operating system inside Notion with:
  - 20+ interconnected lifecycle databases
  - Versioned workspace hubs
  - Relations and rollups covering the entire employee journey
  - Automation playbooks and AI‑ready fields
  - Startup‑scale demo datasets
- Covers the full lifecycle: Candidates → Applications → Interviews → Offers → Onboarding → Check‑ins → Goals → Achievements → Performance Reviews → Compensation → Offboarding → Alumni.
- One‑command provisioning creates all pipelines, workflows, dashboards, and demo data instantly.

## Video Demo (Suggested Flow)
1. One‑command workspace provisioning
2. Hiring pipeline with candidate progress
3. Automated onboarding journeys
4. AI‑generated interview summaries
5. Slack notification workflows
6. Lifecycle dashboards and reporting

## Show Us the Code
- GitHub repository: https://github.com/ujjavala/EchoHR
- Contains everything needed to spin up a functional EchoHR workspace.

## How I Used Notion MCP
- **Notion MCP (hosted)**: Primary CRUD and schema layer for provisioning databases, creating records, updating stages, logging check‑ins, and posting AI summaries.
- **Slack MCP**: Human‑first notifications for candidate updates, onboarding alerts, offer acceptances, and overdue feedback pings.
- **Figma MCP**: Bridges design to product by creating Notion review tasks and Slack alerts when a Figma frame is marked “Ready for Review”.
- **Calendar MCP Pattern**: Schedules interview loops, onboarding meetings, and post‑offer check‑ins via calendar integrations.
- **OpenAI MCP (automation server)**: Processes raw meeting notes into structured interview feedback, safe candidate responses, and manager action items.

## Core Components
- **Notion Workspace Seeder**: Provisions all HR databases, relations, rollups, templates, automation playbooks, and demo data.
- **Automation Server**: Lightweight server exposing endpoints for Notion, Figma, meeting notes, summaries, Slack notifications, and health checks.

## Example Automations
- **Candidate Workflow**: New candidate → automatic application record + SLA follow‑up task for recruiter.
- **Offer Workflow**: Offer accepted → onboarding journey created, first three monthly check‑ins scheduled, onboarding tasks generated.
- **Design Workflow**: Figma frame ready → Notion review task created, linked to check‑in, Slack notification posted.

## AI‑Powered Feedback
- Integrates OpenAI to generate summaries for interview feedback, performance reviews, and exit interviews.
- Flow: capture notes → `/webhooks/meeting-notes` processes → AI generates safe summaries & action items → write back to Notion → Slack notifies.

## Demo Dataset
- Seeds a realistic startup environment with ~50 employees, founders, HR staff, managers, open roles, active pipelines, onboarding journeys, performance reviews, promotions, compensation events, recognition surveys, and exit processes.

## One‑Command Setup
- `npm run demo` provisions the Notion workspace, creates databases, seeds records, and configures relations/rollups.
- `npm run demo -- --force-new` creates a fresh versioned workspace (e.g., EchoHR HQ v1, v2) for safe experimentation.

## Differentiator: Zero‑Ghosting Lifecycle Management
- Focuses on human experience rather than compliance alone.
- Enforces transparency through automated checkpoints:
  - Candidate update deadlines
  - Interview feedback reminders
  - Onboarding check‑ins
  - Review timelines
  - Promotion visibility
  - Exit follow‑ups

## Limitations (Current Notion Constraints)
- **Database Views**: API cannot create board, timeline, or gallery views; users must set up manually via a “Set up Views” page.
- **Visual Styling**: No custom CSS via API; relies on covers, emojis, callouts, and curated views.
- **Charts**: Native Notion charts depend on workspace features; external embeds (Google Sheets, Datawrapper) are alternatives.
- **Formula Updates**: Formulas must be defined during provisioning; cannot be modified later via API.

## Why This Matters
- Communication failures (ghosting, lack of feedback) are the biggest pain points in hiring and employee management.
- EchoHR demonstrates that Notion + MCP + AI automation can deliver a transparent, human‑first operating system, replacing fragmented spreadsheets and disconnected tools with an integrated, responsive HR platform.

---
title: 'Ozigi v2 Changelog: Building a Modular Agentic Content Engine with Next.js, Supabase, and Playwright - DEV Community'
url: https://dev.to/dumebii/ozigi-v2-changelog-building-a-modular-agentic-content-engine-with-nextjs-supabase-and-playwright-59mo
site_name: devto
content_file: devto-ozigi-v2-changelog-building-a-modular-agentic-cont
fetched_at: '2026-03-03T11:16:21.592163'
original_url: https://dev.to/dumebii/ozigi-v2-changelog-building-a-modular-agentic-content-engine-with-nextjs-supabase-and-playwright-59mo
author: Dumebi Okolo
date: '2026-03-02'
description: 'When I first built Ozigi (initially WriterHelper), the goal was simple: give content professionals in... Tagged with webdev, showdev, nextjs, playwright.'
tags: '#showdev, #webdev, #nextjs, #playwright'
---

When I first builtOzigi(initially WriterHelper), the goal was simple: give content professionals in my team a way to break down their articles into high-signal social media campaigns.

OziGi has now evolved to an open source SaaS product, oepn to the public to use and imnprove.

Here is the complete technical changelog of how I completely turned Ozigi from a monolithic v1 MVP into a production-ready v2 SaaS.

## 1. Modular Refactoring of The App.tsx (Separation of Concerns)

In v1, my entire application: auth, API calls, and UI—lived inside a longapp/page.tsxfile. The more changes I made, the harder it became to manage.

* Modular Component Library:I stripped down the monolith and broke the UI into pure, single-responsibility React components (Header,Hero,Distillery, etc.).

* Centralized Type Safety:I created a globallib/types.tsfile with a strictCampaignDayinterface (complete with index signatures) to finally eliminate the TypeScript "shadow type" build errors I was fighting.
* State Persistence:ImplementedlocalStoragesyncing so the app "remembers" if a user is in the dashboard or the landing page, preventing frustrating resets on browser refresh.

## 2. Using Supabase as the Database and Tightening the Backend

A major UX flaw in v1 was that refreshing the page wiped the user's progress.

* Relational Database & OAuth:I replaced anonymous access with secure GitHub OAuth via Supabase.
* Automated Context History:I engineered a system that auto-saves every generated campaign to a PostgreSQL database. Users can now restore past URLs, notes, and outputs with a single click.

* Identity Storage:Built a settings flow to permanently save a user's custom "Persona Voice" and Discord Webhook URLs directly to their profile.

## 3. Core Feature Additions

* Multi-Modal Ingestion:Upgraded the input engine to accept both a live URLandraw custom text simultaneously.

* Native Discord Deployment:Built a dedicated API route and UI webhook integration to push generated content directly to Discord servers with one click.

## 4. Update UI/UX & Professional Branding

* The Rebrand:Pivoted the app's messaging to focus entirely on content professionals, positioning it as an engine to generate social media content with ease and in your own voice.
* Open-First Onboarding:Designed a "Try Before You Buy" workflow. Unauthenticated users can test the AI generation seamlessly, but are gated from premium features (History, Personas, Discord) via an Upgrade Banner.

* Pixel-Perfect Layouts & SEO:Eliminated rogue whitespace andz-indexissues using precise CSS Flexbox rules. Upgradedapp/layout.tsxwith professional OpenGraph and Twitter Card metadata.

## 5. Quality Assurance & DevOps (Automated Playwright E2E Tests)

* Automated E2E Testing:Completely rewrote the Playwright test suite (engine.spec.ts) to verify the new landing page copy, test the navigation flow, and confirm security rules apply correctly.
* Linux Dependency Fixes:Patched my CI/CD pipeline by ensuring underlying Linux browser dependencies (--with-deps) are installed so headless Chromium tests pass flawlessly.

## What's Next? (v3 Roadmap)

With the Context Engine now stable, the foundation is set.My plan for V3 is to fix the deployment pipeline:

* integrating the native X (Twitter)
* LinkedIn APIs so users can publish directly from the Ozigi dashboard.

What has been your biggest challenge scaling a Next.js MVP? Let me know in the comments!Try outOzigiAnd let me know if you have any feature suggestions? Let me know!Want to see my poorly written code? FindOziGi on Github.

Connect with me onLinkedIn!

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (11 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse
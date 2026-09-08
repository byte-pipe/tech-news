---
title: Deploy a SaaS App to Production With Claude Code (No Coding)
url: https://www.productcompass.pm/p/product-engineering-for-pms-part-2
date: 2026-09-09
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-09-09T08:37:44.081866
---

# Deploy a SaaS App to Production With Claude Code (No Coding)

# Deploy a SaaS App to Production With Claude Code (No Coding)

## 1. Overview  
- The post is part 2 of a series showing how a product manager can build and launch a multi‑tenant SaaS app without writing code.  
- The app, **AskOne**, is a Slido‑style Q&A and polling platform.  
- The guide walks through adding a moderator role and moving the app to production using GitHub, Supabase, Netlify, a custom domain, Clerk, analytics, and Google authentication.  

## 2. A Lightweight AI Software Lifecycle  
- **Step 1 – Idea:** Use Claude to brainstorm, ask clarifying questions, and generate an interactive prototype.  
- **Step 2 – Refined Idea:** Define jobs‑to‑be‑done, user scenarios, constraints, and UX decisions; output a markdown file.  
- **Step 3 – Plan:** Let the AI inspect the codebase and produce a detailed implementation plan (architecture, files to change, tests, risks).  
- **Step 4 – Build:** AI writes the feature, runs unit tests, and the PM validates key UI flows manually.  

## 3. Adding a Moderator Role to AskOne  
- **Switch to organization billing:**  
  - Cancel any active user subscriptions in Clerk, then disable user billing and enable organization billing.  
- **Define organization plans:**  
  - Free plan (default) – 1 active room, up to 100 participants.  
  - Premium plan – up to 10 active rooms, up to 1,000 participants, with monthly/annual options.  
  - Feature keys (e.g., `rooms_10`, `participants_1000`) are set to allow flexible gating.  
- **Rename Member to Moderator:**  
  - In Clerk > Organizations > Roles & Permissions, rename the default “Member” role to “Moderator” and set its key to `org:moderator`. Permissions remain unchanged.  

## 4. Production Setup Steps  
1. **Create a production GitHub branch** – branch from the main codebase to host the production version.  
2. **Create a production Supabase project** – provision a new Supabase instance for live data storage and authentication.  
3. **Create a production Netlify site** – connect the GitHub repo, enable continuous deployment, and set build settings.  
4. **Plug a custom DNS domain** – point the domain’s DNS records to Netlify, configure SSL.  
5. **Create a production Clerk instance** – duplicate the development Clerk setup, enable organization billing and the new moderator role.  
6. **Add product analytics** – integrate an analytics provider (e.g., Plausible, Mixpanel) via Netlify environment variables.  
7. **Add real Google Auth** – configure Google OAuth in Clerk and verify the flow works in production.  

## 5. Conclusion  
- The workflow demonstrates that a PM can orchestrate the entire SaaS lifecycle—ideation, planning, building, and deployment—using AI‑driven prompts and no manual coding.  
- By leveraging low‑code services (GitHub, Supabase, Netlify, Clerk) and AI assistants, the product reaches a production‑ready state quickly while the PM deepens engineering understanding.  

## 6. Additional Resources  
- Part 1 guide (building AskOne’s core features).  
- Live session recording of Part 2 (linked in the newsletter).  
- Product Compass newsletter for weekly AI product tips and templates.
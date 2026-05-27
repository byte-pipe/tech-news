---
title: Training our own AI models - PostHog
url: https://posthog.com/blog/training-ai-models
date: 2026-05-27
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-05-28T06:04:23.889516
---

# Training our own AI models - PostHog

# Training our own AI models

## What we want to build
- Two main goals:  
  1. Make existing PostHog products smarter, more proactive, and useful.  
  2. Create new products (e.g., PostHog Code) that help teams build better products faster.  
- Focus areas:  
  - **Session replay analysis** – improve scalability and automate issue detection using models trained on replay data.  
  - **Synthetic user testing** – predict user confusion or flow breaks before release, reducing manual testing workload.  
  - **Behavior prediction** – suggest changes to boost conversion and lower frustration, automating analysis and saving token costs.  
- Acknowledge experimental nature; expect iteration to identify effective training data and methods.

## How this will work
- Aim: shift from providing the best code to making the overall product better; PostHog Code is positioned as a “product editor.”  
- Data usage plan (opt‑out model):  
  1. EU cloud users are opted out by default.  
  2. Users with agreements prohibiting training (e.g., BAA, MSA) are opted out.  
  3. All other US cloud users are opted in by default.  
  4. All data will be anonymized before training.  
  5. Only data already present in a customer’s PostHog instance will be used.  
  6. PostHog will conduct all model training internally.  
  7. No selling or sharing of data with third‑party model providers.  
  8. Users can opt out anytime via org settings (admin access required).  
  9. Training starts on June 29, giving users time to decide.  
- Communication strategy: email to all customers, in‑app notifications, and public announcements (like this post).  
- Emphasis on improving the product, not monetizing customer data.

## Why this is opt out, not opt in
- Opt‑out is necessary to gather enough data for useful models.  
- Opted‑out users will miss new features that rely on the trained models.  
- EU‑cloud users can manually opt in if their legal agreements allow.  
- Transparency is prioritized over silent rollout.  
- Contact: “james at [email]” for discussion; hiring AI researchers is announced.

## Community questions
- Open invitation for users to ask questions about the initiative.
---
title: Email.md - Responsive Emails, Written in Markdown
url: https://www.emailmd.dev/
date: 2026-03-25
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-03-26T01:03:34.386911
---

# Email.md - Responsive Emails, Written in Markdown

# Email.md – Responsive Emails, Written in Markdown

## Overview
- Enables writing responsive email templates directly in Markdown, avoiding manual HTML.
- Provides a simple workflow: write Markdown → compile with `emailmd` → send.

## Core Features
- Front‑matter support for preheader text and theme selection (e.g., `dark`).
- Built‑in component blocks:
  - `header` for logos or branding.
  - `callout` for highlighted content such as codes.
  - `footer` for company details and unsubscribe links.
- Automatic rendering of responsive layouts suitable for various email clients.

## Example Template: `confirm-email.md`
- Front‑matter:
  - `preheader: "Confirm your email address"`
  - `theme: dark`
- Header block displays a logo image with a specified width.
- Main section includes:
  - Title “Confirm your email address”.
  - Instructions to enter the confirmation code.
- Callout block (centered, compact) shows the code `DFY‑X7U`.
- Footer block lists company address and an unsubscribe link.

## Tooling & Resources
- Install the compiler: `npm install emailmd`.
- Available resources:
  - Templates library.
  - Visual Builder for designing emails.
  - Documentation site.
  - GitHub repository for source code and contributions.

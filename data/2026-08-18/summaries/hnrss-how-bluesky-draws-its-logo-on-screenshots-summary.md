---
title: How Bluesky draws its logo on screenshots
url: https://timmarinin.net/2026/bluesky-screenshots/
date: 2026-08-17
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-08-18T12:12:57.507658
---

# How Bluesky draws its logo on screenshots

# How Bluesky draws its logo on screenshots

## Overview
- The author noticed a Bluesky logo appearing in screenshots of posts, while the app itself shows a “Follow” button instead.  
- Investigation revealed that the logo is hidden during normal app use but revealed when a screenshot is taken.

## Technical Explanation
- The behavior is implemented in the `GrowthHack.tsx` file (added Jan 2026 by mozzius).  
- It uses the `expo-privacy-sensitive` package, which:
  - Creates a `UITextField` with `isSecureTextEntry` set to `true`.  
  - Renders the button’s visual content into the text field’s layer.  
  - iOS automatically blanks the layer of secure text fields when a screenshot is captured, causing the underlying Bluesky logo to become visible.  
- On non‑iOS platforms the content is rendered normally without any masking.

## Why It Fails During App Switching
- During an app‑switch gesture iOS takes an early snapshot of the UI before the secure‑text‑field blanking occurs.  
- The screenshot then captures this static snapshot, which lacks the live `UITextField` that would trigger the masking, so the logo does not appear.

## Context and Reception
- The technique is a known privacy‑related trick; similar approaches are used by Telegram (secret chats) and Signal.  
- Some developers in the discussion thread criticized the method, but the conversation was locked.  
- The author finds the approach clever rather than malicious.

## Publication Details
- Published: Sunday, 16 August 2026  
- Author: mt
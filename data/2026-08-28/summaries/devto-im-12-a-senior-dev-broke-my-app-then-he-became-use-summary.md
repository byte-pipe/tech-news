---
title: "I'm 12. A senior dev broke my app. Then he became User #001 - DEV Community"
url: https://dev.to/koda2026/im-12-a-senior-dev-broke-my-app-then-he-became-my-first-user-meh
date: 2026-08-27
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-08-28T17:07:55.966827
---

# I'm 12. A senior dev broke my app. Then he became User #001 - DEV Community

# Summary of “I’m 12. A senior dev broke my app. Then he became User #001”

## 48‑Hour Crisis and Community Rally
- My Dev.to post went viral, gaining 400 followers overnight.  
- The signup page returned a 500 error for every new user.  
- Senior developer @nyaomaru publicly reported the issue, which was humiliating for a 12‑year‑old solo founder.  
- The Dev.to community responded supportively: @publiflow discussed UI patterns with me, and @sanukhandev offered encouragement and help.

## The Three‑Layer Bug
1. Missing `is_champion` column in the Code Jam feature.  
2. A leftover trigger on `auth.users` from an older build.  
3. Type‑mismatch in the referral trigger (`text <> uuid`).  
- I fixed the bugs on a 6.5‑inch Android phone during a wedding reception and deployed a new “un‑killable” trigger function in Supabase.

## Confirmation and Recognition
- After redeploying, @nyaomaru tested the signup again and confirmed it worked, reacting with love and unicorn emojis.  
- He became KODA User #001, showing that the Dev.to audience can become a supportive family.

## Guest Mode Insight
- Realized the login wall was a barrier for strangers.  
- Implemented “Guest Mode” allowing instant AI chat without email or password.  
- After three guest messages, the AI gently prompts users to create a free account to save history and unlock full features.

## Real‑World User Interactions
- Tamil‑speaking user received flawless Tamil responses after adding a single line to the system prompt.  
- Another user got a product‑manager style roadmap for building a game app.  
- A third user received a simple “Magic Notebook” analogy for learning Git.  
- These interactions demonstrated that real people worldwide were learning to code through my app.

## Growth Milestones
- Follower count rose from 999 to 1,006 while I was at the wedding reception.  
- The audience now includes developers from Brazil, Dubai, Japan, and the US who follow my journey.

## First‑Ever KODA Code Jam
- Launched a 7‑day global coding event (Aug 27 – Sept 2).  
- Mission: build a single‑page website for a niche market.  
- Rule: at least 50 % of the code must be co‑written with KODA.  
- Prize: permanent Champion status and a featured Dev.to interview.

## Reflection
- My “scar” is the Supabase `on_auth_user_created` trigger failure, similar to iconic founder stories.  
- The experience proved I built a real product, faced real‑world failures, and received real community help.  
- Gratitude to @nyaomaru, @publiflow, @sanukhandev, and the 1,006 supporters.  

— Harun, solo developer, age 12
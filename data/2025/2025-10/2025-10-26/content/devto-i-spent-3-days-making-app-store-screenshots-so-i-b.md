---
title: I Spent 3 Days Making App Store Screenshots (So I Built a Tool That Does It in 15 Minutes) - DEV Community
url: https://dev.to/mateusz_b9/i-spent-3-days-making-app-store-screenshots-so-i-built-a-tool-that-does-it-in-15-minutes-39cn
site_name: devto
fetched_at: '2025-10-26T11:08:26.796311'
original_url: https://dev.to/mateusz_b9/i-spent-3-days-making-app-store-screenshots-so-i-built-a-tool-that-does-it-in-15-minutes-39cn
author: Mateusz
date: '2025-10-24'
description: Why I Built Lemmi Studio Because App Store Screenshots Are the Worst Part of... Tagged with startup, mobile, ai, ios.
tags: '#startup, #mobile, #ai, #ios'
---

# Why I Built Lemmi Studio

## Because App Store Screenshots Are the Worst Part of Launching

TL;DR:I spent 3 days designing screenshots for my last app launch. It should've taken 15 minutes. So I built Lemmi Studio—an AI tool that generates App Store screenshots, marketing copy, and landing pages automatically.

Try it free →

## The Problem Every mobile Developer Faces 😫

You've just spent 3 months building your app. The code is clean. The features work. You're ready to ship.

Then you hit the wall:marketing assets.

Sound familiar?

### What You Actually Need 📋

* 10 polished App Store screenshots (1200×2600px, device-framed)
* App Store copy (title, subtitle, description, keywords)
* A landing page
* Everything optimized for ASO

### The Problem? You Can't Design 🎨

Or write marketing copy. Or build marketing sites.

### Your "Options" 🤔

1. Hire a designer→ $500-1,000 + wait 1-2 weeks
2. Learn Figma yourself→ 20+ hours of tutorials
3. Use Canva→ still 4-6 hours per app
4. Ship with ugly screenshots→ tank your conversion rate

Spoiler:None of these are good if you're a solo developer shipping fast.

I know becauseI've launched a few apps. Every single launch, this was the bottleneck.

## The Solution I Wish Existed 💡

After my last launch (where I spent 3 days in Figma), I sketched out my dream tool:

The Perfect Tool Would:✨

* ✅ Take my raw iPhone screenshots
* ✅ Generate professional device-framed marketing images
* ✅ Write all the App Store copy (optimized for ASO)
* ✅ Build a landing page
* ✅ Do it all in under 15 minutes
* ✅ Cost less than one designer hour

That tool didn't exist.

So I built it 🤓

## Meet Lemmi Studio 🚀

Your AI-powered go-live kit for app launches.

Upload screenshots → Get complete marketing assets in 15 minutes.

### Here's What It Does 💪

#### 1. AI-Generated App Store Copy 📝

* Title & subtitle (optimized for 30-char limits)
* Promotional text (170-char hook)
* Full description (ASO-optimized)
* Keywords
* Screenshot captions

Real-time character counters ensure you never exceed Apple/Google limits.

#### 2. Professional Marketing Screenshots 🎨

* Device frames (iPhone, iPad)
* Gradient backgrounds (auto-extracted from your app colors or custom)
* Typography overlays (10+ professional fonts)
* App Store–ready sizes (1290×2796 for 6.7" displays, 1242×2688 for 6.5")

#### 3. Visual Canvas Editor ✨

* Multi-screenshot editing workspace
* Drag-and-drop customization
* Change backgrounds, fonts, colors
* Upload custom graphics and logos
* Live preview with zoom (25%-200%)
* Auto-save

#### 4. Landing Page Generator 🚀

* Complete static website (HTML/CSS/JS)
* Hero section, features, FAQ, CTA
* Fully responsive
* SEO-ready with meta tags
* One-click export as ZIP

#### 5. Multi-Language Support 🌍

* Generate everything in 6+ languages
* English, French, Spanish, German, Italian, Polish
* All features work in every language

## How It Works (The 15-Minute Process) ⚡

### Step 1: Upload Your Screenshots ⏱️ 2 min

Drag in up to 10 raw screenshots. Lemmi automatically detects device type and validates orientation.

### Step 2: Let AI Do Its Magic ⏱️ 3 min

AI analyzes your screenshots and generates:

* ✅ All App Store copy fields
* ✅ Device-framed marketing images with backgrounds
* ✅ Landing page content

### Step 3: Fine-Tune in Studio Editor ⏱️ 5-10 min

Visual canvas editor lets you customize everything:

* Edit text overlays
* Change gradient backgrounds (8 directions: top-to-bottom, diagonal, radial)
* Upload your logo
* Adjust fonts and colors
* Add custom graphics

Customize everything visually—no code required.

### Step 4: Export & Ship ⏱️ 1 min

Download everything as organized ZIP files:

* 📱 Marketing images → upload directly to App Store Connect
* 🌐 Landing page → download ZIP package and host anywhere (Netlify, Vercel, etc.)
* ✅ All organized and ready to use

⏱️ Total time: 15 minutes from upload to ready-to-ship.

## The Tech Stack

Frontend:

* Next.js 15 (App Router) for Landing Page
* React
* TypeScript
* Shadcn styled components
* Fabric.js for canvas editor

Backend:

* Express.js
* Supabase (PostgreSQL + Auth + Storage)
* Google Gemini for content generation
* Prisma ORM

Infrastructure:

* Vercel, Railway for hosting
* Stripe for billing

Why these choices:

* Next.js:Fast iteration, great DX, built-in API routes
* Supabase:PostgreSQL + Auth + Storage in one, generous free tier
* Gemini-2.5-flash:Best at maintaining context across multiple copy fields, perfect multi-modal support
* Canvas:Battle-tested JS framework for complex client-side editing

## Pricing (No Surprises) 💰

### 🆓 Free Tier

* 10 credits for totally free
* 3 projects
* All core features

Perfect for:Trying it out or launching 1 app/month

### 💎 Indie — $9.99/month

* 50 AI credits/month
* 20 projects
* Priority support

Perfect for:Solo developers shipping regularly

### 🚀 Studio — $29.99/month

* 150 AI credits/month
* 50 projects
* Team features

Perfect for:Small teams or agencies

### What's a Credit? 🎟️

Think of credits like tokens:

* 1 credit = Generate one App Store copy field
* 1 credit = Generate one marketing image
* 2 credits = Generate complete landing page

Pro tip:Add-on packs available (100 credits for $5, never expire)

### Why This Pricing? 🤷‍♂️

Simple: It'sway cheaper than hiring a designer($500+) butsustainable enoughto keep building features you'll actually use.

## Lessons Learned Building This 📚

### 💡 Lesson 1: AI Is Great at Marketing Copy (If You Prompt Right)

Early versions generated generic, buzzword-filled copy that sounded like every other app.

The breakthrough?Feeding the AI actual screenshot images + app context. Now it writes copy that describes what your appactually does.

### 🎯 Lesson 2: Developers Want Control, Not Full Automation

I initially built this as "one-click, no editing."Users hated it.

Turns out, developers want AI to do 80% of the work but keep control over the final 20%. That's why the visual canvas editor exists—complete with zoom/pan, keyboard shortcuts, and undo/redo.

### 🌍 Lesson 3: Multi-Language Is Harder Than It Seems

Supporting 6+ languages meant solving:

* ✅ UI translation
* ✅ AI prompts in each language
* ✅ Font support for special characters
* ✅ Character limit validation per locale

Was it worth it?Absolutely. International markets are huge for mobile apps.

## What's Coming Next 🔮

Currently shipping:

* 🌐 In-project language switching
* 🤖 Android screenshot templates
* 🎨 Premium theme collections
* 👥 Team collaboration features
* ...and more based on your feedback!

## Ready to Try It? 🎯

I built Lemmi Studio for developers like me who can ship code but struggle with marketing.

If you've ever procrastinated on launching because you dreaded making screenshots, this is for you.

### Start Free Today 🚀

* ✅ Free tier with 3 projects
* ✅ No credit card required
* ✅ Ready in 2 minutes

Try Lemmi Studio →

## Let's Build Together 🤝

This is sort of MVP v1. I'm shipping fast and iterating based on real feedback.

What would make this more useful for your launches?

Reach out:

## - 🐦 X:@mateusz_b9

## The Bottom Line 🎬

Built by developers, for developers.

Ship faster. Skip the designer. Launch today.

Try Lemmi Studio Free →

Cheers!

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse

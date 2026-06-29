---
title: Using Opus 4.8 to get a second opinion on an MRI and where it leaves me
url: https://antoine.fi/mri-analysis-using-claude-code-opus
date: 2026-06-29
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-06-29T19:25:13.905945
---

# Using Opus 4.8 to get a second opinion on an MRI and where it leaves me

# Summary of “Using Opus 4.8 to get a second opinion on an MRI and where it leaves me”

## Context
- Experienced right‑shoulder pain for 2–3 weeks and consulted an orthopedist.  
- MRI was ordered; the radiology report described a **Grade III (>50 % width) partial‑thickness tear** at the apical insertion of the subscapularis tendon.  
- The clinic immediately began an aggressive treatment plan, including shockwave therapy (despite guidelines advising against it for non‑calcific rotator‑cuff tendinopathy) and a Traumeel injection (a homeopathic product without a therapeutic indication in Germany).  
- The author, not a medical professional, felt uneasy and obtained the full MRI DICOM files and the clinic’s treatment list.

## Setting Up Opus 4.8
- Used Opus 4.8 (xhigh) within Claude Code to enable code execution and package installation.  
- Provided minimal clinical input (“right shoulder pain for 2–3 weeks”).  
- After about an hour, Opus generated a PDF report that **identified the subscapularis tendon as intact**, contradicting the clinic’s diagnosis of a Grade III tear.

## Arbitration Between Reports
- Fed both the human radiology report and the Opus report, along with a prior ChatGPT‑5.5 discussion about movement tests, to Claude for a comparative analysis.  
- Claude employed multiple sub‑agents to avoid bias and produced an arbitration PDF.  
- Verdict (moderate‑to‑high confidence): **Mild insertional tendinosis, no discrete partial‑ or full‑thickness tear** at the apical insertion.  
- The arbitration noted unresolved disputes but was decisive on the tear question.

## Personal Reflection
- The stark contrast between the clinician’s aggressive plan and the AI‑derived “no tear” conclusion created a sense of limbo.  
- The author appreciates the reassurance of a trusted human expert but is unsettled by AI’s ability to challenge that trust.  
- Uncertainty remains about whether to seek another doctor’s opinion, continue current rehabilitation, or wait for the shoulder to improve.

## Outlook
- Hopes that future AI model generations will be trusted for MRI interpretation as reliably as they are for tasks like email proofreading.  
- Emphasizes that the post is a technical curiosity, not medical advice, and does not name the clinic or physician.
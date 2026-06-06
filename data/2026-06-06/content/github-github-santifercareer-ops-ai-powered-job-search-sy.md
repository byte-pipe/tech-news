---
title: 'GitHub - santifer/career-ops: AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing. · GitHub'
url: https://github.com/santifer/career-ops
site_name: github
content_file: github-github-santifercareer-ops-ai-powered-job-search-sy
fetched_at: '2026-06-06T19:33:11.367298'
original_url: https://github.com/santifer/career-ops
author: santifer
description: AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing. - santifer/career-ops
---

santifer

 

/

career-ops

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork10.2k
* Star49.2k

 
 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

221 Commits
221 Commits
.agents/
skills/
career-ops
.agents/
skills/
career-ops
 
 
.claude-plugin
.claude-plugin
 
 
.claude/
skills/
career-ops
.claude/
skills/
career-ops
 
 
.github
.github
 
 
.qwen/
skills/
career-ops
.qwen/
skills/
career-ops
 
 
batch
batch
 
 
config
config
 
 
dashboard
dashboard
 
 
data
data
 
 
docs
docs
 
 
examples
examples
 
 
fonts
fonts
 
 
interview-prep
interview-prep
 
 
jds
jds
 
 
modes
modes
 
 
output
output
 
 
providers
providers
 
 
reports
reports
 
 
templates
templates
 
 
writing-samples
writing-samples
 
 
.coderabbit.yaml
.coderabbit.yaml
 
 
.env.example
.env.example
 
 
.envrc
.envrc
 
 
.gitignore
.gitignore
 
 
.release-please-manifest.json
.release-please-manifest.json
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CITATION.cff
CITATION.cff
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
CONTRIBUTORS.md
CONTRIBUTORS.md
 
 
DATA_CONTRACT.md
DATA_CONTRACT.md
 
 
GEMINI.md
GEMINI.md
 
 
GOVERNANCE.md
GOVERNANCE.md
 
 
LEGAL_DISCLAIMER.md
LEGAL_DISCLAIMER.md
 
 
LICENSE
LICENSE
 
 
README.cn.md
README.cn.md
 
 
README.es.md
README.es.md
 
 
README.ja.md
README.ja.md
 
 
README.ko-KR.md
README.ko-KR.md
 
 
README.md
README.md
 
 
README.pt-BR.md
README.pt-BR.md
 
 
README.ru.md
README.ru.md
 
 
README.ua.md
README.ua.md
 
 
README.zh-TW.md
README.zh-TW.md
 
 
SECURITY.md
SECURITY.md
 
 
SUPPORT.md
SUPPORT.md
 
 
TRADEMARK.md
TRADEMARK.md
 
 
VERSION
VERSION
 
 
analyze-patterns.mjs
analyze-patterns.mjs
 
 
check-liveness.mjs
check-liveness.mjs
 
 
cv-sync-check.mjs
cv-sync-check.mjs
 
 
dedup-tracker.mjs
dedup-tracker.mjs
 
 
doctor.mjs
doctor.mjs
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
followup-cadence.mjs
followup-cadence.mjs
 
 
gemini-eval.mjs
gemini-eval.mjs
 
 
generate-latex.mjs
generate-latex.mjs
 
 
generate-pdf.mjs
generate-pdf.mjs
 
 
liveness-browser.mjs
liveness-browser.mjs
 
 
liveness-core.mjs
liveness-core.mjs
 
 
merge-tracker.mjs
merge-tracker.mjs
 
 
normalize-statuses.mjs
normalize-statuses.mjs
 
 
package.json
package.json
 
 
release-please-config.json
release-please-config.json
 
 
renovate.json
renovate.json
 
 
scan.mjs
scan.mjs
 
 
test-all.mjs
test-all.mjs
 
 
tracker-links.mjs
tracker-links.mjs
 
 
update-system.mjs
update-system.mjs
 
 
verify-pipeline.mjs
verify-pipeline.mjs
 
 
View all files

## Repository files navigation

# Career-Ops

English|Español|Português (Brasil)|한국어|日本語|Українська|Русский|繁體中文

I spent months applying to jobs the hard way. So I engineered the system I wish I had.Companies use AI to filter candidates.I just gave candidates AI tochoosecompanies.Now it's open source.

740+ job listings evaluated · 100+ personalized CVs · 1 dream role landed

## What Is This

Career-Ops (career-ops.org, also known ascareerops) turns any AI coding CLI into a full job search command center. Instead of manually tracking applications in a spreadsheet, you get an AI-powered pipeline that:

* Evaluates offerswith a structured A-F scoring system (10 weighted dimensions)
* Generates tailored PDFs-- ATS-optimized CVs customized per job description
* Scans portalsautomatically (Greenhouse, Ashby, Lever, company pages)
* Processes in batch-- evaluate 10+ offers in parallel with sub-agents
* Tracks everythingin a single source of truth with integrity checks

Important: This is NOT a spray-and-pray tool.Career-ops is a filter -- it helps you find the few offers worth your time out of hundreds. The system strongly recommends against applying to anything scoring below 4.0/5. Your time is valuable, and so is the recruiter's. Always review before submitting.

Career-ops is agentic: Claude Code navigates career pages with Playwright, evaluates fit by reasoning about your CV vs the job description (not keyword matching), and adapts your resume per listing.

Heads up: the first evaluations won't be great.The system doesn't know you yet. Feed it context -- your CV, your career story, your proof points, your preferences, what you're good at, what you want to avoid. The more you nurture it, the better it gets. Think of it as onboarding a new recruiter: the first week they need to learn about you, then they become invaluable.

Built by someone who used it to evaluate 740+ job offers, generate 100+ tailored CVs, and land a Head of Applied AI role.Read the full case study.

## Features

Feature

Description

Auto-Pipeline

Paste a URL, get a full evaluation + PDF + tracker entry

6-Block Evaluation

Role summary, CV match, level strategy, comp research, personalization, interview prep (STAR+R)

Interview Story Bank

Accumulates STAR+Reflection stories across evaluations -- 5-10 master stories that answer any behavioral question

Negotiation Scripts

Salary negotiation frameworks, geographic discount pushback, competing offer leverage

ATS PDF Generation

Keyword-injected CVs with Space Grotesk + DM Sans design

Portal Scanner

45+ companies pre-configured (Anthropic, OpenAI, ElevenLabs, Retool, n8n...) + custom queries across Ashby, Greenhouse, Lever, Wellfound

Batch Processing

Parallel evaluation with 
claude -p
 workers

Dashboard TUI

Terminal UI to browse, filter, and sort your pipeline

Human-in-the-Loop

AI evaluates and recommends, you decide and act. The system never submits an application -- you always have the final call

Pipeline Integrity

Automated merge, dedup, status normalization, health checks

## Quick Start

#
 1. Clone and install

git clone https://github.com/santifer/career-ops.git

cd
 career-ops 
&&
 npm install
npx playwright install chromium 
#
 Required for PDF generation

#
 2. Check setup

npm run doctor 
#
 Validates all prerequisites

#
 3. Configure

cp config/profile.example.yml config/profile.yml 
#
 Edit with your details

cp templates/portals.example.yml portals.yml 
#
 Customize companies

#
 4. Add your CV

#
 Create cv.md in the project root with your CV in markdown

#
 5. Personalize with Claude

claude 
#
 Open Claude Code in this directory

#
 Then ask Claude to adapt the system to you:

#
 "Change the archetypes to backend engineering roles"

#
 "Translate the modes to English"

#
 "Add these 5 companies to portals.yml"

#
 "Update my profile with this CV I'm pasting"

#
 6. Start using

#
 Paste a job URL or run /career-ops

The system is designed to be customized by Claude itself.Modes, archetypes, scoring weights, negotiation scripts -- just ask Claude to change them. It reads the same files it uses, so it knows exactly what to edit.

Seedocs/SETUP.mdfor the full setup guide.

## Gemini CLI Integration

Career-ops supportsGemini CLInatively — the same way it supports Claude Code and OpenCode. All 15 slash commands are available, using the samemodes/*.mdevaluation logic.

### Option A — Native Gemini CLI (Recommended)

#
 1. Install Gemini CLI

npm install -g @google/gemini-cli

#
 or: npx @google/gemini-cli --version

#
 2. Authenticate (free — uses your Google account)

gemini auth

#
 3. Run in the career-ops directory

cd
 career-ops
gemini

#
 4. Use slash commands just like Claude Code

/career-ops 
"
Senior AI Engineer at Anthropic...
"

/career-ops-evaluate --file ./jds/openai.txt
/career-ops-scan
/career-ops-pdf
/career-ops-tracker

TheGEMINI.mdfile is auto-loaded as context. All 15 commands are defined in.gemini/commands/*.toml.

### Option B — Standalone API Script (No CLI install needed)

#
 1. Get a free API key at https://aistudio.google.com/apikey

cp .env.example .env

#
 Edit .env → set GEMINI_API_KEY=your_key_here

#
 2. Install dependencies

npm install

#
 3. Evaluate a job description

node gemini-eval.mjs 
"
We are looking for a Senior AI Engineer...
"

node gemini-eval.mjs --file ./jds/my-job.txt
npm run gemini:eval -- 
"
JD text here
"

Free tier:Both options work without billing. Native CLI uses Google OAuth; the API script usesgemini-2.5-flash(15 RPM, 1M tokens/day free).

## Usage

Career-ops is a single slash command with multiple modes:

/career-ops → Show all available commands
/career-ops {paste a JD} → Full auto-pipeline (evaluate + PDF + tracker)
/career-ops scan → Scan portals for new offers
/career-ops pdf → Generate ATS-optimized CV
/career-ops batch → Batch evaluate multiple offers
/career-ops tracker → View application status
/career-ops apply → Fill application forms with AI
/career-ops pipeline → Process pending URLs
/career-ops contacto → LinkedIn outreach message
/career-ops deep → Deep company research
/career-ops training → Evaluate a course/cert
/career-ops project → Evaluate a portfolio project

Or just paste a job URL or description directly -- career-ops auto-detects it and runs the full pipeline.

## How It Works

You paste a job URL or description
 │
 ▼
┌──────────────────┐
│ Archetype │ Classifies: LLMOps / Agentic / PM / SA / FDE / Transformation
│ Detection │
└────────┬─────────┘
 │
┌────────▼─────────┐
│ A-F Evaluation │ Match, gaps, comp research, STAR stories
│ (reads cv.md) │
└────────┬─────────┘
 │
 ┌────┼────┐
 ▼ ▼ ▼
 Report PDF Tracker
 .md .pdf .tsv

## Pre-configured Portals

The scanner comes with45+ companiesready to scan and19 search queriesacross major job boards. Copytemplates/portals.example.ymltoportals.ymland add your own:

AI Labs:Anthropic, OpenAI, Mistral, Cohere, LangChain, PineconeVoice AI:ElevenLabs, PolyAI, Parloa, Hume AI, Deepgram, Vapi, Bland AIAI Platforms:Retool, Airtable, Vercel, Temporal, Glean, Arize AIContact Center:Ada, LivePerson, Sierra, Decagon, Talkdesk, GenesysEnterprise:Salesforce, Twilio, Gong, DialpadLLMOps:Langfuse, Weights & Biases, Lindy, Cognigy, SpeechmaticsAutomation:n8n, Zapier, Make.comEuropean:Factorial, Attio, Tinybird, Clarity AI, Travelperk

Job boards searched:Ashby, Greenhouse, Lever, Wellfound, Workable, RemoteFront

By defaultnode scan.mjs(a.k.a.npm run scan) trusts what each ATS feed returns. Some companies leave stale postings in their public API even after the role is closed, so those expired entries can leak intopipeline.md. Pass--verifyto launch Playwright after the API pass and drop expired postings before they hit the pipeline:

node scan.mjs --verify 
#
 zero-token discovery + Playwright liveness check

The verification is sequential and only runs against new offers (after dedup), so the cost stays bounded.

## Dashboard TUI

The built-in terminal dashboard lets you browse your pipeline visually:

cd
 dashboard
go build -o career-dashboard 
.

./career-dashboard --path ..

Features: 6 filter tabs, 4 sort modes, grouped/flat view, lazy-loaded previews, inline status changes.

## Project Structure

career-ops/
├── AGENTS.md # Canonical agent instructions (all CLIs)
├── CLAUDE.md # Claude Code wrapper (imports AGENTS.md)
├── cv.md # Your CV (create this)
├── article-digest.md # Your proof points (optional)
├── config/
│ └── profile.example.yml # Template for your profile
├── modes/ # 14 skill modes
│ ├── _shared.md # Shared context (customize this)
│ ├── oferta.md # Single evaluation
│ ├── pdf.md # PDF generation
│ ├── scan.md # Portal scanner
│ ├── batch.md # Batch processing
│ └── ...
├── templates/
│ ├── cv-template.html # ATS-optimized CV template
│ ├── portals.example.yml # Scanner config template
│ └── states.yml # Canonical statuses
├── batch/
│ ├── batch-prompt.md # Self-contained worker prompt
│ └── batch-runner.sh # Orchestrator script
├── dashboard/ # Go TUI pipeline viewer
├── data/ # Your tracking data (gitignored)
├── reports/ # Evaluation reports (gitignored)
├── output/ # Generated PDFs (gitignored)
├── fonts/ # Space Grotesk + DM Sans
├── docs/ # Setup, customization, architecture
└── examples/ # Sample CV, report, proof points

## Tech Stack

* Agent: Claude Code with custom skills and modes
* PDF: Playwright/Puppeteer + HTML template
* Scanner: Playwright + Greenhouse API + WebSearch
* Dashboard: Go + Bubble Tea + Lipgloss (Catppuccin Mocha theme)
* Data: Markdown tables + YAML config + TSV batch files

## Also Open Source

* cv-santiago-- The portfolio website (santifer.io) with AI chatbot, LLMOps dashboard, and case studies. If you need a portfolio to showcase alongside your job search, fork it and make it yours.

## About the Author

I'm Santiago -- Head of Applied AI, former founder (built and sold a business that still runs with my name on it). I built career-ops to manage my own job search. It worked: I used it to land my current role.

My portfolio and other open source projects →santifer.io

## Star History

## Disclaimer

career-ops is a local, open-source tool — NOT a hosted service.By using this software, you acknowledge:

1. You control your data.Your CV, contact info, and personal data stay on your machine and are sent directly to the AI provider you choose (Anthropic, OpenAI, etc.). We do not collect, store, or have access to any of your data.
2. You control the AI.The default prompts instruct the AI not to auto-submit applications, but AI models can behave unpredictably. If you modify the prompts or use different models, you do so at your own risk.Always review AI-generated content for accuracy before submitting.
3. You comply with third-party ToS.You must use this tool in accordance with the Terms of Service of the career portals you interact with (Greenhouse, Lever, Workday, LinkedIn, etc.). Do not use this tool to spam employers or overwhelm ATS systems.
4. No guarantees.Evaluations are recommendations, not truth. AI models may hallucinate skills or experience. The authors are not liable for employment outcomes, rejected applications, account restrictions, or any other consequences.

SeeLEGAL_DISCLAIMER.mdfor full details. This software is provided under theMIT License"as is", without warranty of any kind.

## Contributors

Got hired using career-ops?Share your story!

## License & Trademark

The code is licensed underMIT. The "career-ops" name and
brand are governed by theTrademark Policy— permissive
for community use, reserved for commercial product naming and
endorsement.

## Let's Connect

## About

AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, batch processing.

career-ops.org

### Topics

 resume

 cli

 golang

 open-source

 automation

 career

 interview-prep

 job-search

 claude

 ai-agent

 anthropic

 claude-code

 careerops

### Resources

 Readme

 

### License

 MIT license
 

### Code of conduct

 Code of conduct
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

49.2k

 stars
 

### Watchers

207

 watching
 

### Forks

10.2k

 forks
 

 Report repository

 

## Releases8

career-ops: v1.8.0

 Latest

 

May 15, 2026

 

+ 7 releases

## Sponsor this project

 

 

 Sponsor

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

Learn more about GitHub Sponsors

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* JavaScript62.7%
* Go28.9%
* Shell4.8%
* HTML2.3%
* Other1.3%
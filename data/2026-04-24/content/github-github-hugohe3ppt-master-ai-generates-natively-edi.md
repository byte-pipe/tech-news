---
title: 'GitHub - hugohe3/ppt-master: AI generates natively editable PPTX from any document — real PowerPoint shapes, not images — no design skills needed · GitHub'
url: https://github.com/hugohe3/ppt-master
site_name: github
content_file: github-github-hugohe3ppt-master-ai-generates-natively-edi
fetched_at: '2026-04-24T06:00:18.792678'
original_url: https://github.com/hugohe3/ppt-master
author: hugohe3
description: AI generates natively editable PPTX from any document — real PowerPoint shapes, not images — no design skills needed - hugohe3/ppt-master
---

hugohe3

 

/

ppt-master

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork835
* Star7.5k

 
 
 
 
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

330 Commits
330 Commits
.github
.github
 
 
docs
docs
 
 
examples
examples
 
 
projects
projects
 
 
skills/
ppt-master
skills/
ppt-master
 
 
.env.example
.env.example
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
README_CN.md
README_CN.md
 
 
SECURITY.md
SECURITY.md
 
 
index.html
index.html
 
 
requirements.txt
requirements.txt
 
 
viewer.html
viewer.html
 
 
View all files

## Repository files navigation

# PPT Master — AI generates natively editable PPTX from any document

English |中文

Live Demo·About Hugo He·Examples·FAQ·Contact

Official channels —this project is publishedonlyonGitHub(primary) andAtomGit(auto-synced mirror). Redistributions on any other platform are unofficial and not maintained by the author. Licensed under MIT — attribution required.

↑ A 12-page natively editable deck, generated end-to-end froma single WeChat article URLusing Claude Opus 4.7. No manual design. No image export. Every shape, text box, and chart is clickable and editable in PowerPoint.

🛡️ New:10-page dark-tech deckgenerated fromAnthropic's Claude Code Auto Mode engineering blog— see it in theexamples.

Drop in a PDF, DOCX, URL, or Markdown — get back anatively editable PowerPointwith real shapes, real text boxes, and real charts. Not images. Click anything and edit it.

How it works— PPT Master is a workflow (a "skill") that works inside AI IDEs like Claude Code, Cursor, VS Code + Copilot, or Codebuddy. You chat with the AI — "make a deck from this PDF" — and it follows the workflow to produce a real editable.pptxon your computer. No coding on your side; the IDE is just where the conversation happens.

What you'll do: install Python, install an AI IDE, drop in your material. First-time setup is about 15 minutes. Each deck takes ~10–20 minutes of back-and-forth with the AI.

Why PPT Master?

There's no shortage of AI presentation tools — what's missing is one where the output isactually usable as a real PowerPoint file. I build presentations every day, but most tools export images or web screenshots: they look nice but you can't edit anything. Others produce bare-bones text boxes and bullet lists. And they all want a monthly subscription, upload your files to their servers, and lock you into their platform.

PPT Master is different:

* Real PowerPoint— if a file can't be opened and edited in PowerPoint, it shouldn't be called a PPT. Every element PPT Master outputs is directly clickable and editable
* Transparent, predictable cost— the tool is free and open source; the only cost is your own AI editor, and you know exactly what you're paying. As low as$0.08/deckwith VS Code Copilot
* Data stays local— your files shouldn't have to be uploaded to someone else's server just to make a presentation. Apart from AI model communication, the entire pipeline runs on your machine
* No platform lock-in— your workflow shouldn't be held hostage by any single company. Works with Claude Code, Cursor, VS Code Copilot, and more; supports Claude, GPT, Gemini, Kimi, and other models

See live examples →·examples/— 15 projects, 229 pages

## Gallery

Magazine
 — warm earthy tones, photo-rich layout

Academic
 — structured research format, data-driven

Dark Art
 — cinematic dark background, gallery aesthetic

Nature Documentary
 — immersive photography, minimal UI

Tech / SaaS
 — clean white cards, pricing table layout

Product Launch
 — high contrast, bold specs highlight

## Built by Hugo He

I'm a finance professional (CPA · CPV · Consulting Engineer (Investment)) who got tired of spending hours on presentations that could be automated. So I built this.

PPT Master started from a simple frustration: existing AI slide tools export images, not editable shapes. As someone who reviews and edits hundreds of slides in investment and consulting work, that was unacceptable. I wanted real DrawingML — click on any element and change it, just like you built it by hand.

This project is my attempt to bridge the gap betweendomain expertiseandproduct engineering— turning a complex professional pain point into an open-source tool that anyone can use.

🌐Personal website· 📧heyug3@gmail.com· 🐙@hugohe3

## Support This Project

PPT Master is built and maintained by one person, fully self-funded. Every new template, bug fix, and documentation update runs through AI models that cost real money — and right now those token bills come out of my own pocket.

If PPT Master has been helpful to you, consider chipping in. Sponsorship directly funds more templates, faster fixes, and keeps this project free and open-source.

Individual sponsorship

Any amount is appreciated.

Enterprise / Custom work

Need a custom industry template, private deployment, or integration consulting? I take on a limited number of paid engagements each quarter.

📧heyug3@gmail.com

## Quick Start

### 1. Prerequisites

You only need Python.Everything else is installed viapip install -r requirements.txt.

Dependency

Required?

What it does

Python
 3.10+

✅ 
Yes

Core runtime — the only thing you actually need to install

TL;DR— Install Python, runpip install -r requirements.txt, and you're ready to generate presentations.

Windows
 — see the dedicated step-by-step guide 
⚠️

Windows requires a few extra steps (PATH setup, execution policy, etc.). We wrote astep-by-step guidespecifically for Windows users:

📖Windows Installation Guide— from zero to a working presentation in 10 minutes.

Quick version: download Python frompython.org→check "Add to PATH"during install →pip install -r requirements.txt→ done.

macOS / Linux
 — install and go

#
 macOS

brew install python
pip install -r requirements.txt

#
 Ubuntu / Debian

sudo apt install python3 python3-pip
pip install -r requirements.txt

Edge-case fallbacks
 — 99% of users don't need these

Two external tools exist as fallbacks for edge cases.Most users will never need them— install only if you hit one of the specific scenarios below.

Fallback

Install only if…

Node.js
 18+

You need to import WeChat Official Account articles 
and
 
curl_cffi
 (part of 
requirements.txt
) has no prebuilt wheel for your Python + OS + CPU combination. In normal setups 
web_to_md.py
 handles WeChat directly through 
curl_cffi
.

Pandoc

You need to convert legacy formats: 
.doc
, 
.odt
, 
.rtf
, 
.tex
, 
.rst
, 
.org
, or 
.typ
. 
.docx
, 
.html
, 
.epub
, 
.ipynb
 are handled natively by Python — no pandoc required.

#
 macOS (only if the above conditions apply)

brew install node
brew install pandoc

#
 Ubuntu / Debian

sudo apt install nodejs npm
sudo apt install pandoc

### 2. Pick an AI Editor

Tool

Rating

Notes

Claude Code

⭐⭐⭐

Best results — native Opus, largest context

Cursor
 / 
VS Code + Copilot

⭐⭐

Good alternatives

Codebuddy IDE

⭐⭐

Best for Chinese models (Kimi 2.5, MiniMax-M2.7)

### 3. Set Up

Option A — Download ZIP(no Git required): clickCode → Download ZIPon theGitHub page, then unzip.

Option B — Git clone(requiresGitinstalled):

git clone https://github.com/hugohe3/ppt-master.git

cd
 ppt-master

Then install dependencies:

pip install -r requirements.txt

To update later (Option B only):python3 skills/ppt-master/scripts/update_repo.py

### 4. Create

Provide source materials (recommended):Place your PDF, DOCX, images, or other files in theprojects/directory, then tell the AI chat panel which files to use. The quickest way to get the path: right-click the file in your file manager or IDE sidebar →Copy Path(orCopy Relative Path) and paste it directly into the chat.

You: Please create a PPT from projects/q3-report/sources/report.pdf

Paste content directly:You can also paste text content straight into the chat window and the AI will generate a PPT from it.

You: Please turn the following into a PPT: [paste your content here...]

Either way, the AI will first confirm the design spec:

AI: Sure. Let's confirm the design spec:
 [Template] B) Free design
 [Format] PPT 16:9
 [Pages] 8-10 pages
 ...

The AI handles everything — content analysis, visual design, SVG generation, and PPTX export.

Output:Two timestamped files are saved toexports/— a native-shapes.pptx(directly editable) and an_svg.pptxsnapshot for visual reference. Requires Office 2016+.

AI lost context?Ask it to readskills/ppt-master/SKILL.md.

Something went wrong?Check theFAQ— it covers model selection, layout issues, export problems, and more. Continuously updated from real user reports.

### 5. AI Image Generation (Optional)

cp .env.example .env 
#
 then edit with your API key

IMAGE_BACKEND
=
gemini
 
#
 required — must be set explicitly

GEMINI_API_KEY
=
your-api-key

GEMINI_MODEL
=
gemini-3.1-flash-image-preview

Multiple backends are supported across Core / Extended / Experimental tiers. Runpython3 skills/ppt-master/scripts/image_gen.py --list-backendsto see the full list. Environment variables override.env. Use provider-specific keys (GEMINI_API_KEY,OPENAI_API_KEY, etc.) — globalIMAGE_API_KEYis not supported.

Tip:For best quality, generate images inGeminiand selectDownload full size. Remove the watermark withscripts/gemini_watermark_remover.py.

## Documentation

Document

Description

🆚

Why PPT Master

How it compares to Gamma, Copilot, and other AI tools

🪟

Windows Installation

Step-by-step setup guide for Windows users

📖

SKILL.md

Core workflow and rules

📐

Canvas Formats

PPT 16:9, Xiaohongshu, WeChat, and 10+ formats

🛠️

Scripts & Tools

All scripts and commands

💼

Examples

15 projects, 229 pages

🏗️

Technical Design

Architecture, design philosophy, why SVG

❓

FAQ

Model selection, cost, layout troubleshooting, custom templates

## Contributing

SeeCONTRIBUTING.mdfor how to get involved.

## License

MIT

## Acknowledgments

SVG Repo·Tabler Icons·Robin Williams(CRAP principles) · McKinsey, BCG, Bain

## Contact & Collaboration

Looking to collaborate, integrate PPT Master into your workflow, or just have questions?

* 💬Questions & sharing—GitHub Discussions
* 🐛Bug reports & feature requests—GitHub Issues
* 🌐Learn more about the author—www.hehugo.com

For enterprise / consulting / custom-template work, see theSupport This Projectsection above.

## Star History

## Supported by DigitalOcean

This project is supported by:

Made with ❤️ byHugo He— if this project helps you, please give it a ⭐ and considersponsoring.

⬆ Back to Top

## About

AI generates natively editable PPTX from any document — real PowerPoint shapes, not images — no design skills needed

hugohe3.github.io/ppt-master/

### Topics

 svg

 slide

 presentation

 slides

 office

 powerpoint

 pptx

 ppt

 powerpoint-generation

 ai-agent

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

7.5k

 stars
 

### Watchers

28

 watching
 

### Forks

835

 forks
 

 Report repository

 

## Releases1

v2.3.0

 Latest

 

Apr 12, 2026

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
* https://paypal.me/hugohe3

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python86.3%
* HTML10.4%
* JavaScript3.3%
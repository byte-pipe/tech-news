---
title: OpenAI are quietly adopting skills, now available in ChatGPT and Codex CLI
url: https://simonwillison.net/2025/Dec/12/openai-skills/
site_name: hackernews_api
fetched_at: '2025-12-13T19:06:21.956080'
original_url: https://simonwillison.net/2025/Dec/12/openai-skills/
author: Simon Willison
date: '2025-12-12'
description: OpenAI are quietly adopting skills, now available in ChatGPT and Codex CLI
tags:
- hackernews
- trending
---

# Simon Willison’s Weblog

Subscribe

## OpenAI are quietly adopting skills, now available in ChatGPT and Codex CLI

12th December 2025

One of the things that most excited me aboutAnthropic’s new Skills mechanismback in October is how easy it looked for other platforms to implement. A skill is just a folder with a Markdown file and some optional extra resources and scripts, so any LLM tool with the ability to navigate and read from a filesystem should be capable of using them. It turns out OpenAI are doing exactly that, with skills support quietly showing up in both their Codex CLI tool and now also in ChatGPT itself.

#### Skills in ChatGPT

I learned about thisfrom Elias Judinthis morning. It turns out the Code Interpreter feature of ChatGPT now has a new/home/oai/skillsfolder which you can access simply by prompting:

Create a zip file of /home/oai/skills

Itried that myselfand got backthis zip file. Here’sa UI for exploring its content(more about that tool).

So far they cover spreadsheets, docx and PDFs. Interestingly their chosen approach for PDFs and documents is to convert them to rendered per-page PNGs and then pass those through their vision-enabled GPT models, presumably to maintain information from layout and graphics that would be lost if they just ran text extraction.

Eliasshared copies in a GitHub repo. They look very similar to Anthropic’s implementation of the same kind of idea, currently published in theiranthropics/skillsrepository.

I tried it out by prompting:

Create a PDF with a summary of the rimu tree situation right now and what it means for kakapo breeding season

Sure enough, GPT-5.2 Thinking started with:

Reading skill.md for PDF creation guidelines

Then:

Searching rimu mast and Kākāpō 2025 breeding status

It tookjust over eleven minutesto producethis PDF, which was long enough that I had Claude Code for webbuild me a custom PDF viewing toolwhile I waited.

Here’s ChatGPT’s PDF in that tool.

(I amvery excitedaboutKākāpō breeding season this year.)

The reason it took so long is that it was fastidious about looking at and tweaking its own work. I appreciated that at one point it tried rendering the PDF and noticed that the macrons in kākāpō were not supported by the chosen font, so it switched to something else:

#### Skills in Codex CLI

Meanwhile, two weeks ago OpenAI’s open source Codex CLI tool landed a PR titledfeat: experimental support for skills.md. The most recent docs for that are indocs/skills.md.

The documentation suggests that any folder in~/.codex/skillswill be treated as a skill.

I dug around and found the code that generates the prompt that drives the skill system incodex-rs/core/src/skills/render.rs—here’s a Gist witha more readable version of that prompt.

Iused Claude Opus 4.5’s skill authoring skillto createthis skill for creating Datasette plugins, then installed it into my Codex CLI skills folder like this:

git clone https://github.com/datasette/skill \

~
/.codex/skills/datasette-plugin

You have to run Codex with the--enable skillsoption. I ran this:

cd
 /tmp
mkdir datasette-cowsay

cd
 datasette-cowsay
codex --enable skills -m gpt-5.2

Then prompted:

list skills

And Codex replied:

- datasette-plugins — Writing Datasette plugins using Python + pluggy (file: /Users/simon/.codex/skills/datasette-plugin/SKILL.md)- Discovery — How to find/identify available skills (no SKILL.md path provided in the list)

Then I said:

Write a Datasette plugin in this folder adding a /-/cowsay?text=hello page that displays a pre with cowsay from PyPI saying that text

It worked perfectly! Here’sthe plugin code it wroteand here’sa copy of the full Codex CLI transcript, generated with myterminal-to-html tool.

You can try that out yourself if you haveuvxinstalled like this:

uvx --with https://github.com/simonw/datasette-cowsay/archive/refs/heads/main.zip \
 datasette

Then visit:

http://127.0.0.1:8001/-/cowsay?text=This+is+pretty+fun

#### Skills are a keeper

When I first wrote about skills in October I saidClaude Skills are awesome, maybe a bigger deal than MCP. The fact that it’s just turned December and OpenAI have already leaned into them in a big way reinforces to me that I called that one correctly.

Skills are based on averylight specification, if you could even call it that, but I still think it would be good for these to be formally documented somewhere. This could be a good initiative for the newAgentic AI Foundation(previously) to take on.

Posted
12th December 2025
 at 11:29 pm · Follow me on
Mastodon
,
Bluesky
,
Twitter
 or
subscribe to my newsletter

## More recent articles

* GPT-5.2- 11th December 2025
* Useful patterns for building HTML tools- 10th December 2025



This isOpenAI are quietly adopting skills, now available in ChatGPT and Codex CLIby Simon Willison, posted on12th December 2025.

 pdf

39

 ai

1732

 kakapo

2

 openai

374

 prompt-engineering

175

 generative-ai

1530

 chatgpt

188

 llms

1496

 ai-assisted-programming

286

 anthropic

211

 coding-agents

110

 gpt-5

28

 codex-cli

18

 skills

7

Previous:GPT-5.2

### Monthly briefing

Sponsor me for$10/monthand get a curated email digest of the month's most important LLM developments.

Pay me to send you less!

 Sponsor & subscribe






* Colophon
* ©
* 2002
* 2003
* 2004
* 2005
* 2006
* 2007
* 2008
* 2009
* 2010
* 2011
* 2012
* 2013
* 2014
* 2015
* 2016
* 2017
* 2018
* 2019
* 2020
* 2021
* 2022
* 2023
* 2024
* 2025

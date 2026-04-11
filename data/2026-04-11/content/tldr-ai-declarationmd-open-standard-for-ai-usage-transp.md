---
title: AI-DECLARATION.md | Open Standard for AI Usage Transparency
url: https://ai-declaration.md/
site_name: tldr
content_file: tldr-ai-declarationmd-open-standard-for-ai-usage-transp
fetched_at: '2026-04-11T11:12:54.426679'
original_url: https://ai-declaration.md/
date: '2026-04-11'
description: An open standard for declaring AI usage in software projects. Like a LICENSE or README, AI-DECLARATION.md makes AI involvement transparent and consistent.
tags:
- tldr
---

䷼

# AI-DECLARATION.md

Summary

·

Specification

·

Examples

·

Badges

·

FAQ

## Summary

AI-generated code is a reality of our time and it is both a blessing and a curse. The problem is not the code in itself but transparency and clarity. At least, that is the working theory of this specification. The suggestion is simple: to invite everyone to include a structuredAI-DECLARATION.mdfile like they include other files in a repository to make the AI-usage crystal clearand, more importantly, to make it a widespread convention to do so.

This is not to discourage usage of LLM- and other code-generation in the future. On the contrary, it is an enabler. When you declare what parts of the code were, in fact, generated, a skeptic can immediately look into just those parts to satisfy their urge to re-verify and double-check. And, it lets the creator showcase their skillset with code and their skillset with planning and other soft skills simultaneously and with clarity.

## Specification

AnAI-DECLARATION.mdfile uses YAML frontmatter for structured fields, followed by a required## Notessection in the markdown body for human context. At minimum, it requiresversion,level, and a## Notessection.

Optionally, you can declareprocesses, each with their own level. The globallevelmust be the highest level present. Any process not listed is assumed to benoneimplicitly. You can also listcomponents(file paths or directories) with individual levels.

The specification formally definesversion,level,processes, andcomponents.

#### Levels

* noneNo AI tools were used at any point.
* hintAI autocomplete or inline suggestions only. The human writes all code. AI occasionally completes a line or block.
* assistHuman-led. AI is used on demand for specific tasks (generating a function, explaining code, drafting a test) but does not drive the work.
* pairActive human-AI collaboration throughout. Contribution is roughly equal.
* copilotAI implements while the human plans and reviews. The human defines what to build and validates the output, but the AI does most of the writing.
* autoAI acts autonomously with minimal human direction. The human may steer at a high level or approve outcomes, but does not write or closely direct the code.

#### Processes

* designArchitecture, system design, and decision-making.
* implementationWriting production code.
* testingWriting tests, test plans, and quality assurance.
* documentationWriting docs, comments, READMEs, and changelogs.
* reviewCode review and pull request feedback.
* deploymentCI/CD configuration, infrastructure, and release scripts.

## Examples

Below, you will find some examples of different scenarios.

Simple

The simplestAI-DECLARATION.mdrequiresversion,level, and a## Notessection.

---
version: "0.1.1"
level: none
---

## Notes

- No AI tools were used.

---
version: "0.1.1"
level: auto
---

## Notes

- Claude Code was used to create the whole application.

With Processes

Useprocessesto granularly declare AI involvement per development phase. The globallevelmust be the highest level present. Any process not listed is assumed to benoneimplicitly.

---
version: "0.1.1"
level: auto
processes:
 design: auto
 testing: copilot
---

## Notes

- AI drove architecture decisions and test generation. All output was reviewed by a human.

With Components

Usecomponentsto declare AI involvement for specific files or directories.

---
version: "0.1.1"
level: auto
components:
 src/helpers: auto
---

## Notes

- The helpers directory was fully generated. All other code is human-written.

## Badges

Add a badge to yourREADMEto declare yourAI-DECLARATIONlevel at a glance. Please note, this is just for convenience and to comply with the specification, youmustinclude anAI-DECLARATION.mdfile.

* Copy
* Copy
* Copy
* Copy
* Copy
* Copy

## FAQ

What if I lie?

Well, that defeats the purpose entirely, doesn't it? The idea is for all of us to have a social contract that we can trust. If you see a repo with an 
AI-DECLARATION.md
 in it, you can use it as a single source of truth.

Can I build tooling to generate this automatically?

Be my guest. I envision tooling to build it automatically as well as parse it. While I will do it at some point, I appreciate any or all contributions.

Can I contribute a translation?

Absolutely! Please. Just fork the repository and add a 
README_<locale>.md
 e.g. 
README_es.md
. Then, raise a PR. I'll take it from there.

I want to suggest a change to the specification?

Well, good thing it is open-source then. I see the specification evolving naturally with feedback and PRs. So, let us all discuss.

Do I need to include the file if I added a badge to my README?

Yes, the recommendation is to include an 
AI-DECLARATION.md
 as the primary source of truth. The badge in the 
README
 is just a glanceable way for someone to check that A, the 
AI-DECLARATION.md
 would be available and B, the level.

What is the logo?

䷼ Hexagram 61 or Hexagram For Inner Truth (Unicode: 
U+4DFC
) is one of 64 hexagrams in the Yi (I) Ching to illustrate principles where each line is either Yin (broken) or Yang (solid). (
source
)
---
title: 'GitHub - devenjarvis/lathe: Generate hands-on, multi-part technical tutorials on demand, with LLM skills tuned to make content approachable. Then you work through them yourself, by hand ✋ · GitHub'
url: https://github.com/devenjarvis/lathe
site_name: hackernews_api
content_file: hackernews_api-github-devenjarvislathe-generate-hands-on-multi-pa
fetched_at: '2026-06-08T11:00:00.827076'
original_url: https://github.com/devenjarvis/lathe
author: devenjarvis
date: '2026-06-07'
description: Generate hands-on, multi-part technical tutorials on demand, with LLM skills tuned to make content approachable. Then you work through them yourself, by hand ✋ - devenjarvis/lathe
tags:
- hackernews
- trending
---

devenjarvis

 

/

lathe

Public

* NotificationsYou must be signed in to change notification settings
* Fork14
* Star503

 
 
 
 
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

123 Commits
123 Commits
.claude/
skills
.claude/
skills
 
 
.github/
workflows
.github/
workflows
 
 
cmd
cmd
 
 
docs
docs
 
 
internal
internal
 
 
.gitignore
.gitignore
 
 
.golangci.yml
.golangci.yml
 
 
.goreleaser.yaml
.goreleaser.yaml
 
 
CLAUDE.md
CLAUDE.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
install.sh
install.sh
 
 
magefile.go
magefile.go
 
 
main.go
main.go
 
 
View all files

## Repository files navigation

# Lathe

An experiment in using LLMs to teach you, rather than think for you.

Lathe generates hands-on, multi-part technical tutorials on demand, with skills tuned to make content approachable. Then you work through them yourself, by hand, in a local UI built from the ground up for pleasant learning. (Just like we did it in the stone age 😎)

## What is it?

* Generate hands-on technical tutorials (single-part or a multi-part series) from any prompt
* Work through the tutorial yourself in a purpose-built local UI
* Use skills to ask questions, verify the tutorial, and extend it with a new part
* Search, filter, and manage tutorials from your library
* Every tutorial documents its sources, which model was used, and what prompt drove the "voice" for the tutorial

## Quick start

Lathe is a combination of LLM skills and a Golang CLI used to store, manage, and view generated tutorials. After install (below), you can generate a tutorial inside any LLM session (Claude Code, Cursor, and Codex supported) by prompting something like:

/lathe build a 3D Slicer in Erlang

Then open lathe from any terminal:

lathe serve 
#
 starts the web server, opens the browser

Don't worry, we also have dark mode:

Click the tutorial you want to read and start learning!

The CLI has a bunch of other commands, but honestly those were built to give the LLM a deterministic way to manage tutorials. I expect the above to be all you need (it's all I ever use) for day-to-day. If you want to ask a question about a tutorial, have the LLM verify it, or extend it with an additional part, the UI has affordances for each of these which will give you the exact skill/prompt to give your LLM in order to trigger the action.

## Install

Lathe is a single self-contained binary. All you need islatheon your$PATH; the
skills run in an interactive Claude Code, Cursor, or Codex session.

Homebrew(macOS, recommended):

brew install devenjarvis/tap/lathe

Distributed as a cask (a pre-built binary), so it's macOS-only — on Linux use the
install script orgo installbelow.

Install script(curl | sh):

curl -sSf https://raw.githubusercontent.com/devenjarvis/lathe/main/install.sh 
|
 sh

Go(needs Go 1.25+):

go install github.com/devenjarvis/lathe@latest

From source:

git clone https://github.com/devenjarvis/lathe

cd
 lathe
go build -o lathe

### Install the skills

The skills are bundled into the binary. After installinglathe, drop them into a
project so Claude Code (or Cursor / Codex) can discover them:

lathe skills install 
#
 ./.claude/skills/<name>/SKILL.md (this project)

lathe skills install --user 
#
 ~/.claude/skills/<name>/SKILL.md (all projects)

lathe skills install --agent cursor 
#
 ./.cursor/commands/<slug>.md (Cursor slash commands)

lathe skills install --agent codex 
#
 ./.agents/skills/<name>/SKILL.md (Codex Agent Skills)

lathe skills install --agent all 
#
 Claude Code, Cursor, and Codex

lathe skills list 
#
 show the bundled skills

Codex uses the sameSKILL.mdformat as Claude Code, so its skills ship verbatim
(and--userinstalls to~/.agents/skills/...). Cursor commands are slash-invoked
as/<slug>(e.g./lathe); the interactive handoff model is documented for Claude
Code, so a few runtime details differ on Cursor and Codex.

## Why does this exist?

I learned how to program as a teen in the 2000s by building homebrew games for my PSP (PlayStation Portable) in Lua, and then in C++. Lots of what I learned at the time was through the small PSP homebrew community I'm incredibly grateful I got to be a part of, but I also owe much of that formative learning to free online resources and tutorials available on the internet (shoutout to2007 cplusplus.com- man does that site have a lot more ads now than it used to 😅). Eventually I became a professional software engineer and I spent the next decade "upskilling" (though usually to learn more interesting topics than needed for ) by finding and consuming a wealth of technical blogs, and more importantly for my learning style - hands on tutorials. Resources like thebuild-your-own-x repo, andCrafting Interpreters, and the 1,000 other one-off tutorials that taught me everything from buildinga raytracer, toa timeseries database, toa linear algebra matrix libraryand everything in between (seriously, I couldn't even begin to list all the amazing hands-on tutorials out there that have influenced me).

Hands on learning is how I've always learned best. These tutorials gave me the learning curve I needed to go from zero-to-one in a brand new domain, but even more importantly they gave me footing and confidence to take it from one-to-two-to-ten on my own.

Fast forward to 2026, and now we've got LLMs. I'm not going to go off topic about my complicated relationship with LLMs, but for writing software they areinterestingand in many cases they can be really productive! But they do most of the work for you, and with that work gone they also take away the part that helped me learn a new concept or domain. In some cases, that doesn't matter - we've got a product to ship and LLMs help us ship it faster - but for me and my joy in this field and hobby I still crave those "ah ha!" moments where something finally clicks and I have the confidence I need to begin shaping it into my own.

So lathe is an experiment in using LLMs to teach me, rather than think for me. To recreate those moments of hands-on learning that taught me to love this work, and marry it with thepotentialof a broad "expert" LLM who can, in theory, teach me anything. I use lathe as a catalyst to get me started on projects I wouldn't know how to start in, andcan't find any existing human written resources to teach. For example I first came up with lathe because I wanted to write a 3D Slicer Software from scratch (just finding documentation on g-code was a pain, shoutout toreprap). At the time of writing I'm diving into the world of embedded software development with Zig. Both of these cases lathe has been an effective tool in getting me from zero-to-one in obscure or extremely young domains where the human written resources just don't exist yet (and I wonder for how long humans will still bother writing tutorials if only the LLMs read them...).

## But what about hallucinations?

Are lathe tutorials as good as ones written by humans? Not in the slightest. But what they lack in heart, personality, and architectural soundness, they make up for by having the tutorial writer ready and waiting to answer all of your questions, always willing to fix or update their tutorial when it isn'texactlywhat you wanted, and they actually complete writing all 6 parts to that series they started in 2018 (we've ALL been there 😁). Lathe is an LLM, and while I've built and tuned it to be as good as I know how to make it for this particular task, it's still going to fail in the ways LLMs fail. I recommend using the biggest "thinking" model you have access to (Opus, GPT-5 Codex, etc) as these tasks are less about iterative mechanical execution you might optimize for when programming, and more about researching, designing, and explaining a tangible concept from start to finish.

Additionally, the risk for hallucinations in this context is, in my opinion, significantly lower. Lathe is built to helpyoudo the thinking, and is built around the expectation that you're the one typing this code out yourself. By reading through the guide and typing it out, you are actively engaged in the work and should be well positioned to naturally ask "wait, does that make sense?" when you come across something weird. At which point you can/lathe-ask(and sometimes the LLM comes back withgoodreasoning I didn't have because it's a foreign domain, and I learn something) or just straight tell your LLM to update the tutorial. While I have no pedagogical credentials to back this up, I think I may be actually internalizing concepts better by catching and pushing back on perceived slip-ups of the LLM. YMMV.

All of that said, if you can find a tutorial written by a human, I'd always reach for that first. I hope more often than not you do. But if you learn the same way I do and want to dive into a domain that is light on teaching materials, lathe is a pretty cool tool. Just remember it is an LLM and not a human. To help with this, I try to make it clear at all times what you are and are not getting. The lathe skills to write tutorials will tell you when it isn't sure about something it has written, and while I offer a more "personal" voice, I've defaulted to one that doesn't pretend to be something it isn't.

## Be honest, did you vibecode this? Isn't that contradictory to your thesis?

Yep, lathe is "vibecoded". In this case, the scope and risk of lathe is low. It's a living thesis, for personal learning. That said, I've been using it daily lately and it's proven to be a useful and stable tool in my toolbox. I'm learning a lot by using it, and at this point I think it's good enough that others might benefit from it too. I expect the next few point releases to be some intentional code/architecture clean up to ensure it remains stable for others, and of course incorporate any feedback I get.

That said, for the sake of transparency, today I test lathe for my own usecases - Using Claude Code on MacOS. If you are outside of that setup, latheshouldwork, but I've not verified it. If you're willing to try it on a different setup and it does work, or you end up hitting a bump in the road, I'd love an issue letting me know either way!

## Alright then, how does it work?

* LLM skills— generate and work with tutorials, all run in your interactive LLM session:/lathewritespart-01.md,/lathe-extendadds the next part,/lathe-verifyworks through a tutorial to confirm it compiles and runs,/lathe-askanswers questions about a part you're reading, and/lathe-tagadds search tags to existing tutorials.I moved to running all of these interactively, because I am a Claude Code user and headlessclaude -pis planned to be metered as of 2026-06-15. Maybe after that change I'll find that the cost is minimal (generating tutorials does not consume a lot of tokens compared to vibecoding) and we can move some of these interactions back into the UI. We'll see!
* I moved to running all of these interactively, because I am a Claude Code user and headlessclaude -pis planned to be metered as of 2026-06-15. Maybe after that change I'll find that the cost is minimal (generating tutorials does not consume a lot of tokens compared to vibecoding) and we can move some of these interactions back into the UI. We'll see!
* latheCLI(Go) — copies tutorials into~/.lathe/tutorials/, serves the rendered output athttp://localhost:4242, and owns all durable state. It never calls an LLM itself: the web buttons and thelathe verify/lathe extendcommands just hand you the skill command to paste into your session, and the skills call back into the CLI (lathe store,lathe verify-result,lathe extend-start/extend-commit,lathe voice add) to record results.

## What's up with the fancy UI?

I'm glad you asked! The lathe skills and CLI were built in tandem to offer (what I think is) a great reading and learning experience. A few key features that make using lathe worth more than just prompting Claude directly (for me) are:

### Full table of contents navigation if you hover on the right side bar

### Content is written with side-notes throughout to prompt me to think more deeply

### Left-to-the-reader Exercises at the end of each tutorial

## Writing voices

Every tutorial is written in avoice. A voice controlshow the prose soundsbut it doesn't change accuracy, research, citation, verification, or structure, which are fixed. Two voices ship with lathe:

* plainspoken(the default) — honest and precise, with no invented persona
or fabricated first-person war stories. It's written to avoid anthropomorphizing
the LLM that produced it.
* companion— an attempt at a warm, wry, first-person "friend at the keyboard".

Pick one per run by naming it in your/latheinvocation ("…in the companion
voice"), or change the global default:

lathe voice list 
#
 see what's available; * marks the default

lathe voice show companion 
#
 print a voice's full spec

lathe voice set-default companion 
#
 change the default for new tutorials

Custom voices.If you don't like the voices that come with lathe that's cool, you do you. You can author your own with/lathe-voicein an LLM session, and it'll interview you about register, person, and humor, draft a spec, and (on
your approval) save it vialathe voice add <name> --file -into~/.lathe/voices/.

Custom voices are instructed to not impersonate a real named person, fabricate credentials, or deny LLM authorship./lathe-voicerefuses those, and every voice is wrapped with a fixed preamble enforcing the same at generation time. The voice a tutorial was written in is recorded on it (so/lathe-extendcontinues in it) and is disclosed in an authorship byline at the top of every tutorial:Generated by <Model> · voice <name>where the model is the specific LLM used to generate the tutorial (e.g. "Claude Opus 4.8"), and the voice name expands to reveal the full spec.

I fully recognize this is a cat and mouse game, and that any attempts at safety here can be circumvented. Unfortunately, whether I publish lathe or not the bad actors who want to flood the world with AI slop tutorials are already going full steam ahead. I want to do my part though to make it clear that lathe is NOT intended for writing content outside of your personal use for your personal learning.

## Finding tutorials

As your library grows, the web list page (lathe serve) has a search box and filters to narrow it down — all client-side, so it stays fast and offline:

* Searchmatches a tutorial's title, topic, tags, repo, and tool versions.
* Sortby newest, oldest, or title (A–Z).
* Filterby status, by type (single vs. series), by tag, and by version.

Default port is4242; override with--port.

## Storage layout

Tutorials live globally in~/.lathe/tutorials/, one directory per slug:

~/.lathe/tutorials/
 digital-synth-zig/
 metadata.json
 part-01.md
 part-02.md
 part-03.md
 database-from-scratch-go/
 metadata.json
 index.md

metadata.json:

{
 
"slug"
: 
"
digital-synth-zig
"
,
 
"title"
: 
"
Build a Digital Synth in Zig
"
,
 
"topic"
: 
"
build a digital synth in Zig
"
,
 
"created"
: 
"
2026-05-03T19:00:00Z
"
,
 
"status"
: 
"
unverified
"
,
 
"tags"
: [
"
zig
"
, 
"
audio
"
, 
"
dsp
"
],
 
"parts"
: [
"
part-01.md
"
, 
"
part-02.md
"
, 
"
part-03.md
"
],
 
"tools"
: [{ 
"name"
: 
"
zig
"
, 
"version"
: 
"
0.13.0
"
 }],
 
"sources"
: [
"
https://ziglang.org/documentation/0.13.0/
"
],
 
"voice"
: 
"
plainspoken
"
,
 
"model"
: 
"
Claude Opus 4.8
"

}

Everything beyond the core fields (slug/title/topic/created/status) is optional and omitted when empty:tools(the languages/toolchains the tutorial targets, surfaced as version chips and theVersionsfilter),sources(the research trail — see below),voiceandmodel(the byline on the reading page), andrepo/repo_branchwhen a tutorial was written against a specific git repository.

Status is one ofunverified(the default afterlathe store; renders no badge),verifying,verified,failed,skipped, orextending(set while/lathe-extendis writing a new part). On failure, averify-result.jsonis written alongside with the failed part, step number, and error output; the web UI renders it as a panel on the tutorial page.

## Sources & provenance

Every tutorial keeps the research trail behind it — the URLs the generation skill actually consulted while writing. This is distinct from the inline## Sourcescitations inside a part's markdown: it's a durable, tutorial-level record stored in thesourcesfield ofmetadata.jsonand surfaced in the UI as provenance, so you can sanity-check where the material came from rather than taking the prose on faith.

* /lathecaptures them vialathe store --source <url>(repeatable), and/lathe-extendfolds any newly-consulted URLs into the same trail (lathe extend-commit --source), de-duped against what's already there.
* On thelist page, each card shows a· N sourcescount in its metadata line.
* On thereading page, a"Researched against N sources"panel expands to the full list of links.

## Verification

Verification isopt-inand runs in your interactive LLM session. Storing a tutorial leaves itunverifiedand nothing runs until you ask. Thelathe verify <slug>command, the--verifyflag onlathe store, and theVerify this tutorialbutton in the web UI all just hand you the same command to paste into your session:

/lathe-verify <slug>

The/lathe-verifyskill works through every step in the tutorial, creating files in a freshmktemp -dscratch dir (never your repo), running commands, executing each## Checkpointblock and then callslathe verify-resultto record the outcome in the tutorial'smetadata.json. It marks the runverifyingwhen it starts and a terminalverified/failed/skippedwhen it finishes.

Verification only makes sense where the tutorial's toolchain is installed. If a required tool is missing (e.g. nozigbinary), the run is reported asskipped(⚠️) rather than failed — "couldn't verify here" is not the same as "broken."

Because verification now runs in your own interactive session, it executes under your normal LLM permission model, so you see and approve the tool calls. The scratch-dir convention keeps build artifacts out of your repo, but treat it as soft isolation at best, not a security boundary.

## About

Generate hands-on, multi-part technical tutorials on demand, with LLM skills tuned to make content approachable. Then you work through them yourself, by hand ✋

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

503

 stars
 

### Watchers

0

 watching
 

### Forks

14

 forks
 

 Report repository

 

## Releases4

v0.3.0

 Latest

 

Jun 7, 2026

 

+ 3 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Go74.3%
* CSS13.2%
* HTML11.2%
* Shell1.3%
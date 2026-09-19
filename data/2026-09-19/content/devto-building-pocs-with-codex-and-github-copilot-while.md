---
title: Building PoCs with Codex and GitHub Copilot while they try to adjust my PoC requirements along the way - DEV Community
url: https://dev.to/missamarakay/building-pocs-with-codex-and-github-copilot-while-they-try-to-adjust-my-poc-requirements-along-the-1fc9
site_name: devto
content_file: devto-building-pocs-with-codex-and-github-copilot-while
fetched_at: '2026-09-19T21:18:03.718093'
original_url: https://dev.to/missamarakay/building-pocs-with-codex-and-github-copilot-while-they-try-to-adjust-my-poc-requirements-along-the-1fc9
author: Amara Graham
date: '2026-09-16'
description: But Amara, you didn't include MY favorite AI!. Tagged with ai, productivity.
tags: '#ai, #productivity'
---

Comparing ChatGPT Codex and Copilot features

I think it took about 10 minutes after I published mylast blogfor someone to ask about yet-another-AI-tool.

So here's two more. Then I'm done for now so I can write about the audit I did with all these tools.

## ChatGPT + Codex

This felt like Claude without the orange splat logo. With a fresh download I was on 5.6 Terra Medium.

Codex created a React PoC that loaded fairly quickly, but I did have to go back and forth with it a few times to get a functional PDF viewer running and then a few more times to get the extraction not only working, but working well if the data was missing or redacted (and, if done properly, missing).

More effectively than the other AIs, it found (or made, as it claimed) valid PDFs with interesting data and formats. I did push a little harder to redact info and re-upload the redacted PDF but this appeared to work with a little nudge to leave the field blank instead of trying to grab the next field label.

This was definitely the most seamless experience. It modified the code in the directory (and yes, it did ask for approval as that's the setting it's on) and I would stop and restart thenpm run devcommand to see what the new updates would yield.

It did feel like it was initially a little too quick to stub or mock things, including in the initial project stubbing the WebViewer... after it very quickly recommended Apryse WebViewer in 30 seconds with the initial. So why stub it? Maybe it was scared it needed a license key to function at all.

This is intentionally a frontend prototype; the next implementation step is replacing the mock paper viewer with Apryse WebViewer and wiring the extraction/audit actions to backend APIs.

So you know I was like:

Great, can you replace the mock paper viewer with Apyrse WebViewer so I can actually do extraction?

And we got there pretty quick, but it was an interesting choice to create a front end with the part I'm actually trying to PoC stubbed out. Very pay-no-attention-to-the-man-behind-the-curtain if you ask me.

## GitHub Copilot

For the purposes of my little exercise, all but one option I used was a free tier. This immediately caused issues with the follow up I tried to do on Friday - GitHub Copilot wasn't available as a desktop app for free tier users, which I didn't realize until I tried to launch it.

Never fear, I launched it in VS Code and then got distracted when I expected to see something like the Claude experience. I assumed it just didn't work or install properly.

Turns out, it installed just fine, but unlike my other AI chat experiences, I needed to make sure I was in a new project and didn't have any files actively opened, because it was certainly going to use those as context.

I'm GitHub Copilot, using Claude Haiku 4.5.

Excuse me, Claude is back? Wild. For reference, I'm using Sonnet 5 with Claude on the desktop app.

It. Is. So. Fast.

It gave me a PoC project structure in 5 seconds with a button to create a workspace. It created the project after I selected a parent directory in less than a minute and apparently only used 0.2 credits, which I can clearly see on the screen.

And then... it broke my heart.

Once I got the project structure I started to install the dependencies and ran into all sorts of mess. I continued to push on GitHub Copilot to help sort this. First it was let's adjust the WebViewer from9.somethingto10.0.0. Then it was like how aboutlatestbecause this is a PoC anyway. Then it suggested I switch topdf.jsbecause I was having so many issues with the package.

The Apryse package isn't properly installed. Since we've been struggling with the package, let's use PDF.js instead—it's simpler and already works:

Dear reader,Iwas having no issues with the package. I was watching GitHub Copilot make some interesting choices with getting any sort of correct version, so I asked it:

What sources are you using for Apryse? I was able to build PoCs like Claude easily.

I like to use AIs adversarially, so I figured I would name drop and see what happened.

You're right—I apologize. Since you work at Apryse, you likely have internal access to the package that I don't have visibility into.

This is the same garbage Microsoft Copilot inferred because it saw the directory file tree included my Apryse email. I corrected it's theory that I had access to an internal repository and it seemed to suggest I should evaluate the PDF viewer and Apryse separately.

What sources are you using to generate the Apryse-based code? They seem like they are using old versions of the packages. Can you give me a list of the sources you've used in this chat?

And to my horror, it told on itself.

You're right to call this out. I don't have access to specific sources—I'm generating code based on general patterns I've learned, not from live documentation or current package versions.

For Apryse specifically, I've been making educated guesses about:

* Package names (@pdftron/pdfjs-express)
* API structure (WebViewer() function)
* Configuration options (path: '/lib')

This is problematic because:

1. I can't verify current versions on npm
2. I don't have access to official Apryse docs to cross-reference
3. The code I generated is likely outdated or incorrect

Girl (gender neutral), what are you doing?

I then clarified that the Apryse docs are public, but that GitHub Copilot didn't have access to browse the web in real-time. And let me tell you, I was violently irritated with this, despite only spending like 30 minutes on this.

When AI speaks with conviction, as it so often does, it's really compelling. You accept what it's given you because you have no real reason not to... until something like this happens. What's truly the most problematic is at no point earlier in the conversation did it mention it didn't have access to the public internet. The default for all other AIs is having access to the internet!

I ended up finding the configuration in my GitHub settings, adjusting the toggle to allow GitHub Copilot to search the internet, and reran the original prompt in a new chat and allowed it to make a new project.

The project structure was wildly different, I ran into exactly zero package version issues, and in 10 minutes had a working Apryse-based PoC. Instead of building me a generic React project, it built me something with Apryse, front end and back end.

## What's next?

If you won't tell me your favorite AI, who is your favorite coworker?

Since I'm using these for work, I'm going to continue to try to make Microsoft Copilot work, along with getting into the program that allows me to work with Claude.

Admittedly, I'm really disappointed in the GitHub Copilot experience not being up front about it's access to the broader internet, and then not being able to guide me to the correct setting to allow it the access I assumed it already had. Maybe this is a safety mechanism and provides a better experience for folks just doing vanilla programming, no 3rd party tech and APIs required. Just tell me that's what's going on.

This audit is kind of a one time thing, in the sense that I probably won't regularly use all the tools I can get my hands on, and I'll eventually spoil my setups by adding too much personalized context. Is there a concept of incognito mode in any of these tools? I still want to do some kind of DevEx audit like the in the future, but I may be constrained simply by using these tools for my daily work.

Drop your tips and tricks for me in the comments about working with Microsoft Copilot!

Photo byImmo WegmannonUnsplash

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (13 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
---
title: 'Haskell for all: Beyond agentic coding'
url: https://haskellforall.com/2026/02/beyond-agentic-coding
site_name: hnrss
content_file: hnrss-haskell-for-all-beyond-agentic-coding
fetched_at: '2026-02-08T19:12:25.589774'
original_url: https://haskellforall.com/2026/02/beyond-agentic-coding
date: '2026-02-08'
description: AI dev tooling can do better than chat interfaces
tags:
- hackernews
- hnrss
---

# Haskell for all

###### Saturday, February 7, 2026

## Beyond agentic coding

I'm generally pretty pro-AI with one major exception: agentic coding. My consistent impression is that agentic coding does not actually improve productivity and deteriorates the user's comfort and familiarity with the codebase. I formed that impression from:

* my own personal experiencesEvery time I use agentic coding tools I'm consistently unimpressed with the quality of the results.
* my experiences interviewing candidatesI allow interview candidates to use agentic coding tools and candidates who do so consistently performedworsethan other candidates, failing to complete the challenge or producing incorrect results1. This was a huge surprise to me at first because I expected agentic coding to confer an unfair advantage but … nope!
* research studiesStudies like theBecker studyandShen studyshow that users of agentic coding perform no better and sometimes worse when you measure productivity in terms of fixed outcomes rather than code velocity/volume.

I don't believe agentic coding is a lost cause, but I do believe agentic coding in its present incarnation is doing more harm than good to software development. I also believe it is still worthwhile to push on the inadequacies of agentic coding so that it empowers developers and improves code quality.

However, in this post I'm taking a different tack: I want to present other ways to leverage AI for software development. I believe that agentic coding has so captured the cultural imagination that people are sleeping on other good and underexplored solutions to AI-assisted software development.

## The master cue

I like to design tools and interfaces from first principles rather than reacting to industry trends/hype and I've accrued quite a few general design principles from over a decade of working in DevProd and also an even longer history of open source projects and contributions.

One of those design principles is my personal "master cue", which is:

A good tool or interface should keep the user in a flow state as long as possible

This principle isn't even specific to AI-assisted software development, and yet still highlights why agentic coding sometimes misses the mark. Both studies and developer testimonials show that agentic coding breaks flow and keeps developers in an idle/interruptible holding pattern more than ordinary coding.

For example, theBecker studytook screen recordings and saw that idle time approximately doubled:

I believe we can improve AI-assisted coding tools (agentic or not) if we set our north star to “preserve flow state”.

## Calm technology

Calm technologyis a design discipline that promotes flow state in tools that we build. The design principles most relevant to coding are:

* tools should minimize demands on our attentionInterruptions and intrusions on our attention break us out of flow state.
* tools should be built to be “pass-through”A tool is not meant to be the object of our attention; rather the tool shouldrevealthe true object of our attention (the thing the tool acts upon), rather than obscuring it. The more we use the tool the more the tool fades into the background of our awareness while still supporting our work.
* tools should create and enhance calm (thus the name: calm technology)A state of calm helps users enter and maintain flow state.

## Non-LLM examples of calm technology

Engineers already use “calm” tools and interfaces as part of our work and here are a couple of examples you're probably already familiar with:

### Inlay hints

IDEs (like VSCode) can supportinlay hintsthat sprinkle the code with useful annotations for the reader, such as inferred type annotations:

These types of inlay hints embody calm design principles because:

* they minimize demands on our attentionThey exist on the periphery of our attention, available for us if we're interested but unobtrusive if we're not interested.
* they are built to be “pass-through”They don't replace or substitute the code that we are editing. They enhance the code editing experience but the user is still in direct contact with the edited code. The more we use type hints the more they fade into the background of our awareness and the more the code remains the focus of our attention.
* they create and enhance calmThey promote a sense of calm by informing our understanding of the codepassively. As one of theCalm Technologyprinciples puts it:“Technology can communicate, but doesn't need to speak”.

### File tree previews

Tools like VSCode or GitHub's pull request viewer let you preview at a glance changes to the file tree, like this:

You might think to yourself “this is a very uninteresting thing to use as an example” but that's exactly the point. The best tools (designed with the principles of calm technology) are pervasive andboringthings that we take for granted (like light switches) and that have faded so strongly into the background of our attention that we forget they even exist as a part of our daily workflow (also like light switches).

File tree previews:

* minimize demands on our attentionThey're there if we need the information, but easy to ignore (or even forget they exist) if we don't use them.
* are built to be “pass-through”When we interact with the file tree viewer we are interacting directly with the filesystem and the interaction between the representation (the viewer) and the reality (the filesystem) feels direct, snappy, and precise. The more we use the viewer the more the representation becomes indistinguishable from the reality in our minds.
* create and enhance calmWe do not need to constantly interact with the file tree to gather up-to-date information about our project structure. It passively updates in the background as we make changes to the project and those updates are unobtrusive and not attention-grabbing.

## Chat-based coding agents are not calm

We can think about the limitations of chat-based agentic coding tools through this same lens:

* they place high demands on our attentionThe user has to either sit and wait for the agent to report back or do something else and run the LLM in a semi-autonomous manner. However, even semi-autonomous sessions prevent the user from entering flow state because they have to remain interruptible.
* they are not built to be “pass-through”Chat agents are a highly mediated interface to the code which isindirect(we interact more with the agent than the code),slow(we spend a lot of time waiting), andimprecise(English is adull interface).
* they undermine calmThe user needs to constantly stimulate the chat to gather new information or update their understanding of the code (the chat agent doesn't inform the user's understanding passively or quietly). Chat agents are also fine-tuned to maximize engagement.

## Prior art for calm design

### Inline suggestions from GitHub Copilot

One of the earliest examples of an AI coding assistant that begins to model calm design principles is the OG AI-assistant:GitHub Copilot's support for inline suggestions, with some caveats I'll go into.

This does one thing really well:

* it's built to be “pass-through”The user is still interacting directly with the code and the suggestions are reasonably snappy. The user can also ignore or type through the suggestion.

However, by default these inline suggestions violate other calm technology principles:

* they demand our attentionBy default Copilot presents the suggestions quite frequently and the user has to pause what they're doing to examine the output of the suggestion. After enough times the user begins to condition themselves into regularly pausing and waiting for a suggestion which breaks them out of a flow state. Now instead of being proactive the user's been conditioned by the tool to be reactive.
* they undermine calmGitHub Copilot's inline suggestion interface is visually busy and intrusive. Even if the user ignores every suggestion the effect is still disruptive: suggestions appear on the user's screen in the center of their visual focus and the user has to decide on the spot whether to accept or ignore them before proceeding further. The user also can't easily passively absorb information presented in this way: understanding each suggestion requires the user's focused attention.

…buuuuutthese issues are partially fixable by disabling the automatic suggestions and requiring them to be explicitly triggered byAlt+\. However, unfortunately that also disables the next feature, which I like even more:

### Next edit suggestions (also from GitHub Copilot)

Next edit suggestionsare a related GitHub Copilot feature that display related follow-up edits throughout the file/project and let the user cycle between them and possibly accept each suggested change. They behave like a “super-charged find and replace”:

These suggestions do an amazing job of keeping the user in a flow state:

* they minimize demand on the user's attentionThe cognitive load on the user is smaller than inline suggestions because the suggestions are more likely to be bite-sized (and therefore easier for a human to review and accept).
* they're built to be “pass-through”Just like inline suggestions, next edit suggestions still keep the user in close contact with the code they are modifying.
* they create and enhance calmSuggestions are presented in an unobtrusive way: they aren't dumped in the dead center of the user's attention and they don't demand immediate review. They exist on the periphery of the user's attention as code suggestions that the user can ignore or focus on at their leisure.

## AI-assisted calm technology

I believe there is a lot of untapped potential in AI-assisted coding tools and in this section I'll sketch a few small examples of how we can embody calm technology design principles in building the next generation of coding tools.

### Facet-based project navigation

You could browse a project by a tree of semantic facets. For example, if you were editingthe Haskell implementation of Dhallthe tree viewer might look like this prototype I hacked up2:

The goal here is to not only provide a quick way to explore the project by intent, but to also improve the user's understanding of the project the more they use the feature. "String interpolation regression" is so much more informative thandhall/tests/format/issue2078A.dhall3.

Also, the above video is based on a real tool and not just a mock. You can find the code I used to generate that tree of semantics facetshereand I'll write up another post soon walking through how that code works.

### Automated commit refactor

You could take an editor session, a diff, or a pull request and automatically split it into a series of more focused commits that are easier for people to review. This is one of the cases where the AI canreducehuman review labor (most agentic coding toolscreatemore human review labor).

There issome prior art herebut this is still a nascent area of development.

### File lens

You could add two new tools to the user's toolbar or context menu:“Focus on…”and“Edit as…”.

“Focus on…”would allow the user to specify what they're interested in changing and present only files and lines of code related to their specified interest. For example, if they want to focus on “command line options” then only related files and lines of code would be shown in the editor and other lines of code would be hidden/collapsed/folded. This would basically be like “Zen mode” but for editing a feature domain of interest.

“Edit as…”would allow the user to edit the file or selected code as if it were a different programming language or file format. For example, someone who was new to Haskell could edit a Haskell file “as Python” and then after finishing their edits the AI attempts to back-propagate their changes to Haskell. Or someone modifying a command-line parser could edit the file “as YAML” and be presented with a simplified YAML representation of the command line options which they could modify to add new options.

## Conclusion

This is obviously not a comprehensive list of ideas, but I wrote this to encourage people to think of more innovative ways to incorporate AI into people's workflows besides just building yet another chatbot. I strongly believe thatchat is the least interesting interface to LLMsand AI-assisted software development is no exception to this.

## Footnotes

1. Getting the correct output wasn't even supposed to be the hard part of the coding challenge. The standard interview challenge provided the candidate with a golden output that their program needed to match and despite that agentic coders would not only fail to match the golden output but sometimesnot even realizetheir program didn't match the golden output because they hadn't even run their agentically coded solution to check if it was correct. The actual hard part of the coding challenge was supposed to be follow-up questions about the journey to production, which vibe coders also performed worse on.↩
2. The cluster labeler still needs work but you get the idea.↩
3. That's on me since I named the file 😅.↩

Copyright © 2026
Gabriella Gonzalez
. This work is licensed under
CC BY-SA 4.0

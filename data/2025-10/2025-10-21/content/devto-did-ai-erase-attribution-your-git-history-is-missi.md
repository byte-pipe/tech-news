---
title: Did AI Erase Attribution? Your Git History Is Missing a Co-Author - DEV Community
url: https://dev.to/anchildress1/did-ai-erase-attribution-your-git-history-is-missing-a-co-author-1m2l
site_name: devto
fetched_at: '2025-10-21T19:08:02.041638'
original_url: https://dev.to/anchildress1/did-ai-erase-attribution-your-git-history-is-missing-a-co-author-1m2l
author: Ashley Childress
date: '2025-10-15'
description: Your AI assistant might be the most productive co-author you’ve ever had, but your git history doesn’t know it. Here’s how to fix that. Tagged with githubcopilot, ai, productivity, automation.
tags: '#githubcopilot, #ai, #productivity, #automation'
---

🦄 I've been trying to get to this post for a while and I was likely working on it when Idefinitelyshould have been doing something else entirely. I wrote about this topic briefly in a previous post, but that brief aside does the whole concept a disservice.

I've been begging anyone who will listen topleasesteal this idea from me, 🙏 use it in real projects, personal projects, and then give it to a friend like a party favor nobody asked for. So far, feedback is positive and change is very slow. This is my attempt to nudge it along while I figure out the next piece of the puzzle—which is language-agnostic enforcement at scale (yes, I know—thatsounds simple, right?).

So while I've been patiently waiting on Father Time to drop off some 36-hour days from the cosmos, I managed to throw together the first little helper in a much larger puzzle:self-reporting Responsible AI (RAI) statistics within the existing confines of the Software Development Life Cycle (SDLC).

Also (because it's me), this is the dramatic story version of this entire concept from the very first time I tried to define AI attribution. Ireally triedto fit the whole concept into one post instead of spreading it out over a series—spoiler: I failed.🛋️🍿

## Where Things Started 🧨

When I first started this “experiment” with Copilot, I set out to prove that AI was capable of self-directed implementation, at least for very specific and tightly controlled scenarios. I began by writing a small ecosystem of customizations that would not only track the overall effectiveness of this “new AI thing,” but also standardize it in a way that essentially mimicked my own workflow. What ended up being my first working system of reporting was effective, but also overly verbose and only traceable if you take every word I documented as gospel.

To be fair, I was very much learning how to work with these LLMs with any degree of accuracy at all whatsoever. There were no tutorials. No how-to videos. Not even a boilerplate to get me started. Just me, Copilot Agent Mode, the official GitHub docs, anda stubborn determination that this project was absolutely happening.The only “proof” I had that my initial plan was even plausible was my completely baseless gut instinct that AI was far more capable than anything I saw anybody using it for at the time.

I started this nights-and-weekends project sometime late in April 2025 with ChatGPT as acting project manager, and by mid-May I had the initial architecture designed, the first epic storyboarded, and I had somehow managed to wrangle Copilot enough to successfully generate enough code for the first official commit. GPT-4.1 was still a good month away from its preview release. That puts my default baseline somewhere between Claude 3.7 and GPT-4.0.

For anyone still decoding the quirks between LLM models, this was like revving a rusty 20-year-old Corolla and expecting an 8-speed Corvette. Not a great outlook for success, really, butI did not care—the target was an enterprise-grade, AI-generated POCthat could be implemented piecewise without any form of human intervention (outside of the review cycles). As far as I was concerned,that’s exactly what was going to happen, regardless of whether the tech was ready for that fact or not.

🦄 Yes—ambitiousmight have been a tiny understatement. 🤏 At the time though, this was my all-in project. Remember that I don’t do partial amounts of anything? This version of all-in wasa whole other levelthat I’ve filed under“intense determination”(but obsession is also accurate).

Also, no—it did not go smoothlyat all, especially at first! Curious? Check out one of my favorite stories describingwhat you should never do after handing AI the keys.

Ultimately Copilot and I settled into a solid soccer-van approach and that worked well for a while. After a month or so, I’d perfected several sets of specialized instructions and custom prompts that would allow me to use a slash command and a Jira ID to direct every single thing Copilot would do. I’d sit back and enjoy popcorn (and occasional fireworks) while stories were implemented in record time and, for the most part, in the exact same way I would have done it myself.

Self-correcting reviews were baked in from several different perspectives—as were both tech and user documentation. Basic unit and integration tests were enforced with a 90% coverage goal. Short of a couple markdown files I used for personal notes and exactly four well-documented blocks of code (that were later replaced), that entire project is100% AI-generated. It’s alsoa fully tested, production-grade, mostly-secure enterprise POC with attribution(albeit, very ugly attribution) at every single step.

🦄 This project is alsostilltrapped behind work’s seemingly non-existent OS program where it’s currently dying a slow, solitary death—I do have a plan, though! Once I address this non-existent time situation, this project is definitely on the list of planned revivals. Seriously—if enterprise work didn’t require at least six independently repetitive forms with accompanying blood draw for nearly everything, this would not be such an issue!

## RAI As A Default ⚖️

Responsible AI spans the whole chain—from model builders to end-users prompting outputs. I’ll try to explain my thinking and leave the soapbox alone, but let’s establish a baseline first:

1. Attribution is expected for production code.I could probably write a post just on attribution alone, but let’s assume the requirement for simplicity’s sake—not only for legal reasons but because two years from now I’m going to be trying to figure outwhat sort of fever dream inspired this insanity, and every tiny bit of information helps.
2. Assume AI helps every dev, every day.Maybe not with code generation, but AI is lurking there somewhere.Welcome to the future!🔮

Ever since this AI craze started, the one thing I never hear about is traceability for AI assistance. I touched on this topic briefly a few weeks back in myAI, Content, and a Bit of Sanitypost. It really deserves its own special callout, though, becausesince when is it okay for us to collectively ignore attribution in production codebases?

I don’t know if you’ve ever had a true pair-programming experience or not, but in that scenario it’s perfectly normal—if not absolutely required—for both devs to sign every single commit, even if one never touches a keyboard. So why does the assistant get erased just because it’s silicon?

Yes—I’ve heard the arguments that AI is no better than a faster, closer Stack Overflow. To those devs, I simply reply“that’s cause you’re using it wrong!”and I’m happy to share everything I know about therightway to use AI. Don’t expect a simple solution though—it takes practice just like every other thing on the planet. 🌎

🦄 This gap doesn’t have a single thing to do with blame or even productivity. It’s aprocess failurethat previously would’ve been corrected with training, maybe with new tooling—but definitely corrected.

Right now, everyone seems perfectly content with the “maybe AI helped, maybe not,let’s make it a mystery!” approach. This approach leaves a constant trail of reflective glitter dots in my head where attribution should be living instead. 🪩😒

## Imagining A Solution 💭

If I haven’t lost you yet, we can probably agree we need to document AI assistance somewhere we can find it later. But what does that really look like? I had no clue, but became“peripherally aware”of every possibility from that point forward.

I suppose it’s worth calling out that I was literally the world’sworst committer.No joke—I’m sure I hold some kind of unbeatable world record when it comes to bad commits. That message was nothing more than an empty box that accepted random text—sentences were nonexistent and sometimes even a complete string of semi-coherent words was asking too much.

Honestly, it took me far too long to think up anything remotely legit to put in that box. That required a completely separate thought process that interrupted my whole train of code thoughts, and I was making fast progress (even if nobody could tell what that progress was supposed to be)! My name was there, though, and regardless of what randomness went into the text box (or not),that code change was permanently stamped asmine.

When I first ran across this thing calledConventional Commits, I immediately dismissed it as far too much effort for very little return. Then it would come up again, I’d take another look, and again dismiss the whole concept. Then on some random side quest (probably driven by inane curiosity), I read that I could automate the entire release process with conventional commits.

🛑Full Stop: You mean valid documentation? Automatically added to every GitHub release for me? Standardized? Customizable? Repeatable? And my very own built-in “go look over there 👉” shortcut to a whole suite of incessant questions?

GUYS! Why had I not heard of this sorcery before then?!Seriously, somebody could have passed along that tidbit of information at literally any point in the lastfive plus years!😫

For future reference, in case any pertinent info like this surfaces in the future: I can accept messages via comments below, LinkedIn, email, newspaper, postcard, Morse code, carrier pigeon, smoke signals, telepathy, or interstellar vinyl—there's plenty of options available!

Back to my point—now somebody was finally speaking a language I could comprehend! I couldabsolutelywrite commit messages if I was going to get automation out of the deal. Anything is worth me not having to manually copy-paste that information from one place to another or send an email of any kind.

What I’d dismissed several times already as completely unnecessary had instantly transformed into a personal magic wand. At this point, my entire view of commits made an abrupt 180º, and this new me is completely invested in conventional commits. I will be the best damn committer anybody has ever seen and release notes are going towrite themselves!

I researched every possible setting under the sun and started adding commitlint to all of my personal projects (work is slower, but I’m on it). I’d constantly play with one option or another just to see which sparks would fly when something was a little off. Then, out of nowhere really, it hit me—the answer had been staring right at me this whole time!

Co-authored-by: GitHub Copilot <copilot@github.com>

Enter fullscreen mode

Exit fullscreen mode

🦄 It’s so incredibly simple andexactlywhere this whole RAI attribution thing belongs. I mean, that’s exactly where attribution would be for a human pair, right? So, I see zero reason I can’t use it for my AI pair, too. And that’s exactly what I did! GitHub Copilot became my constant co-author in nearly every commit I made from that point forward.

## Evolution In Play 🌱

A co-author tag isn’t enough—it’s only the start. What I really needed was a way to differentiate between code I wrote myself and what I prompted AI to write for me without a complicated system of “this line, that line” nonsense. So that’s been evolving slowly over the last few weeks, and I’ve finally landed on something that’s stabilized enough to share.

I started with a system that split attribution by thirds:

* Assisted-bymeans I wrote the code and AI helped either through prompts or inline completions up to roughly 33% generated code.
* Co-authored-byis the 50/50-ish bucket ranging from 34–66% generated code.
* Generated-bymeans the majority of this code came from AI—roughly 67–100%.

🦄 Originally I tried usingwithinstead ofby—the friendlier industry term—but ultimately I stuck withbyfor consistency with existing Conventional Commit footers.

The next step was to stop guessing how much AI assisted and let AI figure out the math for me. So I created a reusable prompt for Copilot (and Verdent) to do that calculation on its own. I already had a much older prompt that was generating commit messages, so I rewrote that one for the newer models and added attribution as a requirement.

‼️Brief aside:I’m looking for testers to see how this prompt operates outside of my workflows. It does not touch youractualcommits in any way—it adds a./commit.tmpfile that you can add to.gitignore(I use*.tmpand have a whole set of local tracking files that use this extension).

Soplease🙏 go steal a copy from myawesome-github-copilotand report back any problems. If you’ve never set up a prompt before, you’ll need either VS Code or Visual Studio for a global setup. JetBrains, Eclipse, and Xcode can all use prompts stored in.github/prompts/*.prompt.md. See myblog series on reusable promptsfor details.

This “thirds” breakdown works great for just about everything I do, but there are times I write all the code myself and then use a quick/generate-commit-messagecommand. Well, that needs one too—so a fourth attribution was added to the list:

* Commit-generated-bymeans AI summarized a conventional commit message for me (or similar trivial contribution) but none of the code was AI-modified in any meaningful way.

The catch: you only need one footer to make the point. So what happens if AI generates some portion of codeandthe commit message? I solved that quickly and turned the whole system intoa majority-wins situation. Justpick whichever one represents the most AI. Still accurate enough to matter while not overcomplicating things.Perfect!

There is one final latecomer for completeness, which really only becomes important in a future“enforcement”stage of the game. You can’t create a rule that enforces at least one AI-attribution footerandmake the absence of a footer equivalent to human-authored content. Obviously you can’t prompt AI for human content, so until I think of a better way this one is up to you:

* Authored-byis the human author to whom all code should ultimately be attributed.

💡ProTip:Keep reading through this next part if you decide to grab the prompt. Understanding how it works is important if you want a reliable result out of it!

## Under the Hood 🚗

The prompt is just a start—not a miracle worker. The biggest problem is that Copilot doesn’t retain long-term memory; it only remembers what’s inside the active IDE session. Which meansyou have to keep things tidy enough that it can actually follow the instructions.

My current workflow—starting the moment any story moves to “in progress”—is pretty much set. I usually start with the Atlassian MCP to grab the story info plus any linked Confluence docs, the repo needing work is open in VS Code with nothing open in the editor, and a brand-new Copilot chat session ready to go. The first prompt always looks something like this (I added the comments to make it easier to read):

# ─────────────── CONTEXT ───────────────
• Using #atlassian/atlassian-mcp-server, pull info for JIRA-123, including any linked documentation in Confluence.
• Gather info to assess changes required in this #codebase.

# ─────────────── TASK BREAKDOWN ───────────────
• DO NOT MAKE CHANGES YET.
• Break this story into concise iterative pieces that include testing at every step.

# ─────────────── OUTPUT STRUCTURE ───────────────
• Document all iterative steps required to meet all acceptance criteria as an ordered list of individual steps with an accompanying unordered checklist.
• Each numbered step should be clear enough that any AI agent can be prompted one step at a time to complete and fully test with both integration and unit tests, whenever applicable.

# ─────────────── SCOPE GUARDRAIL ───────────────
• DO NOT break down tasks unnecessarily—the goal is for each step to be both meaningful and fully testable.

# ─────────────── COMPLETION CRITERIA ───────────────
• When all items are marked complete, acceptance criteria for this story should be met and all happy, sad, and edge-case paths accounted for.

# ─────────────── ADMIN NOTES ───────────────
• Include documentation updates and any relevant deployment tasks.
• Save this concise story breakdown in a new file named `./progress.tmp`.

Enter fullscreen mode

Exit fullscreen mode

🦄 Yes, I know that’sa lot.Chain-of-thought prompting like this works best with the bigger models—Claude-4, GPT-5, or even Gemini. It’s similar to the flow used bySpec-kitthat’s been making rounds recently. Honestly though? I’ve been doing it this way for so long that the extra structure usually adds time without much payoff. Still, I’m testing it, and I recommend you give it a try, too!

It took me a good bit to squash the instinct to immediately jump into implementation. Before you do that,read every single line in that new implementation plan.Does it make sense? Are there any incorrect assumptions? Are there prerequisites that need attention first? Look for inconsistencies or logic gaps before handing it over.Spec-kithelps simplify that analysis step, too!

💡ProTip:After you’ve reviewed the plan, close all open files and run/clearto start a fresh chat session. A clean slate at every step is key.

## Insert Magic Here 🔮

Once I’m comfortable with the implementation plan and I’ve got a pretty good idea of which Copilot models can safely (and most cheaply) handle each step, thenwith a fresh chat session,each task begins with a prompt that looks something like:

Implement step N in #progress.tmp

Enter fullscreen mode

Exit fullscreen mode

This is exactly how I progress through 3–4 different projects at once. Each prompt may take Copilot up to 10-ish minutes to execute. So, while that’s running I’ll rotate to the next in line to review changes via a PR-style feedback prompt sent back as a single chat message (saving as many premium requests as possible). Sometimes the code is accurate the first time, but more often it takes a couple of turns to work out the kinks. All code gets staged for commit as soon as I review it. That way I know if Copilot changes anything again after the fact.

💡ProTip:You can use the keep/undo feature if you prefer that version, but honestly I skip it. It’s just an extra click between me and toast. I keep everything and let source control be my truth.

Next up is the fun part. Copilot started with a clean session and it tracks every code change made behind the scenes already, including which one of us made that change. So the commit prompt instructs it to use that existing information to generate a commit message with the appropriate attribution footer. It all runs with a single slash command (after the initial prompt setup):/generate-commit-message.

This prompt is designed with commits in mind first and attribution second, so you end up with a valid commit message tucked neatly away in a./commit.tmpfile. Here’s an example of a message it generated recently for one of my utility projects:

fix(security): Sanitize jinja templates and add `CI` security checks

- Replace raw Jinja2 Template with Environment in `utils.py` and `generate_site.py`
- Sanitize Dev.to post HTML with bleach and render sanitized content safely
- Harden slug/filename handling to prevent path traversal and unsafe writes
- Remove unused imports and perform small refactors to resolve CodeQL unused-import alerts
- Add CI security workflow (pip-audit, bandit, flake8) and developer tooling

Generated-by: GitHub Copilot <copilot@github.com>

Enter fullscreen mode

Exit fullscreen mode

🦄 This entire concept only becomes usable if you’re not asking for a complete overhaul in any single dev’s workflow. Well... unless they’remy devs,in which case they’re used to my shenanigans already. Besides, Ireally dotry to make changes as painless as possible!

## It’s Really Just a Start 🎬

Despite testing this prompt extensively, that doesn’t mean much unless it’s repeatable beyond my workflow. So help me out and give it a try! Let me know if you find any gaps up to this point. Do you have any other ideas for more accurate tracking or a different way to memorialize attribution that I haven’t thought of?

🦄 For the record, this is me asking you toaggressivelypoke holes in my theory. Point out all the fallacies that might corrupt the system. Beyond the fact that a real tool would be preferable, do you think it can work?

There’s more still built on top of this, which I’ll cover in my next post—but for devs who are still pushing commits that look like mine used to, this is a huge change in itself! My hope is that it’s enough of a simplification to at least start the conversation.

## 🛡️ Commits and Consequences

ChatGPT helped edit this post—tightening sentences, trimming tangents, and arguing over punctuation until we both gave up. No attributions were erased in the making of this story. 💫

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse

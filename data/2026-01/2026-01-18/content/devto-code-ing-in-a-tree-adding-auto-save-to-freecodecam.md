---
title: 'Code-ing in a Tree: Adding Auto-Save to freeCodeCamp - DEV Community'
url: https://dev.to/sagi0312/code-ing-in-a-tree-adding-auto-save-to-freecodecamp-137b
site_name: devto
fetched_at: '2026-01-18T11:06:35.801200'
original_url: https://dev.to/sagi0312/code-ing-in-a-tree-adding-auto-save-to-freecodecamp-137b
author: Anju Karanji
date: '2026-01-16'
description: freeCodeCamp and Anju, sitting in a tree, code-ing (the e stays. I will die on this hill). First came... Tagged with opensource, react, javascript, webdev.
tags: '#opensource, #react, #javascript, #webdev'
---

freeCodeCamp and Anju, sitting in a tree, code-ing (theestays. I will die on this hill).First came ADHD. Then came coffee.Then—inevitably—a pull request and this blog you are currently reading.

After they set the start date for my next gig—about two weeks out—I suddenly had time to burn.I finished the onboarding docs, cooked actual food, paid the bills, watched some Jimmy Kimmel.

Eventually, I decided to do some coding—lest I find myself vacuuming the bathroom ceiling out of sheer boredom.

I poured myself a cup of coffee — still too early for the wine.

Opened VS Code.

I stared out the window.Stared at my coffee.Watched more Jimmy Kimmel.

All in the hope that a brilliant app idea would magically appear.

It didn’t.

That’s when I decided to go looking for “help wanted” signs on GitHub repos.

So, I slithered my way back into the freeCodeCamp repo. I am, if nothing else, a creature of familiarity.

I did a quick “eeny, meeny, miny, mo” and clicked on one. A small flutter followed, and I knew I’d found the one. Thank God—my Dyson was moments away from meeting the popcorn ceiling.

So, to cut a long story short, I present to you:THE ISSUE. (Here’s the original issue for context, if you’re curious-https://github.com/freeCodeCamp/freeCodeCamp/issues/57818)

Cue trumpet music.

freeCodeCamp doesn't autosave to localStorage. Users have to hit Ctrl+S.But here's the problem — nobody tells them that. So they write beautiful, gorgeous code, navigate away to watch some Netflix, come back, and discover their masterpiece has been sent to the shadow realm. Ctrl+Z can't save you here. Nothing can.

My solution was simple: add autosave—the way LeetCode and GreatFrontend already do.

You can check out the full PR hereif you want to see the implementation details.

So, after the usual forking and branching, I went hunting for the component in question. Channeling my inner High Potential’s Morgan Gillory, I found the right components surprisingly quickly.

Turns out 10,000 hours of TV viewing does pay dividends.

All jokes aside, the folder structure was intuitive. The function names were descriptive and the hunt was fairly straightforward.

I remember chatting with a Netflix engineer once. She sized me up and said, "You probably design applications backend-first, don't you?" She was right—I do. But this time? I wanted to start with something the user could see. A little visual reassurance felt like the right move. So I added a simple indicator to the toolbar (ActionRow): a FontAwesome checkmark and a quick line of text. Nothing flashy—just enough to whisper, hey, your work is safe.

You know—I’m a creature of familiarity. My go-to has always been React’s Context API or, more recently, Zustand. Redux was new territory, so I had Claude walk me through the setup - ’lastSavedTime’ was going to be used to calculate the time lapsed since the last save.

I checked all the boxes on my mental TODO list:

* Persistence to localStorage, wired into debounced onChange, onBlur, onUnmount, and beforeunload.
* A timestamp that updates every five seconds and resets cleanly on navigation—no stale “Saved 20m ago” ghosts.
* A big beautiful download button. Big enough to spot from Mars.
* Respect for the DRY, courtesy of a shared utility function and a custom hook.

Then the tests broke.Of course they did.

First up: the unit test incompletion-modal.test.tsx. I’m blaming Robert Martin andClean Codefor this one—I had refactored the logic into a utility and forgotten to update the test. An easy fix.

Then the e2e tests failed. Two tests inmultifile-cert-projects.spec.ts. Running e2e tests locally felt oddly familiar. Playwright isn’t all that different from Cypress, which I’d used before, and that familiarity helped me zero in on the real issue. The fix turned out to be simple—and, honestly, better design.

Auto-save should be silent.

I updatedcode-storage-epic.jsto suppress flash messages for auto-saves. Manual saves still get explicit confirmation; auto-saves just quietly update the timestamp. Less noise, and better UX.

My PR was officially ready.The damage report:

Days spent: 2Coffee consumed: A few hundred gallonsFat-Cat cuddles: Stole a few (unless she pushed my face away with her paw)Showers taken: 0 (for the environment, obviously!)Lessons learned: Redux isn't scary.Auto-save should whisper, not be a drama queen.

Now? I wait. And maybe shower.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse

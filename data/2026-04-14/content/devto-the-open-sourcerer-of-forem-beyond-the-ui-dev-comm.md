---
title: 'The Open Sourcerer of Forem: Beyond the UI - DEV Community'
url: https://dev.to/francistrdev/the-open-sourcerer-of-forem-beyond-the-ui-4k7p
site_name: devto
content_file: devto-the-open-sourcerer-of-forem-beyond-the-ui-dev-comm
fetched_at: '2026-04-14T11:57:20.427404'
original_url: https://dev.to/francistrdev/the-open-sourcerer-of-forem-beyond-the-ui-4k7p
author: FrancisTRᴅᴇᴠ (っ◔◡◔)っ
date: '2026-04-13'
description: Introducing a New Series "The Open Sourcerer of Forem"! I have been wanting to get into... Tagged with discuss, community, forem, opensource.
tags: '#discuss, #community, #forem, #opensource'
---

# Introducing a New Series"The Open Sourcerer of Forem"!

I have been wanting to get into contributing to Open Source for some time now. However, it was difficult for me because it is quite intimidating.

Not only you have to contribute to a Repositorywith Hundreds of people, but you also have toset up your environment which I believe is the hardest part into getting started on contributing in general. This process requires the user to read documentation, fix errors along the way, etc.

Fortunately, after posting the article on how I usedGoogle Gemini in my Winning Google Gemini: Writing Challenge, I was able to start actual contribution and I was grateful thatone of my Pull Requests got merge for the first time!I hope you guys enjoy this series :D

Check out the post that start it all:

Built with Google Gemini: Writing Challenge

 FrancisTRᴅᴇᴠ (っ◔◡◔)っ


 FrancisTRᴅᴇᴠ (っ◔◡◔)っ


FrancisTRᴅᴇᴠ (っ◔◡◔)っ

 Follow


Mar 3

## I used Google Gemini for the First Time. A Deep Analysis of my Experience so far! ✨

#
devchallenge

#
geminireflections

#
gemini

#
bash

40
 reactions

Comments

 13
 comments

 11 min read


 

# Welcome Sourcerers!

Welcome to the series where I tell a tale of anOpen Sourcerer of Forem (which is me!) made contribution to the Official Forem Repository!I will besharing the issue, the Pull Request, and what I have learned(which you may find it useful if you want to contribute)!

 

# The Issue

There is an issue named"UI Issue"by@konark_13:

# UI Issue#22902

Konarksharma13

 posted on
Mar 05, 2026

Describe the bug

While browsing Dev.to, I noticed a UI issue where two layouts appear to overlap, resulting in a combined and messy layout. This causes visual misalignment on the page and affects readability.

To Reproduce

1. Go tohttps://dev.to/devteam/welcome-thread-v367-33cn
2. Navigate to the comment.
3. Hover over the likes over the comment likes.
4. Notice that two layout components overlap and merge into an inconsistent layout

Expected behavior

The layout should render correctly without overlapping elements. Each component should maintain its intended structure and spacing.

Screenshots

https://github.com/user-attachments/assets/dcb6f2bb-8579-49d2-babb-c3c2f53ed464

Desktop (please complete the following information):

* OS, version: Mac
* Browser, version: Brave

Smartphone (please complete the following information):

* Not tested on mobile.

Additional contextI regularly use Dev.to and noticed this while browsing. It may be a minor UI issue, but I thought it would be helpful to report it so it can be reviewed if necessary.

View on GitHub

This issue states that the UI z-index is out of place, specifically on themultiple reactions. For example, you notice that this UI z-index is incorrect:

This is my first issue I tackle as an Open Source Contributor. I decide to tackle this since it allows me to get a sense of the Code-Base in general.

The first steps I did was tofind the ClassName or ID of the element responsible for the issue.That way, I can search up the name in Visual Studio Code and look for that name in a CSS file.

When I began investigating, I found the ClassName responsible, which iscrayons-article-actions.

On my Visual Studio Code, I search the name and it seems to be in the SCSS filearticle.SCSS. I change the Z-index to the highest number and began making my Pull Request from there.

 

# The Pull Request

Here is the Pull Request I made to solve this issue:

# Z-Index Increase for the Emoji UI#22905

FrancisTRAlt

 posted on
Mar 05, 2026

## What type of PR is this? (check all applicable)

* [ ] Refactor
* [ ] Feature
* [x] Bug Fix
* [ ] Optimization
* [ ] Documentation Update

## Description

Fixed the UI issue on the Emoji where you can see the "Like" button over the list of emojis as shown below:

### Before:

### After:

This also happen in the GIF. It is fixed now:

### Before:

### After:

## Related Tickets & Documents

* Related Issue #22902
* Closes #22902

## QA Instructions, Screenshots, Recordings

1. Go on any post on Dev.to.

2. Inspect the element page and look for the class name "crayons-article-actions print-hidden".

3. Change the CSS.

Instead of:z-index: var(z--sticky)

It should be:z-index: 9999

4. Comment out the z-index for this class below:

5. Then scroll and it should be the highest z-index of the page.

## What gif best describes this PR or how it makes you feel?

View on GitHub

All it does is increase the"z-index" to 9999. It is worth noting thatthis is not a "great" solution, but it does solve the issue for now.

Later on,@benrefine this solution:

//

Ensure

this

is

above

comments

but

below

dropdowns
/
modals
/
popovers

(
like

billboards
)

z-index
:

calc
(
var
(
--z-dropdown
)

-

1
);

Enter fullscreen mode

Exit fullscreen mode

Ultimately, the issue was fixed as shown below:

 

# What I learned

Here is what I learned after working on this issue!

### 1) Humble Beginning

Before this PR, I made my first Pull Request,which did not get merged.I realized that I wascreating a Pull Request that I believe that is needed and not what Forem needs.There is no shame into that and sometimesyou fumble before you can succeed.Not every Pull Request will get merged and that's ok!

When contributing to any open source, understand their needs and accomplish it.To start off, look at their issues and find an issue that seems doable to tackle. It can be as simple as fixing the UI, or changing documentation. Whatever it may be,make sure it aligns to their needs!

### 2) Slow Down

Even after the Pull request got merge, I had a conversation in that issue with@konark_13about it. I feel like it went too quickly since I was so eager into completing that issue.

According to the Forem's documentation, you have atleast 2 weeks to work on the issue.That should give you a lot of time. It is also important to document your work as well and keeping it updated, so that the Repository maintainer will know that you are still working on the issue.

Overall,communication is important to any collaboration!Apologies@konark_13if I was tackling this issue too quickly and not giving you a chance!

 

# I want to become an Open Sourcerer of Forem! Where do I start?

Everything you need is on theOfficial Forem GitHub Repository!

## forem/forem

### For empowering community 🌱

# Forem 🌱

For Empowering Community

Welcome to theForemcodebase, the platform that powersdev.to. We are so excited to have you. With your help, we can
build out Forem’s usability, scalability, and stability to better serve our
communities.

## What is Forem?

Forem is open source software for building communities. Communities for your
peers, customers, fanbases, families, friends, and any other time and space
where people need to come together to be part of a collectiveSee our announcement postfor a high-level overview of what Forem is.

dev.to(or just DEV) is hosted by Forem. It is a community of
software developers who write articles, take part in discussions, and build
their professional profiles. We value supportive and constructive dialogue in
the pursuit of great code and career growth for all members. The ecosystem spans
from beginner to advanced developers, and all are welcome to find their place…

View on GitHub

I suggest to setup your environment and making sure everything is working.Ultimately, you are trying to get the localhost to run!

 

# You made it to the end!

You have made it to the end Traveler!Thank you for reading this chapter andstay tuned for the next chapter!

Questions or Comments? I would love to hear your thoughts about this tale of The Open Sourcerer of Forem!

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse

---
title: 🐍 Snake - rendered with 576 browser windows [warning - this WILL hurt your eyes...and PC!] - DEV Community
url: https://dev.to/grahamthedev/snake-rendered-with-576-browser-windows-warning-this-will-hurt-your-eyesand-pc-3p7i
site_name: devto
content_file: devto-snake-rendered-with-576-browser-windows-warning-th
fetched_at: '2026-07-24T11:34:58.529068'
original_url: https://dev.to/grahamthedev/snake-rendered-with-576-browser-windows-warning-this-will-hurt-your-eyesand-pc-3p7i
author: GrahamTheDev
date: '2026-07-23'
description: I have been quiet lately I know - but don't worry I haven't forgotten you all and how much you like... Tagged with javascript, webdev, programming, css.
tags: '#javascript, #webdev, #programming, #css'
---

Explores browser popup API abuse

I have been quiet lately I know - but don't worry I haven't forgotten you all and how much you like seeing really stupid ideas on the web!

This one came to me after I was chatting with a colleague saying "you know you can control one browser window from another right?"

Now that was for a sensible idea around checking broken links and then confirming they work one after the other (without the issues an iFrame can introduce - there is a demo of that later in the article)...but then I realised this was one of the few parts of the web I have not yet abused!

I was trying to work out how we could build a little game with a controls window and a gameplay window and then I realised something...why limit myself to just two windows?

That has lead to this horrendous idea!

## Snake - rendered with browser windows!

You may not know this, but as long as you have some user interaction and a user allow popups you have a LOT of control over browser windows.

You can define their size (with certain constraints on minimum sizes), position etc.

And you can name a window so you can always reference it in your code so you can move multiple windows around at the positions you want!

With these two things we get a lot of opportunities for chaos!

## The Chaos!

Controls are arrow keys.

You must accept popups (in the URL bar) once you press "Start Game" and select "always allow popups from...".

Only tested on Chrome on Windows - good luck in other browsers / OS combinations!

Do not click anything! Only use the arrow keys.

When the game is over make sure to press "clear all windows" in the top score window, otherwise you may be sat there for a long time closing random windows! haha.

Share a screenshot of your screen and your high score when you have done in the comments!

### Just in case it doesnt work for you or you are on mobile

Here is a screenshot just in case you can't try it out right now.

## Ok, that was silly, lets get serious

While that was very silly, there are some very useful things you can do with this.

As I said in the intro we have a use case at work, hopefully it can serve as some inspiration for you.

We are checking for broken links in 3rd party websites.

Now the problem is some of the content is in SPAs (so we get 200 http response headers even for broken pages), some of it is behind paywalls (so we can check the page exists but can't guarantee the content behind the paywall still exists).

So we want to have a queue of items to check through, and clicking on an item in that queue opens the target page so we can check it, log in etc.

We could try and do this in a single browser window, but that would require an iframe. And, in case you didn't know, iframes can be disabled by some websites (they can block you from showing their site in an iframe on yours).

So for something more robust, we can turn to windows.

We can launch two windows, one on the left of the screen, smaller, with a list of pages to check. One on the right that we can control based on what we click in the first screen.

Click on an item on the left screen, update the URL on the right screen - no iframe magic!

And what is even better is we can resize the windows to fill the screen so they almost act like one application!

### More sensible Demo

Click the items on the left window that opens, they will change the URL in the right panel.

Mark all the working and not working pages appropriately in the left panel!

## What will you build?

What new ideas does this give you?

A window per tool in an editor?

Multi-screen applications (as you can also detect how many screens someone has and position things on second and third screens).

Let me know a) what score you got in snake (assuming it works) and b) what ideas this gives you!

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (14 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse
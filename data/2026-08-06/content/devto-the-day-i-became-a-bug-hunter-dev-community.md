---
title: The Day I Became a Bug Hunter - DEV Community
url: https://dev.to/konark_13/the-day-i-became-a-bug-hunter-3e41
site_name: devto
content_file: devto-the-day-i-became-a-bug-hunter-dev-community
fetched_at: '2026-08-06T12:55:12.325623'
original_url: https://dev.to/konark_13/the-day-i-became-a-bug-hunter-3e41
author: Konark Sharma
date: '2026-08-04'
description: 'This is a submission for DEV''s Summer Bug Smash: Smash Stories powered by Sentry. Did anyone ask for... Tagged with devchallenge, bugsmash, bounty, testing.'
tags: '#devchallenge, #bugsmash, #bounty, #testing'
---

Summer Bug Smash: Smash Stories 🐛🛹

This is a submission forDEV's Summer Bug Smash: Smash Storiespowered bySentry.

Did anyone ask for a bug hunter? No? Well, here I am.

This is an old story and special to me, but I wanted to write about it because it was my first time seriously finding bugs in someone else's software. Not bugs in my own code where I already knew which questionable decision probably caused them. Actual bugs in an actual product that someone else had built.

There was a competition where participants had to test a company's website and report as many useful bugs as possible. I participated randomly despite having almost zero experience in software testing.

There was just one small problem.

We had around six hours.

Find the bugs. Document them properly. Record the issues. Explain how to reproduce them. Submit everything before time ran out.

And obviously, higher-priority bugs were more valuable.

Meanwhile, my qualification for this challenge was basically:

"I build websites. How hard could breaking one be?"

Turns out, that was enough to get me started.

## A Hunter With Absolutely No Hunting Experience

I wasn't a software tester. I had never professionally tested software, and I definitely wasn't someone who could open the Network tab and immediately discover a critical vulnerability hiding somewhere.

I was underconfident about participating, but I've always had this habit of throwing myself into things first and figuring them out later. Sometimes it works. Sometimes it creates another article.

The night before the competition, I started watching tutorials about software testing. I learned about different kinds of bugs, common website vulnerabilities, UI/UX issues, form validation, broken functionality, responsiveness, and anything else that could possibly help me survive the next day.

The biggest question running through my head was:"What if the thing I report as a bug isn't even a bug?"

Imagine confidently submitting twenty issues only for someone to reply:"That's literally how the feature works."

So I made a small checklist of things I could test and decided on a very reasonable goal.

Findoneuseful bug. That's it.

If I could find one legitimate issue, I'd consider the whole experiment worth it.

## The Hunt Begins: Six Hours on the Clock

The challenge started, and suddenly those six hours didn't feel like six hours anymore.

We had to explore the website, identify bugs, reproduce them, document everything properly, and add the findings to an Excel sheet. A bug wasn't very useful if the developers couldn't understand what went wrong or reproduce it themselves.

So I started with the things I actually understood.

Responsiveness.

Navigation.

Forms.

Buttons.

Links.

Validation.

Basically, I approached the website like an extremely annoying user whose only purpose was to click everything and see what broke.

The first hour was comfortable. I was exploring different pages, testing features, resizing the screen, filling forms incorrectly on purpose, clicking buttons that probably wished I would leave them alone, and trying to understand how everything connected.

But time-boxed challenges have a funny effect.

At the beginning:"Six hours? Plenty of time."

A few hours later:"WHERE DID THE SIX HOURS GO?"

The pressure slowly started building, and I still hadn't found anything I considered particularly impressive.

Then I reached the footer.

## I Found My First Bug!

Since I'm primarily a developer, my instincts were naturally focused on the frontend.

Is the website responsive?

Are the links behaving correctly?

Do forms provide proper feedback?

Does something break when I use the website differently from how the developer expected me to?

While checking the footer, I noticed something small.

There were several links, but hovering over them didn't provide any visual indication that they were clickable. No color change, underline, or other hover feedback.

Was this some catastrophic vulnerability capable of bringing down the entire website?

Absolutely not.

Was I ridiculously happy?

Absolutely yes.

I had found my first usability issue.

For someone experienced in QA, this probably would've been Tuesday morning. For me, it felt like discovering a zero-day vulnerability hiding inside the footer.

More importantly, something changed after that first finding.

I stopped thinking:"I don't know how to test software."

And started thinking:"Okay!! what else can I break?"

The hunt was officially on.

## Okay!! What Else Can I Break?

Once I found the first issue, I started looking at the website differently.

Instead of simply using it, I started questioning it.

What happens if I don't fill this field?

What happens if I press Back here?

What if my name is ridiculously long?

Should this link open in another tab?

Why does this button exist if I'm already on the page it takes me to?

Suddenly, bugs started appearing everywhere.

Not huge security vulnerabilities, but real usability and functional issues that could affect someone using the website.

Some of the bugs I reported included:

1. What happens if I submit an incomplete form?:I wanted to check how the form handled partial submissions. Would it submit incomplete data, block me with validation errors, or behave differently depending on which fields were missing? So I started filling the form one input at a time, submitting it, checking the response, and repeating the process. It was tedious, but worth it. During one of these tests, I found that after partially entering the details, theBack button stopped working correctly, preventing me from cancelling the process or returning to the previous screen. A user entering the flow could essentially get stuck unless they refreshed the page or found another way out. What started as a simple form-validation test ended up exposing a navigation/state-management issue.
2. The validation worked, but forgot to tell the user:Whenever we submit a form with missing required information, we expect some feedback: a red border, an error message, focus moving to the invalid field, or at least something saying,"Hey, you forgot this."I deliberately left the required organisation field empty and submitted the form. The submission was correctly blocked, but the field itself wasn't highlighted and there was no clear indication of what I had missed. Technically, the validation was doing its job, but from the user's perspective, the Submit button simply appeared to do nothing. My recommendation was to provide visible inline validation and clearly identify the field that requires attention.
3. How long can a name actually be?:Most forms apply reasonable constraints to text inputs, whether through amaxlength, validation rule, or UI handling for unusually long values. Naturally, I wanted to see what happened here. I started typing a long name and expected the input to eventually stop me.It didn't. So I kept going. And going. The application accepted the oversized value, saved it, and then displayed it back in the UI. That's where the actual problem appeared: the unusually long value affected the layout and made parts of the interface look broken. The issue wasn't simply"the name is too long."It was that the system accepted unbounded user-controlled text without the UI being prepared to display it. A reasonable input constraint, combined with proper text wrapping or truncation on display, could prevent the layout from breaking.
4. Two links, two completely different journeys:While testing navigation, I noticed that clickingSubmissionsmoved me to the relevant section within the existing page, while clickingResourcesunexpectedly opened a new browser tab. Neither behaviour is necessarily wrong on its own, but putting them next to each other while giving them inconsistent navigation behaviour makes the interface unpredictable. If both represent internal sections of the same application, they should generally follow the same navigation pattern unless there's a clear reason not to. This was less about something "breaking" and more about maintaining predictable behaviour across the UI.
5. The URL was wrong. The error message wasn't much more helpful:Next, I deliberately entered invalid and missing URLs to see how the application validated them. The form recognized that something was wrong, but the feedback didn't clearly explain what needed to be corrected. A generic failure message forces the user to guess whether the problem is the URL format, a required field, or something else entirely. More specific validation such as"Enter a valid URL including https://..."would make the error actionable instead of simply telling the user they had done something wrong.
6. The button that takes you exactly where you already are:Some elements looked and behaved like navigation buttons, so naturally I clicked them to see where they went. The answer was surprisingly simple: the page I was already on. The interaction suggested that something should happen, but clicking it provided no meaningful change in state or navigation. From a UX perspective, that's misleading affordance. If an element isn't performing a useful action, it shouldn't look interactive. Either the navigation needed a meaningful destination, or the elements could simply be presented as non-interactive text.
7. And finally, I started questioning every link:Once I had found inconsistent navigation behaviour, I started checking links more deliberately: internal links, external links, same-tab navigation, and new-tab navigation. I found external resources that replaced the current application in the same tab, which meant users could lose their current position or partially completed workflow when leaving the site. Depending on the product's intended navigation policy, opening clearly external resources in a new tab could preserve the user's current state and make returning easier. More importantly, the application needed a consistent rule for how internal and external navigation should behave.

None of these were going to make headlines on cybersecurity Twitter. But that's when I learned something important about bugs. A bug doesn't have to crash the entire application to matter.

Sometimes a tiny interaction that makes absolutely no sense is enough to frustrate a user.

And users don't care whether the problem came from JavaScript, CSS, an API, or Mercury being in retrograde. They just know the website isn't working the way they expected.

## Bringing Home the Bugs

As the clock started running out, I organized everything as clearly as I could.

For every issue, I tried to explain what happened, what I expected to happen, and where the problem occurred. I tested the website on both my laptop and phone because I wanted to catch responsiveness issues as well.

Then, with only a few minutes remaining, I submitted the file.

My first proper bug report.

I was happy that I'd actually completed the challenge, but there was still something bothering me.

Most of my findings were related to UI, UX, navigation, validation, and frontend behaviour.

I hadn't discovered some massive network vulnerability. No authentication bypass. No dramatic hacker moment where green text started flying across my screen.

Just frontend bugs.

So naturally, I assumed I hadn't done particularly well.

This bug-hunting event was actually a mini challenge alongside a larger competition I had also participated in. I cared much more about the results of the main challenge because I thought that was where I actually had a chance of winning.

When those results came out, I wasn't in the top three.

That hurt.

I had wanted to win, and for a while that disappointment completely overshadowed the little bug-hunting challenge I'd almost forgotten about.

Then I went to sleep.

## The Hunter Gets Hunted... by an Email

The next morning, I woke up and saw an email from the organizers.

I'd won something.

My immediate thought was:"Nice. Probably third place."

Then I thought maybe it was a consolation prize.

Something along the lines of:"Thanks for participating. Here's a virtual pat on the back."

I opened the email.

First Position.

I stared at it for a moment.

Then probably read it again just to make sure my morning brain hadn't accidentally added the word "First."

I had won the mini challenge.

The challenge where I'd entered with no professional testing experience.

The challenge where my entire strategy the night before was essentially"please let me find one real bug."

And somehow, the bugs I'd found were useful enough to put me in first place. Even better, some of those findings were later used to improve the website's UI/UX.

That's when the win started meaning something different to me.

## The Biggest Bug Wasn't in the Website

Looking back, the biggest thing I discovered that day wasn't hiding inside the website.

It was an assumption I'd made about myself.

I entered the competition thinking:

"I'm a developer. I'm not a tester. I probably won't be good at this."

But being a developer actually helped me notice things.

I understood how websites were supposed to behave. I knew what users expected when they clicked buttons, submitted forms, resized screens, or navigated between pages.

I didn't suddenly become a software tester in six hours.

I simply used what I already knew from a different perspective.

And maybe that's why I still remember this challenge.

I entered hoping to findone bug.

I left with first place.

Sometimes you don't need to be an expert before trying something. Sometimes you just need enough curiosity to click the button you're probably not supposed to click and ask:

"Okay what happens if I do this?"

Turns out, occasionally you find a bug.

And occasionally, that bug finds you a trophy.

Thank you so much for taking the time to read my little bug-hunting adventure! What started as"let me somehow find one bug"somehow ended with a first-place win and a completely different way of looking at software.

Have you ever tried something completely outside your usual role and accidentally discovered that you were actually pretty good at it? I'd love to hear your story, especially if it involved breaking something that definitely worked five minutes earlier. Feel free to connect with me onLinkedIn.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
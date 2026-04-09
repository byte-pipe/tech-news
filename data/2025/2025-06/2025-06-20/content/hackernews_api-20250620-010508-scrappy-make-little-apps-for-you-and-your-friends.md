---
title: 'Scrappy: make little apps for you and your friends'
url: https://pontus.granstrom.me/scrappy/
site_name: hackernews_api
fetched_at: '2025-06-20T01:05:08.676439'
original_url: https://pontus.granstrom.me/scrappy/
author: 8organicbits
date: '2025-06-18'
description: Scrappy – Make little apps for you and your friends
tags:
- hackernews
- trending
---

UPDATE:Hello Hacker News!Here’s an FAQfor common questions not addressed in the article. We’ll keep updating it and eventually add it at the bottom of this page.

Software is important to people. Most of us spend our workdays in front of computers. We use the computer in our pocket tens if not hundreds of times every day. The apps we use are almost exclusively mass-market, sold on an app-store, made for thousands if not millions of users. Or they are enterprise apps that are custom-built for hundreds of thousands of dollars.

But there isn’t really any equivalent of home-made software — apps made lovingly by you for your friends and family. Apps that aren’t polished or flashy, but are made toyourpreferenceand help you withyour particular needs.

We’re John and Pontus, and we’ve been exploring the potential of home-made software together.

We ended up creating a research prototype that we callScrappy— a tool for makingscrappy apps for just you and your friends.First and foremost, we aim to contribute avisionof what home-made software could be like. We want to make this vision as concrete as we can, by sharing a working tool and examples of apps made in it. Scrappy, in its current state, is a prototype, not a robust tool, but we hope it paints the picture we carry in our heads — of software as something that can be creative, personal, expressive. Made by anyone, for themselves and their loved ones.

## What is Scrappy?

It may not be clear what “a scrappy app for you and your friends” means. What kind of apps are these? Let us paint a picture with a few examples. (We call them “Scrapps”.)

Arithmetic practice for a kid in elementary school.When outgrown, the Scrapp can be extended with harder problems.(try on desktop)

Attendee counter for a local event.The counter’s state is shared, so the Scrapp can be used to let people in and out at multiple entrances.(try on desktop)

Meeting cost clock,to help meetings stay on track. A Scrapp like this can be put together in 15 minutes and shared with coworkers right away.(try on desktop)

Weekly chore tracker.Let roommates flexibly swap weeks, while making sure to track whose up next, to keep things fair.(try on desktop)

## What is it like to make an app in Scrappy?

Scrappy is an infinite canvas of interactive objects. The workflow is similar to an app such as Figma, Miro, or Google Slides — except you can attach behaviors to the objects.

You drag objects out on the canvas — a button, a textfield, a few labels. Select an object, and you can modify its attribute in an inspector panel. Certain objects, like buttons, has attributes like “when clicked” that contain javascript code. When the button is clicked, that code is run — maybe it records the contents of the textfield to a label that acts as a log. You build your app step by step: tweaking and rearranging the objects, and attaching a little bit of code to them.

There’s no better way to get a feeling for an authoring environment than to see someone use it in action. In the following videos, I’m making an attendee counter for an event.

The basics.I start out by adding a number field to track the number of attendees, and two buttons for recording people entering and exiting the venue.

Your browser cannot play this video.

Reactive formulas.Next, I add a field for the venue’s capacity, and a warning when too many people have been let in.
I use a reactive formula to control the visibility of the warning and the border color of the field.

Your browser cannot play this video.

A shared, persistent world.Without any extra work, Scrappy apps are multiplayer.
App state is persisted and synced, like users expect from online documents like Google Sheets or Figma.

Your browser cannot play this video.

The app is always live.There’s no distinction between editing and running. I can edit the app while a friend is using it.

Your browser cannot play this video.

Selective sharing.I make a variant of the app that’s limited to only entering and exiting people. This is done by putting a part of the app in a frame, and sharing only that frame. The limited version is still linked to the main app.

Your browser cannot play this video.

Visible, tangible data.Here’s what theMeeting Cost Clock appshown above looks like when zoomed out, revealing a common pattern in Scrapps.

Outside the shared frame are a bunch of fields used to compute the cost of the meeting. This lets me see the data while I’m working on the Scrapp, just like in a spreadsheet, which is very helpful for debugging — and it makes future tweaking or remixing easier.

## Why make Scrappy?

This project is driven by a desire to reimagine software creation and use. As part of a growing movement variously termed “small computing,” “casual programming”, and “home-cooked software” we want toemancipate end-users— to “empower people to express themselves without requiring them to be heavy-duty programmers,” to “liberate the programming of computers from the priesthood to the layperson”, as Bill Atkinson worded it. We want to shift the world away from mass-market, industrially-produced software toward morepersonal, even disposable,tools that are designed for and readilymodified and adaptedtospecific social contexts. Above all, we want to foster a sense of agency and to ultimately contribute to “redistributing the means of software production”.

We were inspired by the simplicity of tools likeNotion,tldraw, andmmm.page, but wanted to empower people with richer interactivity and programming capabilities. However, knowing the strengths and limitations of the standard visual programming paradigms of blocks (e.g.Scratch,Blockly) and nodes-and-wires (e.g.Max/MSP,Node-RED,natto,Holograph), we deliberately wanted to go down a different path. Instead, we drew direct inspiration from “media with scripting” environments, both classic systems likeHyperCard,Visual Basic, andMacromedia Director, as well as contemporary platforms likeDynamiclandandMinecraft, where the “media with scripting” exist in a shared online world.

Overall, our target user experience was that of a productivity tool, specifically a canvas-based tool (e.g.Figma,Miro, andtldraw)—rather than programming environments (e.g.Squeak/Smalltalk, modern IDEs) and website and app builders (e.g.Squarespace,mmm.page,Bubble). And we also wanted that kind of modern “share link”-based real-time collaboration popularized byGoogle DocsandFigma.

Finally, while we acknowledge the capabilities of AI-centric systems that leverage LLMs for code generation (e.g.,Lovable,bolt.new, andtldraw computer), we deliberately chose to focus our design on direct manipulation and user control.

## Who is Scrappy for?

As we were prototyping, it wasn’t clear who the ideal user for Scrappy was. We left this open, to see what we’d learn from building the system. Eventually, a few potential personas revealed themselves.

* The process optimizer.In business environments, there’s always some improvement that can be made using software. But the person who sees the process inefficiency likely can’t make software themselves, and involving a professional programmer is expensive. So what usually happens is they make what improvements they can using tools they are familiar with, such as Excel. Here Scrappy could be a more powerful and flexible Excel, while retaining familiarity and ease of use.
* Teachers and students. Teaching programming requires teaching a multitude of inessential technical details: how to use the command line, how file systems work, how to set up the environment, dependency management, version control, servers and clients, and on and on. With Scrappy, you can just create a button, write a line of code and click the button to run the code.
* Ourselves!We are professional programmers who don’t like programming. Why? Because of the all the aforementioned complexity that adds friction to what could be so much simpler. When making mass-market apps, we know we have to deal with that complexity, but when working on a fun hobby project?! Give us a break. Scrappy is that kind of break.
* The DIYer.People like to customize their house, grow their own vegetables, sow their own clothes, build their own furniture. Scrappy is where a DIY-inclined person makes their own little apps for themselves and their friends.

As Scrappy solidified, we wanted to focus on one of these personas. There’s a pull toward business use cases, since businesses are the most willing to pay for a product, but we believe the incentives there would lead us too close to existing products likeRetoolorLiveCode. The teaching use case is compelling, but we believe it needs a better coding experience (discoverability, better error messages, debugger) which was out of scope for us (for now). We are itching to make stuff for ourselves in Scrappy (and we are strong believers in dogfooding), but most of our projects required features that would balloon the scope.

The DIYer making home-made software is the least served by existing tools, and fits our vision of democratized computing the best. We decided this is where we could make the biggest contribution (theblue ocean strategy), and decided to make the DIYer our target persona.

Ideally, Scrappy would let anyone with basic computer literacy make a simple app and learn from there. This is not quite the case yet — some JavaScript knowledge is required. So today, the person making Scrapps from scratch is aprogrammer DIYer.But when a Scrapp is shared with friends, those friends can use it and remix it without needing programming experience.

## What should I make in Scrappy?

Home-made, scrappy apps don’t really exist today, so most people (including us!) are not used to coming up with ideas for them. When faced with a problem that would make a great Scrapp, instead our minds go to “maybe there’s an app for that”, searching the web for one, giving up if we cannot find a good one. To start coming up with good uses for Scrappy requires a shift to a home-made mindset.

To help you build that mindset, here is an assortment of ideas for Scrapps (some of which are not feasible in the current prototype of Scrappy, but should be).

* Custom flashcards
* Meeting agenda manager
* Day clock for person with dementia
* Online workshop facilitation
* Consulting time tracker
* Point-based voting for a board
* Receipt generator
* Simple word game
* School grade calculator
* Interactive visual recipe
* Social quiz game
* Typing tutor
* Lyric writing aids (synonyms, rhymes)
* Board game helper
* Wedding RSVP + seating arrangement
* Dynamic opening hours display
* Family bulletin board
* Group travel planner
* Chore → allowance calculator
* Chess clock productivity timer

What makes a problem well-suited for Scrappy? Here are some things they have in common:

* Shared with friends.While a Scrapp can be for just yourself, Scrappy really shines with multiples users, leveraging the shared, persistent world. Some problems that would need setting up a backend server can be built in minutes in Scrappy.
* Needs tweaking-as-you-go.Life changes, and so does requirements. In Scrappy, you can edit the app at any time — even while your friend is using it. No building, no deploying, no fuss.
* A sprinkle of computation.Scrappy shines when thought of as a shared document first, with a little bit of computation added on top. For complex systems with a lot of moving parts, we recommend reaching for traditional software engineering tools.
* Minimal friction.We all let out a groan inside whenever we are hit with “create an account to continue”. This “account friction” may not be much, but it multiplies when sharing with a group of people — there’s always going to be someone for whom the friction is too much. Scrapps don’t have this problem: just click the link.
* Small number of trusted users.Scrappy assumes you trust the people you share a Scrapp with, which removes a lot of friction, but if you need to control access and permissions, look elsewhere.
* Not mission-critical.If you need guaranteed correctness or perfect control over details, don’t reach for Scrappy. Those qualities are what you pay expert engineers for.

## Scrappy vs mass-market apps

When faced with a “scrappy” problem — something small that would benefit from a computer — most people will think “maybe there’s an app for that”, followed by searching an app store or the Internet to look for one.

If there is no app for that, or there’s no good one, you could make your own in Scrappy. We hope you do! But often thereisan app for that. If there is, it will probably be more polished than anything you can make in Scrappy. In this case, there are still reasons to consider using making your own Scrapp:

* Does exactly what you need.And only what you need. Nothing more, nothing less.
* Home-made with love.Scrapps are made by you for your friends. A home-knitted sweater will always mean more to you than a store-bought one.
* Fun and playful.In Scrappy, it’s easy to play around. Tweak the colors, make a cute layout, add little inside jokes.
* Remixable.Easy to share with others and modify to suit your needs.
* Collaborative by default.All Scrappy apps are multiplayer, like a Google Doc is. You can even edit them while they are being used by someone else!
* No accounts and signups.If you share a Scrappy app with someone, they can start using it right away — no tedious sign-up flows stopping your friends or family from joining in.
* You own your data.The data is stored locally and will only be used for nefarious purposes if its creator (you) wants to!

## Scrappy vs AI-written apps

What about asking an LLM to make a custom, home-made app?

LLMs are getting better and better, and while they are far from able to make a full-fledged app without a lot of help from a software engineer, they can make small apps pretty reliably.

So if I can ask ChatGPT or Claude to make an app, why would I use Scrappy?

* Scrappy is understandable.Using an LLM means going from an English prompt to pages of React code, which is too big a leap for non-programmers. They end up having to rely on the LLM to make changes, and are left helpless if the LLM doesn’t do the right thing. In contrast, Scrappy’s objects-on-a-canvas model is easy to understand, more humane, and acts a shared substrate where user and AI can collaborate on equal footing. And because it is less overwhelming, it’s more likely the user will pick up some programming skills.
* Scrappy is collaborative.All Scrappy apps are little shared worlds, persistent and with live updating — all for free. LLMs are mainly useful for creating static front-end-only web apps. And in Scrappy, apps can be edited by multiple users in realtime, whereas AI workflows are mostly “type, then wait” with little room for collaboration between humans.
* Scrappy is more fun!While typing a few sentences of English and seeing a full app appear out of nowhere still feels like magic, it quickly grows old when you’re waiting for minutes only to see the LLM misunderstood you again. In Scrappy, there is joy in tweaking things or remixing something. A spark of “ooh I want it to do this” and it’s only a few clicks and keystrokes away. A sense of creative ownership. And you can edit it together with friends!

## Scrappy vs HyperCard (and its successors)

HyperCardwas popular among Macintosh users in the early 90s, and is often held as an exemplar of enabling home-made software and end-user programming. Decades later, there have been a number of successors to HyperCard, both commercial (HyperStudio,SuperCard,LiveCode) and non-commercial (DeckerandWildCard, among a number of open-source remakes, most of which are abandonware). Most of these have been quite literal replicas of HyperCard, driven by nostalgia, down to the black-and-white graphics. None have been as successful as the original.

We wanted to create something in the spirit of HyperCard, rather than recreate HyperCard. Scrappy is different from HyperCard and its direct descendants in a few key ways:

* Designed for the Internet.Scrappy apps are easily shareable online with a simple link, whereas using HyperCard and most of its descendants is like being trapped in a virtual machine.
* A shared world.HyperCard stacks could be shared as a file with other users. Scrappy takes this to the next level by letting users edit and use apps at the same time.
* Modern UI conventions.Scrappy apps live on a high-resolution infinite canvas, with selections, copying, panning and zooming, frames for grouping, etc.
* Uses JavaScript for scripting.HyperCard and a number of its descendants use programming languages that aren’t in common use. JavaScript is the most common programming language in the world, is native to the Web and works well for a dynamic environment such as Scrappy.
* A larger palette of interactive objects.Many HyperCard-likes only support a few elements like buttons, text fields, and images. Scrappy supports more UI elements like sliders and timers, but also data types beyond strings: numbers, dates, and compound JSON objects.
* Reactive formulas, like a spreadsheet.The idea of “this value changes when that value changes” is familiar to many, and can be a stepping stone toward event-based programming, where the user has to think about state.

## Future directions

With our prototype, we think that we’ve been successful at proving the ideas and design principles that we started with. But there’s a lot more work to do. The number of Scrapps that can be built in a way that feel “Scrappy native” is still low. Much of the time, existing knowledge of JavaScript is required. To improve this, we need to continue work in both “lowering the floor” and “raising the ceiling”.

Lowering the floor means making things more friendly and approachable for people with little or no programming experience. For example:

* Improve code discoverability.We’ve made coding easier by presenting the names of objects visually on the screen, and listing their methods in the properties panel. But there’s a ton more than we can do. You should be able to click on objects to discover their methods and insert them in the code. Available names should auto-complete so you don’t have remember syntax and do as much typing.
* Improve debugging.You should be able to visualize relationships between objects, perhaps as arrows showing which objects read or modify other objects. Error messages should be better worded and show more information about what went wrong. You should be able pause and rewind execution. All of this while live collaborating on the app with a friend.
* Leverage AI.As we mentioned earlier, we don’t believe in having an LLM make an entire app, but we are interested in having it act as an assistant, directed by the user. Maybe you’d click on the canvas and ask the AI to “make start and stop buttons here”, or go to a text label’s “when changed” handler and ask the AI to write code to “show an error message if using non-english characters”.
* Make it even easier to share and remix. It’s easier to learn by inspecting and tweaking other people’ work than it is to start from a blank canvas. We imagine a public gallery where users can publish their creations, and other users can adopt and customize them for their own needs and preferences.
* Make Scrapps work well on phones/tablets.A hand-sized touchscreen is too small for editing Scrapps comfortably, but using them on phones should work well — this is not currently the case. The infinite canvas paradigm means that objects have fixed positions, which is a way simpler mental model layout rules (like in CSS), but means designs aren’t responsive to screen size. However, drag-and-drop web page design tools likemmm.pageandSquarespaceshow a way to handle this: simply show safe areas for mobile to the user.

Raising the ceiling means adding functionality and expressive power, letting users create more things with less effort. For example:

* Add support for collections. Currently, you can edit and store strings, numbers, dates, and JSON data, but you cannot store lists of them or make an editable tables, like in a spreadsheet. We also don’t have any kind of layout containers, like lists, grids, or stacks. Adding this would let authors express more things visually, and they wouldn’t have to resort to JavaScript knowledge and hidden state.
* Instanced frames.Frames let youselectively shareparts of your app, but that frame is fully synced in real-time across users. This is desirable in some cases and undesirable in others. For example, when sharing a form, each user should only see and edit their own copy. You should be able to share instances of the form, that still collects all the data in one place. Another example is a board game helper where there’s some hidden information and users should see some shared UI and some UI only visible to them.
* Tools for data processing.We’ve found ourselves wanting to use Scrappy to process tabular data. Things like: do the same operations to all rows, filter the table based on some criteria, etc. This can be done in JavaScript, but there should be a Scrappy-native way of doing this, where the data is shown.
* Better support for reuse.Currently, if you want to repeat an object or set of objects in your Scrapp, you have to manually edit them one by one, or write code to manage them. Instead, you should be able to define a reusable component and make instances that stay linked to the main component. Figma has this, PowerPoint has slide masters, HyperCard has card backgrounds, all to this effect. Further, these components could be shared across projects, or even with other users.
* Allow extending Scrappy.Some capabilities will be out of reach using Scrappy’s primitives. Currently, we are the only ones able to add new objects, but we’d want to open this up to more people. We expect this would require programming and web expertise, so it wouldn’t be something for a traditional engineer, not the typical Scrappy user.
* Clean up the conceptual model.Currently, some of the objects store data values, and some support event handlers like “when clicked” and “when changed” handlers. The current implementation is a bit arbitrary about this, which is not only confusing but also limiting. Common behaviors like editing, clicking, and storing data should be made more consistent and freely “mixable” — like theentity component systemsof game engines likeUnity.

## Conclusion

We believe computers should work for people, and dream of a future where computing, like cooking or word processing, is available to everyone. Where you can solve your own small, unique problems with small, unique apps. Where you don’t just rely on mass-market apps made by expert programmers. Where you share home-made little apps with family and friends.

Scrappy is our contribution to this dream. Each Scrapp is a live, persistent world, easily shared and remixed, closer to familiar productivity apps than alien developer tools. Like any vision, ours is incomplete, but we’ve grounded our explorations in a working prototype with examples of apps.

Try Scrappy! (desktop only)

We hope Scrappy will inspire you to further chase this particular windmill. If it does, please let us know!

Follow us on Bluesky for updates:John,Pontus

 

John Chang

jrcpl.ushello@jrcpl.usbluesky

Pontus Granström

pontus.granstrom.mepontus@granstrom.mebluesky,twitter

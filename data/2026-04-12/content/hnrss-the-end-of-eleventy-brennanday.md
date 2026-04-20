---
title: The End of Eleventy · brennan.day
url: https://brennan.day/the-end-of-eleventy/
site_name: hnrss
content_file: hnrss-the-end-of-eleventy-brennanday
fetched_at: '2026-04-12T11:34:30.938946'
original_url: https://brennan.day/the-end-of-eleventy/
author: Brennan Kenneth Brown
date: '2026-04-12'
published_date: '2026-03-04T00:00:00.000-07:00'
description: Build Awesome is a rebrand of 11ty/Eleventy, backed by a successful $40k Kickstarter. But this attempt to monetize static site generators repeats the same mistakes that killed Gatsby and Stackbit—and misunderstands who actually builds static sites.
tags:
- hackernews
- hnrss
---

Source(edited by the Author)

UPDATE: The Kickstarter has beencancelled and rescheduledfor a few months from now due to emails not being sent, ruining the project's "momentum" despite reaching their goal in a single day.

Yesterday, the Font Awesome team launched a Kickstarter for a new project calledBuild Awesomeand Build Awesome Pro, looking to raise $40,000 USD. And it has already reached that funding goal.

What is Build Awesome?Simply put, it's a rebrand of 11ty/Eleventy. Or rather, it isthe end of Eleventy.

I have personal stakes in this. 11ty is what my site, andthousands of others, are built and powered with. I support 11ty onOpen Collectiveand havecreated themesfor the framework. So how do I feel about this?

But before I get into why I (and many other 11ty devs) are not celebrating this hugely successful Kickstarter, let's first answer the question:What the hell is 11ty?Well, it's a static site generator.

Okay, but what the hell is a static site generator, and why does it matter for the literal future of the Internet so much?I'm so glad you asked.

## Part One: A Brief History of the Non-Dynamic

Static websitespredate dynamic content management systemswith their fancy backends and databases. In the early days of the Internet, all websites were mere collections of static HTML files.

Dynamic sites started with the advent of theCommon Gateway Interface (CGI)and later server-side scripting languages like PHP, ASP, and Ruby on Rails, along with database-driven CMS frameworks such as WordPress, whichpowers roughly 43% of the entire Internet.

Thankfully, the pendulum began to swing back towards static approaches with the rise of modern static-site generators. More secure, simpler hosting, and so much faster. Essentially,all you need to do is build a folder with some template languages and Markdown filesand you end up with a fully-rendered website. Here's the timeline:

* Jekyll(2008)was created by GitHub co-founder Tom Preston-Werner, dubbed "blogging for hackers" and repopularized SSGs, particularly with its integration into GitHub Pages, meaning any dev on GH could make a website instantly atusername.github.iowith the framework.
* Hugo(2013), five years later and written in Go, gained traction for its much faster build speed, making it suitable for large-scale static sites unlike the Ruby-on-Rails dependent Jekyll.
* Gatsby(2015)was a React-based SSG introducing the "content mesh" and leveraged GraphQL for data sourcing, aiming to be a modern, performant web development experience.
* Eleventy(2017), finally, positioned as an "anti-framework" SSG, offering a lightweight, flexible alternative to more opinionated tools.

## Part Two: 11ty: Origins

Eleventy was created byZach Leatherman, drawingdirect inspiration from Jekyll. But he wanted an alternative that leveraged the burgeoning Node.js ecosystem without imposing a rigid client-side JavaScript framework.

11ty does three things well: flexibility, leveraging JavaScript, and avoiding being a JavaScript framework. It supports multiple templating engines, allowing webdevs to migrate easily, and mix and match. Liquid, Nunjucks, Markdown, Handlebars, and EJS all within a single project. While Eleventy can use the vast npm ecosystem for the build process, it deliberately avoids dictating client-side JavaScript.

Who uses 11ty? NASA, CERN, the TC39 committee, W3C, Google, Microsoft, Mozilla, Apache, freeCodeCamp, to name a few. TheA11y Projectlaunched with Eleventy 1.0 and itslead developer Eric Baileynoted that nearly three years later, the site couldstill install and run from a cold start with no complications.

Leatherman was initially hired byNetlifyto work on Eleventy full-time, but in September 2024, 11ty moved toFont Awesome, with Leatherman joining their team. Now, in 2026, Eleventy is "Build Awesome", angled as the all-in-one site builder for Font Awesome and Web Awesome. But why?

I'm writing this because Build Awesome is trying to answer a question that I've seen first-hand plague this space of web development for years:

## Part Three: ...How the fuck do we make money off of this?

By 2015, a term was being codified: theJamstack(JavaScript, APIs, and Markup). The concept, popularized heavily byNetlify CEO Matt Biilmann, argued that decoupling the frontend from the backend, pre-rendering static HTML at build time and connecting to services via APIs, was the correct architecture for the modern web. It was fast, secure, and scalable by default.

The Jamstack framing opened a commercial opportunity. If static sites were the future, who would build the tools, the hosting, and the workflows to support them at scale? Gatsby became the darling of the VC-funded startup world. It promised a GraphQL data layer that could pull from any CMS or API at build time. By 2019, Gatsby hadraised $15 million in Series A funding; by 2020,a $28 million Series B followed.

Next.js, fromVercel, emerged as a full-stack React framework that blurred the line between static and server-rendered, competing directly with Gatsby. The companyreached a valuation of $9.3 billionin part due to this framework (but mostly AI). The market was crowded with well-funded, well-marketed options.

Gatsby Inc. raised overa total $46 million in venture capital, attempting to monetize through the"Gatsby Cloud"platform, offering specialized hosting and content management features. Despite huge investment, Gatsby Cloud failed to get the Silicon Valley "hockey-stick" growth and was ultimatelyacquired by Netlify in February 2023. Following the acquisition, Netlify announced the shutdown of Gatsby Cloud, and as of writing,Gatsby itself is deadand no longer maintained.

There was alsoStackbit, which aimed to be a "site builder" for various SSGs, promising to simplify the development workflow. However, the complexity of supporting a multitude of SSG and headless CMS combinations was actually impossible. Stackbit subsequently pivoted its focus to providing a "Visual Editing" layer for headless CMS, allowing content editors to see changes in real-time without direct code interaction. Perhaps unsurprisingly, they too wereacquired by Netlifyand then turned intoNetlify Createbefore quietly being sunset altogether.

And speak of the Devil! Companies like Netlify and Vercel have built businesses around hosting and deployment services for JAMstack applications. Their strategy is to support popular open-source SSGs (e.g., Netlify's support for Eleventy and Vercel's backing of Next.js) as"loss leaders" to attract users to their paid hostingand infrastructure platforms.

You see the problem, right? This model monetizes the infrastructure rather than the SSG itself, and the open-source projects remain dependent on the goodwill and strategic alignment of these larger platforms.

## Part Four: Leatherman's Open Source Dread

Leatherman, as the creator andBDFLlead maintainer of Eleventy, has been a vocal advocate for sustainable open-source development. He recently released an eye-opening podcast episode titled"How Eleventy Survived: Funding, Growth, and Open Source Reality". Leatherman spoke of the inherent struggle of maintaining a project that becomes too-widely adopted and critical infrastructure, with limited resources and significant personal sacrifice.

Maintainers face burnout and boundaries need to be put in place for any of this to actually be sustainable; the VC mindset of hockey-stick growth was antithetical to the open source ecosystem. Leatherman joined Font Awesome because he believed the company shared his commitment to "boring" (reliable and stable) technology and sustainable development, and it's clear that he recorded this podcast while actively planning the hopeful money-maker, Build Awesome.

## Part Five: We've Seen This Movie Before

With that, we've ended up exactly here. With Font Awesome deciding to attempt to monetize the static-site generator by rebranding it as an accessible alternative to clunky full-stack CMSes. Just take a look at the pro features:

* Collaborative visual editing(another way to say "headless CMS")
* Build-in-a-browser(no local dev setup, no terminal needed)
* Premium built-in templates and hosted import tools

Sound familiar? This is exactly what Stackbit was attempting to do before getting acquired and sunset. This is what NetlifyCMS was trying to do before becoming DecapCMS and barely having any support or popularity.

The truth is, there has been no successful CMS for static-site generators becausethe only people that give a fuck about creating static sites would much prefer to use a (free and local) IDE and a terminal.

This is the existential problem and Build Awesome does not solve it.

You are creating and providing tools (which I personally think would be amazing) to people who do not understand nor care for them. And in doing so, you are neglecting your base audience who is actually already using what already exists.

## Part Six: The Alternative Reality That Cannot Exist

Imagine if Build Awesome actually reached out to people who regularly make static sites. You know, the userbases onNeoCitiesorMelonLandor32-bit Cafe?

I'm unsure if the companies creating these products are totally ignorant and unaware of the IndieWeb or haven't developed a relationship with the movement on purpose.

I have a feeling the majority of the userbase would not be in support of something like this. Build Awesome looks and feels corporate, pro-capitalist, and commodifies one of the few remaining artistic hobbies that hasn't been overrun with consumerism and gear-acquisition syndrome.

## Part Seven: The Berry

In truth, I myself have started a business that has a near identical concept to Build Awesome.Berry Houseis my independent web studio aiming to create static websites for fledgling nonprofits and marginalized folks. I want to help onboard people and businesses into this space that typically only have their digital presence be their Instagram account or Facebook page, so that they can actually have autonomy, flexibility, and total freedom of design.

The difference is though that my model is pay-what-you-can, or pro bono. I developedCalgary Groupsfor a client and charged $5/hour for my dev work. I know the people with money are the ones happy to use Squarespace or WordPress indefinitely. The people with money are the ones far more apathetic to the fact they're on the corporate web.

## Part Eight: Conclusion

My point of writing this is that any attempt to monetize the open-source free space of static site generators has failed in the past, and is inherently paradoxical and antithetical.

My point of writing this is that the companies looking to monetize are far too focused on creating high-quality tools instead of focusing on doing the work and research into the"why". Into communicating the philosophy of SSGs in a way that would make them sincerely enticing long-term to non-technical people.

## Appendix: What Other Developers Have to Say

I decided to take to Mastodon to ask my fellow Eleventy devs how they feel about the the Kickstarter and rebrand. Here's what they had to say:

"I only care about and use 11ty. Don't know anything about the awesome stuff but doesn't feel like I'm their target audience. I worry 11ty will get sucked up and cease to exist in a form I want to use."

—Michael Harley

"I use Zola, not 11ty. However, this seems really weird. A company with plenty of resources is running a Kickstarter for a rebrand? Or am I missing something?"

—Ben Overmyer

"Terrible, nothing good survives in this world."

—Grigør

"Mixed feelings I suppose. Initially excitement and that's still there, but I've since seen folks voice concerns that I've now been dwelling on. I've backed Font Awesome, Web Awesome (didn't end up using it, got a nice deck of playing cards though) and now I gladly back Build Awesome. What this really means for 11ty I can't say, but should it go in a direction I don't like, then at least I can use the latest available version we have now, until the end."

—Christian Alder

"I feel like there could be clearer communication besides just launching a Kickstarter that seems to be for people who don't already use 11ty. I just don't see how this helps anyone besides just adding another subscription fee income source."

—🌸 melanie kat 👻

"Wait and see but sceptical. Yeah the name is not the best one — 11ty was short, easy to remember, has a history about the initial project."

—Nicolas (greenman)

"Part of the reason I liked 11ty was the broad community using it and the homegrown feel. The change feels like the community will become centralized and gatekeep-y? I guess time will tell, but there's some grief."

—nannnsss🌱🏴

"Mixed feelings. I don't like change. It's a lame name. I know folks gotta eat, but pro tiers make me queasy. (I really like that diner-style mug, though!)"

—Cobb

Elle the 11ty Possum
, illustrated by
David Neal

## Epilogue: The Mascot

Before I finish this already-very-long post, I wanted to take a second to write aboutEleventy's possum mascot, whose current iteration is aptly named Elle.

This mascot isthe brainchild of the late web developer James Williamson, who ran the websitesimpleprimate.comwhich sadly has lapsed in domain ownership.

I was introduced to James many years ago when I was learning about web development onLynda.com(now LinkedIn Learning). He was an incredibly talented and warm instructor, and one of my favourites on the site. He taught me so much of what I know about web accessibility, design, CSS, and static site generators. Hepassed awayfromALS in 2019.

I wanted to share this because I think it's important to remember who came before, and who give themselves selflessly. James understood this kind of selfless labour intimately. He gave generously to the web community until he couldn't anymore. The tools and lessons he left behind outlasted him in ways no Kickstarter can manufacture.

The courses James taught are no longer available on LinkedIn Learning, and I'm not sure they can be accessed anywhere now, but I will never forget what he taught me.

Enjoy this article? Give it a heart!

❤️

Get new posts delivered to your inbox via RSS. No spam or selling, ever.

Enter your email

Powered by Buttondown.

## Webmentions

### 20 Likes

### 10 Reposts

### 8 Replies

mb21

March 4, 2026

@brennan https://mastrojs.github.io is still independent!

And regarding DecapCMS, there is also the Sveltia rewrite. But yeah, definitely no money in that business.
Mastro: the simplest web framework and site generator

Brennan Kenneth Brown

March 4, 2026

@Tipa I use IndieAuth for my comment system, they support email, GitLab, Codeberg, and PGP keys. I'm sorry they don't have ActivityPub/Fediverse functionality.

Brennan Kenneth Brown

March 4, 2026

@Tipa how exciting! I have a full-write up of how I did mine here, but it is rather technical

 https://brennan.day/building-an-indieauth-comment-system-for-your-static-site/
Building an IndieAuth Comment System for Your Static Site

Tipa

March 4, 2026

@brennan I'll add my GitHub link then. And my itch.io, too -- just in case ???? As someone who is about to convert their website to static, following in the footsteps of @Aywren, I'm super interested in bolt-on comment systems too.

Tipa

March 4, 2026

@brennan not reading the article yet but WHAT? Was just about to launch a static web site...

Tipa

March 4, 2026

@brennan having read the article, I guess my website needs my Github link to comment, since it doesn't support (checks where I am) Mastodon links ????

I didn't know Font Awesome was in the mix. They were great back in the day, less so now.

Well, Hugo was also an option...

Denis Defreyne

March 4, 2026

@brennan I’m so glad I built my own static site generator ????

vga256

March 4, 2026

@brennan thanks for the writeup. i can't pretend to understand all of the subtleties, but it was helpful understanding why people preferred 11ty to other ssg's.

the part that 11ty and the rest, imo, haven't solved are the source trees. they're *massive*. big, complex and diffic…

## Related Posts

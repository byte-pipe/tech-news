---
title: The Slow Formation of Durable Software
url: https://newsletter.dancohen.org/archive/the-slow-formation-of-durable-software/
site_name: hackernews_api
content_file: hackernews_api-the-slow-formation-of-durable-software
fetched_at: '2026-10-08T23:39:56.824968'
original_url: https://newsletter.dancohen.org/archive/the-slow-formation-of-durable-software/
author: benbreen
date: '2026-10-06'
description: How a group of historians took years to imagine Zotero, the research application that would eventually be used by millions
tags:
- hackernews
- trending
---

October 6, 2026
 
 

# The Slow Formation of Durable Software

## How a group of historians took years to imagine Zotero, the research application that would eventually be used by millions

byDan Cohen

Screenshot of the first alpha of what we initially called SmartFox and then Firefox Scholar, before we consulted 1) a lawyer, and 2) an Albanian dictionary for other options, June 2006

* * *

Today, software can be created more or less instantly with AI, for a large user base or for yourself, for any purpose or for no serious purpose at all. As Robin Sloan enticingly puts it, just “ask for what you want.” The genesis ofZotero, the “free, easy-to-use tool to help you collect, organize, annotate, cite, and share research,” used by over 20 million people in dozens of languages and countless disciplines, is the opposite of this instant gratification. It took five years, not five minutes, to produce a rough initial prototype, and years after that to refine and expand the application. If AI had existed in the early aughts, we could not have accelerated Zotero’s conception, because we did not know exactly what we wanted, and so could not have written coherent prompts for an LLM. Instead, it took a great deal of time and collaboration to develop a clear vision for what Zotero should be. But that slow formation led to software that was durable rather than ephemeral, with a strong foundation that could be built upon. As programming increasingly becomes a caffeinated bender with magical bots, this measured pace and emphasis on communal thinking likely holds an important lesson.

On this 20th anniversary of Zotero’s launch on October 5, 2006, I will do my best to recount Zotero’s pre-history, what it took to conceive, design, and build the 1.0 release. It’s a story about a bunch of historians who were knowledgeable about emerging technologies and knew how to code — as a secondary rather than primary skill — and who spent a lot of time, some of it wasted time, at a big table chatting. That conversation eventually coalesced into ideas about the future of scholarly research.

As the well-worn saying correctly asserts, failures are orphans while successes have many parents, and Zotero is no different. A proper accounting would require far more than this relatively modest post, and what follows is, unsurprisingly and necessarily, from my own perspective. My contributions to the success of Zotero date largely to the years before and immediately after the launch of the 1.0 beta, when I was an Assistant Professor of History and Director of Research at the Center for History and New Media at George Mason University. This institute is now the Roy Rosenzweig Center for History and New Media (RRCHNM), named after the visionary historian who founded it and really the entire field of digital history. Roy tragically passed away in 2007 when he was only 57, and his illness and death hang like a dark cloud over this narrative.

I succeeded Roy as the Director of RRCHNM, and from that point on, my day-to-day work on Zotero ebbed, as I handed off responsibilities to other, more capable people: Zotero’s talented lead developer Dan Stillman; Sean Takats, who has deftly overseen the massive growth of the project for much of the last two decades; many others in the orbit of RRCHNM and the non-profit Corporation for Digital Scholarship who handled outreach, support, and countless details; an international team of developers and volunteer contributors; and still more colleagues, only some of whom, regrettably, I’ve been able to highlight below. On this anniversary, you should visitZotero’s Credits and Acknowledgments pageto honor the full slate of productive collaborators. Sean Takats also hasa great post on the continual improvement and influence of Zoterosince its launch.

I’m proud to have been there at Zotero’s origin and early years, and to have helped bring it into existence. At the college graduation of one of my kids this past spring, an attendee who had heard that I had been involved with Zotero hugged me, unexpectedly and at length, in appreciation. No one has ever done that for my scholarly writing, or ever will.

Members of the Zotero team in late 2006. Roy Rosenzweig, months into chemotherapy, is kneeling at center; he had just gotten the Zotero license plate for his Prius to the great delight of all of us. Standing, L-R: Sean Takats, Trevor Owens, Josh Greenberg, me; Kneeling: Kari Kraus, Roy. Photo credit: Sharon Leon

* * *

Software development was not originally on the docket for the Center for History and New Media. With its now delightfully retro, turn-of-the-century name —new mediarather thandigital— it was largely in the business of developing sites for the web, which was just a few years old in 1994 at the center’s founding. I joined RRCHNM in January 2001, as a newly minted Ph.D., to work on a project on the history of science.

Alongside another new Ph.D. who had studied the history of technology,Jim Sparrow(now a history professor at the University of Chicago), we built a website calledECHO: Exploring and Collecting History Online, funded by the Alfred P. Sloan Foundation. “Collecting” was a new gerund for the center, and hinted at an expansion of our methods. Since science was growing exponentially but the number of historians of science was not growing at all, we thought we could use the web to help scientists self-document their work. For this, our site needed to be interactive, so we started to tinker with “tools” — small web apps — that could not only display history online, but also allow it to be uploaded, sorted, and archived.

Toward this end, I wrote several applications inPHP, then swiftly becoming the standard programming language for web applications, because it commingled well with HTML, the web’slingua franca. One of these apps, Web Scrapbook, got a bit of traction, especially in classes, since it allowed students to capture images, links, and other resources from the web browser into a collection that could be shared with their classmates and instructor. Users clicked on a browser bookmark, which had a small bit of JavaScript embedded in it, to select the desired items and pass the data to the application. Web Scrapbook was not, shall we say, arigorouspiece of software — my initial version sent passwords, unencrypted, across the internet — and it paid only basic attention to metadata and other scholarly information that would be needed to assist in writing an article or book, and to form a proper footnote.

Be forewarned, ye who dare log into my web application c. 2002 (screenshot of the Web Scrapbook landing page)

Fortunately, at the same time, another colleague at the center,Elena Razlogova, who was the webmaster at RRCHNM while pursuing her Ph.D. (and is now a history professor at Concordia University), was working on a more scholarly application called Scribe, for taking notes and storing citations. Elena used a database application called FileMaker to build Scribe, which users downloaded and ran on their personal computers.

Elena Razlogova’s Scribe application, c. 2002

Scribe became popular among fellow historians as a good, free replacement for commercial software like EndNote. It ran locally on a Mac or PC, and had the organizational, search, metadata, and annotation capabilities that Zotero would later expand upon. Elena made several improvements to Scribe in the first few years of the century, as I worked in parallel on Web Scrapbook.

* * *

So by 2003, we knew how to write web apps and standalone apps, both helpful but both also naggingly insufficient. We were now starting most of our research on the web, and we thought that any robust research application of the future had to be connected to this environment where primary and secondary sources increasingly resided, either as metadata in library catalogs, or as full objects if they had been digitized. What we really needed was an application that had some aspects of Scribe and some aspects of Web Scrapbook: a full-fledged research tool that could exist independently of the web, but be fully cognizant of what was going on in the web browser, aware as the researcher surfed across digital collections and library catalogs.

On November 29, 2003, Roy asked Elena via email what she would like to do for a next version of Scribe. Roy,Tom Scheinfeldt, another recent history Ph.D. who had joined us to work on theSeptember 11 Digital Archive(now a professor of digital humanities at the University of Connecticut), and I were working on a grant proposal for a new stage of ECHO, and we thought we would include some improved software tools as part of that. Elena wrote back on December 1, 2003:

Roy--Here’s what I'd like to do:setup to connect to online bibliographic databasesmore citation styles (at least APA and legal)setup to add custom citation stylessetup to add more fields and types of referencesuser/password setup to share and co-edit online bibliographies/notessetup to work locally then publish all or parts of bibliographies/notes online (like ical)foreign language supportbetter manualonline discussion list (using the software marty had installed)best,elena

This was a good list. Tom wrote back that “it would be nice to update and ‘webify’ Scribe.” A good word:webify. Elena, Tom, Roy, and I agreed on this essential next step for Scribe: we needed to find a way to put itinto the web browser, like Web Scrapbook, while retaining Scribe’s provenance as a detail-oriented research tool. As I latersummarized our holy grailin a journal article:

We wanted the best of both worlds: the best parts of standalone applications and Web applications. We envisioned a tool that lived in the browser and that was very smart about what was going on in the browser, including the recognition of scholarly metadata and objects, and that could interact with elements both on the desktop, such as word processors or other programs, and via standards, services, and communication protocols to other tools and resources across the Web.

But how to merge these disparate worlds? That was not at all clear in 2003.

* * *

At RRCHNM, we had a large whiteboard with vague ideas, some of them serious and some of them silly, visible to everyone, just in case it gave someone a spark. Over group lunches, the faculty and staff at the center would often talk about new tech we had heard about, and muse about whether we could apply that tech to historical research. Our collective was growing quickly. In the summer of 2004, we were joined by, among others,Josh Greenberg, who had a Ph.D. in science and technology studies (and is now a program director at the Alfred P. Sloan Foundation); Sharon Leon, who had a Ph.D. in American history (and is now the Co-CEO atDigital Scholar); andSimon Kornblith, a young teenager (and son of a historian and friend of Roy’s) who was truly gifted at software development and many other things. (Simon would go on to get a Ph.D. in Brain and Cognitive Sciences at MIT, write important AI papers with future Nobelist Geoffrey Hinton, and work at Anthropic.)

One project that caught our eye was a spinoff of the open-source Mozilla web browser that came to be known as Firefox. That summer Firefox was in beta, and it would be officially released later that year. The new browser had much to recommend it. The original Mozilla browser, descended from Netscape and the early days of the web, had, over time, become slow and bloated. Firefox, on the other hand, was fast and lightweight. But much more exciting was how Firefox embraced and foregroundedXUL, which sounds like an alien god from a 1950s sci-fi movie, but stands for XML User Interface Language. It dawned on us that with XUL, you could— sweet mercy— customize and extend the web browser in any way you wanted.

The day Firefox was released to the world on November 9, 2004, Josh and I — always the earliest of adopters — downloaded it and started to tinker with its possibilities. That night I wrote an email to Josh, Elena, Tom, and Roy with the subject line “Firefox + XUL + AWS = OpenScribe/Online Scribe?” The AWS I was talking about was not the future cloud computing service from Amazon, but an API Amazon provided to retrieve information about books. I thought we could use a combination of a Firefox extension written in XUL and services like Amazon’s to “automatically load citation info into the fields.” Josh wrote back just before midnight:

Please pardon my language when I say "Holy crap, that's cool!"The possibilities are astonishing - it looks like there are XPCOM wrappers for mySQL that would allow us to access a database (either remote or local), entirely replicating Scribe using a relational database (or, offering a custom "Scrapbook Browser.") Alternatively, we could chuck the database and use a Firefox interface to navigate Scribe XML data directly. Regardless, immediate cross-platform compatibility.Either way, we could use a combination of Amazon and Proquest/ISI Citation Index to make itmucheasier to create bibliographic objects, and at the least create a Mac version that would use either Cocoa or more basic scripting to allow citation from within a word processor...Neat-o!

With an open-source database instead of FileMaker to store bibliographic data and notes, and with a Firefox extension of the proper composition, all of the ingredients were within reach to create the research tool of our dreams.

That winter, with Roy as the principal investigator and Josh and me as co-directors, we applied for a grant from the Institute of Museum and Library Services. The abstract from that grant, which we titled “SmartFox: the Scholar’s Browser for Digital Collections,” displayed our new level of clarity, although we still envisioned what we wanted to make as a “set of tools” — such as the item capture tool from Web Scrapbook and Scribe's note-taking interface — rather than one app:

The web browser has become the primary means for accessing information, documents, and artifacts from libraries and museums around the country and the world, thanks in large part to the tremendous commitment these institutions have made to bringing their collections online (as either simple citations or complete text and images). Unfortunately for scholars, while tens of millions of dollars have been spent to create digital resources, far less funding and effort has been allocated for the development of tools to facilitate the use of these resources. The browser remains merely a passive window allowing one to view, but not easily collect, annotate, or manipulate these objects. Moreover, from the user’s perspective individual library and museum collections remain just that—separate websites with distinct designs and different ways of displaying their information, making traditional scholarly practices of bringing together and studying objects of interest from across these collections unnecessarily difficult.

SmartFox, a set of tools incorporated into popular, open, and free web software, will address these major problems by creating a web browser that is “smarter” in two key ways. First, one tool will enable the browser to intelligently sense when its user is viewing a digital library or museum object; this will allow the browser tocaptureinformation from the page automatically, such as the creator, title, date of creation, and copyright information. Second, another tool will store andorganizethis information, as well as full copies of items and web pages (not just their citation information) if so desired by the user and permitted by the institution’s site, allowing the user to sort, annotate, search, and manipulate these individualized collections created for scholarly purposes. Critically, all of this will occur within the web browser itself, not in a separate, standalone application; the web browser will be used not just to discover information, but also to collect, organize, and analyze scholarly materials.

(Zotero did indeed begin its life with a name, SmartFox, that was a riff on Firefox, and our potential trademark violation somehow got worse when we rebranded the app as Firefox Scholar in September 2005. More on that later.)

Even before IMLS funding had come through, Simon had started working with David Norton, another software developer, on a prototype of SmartFox. By July 2005, they had produced a very early “0.0.1” version, with the metadata panel on top, the notes field below, and the folders on the left; all of these would later be combined in a much better unified drawer.

SmartFox version 0.0.1 screenshot, July 27, 2005

Simon, who was paying attention not only to public releases of Firefox but also to the core code development itself, pointed out that summer that Mozilla planned to include “mozStorage” in Firefox, which could act as an interface to a database. (Firefox eventually included SQLite as its native, open-source database.)

Also in the productive summer of 2005, we hired Dan Stillman, a friend of an RRCHNM staff member, to help us with the center’s burgeoning set of servers and increasingly complex digital platforms. Dan fixed so many accumulated issues so well that by January 2006, Josh and I had asked him to join Simon and David on the dev team. (To this day, Dan is the lead developer of Zotero; what a run.) We also addedSean Takats, who had both a doctorate in French history and extensive technical experience, and became Zotero’s longstanding director in addition to his academic career in history and digital humanities;Kari Kraus, our technology evangelist, who became a professor in the College of Information Studies and the Department of English at the University of Maryland; and, later that year,Trevor Owensas our outreach coordinator. (Trevor is now the Chief Research Officer of the American Institute of Physics.)

Members of the Zotero team in late 2006. Standing, L-R: Simon Kornblith, Sean Takats, Trevor Owens, Dan Stillman, David Norton; Kneeling: me, Roy Rosenzweig, Josh Greenberg

With this team in place, development accelerated. In roughly six months, the developers produced a far more coherent design and much-improved functionality, as you can see in the June 2006 screenshot at the top of this piece. With summer always being a busy time at the center, as teaching responsibilities paused for some members and everyone focused on grant projects, the code base iterated rapidly and everything aligned for a fall 2006 release of the 1.0 version.

There was just the pesky issue of the name of the thing. I’m afraid we probably spent as much time in the summer of 2006 rethinking the name as we did fine-tuning the design. We had, by then, long abandoned “SmartFox,” and were calling the software “Firefox Scholar,” but we heard from a lawyer that any branding with “Firefox” in it would be problematic. We were also wondering whether this software was just for fancy “scholars” — it seemed to have broad applicability. We kicked around countless replacements, many of which are howlers in retrospect. Withholding who proposed each of these alternatives to protect everyone involved from embarrassment, we considered iScholar (these were the days of iPods), Scholr (these were the days of Flickr), Citopia, FreeCite, CiteHound, DynoCite, FireScribe, FireHoard, MetaFox, ClioFox, and every pun you could think of involving fires, foxes, and footnotes. The domain name also had to be available; it’s amazing how many of the bad names we came up with had somehow already been registered by other fools.

Late in the summer of 2006, as time was running out, we thought we would move beyond English, taking a cue from other new projects at the time, like Ubuntu, a Linux distribution that used a word borrowed from a family of African languages, and Wikipedia, whose name derived fromwiki, the Hawaiian word for quick. Our colleague Mills Kelly, a historian of Eastern Europe, made the suggestion to consult an Albanian dictionary, which we thought was a good idea as it was unlikely that any other Americans had ever done so, for any reason, much less to find available domain names. We quickly selected the Albanian word for “to learn well or master,”zotero, which was memorable, sounded like it could be pronounced easily in many languages, and was still available with any domain ending we wanted (we registered .org/.com/.net).

On August 29, 2006, I sent Dan Stillman some Photoshop files with a Zotero logotype I created, set inEurostile. I can neither confirm nor deny that this logotype may or may not have been inspired byZpizza, a restaurant near where I was living in Silver Spring, Maryland, which also had a red Z at the front but used Futura Bold, a travesty that led to the restaurant closing soon thereafter. The Zotero font has changed slightly, but the logotype has survived to this day.

The first logotype for Zotero, August 29, 2006

* * *

Twenty years ago, I posteda one-sentence notificationof the initial beta release ofZotero, asking people, a bit manically, to “try it out!” Try it out they did. We had 60,000 users of this new open-source research assistant within a month. The numbers escalated rapidly from there, and additional funding soon followed from the Mellon Foundation and the Alfred P. Sloan Foundation that allowed the app to sync collections across research teams and, eventually, to become independent of Firefox and work with other web browsers.

The library I now lead, like most research libraries, has workshops that teach students and faculty how to use Zotero. It’s part of the fabric of academia, and is widely used outside of the academy as well. Zotero is great, solid software. It continues to evolve in concert with the needs of its enormous user base. Its value, slow to emerge from the collective thinking of a friendly cohort of historians, has been incredibly durable. May it last another 20 years, or more.

Zotero 10.0, released on August 17, 2026

* * *

 
 Don't miss what's next. Subscribe to Humane Ingenuity:
 
 

 Email
 
*

Subscribe
---
title: Changelog - Kagi Search
url: https://kagi.com/changelog#11296
site_name: hackernews_api
content_file: hackernews_api-changelog-kagi-search
fetched_at: '2026-08-21T19:25:05.452248'
original_url: https://kagi.com/changelog#11296
author: speckx
date: '2026-08-21'
description: Better search results with no ads. Welcome to Kagi (pronounced kah-gee), a paid search engine that gives power back to the user.
tags:
- hackernews
- trending
---

# Changelog

Subscribe to RSS
 | Email us 
support@kagi.com

Browse Changelogs

## August 21st, 2026 - A new Stocks widget and a better everyday Assistant experience#

## Kagi Search

#### Bringing Stocks up to speed

We've revamped our Stocks widget. It should appear more often when you need it. It can now display information about exchange-traded funds in addition to stocks. Most importantly, it now features a price chart, with animations between time windows that instantly contexturalize how big the price fluctuations you're seeing are compared to the wider story:

As well, we'veadded a settingfor removing paywalled links from search results automatically.

## Kagi Assistant

### Everyday use just got smoother

Richer messagesUser messages now render links, Markdown, and LaTex.#6674@oxlvlnle,#3283@EvacuatedTerminal

More powerful searchSearch across all your threads, sort by recency or alphabetically, and start with/to filter by folder.

More control with calmer settingsNow you can choose whether temporary threads stick around for 24h, 7 or 30 days. All within a calmer, easier-to-scan settings experience.

## Other improvements and bug fixes

### Kagi Search

* Direct URLs for search pages with our built-in lenses are now easier to use, with names replacing numbers:https://kagi.com/search?lens=forums
* Shortcuts should not trigger with modifiers held#9385@poacher2k
* kagifeeedback xss vuln tag fix#10767@unknown
* Upstream connect error or disconnect/reset before headers. reset reason: connection termination#10680@TheToby
* Select text and Search in Assistant#11242@mb
* Homepage Companions - Random or Rotate#9077@Anonymous12
* Extract API returns emptydatafor an entire batch when one page times out#11176@fredcy
* Currency conversion widget does not handle official name of currency#11175@Keli
* A way to find similar websites#1152@Protech
* Blocked domains are used as sources in Quick Answer#11257@bausauce
* "CHATGPT" Wikipedia article is flagged as slop#10192@fxgn
* Surveillance Watch for play.google.com goes to a page about Zalo#9146@pma_snek
* Assistant no longer decodes URL encoding from !ai bang#11096@arijan

### Kagi Assistant

* Ability to export all Assistant chats in one go#5221@Thibaultmol
* In Assistant, add an option to require ⌘+⏎ to submit a prompt#6110@dudeofawesome
* "Click to Expand" on "Thinking" Section#8004@KagiFeedbackDuder
* Assistant: do not close thinking block if user opened it during extended thinking#6675@DomW
* Assistant prompt code fence syntax highlighting#4775@slater
* FIXED - !ai bang - Query not working#11077@fanged_bagful
* Prevent Search Engine Indexing of Shared Assistant Threads#7867@Hanbyeol
* Web Search toggle state not maintained between app switches#11140@ryonic
* Improvement to code snippet input#6254@Leward
* Choppy animation in Assistant app#11134@Temanor
* Assistant prompt code fence syntax highlighting#4775@slater
* Speech-to-text doesnt support pauses in Android Assistant app#11265@jeroenpelgrims

#### Assistant Mobile Apps

* Keyboard shortcut preference to submit prompts on iPads with connected keyboards
* Back swipe on left side of Kagi Assistant interferes with Android guestures#11126@mb
* After opening Kagi Assistant, back swipe on the right side closes the app#11127@mb
* Choppy animation in Assistant app#11134@Temanor
* Web Search toggle state not maintained between app switches#11140@ryonic
* Cannot Login Kagi Assistant 1.0.4 on iOS#11146@hirsheykiss

### Kagi Translate

* Kagi Translate Reloads the page when using website translate#10852@tijol
* Kagi Translate extension RSS feed 503 error#10831@Albi
* Translate extension context menu options don't work everywhere#10813@WorstWizard
* Alternative-translations request payload has blank "context" string in new update#11278@Drexont
* Regression: saved presets do not automatically apply context to translations#11218@Drexont
* American alias for English (US)#11143@mb

## July 30th, 2026 - Kagi Assistant on the go and design refinements for Search#

## Announcing the official Kagi Assistant apps

Kagi Assistant is now available as a native app foriOSandAndroid!

Ask a question, explore the web, work with files, conduct in-depth research, or choose from leading AI models, all from your phone. Your threads and Custom Assistants stay with you, so you can pick up wherever you left off.

These are the first steps towards delivering a fantastic Kagi Assistant experience on mobile, with much more to come.

Download it now:

* App store:https://apps.apple.com/app/6755965340
* Play store:https://play.google.com/store/apps/details?id=com.kagi.assistant

Give it a spin and let us know what you think!

### Report responses directly from Kagi Assistant

You can now report an assistant response without leaving the conversation. Hover over any assistant message and select the thumbs-down button to open the feedback form, where you can report issues for reasons ranging from UI bugs to harmful content.

Note that when you submit a report, the full thread is shared with Kagi for review. The report and its associated copy of the thread are automatically deleted from Kagi’s review records after 30 days.

### Export or delete all your threads

We've also added important controls, so you can now export all your threads or permanently delete them at once fromSettings > General.

## Kagi Search

### A sharper search experience

We’ve polished the search results page to make its controls easier to find and understand. From the filter bar to domain-related options and menus, these updates bring greater clarity and ease of use to the features you rely on most.

### Exchange rates, right in your search results

Next up in our broader effort to improve search widgets: currency conversion. Comes handy when you’re planning a trip, shopping abroad, or simply want to keep tabs on exchange rates.

## Other improvements and bug fixes

### Kagi Search

* Fixed several animations that didn't respect the system'sprefers-reduced-motionsetting
* 'Open first result' shortcut suggestion tries to escape double-quotes#8752@craftypersimmon
* Fake 1337x domain#9279@fxgn
* Dice Number getting cut off in the thousands#10964@Flossiii
* Some Kagi lenses not working for me in Kagi search#10970@Fearce
* NSFW results when searching for "xteink black vs white" while safe search is turned on#10905@ciccero040
* Incorrect definition of "socialism"#10988@thoroughly
* Nothing triggers the weather widget when the interface language is set to German#4612@laiz
* Cannot Manually Select Location in Privacy Settings#11005@iamjameswalters
* More and share buttons disappeared - Mobile DOM#10957@NyraSyn
* Slopstop blocks whole domains#11039@kslays
* Unable to report AI image slop on mobile due to popup closure#11066@Hanbyeol
* Kagi adding extra {{{s}}} in bang redirect when no query#9885@jadams9
* "Profile not found for ki_research" error when using??shorthand#11020@paying_customer
* Kagi Knowledge answer for "Labour Day 2025" gives wrong date#8713@wanion
* Delete recent language option#8549@ten
* Stopwatch should not start from searches like0424:2422#6061@xfhrnozxqnrnqrsvntp
* [Android] Quick Switch Doesn't work#7695@cr0ntab
* Save a round trip: Advertise HTTP/3 support in an HTTPS DNS record#10829@drrlvn
* Searching for<script>returns no results#11117@Bonarc

### Kagi Assistant

* Camera button in assistant#5261@Arnaud
* Assistant error "something went wrong..." when "web access" is selected#6687@Nyaa
* Gemma 4 31B failing to read images#10947@Dustin
* Assistant: Remove whole history#6971@Wanja
* Didn't like a Quick Answer response? post it here#9082@Thibaultmol
* Hourglass design is bad#11034@shurik
* FIXED - !ai bang - Query not working#11077@fanged_bagful
* Temporary threads don't actually get removed#10780@foxberg34

### Kagi Translate

* Kagi Translate reloads the page when using website translate#10852@tijol
* Dictionary now shows language-specific grammar details, starting with Czech animate/inanimate nouns
* Proofread no longer suggests changes to text that was already correct, such as de-capitalizing German nouns
* Translations no longer occasionally come back untranslated
* Translations keep proper typographic punctuation instead of straightened quotes
* Alternative translations now work when selecting part of a longer text
* Double and triple-click selection in the translated text works as expected, and the alternatives panel no longer flickers while loading
* "New version available" banner appears less often and supports dark mode
* Reset-All Button for Translate#10999@erakagi
* Document Translate for Typst#11098@weriomat
* Palestinian Arabic in Translate#11006@zsoltsb
* Phonetic Translation Placement#10699@dwahdany
* Myanmar alias for Burmese#10495@mb
* Translation History panel cannot be closed in Brave (Windows 11)#10997@vshlapakov
* Prompt being read prior to translated word#10974@kagifeedback-1xxkg
* Kagi Translate Audio Broken#10923@levers

### Kagi News

* Kagi News no longer showing births and deaths Today In History#11026@eggnog_90241
* Content filter should backfill removed articles with the next available ones#10828@roy_carver023
* Clearer feedback door#10919@Coldcartcold
* Fast font option#10001@broken665
* RTL content is displayed in the wrong direction when the interface language is LTR#10298@maxmellen

## July 2nd, 2026 - Heads, tails, and an AI toggle#

## Kagi Search

### New controls to completely turn off AI-based features in search

We've added an option to disable access to AI features in search, undersettings/ai.

We're also planning to add this option to onboarding, so new users can personalise their Kagi experience from the start.

It's finally here! We believe that Kagi's application of AI should always beuseful- there when you'd like it, and never when you don't, and always respecting your privacy.

This took us some time to navigate the right way to communicate this option. We did not want to create a confusing narrative as a company adding a toggle while continuing to invest in AI features elsewhere in our portfolio. But in the end, we want to stay true to putting you in control ofyoursearch engine - so here you are!

We deeply thank the community for their feedback and patience.

### Flip coins and more sports widgets

By popular demand, our dice widget has gained the ability to roll dice with any number of sides. We're not sure what kind of games you're playing that need d7s, but we support them now.

We also added support for flipping coins, which are really just two-sided dice when you think about it:

We've added a set of switches onhttps://kagi.com/settings/more_searchso you can disable any of our widgets you don't want to see. The toggle descriptions include links illustrating the widgets' capabilities so you understand what you're turning on or off; go check it out!

## Orion browser ✴︎

This week, we’re launchingOrion 1.1 for macOS, one of the most significant updates in our history. This version is built around three major new features (in addition to 170+ smaller improvements and bug fixes).

A New Interface ✴︎When Apple releasedLiquidGlass, the reception was mixed—even within our own team. The demand was there, but we weren't ready to just copy-paste what Safari had done. They had even removed compact tabs!So, we created our own implementation.

Containers ✴︎Just like Firefox, we now offer containers. What are they? Each tab becomes completely isolated from the others: total privacy and the ability to log into multiple accounts on the same site from the very same window!

A Personalized Browser Border ✴︎The current trend is an elegant, transparent border seen on many browsers. The problem is, they don't match Apple's design language. So, what did we do?

As we usually do: we made it an option! And we took it even further: transparency, solid colors, gradients, and even an automatic color-match with the website for total immersion.

This option is exclusively available to Orion+ subscribers.

Orion+Orion is your free browser, but we offer asupport planto maintain the independence that guarantees your data is not, and will never be, sold to advertisers—or worse.

We have a dedicated website where you can download all the versions we currently support, as well as any we may support in the future (macOS, iOS, iPadOS, Windows, and Linux):https://orionbrowser.com

## Kagi News & Kagi Translate

Kagi NewsandKagi Translatehave both been successes that took us by surprise.

Kagi News users from all over the world loved being able to read their news in the language of their choice, stress-free, and even add new topics.

Kagi Translate users loved the contextual features that provide a spectacular translation quality — far beyond what typical machine translation offers.

But these unexpected successes led to a massive spike in our costs for applications offered for free.

As a result, we have temporarily removed translations and left access to the articles’ original languages as well as English. Kagi Translate will be back in the coming days as a subscription-based service.

Thank you for your patience and your trust 🙏 we hope to have everything up and running again very soon!

## Other improvements and bug fixes

### Kagi Search

* Missing/nonfunctional settings for Kid account#10803@Acratoseek
* Searching for "@import" (with quotes) breaks search#10866@RandallLeeds
* Quick Answer followup question hangs#10257@MustafaD
* Any search that begins with "what is" shows translation widget before results#10868@unknown
* Missing/nonfunctional settings for Kid account#10803@Acratoseek
* Irrelevant trigger of translate widget#10865@dreifach
* Dice Rolling Widget fails with modifiers without space#10834@adammakesfilm
* False trigger of events/sports widget#10908@dreifach

### Kagi Assistant

* Kimi k2.6 retired in favour of k2.6 Code?#10832@TimJay
* Allow customization of font size in Kagi Assistant#8863@the_fork
* Kagi Assistant Code blank screen#10844@JacksonNunley
* Summarization of MP3s fails#10804@YetAnotherUser
* The stop button in assistant often doesn't work#9938@fxgn
* Models specified in URL parameters are overridden by the Default Assistant setting#10084@ining
* Export to Markdown of large assistant thread omits first half#10858@jonassmedegaard
* Include menu option to "create new folder" when filing an assistant thread#10879@lolroger
* Even when the input box is expanded on Kagi assistant, the enter key submits the request#10851@gm
* Assistant v2 Ignoring Personalized Results#10864@Dustin
* Restore button for custom instructions for Assistants#9502@Felensis
* Kagi Research Assistant misreads table from website#10901@ionpac

## June 16th, 2026 - Search widgets catching up, Assistant starts fresh#

## Bringing search widgets up to speed

We’re starting a broader effort to improve our search widgets! First up: sports scores and dice rolling.

Sports scoresnow show up in a sidebar next to search results, so you can quickly check upcoming games, live scores, and recent results,just in time for the World Cup.

And we’ve alsoadded dice rolling supportfor all you gamers out there, in case you ever need to rolla d20,2d4 + 2, or perhaps even8d6.

## The new Kagi Assistant is here

Over the last few weeks, we’ve been rolling out a new Kagi Assistant experience. Most of you are already using it, and today we’re officially retiring the old assistant.

This is more than a visual refresh, we rebuilt the Assistant experience around a new layout, smoother web and mobile use, and a lot of UX improvements that add up quickly.

And just as importantly, this gives us the foundation we need for the next set of Assistant improvements we’ve been working towards.

Note: there is one notable change - folders have replaced tags. This means each thread can now belong to only one folder. We appreciate this is a downgrade for users who relied on multiple tags per thread, and we don’t want to handwave that away. We made this tradeoff because folders give Assistant a simpler, more predictable organisation model, and because multi tag usage was relatively low: about 20% of active accounts used tags at all, and appx 4% had any thread with more than one tag.

Still, for those affected, we understand this change may be frustrating. Thank you for bearing with us as we build towards a stronger Assistant experience!

## Kagi Translate update

We've paused free access to Kagi Translate while we sort out running costs, so you'll need to be signed in to use it. If you have an active subscription, Translate still works. Sign in on translate.kagi.com or in the mobile apps. We share more details on this decision in thisblog post.

## Other improvements and bug fixes

### Kagi Search

* Different output formats for Wolfram Alpha results#3183@mm00
* Incorrect lens default#10796@maus986
* Wikipedia widget shouldn't show disambiguation pages#10646@Numerlor
* Chaining from one image to another in image search#10458@howtaobrowncow
* Unrelated Wikipedia widget results#10655@kpj
* AI image filter fails on query "porcelain horse toilet"#10318@Recast
* File-only queries do not create corresponding title and subtitle#10130@dreifach
* Wikipedia LaTeX images doesn't render#10659@3top1a
* Lenses don't appear to support queries anymore#10419@arizvisa
* Wildcard suffix domains don't work in lenses but do in a normal search#10438@decayingposture
* Trailing wildcard on path-prefixed domain breaks Lens results#10666@Dannn404
* Quick answer references should link the entire trigger element#10781@mootari
* Account 2FA UX broken#10760@gntlrm
* Incorrect lens default#10796@maus986
* Cloudflare 404 - Kagi Turnstyle (Vivaldi Browser)#10809@NyraSyn
* Assistant threads were wrongly moved to Temporary#10100@eltaco

### Kagi APIs

* NEW: Extraction now keeps links from the original document, to enable deeper crawling flows.
* NEW: Related searches is now part of the API responses, with more metadata than the v0 version where applicable.
* NEW: Per-key cost tracking is now enabled. You can select a key in the usage page to see the specific key cost attached. (Cost tracking only available from when we deployed, historic data is not present.)
* Fix: Extraction is nowfasterand more reliable.
* Fix: Personalization rule types are now correctly validated with the doc types.
* Fix: Various other internal improvements for a more stable experience.

### Kagi Assistant

* Regression: new assistant scrolls to bottom when inference completes#10648@spiffytech
* The new Assistant does not let me edit the output from the model.#10670@Fernold
* Japanese IME: Enter key submits message instead of confirming composition#10707@n22z9y28vh
* New system prompt causing regressions esp. in no-search mode, and ignores /system_prompt_overwrite#10684@igakagi
* New assistant doesn't respectprefers-reduced-motion#10711@magiruuvelvet
* New Kagi Assistant does not remember sidebar on refresh#10727@emptyjar
* New Assistant: Undo File Type Restrictions#10721@AzuraFilth
* Assistant converts CSV uploads into markdown#10647@fxgn
* Specific code snippet returns 403 Forbidden error#10689@Fusl
* Assistant Not Searching Web or Citing Sources Despite Web Sarch Toggle Enabled#10657@cmart
* Kagi Assistant Does Not Reliably Read Larger Documents/Attached Files#10516@aeiro
* Assistant can't reach github files#10697@Numerlor
* Assistant does not scroll on output#10742@emptyjar
* References do not export, Markdown or JSON.#10741@relaxos_palaiologos
* Images inside Kagi Assistant responses do not appear#10296@MustafaD
* Assistant sidebar does not stay closed when resizing the window#10762@emptyjar
* Pressing 'Enter' key should confirm deletion dialog in Kagi Assistant#10793@kray
* Enter key does not submit message on iPadOS#10708@n22z9y28vh
* New assistant models from Anthropic, such as Claude Fable 5, refuse to work.#10812@FranziKay
* New Assistant hides lines, when it clearly has the space#10710@7aad94e9
* The new UI for Assistant is worse in every measurable way#10720@mspgrunt
* Settings -> Appearance -> Save : Not working in Orion Private mode#10724@markkrueg
* Customizable keyboard shortcuts (Assistant/General)#6650@bert
* Kagi Assistent new UI is too small#6142@HRA42
* Pasting text that exceeds x characters should automatically attach it as a text file#6739@Coops
* Dynamic Chat Window Scaling for Widescreen Users#6379@unruffled5088

### Kagi Translate

* Text cannot be copied anymore from Word and text from a PDF has hard returns behind every line#10476@JaninevdK
* “curled quotes” instead of "straight quotes"#7011@FranziKay
* Kagi Translate extension wrongly detects certain monitor as 'mobile'#10693@Roon

### Post of the week

This week's featured social media mention:

### Featured Kagi tip 💡

Here'sa guideon how to make Kagi truly yours with custom CSS. Tweak colors, fonts, and layout, hide elements you don't need, or apply a community theme for a search experience that looks exactly how you want.

## May 21st, 2026 - Search API preview opens to all users#

## Kagi Search API is now in public preview

Today we’re making the Kagi Search API preview publicly available, giving builders access to Kagi search across web, images, videos, news, and podcasts. The API is ready to use today, and we’re using this preview to transition existing beta API users, collect feedback, and finish the remaining launch details before the official announcement.

As a thank you to our subscribers, we’ve added$5 in API creditsto your account. You can use them right away to try the API, explore what’s possible, and see how it fits into your workflow.

Explore theAPI, read thedocs, and checkpricingto get started!

The API is not just a generic search endpoint, queries can inherit the preferences attached to the Kagi account behind the API key, including lenses, upranks, downranks, and blocklists, so applications can search through the same trusted and filtered view of the web that users have already shaped in Kagi.

Pleasesend us candid feedback: what’s confusing, missing, broken, or unexpectedly good!Try it out!

## Search

### Incognito-only mode for Privacy Pass

Our Privacy Pass extension, which allows you to prove to our servers that you're a subscriber without revealing your identity, has gained along-awaitedtoggle that makes it active only in incognito windows, so you can benefit from personalized results most of the time but have added anonymity for your more sensitive browsing. The extension was almost completely rewritten in the process, squashing several long-standing bugs.Try it out!

* Incognito Only Privacy Pass option in extension#6261@snowytrees
* Privacy Pass Authentication Doesn't Work in Private Windows of Firefox unless the Extension Is Turned Off and On Again#10582@kbkle
* Upload speed test started in background after pressing stop during download speed test#10449@shezgara
* "Welcome to your kagi team" email template missing team name#8876@tboby
* Region selection for Images, Videos, Podcasts#6784@batuhan
* 404 Not Found When Deactivating Lens#10564@Vage
* Incorrect definition of English word dingy#10395@tekchip
* Quick Answer Not Showing Short Citation#10406@Hummvie
* Keywords in Lenses act as "AND" instead of "OR" (adding keywords restrict the results).#10614@aussetg
* Small Web: button not clickable when hovering over text 'Start your journey'#10094@alelb22
* Duplicate youtube videos in video search results#7116@Thibaultmol
* Notifications only appear after you make a search#8304@Temanor
* Maps: Searching with no query searches for text "Undefined"#10486@zachary
* Firefox Privacy Pass Extension does not redirect for right click search kagi for ""#6381@Trees79

## Assistant

* LLM's Can't Tell the Difference Between Files with the Same Name#8878@rogue
* Kagi Assistant fails to output answer if too many work blocks are used#10568@PolicyPants
* What model is the Research Assistant based on?#10536@rogue

## Kagi Translate

* Add Interslavic language#10538@Anne-SophieW
* Macedonian (and others) not showing Cyrillic transliteration#10508@ashemedai
* Translate is removing newlines from input#10442@carl

### New on the Kagi Translate mobile app

Support for custom languages, explanations for alternative translations, word suggestions for dictionary mode, app shortcuts, and many other improvements!

Grab the app if you haven't already:AndroidoriOS

### Post of the week

This week's featured social mediamention:

### Featured Kagi tip 💡

We put togethera guideon using Kagi for academic work - the features, shortcuts, and search habits to get precise, more relevant results.

### Around the block

A handful of posts worth sharing with our community:

* Kagi's Small Web is Wonderful
* Daring Fireball -Kagi Snaps
* Kagi: Good Enough to Leave Google (search)
* William Roth -Tools I Trust: Kagi and Orion
* MacSparky -Still on Kagi, Still Happy

### Kagi video

Aquick videofrom our team to serve as a reminder of what Kagi is all about: the web, and your time on it, belong to you.

## April 30th, 2026 - Kagi API preview and ecosystem updates#

## Kagi APIs: the same search technology that powers Kagi is opening up to developers

Starting next week, we’ll begin onboarding developers to the Kagi API dashboard. Access will roll out first to people who joined theAPI waitlistor contacted Kagi support.

With the new Search API developers can bring Kagi Search into their own apps, tools, and AI systems. Here's an early look:

If you'd like to join this early preview of the Kagi API, please fillout this form.We'll reach out next week!

## Kagi Search

#### New landing

We updated our landing page to bring awareness to Kagi's wider ecosystem beyond search.Check it out!

This is the first of many steps toward helping more people discover everything Kagi has to offer.

* IP address and subnet search to bring up the Wolfram Alpha answer#10147@dronics
* Wrong Kagi Knowledge result for Mother's Day search#7086@dreifach
* "1 lakh crore" returns confusing results#9050@holdenr
* Custom assistant without internet access results in error#9876@Thibaultmol
* "Sign up for free" link on Pricing page not working#10314@Hanbyeol
* Disable Search Grouping in News Tab#10254@dvdnet89
* Auto suggest gives results which trigger bangs improperly#5346@LadyStrawberries
* Reverse image search returns primarily Russian and Russian-translated results#9111@Jake-Moss
* Runway (the AI video generation company) got erased from search result#10369@yanda
* Quick, direct access to "Set Kagi as default Search" instructions on your landing page (or close by).#6646@ragnar
* Web search image preview does not match the actual image searches. Also the image results are not relevant at all.#10367@StealthGirl
* Better UX for date calculator widget.#10282@leftium
* Redirect to first result bang no longer working if preceded by a space#10385@znmto
* Imgdata leaking into search results#10355@Keli
* Free search quota never expires#10403@afestein
* Ranking adjustment doesn't do anything when JavaScript is disabled.#10425@SkyDotBit
* Advanced Search modal and scrollbar behavior#4509@dix

## Kagi Assistant

* We increased the Assistant's file upload size limit to 30 MB#8872@mrzv
* Degradation of file analysis functionality in Kagi Assistant#10290@v3max
* Umlauts are sometimes not displayed in the Quick Assistant#9289@Kel
* Universal summarizer "Continue in Assistant" button fails: "We are sorry, this input is not supported. (Invalid Input)"#10368@Self-Perfection

## Kagi News

* Kagi News -> timeline ambigious#8525@yeri
* Story corrections, both from user reports and our own continuous fact-checking. When something turns out to be wrong, we fix it and show a small correction notice on the story, with the changed sentence highlighted on your next visit.
* Stories can pull in related coverage from other categories, so a single big story can span Science, World, and Tech when it makes sense.
* Cleaner prose in hard-news categories: fewer filler phrases, less editorializing, more neutral writing.
* Snappier all around: faster initial load, much faster story search, and browser back/forward now restores the page instead of reloading it.
* Custom category order syncs reliably across devices now. Fixed several cases where reorders were lost or overwritten.
* Category tabs use proper ARIA semantics for assistive tech.

## Kagi Translate

* Keyboard shortcuts in Kagi Translate#10306@mb
* Poor text formatting of image translations on Kagi Translate app#10016@San
* Pinyin absent for alternative translations#10340@phuertay
* Add Seto and Võro to Kagi Translate#10324@mb
* Correct file extensions when saving translations#10311@mb
* Add Montenegrin as an option in Translate#10230@mb
* Pasting text in Translate app is hard#10047@marty
* Pasted text from books or PDFs is auto-formatted: broken mid-sentence line breaks, hyphenation across lines, and stray whitespace get cleaned up. An undo toast lets you revert if you wanted the original.
* Auto-language switch now shows a toast with undo, and skips ambiguous cases like uncertain, mixed, or mid-typing input.
* Pin any language to the top of your list, including custom or non-standard ones.
* Romanization shown beneath alternative translations into Japanese, Chinese, Korean, Arabic, Russian, and other non-Latin scripts.
* Link previews (Open Graph) for translated text now show the actual translation when shared on social media, instead of a generic logo. The /extension page also got its own dedicated preview.
* New languages: Seto, Võro, Montenegrin, and Badini Kurdish (with both Arabic and Latin Hawar scripts).
* Formal Ukrainian now correctly capitalizes Ви and Ваш.
* Downloaded translations get the right file extension based on the detected content format.

### Post of the week

Follow usand tag us in your comments, we love hearing from you.

### Kagi is growing

The team is expanding, and we're looking for talented people who want to help build a better web alongside us. We're hiring for multiple roles, including:

* Product Designer (UI/UX): Take strategic ownership of end-to-end design across Kagi's product ecosystem.Apply here.
* AnEducation Partnerships Lead: If you believe the most important thing technology can do for students is teach them how to think for themselves, we'd like to talk.Apply here.
* ASenior Platform Engineer: If you have strong opinions about API contracts, auth correctness, and migrating user data without losing anyone's trust, we'd like to talk.Apply here.

We also have openings for a Senior Search Engineer, Senior Platform Engineer, Senior Full-Stack Developer (Kagi Labs), and an AI Specialist. See thefull list of openingshere.

### Kagi tip of the week 💡

Between AI-image filters, clickbait controls, reverse lookup, and source filters, there's a lot of power hiding behind the Images and Videos tabs.Here's how to get the most out of them.

### Kagi art

Less scrolling, more living.

## April 9th, 2026 - Tuning the Orchestra#

## Improvements and bug fixes

### Kagi Search

* Support IPv6 cidr ranges in ip whitelist for API#9988@Simonses1
* Dictionary widget only works when words are lowercase#10211@MustafaD
* Lens off by one error#7825@rhythmicorangeturtle
* Quick Answer hint displays even when Quick Answer is explicitly disabled#10267@mcc111
* Both m.imdb.com and imdb.com for the same webpage are in the results#10092@pma_snek
* Search term returns no results: almost anything that includes "sleep()"#10274@bkw777
* Kagi search sometimes ignores site: directive#9815@morj
* Wrong lens gets selected during search#10187@yodathan_
* Logged out when editing custom CSS#10303@SkyDotBit
* Inconsistently between web/image search when it comes to capitalization sensitivity#10309@Thibaultmol
* Islamic prayer time#9982@mishari
* Kagi Knowledge results consistently incorrect, haywire, misleading#6208@aasshhlleeyy

### Kagi Assistant

* Mobile app: Assistant has gray empty bar at top of screen#9570@RMLight
* Page context in assistant searches are limited#10167@jonathan-s
* Assistant thread history dates do not update dynamically when an old chat is continued#10278@xx
* Research Assistant searches fail on certain queries#10110@doggofan
* Kagi Assistant turns ssh commands into<mailto:user@domain>links even once corrected#8521@CodeAvolition
* Editing a prompt with a file, removes it?#5653@Thibaultmol

### Kagi Small Web

* iOS Small Web Dark Mode App Icon#10136@Cal4T5
* Add a tap-based way to switch posts
* Fixed incorrect text formatting for bookmark titles

### Kagi Translate

* Warning badge when translating to/from language using custom instructions
* Wordplay and puns lost in translation are now detected and surfaced to the user if word insights are enabled @zark
* Fixed Spanish text sometimes appearing in French translations on Standard mode @UAguy
* Fixed Japanese/Chinese/Korean IME first character being lost in empty editor @jisaker
* Proofreading a Word Document#8810@jmvleal
* Translate UI does not respect settings#9944@mmartinortiz
* Fix: clear button not working on mobile due to composing state#unknown@unknown
* Same Language bug#10134@KikoAnimations
* Fixed website translation stacking duplicate header bars when switching languages, and Google redirect URLs not being unwrapped
* Fixed clear button not working on mobile after pasting, restoring history, or during keyboard composition
* Fixed error when pasting rich text from webpages
* Fixed translation between same-language variants (e.g. pt-BR to pt-PT) echoing input instead of translating
* Fixed intermittent text-to-speech 503 errors
* Renamed "Azeri" to "Azerbaijani" to match ISO 639 standard
* Korean formality settings now apply to ko-KR locale@Hanbyeol
* Decreased AI refusals when translating text and images
* Pin "Detect Language" at the top of the source language selector for quick access @pineafan
* Add Montenegrin as an option in Translate@mb
* Improved keyboard shortcuts@mb

### Blast from the past

The retro homepage we implemented for April Fools may be gone, but many of you are not ready to let go of the nostalgia just yet.

Here's a dedicated URL to bring it back whenever you want:https://kagi.com/?year=1996

This sets a cookie so your device remembers. To undo it, click Back to the Future at the bottom of the page or visithttps://kagi.com/?year=present_day

### Post of the week

Here is this week's featured social mediamention:

Follow usand tag us in your comments, we love hearing from you!

### Kagi tip of the week 💡

Did you know you can set up URL redirects to reroute search results to the sites or frontends you prefer?Here's how, with examples from the community.

### Kagi art

AI and ads are a toxic combo. Across the Kagi ecosystem, there are no ads, and we're actively working to keep slop out of your search results. Read more about Kagi's SlopStop initiativehere.

## March 19th, 2026 - Small Web Expansion and Translate goes viral#

## Kagi Small Web just got bigger!

Kagi'sSmall Webjust got a whole lot bigger. With over 30,000 feeds and new browser extensions, mobile apps, and categories, there's never been a better way to discover the independent web.

Read thefull announcement here!And check out theTechCrunch coverage.

* Download for iOS
* Download for Android
* Get the browser extensions

## Kagi Translate goes viral!

On March 16, we launched our latest fun language on Kagi Translate,LinkedIn Speak, and it quickly went viral on social media, generating millions of engagements. Check out some of the press coverage below:

* This Viral Tool Turns Anything Into LinkedIn Speak—and the Internet Is Obsessed
* This eerily accurate ‘LinkedIn Speak’ translation tool will help you sound like an instant thinkfluencer
* 'LinkedIn speak' turns Kagi Translate into viral meme machine; here's how to use it

Also, a friendly reminder: the Kagi Translate appslaunched a few weeks agoand are already earning solid reviews. Go grab them if you haven't yet!

## Improvements and fixes

### Kagi Search

* Add quick snaps#5237@Jesal
* Automatically accept dragged images for reverse image search#7482@tuesday
* Seemingly impossible to get current time widget in Georgia (country)#4513@mon
* Doggo Consistency#5191@tjp
* Patreon not Appearing as First Result when specified#9993@JosephT
* AI marked images still show up in the "images" widget/section in normal web search#9445@Thibaultmol
* Show Wolfram Alpha's 'Input interpretation' when a WA answer is provided#9336@Thibaultmol
* Overlapping popups in quick answer#10014@Temanor
* Kagi Missing Results When Searching for Specific News Site under News Section#8181@woodmaster
* Don't use AI slop as a source for Assistant/quick answer#9229@fxgn
* Images on macOS Safari not opening#9891@BrittOmnRex
* Long queries don't work with bangs#5563@Thibaultmol
* Weird top search result forproton#10023@gabriz4803
* Wrong search bar content#10135@someoneiknow
* Popup cut off, not scrollable.#10022@Temanor

### Kagi Assistant

* Llama-4-maverick, o3-pro, gemini 2.5 flash lite and gpt-5-nano models are no longer available.
* Assistant doesn't render code blocks sent from user correctly#6165@kzar
* Assistant: Quick Edit / Jump to AI/edit#6422@ivanovich_alexander
* Assistant typing input speed slow on long conversations#5434@jackkkk
* Assistant returns "We did not get a response from the server" on slow connections, but still works#4689@jvbf
* Kagi Assistant only summarizes PDFs instead of processing full contents (selectable text and handwritten notes)#9930@Pum
* Gemini 3.1 Pro (Preview) unable to read PDF in first attempt#9996@dreifach
* Critical Issues with Recent Copy-Paste Content Changes Affecting Text Summarization Workflow#9832@Fragment5789
* Claude keeps using LaTeX without formatting#8455@fxgn
* Links in the assistant's responses are not clickable#6556@NathanKurz
* Librarian is Truncating Files#10074@RixTheFox
* Some multimodal LLMs fails to see attached images#10113@Anonymous26
* Assistant typing input speed slow on long conversations#5434@jackkkk
* Assistant returns "We did not get a response from the server" on slow connections, but still works#4689@jvbf
* Assistant: Remember model per device#4953@pravinxor
* Provide more default assistants#4926@somerabbit155
* Add swipe gesture action to close the side bar on new Assistant UI#4823@Jassu

### Kagi Translate

* Dialects of Scots listed under English#9965@AndrewA
* Correct naming for Persian language in English#9957@mehdim
* Unable to translate from "Detected (English)" to "English (US)"#9925@Peter
* Put artificial languages into their own submenu#9958@tux0r
* Kagi wrongly changes numbers/time stamps when translating#9971@MartinNo
* Kagi Translate: Language switch button does not work for auto detected language#6065@carl
* Kagi Translate Android App buttons are hard to hit#10004@mb
* About the app version's translation mode#9986@noelchan

#### Mobile Apps

* Poor text formatting of image translations on Kagi Translate app#10016@San
* Kagi Translate Android App buttons are hard to hit#10004@mb
* Pasting text in Translate app is hard#10047@marty
* Prevent translation quality switch when swapping languages#9986@noelchan
* Kagi Translate iOS app is failed to establish session#10125@SukinoVerse

### Kagi News

* Keyboard Shortcuts only work intermittently on Kagi News#8786@the_hattar
* Condensing, locking settings — managing Kagi news for dementia#10115@jimbo95

#### Mobile Apps

* Time Travel: Browse news history by date. Pick any day on the calendar and read past summaries.
* Content Filter: Hide or blur topics you'd rather skip. Choose from built-in presets or add your own keywords.

## Post of the week

Here is this week's featured social mediamention:

Don't forget tofollow usand tag us in your comments, we love hearing from you!

## Kagi Specials

We're excited to welcome the newest addition to ourKagi Specialsprogram:EasyOptOuts! Kagi members in the U.S. now enjoy 25% off for life.

This is a service that removes your name, address and phone number from 200+ data brokers and people-search sites automatically. Deal isreciprocated herefor any EasyOptOuts subscribers in your network who want to try Kagi.

## Kagi art

"Free" search costs more than you think. With Kagi, you get zero ads, zero tracking, and AI on your terms.

## Feb 26th, 2026 - Smoothing the edges#

## Kagi Search

### Wolfram|Alpha widget supercharged

We're introducing a new and improved Wolfram|Alpha widget with support for rich equations, plots, better region-dependent queries, and more!

### Other improvements and bug fixes

* Kagi Privacy Pass extension conflicts with Kagi Search extension in Firefox, breaking login token recognition in private browsing windows.#6432@stone. This was a bug in Firefox -thank you to Mozilla for the fix!
* The after-login redirect doesn't work for maps or assistant#8407@Boomkop3
* !hn bang does not use correct URL#8534@davej
* Emoji search: Japanese symbols should come up when searching for themselves#9823@karol
* Not possible to block TLD in personalised results#7104@MrMoment
* Search box submits incomplete text#9836@ssg
* Translation won't trigger in search until I reload the page#8409@Gamesnic
* Content appears behind Dynamic Island on landscape iOS#9772@ohnojono
* Can’t add a team member from iOS Safari#9003@pbronez
* Kagi Wolfram answer doesn't match direct Wolfram query#9866@RonanCJ
* Reverse image search comes up with empty spots#8666@Boomkop3
* Opening search results in new tab with Vimium shortcuts doesn't work when authenticating via Privacy Pass#9894@kbkle
* Image search directly from regular search bar#9889@Boomkop3
* "Weather Saturday" returns for location Saturdaygua instead of weather on saturday#2388@kevin51jiang
* SearchingPseudo Codegives(data not available)from Kagi Knowledge#9922@xjc
* "Interesting Finds" does not respect filter rules#8578@dabluecaboose
* Search snap: Reddit - @r returns little to no results on iOS due toold.reddit.com#9582@owl
* Allow setting open_snap_domain for custom bangs#9901@shorden
* Low quality translated Reddit results#5212@bram
* Click on "More Results" loses the focus#5736@expurple

PS, we've started publishing results for your SlopStop reports --see them here. More details in the upcoming changelog.

## Kagi Assistant

* Kagi Assistant - Ki Model - Toggle detailed search results broken with a lot of searches#7880@Elias
* Assistant turns email address like text into mailto in codeblocks#9843@Numerlor
* Slash-commands being sent to model along with system prompt#9852@igakagi
* Ki can't access uploaded images from Python#7376@fxgn

## Kagi Maps

* Kagi maps "No POI found matching the query"#9799@Jobby
* Maps sends double-URL encoded string to images#9698@gdfgfasf
* Inconsistent Display of Postal Codes#9711@iamjameswalters
* Maps Search Not Finding Some Places On First Try#9637@Gredharm
* Searching "Chagos Islands" (or other locations w/o POI data) fails; doesn't fall-back to entry w/ valid POI data#9888@Cajunvoodoo

## Kagi Translate

* Translate Document - "Upgrade to premium" / inconsistent limits#9811@widow5131
* Kagi translate mixup: Swiss High German vs. Swiss German#9827@kagiiskey
* I'm interested in integrating Kagi Translate with Anki Flashcards#9750@johnsturgeon
* Ability to set the default translation quality#9802@PetrIako
* Translating input to same language: English->English#9690@Cyb3rKo
* Translate document - premium not working#9879@widow5131
* Fix needed for Korean word order of "total" count#9718@Hanbyeol
* Wrong interface language in Kagi Translate#9880@jstolarek
* Kagi Translate Firefox extension: incomplete translation on some sites#9862@exzombie
* When I type a long sentence, it freezes and I can't scroll.#9940@ZK

### Kagi Translate - iOS and Android apps

* Fix needed for Korean word order of "total" count#9718@Hanbyeol
* Make “Translate with Kagi” appear directly in Android text selection menu#9801@Matou
* Added 'email' writing style for proofreading
* Added setting to toggle haptics ON/OFF
* Fixed UI issue on Android where certain elements were being drawn under system bars

## Post of the week

Here is this week's featured social mediamention:

Don't forget tofollow usand tag us in your comments, we love hearing from you!

## Kagi Specials

Kagi is happy to be part of theprivacy alliancewith Windscribe, a feature-rich VPN with built-in ad and malware blocking and audited no-logs policy.

Through this partnership viaKagi Specials, Kagi members receive a 3-month Windscribe Pro trial, then lock in the Pro plan at just $49/yrfor life. In turn, Windscribe members get 3 months of Kagi's Professional plan.

## Community creations

If you're usingScribblesto run your blog, you can now addSmall Webbadges directly to your blog footer, just head to the new "Small Web" section in your blog settings:

## Kagi on TV!

Kagi wasprominently featuredas a private alternative to Google on KTLA 5 News, including an interview with Kagi's very own John Bardinelli, who recently joined the team as our Growth Manager.

## Feb 12th, 2026 - Kagi Translate on Android & iOS: translate anything, anywhere#

## Kagi Translate Arrives on Mobile

Kagi Translate is now available as an app forAndroidandiOS!

The app supports over 248 languages and offers context-aware image translation, live voice-to-voice conversations, and a rich dictionary with audio, to name just a few of its features.

Read the full announcement and feature highlightshere.

Fast Companyfeatured the launchas a privacy-first Google Translate alternative worth noticing. Asimilar guidewas published on The Intelligence, which covers tips and tricks to help users get the most out of Android devices.

## Other improvements and bug fixes

### Kagi Translate apps

* Allow removing individual translation history entries in kagi translate mobile app#9774@alcroito
* Kagi translate mobile app: Editing text in the middle causes scrolling / jumping around, makes it hard to edit#9758@alcroito
* Inconsistent Swipe-to-Go-Back Gesture in Kagi Translate (iOS)#9729@xx
* An option to individually delete translations on Kagi Translate#9713@xx
* Kagi Translate iOS App reports "No Connection"#9679@Frank

### Kagi Search

We've added a new copy emoji widget!

* Fixed team invitations not working in some cases
* Fixed links in our Welcome email
* Attempted fix at some browsers showing outdated favicons
* Video Personalization Function Appears Completely Broken#9313@ooh
* Show a copy emoji button#9728@astronaut
* Exact Domain Query Buried Despite Perfect Relevance#9780@k19b1
* Update kagi.com/assets#9742@Anonymous12
* Filter buttons are not marked as buttons#9624@spiffyk
* Quick Answer Search Query Bug#7801@Xytronix
* Calculator widget triggers for plain number searches#9464@dreifach
* Stylesheet definition order for ‘small results’ (srgi)#8591@KKagi

### Kagi Assistant

* We've made changes to how we phase out older or superseeded models. When a model is being phased out, your Custom Assistants using it will first show a warning for ≈2 weeks. Once the model is fully retired, the Custom Assistant is disabled until you update the model in settings.#5597@Thibaultmol
* Larger copy-pasted content is now automatically converted to a.txtfile and works like any other attachment. This ensures the full original content is always preserved, even in very large threads that hit context window limits. In most cases, it remains fully within the context window. In longer threads, the original content is stored separately and retrieved as needed.
* Do not re-rank Assistant threads when their title changes#8434@dreifach
* Remove ads/upselling for flagship AI models in Kagi Assistant#9693@lasu
* Kagi Assistant customize tab styling error#9688@gromgrom
* Performance improvements when submitting prompts on accounts with a lot of threads

## Post of the week

Here is this week's featured social mediamention:

Be sure tofollow usand tag us in your comments!

## Fastmail supports Kagi Search

To mark Safer Internet Day, Fastmail explains why your search engine matters just as much as your email provider when it comes to privacy, and whythey recommend Kagito their users: "Adding Kagi creates a powerful privacy stack".

## Addy.io joins Kagi Specials

We're excited to welcome Addy.io as a new partner onKagi Specials! Addy.io is an email forwarding and alias service that helps protect your privacy by allowing you to create unlimited email aliases.

As part of this partnership, Kagi users can now access exclusive discounts through Kagi Specials, and Addy.io users can discover Kagi through theirperksprogram.

## Jan 29th, 2026 - Assistant reliability upgrades and Search refinements#

## Waiting for dawn in search

We published a new blog post on the state of search and the critical need for open index access. The dawn of a healthier, user-centric web is possible, but it requires structural change.

https://blog.kagi.com/waiting-dawn-search

## Kagi Search

* We've upgraded our Academic lens! Try it when you want research results drawn from scholarly and professional sources. Ideal for topics like medicine, sports science, or other specialist fields
* Added functionality for users to manually set their location, improving local search queries. This is part of our weekly incremental improvements to localised search in Kagi.
* Several accessibility improvements have been made, including corrected roles and proper fieldset semantics for our dropdown menus throughout the site, thanks to Tamara Cook, an accessibility consultant who proactively reached out to us via our support email. Thank you very much for the input!
* If search fails because no upstream sources responded in time, show Click to Retry#7795@kirkmc
* New favicon pixelated when default search engine (Firefox?)#9585@Replica6
* Related search suggestion for current search#7781@Keli
* Unable to Renew Plan After Reaching Limit in Kagi Assistant#7152@0rb
* Orion+ renewal date is in the past#9608@marcel
* Control Center is accessible when browsing via privacy pass and features do nothing#9588@Sludge
* False summary of wikipedia article#5007@greyfivenine8244
* "uploaded file" appears in web search when switching from image search#9566@Arlo
* Supportdefine:<term>#6040@yeri
* Mobile back to top/search appears too easily#8215@Numerlor
* Hide Stats Button Missing#9065@Timmy256
* Kagi light theme issue on Steam embedded browser#8384@JulianGro
* Programming lens doesn't work#8310@Khyta
* Make Wikipedia bang/snap region neutral#8069@Thibaultmol
* Incorrect timezone for Kazakhstan#8964@mxp
* Related search suggestion for current search#7780@Keli

## Kagi Search Android

* The app now follows the "Open in External Browser" setting, opening search results either in-app or in your default browser

## Kagi Assistant

* Recommended models are now more useful to users. We clearly outline which base models we recommend: best fast (speed), best balanced (speed<>depth), best overall (max quality)
* We've made several changes to ensure the Assistant reconnects you to any response in progress if your network connection drops or you navigate away from your browser. This means no more loading animations while you wait 🚧
* Image generation does not work with Research Assistant#9071@darsnack
* Kagi Assistant — attached files don't remain attached in edited queries#6652@dreifach
* Complex branching scenarios no longer result in duplicate entries in the branch picker or showing < 0 / x >
* Added Kimi K2.5 models
* Some Assistant Search Queries Don't Return#8174@iamjameswalters
* In Assistant, Kimi K2 (reasoning) is rated with the same speed as K2 despite being described as "much slower"#9665@RonanCJ
* Shared thread doesn't show read only UI after clicking away and back in#7951@Numerlor
* Change reasoning effort for Claude Opus 4.5#9610@kray

## Video tutorials and guides

We have aYouTube playlistwith all kinds of guides, quick tips and tricks to help you get the most out of your Kagi subscription.

## Post of the week

Here is this week's featured social mediamention:

We truly appreciate your support in spreading the word, so be sure tofollow usand tag us in your comments!

### Kagi art

Technology should serve you, not trap or burden you.

## Jan 15th, 2026 - New Year tune-up: smoother everything!#

## Kagi Search

### Kagi Search Android app

We’ve made meaningful improvements to the Kagi Search app — faster performance, smoother overall experience. If you’re on Android, give the update a try.

We also hope this makes it even easier to share Kagi with the people you care about.Let us know what you think!

* Improved app startup time
* Updated search home screen with native text editing
* Updated home screen widgets with faster access to Translate, Summarize and Assistant
* Add settings to Kagi Search app to autofocus the search bar on launch and to move the search bar to the bottom#9042@conradsrc
* Improvements/fixes to the Android app screenshots#5019@Niraj
* Android app: Pressing Enter on a physical keyboard should search#8838@ItsHarper
* Android app: image, news... etc don't stay selected in the first screen#7207@Ronzino
* Android Share Menu: "Assistant" option appears twice, first instance should be labeled "Search"#8773@artemp84
* Image Search With Camera#5032@Wes
* Add voice search#3270@Browsing6853
* Launching translate from the Android widget is very slow#8453@zslayton
* Fixed login for Github connected accounts

### Other fixes and improvements

* !word bang now directs to Kagi Translate Dictionary
* Toggle to Disable SlopStop#9105@______nick(also adds settings around it though)
* While authenticating via privacy pass, you are unable to use any non-default lens#9510@Sludge
* Trying to change rank status of a domain from Kagi's leaderboard isn't working as expected#9392@Puddle
* Personalized Results page has Incorrect Link#9517@catgirlinspace
* Thekagi.com/botpage is hard ro read#9511@thekarel
* Maintain 'annual' choice on pricing page when switching between Individual, Family, Team#9378@keunes
* Translations spill over container in pricing page#9377@keunes
* Link doesn't resolve to anything#9413@onlineversioncontrolsystem
* Reverse image search not working correctly with text copied from Excel#8598@bxd41
* Embed Google Maps Reviews alongside Yelp Reviews#4204@mackid1993

## Kagi Assistant

* We upgraded to GLM 4.7 (with thinking variant)
* Case-agnostic alphabetical sorting for tags#8967@lolroger
* Make searching on/off more clear
* Special characters like German Umlaut (ä, ö, ü etc.) are broken when customizing Assistant#9501@Felensis
* The first letter(s) of Grok 4 responses are cut#9484@4fzx6
* Problem with unicode characters in assistant's output#9345@chbug
* Kagi Assistant Thread Search Performance degradation (WebKit?)#9462@tockrock
* Diacritics in filenames prevent document analysis#9361@noquierouser
* Allow immediate typing when you load the Assistant#9401@Thibaultmol-kagi
* Research (Experimental) can now generate and edit images
* Model selection window breaks into two lines in CJK languages#9032@Hanbyeol
* Kagi Assistant: Renaming a thread does not allow you to select single words or characters in the thread name#8909@__
* Assistant lens dropdown sometimes lights purple with no lens selected#9169@howie
* Message info now includes timestamp of when the prompt was submitted

## Kagi News

* Time Travel mode to access past daily summaries - available to all during beta, subscriber-only after
* Paywall indicator for paywalled domains
* Keyboart shortcuts for navigation do not work as expected @mr-f00
* Wide screen mode @xatier
* Added Estonian as UI language @Tarpsvo
* Heat index graph does not update when refreshing news from notification#9547@ashemedai
* Allow user to set a universal reading level for category#9531@cakeboss
* Ordering Sources List in Kagi News#9450@catfriend
* Links to source articles should be actual links#9273@r5x

### Kagi News Apps (iOS and Android)

* Faster app launch and improved offline support
* Pull-to-refresh added to the feed
* Category settings now include search for easier discovery
* Sources section in story view now shows the number of publishers and articles
* Support for selecting multiple content languages, stories are automatically translated to your primary language when needed#8822@LordDuckingling
* Exception messages are now localized for better clarity
* Improved image caching to reduce local storage usage
* Enhanced layout responsiveness on wide screens, including iPads and tablets
* General UI improvements across the app

## Kagi Translate

* Help documentation redone(including detailed information about what you can do withURL paramterswith Translate)
* Pinned languages and language history are now synced across devices if settings syncing is enabled
* Improved speech-to-text
* Background processing for document translations - start a job, switch tabs or close the browser, and download later
* Chinese localization tweaks@CTAO
* Alternatives button does not animate when only two characters are selected@CTAO
* No minimum text box size causes mobile view to become unusable below certain height#9499@BenMacphail
* Japanese Input Issues on Mobile#9496#9495@TusedayGhost
* Clicking 'Show More' long romanicized text hides the box#9394@theDoctor
* Alternative translation descriptions appear in target language#9431@theDoctor
* Dictionary view pulls in other language tags and categories#9419@ashemedai
* Duplicate language suggestions for "Detect Language"#9416@dreifach
* Make buttons in Dictionary actual hyperlinks instead of js links#9408@Thibaultmol
* Improve 'Dictionary sections' in Kagi Translate#9407@Thibaultmol
* Document Wikitionary usage within Kagi Translate Dictionary#9405@Thibaultmol
* Backdrop blur doesn't work in Safari on the translate pop-up controls @Carl

## Kagi Maps

* Single clicking a city in maps doesn't do anything#9493@CameronLittle
* Kagi maps doesn't show me the location linked to if I've given it location access#9492@CameronLittle
* Extremely Distant Cafe & Restaurant Suggestions in Kagi Maps#9214@Manipesto
* Maps Opening Hours Wrongly Shows Closed#9342@Gredharm
* Maps Broken on Brave#9323@Gredharm

## Post of the week

Here is this week's featured social mediamention:

We truly appreciate your support in spreading the word, so be sure tofollow usand tag us in your comments!

## 2025: Year in Review

Explorethe major updates, product launches, milestones and press highlights that defined last year for Kagi.

## Windscribe partnership & privacy alliance

Kagi has partnered with Windscribe, Notesnook, Addy.io, and Ente to create a privacy-focused alliance.Read the announcement here,and check out our currentKagi Specials.

## Kagi around the web

* Kagi News and Kagi Summarize are featured on a list of "incredible Android apps", check out the videoreview here.If you haven't yet, download Kagi News oniOS,Android, or view theweb version, and grab Kagi Summarize oniOSorAndroid.
* If you haven't yet, download Kagi News oniOS,Android, or view theweb version, and grab Kagi Summarize oniOSorAndroid.
* Ourvideo about Kagi Small Webis resonating with members. We talk about the purpose behind this initiative and why we're committed to growing it.

## Dec 18th, 2025 - Popular areas land in Kagi Maps#

## Kagi Maps

We're continuously improving Kagi Maps, and with the latest release we've added a new data layer: Popular Areas. It highlights the busiest and most frequented spots when you're exploring a new city.

New Global Map Layer:

* Highlights most popular areas where people congregate near Cafes/Restaurants/Shops/Cultural-Centers

POI Infoboxes have more 3rd party external links:

* OpenStreetMap, Wikipedia, Google Maps, Apple Maps
* Reviews on Yelp and TripAdvisor
* Social media profiles (Facebook, Instagram, Twitter)
* Reservations via OpenTable
* easier-to-read opening hours with weekly schedules
* Direct links to restaurant menus when available

Strengthening ties to OpenStreetMap Community:

* with ability to Report Map Issues to OpenStreetMap directly. A new "Report an issue" option in Infobox connects you to OpenStreetMap's note system, where you can flag errors or suggest improvements to the underlying map data.

Additional Map Data:

* POI data now preloads in the background for faster navigation when clicking markers or search results
* Mobile-optimized zoom controls for smoother touch interaction
* Sorting preferences (distance, rating, price) now persist across sessions
* Faster POI on click load-times with use of shorterm caching
* Middle-click support on search results and sorting buttons

Various ad-hoc bug fixes and database improvements:

* Improved caching system for POI data reducing redundant API calls
* Better location cookie handling usingkagi_precise_location
* Various improvements to our POI-matching algorithms
* UI rendering fixes

## Kagi Search

* Location management is now available in settings, where you can view and update your location at any time. Kagi uses either a coarse location estimated from your IP address or, if you opt in, your device's precise location. This isstored only on your device as a cookie. It supports local-intent searches (e.g. "petrol stations near me") and sets the initial map position in Kagi Maps.
* Incorrect geoip location#9194@klandarey
* Searching for 'Pop! OS (System76)' redirects to incendar.com#9053@gigabit-jack
* Summarizer fails on all YouTube videos, "Sorry, no transcript could be found for this video."#9278@urrlich
* Kid accounts cannot select a companion.#9246@leuchtthurm
* Quick answer responds in Indonesian, despite results being English#9237@zq40000
* Can't get to the consumption page from a team plan account#7265@Thibaultmol-kagi
* Add an indicator to the shield for websites marked by Surveillance Watch#8912@pma_snek
* !tr as the regional bang for Turkey#6376@GERGE
* Quick Answer shifts layout on mobile#9171@hmnd
* Context menus for inline news and videos are stuck inside the frame#9127@pma_snek

## Kagi Assistant

You can now effortlessly navigate your threads and jump to specific messages with our new thread scrollbar.

* We've made the following model upgrades:Grok 4 Fast and GPT 5 have been updated to their latest versionsRetired Mistral Medium in favor of Mistral Large
* Grok 4 Fast and GPT 5 have been updated to their latest versions
* Retired Mistral Medium in favor of Mistral Large
* Add a column to the Custom Assistants settings table that displays each assistant's associated bang#7440@jogojapan
* Kagi Mobile Assistant: Tapping or holding a model name should prompt the model info box#8023@__
* Claude output cut off around6500tokens#9265@igakagi
* When using Web Access, Kagi Assistant searches too few sources#6149@Mar
* Buttons to quickly jump between chats in an Assistant thread#9232@brrrendan
* Right click on highlighted text cause thinking, search, plan and etc to expend#9117@rxzlion
* Assistant using 2024 as the search year in 2025#8350@blackbird2150
* Update Grok Fast to 4.1#9190@mitch
* Sharing page for Assistant broken#9176@catwars
* Research Assistant image generation should allow you to specify higher resolution than 1024x1024#9156@jmp242
* Navigating between versions of the same prompt is broken with 3 prompts after page reload in Kagi Assistant#7134@bsamek

## Post of the week

Here is this week's featured social mediamention:

We truly appreciate your support in spreading the word, so be sure tofollow usand tag us in your comments!

## Is your browser a rat?

Check outthis fun videowe made forOrion. We also made this comic in collaboration with artistChaz Huttonto show why we built Orion to be your trusted daily companion for the web:

## End-of-Year Community Event

Join us tomorrow, December 19, at 09:00 PST (convert tolocal time) for Kagi's annual community event, covering major updates, launches, and what's next. Pluslive Q&Awith the Kagi team.Register via Zoom.Looking forward to seeing you there!

## Dec 4th, 2025 - New Kagi Search companions and quality-of-life improvements#

## Kagi Search

### Introducing Kagi Search companions

You can now choose your preferred companion on Kagi Search! And more companions coming soon.

#### Other improvements and bug fixes

* Context menus for inline news and videos are stuck inside the frame#9127@pma_snek
* "We haven't found anything" when asking a follow-up question in Quick Answer#8986@jstolarek
* Feedback on the new Quick Answer experience#8729@Jesal
* Custom Default Model for Quick Answer Follow-ups#5533@MaCl0wSt
* Quick Answer 'Show More' Memory#8902@Anonymous12
* Out of place image in wikipedia widget#9114@Numerlor
* Quick. kagibara eye animations.#9103@kagifuser
* Doggo's snoot isn't contrasting well on the pricing page#8477@Thibaultmol
* Quick Answer - Continue in Assistant not clickable#9010@Anonymous12

### Kagi Assistant

* We've made the following model upgrades:Research Assistant now uses Nano Banana Pro for image generation and editingClaude 4.5 Opus and Deepseek v3.2 have been updated to their latest versions
* Research Assistant now uses Nano Banana Pro for image generation and editing
* Claude 4.5 Opus and Deepseek v3.2 have been updated to their latest versions
* Weird recording of voice in assistant#8672@StefanHaglund
* GPT OSS 120B straythinktag#8951@claudinec
* Citation popups cropped within tables#9025@hinq
* Include chat title in shared chat link preview#9045@bert

### Kagi Translate

* [Extension] Discord, Whatsapp, Telegram, Reddit integrations
* [Extension] Redirect from translate.kagi.com/url#8503@Thibaultmol
* [Extension] Statistics page in setting
* [Extension] Apply suggestions (translate/proofreading) directly from overlay#8695@orschiro

### Slop Detective

* Slop Detective page doesn't scroll, which can prevent progress#9079@jducoeur
* Slop Detective image zoom/magnifying glass should be shifted on phone/mobile/touch screens#9080@dru4522
* Slop Detective calls all images "photographs"#9072@ccombsdc

### Post of the week

Here is this week's featured social mediamention:

We truly appreciate your support in spreading the word, so be sure tofollow usand tag us in your comments!

### Community creations

James Downs built aKagi News appfor Pebble watches:

Check out thisgrowing listof Kagi community creations for various devices and apps! Have one to share? [Let us know](mailto:esra@kagi.com).

### Small Web badges

Small Web initiative members can display badges on their websites to identify themselves as part of a community committed to authentic content created by humans.Grab them here!And keep exploring what theSmall Webhas to offer.

### End-of-Year Community Event

As we wrap up an exciting year for Kagi, we'd love to have you join us for our end-of-year community event onDecember 19 at 09:00 PST(convert to yourlocal time).

We'll share a comprehensive "Year in Review" covering Kagi's major updates, product launches, and what's ahead, followed by an interactive Q&A session where we'll address your questions directly.

How to participate:

* Register via Zoom.
* Submit and upvote questionsin advance for the Q&A portion of the event.

## Nov 22nd, 2025 - Kagi Hub Belgrade#

## Kagi Hub Belgrade: Making the human web real

We just opened the Kagi Hub in Belgrade, Serbia!

If you’re a Kagi member,you can book up to 5 FREE reservations per monthand treat the Hub as your base whenever you’re in Belgrade. It is the same space our team uses, so you will be working directly alongside the people shaping Kagi’s future. More details, including how to reserve your spot, are in this blog post:https://blog.kagi.com/kagi-hub

Having an actual physical space makes our mission to "humanize the web" feel so much more real. It is a place for Kagi members and our fully remote team to work, trade ideas, and build the tools we all wish existed.

We are looking forward to welcoming you to Kagi's first ever Hub!

## Nov 20th, 2025 - Introducing Quick and Research assistants#

## Kagi Assistant

### Introducing Quick and Research assistants

Today, we are officially introducing Kagi Research assistants (previously known as "KI").Read our full announcement here.

Their main strength is research: identifying what to search for, executing multiple simultaneous searches (in different languages, if needed), and synthesizing the findings into high-quality answers.

Simply choosewhether to prioritise speed or depth:

* Quick optimises for speed, providing direct and concise answers.
* Research focuses on depth and diversity, conducting exhaustive analysis for thorough results. Research is available to Ultimate subscribers only.

To achieve this, they employ different base models for specific tasks. Wecontinuously benchmark top-performing modelsand select the best one for each job, so you don't have to.

And on top of web search, we’ve added new behavioural layers and a wider toolset, including Python execution and image generation for higher-quality answers. These capabilities go beyond what was already possible in Kagi Assistant using a base model with web search. See ourdocumentationfor the full details.

Finally, a huge thank you to everyone in ourDiscordfor beta testing this with us and providing tons of feedback along the way! 🙏

Note:

* With this change, we set the Quick assistant as the default mode in Kagi Assistant. You can always adjust this in yourAssistant Settings.
* Additionally, we plan to migrate theqbang, currently used for Quick Answer, to trigger an Assistant thread targeting the Quick assistant.

### LLMs are bullshitters. But that doesn't mean they're not useful

Yesterday, we published an opinion essay exploring the useful yet disruptive nature of LLMs. Give it a read and let us know what you thinkhttps://blog.kagi.com/llms

### Colour code your Assistant tags

Now you can assign icons and colours to your tags. Spot important threads instantly.

### Other improvements and bug fixes

* Retired a handful of models. As part of a regular process, we occasionally review and retire models that are not used by Kagi customers and have been superseded by better, newer models. Saying bon voyage to:gpt-oss-20b,gpt-4-1-nano,gpt-4-1-mini,gpt-4-1,o4-mini,o3,grok-code-fast,mistral-large,deepseek-r1, andhermes-4-405b. In the future we will forecast these changes with more advanced notice.
* Various untranslated Kagi Assistant texts#5328@MonoMatrix
* Kagi Assistant - work on relationship between Custom Assistant and Model in the UI#8327@RobOK
* Show more info in dialog when using Kagi Assistants#8335@Thibaultmol
* Case-agnostic alphabetical sorting for assistant tags#8967@lolroger

## Kagi Search

### SlopStop Update

Last week we kicked off ourSlopStopinitiative. Since then, thecommunity has submitted over 3,000 reports!Our team is reviewing this data to refine our evaluation pipeline, with improvements expected to go live next week

Please continue reporting AI slop in your search results.

* Paywalled news sites are now signaled on/news.
* The new AI slop report breaks the layout when translated#8923@tux0r
* Programming lens doesn't work#8310@Khyta
* Timer not removed when search is changed#8780@acut3
* No reference list for quick answer with privacy pass#8917@Jesal
* Reverse image search for recent image works on Google but not Kagi#8380@leftium
* You can report the same website as AI generated multiple times#8911@pma_snek
* Family invite page for some accounts has garbage html#8943@Temm
* Quick Answer 'Show More' doesn't save state#8902@Anonymous12
* Quick Answer autocomplete suggestion opens non-search tabs, should go to search#8941@Thibaultmol

## Kagi Translate

* Add Bavarian dialect#8910@Anonymous12

## Post of the week

Here is this week's featured social mediamention:

Haven't tried the Kagi Translate extension yet?Check it out!

## Nov 13th, 2025 - Raising the shield against slop#

## Kagi Search

### Introducing SlopStop: community reporting to reduce low-quality AI content

Today we're releasing SlopStop, our first step in collaborative filtering.This allows our community to directly improve search quality for everyone!Read the full announcement here!

Low-quality AI content is flooding the web. Kagi’s ranking already downranks and filters much of it. SlopStop gives you a simple mechanism to help us keep results even cleaner and more authentic.

How it works:

1. If you see low-quality AI content in web, image or video results, click the shield icon next to the result to report it. If something is flagged in error, use the same control to report the mistake.
2. Check your reports statuses inSettings.
3. We verify reports alongside our own signals. When a domain or channel is confirmed to primarily publish AI content, we deprioritise it in Kagi.

You can read more about this initiative in ourannoucement blog postor in ourdocumentation.

### Highlighting surveillance actors

We've integrated withSurveillance Watch, an interactive database that documents surveillance and spyware entities. When you visit a domain on their list, we'll display a banner to alert you.

### Other improvements and bug fixes

* Results show centered despite the setting being set to "Left"#8886@vaartis
* Feedback on the new Quick Answer experience on mobile#8729@Jesal
* Add option to auto trigger Quick Answer when submitting an edited query in which Quick Answer previously was used#6769@RoxyRoxyRoxy
* Info panel display on 13# laptop#7810@kirkmc
* Quick answer doesn't work when Privacy Pass is enabled#8731@laiz
* Blocked Domains still show up in video results#8694@MCWhitaker
* Timer auto started when searching for usb/spi device id#8216@kagi6741
* The !cpp bang doesn't work#8699@exzombie

### Kagi Assistant

* Document search sources individually#8041@Diniboy1123
* Ki Says It Can't Edit Images#8705@iamjameswalters
* Qwen-3-235B code formatting broken#8840@crhallberg
* Copy-paste of Assistant text on mobile accidentally selects all prompt titles out of view#6701@sshine
* The "X" button in Assistant settings should go back to Assistant#6985@fxgn
* Dragging to select text can resize divider bar in Kagi Assistant#8843@CameronLittle
* Kagi Assistant with Kimi K2 ignores accepted answer on a Stack Overflow page#8857@scorchio
* Qwen-3-235B code formatting broken#8840@crhallberg
* Incorrect reference numbers in assistant response#8677@Arahizzz
* Don't copy 'thinking' process#6535@Thibaultmol

## Kagi Maps

* Improved preloading of POI data
* Caching maps search results#8068@Boomkop3
* Map doesn't recenter after dismissing sidebar#8099@tuesday
* Clicking a POI on the map seems to selects closest match, not actual POI#8317@Cybolic
* Kagi Maps ignores 24-hour clock preference and shows 12-hour times#8560@Gilfoyle
* Maps will open POI after dragging or zooming if any finger lifts while touching a POI#8847@Lousy
* Restaurant search near poi seems to miss a lot of locations#7608@Thibaultmol
* Globe off-centre when zoomed out.#8291@tsr
* An option to submit corrections to the map#8281@Boomkop3
* Make sorting preferences stick across searches#8198@Boomkop3
* The after-login redirect doesn't work for maps or assistant#8407@Boomkop3

## Kagi Translate

* Redesigned dictionary
* Translate renders the word "IBAN" using four different fonts#8720@arty
* Add Scottish dialects#8850@dreifach
* RSS feed for Kagi Translate Extension updates#8892@BattleHawk
* (More) Chinese localization tweaks@CTAO

## Kagi News

* Improved story filter to prevent generation of mundane news (non-news) @petelingo
* Less emotional/screaming TTS@hsiktas
* Chaos index experimental feature broken on mobile @xytronix
* Search and content filter should consider sub-category@laiz
* USA | Austin, TX category returns a 404 when navigated to directly @loganmccaul

## Kagi Summarize

* 300+ languages added for mobile users
* Improved layout for right-to-left languages on mobile
* Liquid Glass design for iOS users

## Post of the week

Here is this week's featured social mediamention:

Follow uson your preferred social media platform and tag us with your feedback!

## Oct 23rd, 2025 - Go deeper with Quick Answer#

### Quick Answer gets an upgrade

If you use Quick Answer on Kagi Search, you already know it finds relevant content fast. Now we're taking it even further as a powerful research tool:

Built-in follow-ups. Every answer now comes with three suggested follow-up questions to keep the momentum going.

Seamless transition to Kagi Assistant. Your conversation thread carries over automatically so you can continue exploring instantly.

Mobile now has its own dedicated experience.Use the new full-screen view and input field to ask your next question. You can switch back to the Search results page at any time by tapping the magnifying glass.

The goal is for your research to feel less like a chore and more like following your curiosity wherever it leads.

### Privacy Settings

* As we continue building tools for both greater privacy and anonymity, we wanted to make this information easier to find. Our new dedicated privacy page puts everything in one place: ourPrivacy Policy,Privacy Pass,Tor access, and privacy-preserving payment methods.

### Other improvements and bug fixes

#### Kagi Search

* Improve Lenses UI#6526@HIFBIBER
* Search UI mostly unusable on iOS 26#8701@mcg
* Align quick answer button location to match mobile view#3512@oup_oup_andaway
* Moving from Quick Answer to Assistant#6730@Fernando
* Ability to share quick answer#3383@bert
* Quick Answer follow up questions (Assistant integration)#2093@mackid1993
* The !cpp bang doesn't work#8699@exzombie

#### Kagi Assistant

* Assistant: show the Total cost of a thread#8176@someoneiknow
* Ki failed to respond in a specific scenario: search for scientific papers and create a formatted bibliography#8603@dru4522

#### Kagi Translate

* Expand fictional language support: Dothraki, Na'vi, and High Valyrian#8518@vicky
* Add furigana support for Japanese@benoit
* Chinese localization tweaks@CTAO
* Character-by-character conversion for Simplified ↔ Traditional Chinese (instead of AI translation)#8659@ooh
* Add Korean "문어체" to translation formality style.#8655@gladiator2339
* Add semantic roles in input area@kagiiscool

#### Kagi News

* Single page mode (Sequential, Mix, Random) setting [web]
* Add TTS, Simplifier and Anki flash card generation for Kagi Search subscribers [web]
* Implement sharing [mobile]

### Kagi Maps

* Kagi Maps ignores 24-hour clock preference and shows 12-hour times#8560@Gilfoyle

## October 17th, 2025 - Autumn patch notes & a new Kagi Special#

### Kagi Specials

OurKagi Specialsinitiative is expanding. Today we are addingNotesnook, the privacy-first note taking app.

Kagi members will get a 10% lifetime discount to Notesnook, and Notesnook members will get a complimentary 3-month subscription to the Kagi Professional plan. Visit ourSpecials pageor learn more aboutthis wider initiative.

### Kagi Search

* Every image is flagged as potential AI#8644@Remindful5141
* Kagi News not working#8592@Khyta
* Long page titles exceed page width on mobile#8395@bln
* Reference links in AI assistant difficult to click#8396@MightyPork
* Unable to select date#8421@Temanor
* Currency conversion with space as thousand separator do not trigger widget#3640@Vapid

### Kagi Assistant

* Kagi Assistant Voice input and search button improvements [Mobile]#7233@NathanBreithaupt
* Unclear description for Gemini 2.5 Flash#7034@fxgn
* Assistant answer in language based on geoip#8572@NotableUser772
* Thread renaming UI issue for long titles#8436@dreifach
* Update Kagi's Z AI Model from GLM 4.5 to Newly Released 4.6#8496@vicky
* Shared Assistant Threads Don't Appear in UI Update#8569@iamjameswalters
* Kagi Assistant References Section Broken#8357@markjouh
* Clicking "See Kagi Benchmark" in the tooltip next to "Kagi Recommended" in Kagi Assistant is extremely difficult#8089@wasleyj
* Assistant produces invalid struct tags in go#6748@SvenEngelhardt
* Highlight important points of quick answers when the answer is a definition or explanation.#5180@dotdashdot
* Improve speech recognition in Assistant: setting to keep listening#5591@Thibaultmol
* Pointer cursor for buttons in assistant#8355@greyfivenine8244

### Kagi News

* More granular content language settings [web]
* Keyboard shortcuts [web]193 @farnoy
* Make update status clearer [web]241 @Zerwin
* Add core/community indicators for categories [web]#8461@Woutuuur
* Typography glitch: space-dot at sentence end needs trimming [web/mobile]#8587@Jeanchallet
* Text cuts off [web/mobile]259 @"weierfischen"#6275
* "Kite News" used as a title in RSS feeds280 @nzhuk
* Translate 'Today in History' in other languages [web]

### Kagi Translate

* Language complexity setting for translation/proofreading@laiz
* Add Continue in assistant button789@yeddyfit
* Wordstar translation fixes794@tux0r
* Simplified TXT export for translation history792@fotland
* CJK detect language prioritization setting @リボーン
* Definition meaning equivalents @リボーン
* Move romanization directly under input/output on desktop@p0ly60n
* Proofreading adding em-dashes when not present in original text@alexchadwick
* Translating to simplified chinese leaves some word in the source language@CTAO
* Dictionary throwing "Failed to search dictionary. Please try again."#8651@kayo

### Kagi on Socials

Here is this week's featured social mediamention:

Follow uson your preferred social media platform and tag us with your feedback!

### Kagi around the web

* David Pierce of The Vergedescribed Kagi Newsas "simple, straightforward, super useful."
* Watch Cory Doctorowtalk about the journey to finding a "magical" search experience with Kagi on the inaugural episode of The Honest Broker video interview series. You can alsocatch himtalking about Kagi on Adam Conover’s podcast.
* Listen to our founder Vlad on Monocle Radioannounce Kagi's upcoming SlopStop initiativeto help combat AI slop on the web(min 19:26).
* Kagi News also had ashout outon MacSparky: "If you want to stay informed without the doomscrolling, Kagi News is worth trying."
* We enjoyed readingthis comprehensive postabout Kagi News by Esor Huang.Read with Kagi Translate.
* After two years with Kagi, Michael Peter shares hispositive experienceand reflects on upgrading to the Ultimate plan: "I’m surprised I didn’t do it sooner. The AI assistant is really good and fits perfectly into my browser workflow."

### Industry news

* Meta plans tosell targeted adsbased on data in your AI chats
* Google AdsUsed to Spread TrojanDisguised as TradingView Premium

### Community creations

The creativity of the Kagi community amazes us as always! Thanks to Remy Wang, you can nowread Kagi News on Playdate:

### Kagi art

With Kagi, you're always the customer. Never the product.

## Sept 30th, 2025 - Kagi News#

## Announcing Kagi News!

Todaywe’re officially introducing Kagi News:a once-a-day press review that cuts through the noise. Global stories, community-curated sources, and zero tracking. News the way it should be.

#### What can I do with it?

* Get athoughtful daily press review, tailored to your interests and reading pace
* Exploreup to 12 key stories per category— choose global news, local coverage, or both
* Dive intointernational perspectivesfrom major global outlets
* Orfocus on local newsfrom a specific country, with content curated from its national press
* Read any articlein your preferred languagewith built-in translation
* See every storystructured clearly: Summary, Highlights, Key Quotes, Timeline, Context, and Impact
* Tap once toaccess the original source
* Help shape the feed by contributing trusted outlets to the community-curated platform

#### How It Works

Every day at 12:00 KT (Kagi time), we deliver a fresh press review based on your preferences.

#### Built on Values You Can Trust

✨ No surveillance, ads, or trackers🌍Open-source curationby the Kagi community🧠 Designed to empower you, not exploit your habits

#### Download it now on

App Store:https://apps.apple.com/app/kagi-news/id6748314243Play Store:https://play.google.com/store/apps/details?id=com.kagi.newsWeb:https://kite.kagi.com/

We'd love to hear your feedback onhttps://kagifeedback.org

## Improvements and bug fixes

### Kagi Search

* Wikipedia red links in widget#8343@Numerlor
* Enable paste for reverse image search#8292@ssg
* YouTube search results missing in Kagi video search#6579@Peter
* Kagi Index has a result for Bing Search#8406@fxgn
* Image search for common words in Japanese will bring up NSFW sites if SafeSearch is on.#7032@eai04191
* Summarizer doesn't work and gives an error#8321@ItsLiwads
* Currency conversion with space as thousand separator do not trigger widget#3640@Vapid

### Kagi Assistant

We've added several new flagship models to the Kagi Assistant.

* For Ultimate subscribers:Claude 4.5GPT-5 Codex
* Claude 4.5
* GPT-5 Codex
* And for all users:Grok 4 FastDeepseek v3.1 Terminus
* Grok 4 Fast
* Deepseek v3.1 Terminus
* Kagi Assistant Temporary Mode#6728@joeyeamigh
* Ki Assistant is still omitting images in responses while claiming they were generated#8241@lolroger
* Assistant using 2024 as the search year in 2025#8350@blackbird2150
* Gemini 2.5 Pro no longes shows thinking#8370@fxgn
* Clicking the New Thread button should focus the cursor in the prompt box#8297@cheesekeeper
* Syntax highlighting for PHP doesn't work#8007@TomiK

### Kagi Translate

* Add standard/best toggle to Dictionary page
* Stroke count for Chinese characters are incorrect@andelink

## Kagi on Socials

Here is this week's featured social mediamention:Follow uson your preferred social media platform and tag us with your feedback!

## Sept 18th, 2025 - Releasing Ask, a round of product polish, and translation upgrades#

### Kagi Search

* Reduce number of links shown per domain#3500@TheBOT
* Extremely poor image results for "v-tail", when text results are perfect#8178@luked
* Cache or otherwise shorten load time when switching between All/Images/Videos etc#7733@bert
* Links in Wikipedia previews are hard to distinguish from surrounding text on mobile#8028@schuelermine
* Wikipedia summary anchor tag that point to pages that don't exist doesn't do anything#8267@gromgrom
* I can no longer search in ios 14#4838@dox
* After changing domain ratings, do not scroll to top of page#8177@nissa

### Kagi Maps

* Mobile | no information window / can't click POI#7941@Synasenn
* Double clicking POI shows undefined in label#8184@Numerlor

### Kagi Assistant

* Duplicate Entries in Kagi Assistant Sources#7280@roach
* Assistant: Reference Citations#8188@Pleonasm

### Kagi Translate

* Add support for .ws/.ross files@tux0r
* Increase limits for document translation@Lightnin
* Bulk accept corrections on proofread by correction type#8262@Thibaultmol
* Copy button in Proofread copies reverted corrections#8268@fxgn
* Sending Feedback giving an error message@tux0r

### Ask - bash script for quick AI queries in the shell

We open-sourcedask, a lightweight (about 200 lines) shell script for interacting with LLMs through OpenRouterAPI (in the future Kagi Assistant API).

Example usage:

ask command to find files larger than 100mb

# Output: find . -type f -size +100M

ask ffmpeg command to convert mp4 to gif

# Output: ffmpeg -i input.mp4 -vf "fps=10,scale=320:-1:flags=lanczos" output.gif

Check it out here.

### Kagi Specials

We're excited to introduceKagi Specials, where we spotlight privacy-first companies that share our values: no surveillance, no ads, no data selling, and providing special offers on these services for Kagi members.

Our first featured special isEnte! It's an end-to-end encrypted photo and video storage service that ensures only you can access your memories.

For users who value privacy, Ente is a perfect complement to Kagi, and Kagi members will get 25% off for the first 12 months.Read moreabout this initiative and keep an eye open for upcoming specials!

### Kagi on Socials

Here is this week's featured social mediamention:

Tag our accountsor use #Kagi when mentioning us in your posts!

### Kagi around the web

* Jarrod Blundysharessome appreciation forKagi News.
* JTR also shares their positive impression ofKagi Newsand theSmall Web.
* Mats Staugaard writes agreat reviewof Kagi in Norwegian.Read with Kagi Translate.
* A concisepost in Germanhighlighting the usefulness of Kagi Summarize.Read with Kagi Translate.
* Edward Kiledjianexpresseswhy he moved away from Google Search and the switch to Kagi, specifically noting: "it was about choosing a search experience that aligns with my values: privacy, control, and quality."

### Industry news:

* Google must pay $425 million in privacy lawsuit
* Threat actors abuse adtech companies to target users with malicious ads

## September 4th, 2025 - Kagi Summarize goes mobile, Kagi Assistant adds source attribution and study mode#

### Announcing proportional source attribution in AI answers

We built technology that provides proportional content attribution in AI answers.

This helps you understand the importance of each source in forming the final answer.

More importantly, this technology paves the way down the road for Kagi to share profits with publishers participating in our AI answers. This would happen automatically for all websites, with no deals, no contracts needed.

Try itKagi Assistantnow.

### Announcing Kagi Summarize for mobile

We're launching the Kagi Summarize mobile app foriOSandAndroid!

What can I do with it?

* Save time by reading long articles and getting straight to the point
* Reorganize an article’s structure into key takeaways
* Native integrations into share flows on mobile
* Multilingualarticle transformation to your preferred language

Download it now on

* App Store:https://apps.apple.com/app/kagi-summarize/id6748308326
* Play Store:https://play.google.com/store/apps/details?id=com.kagi.summarize

We'd love to hear yourfeedback!

Demo:

### Study mode in Assistant

We're introducing our take onstudy mode: a Kagi Custom Assistant designed to guide your learning journey through active discovery. Using Socratic method, evidence-based learning techniques, and collaborative exploration, it helps you uncover answers rather than simply providing them.

Please note that the Kagi Study Custom Assistant is available only on the Ultimate plan, as it relies on premium models.

### Kagi Search

* Going to the edit lens menu makes "Edit" the current lens#7426@fxgn
* Typo and english text in French localization on kagi 100 searches page#8132@Sandbank2737
* Improver url encoding in kagi bangs#8078@hisham
* More menu not positioned correctly / not fully visible on smaller windows width#8076@marc-eu
* Universal Summarizer gives unwanted repetition of "summary in 1 sentence"#7892@kfb4e

### Kagi Assistant

* Assistant threads not listed when expired thread is being viewed#6166@kzar
* "Copied to Clipboard" toast when copying Assistant references appears below the text#7974@nick125
* Match LLM card descriptor to Kagi system-wide language setting#7737@dreifach
* Ki Frequently Leaves Out Generated Images#8080@iamjameswalters
* Deepseek V3.1 is showing its thought process.#8092@vlopez
* ResearchAgent cannot search "c++"#8074@kdh8219
* Kagi Assistant PWA icon too large in macOS dock#7933@xx
* Assistant threads not listed when expired thread is being viewed#6166@kzar
* Assistant code flowing out of boundaries#8148@Numerlor

### Kagi Maps

* Middle mouse to open location in new tab#8067@Boomkop3
* Parkings in Maps don't work well#7611@Thibaultmol

### Kagi Translate

* Dictionary mode with settings for context/definition details/synonyms
* Dictionary popup during Translation, when selecting part of the input/output text (Kagi subscribers only)
* Localization for Hebrew & Arabic (RTL)
* Language-specific features in dictionary for Hebrew
* Experimental Translation Context memory feature (Kagi subscribers only)
* Settings/history sync across devices for logged-in users.
* Validation failed when using custom settings for proofreading@Sominemo
* Dark mode getting mixed with light mode under specific circumstances@nfd

### Kagi in Japan

We're honored to join theShibuya Startups programand community in Japan! 🇯🇵

This exciting opportunity came about through meeting Shiho Watabe, the startup hub manager, during our recentJapan visit. We were immediately drawn to their vision of supporting bold, boundary-pushing ideas from the heart of Tokyo's creative scene.

Japan has already become our second highest source of traffic through organic growth, thanks largely toKagi Translate, and we see tremendous potential to deepen our presence there. Being part of this program opens doors to bring Kagi directly to Shibuya's libraries and schools.

### Kagi on Socials

Here is this week's featured social mediamention:

Tag our accountsor use #Kagi when mentioning us in your posts!

### Kagi in the news & around the web

* This videoby EposVox perfectly sums up how when we choose better search engines like Kagi, we get better search results that actually surfacesmaller sitesand content by independent creators.
* Great segment featuring Rory Sutherlandand Kagi's fair pricing model, which you can learn more abouthere.
* We really enjoyed reading thiswonderful reviewof Kagi on a beautifully designed blog.

### Tech corner

Our colleague Jacob does adeep diveinto how we optimized Kagi Assistant to load twice as fast.

### How search engines should work

In collaboration with artistChaz Hutton, we've illustrated what search should be: Zero ads. Zero tracking. Just the results you're looking for.

## August 19th, 2025 - Midsummer patch notes#

### Kagi Search

* Allow for multiple triggers on one entry in the json bang files#5202@Thibaultmol
* Homepage improvements#5251@Thibaultmol
* Domain ranking selection's active option invisible with forced-colors#1841@Seirdy
* Custom bangs delete button has no accessibility label and no confirmation#7565@mehgcap
* Translate website option only with websites in my own language?#7925@marc-eu
* Cant save appearance settings on mobile#7954@breadguy
* Searches returning nonsense AI generated videos#5694@xavierclarkvt
* Twitch channels shouldn't show up in videos tab#6618@RoxyRoxyRoxy
* Latest/Recency ordering not working on image search#7876@loloriz
* Homepage update time and frequency to be clear in kagi.com/news#7912@jamescridland
* Wikipedia widget doesn't honor "correct title"#5394@tuesday
* "Quick Answer" timezone issue#7253@macalba

### Kagi Assistant

We've improved how you can organise your threads with tags. Here's a summary:

* You can add any number of tags to a Kagi Assistant thread
* Threads tagged asTemporaryexpire in 24 hours. If you remove this tag, the thread will be saved.
* If you have enabled"24h mode" in Kagi Assistant, which is the default, all new threads will start with theTemporarytag.
* Saved threads without tags appear underUntaggedin the sidebar.
* Threads you make publicly accessible are tagged asPublic. Removing this tag will make them private.

Plus,

* LaTeX still not working in Assistant#7952@nmh5001

### Kagi Translate

* Pinned languages@Kolobamanacas
* Feedback system (thumbs up/down)
* Add document translation support for RTF, TSV, HTML, ODT, ODS, JSON, YAML, SRT, ASS, ENV, LOG, VTT, MDX, RMD, IPYNB, TEX.
* Document conversion for a subset of document formats
* Settings presets@nichu42
* Broken manifest.json@highseat1691
* 'Best' proofreader model is incorrectly claiming a word doesn't exist#7712@laiz
* Add separate entries for American and UK English for dictionary language@dreifach
* Web translation strips URL parameters#7895@quinncom/@hinq
* Debounce font updates for better typing experience@kotaro
* Russian translation looping character@hovhhxlrlx
* "Laothian" should be "Lao"@redtaro
* Azure's content management policy breaking translation@lssandra3
* Pasting texts sometimes deletes existing input text@anton9
* Full history breaking page@goeo_
* PDF Translation not working@ErikMH
* Definitions appear on firefox, then immediately disappear@Provisional
* Korean localization tweaks@Hanbyeol
* Proofreading replacing german quotation marks#7581@FranziKay
* Translate sometimes picking languages I never used#7639@sshine
* Hide definition under collapsable area on mobile@mjstrasser

### Kagi Maps

* Clicking on place gives no feedback until search finishes#7430@Numerlor
* UK postcodes zooming to wrong area#7836@dreifach
* Change displayed information for postcodes#7837@dreifach
* Clicking on place gives no feedback until search finishes#7430@Numerlor
* Direction switches between miles and KM#6081@steveymacjr
* Open map links in any installed maps application.#7850@shilohfen
* Sticky Description in POI popup#7734@Damp_Cuttlefish
* Kagi Maps bang is useless#5974@KamilKurde
* Using !maps bang with a location doesn't automatically search for that location#6747@pem314

### Kagi on Socials

Here is this week's featured social mediamention:

Tag our accountsor use #Kagi when mentioning us in your posts!

### Kagi in the news & around the web

* Lee Hutchinson wrote agreat in-depth pieceon Ars Technica about making the switch to Kagi.
* Orion getsa prominent shout outby designer Juxtopposed for its wide range of customization options and unique features.
* Our CEO Vlad was interviewedon an episodeof the Intelligent Machines podcast with Leo Laporte, Jeff Jarvis and Paris Martineau.
* Sedat Kapanoğluwroteabout "good people doing good things", using Kagi as an example of a service whose incentives are aligned with its users.
* Writer Dave Pollard mentions Kagi inan articleabout the internet’s "tragedy of the commons," using it as an example of a functioning digital commons.
* Listen to Vlad on theMac Power Userspodcast with David Sparks and Stephen Hackett talk about what Kagi offers its customers and its role as a powerful alternative to products offered by tech giants.

### From the Blog

Free search isn’t actually free. You’re just paying with something else.Read why paying for search is worth every penny.

### Industry News

The true cost of "free" ad‑supported search isn't mere annoyance, it's also real loss of money and time. ACBS Chicago segmentshows how scam ads are flooding results and hurting users. That's why Kagi is and will always remain ad‑free.

## July 31st, 2025 - Kagi Assistant gets tags, bulk actions, and much more#

### Kagi Assistant

This week's release brings several big updates to Kagi Assistant, laying the groundwork to exciting new chapters ahead.

Introducing tagsTags let you organise your Kagi Assistant threads. Each thread can have multiple tags.

* You can use theTemporarytag to mark any thread as temporary, and it will auto-delete 24h after its last update.
* If you use Kagi Assistant in 24h mode, all new threads will be tagged asTemporaryby default. When you remove theTemporarytag, that thread will be saved.
* When you create a thread while viewing a specific tag, the new thread will automatically inherit that tag.
* Threads without a custom tag, such as all your currently saved threads, appear in theAllfolder.

Learn more on ourhelp page.

Bulk managing threadsWe've also made thread management easier: select multiple threads and either tag them or delete them permanently.[upl-image-preview url=https://kagifeedback.org/assets/files/2025-07-31/1753986178-528658-image.png]

Model pickerThe model picker now features a curated set of base models that we believe deliver the strongest performance, helping you choose the best option for your specific task. We continuously update this list using our ownin-house benchmarking.

Define your default AssistantYou can nowdefine your default Kagi Assistant model, as either one of your Custom Assistants, a base model or the last used model. Every new thread you create will start with that default model.

Removal of context windows limitsKagi Assistant no longer enforcescontext window limits. We include all available information, and if we reach the model’s maximum size, we carry forward relevant context so it remains available for your next instructions.

Plus many other fixes and improvements

* LLM selection drop-down menu filter issue#7739@dreifach
* I don't know which language model to choose in Assistant#7538@Recast
* Various Mistakes in Assistant Model Descriptions#7685@Vage
* Assistant search result link embedded in<img>tag#7736@Numerlor
* Kagi Assistant “info boxes” not visible on iPad#7684@Nyaa
* Tracking User Use of Assistant#7276@Alligator
* Model price and ranking tooltip for model selection drop-down menu#7461@Alvir
* Make the word 'refresh' a refresh button in Assistant response WIP message#7787@Thibaultmol
* AI cost in model picker/sort models by cost#7354@fs1010
* Kagi Assistant Model Cheatsheet#6940@oup_oup_andaway
* Folders in assistant#5080@Arlo
* Add new Assistant thread orginization options.#6138@UniquePixels
* Need better assistant thread management#6246@gladiator2339
* Better Kagi Assistant UI to preserve threads#6609@sarno
* Assistant: Support to group chats into folders#6608@magiruuvelvet
* Kagi Assistant multi-selection#7068@michaeljcallahan
* Kagi Assistant: bulk-deleting threads and other bulk actions#6752@dreifach
* Reveal Search Queries in Kagi Assistant Web Search#6911@snowynest
* Add an option to delete multiple Assistant threads simultaneously#5677@Kolorni
* Need better assistant thread management#6246@gladiator2339
* Ability to remove ALL assistant threads#6340@Vapid
* Navigating between versions of the same prompt is broken with 3 prompts after page reload in Kagi Assistant#7134@bsamek
* Add Placeholder Text to the Assistant’s Sidebar#6515@sarno
* Search results for "kagi maps" shows Kagi maps as "N"#7326@phagi
* Readjust Kagi logo in Assistant navbar#5072@Prostagma
* When Ki returns an image, it should provide a source link#6775@Thibaultmol
* Ki needed to be re-prompted to create visualization of data#7244@Alvir
* The assistant is quite slow#7241@atm
* Certain models don't realize what Summarizer can do#7090@Thibaultmol

### Kagi Search

As we gear up for important updates, this release brings a round of improvements and bug fixes,

* Dates in advanced mode filter mislabelled#7655@eigenmagic
* Cut off text on app screenshot#7379@fxgn
* Lenses setting is blank in search options#7296@gen_Eric
* The Videos link does not redirect to the expected page#7777@jeffdaley
* UUID Widget#7446@0xadd1e
* The 'hide stats' button confusingly shows up on pages where it does nothing.#7619@Bodine
* Allow Ranking Adjustments for YouTube Channels#694@SebastianKra
* Issues sub-result when searching "dxvk github" leads to incorrect page#816@carnage
* Speed test font too large on mobile Safari#7793@kirkmc
* Actuality display lens#7786@WTD
* Kagi chrome extension doesn't set Kagi as one of the available search engines on Android#787@shopping2008
* Wrong results appearing in search results#473@GrantRutherford
* Aktion-Mensch wrong preview picture#457@Kai
* Allow buying and redeem gift codes#654@Browsing6853
* Add instant answer for date queries#663@zastrowm
* Suggest other search engines and allow bangs when rate limited#72@Browsing6853
* Search for spotify returns no results#438@benelgar
* Query on mobile displays blank results#309@Kai
* We need a special beta tester query to save money#368@gesumin
* Use old UI#279@mizlan
* Perform math with datetimes and durations in Kagi search queries#7732@menturi
* On kagi news, USA is missing from the region list.#7692@rr
* “Nested” results should be opt-in#500@Sss
* Add "Translate this page" to crystal orb#600@Browsing6853
* Advertise the free tier on the landing page#1446@scvalex
* No results in kagi or bing, only Google#1005@CWagner
* Early Adopter Bonus should apply to all plans#1294@Spirits-
* Discord icon showing up for Fidelity webiste#1241@null
* USA missing from News region list#7692@rr
* News showing 'none' highlights in feed#7701@PineaFan
* Lens 'News' display style won't save#7786@WTD
* PNGs with dark content and transparent backgrounds are unreadable on a dark background#7765@KaiTheBuilder

### Kagi Maps

* More precise results when interacting with map POIs
* Merging of information from multiple sources in search results

Fixes and improvements:

* Fix hours display#7798@mpldr
* Search in maps, select search suggestion from menu, not found#7854@kirkmc
* Opening hours are wildly incorrect#7798@mpldr
* Imrovements to phone number display#7613@Thibaultmol
* Kagi map no longer let's me jump to google maps to get directions#7500@WarrenParad
* Map search didn't work after successfully making a normal query#6097@RonanCJ
* Kagi Maps shows local bookstore closed every day#7576@akaee

### Kagi Android app

Our latest release introduces several quality-of-life improvements, including

* Added a Kagi Assistant button right in the native search screen: faster access, less tapping#7166@COValhalla
* Fixed: tapping 'x' no longer clears your bottom search bar#7677@yk

### Kagi on Socials

Here is this week's featured social mediamention:

Tag our accountsor use #Kagi when mentioning us in your posts!

### Kagi around the web

* Kagi was featured ona listof "Smarter Search Engines to Try in 2025" by PC Mag:

"Good for research, it offers outstanding control over your results, including letting you favor specified domains over others."

* French tech site Clubic featuredan interviewwith Vlad about 7 reasons to try Orion. Read with Kagi Translatehere.
* Cory Doctorow gave Kagi another shout out ina postabout Google's declining quality and spam results:

"It's been more than a year since I gave up on Google Search (I switched to Kagi.com and never looked back). I don't miss it."

## July 11th, 2025 - New News Homepage#

### Kagi Search

Our redesignedNews homepageis now live. You'll find top stories and selected categories featured prominently, so you can quickly access the news that matters most. Updated once per day, spend less time scrolling and more time staying informed. We plan to launch mobile native News experience soon.

Let us know how you like it!

We are still rapidly iterating on the quality of this content & welcome your feedback!

* Regional results are incorrect#7508@kurucu
* AI Images filter, small UI inconsistency.#7660@Synteal
* Strict language filtering produces no search results#7650@batist
* Contrast of team badge in the top left in the start screen is bad in dark mode#7601@Thibaultmol
* Universal Summarizer Couldn't Summarize Podcast MP3#7575@iamjameswalters
* Unable to switch back to 'Current Month' in the usage page after viewing 'Monthly Overview'#7567@laiz
* Members who are not leaders of family plans cannot see the "billing" tab in the settings navigation bar#7418@kdh8219
* Browser Compatibility Request - Firefox ESR 115.24.0 on Windows 7 - Dropdown Menu Issues#7554@NOVALLY
* The Kagi Search logo doesn’t look centred on mobile#7621@xx
* Flight Widget not appearing in correct location on desktop#7553@hmnd
* Wrong Timestamps in the Search Result#7488@yelinaung

### Kagi Assistant

We've added model info boxes that highlight each model’s strengths with scores from theKagi LLM benchmark, so you can pick the best fit for your task without wading through docs. For more in-depth information, see thefull details here.

* Grok4 (preview) has been added for Ultimate subscribers
* When consuming Discourse forum posts in Assistant: use /raw/#7661@Thibaultmol
* No citations or references shown on assistant prompts anymore#7120@mrmanago
* Clarify if Kagi's contract with OpenAI means that OpenAI saves all their chats#7509@Deebster
* Assistant only visits the first link in the message#7097@fxgn
* Assistant error "something went wrong..." when "web access" is selected#6687@Nyaa
* Storage.googleapis.com image reference on assistant response#7574@Numerlor
* Model specific bangs don't work if query empty#7591@Thibaultmol
* Grok 3 Mini performs unnecessary escaping for code output#7533@jogojapan
* Add "bang" field to custom assistant widgets in chat and settings#5282@droserasprout

### Kagi Android app

New homescreen widgets for Kagi Assistant, Translate, and Summarizer -- access in one tap. Plus: smoother performance, cleaner experience, and fixes for the little things. Enjoy!

* Android blank screen when going back from external window#7360@Numerlor
* Add Kagi Assistant to homepage#7166@COValhalla
* After selecting a search category, typing deselects chosen category#7224@Alvir
* Blank screen when going back from external window#7360@Numerlor

### Kagi Translate

* Grammatical Gender, notes, usage over time added to Dictionary
* Navigate to text mode when clicking on a translation history element
* Improved UI on mobile
* More consistent font across devices
* Do not show "Alternatives" title when there are none
* Improved language auto-detection
* Kagi Translate shows stop token in translation#7448@phagi
* Proofreading mode is broken with dark theme, scrolling to text near header is janky@MomentumBuffet

### Kagi on Socials

Here is this week's featured social mediamention:

Tag our accountsor use #Kagi when mentioning us in your posts!

### Kagi around the web

* In one of thelatest episodesof the Behavioral Science for Brands Podcast, Rory Sutherland discusses how Kagi stands out by prioritizing user interests over advertisers - highlighting what happens when search engines put advertisers first.
* Jonathan Margolisinterviewedour CEO Vlad in Air Mail magazine:

At last, a search engine that won’t collect your data and feed you ads.

* Longtime Kagi user wrote agreat guideon customizing Kagi Search with Lenses, Personalized Results / domain ranking to help you get the most out of your Kagi experience.
* Kagi got anice shout outon the Intelligent Machines podcast with Leo Laporte, Mike Elgan and Jeff Jarvis. An interview with Vlad will be on the show soon!

### Industry News

* Beware of the Google AI salesman and its cronies
* TurboTax Quietly Starts Advertising on Perplexity

## June 27th, 2025 - Accessibility wins, regex bangs, relentless bug fixing#

### Kagi Search

#### Accessibilty upgrades

Over the past few weeks, we've made many tweaks to improve accessibility of our settings pages for keyboard users, screen reader users, and users who have JavaScript disabled.

#### Advanced control for Bangs via Regex

We've added an optional "Regex" field to Custom Bangs for more precise control. Instead of$1always being the first word and$2the second, you can now define exactly how your query is split to create more powerful shortcuts.

For example, to create a custom translator for a query like!tr spanish live long and prosper, you can now separate the language from the text. In your Custom Bang settings, you would use:

* Template:https://translate.kagi.com/?to=$1&text=$2
* Regex:(\w+)\s+(.*)

This pattern tells the Bang to use the first word for$1and the entire rest of the query for$2. If you leave the Regex field blank, your Bangs will continue to work as they always have. We're excited to see what you build with this

#### Other bug fixes and improvements

* Site ranking radio buttons have no accessibility labels#7412@mehgcap
* Quick answer bang doesn't work with snaps#5166@Jesal
* Kagi Snaps do not default to domain of custom bang template#6301@__
* Date fields cut off in Safari on iPad#7306@kirkmc
* Give error bang shortcut field empty after sanization#7202@Thibaultmol
* IPv6 address displayed off screen#6659@hugh198
* Color picker copy button cuts off text#6464@Numerlor
* Please add support for -intitle:_____ to exclude results with _______ in the title#2094@conf4tti
* Please scrape the ads/trackers data again#4484@smspoolnet
* On iPhone, it is difficult to edit search field when text is too long#7498@patrick-nicholson
* Kagi's reverse image search is noticeably poorer than other providers#6760@RoxyRoxyRoxy
* Quick answer wrong when asking the same question twice#5506@igc
* Button cut off#7356@Boomkop3
* Reverse Image Search Icon Appears Wrong in Search Interface#7459@Reuzehagel

### Kagi Assistant

* Summarizer is unable to retrieve arXiv PDFs#6988@mrzv
* LaTeX Inline Math not rendering (Gemini 2.0)#7099@Krishy
* The Assistant doesn't seem to quote top search results when searching manually#5615@uppercuts8
* Show error if python code failed in Assistant#6884@Thibaultmol
* Mobile viewport doesn’t account for keyboard in mobile#6961@chrskerr
* Add hover and focus state to assistant buttons#7454@kevin51jiang
* Kagi Assistant doesn't always render LaTeX code.#7449@bhagwad
* Opus 4 thinks it's Sonnet 3.5#7189@WhatMatters

### Kagi Translate

* Proofreading mode improvements (statistics tab, apply/revert corrections, hover to find correction in text/list, all corrections now have explanations)
* Added virtual keyboard for some alphabets
* Language-specific tweaks for Russian, Estonian, Sami (All variants), Afrikaans and Cherokee.
* Fix "Sorry, I cannot complete this request" censorship for some querieshyacinth
* TTS using the wrong accentfbkagirrmiguel
* Enable output controls after text is processed, even if other features are notazdanov
* Regression in RTL supportkaguru
* AM/PM vs 24H clock settingnichu42
* TTS not playing on iOS if ringer is mutedsnowytrees
* Translate is vulnerable to being prompt injectedColonial
* Translation refuses to translate text that is censored in China JP Discord User/Hanbyeol
* Some symbols are escaped as HTML chars in translationUserOfOrion
* Language detection thinks that [アラビア文字] arabic text instead of japaneseJulianGro
* Top bar in mobile Orion/Safari does not follow themeartem
* Auto language switcher not working when pasting output text in source boxAnonymous22
* Korean locale tweaksHanbyeol
* Remove Sami dialects which are meaningless, only keep northern and sourthern variantHanbyeol
* Add login button redirecting to kagi.com on mobilekotaro
* Language switch to Norwegian is broken#7510@Temanor
* Setting to have "Detect Language" as the default source language#7511@Temanor
* Translate screwing up HTML code for < and > symbols#7436@carl
* Translate makes up meanings for short/invalid words#7405@Numerlor
* Context Field in Kagi Translate Causing Internal Error#7543@TusedayGhost/@cictao_85080
* Translation quality is subpar while detecting the language of the text for the first time @cictao_85080

### Kagi Android

* GitHub Authentication in Android App Broken#7111@Tbusk
* Android app: pressing "back" on the main screen doesn't exit app#7210@Ronzino
* Sharing url with the android app summarizer results in "sanitized" strings#7201@Ronzino
* Android app: Tapping on completions usually does nothing#7205@urrlich
* Android app: Speech input broken in both assistant and translator#7206@urrlich

### Kagi Maps

* Map search should prioritize locations on screen, nearby, or selected in search options#7362@vaartis
* Kagi Maps can't find address#7324@Bokai
* Map compass W/E swapped on rotated view#7437@Numerlor
* OSM layer doesn't load when switching on closest zoom level#7463@Numerlor

### Kagi on socials

Here is this week's featured social mediamention:

Tag our accounts or use #Kagi when mentioning us in your posts!

### Kagi in the news & around the web

* Kagi is highlighted in anarticle by Ars Technicadiscussing the potential impact of a search engine spinoff from Google.
* Kagi suggested by Mark Frauenfelder on thelatest issueof Recomendo.
* Review of Kagiby Olly Headey.
* Orionmentioned on Lifehackeron a list of best browsers for iPhone.

### Kagi for Libraries

With the Kagi for Libraries program, we'll offer free access to Kagi for public library patrons worldwide 📚

If your library is interested or you know a local public library that could benefit,encourage them to applyand help us expand this program.

## June 9th, 2025 - Celebrating 50k customers#

## More than 50,000 reasons we keep building

Today marks a special milestone in Kagi's history as we reach more than 50.000 paying subscribers. That’s not just a milestone, it’s 50.000 real humans who looked at the web, saw what we’re trying to do, and said, “yeah, I'm in.” That means everything to us.

As tradition demands, we’ve written a blog post packed with announcements and new stuff:read it here!

Thank you for believing in us. Here’s to the next 50k, we’re grateful to be building something that matters, with you! 🥂

### Kagi Search

* Improving mobile UI for search filters#5868@GrygrFlzr
* Remove .index.html from Summarizer URL#6592@Temanor
* Footer inconsistency#6586@Temanor
* Lenses setting is blank in search options#7296@gen_Eric
* The billing screen seems to struggle with scaling, the numbers and text got cutted#7266@TheLastEnvoy
* Image result thumbnails not loading#7291@ickybus
* Alt text for ranking help on mobile app overflows screen edge#6483@bhazelett

### Kagi Assistant

* Show (estimated) monetary usage of the assistant#6899@dabaldeagul
* Kagi Assistant logo link to Kagi.com#5863@dix
* Cannot add New Lines to Previous Message on Mobile (Enter Key during Edit)#7185@silvenga
* Assistant: Web search can no longer be forced from custom instructions#6845@magiruuvelvet

### Kagi Maps

* Maps: Undefined behavior in the pacific#7216@zwei
* Add more useful selection of Wikipedia Entries Showing on Maps#6527@OJD

## June 2nd, 2025 - Kagi turns 3: past, present, and future#

# 3 years of Kagi!

We are extremely proud and happy to be celebrating three years of Kagi today!

Read everything about where we are as a company and where we want to go inKagi status update: First three years blog post.

## Improvements and Bug fixes

### Kagi Search

* We've updated our control centre on mobile, making it easier for you to navigate between different Kagi products (#4864@Niika,#5140@Prostagma)
* Rank options don't fit in modal window#5887@[deleted]
* Family Pricing page mobile UI is broken#5515@Value7609
* Cannot click on Control Center button in changelog page#7180@papetoast
* Unofficial Mullvad website showing in results#6902@xx
* Interface Detect language Behavior#7200@inesicio

### Kagi Assistant

Since we introduced the Kagi Assistant to all subscriptions and began enforcing fair-use limits, users have requested better visibility on costs. In response, we have added the total token cost per month to thebilling page.

* Assistant: Web search includes domains that are not part of the Lens#6768@magiruuvelvet
* Assistant answer includes citations without links#7141@jogojapan
* Claude 4 Sonnet / Opus Cannot Intake Files#7179@patchmonkey
* Kagi Assistant - Cannot upload images on iOS in Lockdown Mode#6392@pseudonym

### Kagi Maps

We're happy to announce the launch of the (new) Kagi Maps. It's still early days, but we're working hard because maps are long overdue for a major upgrade. Our roadmap is packed with innovative ideas and, most importantly, interesting data to make local mapping meaningful again. Check out the alpha atkagi.com/maps. This is just the beginning.

* !m bang doesn't work @thibaultmol#5946
* Close button on Maps UI is confusing and doesn't work as expected@twingeofregret#6582
* Maps search result layout bugged@Temanor#6587
* UI inconsistency in Kagi Maps@Temanor#6588
* Empty map shows up when searching for nonexistent city@LucasOe#5450
* Wrong wikipedia info with map@speedy#5876
* 'support' link not the right format in the assistant menu in mobile app#5618@Thibaultmol
* Kagi maps: Sitia isn't Syria#4820@Kagibeh

### Kagi Translate

* Kagi Translate: hard limits translated text#5404@OscarZamora

### Kagi on socials

Here is this week's featured social mediamention:

Tag our accounts or use #Kagi when mentioning us in your posts!

### Podcast feature

On the latest Timetable podcast, Kagi CEO Vlad joins Manton Reece to discuss building a user-first, ad-free search engine, why the economics of search are broken, and how Kagi helps you discover hidden gems from theSmall Web- the kind of sites you'd never find on mainstream, ad-driven engines.Listen here.

### Industry news

The latest developments in the tech and search industries that captured our attention and reinforces our mission:

* Get ready for more ads in Google's AI search answers
* Ads Ruined Social Media. Now They’re Coming to AI

## May 22nd, 2025 - Big in Japan#

### Kagi Search

* More intuitive icon to represent a result from the Kagi-index#5800@sw
* When searching "macos", "acos" is interpreted as a calculator expression#6860@synapse
* Zapier integration preventing correct selection of "takeaway", instead forcing "takeaways"#5336@TimMilazzo
* Website Security and Configuration Check for KagiSuggest.com#6937@xx
* Microsoft Bing retiring Search API - What does that mean for Kagi?#7107@[deleted]
* Some channel names don't appear in video searches#5894@Thibaultmol
* Billing Period Tooltip is Partially Hidden#7105@Hanbyeol
* Custom bangs' exclamation mark order not working#7096@dreifach
* Kagi Summarizer extension popup is "hard to read"#7131@Vapid
* Kagi Summarizer browser extension should support dark mode#5179@mojolobo
* Typo in recent news#6938@yarnaid
* Unofficial Mullvad website showing in results#6902@xx
* Using bangs with search suggestions doesn't use the search suggestions#6545@gustav
* On/off switch for redirects#1326@Naymul

### Kagi Assistant

* New models dropped, Ultimate users now get access toClaude 4,Mistral Medium,Qwen 3 (30B, 235B), andOpenAI o3
* No gpt o3#6888@artem
* Kagi assistant - return broken hangul(korean alphabet)#6029@dungsil
* Keyboard pops up after every assistant message#6946@fxgn
* Quick Answer generating innacurate and NSFW responses#4595@Corvana
* 3.7 Sonnet (extended thinking) not following custom instructions#6954@dreifach
* New Assistant layout causes "submit" if you open a menu#7039@Thibaultmol
* Don't open keyboard after selecting thread in assistant (on mobile)#7043@Kiito
* Kagi Assistant redirect to signin page instead of help.kagi.com#7124@0xGingi
* Group saved threads by time period in Assistant sidebar#6680@bausauce
* !chat bang throws an error after yesterday evening's update#7046@m2jest1c
* Images found by Ki image search give CORS errors before image proxy#7062@Thibaultmol

### Kagi Android app

Search from the Kagi widget is now WAY faster 🚀 Plus, we've squashed bugs and added some handy features:

* Share files and images to the app shortcuts#5648@Thibaultmol
* Copy and share link from results page on mobile#6550@Brightart
* Context Menu Fails (App Opens to Homepage)#6697@SamGreenwood1
* Special chars break sharing text#6634@Touko
* App home screen widget is slow to load#6883@WarrenParad
* Clicking a result with no browser installed crashes the app#6549@Brightart

### Kagi Translate

* Translation quality and speed improvements for best and standard modes
* Word dictionary now shows synonyms
* Proofreading mode, shows list of corrections with explanations, style and repetition analysis
* Page height on mobile devices is too large, causes unwanted scrolling#7074
* Custom CSS applying with setting disabled, system theme not respected on page load@electric_eel_maki
* Preserve text while switching between modes@nichu42
* Suggest to switch input language if selection doesn't match the detected one@vaartis
* Pressing enter while in the language selector should pick the first option@bert
* Add UK and US english as different options in the dropdown#7148@Anonymous22
* Ctrl+a selects all text on macOs#7095@laiz
* Kagi Translate refuses to translate NSFW text#7059@ZK
* Kagi Translate mobile layout is suboptimal#6878@DeeKahy
* Text overlapping on iOS/PWA#7045@dartcircle

### Kagi's Japan trip

A look into Kagi's trip to Tokyo, where we connected with the Kagi community, collaborated with local companies and potential partners, and enjoyed everything the city has to offer. A heartfelt thank you to everyone who met with us, shared meals, and made this experience unforgettable!また次回お会いしましょう。

Or view on PeerTubehere.

### Kagi on Socials

This week's featured social mediapost:Tagour accountsor use #Kagi when mentioning us in your posts!

### Kagi in the News

* German tech site Golem featuredan articleabout Kagi being much more than just a Google alternative.Read with Kagi Translate.
* French tech site Just Geek featuredan articleabout Kagi's many features and how it might make you "forget Google."Read with Kagi Translate.
* OMG UbuntucoveredKagi's Orion Browser and its usage of GTK4/libadwaita for its Linux launch.
* Kagi Assistant was mentioned on Computer World's "20 genuinely useful AI apps for Android"list:

Beyond basic queries, its $25-a-month Ultimate plan includes access to something called the Kagi Assistant, which lets you access the underlying intelligence from Gemini, ChatGPT, Claude, and other AI engines in a single streamlined spot and with the added advantage of complete privacy and custom filtering to help refine the results.

* Liam Proven of The Register gives a shout out to Kagi ina pieceabout the enshittification of search:

Another option is to pay for your search engine. We've already mentioned Doctorow once, but his post about Kagi – a no-ads, no-tracking search engine with a tiered payment model – from a year ago makes interesting reading. The idea has gained traction with others, including Daring Fireball's John Gruber.

### Kagi shout outs

* Kagi is described as being best for "power users and professionals who want fast, curated, ad-free results" ina postby Maple Web Design.
* Alan Jacobs shares a concisereviewof Kagi:

Google’s search results have become so bad that I recently subscribed to Kagi, and so far it’s been great.

 

* Have a site or blog and want to have an easier way to search through its archives?This postoutlines a good use of Lenses to make that easier.

A Lens will focus Kagi’s search on one or more (up to ten) particular sites, date ranges, regions, keywords, or file types. You can also exclude sites or subsites. Kagi has several default Lenses, and you can add your own customized Lenses:

* Kagi is used as an example for why it's important topay for what you love, and how it helps align the incentives between the user and the service provider:

In order for Kagi to make more money, they have to make search quality better. By adopting a subscription model, Kagi has fundamentally aligned the goal of the service with providing excellent search. This is why a subscription-based service is the most likely to keep its users satisfied over time, and why — if you care, and if you have the choice — you should choose to use a subscription-based service over other offerings.

* Along those same lines, Liu Miao writes about howpaying for searchoffers a different perspective on using the internet:

Indeed, our generation grew up with the internet, and search engines have been free since their inception. Why pay to use one? But looking at it from another angle, if search engines have been free for over twenty years, then who has been paying for me all this time?

 

And noting specifically about Kagi:

I hope to see more products like this in the future—products that treat users as users rather than as products.

### Industry News

The latest developments in the tech and search industries that captured our attention and reinforces our mission:

* Mark Zuckerberg’s AI ad tool sounds like a social media nightmare
* Google agrees to pay Texas $1.4 billion data privacy settlement
* YouTube announces Gemini AI feature to target ads when viewers are most engaged
* Google is stuffing even more ads into its AI results

### How search engines should feel

In collaboration with artistChaz Hutton, this illustration captures how using a search engine should feel: straightforward and focused, guiding you directly to what you’re looking for.

## May 6th, 2025 - Video search upgrades, enhanced Kagi Assistant experience and more#

## Search

### Video search upgrade

Video search now pulls from more sources and shows richer data:

* See likes / dislikes on videos
* Peertube integration! Peertube results now show up in regular searches, plus you can filter by "source" to see more Peertube content

And other bug fixes and improvements,

* Colour picker does not show correct colour on desktop with Zen Browser#7001@larke12
* Kagi Search: Translate Button Accidental Taps on Mobile#6994@slanderous-mambo
* Web search results broken in Safari#6773@Wildpixels
* 403 when privacy pass is active#6793@jlnslv
* Missing special characters on search results#6876@NeilCarvalho
* Searching "people who know" incorrectly includes images of the pope#6965@mon
* Inconsistencies in Search Settings Descriptions : Period Usage and "Whether or Not"#6991@Hanbyeol
* Raw href text appears in bang popup#7017@erakura
* Shows likes and dislikes for videos#6998@holybaechu
* Searching "people who know" incorrectly includes images of the pope#6965@mon
* Invalid token error on private window in Brave, Firefox#6906@private-kagi

## Kagi Assistant

This release packs important upgrades to make your experience smoother and more customisable:

* Adjustable sidebars: on desktop, you can now resize both the primary and secondary sidebars to fit your workflow
* Mobile revamp: we've upgraded the mobile experience for better usability and flow. Try it out and feel the difference
* Lenses integration: you can now use your Lenses directly in the Kagi Assistant to further guide its search

This update is all about giving you more control and a better experience. Enjoy!

And other bug fixes and improvements,

* Assistant Family Plan#6824@nirvdrum
* Shared assistant threads cannot be accessed without signing in#7004@laiz
* Move model selection to the top of the screen#4945@jonmpd
* Pixtral ignores pre-prompt#6663@nichu42
* Assistant rendering table#6560@Leward
* Add additional models from Mistral.ai#6809@Dexter
* Some languages cause bad ui in Assistant#6929@Thibaultmol
* Kagi Assistant doesn't show links#6962@Peter
* Shared assistant threads cannot be accessed without signing in#7004@laiz
* Assistant reference link text absent#6815@Numerlor
* AI Assistant Timeout Error When Solving Complex Problems#6967@hrayleung

## Kagi Translate

* Fast/Best quality toggle: select quick processing or maximum accuracy
* Add english language varieties to list of supported languagesJR. Automatically switch to/from language, when typing text from "to" language in the input fieldTomA
* Swiss german/high germanbobobo1618
* Import translation historytauon
* Separate setting to specify dictionary languageKurotsuchi
* Voice selection for TTSfrin
* Support RTL languages in text fieldskaguru
* Clear dictionary definition after changing source languagepim
* Show voice gender in dropdownfrin
* Preload essential imagesThibaultmol

## Kagi on socials

This week's featured social mediapost:

Tagour accountsor use #Kagi when mentioning us in your posts!

## Kagi in the news

* Digital Trends features an article about what makes Kagiworth paying for.
* Frandroid, a popular French technology publication, publisheda pieceabout Kagi being an ideal alternative to Google. Read with Kagi Translatehere.
* Spider's Web, a prominent Polish tech site,wrote aboutthe importance of a search engine like Kagi that puts users' interests ahead of ads and other incentives. The article also emphasizes Kagi's dedication to privacy and supporting the small web. Read with Kagi Translatehere.
* Tecnobits featuredan articleabout how Kagi improves your search experience:

Everything you see on Kagi is there because it's useful, not because someone is behind it paying for clicks.

 

## Kagi shout outs

* Neel Dhanesha at the Nieman Lab publishedan article about Kagihighlighting its extensive features and the advantages of having full control over your search experience:

After testing Kagi both as my everyday search engine and as a research tool for a working journalist, I’ve been delighted to find that it’s the search engine equivalent of a Honda Civic: reliable, unobtrusive, and able to get you where you need to go.

* Bart Busschots:"How I Fell in Love with Kagi"

Kagi gives me better results than Google, it lets me pay with money instead of my privacy, and it works great everywhere, even in Safari.

* John Gruber's latest recommendation on Daring Fireball:"Another Periodic Suggestion to Try, Just Try, Switching to Kagi for Search"

Paying for Kagi today feels a lot like paying for HBO back in the cable TV heyday. Part of the deal is that you are paying for ad-free service, yes. But you’re also paying for noticeably higher quality. [...] It’s that good. No ads, no unwanted AI (but very good AI results if you want — just end your query with a question mark), and better search results.

* In this independent test by sizeof.cat, Kagi'sOrion is listed amongst the winnersfor making 0 unsolicited network connections on start-up:

* Orion was also featuredin this listof "Best Browser For Mac In 2025: Top Picks For Speed, Privacy & Features"
* Thomas Clöerwrote abouthow quickly he became a Kagi user after a free trial due to the quality of results. Read with Kagi Translatehere.
* Erwin shared hisinitial impressionsand a review of his experience using Kagi.
* The Liqui AI channel on YouTube has ashort explainerabout Kagi for those "sick of SEO junk, cluttered results, and endless ads".
* Kagi was recommended on the Chaos Lever podcast:"Escaping Google's Grasp: Tools for the Privacy-Minded"

I totally think it's worth the money.

* Paul Knight shares what makes Kagia better search engine:

My inaugural experience using Kagi was eye-opening: on my first search I got a genuine blog post instead of yet another click-bait AI-generated article. Think about it for a second: when was the last time you got someone's personal blog at the top of your search?

## Industry news

The latest developments in the tech and search industries that captured our attention and reinforces our mission:

* Perplexity CEO says its browser will track everything users do online to sell ‘hyper personalized’ ads
* U.S. search ad revenues surged to $102.9 billion in 2024

## Real cost of "free"

A few weeks ago, reporter Aaron Pressmandescribedhow "free" search engines come at an actual financial cost, sharing his journey that ultimately brought him to Kagi.

ArtistChaz Huttonhelped us illustrate how a Kagi subscription can save you money in the long run by eliminating the many hidden costs associated with "free" search engines:

## April 17, 2025 - Kagi Assistant rolls out to all Kagi users#

## Announcements

### Kagi Assistant is now open to all plans

We're happy to announce thatKagi Assistant is now available to everyone, across all subscription plans!

Check ourannouncement blog here.

To use Assistant, head tokagi.com/assistant.

⚠️Note:We are enabling the Assistant for all plans in phases, based on regions starting with USA today. The full rollout is scheduled to be completed by Sunday, 23:59 UTC.

With this release, we are beginning to enforce ourfair use policyto ensure a sustainable, high-quality service for everyone as we expand access. Basically our policy states that you can use AI models based on your plan's value. For example, a $25 monthly plan allows up to $25 worth of raw token cost across all models (there is a 20% built-in margin that we reserve for providing searches, development and infrastructure for the service). This impacts only a very small percentage of users with extremely high usage patterns and is a simple way to control usage, compared to arbitrary usage limits. Our goal is to ensure broad availability without users needing to worry about typical usage. Affected users can currently renew their cycle instantly, with more flexible credit top-ups planned soon.

We're very happy to offer Kagi Assistant as another optional tool to support your work and exploration online. Let us know what you think via ourfeedback forumorDiscord! Also see ourdocumentation for Assistant.

## Release notes

### Search

* The Yahoo Finance bang, eg "<ticker symbol> !yf", now leads to a yahoo.com error page#6778@numbers
* "Share search" button disappears when toggling an image search discriminator.#6172@RoxyRoxyRoxy
* Missing special characters on search results#6876@NeilCarvalho
* Not all search widgets can be disabled#6613@mnly
* Image size search broken for "Extra large" (and other categories, manual values seem to work)#6808@iynaejVcJ
* Quick answer link displayed even when quick answer is visible#6835@jlinder
* Kagi Lenses: Deleting a lens doesn't delete it from the "Active Lenses" list#6742@__
* Desktop images look cropped#6771@mark248am
* Search region dropdown reset when enabling/disabling lenses#6658@Boomkop3
* Landscape view on kagi.com causes the upper part of Doggo to be cut off#6724@laiz
* Suggest 'Web' Option Rename on Search Page#6529@HIFBIBER
* IPv6 Address creates a timer?#6676@speakblanket
* More results should show only when more results are available#3507@xavierclarkvt

### Assistant

* Add OpenAI GPT4.1 models, o4-mini, o3 models and XAi Grok models + Gemini 2.5 Pro Experimental+ Mistral Small 3.1
* Kagi Mobile Assistant: Kagi logo in the top left takes you to Kagi Search, but the logo says "Kagi The Assistant"#6734@__
* Assistant thread titles aren't summarized/updated anymore#6688@krade
* Clicking on the active Assistant thread exits out of the thread#6712@RoxyRoxyRoxy
* Custom Assistant Doesn't Use Lens#6741@iamjameswalters
* Kagi Assistant searching the web on every message#6638@jcf
* Deepseek V3 0324#6719@batuhan
* Assistant: "<summary>" in code output forcibly converted into HTML element#6679@magiruuvelvet
* Assistant: with extended thinking, the </details> close tag is sometimes messed up#6591@DomW
* Sharing Assistant Chats With Non-Kagi Users Doesn't WOrk#6681@iamjameswalters
* Sensitivity in Action Panel Above Assistant Text Field#6625@Tarrek

### Translate

We've launched our brand-new UI and a bunch of new feature to make your translation experience exceptional! We are incredibly proud of the work on this product. Check outKagi Translate.

Improvements and bug fixes:

* Enhanced alternative translations now provide insight about the main translation
* Dictionary entries can now appear in the input box
* Added 81 languages to the supported listsome-userAdemalhanolu
* If you can't still find the language you are looking for, you can just type it injvbf
* Default Target Language option - your locale language will be automatically set as the default "translate to" language instead of it defaulting to the last one you used.
* New website translation views - while translating a website, you can now view both the original and translated versions in a horizontal or vertical split. Drag your mouse in the middle to resize the iframes to your liking.
* Audio download now available for translationspeterfgalbraith
* Can't type correctly using an IMEining
* URL field not having same padding as language fieldRoxyRoxyRoxy
* 1password trying to auto complete context field incorrectlyfrin
* Corrections counter in proofreading modebatuhan
* Setting to disable custom CSS (inspired bysomeoneiknow)
* Pick what meaning from the dictionary entry to use for translationKurotsuchi
* Increase context max characters limit for Kagi Search subscribersKurotsuchi
* Translator: Kyrgyz shows up twice#6700@Kel
* There is 2 Detect language#6783@batuhan
* Kagi Translate language selection filter not working#6583@psaints
* 3 Norwegian options in Kagi translate#6685@Temanor

### Kagi on socials

This week's featured social mediapost:

Tag our accounts or use #Kagi when mentioning us in your posts!

### Kagi in the news

* Kagi is featured on thePalo Alto Daily in a Spotlight pieceabout the company's background and purpose:

* Lifehacker featured Kagi inan extensive piecedetailing several features to get the most out of your Kagi experience.
* On the Boston Globe, business reporter Aaron Pressman describes the journey that ultimately led him to Kagi, and how "free" search engines come at an actual financial cost:"I switched all my default searches to Kagi."
* Gizmodo author Matthew Gaultshares his journeyto paid search with Kagi:

I resisted this one for a long time, but now that I’ve started using it I can’t go back. Google search is broken and Kagi works like magic.

* City Magazineexplores the future of search engines, discussing how paid models like Kagi could pave the path forward.
* HubSpot'sThe Hustlehighlights how Kagi offers a premium experience for users willing to pay for quality.
* Kagi wasfeatured on de Volkskrant, a Dutch newspaper, about what sets it apart as a search engine. Read with Kagi Translatehere.
* Ars Technica included a shortstatement from Kagiin an article about Apple being barred from testifying in Google's antitrust trial.
* The Knowledge newsletterfeatured Kagias a search alternative with advanced features that is worth exploring.

### Kagi shout outs

* Om Malik has aninsightful piece on search, and mentions being a Kagi user now:

As for me? I’ve voted with my wallet. I now use Kagi for search (and pay for it gladly)

* Author Dave Pollardmentions Kagiin a links of the month post, stating:

I switched to Kagi from the enshittified Google search engine last year, and I’ll never go back. No ads, no sponsored links, no tracking your searches, no selling your data, no clutter.

 

* Parth Shahtested8 search engines, stating the following about Kagi:

Kagi was new to me before this study, but it stood out quickly. It’s a paid search engine with no ads at all. The results were accurate, useful, and easy to read. I also liked the clean layout. [...] Kagi quickly became my favorite.

* The Linux Experiment featured the news ofOrion coming to Linuxin one of theirlatest videos.
* The Naeth wrote athorough review of Kagi, noting how "Kagi’s unique traits set it apart."
* "The Bill, Please" featureda thorough pieceabout why Kagi launched the "no use, no pay" fair pricing model.
* Luke Mayer calls Kagi "the best search engine I’ve ever used" inthis comprehensive review.

Have a Kagi review you'd like to feature? Please share it and ping us on any of ourvarious socialswhen you do!

### Industry news

The latest developments in the tech and search industries that captured our attention and reinforces our mission:

* Google Hit With Lawsuit Over Data Collection on School Kids
* Meta whistleblower Sarah Wynn-Williams says company targeted ads at teens based on their ‘emotional state’

### Search smarter with Kagi

We partnered with artistChaz Huttonon a graphic that illustrates how Kagi empowers you to search without the noise, trackers and distractions. Help us share it widely!

### Tokyo, meet Kagi!

As noted previously, from April 21–25, Kagi’s team, including CEO Vlad, will be in Tokyo 🇯🇵 to meet companies and connect with the local community. If you are a local Kagi user, we'd love for you to join us for casual food&drinks! If interested, please contact Gillian atgillian@kagi.comto arrange.

## March 21st, 2025 - Leveling up the Kagi Assistant experience, meet Kagi in Tokyo, and more...#

## Next chapter in the Kagi Assistant experience

With this release, we'reintroducing a new sidebar, designed to streamline your workflow and keep everything you need within reach. This is just the beginning - the new sidebar lays the foundation for even more powerful features to come.

We're also rolling outClaude 3.7 Sonnet with extended thinkingto tackle even more complex challenges.

As always, we’d love to hear your thoughts - join the conversation onDiscordor share your feedback through our forum athttps://kagifeedback.org

### Kagi, lost in translation, in Tokyo!

From April 21 to 25, a dedicated team from Kagi including CEO, Vlad, will travel to Tokyo 🇯🇵 to meet with companies interested in ouradvanced translationsolutions. If you are based in Japan and your company is interested, please get in touch with Gillian.

We'd also love to meet our local user community while we're there. If you're based in Tokyo, we'd love toorganise a dinner and connect in person. Looking forward to great conversations and good food with fellow Kagi fans!

Please contact Gillian atgillian@kagi.comto arrange.

### Jobs, jobs, jobs

We are looking for aHead of Business Developmentand aTechnical Architect(basically CTO equivalent in Kagi world).

Head out toKagi hiringto apply and check out other open positions.

## Improvements and bug fixes

### Search

Based on the community's feedback, we’ve added a setting to always hide AI-generated images by default (suggested by#5998@keyboardJones). You can enable it onSettings>Search>AI.

* Show search result favicons by default#6393@artem
* User friendly URL does not show for search result#6472@jenese
* Strange interaction between bangs and "#" sign in query#6430@BobLoblaw
* Orca Slicer malware sites in search results#6192@gregatron5
* Universal summarizer gives me gibberish#6462@Tomaz
* Tooltip hovers over search result symbols#6471@jenese
* Expanded image info is squashed together#6544@RoxyRoxyRoxy
* Kagi Search: Image Filter Icons are misaligned from their text#6522@__
* Changelog illustation not optimised for dark mode#6547@RoxyRoxyRoxy
* Summarizer failing even with shortened YouTube URLs#6576@achilles
* Domain settings button is sometimes blank when inline image viewer result is expanded#6543@RoxyRoxyRoxy
* Login QR code not readable on Edge with Dark Reader enabled#6358@YuriySamorodov
* For various searches, the actual podcasts themselves don't appear#5896@Thibaultmol

### Kagi Assistant

* Make Assistant scrolled to bottom of convo by default instead of the top#6099@RoxyRoxyRoxy
* "Pre-prompting" not working?#6525@Dexter
* Indication that a link is being copied in Kagi Assistant#6198@Sidpatchy
* Code-Assistant removes <br> Tag in displayed Code#6555@Lorem
* Issues with the Mistral models (No internet Access and "an error occured")#6398@Dexter
* Assistant doesn't understand "yes" response#5495@beetstabasco
* Assistant's LaTeX rendering breaks due to 조사(Korean postpositions)#6482@kdh8219
* Safari zooms to text field on assistant#5440@snowytrees
* UI Clipping in Kagi Settings#6069@One
* Qwen QwQ thinks everything is dangerous and political and refuses to answer questions#5691@sudoer-777
* Assistant ignores languge of prompt#6493@Maxolino

### Kagi Translate

* Addtokenand other URL parameters to make it easier to use translate in private modeaminomancer
* Fix translation of Catalan traditional timeturly
* IP URLs not being detectedHanbyeol
* Inaccurate one-word translationsnichu42JW
* Copied translation incorrectly removes line breaksLunarWatcher
* Sync translation theme and language from Kagi Searchfrin
* Add section in language picker for most commonly used languagesMarcin
* Fix some words being incorrectly identified as URLsnichu42
* Add support for markdowngoulot_situez
* Clicking a link from a translated website doesn't redirect to translation of that pageRexios
* Alternative translations getting cut offPeter
* Page flashes in light mode theme for a second before turning darknichu42
* Source textarea steals focus while user is typing elsewheretuesday
* Selection of output text is unreliable on Firefoxbkrein
* Load alternative translations for user-selected text in the output boxnichu42
* Text alignment: When user hovers on input text, highlight the corrisponding part in the outputRoxyRoxyRoxy

## Orion browser release: smoother, smarter, and more secure

This week's Orion release brings big upgrades:

🔐 3rd party Password Managers & AdblockWe have updated support for uBlock Origin, 1Password, and Bitwarden extensions.

👓 User InterfaceSeveral improvements concern vertical tabs, the sidebar, and favicons.

📺 Youtube and PiPSeveral improvements enhance the use of Youtube and the Picture-in-Picture feature.

🪲 Crash fixes & StabilityBye bye crashes on launch, instability if the browser stays open for a long time, and freezes.

For all the details, please refer toOrion's changelog.

## Kagi on Socials

This week's featured social mediapost:

Tag our accounts or use #Kagi when mentioning us in your posts!

## Kagi in the News

* The Verge provides anin-depth review of Kagi, describing it as a better vision for search.

* ThisTechCrunch articlementions Kagi as an option for users who prioritize not just a better search experience but also a more privacy-focused search.
* OMG! Ubuntu coveredOrion's expansion to Linux.
* t3n, a German tech magazine, alsofeatured Kagi, highlighting it as a privacy-friendly and ad-free alternative. Read with Kagi Translatehere.

## Kagi Community Reviews

We are deeply grateful to everyone who takes the time to share their experiences, tips, and feedback about Kagi, helping to spread the word and inspire others to discover its value. Here are some recent reviews to highlight:

* Kagi review from Tim Hårek Andreassen
* "Why You Should Give Kagi A Try"by Optional
* Kagi review by Alec
* Review of The Assistantand its privacy benefits in Japanese. Read with Kagi Translatehere.

Have a Kagi review you'd like to feature? Please share it and ping us on any ofour various socialswhen you do!

## The Kagi Way

We partnered with artistChaz Huttonon a graphic that illustrates how Kagi empowers you to search without the noise, trackers and distractions. Help us share it widely!

## March 6th, 2025 - Orion Embarks on Linux Journey & Kagi Doggo Art Celebration#

## Orion's Next Chapter: Linux Development Officially Launched

We're thrilled to announce that development of Orion Browser for Linux has officially started! Our team is working hard to bring the same speed, privacy, and innovation that Mac users love to the Linux platform.

This is an ambitious project that we expect will take approximately one year to complete. Our target is to achieve feature parity with the current macOS version by March 2026.

Want to stay updated on Orion for Linux?Register hereto receive news and early access opportunities throughout the development year.

## Celebrating Kagi's Community Creativity with Doggo Art

This month, Kagi Search is showcasing incredible community-created renditions of our beloved Doggo mascot,

Shoutout to the featured artists—Edin Pasovic,Fangmoder,Eve Davison,Kevin, andLynn—who wowed us with their talent and earned 3 free months of ultimate. This is just the start: we’re making this a regular celebration of independent creators. Full story in ourdocs.

## Improvements and bug fixes

### Search

* Irrelevant Image Search Results#6179@otaviocc
* Duplicate results in "Videos"#6342@dmz
* Add bangs for different Assistant models#6389@RoxyRoxyRoxy
* Summarizer still can't capture Youtube videos' tittles after bug fix#6428@sleepysnooze
* Kagi summarizer outputs same text for both "summary" and "key moments" modes#6414@invisibles0l

### Kagi Assistant

* The new QwQ-32B model just landed in Kagi Assistant—blazing fast and another strong choice for most tasks
* Plus we've implemented multiple improvements and bug fixes forKI, our multi-step reasoning assistant, based on feedback from users in theCommunity Discord
* Ai chat download filename has extra dot at end#6402@widow5131

### Kagi Android app

The latest app release resolves several bugs including,

* Assistant session download does not complete on Android#6404@peppercup
* Kagi Widget does not automatically pull up keyboard upon clicking on it#6287@StevenMarkie
* Android app "web search" shortcut not working#6328@oogl6fhk6
* Android App not Searching#6295@silvenga

## Feb 27, 2025 - Sonnet 3.7 hits Assistant, early access to Ki, TikTok search and major Translate improvements#

### Kagi Assistant adds Sonnet 3.7 and the preview of multi-step reasoning assistant called Ki

We're happy to unveil the latest updates to our assistant experience. This release brings a smoother, smarter, and more intuitive interface designed to make your interactions simpler.Try it out and feel the difference!

We also added Claude 3.7 Sonnet to our model lineup! It's now powering our!codeassistant and plays a key role in our advanced multi-step reasoning model,Kii. Currently in early testing, Ki is available exclusively to ourDiscord communitymembers - join now to get early access (Ultimate account users only)!

And today OpenAI released GPT4.5 - we have already benchmarked it. CheckKagi LLM benchmark.

## TikTok video search

Video search just got even sharper—you can now filter specifically for Tiktok videos.Find exactly what you're looking for, faster.

## We are hiring a Flutter developer!

We just opened a position for a skilledFlutter Developer. Apply now or send someone our way.

## Improvements and bug fixes

### Search

* Show tiktok as a video source in video search#6356@Thibaultmol
* Kagi Search: Using "Quick Answer" on a search query that has an ampersand (&) will ignore the stuff after the ampersand#6085@__
* Unclear Privacy Policy on Search Logging#5276@UnderdogSquad
* Currency conversion, i.e., "100 usd to sek", should display widget#2031@Vapid
* Outage of summarize feature in france#6314@TarekLazaar
* Low quality translated Reddit results#5212@bram
* Summarizer doesn't work with WalletHub#6324@yokoffing
* User submitted themes#6332@Kanx
* Search switching to an earlier search on it's own#6286@Boomkop3
* Errant summary section when conducting specific search#6174@linuxpng
* Kagi Search: When the search suggestions are open, pressing Enter won't search#6147@__
* FastGPT bangs (!fast and !fgpt) redirect to Kagi Search instead of Kagi FastGPT#6167@doggofan
* Can't search for things beginning with capital I#6308@Ludwik
* Summarizer can't capture Youtube tittles#6281@sleepysnooze
* Improve performance results page#5250@Thibaultmol
* Can't apply region with keyboard#6185@goulot_situez
* Kagi Search: "More" button is misaligned when using the "Larger" font#6063@__
* Unclickable link on Wikipedia sidebar widget#6266@RoxyRoxyRoxy
* "exact match" for reverse image search#6036@Thibaultmol
* Publish date for news search is in a language different from the interface language#5437@huey
* CSS toggle and Status removed from the Control Center in Assistant#6250@Temanor
* Images widget blank on mobile#6243@tuesday
* Asking "WNBA standings?" in kagi gets everything wrong#4245@alexisd
* New York is a European city according to Kagi Quick Answer#4378@xx
* "Quick Answer" not recognizing outdated information#5086@Kagibeh
* Same image appears in any search regardless of terms#6382@dabluecaboose

## Assistant

* Ability to download Assistant response files
* Asking AI on Kagi-ChatGPT (for example) is different from asking ChatGPT directly. Why is this?#6136@Paato
* Can't use 'Gemini 2.0 Flash'#6302@jyyen
* Claude Efficiant Tool Usage Beta#6364@HRA42
* Assistant "Document Size Exceeded" Error for 4mb picture#6370@blackbird2150
* Adjust Saved Code Snippet File Extension#6378@pophob
* "Ask questions about page" doesn't open Assistant#6108@mullinggroove
* Mac Kagi Assistant shortcuts not working#6343@miicat_47
* Make title of Assistant reference a hyperlink#6350@RoxyRoxyRoxy
* Kagi Assistant Downloads as .html#6207@lloyd094

### Translate

Try Kagi Translate athttps://translate.kagi.com

* If on 'manual' translate mode, do a translate when the user changes target language#6037@Thibaultmol
* Improve Korean Localization#5305_334,#5305_329@Hanbyeol
* Don't show alternative translations in JP, if the only thing that's changed from original is the pronunciation being added.#5305_328@frin
* JP romanization is sometimes incorrect/overly formal#5305_328#5305_323@frin
* German (Switzerland) translations using the wrong "ss"#5305_314@psy-q
* Translated text sometimes put into quotation marks#5305_306@nichu42
* Disable/export/delete translation history#5305_308@ajimix
* CTRL+A should only select the translated text, not whole page#5305_316@RoxyRoxyRoxy
* Add Hawaiian to list of supported languages#5305_320@Bradh
* Change URL params when translation is completed#5305_323@frin
* While proofreading hindi, strike/correct whole diacritic / ligature. @aldehyde.8578
* Document translation: translate your .doc(x), .txt and .csv documents
* Alternative translations: along the main translation, show multiple translation options
* Word insights: fine-tune individual words or phrases
* https://translate.kagi.com/iso_codenow redirects to the main page, with thetolanguage being set to [iso_code].
* Make tooltips appear immediately, adjust style
* Dynamic text size depending on length in input/output box
* Increase max size of request header to allow longer romanization requests
* [Forgot to credit last time] Add translation context field#5305_253@Kate-Karui

### Kagi on Socials

This week's featured social mediapost:

Tag our accounts or use #Kagi when mentioning us in your posts!

### Kagi in the News

* The Vergecovered Kagi's recent Privacy Pass feature.
* Privacy Pass was also mentioned on multiple podcasts, includingEnterprise Security Weeklyand Techlore'sSurveillance Report.

Interested in covering Kagi on your outlet, newsletter or podcast? Hit us up! Our team is very approachable and we welcome any opportunity to engage with various communities about our latest features.

 

## 13th Feb, 2025 - Redefining Privacy in Search#

## Announcing Kagi Privacy Pass

Kagi now supportsPrivacy Pass, anIETF-standardized protocolensuring your searches are technically unlinkable to your account.

Read all about why this matters and the details of implementation in ourannouncement blog post!

Privacy Pass support is provided:

* Natively forOrion browserusers (macOS/iOS/iPadOS). On iOS, make sure to have version 1.3.17 and above (expected to roll out globally today) and update your macOS Orion to version 0.99.131.
* Natively throughKagi App for Android(make sure to have version 0.29, expected to roll out globally today)
* Browser extension forFirefoxorChrome

A few important details:

* Privacy Pass implementation isfully open-sourcedfor transparency and community collaboration
* Kagi Privacy Pass is available for the Professional, Ultimate, Family, and Team plans.
* Limitations:It's not available for Trial/Starter plansPrivacy Pass mode disables account-specific features, like domain personalisaton (as we do not know which user is searching)Privacy Pass mode is supported for Kagi Search in this initial phase, we will add support other services in the coming weeks. Check theblog post FAQsection for more details!
* It's not available for Trial/Starter plans
* Privacy Pass mode disables account-specific features, like domain personalisaton (as we do not know which user is searching)
* Privacy Pass mode is supported for Kagi Search in this initial phase, we will add support other services in the coming weeks. Check theblog post FAQsection for more details!

Kagi is redefining privacy in search. Try it now!

## Kagi Tor Onion service

Access Kagi securely and anonymously via our new Tor Onion Service.

You can now access Kagi directly through the Tor network using our dedicated onion address:

kagi2pv5bdcxxqla5itjzje2cgdccuwept5ub6patvmvn3qgmgjd6vid.onion

See more information about Kagi Tor service in ourdocumentation.

## An updated comprehensive privacy policy

We're also excited to share ourupdated privacy policy, with simplified language and designed to clearly reflect our strong commitment to protecting your privacy.

## Improvements and bug fixes

### Search

* Quick Peek Breaks after Clicking More Results#6016@silvenga
* Add option to save the mobile advanced settings state#5826@miicat_47
* Analytics for kids accounts do not show name/username#6189@kingtong
* News search sorting issue#6187@Alastair
* Kagi maps finds Texas in Alaska#5904@Boomkop3
* News Search has no headings, not accessible to blind users#6140@gordon582
* Escaping <br/> in IP Widget#6225@silvenga
* Ranking adjustment info popup contains raw HTML#6241@frereit
* Quick answer code snippets display broken (sometimes)#6224@lelovsky
* Images widget blank on mobile#6243@tuesday

### Kagi Assistant

* Kagi Assistant now supportsO3 Mini,Gemini 2.0 Flash, andR1 Distill Llama 70B!
* Announce new results from assistant using ARIA Live#5996@fastfinge
* Allow to hide thought process for reasoning LLMs#6025@KamilKurde
* Add o3-mini model to Kagi Assistant#6135@RegChien
* Formatting issues in Reasoning for R1 in Assistant#6148@hansihe
* Assistant should wait with naming a thread until it's finished if not enough info#5828@Thibaultmol
* Space missing below reference list in Assistant downloaded transcript#5833@thomasjsn
* Allow for disabling the CTRL + SHIFT + Backspace shortcut#5550@4P5mc
* Images cannot be pasted into the Assistant on WebKit browsers#6193@laiz
* Info panel not visible for new Assistant UI#6143@azdanov
* The assistant prompt "think about </think> tag" breaks auto-hiding of reasoning text#6181@ssg

### Kagi Android App

Privacy Pass support! You can add the Privacy Pass shortcut by holding the Kagi Android icon.

* The app returns to the main screen every time it re-renders (e.g., entering/leaving split screen)#5875@Philippe_Choquette
* Assistant via Android app doesn't work with multi file uploads#5959@Thibaultmol

### Kagi on Socials

Here is this week's featured social mediapost:

Tag our accounts or use #Kagi when mentioning us in your posts!

### Kagi in the News

Orion tops Apple'sApp Store's listof superpowered internet browsers "to seriously level up your web browsing"!

And Android Policepublished an articleabout Kagi's new fair pricing model: "This ethical search engine will return your subscription money if you don't use it." The Verge alsocovered the news.

/
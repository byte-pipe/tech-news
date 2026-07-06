---
title: Can a URL in a prompt change an LLM's output? | AI Focus
url: https://aifoc.us/influencing-model-output-with-urls/
site_name: tldr
content_file: tldr-can-a-url-in-a-prompt-change-an-llms-output-ai-foc
fetched_at: '2026-07-06T12:20:31.340985'
original_url: https://aifoc.us/influencing-model-output-with-urls/
date: '2026-07-06'
published_date: '2026-07-03T09:00:00+00:00'
description: Testing whether opaque URLs act as pointers to memorized content, and finding that JavaScript-rendered sites may be missing from model training entirely
tags:
- tldr
---

# does a url in a prompt steer an llm's output toward its content?

Published byPaul Kinlanon:July 3, 2026; Reading
time:
22
minutes

Expand to see summary

At first, this was a really easy post to write, but then I discovered some things. Built a lot of things. Spent a lot of tokens… And it became one of the hardest, longest, and most expensive posts I’ve done (the API costs were not small).

I’ve had this thing on my mind for ages and it started when I was thinking about how the mere presence of a technology name in a prompt seemed to bias the output to that technology.

For example, I looked through a number of system prompts for Agentic tooling and they would include text like(e.g. React)and then it felt like these tools would output React code vs a similar prompt that didn’t mention React.

I’ve spent the last few weeks running experiments to scratch this itch. But before I get too far, I have a request for help. I’m not a researcher. I think what I have here is compelling information (or at least it taught me something), but I might have made a lot of mistakes or made assumptions that have biased the output. If you have any advice I would LOVE to hear from you.Email me.

The question I had was: would the presence of a URL in a prompt influence the output of the LLM, based on the content at that URL or the literal text of the URL itself?

If yes, then this could lead to us not having to embed lots of context into the prompt. For example, you might have a Skills file that is deeply integrated into the model’s weights and by saying “use what you know about:https://skills.sh/super-security-reviewerdo a deep analysis” then information in the model’s latent space would bias the output towards the content encoded at that URL.

I came away from this with:

1. A URL in the prompt does influence the output, but only when that URL and its content made it into the model’s training data
2. It’s really unclear how LLM providers gather the data they train on, and I think they should tell us.
3. There’s heaps of data that is not in the models
4. If your site relies on JavaScript to load its content, that content is very likely not in a model (you might consider that a feature). The training crawlers I could verify (ClaudeBot, GPTBot) fetch a page’s assets but never execute the JavaScript; the only verified bot I’ve caught running JavaScript is OpenAI’s search crawler, OAI-SearchBot.
5. LLMs are expensive!

What follows is the journey I took.

The first step was tobuild a system that can analyse a range of URLs across a range of models and use an LLM-as-a-judge to help me test the hypothesis.My plan was:

1. to find each model’s known “Knowledge Cut-off date”
2. then find content on either side of that to test if the model could recall the data that I believe should be known in the model.
3. find ranges of content ranging from content that I believe would be popular all the way to likely esoteric.

Content known to be after a cutoff would help me control against hallucination. If my original hypothesis was correct, then for that content the model should decline, or say it doesn’t know, rather than confidently make something up.

Once I had the data I created a range of tests to help me understand how the models work. The tests are classified as:

1. described: the task described in words, no URL (the baseline)
2. opaque-url: ONLY the opaque URL string, and the page is never fetched
3. mdn-url-only/spec-url-only/bcd-key-only: optional identifier probes, not part of the main comparison
4. url+described: the opaque URL plus the task described
5. full-content/content-only: the real page pasted in, with and without the task spelled out (the ceiling)
6. fake-structural-url/random-url: controls (a nonexistent URL of the same shape, and an unrelated real URL)

opaque-urlwas my real test, to try to ensure that the LLM couldn’t infer the contents from the literal URL string. So for example I used some URLs from chromestatus.com (which is our public dashboard of Chrome features) because it has URLs likehttps://chromestatus.com/feature/5157805733183488, and while I believe it’s pretty clear to the LLM that they are web-related, you can’t infer that it’s about CSS Gap Decorations.

I then had other tests, like descriptive URLs (MDN for example is very descriptive, which is very good UX for the web) to validate whether the literal URL influenced the output, as well as what happens when we add in extra context.

I have a report hereand all thedata is here(iframed too). I think it’s worth looking at, and there’s a pretty clear picture and answer to my question.

My first hunch was thatURLs are not magic context, and the ChromeStatus numbers seemed to back it up. ChromeStatus feature URLs are a good opaque test because the domain tells the model the page is web-related, but the numeric feature ID tells it nothing about what is behind it, and most models failed to recover the right API from that number alone. Adding a bare opaque URL to a prompt did almost nothing on average, and plenty of opaque URLs recovered nothing at all.

But then I had a lot of other URLs that had really good recall, and a lot of other opaque IDs that didn’t. StackOverflow, for one was mixed, and then I looked at theirrobots.txtand it’s pretty much deny everything. Hmm. What’s ChromeStatus’s? I checkedits robots.txtand it looked fine… maybe ChromeStatus URLs are just not in the model for some other reason. For example, one of Chrome’s most popular features,Service Worker, couldn’t be recalled from the URL… It was just odd.

I went to look for what the models use to ingest data, and it’s kinda hard to find the exact corpus of crawl data, but I did remember a podcast from a little while ago that discussedCommon Crawlbeing used as a source of a lot of data. So I went to check if Chromestatus was in the common crawl. It is. The pages show up in Common Crawl about as often as the arXiv papers that decode almost perfectly. But when I pulled the actual crawled bytes, there was no content in them!!!

ChromeStatus is a JavaScript app (I remember it first being built with Polymer) and the crawler captured an empty shell. The saved page for CSS Gap Decorations is about 3KB of HTML with 22 characters of visible text, “Chrome Platform Status”, and not one word about the feature (here is the actual Common Crawl capture). I checked four features and they were all identical empty shells. The arXiv page, by contrast, is server-rendered, so the crawl holds the full title and abstract (its capture).

IfCommon Crawl is a source of data, then I’m going to flat out say that SPAs that require JS to get data to the user are very likely to not be in the models training data (that might be a feature for some folks - heh.) My evidence is that you can watch every model flatline on the bare ChromeStatus id, then recover the feature once handed the actual page,in the per-test view here.

I found a second case that is even harder to wave away, and it doubles as my “controlled” before-and-after. “The Adaptive COVID-19 Treatment Trial” is a good example because it is on clinicaltrials.gov. A couple of years ago the site server-rendered its pages, and Common Crawl’s 2022 capture of the trial is the whole thing: 47,000 characters of visible text, titled “Adaptive COVID-19 Treatment Trial (ACTT) - Full Text View”, with COVID, remdesivir, and placebo all through it (the old capture). Then it appears that clinicaltrials.gov migrated to a JavaScript single-page app. Common Crawl’s 2026 capture of the very same trial is 94KB of HTML carrying 175 characters of visible text, “ClinicalTrials.gov Show glossary Search for terms…”, and not one mention of COVID or remdesivir (the new capture).

One of the most documented trials of the pandemic went from fully present in the crawl to effectively blank. The models still half-recall it from the bare URL anyway, around47% across models, and the reason matters. The NCT id is cited all through the remdesivir literature, and the page was server-rendered and crawlable right up until the migration, so the old content is almost certainly already baked into the weights. What the migration breaks is the future. Anything clinicaltrials.gov publishes from here on renders only in JavaScript and will probably never make it into the crawl. So being missing from Common Crawl is not the same as being missing from the model. It’s more of a sliding scale: a server-rendered, widely-citedCVEover at NIST comes back from the bare URL about 92% of the time, this trial (a shell now, but crawled for years and still cited everywhere) about 47%, and a ChromeStatus feature (rendered in the browser and cited nowhere) a flat zero.

This whole space is murky, and rendering is what muddies it most. Ilabelled every test URLby whether its content sits in the raw HTML or only shows up once JavaScript runs, then looked at recall from the bare URL. The 31 client-rendered items, mostly ChromeStatus features, average 6% recall, and 25 of them are a flat zero. These are not obscure features either (view-transitions, popover, anchor positioning, the Temporal API). The 60 server-rendered sources (arXiv, CVEs, RFCs, Wikipedia) average 55%. Hold fame roughly constant, and content that was already in the HTML recalls about nine times better than content a browser has to assemble.

I really wanted to kill the “maybe it just wasn’t crawled” doubt entirely, so I tried a case where the content is beyond question in the model. Every Wikipedia article has an internal numeric id you can address directly:en.wikipedia.org/?curid=24544is Photosynthesis. The content is server-rendered and unquestionably in every model. But the?curid=form of the URL is in none of the crawl indexes I looked at, while the canonicalen.wikipedia.org/wiki/PhotosynthesisURL is in all of them (200, full text), because Wikipedia points the curid page at the canonical title URL and the crawler respects that. I checked five articles; every/wiki/present, every?curid=absent. Ask by name and the models score perfectly, paste the article in and they score perfectly, give the bare numeric id and wah wah, a fat nope. Same shape on all five:Photosynthesis,the Transformer,Mitochondrion,HTTP 404,Bitcoin.

So the bare opaque URL mostly does nothing. But there are two cases where a URL clearly does pull its weight, and neither of them contradicts the ChromeStatus story.

1. Descriptive URLs influence output. If the URL contains words likeReact,fetch, ortext-justify, those words are just normal prompt text, and the model uses them like any other token.
2. Some famous opaque identifiers really do decode. Landmark arXiv IDs,classic RFCs, andwell-known CVEsrecover their content surprisingly well from the bare identifier alone. From justarxiv.org/abs/1706.03762, with no other hint, the models reconstruct “Attention Is All You Need” and the transformer (every model on that bare id). That looks less like “the URL points to live content” and more like “this identifier and its content appeared together often enough in the training data to be memorized”. And it’s a gradient, not a switch: the decoding is strong for famous identifiers and fades steadily as the content gets more obscure, down to roughly nothing for the long tail. You can watch that gradient directly with GitHub commits. The famous first commits toLinux,Git, andBitcoindecode from the bare SHA, whileordinary routine commitsfrom the same kinds of repos return nothing at all. The knowledge cutoff bites the same way. Anything published after it is gone, even for otherwise well-known sources.

This is the part that gets back to my original question about React. Everything above asks the model to decode the URL on command. But the thing I really wanted to know was whether a URL just sitting there in the prompt tilts the output, the way mentioning React in a system prompt seems to tilt code towards React. SoI ran a second experimentwhere I never told the model to use the URL at all.

The setup is a neutral brainstorm task, something like “I’m putting together a short talk about memorable software security incidents, suggest one worth covering.” Into that, I dropped one of four things into the same ambient slot, framed as “a tab I happen to have open right now”:

1. nothing, the baseline, how often does the model land on this item on its own?
2. the item’s opaque URL
3. a random real URL, unrelated to the topic, does any link nudge it, or only the right one?
4. the item’s descriptive name, like “the Log4Shell vulnerability”, the React analog, words actually in the prompt

I ran this across five models (Claude Opus, Gemini, GPT, Grok, GLM) and 39 items covering security incidents, landmark ML papers, web features, web standards and biomedical literature. An LLM judge reads each answer and decides whether the model actually surfaced the thing behind the link. I had to tighten the judge up because my first version was getting fooled: models would repeat the URL back at me, or say “I see you have RFC 9701 open but I can’t tell you what it is”, and that was getting scored as a pass. It’s not a pass, the model has to show it actually knows what’s behind the link. And to be clear, I never ask the model to use the link, it’s just sitting there in the prompt.

With a famous CVE link sitting there as an open tab, the model raised that exact vulnerability almost every time, when otherwise it would have picked something else. A random link did nothing, essentially the same rate as no link at all.Across the set, the off-hand URL lifted the topic from about 7% (no URL) to 45%, and the descriptive name did better still at 83%, which makes sense, it is real words the model can read. So a memorized URL doesn’t just answer when you ask about it, it tilts the output just by being there. That’s my React question answered, but only for the URLs the model has already memorized.There’s a recall matrix on the results pageshowing exactly which URLs decode on which models, and why: identifier type, training cutoff, and what Common Crawl actually captured.

Here’s an actual run so you can see it. The prompt asks for a security-talk suggestion and the xz backdoor’s NVD link is just sitting there as an open tab. No model picks the xz backdoor without the link, every model picks it with the link there, and Opus even says “I notice you’ve got it open already”. The judge’s verdict and the full prompt are in the run.

(My third favourite of these isRFC 1149, the April Fools’ standard for carrier pigeons: no model brings it up unprompted, and four out of five recall exactly what it is from the bare URL.)

The controls make me more confident this is about memorized content and not the URL itself. In the ambient test an unrelated real URL sat at 6%, next to the 7% no-link baseline. And back in the direct tests, a fake URL of the same shape and an opaque-shaped fake identifier both scored near zero too. So it’s not just having a URL in the prompt, or having one that looks right, it’s whether the real content was in the training data.

One caveat so I don’t oversell the crawl angle. Stack Overflow blocks the crawler, so none of my Stack Overflow questions are in Common Crawl at all, yet the famous ones still decode from the bare question URL. Stack Overflow clearly reaches the models another way, most likely its openly licensed data dumps. The crawl is one source among several. ChromeStatus is the clean failure because its content is missing from the crawl and isn’t reposted anywhere else either, so it never made it into training by any route.

When I stopped pointing at the content and just pasted the page in, the models did fine: the bare ChromeStatus URL recovered almost nothing, and the actual page text got most of the way to a correct answer. If you want a model to use a page, give it the page, not a link to it. So the answer is not “URLs never matter”. It is: a URL matters when it’s readable text, or when the exact identifier appeared often enough in training to be memorized along with its content. For the long tail of opaque URLs, I would not rely on the URL alone as context. Which is exactly the problem for the idea I started with: askills.sh/super-security-reviewerpointer is, by definition, new and niche, the long-tail case where none of this works.

Here is the part that actually stuck with me, and it has nothing to do with URLs. ChromeStatus is close to home for me: it’s Chrome’s own dashboard of the web platform, I helped build the very first versions, and its entire job is documenting the platform from Chrome’s perspective. Yet it contributes almost nothing to what these models know, because it renders its content with JavaScript and the crawler only ever saw an empty shell. That is not a knock on the team or the content. The site was built as a JavaScript app years before anyone knew that crawlers which never run JavaScript would end up deciding what an AI learns, which is exactly what makes it such a clean example. The page is public. It is crawled. Its robots.txt allows it. And it is still effectively absent from the model.

If that is true for ChromeStatus, it could be true for a slice of the modern web. Single-page apps, JavaScript-rendered docs, anything that assembles its content in the browser: a crawler can get the URL and come away with nothing but a loading shell.

So I went back to Common Crawl, this time not to look up individual pages but to measure how common these blank shells actually are. Istreamed a big sampleand counted the pages a model would see as blank. Counting by “too little visible text” needs an arbitrary cutoff, so the number I trust uses none: a client-rendered page ships its app mount empty (a literal<div id="root"></div>waiting for JavaScript) where a server-rendered page has already filled it. Across about 1.04 million pages from 88 crawl files,0.45% were empty mounts like that. (A looser text-based count lands near 1.2%, but I keep that next to its sensitivity sweep because the cutoff moves it. 0.45% is the floor.) These are not small files: shells average about 53KB of HTML, all bundles and markup with almost no text. The biggest buckets are pages with no attributable framework, then jQuery building its DOM on load, then Next.js.Full breakdown and the exact crawl files are in the dashboard.

I also ran it twice, on the February crawls a year apart, to see which way this is going, and it is getting worse rather than better. The threshold-free empty-mount rate rose from 0.38% to 0.45% year over year, and the looser text-based estimate from 0.94% to 1.21%. Both measures, over more than a million pages each, move in the same direction. The blank slice of the web is growing, not shrinking.

It gets worse the more popular the site is. Joining each page to a domain ranking, the shell rate climbs from 0.86% across the long tail (unranked domains) to about 2% in the 10k-100k band and 2.5 to 2.8% among the top 10,000 sites. The polished, well-funded, modern front of the web is the part most likely to be a blank shell in the crawl. And that gap is widening: a year earlier the top-1k shell rate was 1.6%, and now it is 2.5%. So this is not a problem of obscure sites being neglected; it is the opposite. (Every number here is from a sample I have published, including the exact list of crawl files used, so it can be re-run and checked.)

Being absent from the training data is a real discoverability problem, and I don’t think it is well understood yet. There is a lot more to dig into: does the rate differ between providers, given some of them run search crawlers that do execute JavaScript? I would be glad if this nudged someone to take it further.

So I went looking for what the model providers actually say about how they collect the web, and the answer is very little.Anthropicdescribes a general-purpose crawler (ClaudeBot) that follows the robots.txt guidelines, but says nothing about whether ClaudeBot renders the pages it fetches (my own traces, below, say it downloads the JavaScript and CSS and never executes any of it).OpenAIsays its models are trained on publicly available data, alongside data from partners and from its own users.Googlesays Gemini is trained on publicly available web documents. Every one of them tells you they crawl the public web. Not one of them tells you whether the crawler runs JavaScript, and that single detail decides whether a huge part of the modern web makes it in at all. I would like to see that in the model cards.

That last question, whether a crawler even fetches the sub-resources a page depends on, is one I am now testing directly. I put together a small site,uatracer.com, that hands every visit a unique set of asset URLs (images, CSS, JavaScript, fonts) and records which of them actually get requested, along with whether any of the on-page JavaScript runs at all. The idea is to watch a named crawler arrive and see, per agent, whether ClaudeBot or GPTBot or Googlebot pulls the whole page down and executes it, or just takes the HTML and leaves. It is early, but it’s the same problem seen from the crawler’s end: if a bot never fetches your JavaScript, it was never going to see anything that JavaScript renders.

Early analysis is interesting, and the first lesson was that I can’t trust a User-Agent string on its own. It’s trivially spoofable, so ua-tracer checks every bot against the IP ranges its operator publishes, and that caught something straight away: the first “ClaudeBot” that ran JavaScript in my traces was a fake, its IPs are nowhere in Anthropic’s published list. Sticking to verified traces only:

* ClaudeBot(verified) does not run JavaScript, which is the important bit, because it fetches nearly everything else a browser would: the CSS, the JavaScript files themselves, module scripts, images, fonts, the manifest, the preload and prefetch hints, and it even parses the iframe’s HTML and grabs the image inside it. But it downloads the stylesheet without parsing it (it never follows thebackground-imageor@font-faceURLs inside), and the classic script and ES module it downloaded never executed (here’s a verified trace). Just because a bot downloaded your JavaScript doesn’t mean it ever saw what it renders.
* GPTBot(verified) goes one step further: it fetches the same set and it does parse the CSS, following thebackground-image, the@font-facesource, and an@import. Still no JavaScript execution.
* OAI-SearchBot(verified) is the surprise: it arrives with a full Mac Chrome user agent and actually runs the page, both the classic scripts and the ES modules. So OpenAI’s search crawler renders JavaScript, while its training crawler does not.
* ChatGPT-User fetched the page and ran nothing, and OpenAI publishes no IP ranges for it, so its identity can’t be checked at all.
* Googlebot is documented to render pages in a second pass with headless Chromium, but I can’t confirm it from my own data yet: the only “Googlebot” trace so far failed IP verification (another fake), and the real one hasn’t visited.

I’ve written the crawler side up in more detailon my blog.

There’s a slow-burn experiment hiding in there too. Every trace on uatracer.com mints a unique, opaque URL (something likeuatracer.com/trace/GS6aE5u1) that exists nowhere else on the web, and the crawlers are fetching those pages right now. So in a year or two I can run this whole experiment in reverse: hand a future model one of today’s trace URLs and see whether it can tell me what was behind it. I planted the URLs, I know exactly what each page contains, and I log which bot fetched which trace, so if a future model recalls one, that would say something about whose crawl feeds whose model. Though I’ve now contaminated that one myself: by linking a trace URL earlier in this post next to text describing exactly what it contains, I’ve done to it what the internet did to 1706.03762. The clean canaries are the thousands of traces nobody ever writes about. The identifiers in this post started as things I could only observe from the outside; these ones I seeded myself.

It feels like a gap everyone is sleep-walking into. Developers ship sites that look perfect in a browser and are blank to a crawler, and never find out. Providers train on a web that quietly drops a chunk of itself, and won’t tell you which parts they can and can’t see. Both are easy to miss. Both are fixable. But only if you know to look.

If you run a site and you care whether models know it exists, the safe move imo is to server-render your content, or at least make sure the content you care about is in the HTML before any JavaScript runs.

So I took my own advice, starting close to home. Precisely because I care about ChromeStatus and the data inside it, I builtchromestatuslite.com, a server-rendered view over the same Chrome Platform Status data. Same release log, same deprecations, same per-feature detail, but the words are in the HTML before a single line of script runs, so a crawler that never executes JavaScript still walks away with the actual feature instead of an empty shell. It is a small thing, and it does not fix the source, but it is the difference between this stuff being in the next model or not. If the real site is going to render in the browser, the least I can do is leave a server-rendered mirror that the crawl can read.

So, did I answer my question? Does a URL in the prompt influence the model’s output? At one point I said no, because the ChromeStatus URLs did nothing. Then the famous identifiers started decoding perfectly and I flipped back to yes. Where I’ve landed is yes, with a condition you can check item by item inthe data: when a URL and its content made it into the training data, the bare URL works as a key into the weights. The model isn’t fetching anything. The string alone recalls the content, and that’s strong enough to tilt answers to questions that never asked about it. When the content never made it in, and for the JavaScript-rendered web a surprising amount never does, the URL is just a string. My skills-file-at-a-URL idea is dead on arrival: its URL is by definition one no model has memorized. But at least I now know why, and the why turned out to be a bigger story than the question.

## Subscribe to the Newsletter

Get the latest essays and projects on how AI is changing the medium of the web delivered straight to your inbox.

Email address

### Share this post

Share

X

Bluesky

Mastodon

Email

## More essays

### how might a modern lighthouse work with large language models?- 2026-07-03

### please mind the model gap- 2026-06-07

### I think i've got it: WebMCP is the new web intents- 2026-06-06

### building a claw in the browser- 2026-05-22

### shipping a prompt- 2026-05-22

### model half-life- 2026-05-18

### are pwas cooked?- 2026-05-17

### a business in a box- 2026-05-10

### How might a browser be developed?- 2026-05-03

### agent-do: my agent loop- 2026-05-01

### webmcp is the new web intents ... maybe- 2026-04-27

### damn claude, that's a lot of commits- 2026-03-30

### the token salary- 2026-03-27

### the llm whisperer- 2026-03-08

### the prompt is the program- 2026-02-21

### If NotebookLM was a web browser- 2026-01-25

### the browser is the sandbox- 2026-01-25

### projects- 2026-01-02

### hyper content negotiation- 2025-11-27

### headless stopgap- 2025-11-23

### dead framework theory- 2025-10-12

### interception- 2025-09-21

### dangerous- 2025-08-22

### hypermedia- 2025-08-18

### elements- 2025-07-16

### Whither CMS?- 2025-07-05

### token slinging- 2025-06-30

### on-device- 2025-06-12

### AI Assisted Web Development- 2025-06-04

### embedding- 2025-05-28

### Mashups 2.0- 2025-05-24

### latency- 2025-05-22

### A link is all you need- 2025-05-17

### super-apps- 2025-05-12

### transition- 2025-05-09
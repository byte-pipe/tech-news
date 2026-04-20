---
title: Dictionary Compression is finally here, and it's ridiculously good
url: https://httptoolkit.com/blog/dictionary-compression-performance-zstd-brotli/
site_name: tldr
content_file: tldr-dictionary-compression-is-finally-here-and-its-rid
fetched_at: '2026-02-28T19:08:36.166020'
original_url: https://httptoolkit.com/blog/dictionary-compression-performance-zstd-brotli/
date: '2026-02-28'
published_date: '2026-02-23T13:00:00.000Z'
description: Dictionary compression could completely change how applications send data over the web. It's recently gained broad support, and offers absurd real-world...
tags:
- tldr
---

GO BACK TO BLOG

http

performance

standards

browsers

# Dictionary Compression is finally here, and it's ridiculously good

February 2026
Author:
Tim Perry
opens in a new tab
GO BACK TO BLOG

Dictionary compression could completely change how applications send data over the web. It's recently gained broad support, and offers absurd real-world traffic reductions: initial testing shows YouTube JS download size for returning desktop usersshrinking up to 90%opens in a new tab(!!!) compared to existing best-practice compression, while the Google search results HTML (arguably the most optimized content on the internet)shrinks nearly 50%opens in a new tab.

This works by initializing the (de)compression algorithm with a dictionary of data known in advance to both compressor & decompressor, so that the compressed data can just be references to that directly ("insert bytes 1 - 10,000 from the dictionary") without having to include the original data at all. This is applicable in a surprising number of scenarios, because most data we send (especially on the web) isn't completely novel or unpredictable. Today's JavaScript bundle shares 99% of its content with yesterday's JavaScript bundle - if the browser already has the old one, using that as a dictionary means you can compress down to (approximately) just the differences.

This can work either using a previous response as the dictionary for the next response, or using an explicit custom dictionary; for many kinds of dynamic response, you do know large chunks of the data in advance, like all the keys in your API's JSON response, and many common values that might be included, and you can generate & preload a dictionary defining exactly this to efficiently cover those. In either case, this can drastically shrink JS bundles, WebAssembly files, known-structure API responses, or many other kinds of incrementally updated & diffable content - a lot of the worst offenders for bandwidth usage that have become very common on the modern web.

This is now widely usable, safe to deploy without compatibility concerns, and surprisingly easy to set up.

Here's a quick low-level demo for Node.js (v24.6+ or v22.19+) so you can play with the raw compression directly for yourself:

const zlib = require('zlib');

// A very basic dictionary - a previous API response
const dictionary = Buffer.from(
 '{"type":"event","source":"server-2","status":"active"}'
);

// A new response we want to compress:
const dataToCompress = Buffer.from(
 '{"type":"event","source":"server-1","status":"inactive"}'
);

console.log(
 "Compressed data size without dictionary",
 zlib.zstdCompressSync(dataToCompress).length
);

console.log(
 "Compressed data size with dictionary",
 zlib.zstdCompressSync(dataToCompress, { dictionary }).length
);

Even in a toy example like this, that comes out to 65 bytes with normal Zstandard compression, vs 28 bytes when using the past response as a dictionary -57% smaller.

You're welcome toskip to the meatto get this set up right now, but before we do, let's talk about how this works under the hood, the history and where this is supported today, and then pull back and look at practical setup.

## Under the hood

We're going to focus on Zstandard here, just to keep things simple & focused (and because it's great). When we do the compression from the example above, the output is:

> console.log(zlib.zstdCompressSync(dataToCompress, { dictionary }));
<Buffer 28 b5 2f fd 20 38 9d 00 00 58 31 69 6e 61 63 74 69 76 65 22 7d 02 00 80 93 3c 2a 20>

What does this little string of hex actually mean?

* 28 b5 2f fd- this is a Zstandardmagic numberopens in a new tab, so we know this is Zstandard data.
* 20- Frame header description, with no dictionary id (we didn't include any dictionary name metadata) and the single-segment flag set.
* 38- Hex 0x38 = 56 in decimal. This is the final size of the decompressed data.
* 9d 00 00- Data block header, telling us we're about to read the last (and only) block of data, and it's 19 bytes long.
* 58- Start an 11 byte 'literals' section (raw content, which the decompression process will read from to build the output).
* 31 69 6e 61 63 74 69 76 65 22 7d- in ASCII, this decodes as1inactive"}.This is the only actual data from the input included in the output.
* 02- Start the sequences section (LZ77opens in a new tabdecompression instructions).
* 00- The compression mode is FSE - this is how the following instructions are encoded.
* 80 93 3c 2a 20- The decompression instructions. These are very complicated and tightly packed, but roughly work out as:Copy 33 bytes from the dictionary at offset 0: everything from the start to...server-Copy 1 byte from literals:1Copy 12 bytes from dictionary at offset 34:","status":"Copy 10 bytes from literals:inactive"}
* Copy 33 bytes from the dictionary at offset 0: everything from the start to...server-
* Copy 1 byte from literals:1
* Copy 12 bytes from dictionary at offset 34:","status":"
* Copy 10 bytes from literals:inactive"}

(Somewhat simplified, but you get the gist)

I think there's two notable things here: firstly, compressed data comes with a disproportionally large amount of overhead in small examples like this, and secondly, very very little of the original data is included here, so despite that overhead it ends up tiny. By pulling data directly from a dictionary, the vast majority of the original content we're compressing never actually appears in the output at all.

As you might imagine, as data gets larger the proportional overhead reduces drastically, and you get asymptotically closer to just distributing a diff between your data and the dictionary. In this kind of scenario, this is effectively a mechanism to efficiently deliver deltas between data, that's already tightly optimized & built-into browsers and backends you already use. Neat!

## How did we get here?

Compressing data with custom dictionaries like this isn't especially new as a concept. It's existed at least back tothe zlib rfcopens in a new tabin 1996. However, until now use cases were relatively limited, as the DEFLATE (the compression algorithm that zlib wraps) comes with quite a few limitations like a tiny 32KB maximum sliding window, meaning you could only use a very small dictionary, and once you've processed another 32KB of data the original dictionary is out of the window & unusable. Maybe OK back in 1996, but not practical for much recently.

The larger problem though was that zlib lost the HTTP encoding war. Bothgzip(meaning gzip-wrapped deflate) anddeflate(meaning zlib-wrapped deflate) were standardized as options for thecontent-encodingheader in HTTP, butdeflatewas incorrectly implemented by Internet Explorer and IIS (thanks Bill) creating a compatibility mess, so everybody stuck withgzipwhich actually worked reliably everywhere (but didn't support custom dictionaries).

In 2008, Google made a shot at custom dictionaries on the web anyway, introducingShared Dictionary Compression for HTTPopens in a new tab(SDCH) powered by theVCDIFF delta algorithmopens in a new tab, including it in the very first version of Chromium, and using it on their own sites. This didn't really go anywhere, with no other browser implementations and little other usage on the web. The main issues here were privacy & security concerns, such as dictionary ids being used as a global cross-site tracking vector, and the uncertainty & caution around new compression options at the time, as attacks likeCRIMEopens in a new tabwere showing how compression could leak secrets in surprising ways. SDCH was also much more specialized, as VCDIFF is an algorithm for file deltas specifically, not a general purpose compression tool, and the lack of HTTPS usage meant middleboxes messing with headers & recompressing content could cause enormous problems as well.

SDCH wasremoved entirelyopens in a new tabwith minimal fanfare in 2017.

In addition to all those good technical reasons, the real killer for SDCH was the rise ofBrotliopens in a new tab. The Brotli RFC was published in 2016, and included a fixed dictionary specifically designed to cover many core web use cases, blowing gzip performance out of the water by compressing common web content 10-20% better (although slower to do it, so generally used for static pre-compressed content). My impression is this took the last gasps of energy away from SDCH, shifting the performance focus in Chromium fully onto Brotli instead, and nailing that coffin for good.

So now lastly, bringing us up to the current day, a new competitor emerged in the form ofZstandardopens in a new tab. Zstandard offers different state-of-the-art tradeoffs (almost as effective compression as Brotli, but much faster to do it) and with custom dictionary support from day 1, standardized in2018opens in a new tab. Brotli added its own official custom dictionary support in 2023 as well, and both algorithms now have standardized & reasonably widespread browser support.

That means all of a sudden nowadays we have a great pair of compression algorithms (very-efficient but slow Brotli, and pretty-efficient but super-fast Zstandard) which are widely supported everywhere on the modern web, and most importantly: both support custom dictionaries.

## Where can I use dictionary compression today?

To actually use this, you need two things:

* An implementation that supports custom dictionaries on both sides.
* A way to coordinate both sides on the dictionary you're going to use.

If you want to use this entirely within your own codebase, coordination is generally fairly simple, so you just need implementations. There's been some great progress there recently. My understanding of the current state of things is:

* In Node, Zstandard with custom dictionaries comes built-in as part ofzlibin Node v24.6+ and v22.19+. Basic Brotli support has been around longer, but custom dictionary support wasjust mergedopens in a new tabrecently, so should be landing in the next releases.
* In Python, Zstandard with custom dictionaries comes built-in ascompression.zstdopens in a new tabfor Zstandard as of Python 3.14, and there's a popularBrotliopens in a new tabpackage on Pypi as well.
* Rust has mature popular packages for bothZstandardopens in a new tabandBrotliopens in a new tabboth including custom dictionary support.
* JVM has mature packages likezstd-jniopens in a new tabandBrotli4jopens in a new tab
* Go, .NET and others have less clear options, but plenty of libraries in the space, and often bindings to the native zstd/brotli libraries that can be used directly.

You do need support on the decompression side as well. If that's elsewhere within your systems, great, however if it's in a browser then for now this is only available in Chrome 130+ (and related browsers: Edge, Brave, etc). That said, both Safari & Firefox have public plans (hereopens in a new tabandhereopens in a new tabrespectively) to support this as well so hopefully this will be universally supported soon.

Fortunately, you can start using it today even just for your Chrome users, because the browser proposal for this is designed around automatic negotiation of the dictionary to use. The standard for this is known as:

## Compression dictionary transport

This is anIETF standardopens in a new tabdefining how clients & servers should distribute and use custom dictionaries, with Zstandard and Brotli, over HTTP. In the minimal case, the key step looks like this:

Client sends:

GET /some/content HTTP/1.1
[...other headers...]
Available-Dictionary: :abcdefabcdefabcdef:
Accept-Encoding: br, zstd, dcb, dcz

That means:

* Here's the SHA-256 hash of the best dictionary I have for this request (encoded as base64, enclosed in colons - this isstructured field byte sequence formatopens in a new tab).
* Here's the encodings I support, e.g. dictionary-compressed Brotli (dcb) and dictionary-compressed Zstandard (dcz).

Then, if the server agrees to use the requested dictionary, it might send:

HTTP/1.1 200 OK
Content-Encoding: dcb
Vary: Accept-Encoding, Available-Dictionary

...a stream of data compressed with Brotli
using the abcdefabcdefabcdef dictionary...

If the server doesn't have or doesn't want to use that dictionary, it can reply in any other normal way, just like today. It's entirely opt-in on both sides, so it's safe to deploy now.

Note though that theVaryheader here is important - that is an existing standard that tells any caches en route that this response depends on the request headers listed, and so any future requests with different values there (e.g. any requests asking for a different dictionary) should not be given this response from the cache.

This leaves one open question though: how does the client get the dictionary? There's two options:

1. The server can add aUse-As-Dictionary: match="/file/pattern/*"to any existing response. This tells the client it should save this response as a dictionary, and offer it later for matching requests.
2. You can add link relations (e.g. aLink: ...HTTP headeropens in a new tabor a<link ...>HTML elementopens in a new tab) withrel="compression-dictionary"to tell the client to actively fetch a separate dictionary file. That file can then be served withUse-As-Dictionaryto configure it.

The latter is largely relevant if you're planning to use a custom dictionary (building a custom file to maximize dictionary applicability & efficiency, instead of reusing existing content). See theBuilding your own custom dictionarysection below for more details.

That's it! There's a few bonus things to note:

* You can add ids to dictionaries, in addition to just using the cache, withid=...inUse-As-Dictionary, in which case the client will send it back to you in aDictionary-IDheader with the request.
* This is all only usable on the same origin. This solves the privacy concerns with SDCH: you can't share dictionaries across origins in any way, so in terms of tracking they're only as capable as a first-party cookie.

## Putting compression dictionaries into practice

Ok, the important bit, how do you actually implement this right now?

Let's assume you're interested in the most obvious use case: JavaScript bundles. For simplicity, let's say you have one JavaScript bundle athttps://website.example/js/bundle.jswhich frequently changes in small ways, and you'd like to use dictionary compression to avoid resending every single byte from scratch every time, reducing this download size by 80% or so for returning users. Here's an outline of the setup steps:

1. Store your old bundles somewhere your backend can reach them. You need to organize them either by SHA-256 hash, or by some tightly linked id (e.g. git commit). This could be a folder on disk, an S3 bucket, or an internal cache service. You could keep the last few months, every version ever, or just the last few days depending on how often users generally return to your site.
2. Have your backend serve your JS bundle withUse-As-Dictionary: match="/js/bundle.js". Insert wildcards here (/js/bundle.*.js) here if the name can vary (e.g. if you use a hash or version or similar in the filename). Append, id="your-id"if you want a distinct id for each dictionary for easier reference.
3. If you receive a request for this path with anAvailable-Dictionaryheader, see if you have the matching bundle available (looking it up by hash, or use the id from theDictionary-IDheader).
4. If you find a matching bundle, and you support a dictionary-compression (dcbordcz) that the client has sent in theirAccept-Encodingheader, then compress the content using this dictionary and send them the resulting tiny response.

Here's a rough outline for Express & Node.js, using Zstandard (dcz):

const express = require('express');
const fs = require('fs/promises');
const zlib = require('node:zlib');
const { promisify } = require('node:util');

const zstdCompress = promisify(zlib.zstdCompress);
const app = express();

const currentBundle = await fs.readFile('./dist/current/bundle.js');

async function getPreviousBundle(base64Hash) {
 // ...Lookup past bundle version from the hash somehow...
}

app.get('/js/bundle.js', async (req, res) => {
 const rawAvailableDict = req.get('Available-Dictionary') || '';
 const acceptEncoding = req.get('Accept-Encoding') || '';

 // Extract the base64 hash from the structured field (e.g. :hash:)
 const hashMatch = rawAvailableDict.match(/^:(.+):$/);
 const dictionaryHash = hashMatch ? hashMatch[1] : null;

 let dictionary = null;
 if (dictionaryHash) {
 dictionary = await getPreviousBundle(dictionaryHash);
 }

 if (dictionary && acceptEncoding.includes('dcz')) {
 // If we have a matching dictionary, and the client supports it, use it to
 // compress the content:
 const compressedBundle = await zstdCompress(currentBundle, { dictionary });

 res.set({
 // Confirm that you're using the dictionary:
 'Content-Encoding': 'dcz',
 // Tell caches not to reuse this for requests without this dictionary:
 'Vary': 'Available-Dictionary, Accept-Encoding',
 // Tell the client it can use this as a dictionary as well later on:
 'Use-As-Dictionary': 'match="/js/bundle.js"'
 });

 return res.send(compressedBundle);
 } else {
 // No dictionary - just send as is. You probably want to do some other
 // non-dictionary compression here depending on what the client supports.

 // But still, tell the client they can use this as a dictionary in later
 // requests for the same path:
 res.set('Use-As-Dictionary', 'match="/js/bundle.js"');

 res.send(currentBundle);
 }
});

This should immediately reduce traffic for returning users using modern Chrome versions (currentlyopens in a new tababout 70% of web clients) dramatically, improving loading times for users client side, and reducing any bandwidth costs or constraints on the server side.

The open question here of course is how to store & access your old bundles. The easiest option is likely adding "push the bundle to S3, keyed by hash" to your deploy step, and then querying S3 for the hash here, with some limited caching in memory to skip the lookup entirely where possible. In time I expect this will become more standard practice with a clearly trodden path, but in the meantime that style of approach seems like a good starting point. Remember of course that the hash is a user-controlled value - don't just stick it in a URL and load the data without validation!

## Building your own custom dictionary

For delta cases, where you're repeatedly delivering changing content and you really want to just transmit the changes, the easiest option is to use your past content as your dictionary as above. Simple and effective. I'm expecting CDNs will start to support this automatically in the not too distant future, since it's a quick win that they're very well positioned to enable (and charge for) to offer big performance boosts.

For other cases though, you may be able to do better than a simple delta: producing a smaller custom dictionary, that's relevant to more requests. Building the right dictionary however can be complex. Fundamentally it's just a bag of data that compressed output can reference without having to repeat it directly ("insert data from dictionary bytes 500 - 10,000 here"), but there are open questions about the efficient dictionary size and how to find and pack the relevant values for each use case. There's a few options for actually building this dataset:

* Generate a dictionary explicitly, using training functionality built into thezstdCLI tool with a large set of example values. This is the best option, if you have a good example dataset of values on hand. Install zstd, then runzstd --train TrainingData/* -o dictionaryName. Brotli doesn't appear to have an official equivalent, but you can reuse a Zstd dictionary (although there are some Zstd-specific tweaks, so it's a bit less efficient) or there are plenty of unofficial implementations floating around.
* Use a known template or example value - if you have a lot of content all related to a single base value (many HTML pages sharing some core content, API responses which all have the same structure) you can use any fixed example of the output or empty template of the structure as the dictionary. The best example is one that contains as much as possible of the data of the other responses, but nothing else, and without internal duplication.
* Write a custom dictionary manually. It's just raw data, no structure required, so if you know lots of values that are likely to appear in your data (e.g. JSON keys & common repeated values) then you can just fill up a file with those directly and call it a day.

In all cases, this is an advanced manoeuvre, and it's very important to test the results in practice and tweak and tune to optimize this. Use the general case Node example from the intro above to quickly compare the performance with & without your dictionary, and test different examples of your data to confirm the dictionary really helps.

## Real-world results

This is all early days (the RFC was officially finished in September 2025) but production rollouts and initial data are starting to appear, along with lots of published numbers from external testing of existing sites.

Digging into thehttparchiveopens in a new tabdata from February 2026, despite the early experimental status there's now real-world high-profile use including:

* Google.com, using a custom dictionary file covering all content on the origin (match="/*").
* Pinterest, applyingUse-As-Dictionaryto all JS on theirs.pinimg.comCDN domain.
* Notion, applyingUse-As-Dictionaryto all JS within the Notion app itself.
* Speedkit, a "website acceleration" product used by people like Swarovski and Hyundai, generating & publishing a custom dictionary file for each of their customers which covers all their assets collectively.
* Connatix, a widely-used embedded video platform, in sites like the Huffington Post and El Tiempo, applyingUse-As-Dictionaryto each JS file.
* Shopify, embedded in sites across the web under/cdn/shopifycloudpaths, using both their JS & CSS files directly as dictionaries.
* Doubleclick and similar 3rd-party ad services, using each of their embedded JS scripts directly as a dictionary.

Most of these don't seem to have published much detailed info on how well it's working for them, except:

* Google, whosayopens in a new tabthis results in a 23% drop in average HTML traffic for Chrome users on the search results page, when including first-time users as well and the overhead of downloading the custom dictionary, increasing to a 50% reduction for returning users.
* Speed Kit, who arereportingopens in a new tabto up 95% compression ratios through their custom trained dictionary approach on their customer sites.

Beyond production deployments, there's plenty of public test results, where people have externally downloaded assets from a site over a period (e.g. two versions a week apart), and then tested the resulting dictionary compression that provides. Lots of these are listed in the original spec proposalhereopens in a new tab. Some notable examples include:

* Youtube's desktop video player's JavaScript bundleopens in a new tab: This is normally 10MB of JS, normally compressed with Brotli down to 1.8MB for transfer. Testing this with dictionary compression, assuming a user visited once and then again 2 months later, reduces that down to just 384KB (78% smaller than plain Brotli). Testing versions only a week apart reduced this even further down to 172KB (90% smaller than Brotli).
* Amazon product listing pagesopens in a new tab: with a large custom dictionary, these shrink 60-70% compared to plain Brotli (e.g. 539KB uncompressed HTML = 84KB of Brotli = 10KB of Brotli with a custom dictionary)
* Yoni Feng rana broad set of external testsopens in a new tabon various popular sites, and found multi-megabyte (!) reductions for WASM-based apps like Figma & Google Earth, which often need to deliver large WASM bundles that frequently change in small ways, along with compression improvements of up to 95% for popular JS-heavy sites like Reddit and Excel online. On the flip side, this did show much smaller benefits for text-heavy minimal sites like Wikipedia, down to just 28% improvement over plain Brotli.
* Loveholidays developed aproof of conceptopens in a new tabusing the technique early on (before official browser support) showing up to 57% reductions in their JS bundle data transfer size using a custom dictionary - training a single dictionary on all past versions of their bundle, rather than using past bundles.

On the flip side however: Discordexploredopens in a new tabusing custom dictionaries with Zstandard to compress websocket messages within their client, manually coordinating the dictionary configurations involved (not using the HTTP headers above, since those don't apply to WebSockets). They found reductions of up to 60% on some messages, but less than 1% on others, and that manual coordination and distribution of dictionaries added too much complexity & overhead to be worthwhile - eventually rolling out plain Zstandard and tweaking their underlying protocol to communicate in deltas natively instead.

## Caveats

Hopefully that's all very interesting and exciting for the future of data transfer. There are a few important things to note here:

* In browsers, this is usable same-origin only. For tracking & security protection, you can't share dictionaries between origins, and you can't load one from elsewhere. If you're hosting widely embedded content, this is still useful, but won't magically get reused across the web in the way you might want (in much the same way that loading your website's JS libraries from a public CDN isno longer helpfulopens in a new tabeither).
* Caches can be tricky - be very careful that you don't accidentally cache dictionary-compressed data and use it in other cases. Recipients without access to the required dictionary won't be able to read the compressed data at all. When using the HTTP headers here,Vary: Available-Dictionary(meaning: only reuse this response for matching requests with the sameAvailable-Dictionaryheader) is your friend.
* Although this is unlikely to make your compression worse, it does add complexity & server processing time, and using your own custom dictionary has a bandwidth cost itself, since it needs to be downloaded separately. This isn't a free lunch, so you'll need to actually test the end results and compare the real bandwidth upsides to the extra complexity & processing required to see if it's worthwhile for your scenario.
* These compression algorithms can beveryefficient - if you're decompressing data with dictionaries yourself, don't forget to add maximum size limits to the output to ensure an attacker can't send you some small data that expands to become truly enormous. That risk already exists with standard compression, but this only makes it worse.
* This allows you to frequently deliver incrementally changing application bundles like JavaScript and WASM much more efficiently. That's great, but remember it only affects the amount of data on the network. It'll still unwrap to the same size at the other end, and the time to actually parse & execute your enormous JavaScript bundle client-side won't change. Please please don't treat this as a license to deliver even bigger piles of JavaScript.

## Wrapping up

Dictionary compression is potentially going to drive a huge change in network traffic, on the web and elsewhere. Our systems have effectively spent years sending the same bytes between the same computers over and over again, and this might just let us stop doing a very significant portion of that. It's very exciting!

Test it out for yourself and see how it works for you, and please do share any feedback or fixes back to this article (PRs welcomeopens in a new tab).

And of course, if you're working on this and you need great tools to debug and test HTTP up close, giveHTTP Toolkitopens in a new taba go - fully open-source, one-click setup HTTP interception for browsers, Node, Docker and more, so you can see every header and byte that you're actually sending.

Suggest changes to this pageon GitHubopens in a new tab

Share this post:

Blog newsletter

Become an HTTP & debugging expert, by subscribing to receive new posts like these emailed straight to your inbox:

An extra form field you should ignore
Sign up

## Relatedcontent

http

March 2025

### HTTP/3 is everywhere but nowhere

HTTP/3 has been in development since at least 2016, while QUIC (the protocol beneath it) was first introduced by Google way back in 2013. Both are now standardized, supported in 95% of users' browsers, already used in 32% of HTTP requests to Cloudflare, and support is advertised by 35% of websites (through alt-svc or DNS) in the HTTP Archive dataset. We've developed a totally new version of HTTP, and we're on track to migrate more than 1/3 of web traffic to it already! This is astonishing progress.

Read more

http

December 2024

### ERR_PROXY_CONNECTION_FAILED errors with HTTP proxies

If you're using a local debugging proxy tool like HTTP Toolkit, you might run into the dreaded "ERRPROXYCONNECTIONFAILED" error in Chrome and other similar apps. This can be a very frustrating and unhelpful error! There's only a few possible causes though, and it's usually easy to fix.

Read more

apis

September 2024

### Designing API Errors

When everything goes smoothly with an API, life is pretty straightforward: you request a resource, and voilà, you get it. You trigger a procedure, and the API politely informs you it’s all gone to plan. But what happens when something goes pear-shaped? Well, that’s where things can get a bit tricky. HTTP status codes are like a first aid kit: they’re handy, but they won’t fix everything. They give you a broad idea of what’s gone wrong, which can help plenty of tools and developers make reasonable assumptions, like:

Read more

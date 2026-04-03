---
title: 'Gwtar: a static efficient single-file HTML format · Gwern.net'
url: https://gwern.net/gwtar
site_name: hnrss
content_file: hnrss-gwtar-a-static-efficient-single-file-html-format-g
fetched_at: '2026-02-16T11:19:18.019710'
original_url: https://gwern.net/gwtar
author: Gwern
date: '2026-02-15'
description: Gwtar is a new polyglot HTML archival format which provides a single, self-contained, HTML file which still can be efficiently lazy-loaded by a web browser. This is done by a header’s JavaScript making HTTP range requests. It is used on Gwern.net to serve large HTML archives.
tags:
- hackernews
- hnrss
---

Skip to main content

compression,Internet archiving

Gwtar is a new polyglot HTML archival format which provides a single, self-contained, HTML file which still can be efficiently lazy-loaded by a web browser. This is done by a header’s JavaScript making HTTP range requests. It is used on Gwern.net to serve large HTML archives.

2026-01-20–2026-01-27

finished

certainty
:
certain

importance
:
4

bibliography

* Background
* HTML Trilemma
* TrisectingDownload Stopping Mechanisms
* Download Stopping Mechanisms
* Concatenated Archive DesignCreationImplementationHeaderDetailsFallbackCompressionLimitationsLocal ViewingRange Request SupportCloudflare Is BrokenAccessing Binary AssetsOptional Trailing DataFECSigning
* Creation
* ImplementationHeaderDetails
* Header
* Details
* Fallback
* Compression
* LimitationsLocal ViewingRange Request SupportCloudflare Is Broken
* Local Viewing
* Range Request SupportCloudflare Is Broken
* Cloudflare Is Broken
* Accessing Binary Assets
* Optional Trailing DataFECSigning
* FEC
* Signing
* Metadata
* IP
* Further Work


Archiving HTML files faces a trilemma: it is easy to create an archival format which is any two of static (self-contained ie. all assets included, no special software or server support), a single file (when stored on disk), and efficient (lazy-loads assets only as necessary to display to a user), but no known format allows all 3 simultaneously.

We introduce a new format,Gwtar(logo; pronounced “guitar”,.gw⁠tar.htmlextension), which achieves all 3 properties simultaneously. A Gwtar is a classic fully-inlined HTML file, which is then processed into a self-extracting concatenated file of an HTML + JavaScript header followed by a tarball of the original HTML and assets. The HTML header’s JS stops web browsers from loading the rest of the file, loads just the original HTML, and then hooks requests and turns them into range requests into the tarball part of the file.

Thus, a regular web browser loads what seems to be a normal HTML file, and all assets download only when they need to. In this way, a static HTML page can inline anything—such as gigabyte-size media files—but those will not be downloaded until necessary, even while the server sees just a single large HTML file it serves as normal. And because it is self-contained in this way, it is forwards-compatible: no future user or host of a Gwtar file needs to treat it specially, as all functionality required is old standardized web browser/server functionality.

Gwtar allows us to easily and reliably archive even the largest HTML pages, while still being user-friendly to read.

Example pages:“The Secret of Psalm 46”(vsoriginal SingleFile archive—warning: 286MB download).

# Background

Linkrotis one of the biggest challenges for long-term websites. Gwern.net makesheavy use of web page archivingto solve this; and due to quality problems andlong-term reliability concerns, simply linking to theInternet Archiveis not enough, so I try to create & host my own web page archives of everything I link.

There are 3 major properties we would like of an HTML archive format, beyond the basics of actually capturing a page in the first place: it should not depend in any way on the original web page, because then it is not an archive and will inevitably break; it should be easy to manage and store, so you can scalably create them and store them for the long run; and it should be efficient, which for HTML largely means that readers should be able to download only the parts they need in order to view the current page.

# HTML Trilemma

No current format achieves all 3. The built-in web browser save-as-HTML format achieves single and efficient, but not static; save-as-HTML-with-directory achieves static partially and efficient, but not single;MHTML,MAFF,SingleFile, &SingleFileZ(aZIP-compressed variant) achieve static, single, but not efficiency;WARCs/WACZsachieve static and efficient, but not single (because while the WARC is a single file, it relies on a complex software installation likeWebRecorder/Replay Webpageto display).

An ordinary ‘save as page HTML’ browser command doesn’t work because “Web Page, HTML Only” leaves out most of a web page; even “Web Page, Complete” is inadequate because a lot of assets are dynamic and only appear when you interact with the page—especially images. If you want astaticHTML archive, one which has no dependency on the original web page or domain, you have to use a tool specifically designed for this. I usually use SingleFile. SingleFile produces a static snapshot of the live web page, while making sure thatlazy-loadedimages are first loaded, so they are included in the snapshot.

SingleFile often produces a useful static snapshot. It also achieves another nice property: the snapshot is asingle file, just a simple single.htmlfile, which makes life so much easier in terms of organizing and hosting. Want to mirror a web page? SingleFile it, and upload the resulting single file to a convenient directory somewhere, boom—done forever. Being a single file is important on Gwern.net, where I must host so many files, and I run so many lints and checks and automated tools and track metadata etc. and where other people may rehost my archives.

However, a user of SingleFile quickly runs into a nasty drawback: snapshots can be surprisingly large. In fact, some snapshots on Gwern.net are over half a gigabyte! For example, the homepage for the research project“PaintsUndo: A Base Model of Drawing Behaviors in Digital Paintings”is 485MBaftersize optimization, while the raw HTML is 0.6MB. It is common for an ordinary somewhat-fancy Web 2.0 blog post like aMedium.compost to be >20MB once fully archived. This is because such web pages wind up importing a lot offonts, JS, widgets and icons etc., all of which assets must be saved to ensure it is fully static; and then there is additional wasted space overhead due toconvertingassets from their original binary encoding intoBase64text which can beinterleaved with the original HTML.

This is especially bad because, unlike the original web page, anyone viewing a snapshotmustdownload theentire thing. That 500MB web page is possibly OK because a reader only downloads the images that they are looking at; but the archived version must download everything. A web browser has to download the entire page, after all, to display it properly; and there is no lazy-loading or ability to optionally load ‘other’ files—there are no other files ‘elsewhere’, that was the whole point of using SingleFile!

Hence, a SingleFile archive is static, and a single file, but it is notefficient: viewing it requires downloading unnecessary assets.

So, for some archives, we ‘split’ or ‘deconstruct’ the static snapshot back into a normal HTML file and a directory of asset files, usingdeconstruct_singlefile.php(which incidentally makes it easy to re-compress all the images, which produces large savings as many websites are surprisingly bad at basic stuff like PNG/JPG/GIF compression); then we are back to a static, efficient, but not single file, archive.

This is fine for ourauto-generated local archivesbecause they are stored in their own directory tree which is off-limits to most Gwern.net infrastructure (and off-limits to search engines & agents or off-site hotlinking), and it doesn’t matter too much if they litter tens of thousands of directories and files. It is not fine for HTML archives I would like to host as first-class citizens, and expose to Google, and hope people will rehost someday when Gwern.net inevitably dies.

So, we could either host a regular SingleFile archive, which is static, single, and inefficient; or a deconstructed archive, which is static, multiple, and efficient, but not all 3 properties.

This issue came to a head in January 2026 when I was archiving the Internet Archive snapshots of Brian Moriarty’s famous lectures“Who Buried Paul?”and“The Secret of Psalm 46”, since I noticed while writingan essay drawing on themthat his whole website had sadly gone down. I admire them and wanted to host them properly so people could easily find my fast reliable mirrors (unlike the slow, hard-to-find, unreliable IA versions), but realized I was running into our long-standing dilemma: they would be efficient in the local archive system after being split, but unfindable; or if findable, inefficiently large and reader-unfriendly. Specifically, the video of “Who Buried Paul?” was not a problem because it had been linked as a separate file, so I simplyconverted it to MP4and edited the link; but “The Secret of Psalm 46” turned out to inline the OGG/MP3 recordings of the lecture and abruptly increased from <1MB to286MB.

I discussed it withSaid Achmiz, and he began developing a fix.

# Trisecting

To achieve all 3, we need some way to download only part of a file, and selectively download the rest. This lets us have a single static archive of potentially arbitrarily large size, which can safely store every asset which might be required.

HTTP already easily supports selective downloading via the ancientHTTP Range query feature, which allows one to query for a precise range of bytes inside a URL. This is mostly used to do things like resume downloads, but you can alsodo interesting thingslike run databases in reverse: a web browser client can run a database application locally which reads a database file stored on a server, because Range queries let the client download only the exact parts of the database file it needs at any given moment, as opposed to the entire thing (which might be terabytes in size).

This is how formats like WARC can render efficiently: host a WARC as a normal file, and then simply range-query the parts displayed at any moment.

The challenge is the first part: how do we downloadonlythe original HTML and subsequently only the displayed assets? If we have a single HTML file and then a separate giant archive file, we could easily just rewrite the HTML using JS to point to the equivalent ranges in the archive file (or do something server-side), but that would achieve only static and efficiency, not single file. If we combine them, like SingleFile, we are back to static and single file, but not efficiency.

The simplest solution here would be to decide to complicate the server itself and do the equivalent ofdeconstruct_singlefile.phpon the fly. HTML requests, perhaps detecting some magic string in the URL like.singlefile.html, is handed to aCGIproxy process, which splits the original single HTML file into a normal HTML file with lazy-loaded references. The client browser sees a normal multiple efficient HTML, while everything on server sees a static single inefficient HTML. (A possible example isWWZ.)

While this solves the immediate Gwern.net problem, it does so at the permanent cost of server complexity, and does not do much to help anyone else. (It is unrealistic to expect more than a handful of people to modify their servers this invasively.) I also considered taking the WARC red pill and going full WebRecorder, but quailed.

## Download Stopping Mechanisms

How can we trick an HTML file into acting like atarballor ZIP file, with partial random access?

Our initial approach was to ship an HTML + JS header with an appended archive, where the JS would do HTTP Range queries into the appended binary archive; the challenge, however, was tostopthe file from downloading past the header. To do this, we considered some approaches ‘outside’ the page, like encoding the archive index into the filename/URL itself (ie.foo.gwtar-$N.html) and requiring the server to parse$Nout and slice the archive down to just the header, which then handled the range requests; this minimized how much special handling the server did, while being backwards/forwards-compatible with non-compliant servers (who would ignore the index and simply return the entire file, and be no worse than before). This worked in our prototypes, but required at least some server-side support and also required that the header be fixed-length (because any changes would in length would invalidate the index).

Eventually, Achmiz realized that youcanstop downloading fromwithinan HTML page, using the JS commandwindow.stop()!MDN(>96% support,spec):

Thewindow.stop()stops further resource loading in the current browsing context, equivalent to the stop button in the browser.

Because of how scripts are executed, this method cannot interrupt its parent document’s loading, but it will stop its images, new windows, and other still-loading objects.

This is precisely what we need, and the design falls into place.

# Concatenated Archive Design

A Gwtar is an HTML file with a HTML + JS + JSON header followed by a tarball andpossibly further assets. (A Gwtar could be seen asalmostapolyglot fileis a file valid as more than one format—in this case, a.htmlfile that is also a.tararchive, and possibly.par2. But strictly speaking, it is not.)

## Creation

We provide a reference PHP script,deconstruct_singlefile.php, which creates Gwtars from SingleFile HTML snapshots.

It additionally tries to recompress JPG/PNG/GIFs before storing in the Gwtar, and then appendsPAR2 FEC.

Example command to replace the original2010-02-brianmoriarty-thesecretofpsalm46.htmlby2010-02-brianmoriarty-thesecretofpsalm46.gwtar.htmlwith PAR2FEC:

php
 ./static/build/deconstruct_singlefile.php
--create-gwtar

--add-fec-data

\

 2010-02-brianmoriarty-thesecretofpsalm46.html

## Implementation

### Header

The first line of the header is the magic HTML string<html><!-- Gwtar self-extracting HTML archive, v1 -->, and the final line is the magic HTML string<!-- GWTAREND. (Additional metadata like the original input filename/hash/date may be included in comments.)

The header stores a JSON dictionary of files/sizes/types/SHA-256-hashes1of the real HTML (always first), followed by all of its assets (basename-asset-N.ext). There is always a HTML file and at least one asset. All of these assets are stored in the tarball immediately following the header (but which does not necessarily containonlythese assets). Example (with whitespace added for readability):

<
script
>

let
 assets
=
 {


"0"
:
 {


"size"
:

130673
,


"content-type"
:

"text/html"
,


"basename"
:

"1999-03-17-brianmoriarty-whoburiedpaul"
,


"hash"
:

"79111815b482504d79428f5cea329741348060fd2d943da933288595e2c9e969"

 }
,


"1999-03-17-brianmoriarty-whoburiedpaul-asset-1.js"
:
 {


"size"
:

15127
,


"content-type"
:

"application/x-javascript"
,


"hash"
:

"d739d46b0f3b188cd409c97ab47964ea3a009cce9d08a50b763fdb958e39b822"

 }
,


"1999-03-17-brianmoriarty-whoburiedpaul-asset-2.js"
:
 {


"size"
:

27146
,


"content-type"
:

"text/javascript"
,


"hash"
:

"dd29affcde5ff55d96613aa7ac55fa56cc8eeda20d6aef90185b75332e2c3cde"

 }
,


...

}

</
script
>

(Unfortunately, the assets are not necessarily valid for their mime-type—SingleFile passes through invalid or mismatched images and doesn’t guarantee much about the validity of its generated HTML. So Gwtar cannot require or guarantee much about the input or output HTML and is best-effort.)

The header JSis attached to the window once it stops loading and does nothing initially.

Finally,window.stop()is called at the end, before the appended tarball begins. This stops the web browser from loading any more data; then the main JS is free to run.

The main header JS starts using range requests to first load the real HTML, and then it watches requests for resources; the resources have been rewritten to be deliberately broken 404 errors (requesting from localhost, to avoid polluting any server logs), so when they fail, the JS then rewrites them into working range requests into the tarball, and repeats them.

### Details

The simple approach is to download the binary assets, encode them into Base64 text, and inject them into the HTML DOM. This is inefficient in both compute and RAM because the web browser must immediately reverse this to get a binary to work with. So we actually use the browser optimization ofblobsto just pass the binary asset straight to the browser.

A tricky bit is that inline JS can depend on “previously loaded” JS files, which may not have actually loadedyetbecause the first attempt failed (of course) and the real Range request is still racing. We currently solve this by just downloading all JS before rendering the HTML, at some cost to responsiveness.

So, a web browser will load a normal web page; the JS will halt its loading; a new page loads, and all of its requests initially fail but get repeated immediately and work the second time; the entire archive never gets downloaded unless required. All assets are provided, there is a single Gwtar file, it is efficient; it doesn’t require JS for archival integrity, as just the entire archive downloads if the JS is not executed; and it is cross-platform and standards-compliant, requires no server-side support or future users/hosts to do anything whatsoever, and is a transparent, self-documenting file format which can be easily converted back to a ‘normal’ multiple-file HTML (catfoo.gwtar.html|perl-ne'print $_ if $x; $x=1 if /<!-- GWTAR END/'|tarxf-)ora user can just re-archive it normally with tools like SingleFile.

## Fallback

In the event of JS problems,a<noscript>messageexplains what the Gwtar format is and why it requires JS, and links to this page for more details.

It also detects whether range requests are supported or downgraded to requesting the entire file. If the latter, it will start rendering it.

This is not as slow as it seems because we can benefit from connection level compression likegziporBrotli compression. And because our preprocessing linearize the assets in dependency order, we receive the bytes in order of page appearance, and so in this mode, the “above the fold” images and stuff will still load first and quickly. (This in comparison to the usual SingleFile, where you have to receive every single asset before you’re done, and which may be slower.)

## Compression

Gwtar does not directly support deduplication or compression.

Gwtars may overlap and have redundant copies of assets, but because they will be stored bit-identical inside the tarballs, ade-duplicatingfilesystem can transparently remove most of that redundancy.

Media assets like MP3 or JPEG are already compressed, and can be compressed during the build phase by a gwtar implementation.

The HTML text itself could be compressed; it is currently unclear to me how Gwtar’s range requests interact with transparent negotiated compression like Brotli compression (which for Gwern.net was as easy as enabling one option inCloudflare).RFC 7233doesn’t seem to give a clear answer about this, and thecursory and unhelpful discussion hereseemsto indicate that the range requests would have to be interpreted relative to the compressed version rather than the original, which is useful for the core use-case of resuming downloads but not for our use-case. So I suspect that probably Cloudflare would either disable Brotli, or downgrade to sending the entire file instead. It is possible that“transfer-encoding”solves this, butas of 2018, Cloudflare didn’t support it, making it useless for us and suggesting little support in the wild.

If this is a serious problem, it may be possible to compress the HTML during the Gwtar generation phase and adjust the JS.

## Limitations

### Local Viewing

Strangely, the biggest drawback of Gwtar turns out to belocalviewing of HTML archives. SingleFileZ encounters the same issue: in the name of security (origin/CORS/sandboxing), browsers will not execute certain requests in local HTML pages, so it will break, as it is no longer able to request from itself.

We regard this as unfortunate, but an acceptable tradeoff, as for local browsing, the file can be easily converted back to the non-JS dependent multiple/single-file HTML formats.

### Range Request Support

Range requests are old, standardized, and important for resuming downloads or viewing large media files like video, and every web server should, in theory, support it by default. In practice, there may be glitches, and one should check.

An examplecurlcommand which should return a HTTP 206 (not 200) request if range requests are correctly working:

curl

--head

--header

"Range: bytes=0-99"

'https://gwern.net/doc/philosophy/religion/1999-03-17-brianmoriarty-whoburiedpaul.gwtar.html'

# HTTP/2 206

# date: Sun, 25 Jan 2026 22:20:57 GMT

# content-type: x-gwtar

# content-length: 100

# server: cloudflare

# last-modified: Sun, 25 Jan 2026 07:08:33 GMT

# etag: "6975c171-7aeb5c"

# age: 733

# cache-control: max-age=77760000, public, immutable

# content-disposition: inline

# content-range: bytes 0-99/8055644

# cf-cache-status: HIT

# ...

Serversshouldserve Gwtar files astext/htmlif possible. This may require some configuration (eg.in nginx2), but should be straightforward.

#### Cloudflare Is Broken

However, Cloudflare has an undocumented, hardwired behavior: its proxy (not cache) will strip Range request headers fortext/htmlresponses regardless of cache settings. This does not break Gwtar rendering, of course, but it does break efficiency and defeats the point of Gwtar for Gwern.net

As a workaround, we serve Gwtars with the MIME typex-gwtar—web browsers like Firefox & Chromium will content-sniff the opening<html>tag and render correctly, while Cloudflare passes Range requests through for unrecognized types. (This is not ideal, but a more conventional MIME type likeapplication/...results in web browsers downloading the file without trying to render it at all; and using a MIME type trick is better than alternatives like trying to serve Gwtars as MP4s, using a special-case subdomain just to bypass Cloudflare completely, using complex tools like Service Workers to try to undo the removal, etc.)

## Accessing Binary Assets

Because a Gwtar can store large binary assets without burdening the viewer and is an archive format, it may be useful for reproducible science/statistics: include datasets, such asSqlite3 databases, and do computation on them like visualization or analysis. The question is, how do we ensure that assets get referenced in a way that SingleFile can “see” them and include them inline (to be stored in the final Gwtar as split-out objects), and then addressed and loaded by simple user JS, in a way which still workswithoutGwtar?

A potential approach in Gwtar v1 would be to reference all such assets using the<object>tag3, and then the user JS adds a simple listener hook to theloadevent, which will fire either when the browser loads the asset normally (multi-file) or when Gwtar completes its range-fetch rewrite, and then kicks off the actual userland work. This does not require any unusual or contorted user JS, appears to be backwards/forwards compatible, and to satisfy all our desiderata.

Untested pseudo-code:

<
object

id
=
"dataset"

data
=
"dataset.sqlite3"

type
=
"application/x-sqlite3"

width
=
"0"

height
=
"0"
></
object
>

<
script
>

document
.
getElementById
(
'dataset'
)
.
addEventListener
(
'load'
,

function
 () {


fetch
(
this
.
data
)


.
then
(
function
 (r) {
return
 r
.
arrayBuffer
()
;
 })


.
then
(
function
 (buf) {


// `buf` is the raw .sqlite3 bytes.


// Hand off to whatever SQL-in-JS library you're using.

 })
;

})
;

</
script
>

## Optional Trailing Data

The appended tarball can itself be followed by additional arbitrary binary assets, which can be large since they will usually not be downloaded. (While the exact format of each appended file is up to the users, it’s a good idea to wrap them in tarballs if you can.)

This flexibility is intended primarily for allowing ad hoc metadata extensions likecryptographic signaturesor forward error correction (FEC).

### FEC

The Gwern.net generation script uses this feature to addpar2FEC in an additional tarball.4This allows recovery of the original Gwtar if it has been partially corrupted or lost. (It cannot recover loss of the file as a whole, which is why FEC is ideally done over large corpuses, and not individual files, but this is better than nothing, and gives us free integrity checking as well.)

PAR2 can find its FEC data even in corrupted files by scanning for FEC data (“packets”) it recognizes, while tar ignores appended data; so adding, say, 25% par2 FEC is as simple as runningpar2create-r25-n1foo.gwtar.html&&tarcf.-foo.gwtar.html.par2 foo.gwtar.html.vol*.par2>>foo.gwtar.html&&rmfoo.gwtar.html*.par2, andrepairing a corrupted file is as simple asln--symbolicbroken.gwtar.html broken.gwtar.html.par2&&par2repairbroken.gwtar.html.par2 broken.gwtar.html.5

This yields the originalfoo.gwtar.htmlwithout any FEC. A repaired Gwtar file can then have fresh FEC added to be just like the old Gwtar + FEC archive, or be integrated in some broader system which achieves long-term protection some other way.

### Signing

A simple form of cryptographic signing would be to use GPG to sign it as a normal, separate, signature file (createsfoo.gwtar.html.sig):gpg--detach-sign--armorfoo.gwtar.html.

And we could also append an ASCII ‘armored’ GPG signature, as it won’t confuse tar, likegpg--detach-sign--armorfoo.gwtar.html>>foo.gwtar.html. Since GPG won’t munge a file like PAR2 will, an adhoc format would be to wrap it in tar to assist extracting:

gpg

--detach-sign

--armor
 foo.gwtar.html

tar
 cf.
-
 foo.gwtar.html.sig
>>
 foo.gwtar.html

rm
 foo.gwtar.html.sig

or in magic text, like a HTML comment:

# sign and append

FILE
=
"foo.gwtar.html"

gpg

--detach-sign

--armor

-o

"
$FILE
"
.asc
"
$FILE
"

echo

'<!-- GWTAR-GPG-SIG'

>>

"
$FILE
"

cat

"
$FILE
"
.asc
>>

"
$FILE
"

echo

'-->'

>>

"
$FILE
"

rm

"
$FILE
"
.asc

# Extract and verify:

SIG
=
$(
mktemp
 XXXXXX.asc
)

CONTENT
=
$(
mktemp
)

sed

--quiet

'/<!-- GWTAR-GPG-SIG/,/-->$/p'

"
$FILE
"

|


grep

-Ev

'GWTAR-GPG-SIG|-->'

>

"
$SIG
"

sed

'/<!-- GWTAR-GPG-SIG/,$d'

"
$FILE
"

>

"
$CONTENT
"

gpg

--verify

"
$SIG
"

"
$CONTENT
"

rm

"
$SIG
"

"
$CONTENT
"

# Metadata

A Gwtar is served with atext/htmlmime-type. If necessary towork around broken services like Cloudflare, its mime-type isx-gwtar.

# IP

This documentation and the Gwtar code is licensed under theCC-0public domaincopyright license. We are unaware of any software patents.

# Further Work

Gwtar v1 could be improved with:

1. Validation tool
2. Checking of hashsums when rendering (possibly async or deferred)
3. More aggressive prefetching of assets
4. Integration into SingleFile (possibly as a “SingleFileZ2” forma?)
5. Testing: corpus of edge-case test files (inline SVG,srcset, CSS@importchains, web fonts, data URIs in CSS…)

A Gwtar v2 could add breaking changes like:

1. format provides more rigorous validation/checking of HTML & assets; require HTML & asset validity, assets all decode successfully, etc.
2. standardize appending formats
3. require FEC
4. built-in compression with Brotli/gzip for formats not already compressed
5. multi-page supportOne would try to replace MAFF’s capability of creating sets of documents which are convenient to link/archive and can automatically share assets for de-duplication (eg. page selected by a built-in widget, or perhaps by a hash-anchor likearchive.gwtar.html#page=foo.html? Can an initial web page open new tabs of all the other web pages in the archive?)
6. Better de-duplication, eg. content-addressed asset names (hash-based) enabling deduplication across multiple gwtars

[Error: JavaScript disabled.]



[Backlinks, similar links, and the bibliography require JS enabled to load.]

# Bibliography



[Bibliography of links/references used in page]



[ Send Anonymous Feedback ]

[Quote Of The Day]

[Site Of The Day]

[Annotation Of The Day]



​

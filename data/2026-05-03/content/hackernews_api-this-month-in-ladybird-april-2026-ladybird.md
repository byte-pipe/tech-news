---
title: This Month in Ladybird - April 2026 - Ladybird
url: https://ladybird.org/newsletter/2026-04-30/
site_name: hackernews_api
content_file: hackernews_api-this-month-in-ladybird-april-2026-ladybird
fetched_at: '2026-05-03T11:40:50.762878'
original_url: https://ladybird.org/newsletter/2026-04-30/
author: richardboegli
date: '2026-05-02'
description: Inline PDF viewer powered by pdf.js, GTK4 frontend, browsing history, speculative HTML parsing, off-thread JS compilation, async DNS, CSS anchor positioning, and more.
tags:
- hackernews
- trending
---

# This Month in Ladybird — April 2026

 
 
 
 
 

Hello friends! In April we merged 333 PRs from 35 contributors, 7 of whom made their first-ever commit to Ladybird! Here’s what we’ve been up to.

### Welcoming new sponsors

Ladybird is entirely funded by the generous support of companies and individuals who believe in the open web. This month, we’re excited to welcome the following new sponsors:

* Human Rights Foundation(via the “AI for Individual Rights” program) with $50,000
* Jakub Stęplowskiwith $1,000

We’re incredibly grateful for their support. If you’re interested in sponsoring the project, pleasecontact us.

### Inline PDF viewer

PDFs now render inline through the bundledpdf.jsviewer (#9132). pdf.js is a full-featured PDF viewer written entirely in JavaScript, HTML, and CSS, with page navigation, text selection, zoom, and find-in-document. Profiling pdf.js loading theIntel ISA Manualalso drove improvements to our typed-array view cache and:has()invalidation.

### Browsing history and rich address bar autocomplete

Type in the address bar and you now get rich, history-aware suggestions: previously visited pages with favicons and titles, a search-engine shortcut, and plain URL completions (#8933). Behind the scenes, a SQLite-backedHistoryStorepersists every navigation along with its title, favicon, visit count, and last-visit time, and “Clear browsing history” is wired up in the Privacy settings page. Both the Qt and AppKit UIs render the new rich rows.

### Speculative and incremental HTML parsing

The HTML parser now consumes the response body incrementally (#9151). Bytes flow through a streaming text decoder into the tokenizer one chunk at a time, the tokenizer pauses when it runs out of input, and resumes when more arrives. This replaces a model where we waited for the full body before starting to parse.

We also implemented the speculative HTML parser (#9114). When the main parser blocks on a synchronous external script, a separate tokenizer scans ahead through the unparsed input and issues speculative fetches for the resources it finds:<script src>,<link rel=stylesheet|preload>, and<img src>. It tracks<base href>and skips into templates and foreign content correctly. A follow-up wired the speculative parser into the document’s preload map (#9164), so resources discovered speculatively get deduplicated against the regular parser’s later fetches instead of being requested twice.

### Off-thread JavaScript compilation

Bytecode generation for fetched scripts’ top-level code now runs on a background thread pool (#9118). Worker threads produce the bytecode and the data needed to build anExecutable, while everything that touches the VM or GC heap stays on the main thread. This covers classic scripts, modules, and top-level IIFEs, and shifts roughly 200ms of main thread time onto background threads while loading YouTube alone.

### Per-Navigable rasterization

Each Navigable now rasterizes independently on its own thread (#8793). Previously, iframes were painted synchronously as nested display lists inside their parent’s display list, which meant only the top-level traversable’s rendering thread was ever active. The parent’s display list now references each iframe’s rasterized output through anExternalContentSource, so iframe invalidations no longer require re-recording the parent. Beyond the parallelism, this is prep work for moving iframes into separate sandboxed processes.

### JavaScript engine

With the C++/Rust transition behind us, we spent April cashing in.

Faster JS-to-JS calls.A multi-part series (#8891,#8909,#8912) madeCall,Return, andEndinstructions stay entirely in the AsmInt assembly interpreter for the common case, with hand-tuned ARM64 paired load/store (ldp/stp) for register save/restore. Native function calls also dispatch directly from AsmInt now, via a newRawNativeFunctionvariant that holds a plain function pointer instead of anAK::Function(#8922).

O(1) bytecode register allocator.Generator::allocate_registerused to scan the free pool to find the lowest-numbered register. We were spending ~800ms in this function alone while loading x.com. With the C++/Rust pipeline parity period over, the allocator is now a plain LIFO stack (#9007).

Cached for-in iteration.for (key in obj)sites now cache the flattened enumerable key snapshot and reuse it as long as the receiver’s shape, indexed storage, and prototype chain still match (#8856). Speedometer 2 went from 67.7 to 73.6, and Speedometer 3 from 4.11 to 4.22!

A grab-bag of other improvements:

* The parser uses zero-copy identifier name sharing across the lexer, parser, and scope collector. On a corpus of website JS, parsing is 1.14x faster and uses 282 MB less RSS. (#8801)
* Short string concatenations skip the rope representation when the result is going to be observed as a flat string anyway. 2.13x speedup on a tighta + bloop. (#9184)
* Lexical-this arrow functions no longer allocate a function environment per call. Another 2.13x on a microbenchmark. (#9192)
* Sparse arrays no longer pay an eager cost for their holes:Array(20_000_000)stays mostly metadata instead of doing work proportional to twenty million imaginary elements. (#8847)
* A new lazyJS::Substringtype backs regexp captures and string builtins likeslice,split, and indexed access, gaining 1.066x on Octane’s regexp benchmark. (#8863)
* Source positions are preserved end-to-end in bytecode source maps, saving ~250ms on x.com. (#9027)
* Zero-copyTransferArrayBuffersaves ~130ms on YouTube load. (#9088)
* Cached typed-array views switched from aWeakHashSetto an intrusive list, saving ~250ms loading the Intel ISA PDF in pdf.js. (#9180)
* EveryPromiseallocated twoPromiseResolvingFunctioncells withAK::Functionclosures that didn’t actually capture anything. They’re now static functions dispatched by aKindenum, dropping a per-resolver allocation across every promise the engine creates. (#9188)
* Skipping property-table marking for non-dictionary shapes cut 1.3 seconds off GC time while loadingmaptiler.com. (#9044)
* A fast path forArray.prototype.indexOfon packed arrays (#9123)
* Array.prototype.sortreuses cached UTF-16 instead of re-transcoding on every comparison (#9036)
* Imports forWASM, JSON, and CSS modules(#6029)
* RemovedShadowRealmsupport, since the proposal has stalled in the standards process (#8753)

### GTK4 / libadwaita frontend

Ladybird has a new Linux frontend built on GTK4 and libadwaita, sitting alongside the existing Qt frontend (#8691). It’s inspired by GNOME Web (Epiphany) and follows GNOME’s design guidelines: no menubar, a hamburger menu, andAdwTabViewfor tabs. Out of the box you get autocomplete and security icons in the URL bar, find-in-page, fullscreen, context menus, alert/confirm/prompt/color/file dialogs, clipboard, multi-window, light/dark theme, and DPR scaling. It’s still early, so not yet at feature parity with the Qt and AppKit frontends.

### Bookmarks

Last month we got bookmarks. This month they got a proper management UI:

* Anabout:bookmarkspage for managing bookmarks and folders (#8825)
* Bookmark import and export from the new page (#8938)
* Context menus for editing bookmarks and folders (#8715)
* Adate_addedtimestamp on every bookmark and folder (#8867)
* Bookmarks bar QoL: open in new tab, copy URL, middle-click and Ctrl/Cmd+click to open in new tab (#8758)
* The HTML5 drag-and-drop API is now wired up (#8783).about:bookmarksuses it for reordering, and it works on regular web pages too.

### Cache and CacheStorage

We implementedCacheandCacheStorageend to end, with all nine methods (open,has,delete,keys,match,matchAll,add,addAll,put) backed by an ephemeral in-memory store (#8745).

### CSS features

* image-set(): Basic support for the standard and-webkit-prefixed forms. At paint time we pick the candidate whose resolution best matches the device pixel ratio, skipping unsupported MIME types. This makes header images show up ongocomics.com. (#9090)

Before
After

* position-anchorand CSS anchor positioning: Initial support for anchor-positioned elements, fixing the hand and gun positioning oncssdoom.wtf. (#8686)

Before
After

* Color interpolation rewrite: Aligned withcss-color-4. We now interpolate in float instead ofu8, handle missing and powerless components correctly, deal with out-of-gamut sRGB, and apply alpha multipliers consistently. (#8934)
* Presentational hints through the cascade: Legacy presentational HTML attributes (align,bgcolor, etc.) used to bypass the regular CSS cascade and write directly into the element’s cascaded properties. They now go through the cascade as normal author declarations, sovar()substitution and the invalid-at-computed-value-time fallback work correctly. Fixes a crash onhtml.spec.whatwg.org. (#9176)
* alignon table sections and rows:<thead>,<tbody>,<tfoot>, and<tr>honor thealignpresentational attribute, fixing button placement onbricklink.com. (#9177)BeforeAfter
* stroke-dasharrayinterpolation: SVG dashes finally animate smoothly. (#9133)
* autofocus: Elements with theautofocusattribute actually receive focus on page load now. (#9016)
* List markers in RTL text: Bullets now sit on the right side of right-to-left text, fixing list rendering on Arabic Wikipedia. (#9099)BeforeAfter
* Inline flex/grid baselines: An inline flex or grid container now derives its baseline from its child’s first line box, not its last wrapped line. Fixes link text and icon alignment onnos.nl. (#9183)BeforeAfter

### Networking

getaddrinfono longer blocks the event loop. LibDNS now runs lookups on a thread pool, firesAandAAAAqueries in parallel (RFC 8305-ish), and coalesces concurrent lookups for the same name. RequestServer’s preconnect path was sneaking past our resolver and letting libcurl spawn its own threaded resolver that wouldpthread_joinus on the main thread; that’s now routed through the same DNS pool. (#9109)

Profile of loading x.com when DNS is slow, before and after:

Over in RequestServer, draining queued response data was O(n²) when WebContent was slower than the network. RequestServer was spending ~30 seconds inmemcpyand 3 seconds inVector::removewhile opening a YouTube video! SwitchingAllocatingMemoryStreamto a singly-linked chunk list made consumption O(1). (#9028)

We now advertise AVIF and WebP in ourAcceptheader for image requests, matching other engines. Some CDNs use theAcceptheader to decide whether to serve modern formats or fall back to JPEG. (#9046)

### Style invalidation

Selector invalidation used to be straightforward: selectors always looked downward.:hostruined that.:has()made it way worse. Any descendant change can now force you to walk up the tree finding ancestors whose:has()arguments just flipped, and a lot of this month’s invalidation work is about making that walk less wasteful.

Four big wins this month:

* Reddit rule cache rebuilds: 13.2s → 3.2s.Stylesheet mutations no longer rebuild every style scope’s cache when only one scope changed. (#9138)
* Reddit infinite scroll: 11% fewer pointless recomputes.Sibling structural invalidation stopped fanning out to descendants that don’t observe the position. (#9155)
* :has()mutation invalidation skips unaffected anchors, with substantial reductions measured onazure.com. (#9168)
* :has()child-list visits on the Intel ISA PDF: 71k → 1.6k.Coalesced when pending data already covers every concrete feature bucket the scope cares about, saving ~650ms on the pdf.js load. (#9179)

A large new structural-invalidation test battery exposed and fixed several invalidation holes (#9095), and a string of smaller tightenings landed around hover, stylesheet mutation scope, custom-property maps, and computed-style diffing (#9077,#9049,#9079,#9080,#9141).

### Linux GPU painting via dmabuf

On Linux Vulkan builds, GPU-backed painting was being secretly undone every frame: WebContent painted into a GPU-backed Skia surface, but the buffer it shared with the UI process was a CPU bitmap, which forced a full GPU-to-CPU readback on every flush.SharedImagecan now carry a Linux dmabuf handle, so the front and back buffers stay GPU-resident the whole way to the UI process. (#8917,#8920)

### mimalloc as the main allocator

Our C++ and Rust code now share a single allocator instance,mimalloc v2, instead of each going through the system allocator separately (#8752). We don’t overridemalloc()system-wide, so third-party libraries keep their own allocator contracts. JS benchmarks improved across the board.

### Sites that work better

The biggest visible wins this month are on Reddit and YouTube.

Redditimage gallery carousels actually work now, after fixing two unrelated layout bugs around::slotted()matching and absolutely positioned descendants of split inlines (#9148). And thanks toTextDecoderStream, the SPA stops swallowing link clicks, so you can finally open the comments! Infinite scroll also benefits from the structural-invalidation work covered above.

YouTubebenefits from a stack of unrelated improvements: off-thread top-level JS compile, off-thread WOFF2 decompression (saves ~170ms on Gmail too,#8976), reduced@font-facefetch fanout (177 → ~9 fetches on initial load,#9032), the RequestServer memory churn fix, and zero-copyTransferArrayBuffer.

A handful of smaller fixes:

* gocomics.com: Header images show up, thanks toimage-set().
* yandex.com/maps: Vector-tile WebGL rendering works after a small pile of WebGL fix-ups, including theWEBGL_debug_renderer_infoextension (#9043).
* strava.com: Login works now thatNavigator.getBatterythrows the spec-mandated error type instead of one of our own (#8770).
* GitHub Insights: Loads ~100ms faster thanks to theElement.matches()and.closest()selector cache (#8987).
* tweakers.net: The laptop comparison page is ~31% faster from indexedHTMLFormElementproperty name lookups (#9009).
* neon.com: No longer crashes (#8812).
* channel4.com: Vertically misaligned category text fixed in flex auto-margin resolution (#9050).
* Cloudflare Turnstile: Still doesn’t pass, but we fail itmuchfaster now thanks to auth-scheme handling,Array.prototype.shift()optimizations, and a pile of UA event handler hardening on<input>range and number elements (#9063).

### Web Platform Tests (WPT)

OurWPTscore went from 2,003,537 to 2,067,263 this month, a headline gain of 63,726 subtests. There’s an asterisk on that number: WPT importedtest262, the official ECMAScript conformance suite, upstream this month, which added 53,207 JavaScript subtests to the count. We pass 52,045 of them (a 97.8% pass rate), since we’ve been running test262 independently for years and LibJS conformance is in great shape. So roughly 52k of the 63.7k gain is from the import, and the remaining ~11.7k is genuine new browser-platform progress, in the same ballpark as January’s 13,690.

The upside of the import is that WPT now actually measures JavaScript conformance alongside the rest of the platform, which is the way it should have been all along.

### Other notable changes

* Rust is now mandatory: TheENABLE_RUSTbuild option is gone (#8742), and the GN build system was removed entirely, leaving CMake as the single source of truth (#8931).
* Stack-zeroing for the GC’s benefit: We now compile with-ftrivial-auto-var-init=zero, which overwrites stale GC pointers on function entry so our conservative stack scanner finds fewer of them. (#9171)
* Selecting through ligatures: Selection and hit testing on text with ligatures used to assume one glyph per code unit, so trying to highlight half of aﬃselected either all or none. We now walk grapheme clusters and split each glyph’s advance across the graphemes it covers. (#8829)
* Layout state slimming: Rarely-usedUsedValuesproperties moved behind a lazy pointer, dropping the struct from 424 to 176 bytes and cuttingLayoutState::populate_node_from()from 139ms to 65ms while loadingsainsburys.co.uk. (#9104)
* Targeted ShadowRoot layout invalidation: SettinginnerHTMLon a shadow root no longer invalidates the entire document’s layout tree. Reduces layout-and-paint time onpomax.github.io/bezierinfoby 21%. (#9191)
* Fetch body chunks straight into the stream: Fetched bytes used to be delivered through a pull-promise dance that allocated seven GC objects per chunk and did nothing useful. They now go directly into the byte stream controller. (#9169)
* Cross-site popup navigation: Navigating a popup tab to a different site no longer kills the parent’s WebContent process. (#8730)
* Ctrl+Tabfor tab navigation: On the Qt UI,Ctrl+TabandCtrl+Shift+Tabcycle through open tabs. (#8704)
* Middle-mouse autoscroll: Hold the middle mouse button and drag to scroll, or click in place to enter autoscroll mode. (#8881,#8928)
* Address-bar error page: When you type text into the address bar that can’t be sanitized into a URL or search query (for instance, with search disabled), you now get a proper error page instead of the input being silently dropped. (#9072)
* TextDecoderStream: The streaming counterpart toTextDecoderis now implemented, including the partial-UTF-8 hold-back across chunk boundaries that makes the Reddit comments fix above possible. (#9143)
* Cross-processBroadcastChannel: Messages now route over IPC between WebContent and WebWorker processes, so aBroadcastChannelworks the same way it does in other browsers regardless of which process the listener is in. (#8865)

### Credits

We’d like to give a special shout-out to the 7 people who made their first code contribution this month:

* CalebC48. Made the Qt UI open the new tab page when “New Window” is invoked without a URL (#8864)
* Darshanx256Preserved copy flags when recursing into directories in LibFileSystem (#8834)Updated documentation to use theReleaseCMake preset (#8814)
* Preserved copy flags when recursing into directories in LibFileSystem (#8834)
* Updated documentation to use theReleaseCMake preset (#8814)
* j-stechmann. AddedCtrl+TabandCtrl+Shift+Tabfor tab navigation in the Qt UI (#8704)
* James Raspass. Switched the settings dialogs over to native light dismiss (#8808)
* jarusll. Added support for multiple--debug-processarguments to LibWebView (#8841)
* slydetector. Various devcontainer fixes to get things working again (#9149)
* Yayoi-cs. Reported and fixed a use-after-free in TypedArray views over sharedWebAssembly.Memory(GHSA-w89h-j2xg-c457)Initial security fix (d8aee7f1e6)Follow-up cache hardening (#9086)
* Initial security fix (d8aee7f1e6)
* Follow-up cache hardening (#9086)

And of course we’d like to thank everyone who contributed code this month:

Ali Mohammad Pur, Aliaksandr Kalenik, Andreas Kling, Andrew Kaster, ayeteadoe, CalebC48, Callum Law, Christian Frey, Darshanx256, Glenn Skrzypczak, InvalidUsernameException, James Raspass, Jelle Raaijmakers, Johan Dahlin, Jonathan Gamble, Jonathan (j-stechmann), jarusll, Luke Wilde, mikiubo, Nicolas Danelon, Ollie Hensman-Crook, Pavel Shliak, Psychpsyo, R-Goc, RubenKelevra, Sam Atkins, Shannon Booth, slydetector, Suraj Yadav, Tete17, Tim Ledbetter, Timothy Flynn, Undefine, Yayoi-cs, Zaggy1024
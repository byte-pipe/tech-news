---
title: 'My OSS Projects: AngleSharp - DEV Community'
url: https://dev.to/florianrappl/my-oss-projects-anglesharp-3b8j
site_name: devto
content_file: devto-my-oss-projects-anglesharp-dev-community
fetched_at: '2026-09-14T16:47:27.612401'
original_url: https://dev.to/florianrappl/my-oss-projects-anglesharp-3b8j
author: Florian Rappl
date: '2026-09-09'
description: This is the first post in a new series, "My Open-Source Projects", where I go through some of the... Tagged with dotnet, opensource, csharp, webdev.
tags: '#dotnet, #opensource, #csharp, #webdev'
---

The story behind building a spec-conformant DOM

This is the first post in a new series,"My Open-Source Projects", where I go through some of the OSS projects I started or maintain and tell you the story behind them - the good, the bad, and the "why did I think this was a good idea at 30,000 feet" parts. First up:AngleSharp.

## What Is AngleSharp, Actually?

Before the story, the pitch:AngleSharpis a .NET library that parses HTML, SVG, MathML, CSS, and (to a good extent) XML, and gives you back a fully-featured, spec-conformant DOM. Not "DOM-ish." Not "good enough for scraping." The actual W3C DOM API, the samequerySelector,querySelectorAll, and element interfaces you already know from the browser console - except it's C#, it runs headless, and there's no browser in sight.

If you've ever reached for a regex to parse HTML: please don't. You know why. AngleSharp exists so that nobody has to write<div[^>]*>ever again.

Now, onto how it got here.

## The Original (Slightly Unhinged) Idea

Once upon a time, I had what I thought was a brilliant idea: build a cross-platform GUI toolkit using HTML, CSS, and C#. I was certainly not the first person to think of this - plenty of people had similar thoughts before me - but back then it was still a fairly fresh take.

The more I thought it through, though, the more obvious it became: you can't just take HTML and CSS and strip them down to "the easy 80%". If you want this to actually work, you need the real deal - a proper HTML parser, a proper CSS engine, the whole circus. No shortcuts.

So naturally, the reasonable thing to do was to just... write an HTML5 parser. From scratch. In C#. Sure, why not.

## Coding at 30,000 Feet

In 2013 I was flying to the Microsoft MVP Summit, and for reasons that made complete sense to me at the time, I brought a printed copy of the HTML5 spec with me. Not a novel. Not a magazine. The spec.

I started coding on the plane. By the time we landed, the parser was already "working" - in the sense that the happy paths worked. Feed it well-formed markup and it would dutifully produce a DOM. Great success, right?

Well, that's roughly the point where I discovered the dirty little secret of the HTML5 spec: it's massive not because HTML is a complicated language, but because of everything around it - error handling, edge cases, and the glorious pile of "what should happen when the markup is garbage" scenarios that browsers have been quietly agreeing on for decades. Turns out the "happy path" is maybe 20% of the actual spec. The other 80% is browsers being incredibly forgiving about human mistakes.

I kept grinding away at it, and eventually most of the edge cases and tests turned green. And then, like clockwork, I hit the point every side project hits: frustration, a pause, and a "why am I doing this to myself" moment. Every maintainer knows this phase. It has no official name, but "why did I do this to myself" captures it well enough.

## Ship It Before It Goes Nowhere

Eventually I picked it back up with a very simple thought: before this thing quietly dies in a local folder, let's write a CodeProject article about it and push the code to GitHub.

I already had some open-source experience at that point - mostly as a contributor. The one project I actually maintained wasYAMP, and thanks to some very patient people with a lot more GitHub experience than me, I'd picked up a few things about "doing OSS properly."

So I published the article, pushed the repo, and went to bed.

When I woke up, something had clearly happened. The repository already had 120+ stars, and the article was ranking surprisingly well. Nothing makes you suddenly very motivated about a side project like waking up to numbers you didn't expect.

So I kept going. And going.

## Stabilizing, Then Breaking Everything (On Purpose)

For a while, most of the effort went into the internals - making the parsing actually correct, not just "correct enough." Once that settled down, the API itself went through some pretty massive changes. Not always changes that users loved, if I'm honest. Breaking changes are never fun to be on the receiving end of, and I was on the giving end a fair bit during this period.

The big turning point wasAngleSharp 0.10. This release quietly laid the groundwork for what would define AngleSharp going forward: modularity. Suddenly you could just add another library and your document could parse JavaScript. Add another one and you got CSS. This came from a lightweight-but-surprisingly-capable dependency injection system and a service-based configuration approach that let you chain extensions together like Lego bricks.

That modular shape is still exactly how the ecosystem looks today:

## The Long Road to 1.0

For years, I genuinely wasn't sure I could call the API "stable" and commit to semver. Not because it was shaky - it just felt like a big commitment. Eventually, after years of the API beingde factostable (even if I hadn't officially blessed it as such), I released1.0.

From that point on, my main driver hasn't been "let's avoid a 2.0 or 3.0 forever." I have nothing against major version bumps. My actual rule is simpler: a breaking change needs to earn its place. If it's not genuinely useful enough to justify the pain it causes downstream, it doesn't happen.

## It Was Never a Solo Project

I've told this story mostly in first person so far, which is a bit unfair, because AngleSharp would have died somewhere around "some happy paths seemed to work" if it had stayed a one-person effort.

The project'sCONTRIBUTORS.mdreads like a highlight reel of people who showed up over the years to fix a parser edge case, argue with me about API naming (we've hadopinions), or add a feature I didn't know I needed. In order of first contribution: Andreas Augustin, Jerrie Pelser, Liwen Guo, Raphael Ducom, Georgii Dolzhykov, Joel Verhagen, Michael Ganss, Robin Sue, Henry Roeland, Adrian Phinney, Andreas Håkansson, Jeremy Meng, Yehudah Asher, Dennis Daume, Jakub Świętek, Dennis Gorelik, Georgios Diamantopoulos, Brian Ricketts, Laurynas Ruškys, Martin Wakley, Bastian Buchholz, Keith Hall, Nikita Ilinykh, Thomas Bolon, Alexander Ubillus, Max Katz - and plenty more across the ecosystem repos who deserve just as much credit.

One name on that list deserves a special callout:Michael Ganss. He contributed to AngleSharp early on, then went off and builtHtmlSanitizer- a library that cleans HTML of XSS payloads - directly on top of it. So somewhere out there, a chunk of the web's HTML sanitization is running through code that started as a side project on an airplane, maintained partly by someone who used to fix that airplane project's bugs. I don't think you can plan a story arc like that.

Also worth saying clearly: AngleSharp is a.NET Foundationproject. That's not nothing - it means the project has a support structure behind it beyond just "one person's spare time and mild sleep deprivation."

## Where AngleSharp Shows Up Today

It's easy to undersell this part, so let me just put some numbers on the table. As of writing, the coreAngleSharp NuGet packagealone sits atover 310 million downloads. Add the satellite packages and you're comfortably north of 500 million installs across the ecosystem.

The curve is the fun part - this is basically a hockey stick with a decade-long windup:

Barely a blip until around 2019, and then it just... doesn't stop. That little dip in early 2025 on the core package is a NuGet stats quirk, not a mass exodus - don't worry, nobody suddenly stopped parsing HTML.

A few of the places AngleSharp quietly does the heavy lifting:

* HtmlSanitizer(128M+ downloads on its own) uses AngleSharp to parse and re-render HTML while stripping out anything that could be used for cross-site scripting. If a .NET app on the internet safely accepts user-submitted HTML, there's a decent chance AngleSharp is standing guard.
* bUnit, the go-to unit testing library for Blazor components, uses AngleSharp under the hood (viaAngleSharp.Diffing) for its semantic HTML comparisons - the thing that lets you assert "this rendered markup is equivalent to that markup" without caring about attribute order or whitespace.
* PreMailer.Netinlines CSS into HTML emails (because email clients are still living in 2003) using AngleSharp to actually understand the markup and styles it's rewriting.
* WebDriverManagerfor .NET, which manages Selenium WebDriver binaries, also leans on it.

And then there's the list of projects that depend on it directly - some of which you've almost certainly used:Bitwarden(the password manager),JackettandProwlarr(torrent/indexer tooling),Playnite(game library manager),ArchiSteamFarm,OrchardCore(a full CMS/app framework),OpenIddict(OAuth2/OpenID Connect for .NET),YoutubeExplode, and even Microsoft's ownASP.NET Core documentation toolingrepository.

None of this was the plan when I was scribbling parser states on a plane. But it turns out "a really solid, standards-compliant HTML parser for .NET" is one of those unglamorous building blocks that ends up everywhere once it exists.

## Getting Started

Install the core package from NuGet:

dotnet add package AngleSharp

Enter fullscreen mode

Exit fullscreen mode

And parse your first document:

using
 
AngleSharp
;

using
 
AngleSharp.Html.Parser
;

var
 
parser
 
=
 
new
 
HtmlParser
();

var
 
document
 
=
 
await
 
parser
.
ParseDocumentAsync
(
"<h1>Hello!</h1><p>AngleSharp says hi.</p>"
);

var
 
heading
 
=
 
document
.
QuerySelector
(
"h1"
);

Console
.
WriteLine
(
heading
.
TextContent
);
 
// Hello!

Enter fullscreen mode

Exit fullscreen mode

That's the "hello world" version. Most real usage, though, goes through aBrowsingContext, which acts like a browser tab - it can load documents from the network, follow links, submit forms, and generally behave like something a bit more alive than a static parser:

using
 
AngleSharp
;

var
 
config
 
=
 
Configuration
.
Default
.
WithDefaultLoader
();

var
 
context
 
=
 
BrowsingContext
.
New
(
config
);

var
 
document
 
=
 
await
 
context
.
OpenAsync
(
"https://example.com"
);

foreach
 
(
var
 
link
 
in
 
document
.
QuerySelectorAll
(
"a"
))

{

 
Console
.
WriteLine
(
link
.
GetAttribute
(
"href"
));

}

Enter fullscreen mode

Exit fullscreen mode

Want CSS support too? Add the plugin and register it in the configuration:

dotnet add package AngleSharp.Css

Enter fullscreen mode

Exit fullscreen mode

var
 
config
 
=
 
Configuration
.
Default

 
.
WithDefaultLoader
()

 
.
WithCss
();

var
 
context
 
=
 
BrowsingContext
.
New
(
config
);

var
 
document
 
=
 
await
 
context
.
OpenAsync
(
"https://example.com"
);

var
 
body
 
=
 
document
.
QuerySelector
(
"body"
);

var
 
style
 
=
 
body
.
ComputeCurrentStyle
();

Console
.
WriteLine
(
style
.
GetPropertyValue
(
"background-color"
));

Enter fullscreen mode

Exit fullscreen mode

Same idea for scripting (AngleSharp.Js), XML validation (AngleSharp.Xml), or semantic diffing of HTML fragments (AngleSharp.Diffing) - oneWith...()call, and a new capability shows up.

## Where It Shines

* Standards over vibes.The parser follows the actual HTML5 parsing algorithm, including its error-recovery rules. Feed it broken markup, and it recovers the way a browser would - not the way a regex-and-hope solution would.
* A real DOM, not a wrapper.querySelector,querySelectorAll, LINQ-to-DOM, form submission, navigation viaBrowsingContext- it feels like scripting a browser tab from C#, minus the browser.
* Modular by design.Only pay (in dependencies and startup cost) for what you actually use. Need CSS cascade computation? Add one package. Need to run inline<script>tags? Add another.
* Performance.It's not trying to be a browser engine, and that's exactly why it's fast - large documents parse in milliseconds, with internal reuse of elements to keep allocations down.
* It composes well with automated testing.AngleSharp.Diffingin particular is great for asserting "this HTML is semantically the same as that HTML" without caring about attribute order or whitespace.

## Where It Struggles

No project is without trade-offs, and I'd rather tell you about them than let you find out the hard way:

* It's not a browser.There's no layout engine, no painting, no actual visual rendering (yet - more on that below). If you need pixel-accurate rendering, you still want something like Playwright or a headless Chromium.
* JavaScript support is limited.AngleSharp.Jsruns onJint, which is a real ECMAScript engine, but it's not V8. Heavy, modern JS-driven pages (SPAs relying on a full browser runtime) are not its comfort zone, but definitely possible.
* The ecosystem is spread across several repositories.Core, Css, Js, Xml, Io, Diffing, Wasm - it's modular by design, which is a strength, but it also means version compatibility between packages occasionally needs a bit of attention (dependency ranges across separately-versioned repos are always afunproblem to own - but generally the only dependency they all have is the core lib).
* Breaking changes did happen historically.Pre-1.0 AngleSharp went through real API churn. It's stable and semver-respecting now, but if you find decade-old blog posts referencing the API, expect it to look different today.

## The Wider Ecosystem

Depending on what you need, the packages you'll likely run into are:

* AngleSharp(NuGet) - the core: HTML5/XML parsing, DOM, configuration.
* AngleSharp.Css- CSSOM, selectors, cascades, computed styles.
* AngleSharp.Js- JavaScript execution via Jint.
* AngleSharp.Xml- XML parsing plus XSD/DTD validation.
* AngleSharp.Io- requesters, cookies, and the networking stack.
* AngleSharp.Diffing- semantic DOM diffing, great for tests.
* AngleSharp.Wasm- running AngleSharp inside the browser via WebAssembly/Blazor.

If you want to talk to actual humans about it best case is to open an issue in one of the repos. Historically, there's also aGitter chatand a tag that was / is used onStack Overflow.

## What's Next: Coming Full Circle

Remember that original goal - a cross-platform GUI built on HTML and CSS? That idea got shelved pretty early on in favor of "let's just get the fundamentals right first." But it never really left.

The next big frontier for AngleSharp isrendering. The plan is a general-purpose headless renderer that can be used interactively - moving a pointer, sending keystrokes, the works - or just to grab a screenshot. On top of that, the goal is a cross-platform control (most likely built onAvalonia) that can be embedded into apps.

Am I building a browser? Let's not get ahead of ourselves. But it's fair to say the project is closer to its original vision now than it's been at any point in the last decade.

That's the AngleSharp story - from a stack of printed spec pages on an airplane to a mature parsing ecosystem with XSD validation and WASM support. If you want to poke around, the code lives onGitHub, and the package is onNuGet.

Next up in this series: another one of my projects, and probably another origin story that started with me underestimating how much work something would be. Stay tuned!

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
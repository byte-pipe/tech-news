---
title: Google is killing the open web, part 2
url: https://wok.oblomov.eu/tecnologia/google-killing-open-web-2/
site_name: hackernews
fetched_at: '2025-11-17T19:06:52.594920'
original_url: https://wok.oblomov.eu/tecnologia/google-killing-open-web-2/
author: Oblomov
date: '2025-11-17'
description: Do not comply in advance.
---

I wrote a few months ago aboutthe proxy war by Google against the open web by means of XSLT.
Unsurprisingly,Googlehas been moving forward on the deprecation,
still without providing a solid justification on the reasons why other than
“we've been leeching off aFLOSSlibrary for which we've finally found enough security bugs to use as an excuse”.
They do not explain why they haven't decided to fix the security issues in the library instead,
or adopt a more modern library written in a safe language, taking the opportunity to upgradeXSLTsupport
to a more recent, powerful and easier-to-use revision of the standard.

Instead, what they do is to provide a “polyfill”, a piece ofJavaScriptthat can allegedly used to supplant the functionality.
Curiously, however, they donotplan to ship such alternative in-browser,
which would allow a transparent transition without even a need to talk about XSLTat all.
No, they specifically refuse to do it, and instead are requesting anyone still relying on XSLT to
replace the invocation of the XSLT with anon-standardinvocation of the JavaScript polyfill that should replace it.

This means that at least one of these two things are true:

1. the polyfill is not, in fact, sufficient to cover all the use cases previously covered by the built-in support for XSLT,
and insofar as it's not, they (Google) do not intend to invest resources in maintaining it,
meaning that the task is being dumped on web developers
(IOW, Google is removing a feature that is going to createmore workfor web developers just to provide the same functionality that they used to have from the browsers);
2. insofar as the polyfill is sufficient to replace the XSLT support in the browser,
the policy to not ship it as a replacement confirms that the security issues in the XSLT library used in Chrome
were nothing more than excuses to give the final blow toRSSand any otherXMLformat
that is still the backbone of an independent web.

As I have mentionedin the Fediverse thread I wrote before this long-form article,
there's an obvious parallel here with the events that I already mentionedin my previous article:
whenMozillabent over toGoogle's pressure to kill off RSS by removing the “Live Bookmarks” features from the browser,
they did this on presumed technical grounds (citing as usualsecurity and maintenance costs,
but despite paid lip service to their importance for an open and interoperable web,
they didn't provide any official replacement for the functionality,
directing users instead toa number of add-ons that provided similar functionality,none of which are written or supported by Mozilla.
Compare and contrast with theirPocketintegration that they force-installed everywherebefore ultimately killing the service

Actions, as they say, speak louder than words.
When a company claims that a service or feature they are removing can be still accessed by other means,
but do not streamline such access said alternative,
and instead require their users to do the work necessary to access it,
you can rest assured that beyond any word of support they may coat their actions with
there is a plain and direct intent at sabotaging said feature,
and you can rest assured that any of the excuses brought forward to defend the choice
are nothing but lies to cover a vested interest in sabotaging the adoption of the service or feature:
the intent is for you tonotuse that feature at all, because they have a financial interest in younotusing it.

And the best defense against that is to attack, and push the use of that feature even harder.

1. Google is killing the open web, part 2Do. Not. Comply.The WHATWG is not a good steward of the open webA new browser war?Another web?A Web of interconnected software?The role of multimedia streaming in the death of the User AgentControlled evolutionA mesh of building blocksResistPost scriptum
2. Do. Not. Comply.
3. The WHATWG is not a good steward of the open web
4. A new browser war?
5. Another web?
6. A Web of interconnected software?The role of multimedia streaming in the death of the User AgentControlled evolutionA mesh of building blocks
7. The role of multimedia streaming in the death of the User Agent
8. Controlled evolution
9. A mesh of building blocks
10. Resist
11. Post scriptum

## Do. Not. Comply.

This is the gist ofmy Fediverse thread.

Do not install the polyfill.
Do not change your XML files to load it.
Instead, flood their issue tracker with requests to bring back in-browser XSLT support.
Report failed support for XSLT as a broken in browsers, because this is not a website issue.

I will not comply.As I have foryearscontinued usingMathML,SVGandSMIL(sometimeseven all together) despite Google's intent on their deprecation,
I will keep using XSLT, and in fact will look for new opportunities to rely on it.
At most, I'll set up an infobox warning users reading my site about their browser's potential brokenness
and inability to follow standards, just like I've done for MathML and SMIL
(you can see such infoboxes in the page I linked above).
And just like ultimately I was proven right
(after several years, Google ended up fixing both their SMIL and their MathML support in Chrome),
my expectation is that, particularly with more of us pushing through,
the standards will once again prevail.

Remember: there is not technical justification for Google's choice.
This is not about a lone free software developer donating their free time to the community
and finding they do not have the mental or financial resources to provide a particular feature.
This is a trillion-dollar ad company who has been actively destroying the open web
for over a decadeand finally admitting to itas a consequence of theLLMpush
andintentional[enshittification of web search]404mediaSearch.

The deprecation of XSLT is entirely political,
fitting within the same grand scheme of the parasitic corporation killing the foundations of its own success
in an effort to grasp more and more control of it.
And the fact that theWebKitteam atAppleand theFirefoxteam atMozillaare intentioned to follow along on the same destructive path is not a counterpoint,
but rather an endorsement of the analysis,
as neither of those companies is interested in providing aUser Agentas much as asurveillance capitalismtool that you happen to use.

(Hence why Mozilla, a company allegedly starved for resources,
is wasting them implementingLLM features nobody wantsinstead offixing much-voted decade-old bugs with several duplicates.
Notice how the bug pertains the (mis)treatment of XML-based formats —like RSS.)

If you have to spend any time at all to confront the Chrome push to deprecate XSLT,
your time is much better spent inventing better uses of XSLT
and reporting broken rendering if/when they start disabling it,
than caving to their destructive requests.

## The WHATWG is not a good steward of the open web

I've mentioned itbefore,
but theWHATWG, even assuming the best of intentions at the time it was founded,
is not a good steward of the open web.
It is more akin to the corrupt takeover you see inregulatory capture,
except that instead of taking over theW3Cthey just decided to get the ball and run with it,
taking advantage of the fact that, as implementors,
they had the final say on what counted as “standard”
(de factoif notde jure):
exactly the same attitude with whichMicrosofttried taking over the web
throughInternet Explorerat the time of theFirst browser war,
an attitude that was rightly condemned at the time
—even as many of those who did, have so far failed to acknowledge the problem
with Google's no less detrimental approach.

The key point here is that,
whatever theWHATWGwas (or was intended to be)
when it was founded byOperaandMozilladevelopers,
it is now manifestly a corporate monster.
Their corporate stakeholder have a very different vision of what the Web should be
compared to the vision on which the Web was founded, the vision promoted by theW3C,
and the vision that underlies a truly open and independent web.

The WHATWG aim is to turn the Web into anapplication delivery platform,
a profit-making machine for corporations where the computer
(and the browser through it)
are a means forthemto make money offyourather than foryouto gain access to services you may be interested in.
Because of this, the browser in their vision is not a User Agent anymore,
but a tool that sacrifices privacy, actual security and user control
at the behest of the corporations “on the other side of the wire”
—and of their political interests
(refs. forApple,Google,
anda more recent list with all of them together).

Such vision is in direct contrast with that of the Web as arepository of knowledge, a vast vault of interconnecteddocumentswhose value emerges from organic connections, personalization,
variety, curation anduser control.
But who in the WHATWG today would defend such vision?

## A new browser war?

Maybe what we need is a new browser war.
Not one of corporation versus corporation
—doubly more so when all currently involved parties are allied
in their efforts to enclose the Web than in fostering an open and independent one—
but one of users versus corporations,
a war to takebackcontrol of the Web and its tools.

It's kind of ironic that in a time whenhostinghas become almost trivial,
the fight we're going to have to fight is going to be on theclientside.
But the biggest question is: who do we have as champions on our side?

I would have liked to see browsers likeVivaldi,
the spiritual successor tomy beloved classic Opera browser,
amongst our ranks,
but with their dependency on theBlinkrendering engine, controlled by Google,
they won't be able to do anything but cave,
as will all other FLOSS browsers relying on Google's or Apple's engines,
none of which I foresee spending any significant efforts rolling back the extensive changes that these deprecations will involve.
(We see this already when it comes to JPEG XL support,
but it's also true that e.g. Vivaldi has made RSS feeds first-class documents,
so who knows, maybe they'll find a way for XSLT through the polyfill that was mentioned above,
or something like that?)

Who else is there?
There isServo, the rendering engine that was being developed at Mozilla to replace Gecko,
and that turned into an independent project when its team was fireden massein 2020;
but they don't support XSLT yet,
and I don't see why they would prioritize its implementation over, say, stuff like MathML or SVG animations with SMIL
(just to name two of my pet peeves), or optimizing browsing speed
(seriously, try openingthe home page of this siteand scrolling through).

What we're left with at the moment is basically just Firefox forks,
and two of these (LibreWolfandWaterFox)
are basically just “Firefox without the most egregious privacy-invasive misfeatures”,
which leaves the question open about what they will be willing to do when Mozilla helps Google kill XSLT,
and only the other one,Pale Moon, has grown into its own independent fork
(since such an old version of Firefox, in fact, that it doesn't support WebExtensions-based plugins,
such as the most recent versions of crucial plugins likeuBlock OriginorPrivacy Badger,
although it's possible to install community-supported forks of these plugins designed
for legacy versions of Firefox and forks like Pale Moon).

(Yes, I am aware that there are other minor independent browser projects,
likeDilloandLadybird,
but the former is in no shape of being a serious contender for general use
on more sophisticated pages —just see it in action on this site, as always—
and the latter is not even in alpha phase,
just in case the questionable “no politics” policies
—which consistently prove to be weasel words for “we're right-wingers but too chicken to come out as such”—
weren't enough to stay away from it.)

Periodically, I go through them (the Firefox forks, that is) to check if they are good enough for me to become my daily drivers.
Just for you (not really: just for me, actually), I just tested them again.
They're not ready yet, at least not for me, although I must say that I'm seeing clear improvements since my last foray into the matter,
that wasn't even that long ago.
In some cases, I can attest that they are even better than Firefox:
for example, Pale Moon and WaterFox have good JPEG XL support
(including transparency and animation support,
which break in LibreWolf as they do in the latest nightly version of Firefox I tried),
and Pale Moon still has first-class support for RSS,
from address bar indicator to rendering even in the absence of a stylesheet
(be it CSS or XSLT).

(A suggestion? Look into moremicroformatssupport.
An auxiliary bar with previous/next/up links on pages where this is relevant
would be a nice touch, for example.It's one of those little details that really made classic Opera shine.
EDIT: Ijust found outthat there'sa relevant addonfor Pale Moon!)

An interesting difference is that the user interface of these browsers is perceivably less refined than Firefox'.
It's a bit surprising, given the common roots,
but it emerges in several more and less apparent details,
from the spacing between menu items to overlapping text and icons in context menus,
passing through incomplete support for dark themes and other little details that all add up,
giving these otherwise quite valid browsers and amateurish feeling.

And I get it: UI design is hard, and I myself suck at it, so I'm the last person that should be giving recommendations,
but I'm still able to differentiate between more curated interfaces and ones that need some work;
and if even someone like me who distinctly prefers function over form finds these little details annoying,
I can imagine how much worse this may feel to users who care less about the former and more about the latter.
Sadly, if a new browser war is to be fought to wrestle control from the corporate-controlled WHATWG,this matters.

In the end, I find myself in a “waiting” position.
How long will it take for Firefox to kill their XSLT support?
What will its closest forks
(WaterFox in particular is the one I'm eyeing)
be able to do about it?
Or will Pale Moon remain the only modern broser with support for it,
as a hard fork that has since long gone its own way?
Will they have matured enough to become my primary browsers?
We'll see in time.

## Another web?

There's more to the Internet than the World Wide Web built around theHTTPprotocol and theHTMLfile format.
There used to bea lotof the Internet beyond the Web,
and while much of it still remains as little more than a shadow of the past,
largely eclipsed by the Web and what has been built on top of it
(not all of it good) outside of some modest revivals,
there's also new parts of it that have tried to learn from the past,
and build towards something different.

This is the case for example of the so-called “GeminiSpace”,
a small corner of the Internet that has nothing to do with the LLM Google is trying to shove down everyone's throat,
and in fact not only predates it,as I've mentioned already,
but is intentionally built around dfferent technology tostay awayfrom the influence of Google and the like.

The Gemini protocol is designed to be conceptually simpler than HTTP,
while providing modern features like built-in transport-level security
and certificate-based client-side authentication,
and its own “native” document format, the so-calledgemtext.

As I said inmy aforementioned Fediverse thread:

There's something to be said about not wanting to share your environment with the poison that a large part of the web has become,
but at the same time, there's also something to be said about throwing away the baby with the bathwater.
The problem with the web isn't technical, it's social. The tech itself is fine.

I'm not going to write up an extensive criticism of the Gemini Space:
you canfind here an older opinionby the author ofcurl,
(although it should be kept in mind that things have changed quite a bit since:
for example,the specification of the different components has been separated,
as suggested by Daniel),
andsome criticism about how gemtext is used.

I'm not going to sing the praises of the Gemini protocol or gemtext either,
even though I do like the idea of a web built on lightweight markup formats:
I would love it if browsers had native support for formats likeMarkdownorAsciiDoc(and gemtext, for the matter):
it's why I keep theAsciiDoctor Browser Extensioninstalled.

But more in general, the Web (or at least its user agents) should not differentiate.
It should not differentiate by protocol, and it should not differentiate by format.
We've seen it with image formats likeMNGbeing unfairly excluded,
with [motivations based on alleged code bloat][nomng] that today are manifest in their idiocy
(and yes, it hasn't escaped my that even Pale Moon doesn't support the format),
and we're seeing it today with JPEG XL threatened with a similar fate,
without even gracing us with a ridiculous excuse.
On the upside, we have browsers shipping witha full-fledged PDF reader,
which is a good step towards the integration of this format with the greater Web.

In an ideal world, browsers would have not deprecated older protocols
likeGopherorFTP,
and would just add support for new ones like Gemini,
as they would have introduced support for new (open) document formats as they came along.

(Why insist on theopenpart?Inanother Fediverse thread about the XSLT deprecationI had an interesting discussion with theOPaboutSWF,theinteractive multimedia format for the Web at the turn of the century.
TheAdobe Flash Playerultimately fell out of favour,
arguably due to the advent of mobile Internet:
it has been argued thatthe iPhone killed Flash,
and while there's some well-deserved criticism of hypocrisy levelled againstSteve JobsinfamousThoughts on Flashletter,
itistrue that what ultimatellytrulykilled the format was it being proprietary and not fully documented.
And while we might not want to cry about the death of a proprietary format,
it remains true even today that the loss of even just legacy suport for ithas been a significant loss to culture and art,
as argued by@whiteshark​@mastodon.social.)

## A Web of interconnected software?

It shouldn't be up to the User Agent to determine which formats the user is able to access, and through which protocol.
(If I had any artistic prowess (and willpower), I'd hack the “myth of consensual X” meme
representing the user and the server saying “I consent”, and the browser saying “I don't”.)
I do appreciate that there is a non-trivial maintenance cost that grows with the number of formats and protocols,
butwe know from classic Operathat it is indeed quite possible
toship a full Internet suitein a browser packaging.

In the old days, browser developers were well-aware that a single vendor couldn't “cover all bases”,
which is how interfaces like the once ubiquituousNPAPIwere born.
The plug-in interface has been since removed from most browsers,
an initiativeagain promoted by Google, announced in 2013 and completed in 2015
(I should really add this tomy previous post on Google killing the open web,
but I also really don't feel like touching that anymore; here will have to suffice),
with the other major browsers quickly following suit,
and its support is now relegated only to independent browsers like Pale Moon.

And even if it can be argued that the NPAPI specifically was indeed mired with unfixable security and portability issues and it had to go,
its removal without a clear cross-browser upgrade path has beena significant loss for the evolution of the web,
destroying the primary “escape hatch” to solve the chicken-and-egg problem of client-side format support versus server-side format adoption.
By the way, it was also responsible for the biggestW3Cblunder,
the standardization ofDRMfor the web through the so-calledEncrypted Media Extensions, a betrayal of the W3C own mission statement.

### The role of multimedia streaming in the death of the User Agent

The timeline here is quite interesting, and correlates withthe already briefly mentioned history of Flash,
and its short-livedMicrosoft Silverlightcompetitor, that were largely responsible forthe early expansive growth of multimedia streaming servicesin the early years of the XXI century:
with the tension between Apple's effort to kill Flash
and the need of emerging streaming services likeNetflix' andHulu's
to support in-browser multimedia streaming,
there was a need to improve support for multimedia formats in the nascentHTML5specification,
but also a requirement from theMAFIAApartners
that such a support would allow enforcing the necessary restrictions that would, among other things, prevent users from saving a local copy of the stream,
something that could be more easily enforced within the Flash players the industries had control over
than in aUser Agentcontrolled bythe user.

This is where the development ofEMEcame in in 2013:
this finally allowed a relatively quick phasing out of the Flash plugin,
anda posterioriof the plugin interface that allowed its integration with the browsers:
by that time, the Flash plugin was by and largetheplugin the API existed for,
and the plugin itself was indeed still supported by the browsers for some time after support for the API was otherwise discontinued
(sometimes through alternative interfaces such as thePPAPI,
other times by keeping the NPAPI support around, but only enabled for the Flash plugin).

There are several interesting consideration that emerge from this little glimpse at the history of Flash and the EME.

First of all,
this is one more piece of history that goes to show how pivotal the year 2013 was for the enshittification of the World Wide Web,as discussed already.

Secondly,
it shows how the developers of major browsers are more than willing to provide a smooth transition path with no user intervention,
at least when catering to the interests of major industries.
This indicates that when they don't, it's not because theycan't:
it's becausethey have a vested interest in not doing it.
Major browser development is now (and has been for over a decade at least)
beholden not to the needs and wants oftheir own users,
but to those of other industries.But I repeat myself.

And thirdly, it's an excellent example, for the good and the bad, of how the plugin interface has helped drive the evolution of the web,as I was saying.

### Controlled evolution

The removal of NPAPI support,
followed a few years later by the removal of the (largely Chrome-specific) PPAPI interface
(that was supposed to be the “safer, more portable” evolution of NPAPI),
without providinganyalternative,
is a very strong indication of the path that browser development has taken in the last “decade plus”:
a path where the Web is entirely controlled by what Google, Apple and Microsoft
(hey look, it'sGAFAMall over again!) decide about what is allowed on it,
and what isnotallowed tonotbe on it (to wit, ads and other user tracking implements).

In this perspective,
the transition from plugins tobrowser extensionscannot be viewed (just) as a matter of security and portability,
but —more importantly, in fact— as a matter of crippled functionality:
indeed, extensions maintainenough capabilitiesto bea vector of malware and adware,
butnot enoughto circumvent unwanted browser behavior,
doubly more so with the so-calledExtension Manifest V3specifically designed to thwart ad blockingas I've already mentioned in the previous post of the series.

With plugins,anythingcould be integrated in the World Wide Web,
and such integration would be close to as efficient as could be.
Without plugins, such integration, when possible at all,
becomes clumsier and more expensive.

As an example, there are browser extensions that can introduce support for JPEG XL to browsers that don't have native support.
This provides a workaround to display such images in said browsers,
but when a picture with multiple formats is offered
(which is what I do e.g. to provide a PNG fallback for the JXL images I provide),
this results inboththe PNGandJXL formats being downloaded,increasingthe amount of data transferred instead of decreasing it
(one of the many benefits of JXL over PNG).
By contrast, a plugin could register itself a handler for the JPEG XL format,
and the browser would then be able to delegate rendering of the image to the plugin,
only falling back to the PNG in case of failure,
thus maximizing the usefulness of the format pending a built-in implementation.

The poster child of this lack of efficiency is arguablyMathJax,
that has been carrying for nearly two decades the burden of bringing math to the web while browser implementors slacked off on their MathML support.
And while MathJaxdoesoffer more than just MathML support for browers without native implementations,
there is little doubt that it would be more effective in delivering the services it delivers
if it could be a plugin rather than a multi-megabyte
(any efforts to minimize its size notwithstanding)
JavaScript library each math-oriented website needs to load.

(In fact, it is somewhat surprising that there isn't a browser extesion version of MathJax that I can find
other than aGreaseMonkeyuser script with convoluted usage requirements,
but I guess this is the cost we have to pay for the library flexibility,
and the sandboxing requirements enforced on JavaScript in modern browsers.)

Since apparently “defensive writing” is a thing we need when jotting down an article such as this
(as if it even matters, given how little attention people give to what they read —if they read it at all— before commenting),
I should clarify that I'm not necessarily for a return to NPAPI advocating.
We have decades of experience about what could be considered the actual technical issues with that interface,
and how they can be improved upon
(which is for example what PPAPI allegedly did,
before Google decided it would be better off to kill plugins entirely
and thus gain full control of the Web as a platform),
as we do about sandboxing external code running in browsers
(largely through the efforts to sandbox JavaScript).
A better plugin API could be designed.

It's not going to happen.
It is now apparent that the major browsers explicitly and intentionally do not want to allow the kind of flexibility that plugins would allow,
hiding their controlling efforts behind security excuses.
It would thus be up to the minority browsers to come up with such an interface
(or actually multiple ones, at least one for protocols and one for document types),
but with most of them beholden to the rendering engines controlled by Google
(for the most part), Apple (some, still using WebKit over Blink), and Mozilla (the few Firefox forks),
they are left with very little leeway, if any at all, in terms of what they can support.

But even if, by some miraculous convergence, they did manage to agree on and implement support for such an API,
would there actually be an interest by third party to develop plugins for it?
I can envision this as a way for browsers to share coding efforts in supporting new protocols and formats before integrating them as first-class
(for example, thealready mentionedGemini protocol and gemtext format could be implemented first as a plugin
to the benefit of any browsers supporting such hypothetical interfaces)
but there be any interest in developing for it, rather tha just trying to get the feature implemented in the browsers themselves?

### A mesh of building blocks

Still, let me dream a bit of something like this,
a browser made up of composable components,
protocol handlers separate from primary document renderers separate from attachment handlers.

A new protocol comes out?

Implement a plugin to handle that, and you can test it by delivering the same content over it,
and see it rendered just the same from the other components in the chain.

A new document format comes out?

Implement a plugin to handle that, and it will be used to render documents in the new format.

A new image format comes out?

Implement a plugin to handle that, and any image in the new format will be visible.

A new scripting language comes out?

You guessed it: implement a plugin to handle that …

How much tech would have had a real chance at proving itself in the field if this had been the case,
or would have survived being ousted not by technical limitations,
but by unfriendly corporate control?
Who knows, maybe
RSS and Atom integration would still be trivially at everybody's hand;
nobody would have had to fight with the long-standing bugs in PNG rendering from Internet Explorer,
MNG would have flourished, JPEG XL would have become ubiquituous six months after the specification had been finalized;
we would have seen HTML+SMIL provide declarative interactive documents without JavaScript as far back as 2008;
XSLT 2 and 3 would have long superseded XSLT 1 asthetemplating languages for the web,
or XSLT would have been supplanted by the considerably more accessible XQuery;
XHTML2 would have lived and grown alongside HTML5,
offering more sensible markup for many common features,
and much-wanted capabilities such as client-side includes.

The web would have been very different from what it is today,
and most importantly we would never would have had to worry
about a single corporation getting to dictate what is and what isn't allowed on the Web.

But the reality is much harsher and darker.
Google has control, and we do need to wrestle it out of their hands.

## Resist

So, do not comply.Resist.Force the unwanted tech through.Use RSS.Use XSLT.Adopt JPEG XL as your primary image format.And report newly broken sites for what they are:a browser fault, not a content issue.

## Post scriptum

I would like to add here anypièces de résistancefor XSLT.

I'm going to inaugurate with a linkI've just discoveredthanks toJWZ:

1. xslt.rip(best viewed with a browser that supports XSLT; viewing the source is highly recommended);
2. and last but not least (yeah I know, doesn't make much sense with the current short list, but still),
a shameless plug ofmy own website, of course,
because of the idea to use XSLT not to produce HTML, but to produce SVG.

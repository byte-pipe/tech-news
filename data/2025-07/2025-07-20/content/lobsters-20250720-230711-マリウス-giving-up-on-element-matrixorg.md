---
title: マリウス . Giving Up on Element & Matrix.org
url: https://xn--gckvb8fzb.com/giving-up-on-element-and-matrixorg/
site_name: lobsters
fetched_at: '2025-07-20T23:07:11.924862'
original_url: https://xn--gckvb8fzb.com/giving-up-on-element-and-matrixorg/
date: '2025-07-20'
published_date: '2025-07-18T16:08:15-05:00'
description: The Matrix.org network has great potential, but after years of dealing with glitches, slow performance, poor UX, and one too many failures, I’m done with it.
tags: rant
---

TheMatrix.orgnetwork has great potential, but after years of dealing with
glitches, slow performance, poor UX, and one too many failures, I’m done with
it.

Tl;dr:After five years of usingMatrix.org/Elementas my primary
communication platform, and rooting for it,andpromoting it,andenduring its many quirks, I’ve decided to move on (or ratherback). Despite
promising ideals and growing institutional adoption, the network remains slow,
unreliable, and confusing for everyday users. Development feels directionless,
client and server projects are fragmented, and the user experience still lags
far behind my expectations. A recent incident that essentially broke my own
community channel on theMatrix.orghomeserver was the final straw: I’m
heading back toXMPP.

For the past few years, I’ve been trying to makeMatrix.org, and with it theElementclient applications, my primary platform for communication. WhenMozilla announced its move toMatrixback in 2019, it felt like
the ecosystem was finally taking off. A wave of third-party clients andMatrix.org-based projects emerged, and I eagerly hopped on the bandwagon. I
gradually phased out my presence onIRCandXMPP,
hopeful that this would be the nextSlack-orDiscord-killer.

Five years later I’m leaving theMatrix.orgecosystem with a bruised eye and
the bitter aftertaste of a future that never arrived. Let me explain.

Disclaimer:I know the difference betweenMatrix.org, the foundation, andElement, the product developed byNew Vector, the company. However, in order
to tell the story for the casual reader, from a user perspective, I am
intentionally leaving out such details.

## Early days

Matrix.orgbegan just over a decade ago as a federated messaging protocol. Its
primary goal was to make real-time communication seamless across different
providers, similar to how SMTP enables cross-provider email.

“Wait, isn’t that exactly what XMPP has done since forever?”, you might ask.
And you’d be right.Matrix.orgessentially reinvented the wheel, swapping out
XML for JSON and incorporating technologies like WebRTC and, at some point,
end-to-end encryption (E2EE) asbuilt-inrather than anextension, although
from a practical standpoint it doesn’t make much difference as long asmetadata isstill unencrypted.

The project originated insideAmdocs, a software company founded by theAurec
Groupin Israel, which is headquartered in St. Louis, Missouri, USA today, and
employs over twenty-nine thousand people.Amdocsitself has an interesting
(read:controversial) history, with investigations by U.S. federal agencies
into alleged espionage. The history aroundAmdocshas been debated for a few
years now, withMatrix people(“Agents”? *scnr*) rebuttingthe supposedconspiracy theoriesevery once in a while, but that’s a story for another
time.

What matters here is thatAmdocsfunded most ofMatrix’s development from
2014 until the end of 2017, under a subsidiary namedVector Creations Limited.
When that funding ended, the UK-based companyNew Vector Limitedwas formed to
continue development of the protocol and its main client,Riot(now known asElement).

That’s whenMatrix.orgseemed to gain serious traction. The community rallied
to support the newly independent project. Organizations likeKDE, companies such asPurismandStatus, and even the
French government got involved. But while enthusiasm surged, the implementation
quality of core components remained mediocre at best.

The officialMatrixhomeserver,Synapse, was built with a tech stack
ill-suited for its long-term goals and scale. The protocol also implemented
features that drove overall complexity through the roof. Community projects likeDendriteemerged to rewrite the homeserver more sensibly. Some efforts, likeConduit, even received government funding to stabilize the foundationMatrix.orgwas built on.

## Use Matrix!

After Mozilla’s bold move,New Vectorhit the accelerator and wentall gas no
brakes. E2EE became the default for all private conversations.Riotwas
rebranded asElement. Within two years,New Vectoreffectively took overDendriteas its official future homeserver implementation.

Meanwhile,Matrix.orgcontinued to attract interest, especially from European
governments eager to reduce their dependencies on U.S. tech giants. France’s
central administration adoptedTchap, a software based onMatrix.org,
Germany’s armed forces and healthcare institutions rolled outMatrix-based
tools, Luxembourg launched itscreativelynamedLuxchat4Gov, and even
Sweden’s social insurance agency joined in.

The sense thatMatrix.orgwasfinallytaking off was further reinforced by
the rise of projects likeSchildiChatandFUTO Circles, and by the
announcement ofElement X, a new native client promising to eliminate the UX
and performance woes of the oldElectron-basedElementapp. It all sounded
too good to be true.

Encouraged bythe hype, I doubled down on my engagement withMatrix. I
launched an official community channel onMatrix.orgfor topics related to
this site and persuaded several friends to give the platform a try. Group chats,
DMs, community discussions: I wantedMatrixandElementto succeed. I wanted
to love the platform.

## Fast-forward

Today, I’m writing this post to say that I’ve lost hope and patience.

After five years of usingMatrixandElementas my main platform, I no
longer have the energy or desire to keep using it, much less convince others,
especially the people close to me, to do the same.

Despite all the perceived hype a few years ago, the basics of the platform
remain undercooked.New Vectorseems to be chasing too many goals
simultaneously, with no clear direction. Just a few months ago, they migrated to
theMatrixAuthentication Service (MAS), which was supposed to be a
leap forward, yet lacks even essential security features like 2FA/MFA.
Meanwhile, the company appears to have begunquietly phasing outthe classicElementapp in favor ofElement X, even though it still misses crucial
features like threads and spaces, besides the less important things like
widgets, grouping by priority, and live location sharing.

Yes,Element Xis faster than its Electron predecessor, but only relatively.
Compared to other popular communication apps likeSignal,Telegram XorWhatsApp, it’s still slow. Launching the app requires network synchronization
that hampers responsiveness. Especially on older devices (like my GrapheneOStablet) the whole UI feels sluggish in a way you’d usually only expect from
poorly built hybrid apps. On more modern flagship devices the experience isn’t
significantly better either.

TheMatrix.orgservice, especially itsmatrix.orghomeserver, is also slow,
especially onthinnerbroadband connections. On mylaptop, I’ve been usingiamb, a TUIMatrixclient, and even there I experience delays of
tens of seconds when launching it, and a lag of several seconds between pressingEnterand seeing the message actually appear in the chat room. And that’s
certainly notiamb’s fault, becauseit’s written in Rust, btw™. If
you’re accustomed to IRC, XMPP, or even bloated platforms likeDiscord, you’ll
likely findMatrixpainful to work with in comparison.

Thishad been my experience with theElementweb client, even these days. The video was not slowed down, it literally takes
almost 40 seconds for the web UI to just load, with the browser tab running on
100% of a CPU core and munching through plenty of RAM. Once loaded, using the
web UI isn’t much smoother either.

Over the years I’ve tried several times to find a way toabstractthese
performance issues, e.g. by usingMatrixviaIrssi, the popular IRC client,
and aMatrix-IRC-bouncersoftware. However, each of these attempts fell short
of important features, most prominently the lack of E2EE between the bouncer andMatrix, rendering the whole end-to-end-encryption promise thatMatrixis
making useless.

Speaking of E2EE,device cross-verificationis another thing that has
been hauntingMatrix/Elementusers for years and has only gottenless
brokenin the past year or so. The story goes like this: Whenever you log on
from a new device, you have to cross-verify the device using either a secret key
or, more comfortably, another device that has already been verified. Not only
has this feature been particularly complicated to implement for 3rd-party
clients, but even the officialElementandElement Xclients have struggled
to get it right up until recently. Verifications would either not start at all
or simply break in the middle of the process, requiring users to re-start the
process or ultimately give up and use their secret key.

With thecomplexity of the underlying protocoland its
encryption, the pace at which it evolved and the lack of proper first-party
libraries for 3rd-party developers to build on top of, it became visible that
the once-vibrant ecosystem, does no longer look so healthy. Development on
Synapse alternatives has stagnated. EvenConduit, despite its government
support, is largely dormant.Dendritestill isn’t production-ready for large
deployments. And while many community members self-host it, the project has yet
to prove it can scale robustly.

On the client side, things aren’t much better. The FUTO-fundedCirclesclient shut down in 2025, with a quite telling reason.
Other clients likeSchildiChatare faced with the dilemma of continuing their
existing work or starting over by forkingElement X. Given the divergence in
tech stacks, adopting the newermatrix-rust-sdkseems inevitable, but costly.

Speaking of SDKs,New Vectorappears to lack a coherent technology strategy.
They’ve built infrastructure in Python and Node.js/TypeScript, moved into Go for
the Synapse replacement, and now maintain a Rust-based client SDK, while
abandoning their Go client library
(which is now community-maintained). This fragmentation isn’t justmessy, but it’s expensive. Especially for an organization that appearsperpetually cash-strapped.New Vector’s approach feels more like
indecisiveness thanthe right tool for the right jobwhen looking through
theirrepositories on GitHub.

Note:As of writing, the officialElement DendriteimplementationusesGo librariesthat haven’t been updated in months or years, with dependencies that are equally
stale.

## Maybe it’s you?

It’s always worth asking“Is it me?”, before condemning something asbadorbroken. In search of other perspectives, I found mostly positive comments on/r/matrixdotorgand similar sites, from people actively usingElement/Matrix, which, well, isn’t surprising. However, the deeper I dug,
the more Istumbleduponblog-andforum-posts,andcommentthreadsfilledwithexperiences that echoed many of the issues I had
observed and described, e.g.:

Matrix was never good.Have you met a person who actually enjoyed using
Matrix? Because, I haven’t. This isn’t to say that Matrix isn’t more usable
than other open alternatives, but that’s a low bar. There’s a reason why“Unable to decrypt message”is a common gag in the FOSS community. The
promise of what Matrix could become, plus, being already more accessible than
other open alternatives, was what kept me there. I’m willing to bet it’s the
same for many others. However, I’ve come to terms that these ambitions will
not be realized, at least in the current direction

Yes, cartoon person with cat ears, that’s exactly what kept me onMatrix/Elementas well! I could go on for hours linking to posts that
criticize the platform’s functionality. And while this might be a case of
confirmation bias, itfeelslike there don’t seem to be as manydedicated
postspraising howgreatMatrix Element Xisas there are write-ups
of people going into great length to describe their negative experiences with
the platform. Then again, the confusing naming (“SEO”) makes it difficult to
find things in the first place. Just imagine the average Joegooglingthings
like“What to do when Matrix doesn’t work”, or“Why won’t Element start?”–
oh boy.

Matthew, if you’re reading this: We both
know thatnaming thingsis one of the hardest problems in computer science,
right aftercache invalidation. I totally get the geeky,31337thrill a name
likeMatrixmight evoke, but believe me when I say thatusing generic namesis a bad idea. Things
would have been a lot easier for everyone involved if you had at least rebrandedRiotto somethingmoredistinctive. For future rebrandings, I
highly recommend using theSynthwave Band Name Generatorand some good
old human creativity. :-)

## The straw that broke the camel’s back

In early July, I openedElement Xon my phone and noticed an eerie silence in
my community channel there. It wasn’t unusual for the channel to be quiet, but
this feltoff. I tried posting something. Nothing sent.

Puzzled, I switched to my laptop and loadedapp.element.io, only to discover
that the channel wasgone, or at least, I appeared to have left it. It now
showed up under“Suggested”, as if I could rejoin. But I never left it.

Back onElement X, I still appeared to be a member. I suspected a browser
glitch, so I tried it from a clean profile without extensions and cached data.
Same result.

Attempts to rejoin the room failed. Amongst literally dozens of other JavaScript
warnings and errors, even with uBlock Origin turned off –w.. t.. f..– the browser’s developer console showed this
particular one:

rageshake.ts:69 [getVersion] Room !PHlbgZTdrhjkCJrfVY:matrix.org does
not have an m.room.create event

rageshake.ts:69 Failed to update sticky room Error:
!PHlbgZTdrhjkCJrfVY:matrix.org does not belong to a tag and cannot be sticky
at M.doUpdateStickyRoom (Algorithm.ts:196:25)
at M.updateStickyRoom (Algorithm.ts:163:14)
at M.setStickyRoom (Algorithm.ts:115:18)
at G.handleRVSUpdate (RoomListStore.ts:147:32)
at H. (RoomListStore.ts:115:85)
at i.emit (events.js:158:7)
at H.setState (RoomViewStore.tsx:207:14)
at H.viewRoom (RoomViewStore.tsx:433:18)
at H.onDispatch (RoomViewStore.tsx:220:22)
at Object.invokeCallback (dispatcher.ts:115:9)

I reached out to a few channel members, asked in the officialElement Webchannel onMatrix.org, and also contacted theElementsupport (ticket2386). The next day,gonzalo, who runs his own homeserver, helped me
investigate. Surprisingly, he was still part of the channel and could chat with
others. But accounts onmatrix.org, including mine, couldn’t interact with it
at all.

gonzalo and I tried joining the channel with differentmatrix.orgaccounts,
which also failed with the following error for both of us:

MatrixError: [403] No create event in auth events (https://matrix-client.matrix.org/_matrix/client/v3/join/%23root%40localhost%3Amatrix.org?server_name=matrix.org&via=matrix.org)

It was as if thematrix.orghomeserver had somehowlostthe room, without
communicating this to the rest of the network. Even stranger, from gonzalo’s
point of view, I was still in the room, just offline:

I attempted to elevate his permissions via theSpacethat the channel belonged
to, but even though I could add him as an admin, he never saw the change
reflected. And I couldn’t even revoke it:

So much for (overly complex) permission models andMatrixfederation. I would
be genuinely curiouswhat exactly brokethat led to the status of the room
seemingly becomeFUBAR. If it is indeed an issue with theMatrix.orghomeserver havinglosta handful of important events along the way, then I’d
be curious to know how bad the situation could turn out for other communities or
maybe even enterprise customers using the platform.

Note:To prevent comments like“Well, it’s your fault, because you should
have just dropped a message to/in <insert here> to get supportfor your
specific case”:

Sure, I probably could have gone the extra mile and open an issue on GitHub, or
cc the@matrix.orgaddress, or taken any number of other steps. But, from a
real-world user perspective, that’s all nonsense. It’s not the user’s
responsibility to understand the separation betweenMatrix.organdElement,
nor to figure out whose responsiibility a particular issue falls under. That
separation was a deliberate choice made byMatrix.org/Element, not by the
user, which means it’s on them to have the support pipelines in place that
clearly guide users to the right channels. That’s simply not happening.I triedto
reachsomeonewho felt responsible enough to help.

## GoodbyeMatrix.org

With no access to thematrix.orgserver logs and no response from the support
whatsoever, I’ve all but closed theElementchapter in my mind. Till this day
I haven’t heard back from the support team, and I still haven’t regained access
to my channel. While the channel was home to only a few dozenidlers– unlike
theSimpleX roomthat has accumulated over a hundred people in a
fraction of the time – it is nevertheless sad to have lost it just like that.
At least this post can hopefully serve as a cautionary tale for others who are
considering hosting their community onMatrix.org’s homeserver.

Between the slow performance, the increasing amount of spam, the miserable web
client, and the unfinished state ofElement X, theMatrix.orgnetwork is not
something I am willing to continue to recommend, especially to non-technical
users.Normal peopleare simply tolerating it to communicate with idealistic
nerds like myself who insist(ed) on using it.

Despite my experience withElementandMatrix.orgover the past years, I
still believe that they won’t be going anywhere soon. European governments in
particular seem willing to endure all sorts ofdigital tortureif it means
reducing dependency on U.S.big tech. After all, their institutions which have
failed over and over to develop own solutions, and that just“recently”(in
relative terms) migrated off Windows XP and Internet Explorer, yet continue to
use Lotus Notes and fax machines, are unlikely to be deterred by sluggish UIs or
bizarre permission bugs.

But as long as things remain as they are, I don’t see the general public warming
toMatrix.org/Element. The platform is cumbersome for newcomers and lacks
user-facing features that people actually want, while simultaneously
overexposing complex settings like roles, permissions, and addresses. It’s the
idealenterprise software– and I don’t mean that as a compliment. Even
overloaded platforms like Discord ultimately focus on what users want:Dumbemojis and stickers,sillycolor themes, and intuitiveserverand friend
management.Matrix, by contrast, feels like it was built for compliance
departments and bureaucrats, not communities.

This is where I part ways withElement/Matrix.org. Not out of bitterness
over losing my channel, and not out of frustration over the complete lack of
support, but out of exhaustion from dealing with glitches and a frankly terrible
user experience on a regular basis.

I’m still all for the ideals behind the project: Open protocols, privacy by
design, decentralized and federated infrastructure, and maybe one daypeer-to-peernetworking. Unfortunately ideals alone don’t
make for usable tools. At this stage, I have to admit that the user experience
on XMPP… heck, even on the IRC, is so much superior to whatElement/Matrix.orgdelivers, that it doesn’t make any sense at all for me to
continue moving into this direction. Considering that a self-hostedDendriteinstance should ideally have, quote:

For a comfortable day-to-day deployment which can participate in federated
rooms for a number of local users, be prepared to assign 2-4 CPU cores and 8GB
RAM — more if your user count increases.

…Matrixends up being worse not just in terms of user experience, but also
from an administrative and cost perspective, especially when compared to
something likeEjabberd, which hashistoricallyproven capable
of supporting large numbers of users even in highly resource-constrained
environments.

Hot take:Erlang/OTP isrenowned for handlingridiculousnumbers of
concurrent usersand has been
battle-testedfor decadesin distributed systems,especially in comms platforms.
To this day, I cannot comprehend whyMatrix.orgchose to usePythonandNode.jsof all things, instead of Erlang, or more recently, Elixir. This feels
like such a low-hanging fruit in terms of architecture design, yetMatrix.org,
and later onNew Vectornever really appear to have had that lightbulb moment
of“Hey, wait, theOpen Telecom PlatformprovideseverythingMatrix needs
right out of the box and would make large-scale deployments significantly easier
(and cheaper) – let’s use that!”. Imagine how beautifully simple aclustercould have been set up, without the headache that is Kubernetes. Imagine how“easy”integrating anXMPP bridgeintoMatrixcould have been, in comparison to thefrankensteinedthing that it is today.
Heck, they could have straight-up forkedEjabberdand built their protocols
and ideas on the shoulders of this two-decade-old giant, while continuing to
natively support XMPP for migration purposes.Matrixwould have had a near
drop-in replacement for administrators who’d like totry before they buy, to
ease the transition from XMPP toMatrix. And they still could have leveraged
the Rust expertise they gained while building the client SDK in areas where
low-level performance is critical, viaErlang’s
Native Implemented Functions (NIFs).

I truly hope the team behindMatrix.orgfinds their footing, because the worlddoesneed an open alternative to the corporate silos that are Slack, Teams,
Discord and all the others. But until that vision materializes into something
dependable, fast, and user-friendly, I’ll be elsewhere, quietly rooting for a
comeback, but no longer waiting for it.

## A new home

Over the years, I’ve tried just about everynew thing, only to eventually
return to where my journey began decades ago, namely XMPP (and IRC). This time
is no different. Sure, both platforms have their quirks and limitations, but
their reliability, simplicity, and interoperability remain unmatched.

I want every member of the former community channel onMatrix.orgto know that
there is anew (old) home: XMPP, and that the room onMatrix.orgis
effective immediately arogue roomthat I have no control over. If you have
been part of theMatrix.orgroom, I would be happy to have you on theVT100multi-user chatroom, as well as on my own roster on XMPP. If you are new here
or on XMPP in general, I also invite you to join the shindig: Find yourself a
suitableXMPP client, and sign up onaninstanceorhost it yourself.

While thenewXMPP instance is operable, I’m still improving things here and
there and dealing with quirks along the way, so it might be that its
availability might only reach 73.31% atm. Things on my todo list include making
the instance available via Tor and I2P, setting up a dedicated rewrite proxy forUnifiedPush, as well as (maybe at some point) setting up an IRCv3 server
alongside the XMPP service and create a dedicated channel there as well.

PS: TheSimpleX roomis still around as well, just in case you prefer
aneasier to useoption. However, keep in mind that this is another
non-self-governing space that’s at the mercy of the operating platform.

Footnote:The artwork was generated using AI and further botched by me using
thegreatest image manipulation program. The original artwork was
shamelessly stolen from the incredibly talented artists behindWatch Dogs 2, which, to this day,
is arguably one of the best third-person action-adventures ever made – fight
me. They crafted a brilliant and worthy homage to the mid-1960s horror comic
genre and glitched it up with a dose of ’90s pixel and ANSI art. And no, I’m not
just honeydickin’ Ubisoft to persuade them to not sue me for using their IP; I’d
assume they currentlyhave bigger yaks to shaveanyway.

Enjoyed this?Please consider supporting my work.

Published on

2025-07-18

and updated on

2025-07-18

in

journal

and tagged with

decentralization

infrastructure

irc

open-source

privacy

security

xmpp

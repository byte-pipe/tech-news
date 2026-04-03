---
title: Where It's at:// — overreacted
url: https://overreacted.io/where-its-at/
site_name: hackernews
fetched_at: '2025-10-04T19:07:55.864724'
original_url: https://overreacted.io/where-its-at/
author: steveklabnik
date: '2025-10-04'
description: From handles to hosting.
---

# Where It's at://

October 2, 2025

Pay what you like

You might have heard about the AT protocol (if not,read this!)

Together, all servers speaking the AT protocol comprisethe atmosphere—a web of hyperlinked JSON. Each piece of JSON on the atmosphere has its ownat://URI:

* at://ruuuuu.de/app.bsky.feed.post/3lzy2ji4nms2z
* at://danabra.mov/sh.tangled.feed.star/3m23ddgjpgn22
* at://tessa.germnetwork.com/pub.leaflet.publication/3lzz6juivnc2d

But where do they point, exactly?

Given anat://URI, how do you locate the corresponding JSON?

In this post, I’ll show you the exact process of resolving anat://URI step by step. Turns out, this is also a great way to learn the details of howat://works.

Let’s start with the structure of a URI itself.

### The User as the Authority

As you might know, a URI often contains a scheme (for example,https://), anauthority(likewikipedia.com), a path (like/Main_Page), and maybe a query.

In most protocols, includinghttps://, the authority part points at whoever’shostingthe data. Whoevercreatedthis data is either not present, or is in the path:

https:///profile//post/3lzy2ji4nms2zbsky.appruuuuu.dethe appthe user

Theat://protocol flips that around.

Inat://URIs, whoevercreatedthe data is the authority, in the most literal sense:

the formatthe user.feed.post/3lzy2ji4nms2zat:///app.bskyruuuuu.de

The user is the authority for their own data.Whoever’shostingthe data could change over time, and isnotdirectly included in anat://URI. To find out the actual physical server hosting that JSON, you’re gonna need to take a few steps.

### A Post in the Atmosphere

Let’s try to resolve thisat://URI to the piece of JSON it represents:

the formatthe user.feed.post/3lzy2ji4nms2zat:///app.bskyruuuuu.de

An easy way to resolve anat://URI is to use anSDKor a client app. Let’s try an online client, for example,pdslsorTaprootoratproto-browser. They’ll figure out the physical server where its JSON is currently hosted, and show that JSON for you.

The aboveat://URI points at this JSON, wherever it is currently being hosted:

{

 "
uri
"
:
"
at://did:web:iam.ruuuuu.de/app.bsky.feed.post/3lzy2ji4nms2z
"
,

 "
cid
"
:
"
bafyreiae4ehmkk4rtajs5ncagjhrsv6rj3v6fggphlbpyfco4dzddp42nu
"
,

 "
value
"
:
{

 "
text
"
:
 "
posting from did:web, like a boss
"
,

 "
$type
"
:
 "
app.bsky.feed.post
"
,

 "
langs
"
:
 [
"
en
"
],

 "
createdAt
"
:
 "
2025-09-29T12:53:23.048Z
"

 }

}

You can guess by the$typefield being"app.bsky.feed.post"that this is some kind of a post (which might explain why it has fields liketextandlangs).

However, note that this piece of JSON represents a certain social media postitself, not a web page or a piece of some app.It’s pure data as a piece of JSON, not a piece of UI. You may think of the$typestating the dataformat; theapp.bsky.*prefix tells us that thebsky.appapplication might know something about what to do with it. Other applicationsmay alsoconsume and produce data in this format.

A careful reader might notice that theuriin the JSON block isalsoanat://URI but it’s slightly different from the originalat://URI we requested:

// What's at://ruuuuu.de/app.bsky.feed.post/3lzy2ji4nms2z ?

{

 "
uri
"
:
"
at://did:web:iam.ruuuuu.de/app.bsky.feed.post/3lzy2ji4nms2z
"
,

 // ...

}

In particular, the shortruuuuu.deauthority has expanded into a longerdid:web:iam.ruuuuu.deauthority. Maybe that’s the physical host?

Actually, no, that’s not the physical host either—it’s something called anidentity. Turns out, resolving anat://URI is done in three distinct steps:

1. Resolve the handle to an identity(“who are you?”)
2. Resolve that identity to a hosting(“who holds your data?”)
3. Request the JSON from that hosting(“what is the data?”)

Let’s go through each of these steps and see how they work.

### From Handles to Identities

Theat://URIs you’ve seen earlier are fragile because they use handles.

Here,ruuuuu.de,danabra.mov, andtessa.germnetwork.comare handles:

* at://ruuuuu.de/app.bsky.feed.post/3lzy2ji4nms2z
* at://danabra.mov/sh.tangled.feed.star/3m23ddgjpgn22
* at://tessa.germnetwork.com/pub.leaflet.publication/3lzz6juivnc2d

(Read more aboutdomains as “internet handles” here.)

The user may choose to change theirat://handle later, and it is important for that not to break any links between pieces of JSON already on the network.

This is why, before youstoreanat://URI, you should turn it into a canonical form by resolving the handle to something that never changes—anidentity. An identity is like an account ID, but global and meant for the entire web. There are two mechanisms to resolve a handle to an identity (also known as a “DID”):

1. Query the DNS TXT record at_atproto.<handle>looking fordid=???
2. Make an HTTPS GET tohttps://<handle>/.well-known/atproto-did

The thing you’re looking for, the DID, is going to have a shape likedid:something:whatever. (We’ll revisit what that means later.)

For example, let’s try to resolveruuuuu.devia the DNS mechanism:

$
 nslookup
 -type=TXT
 _atproto.ruuuuu.de

Server:
		192.168.1.254

Address:
	192.168.1.254#53



Non-authoritative
 answer:

_atproto.ruuuuu.de
	text
 =
 "
did=did:web:iam.ruuuuu.de
"

Found it!

Theruuuuu.dehandleclaimsto be owned bydid:web:iam.ruuuuu.de, whoever that may be. That’s all that we wanted to know at this point:

at://at://did:web:iam.ruuuuu.de/.../...ruuuuu.de

Note this doesn’tprovetheir association yet.We’ll need to verify that whoever controls thedid:web:iam.ruuuuu.deidentity “agrees” withruuuuu.debeing their handle. The mapping is bidirectional. But we’ll confirm that in a later step.

Now let’s try to resolvedanabra.movusing the DNS route:

$
 nslookup
 -type=TXT
 _atproto.danabra.mov

Server:
		192.168.1.254

Address:
	192.168.1.254#53



Non-authoritative
 answer:

_atproto.danabra.mov
	text
 =
 "
did=did:plc:fpruhuo22xkm5o7ttr2ktxdo
"

That also worked! Thedanabra.movhandle claims to be owned by thedid:plc:fpruhuo22xkm5o7ttr2ktxdoidentity, whoever that may be:

at://at://did:plc:fpruhuo22xkm5o7ttr2ktxdo/...danabra.mov/...

This DID looks a bit different than what you saw earlier but it’s also a valid DID. Again, it’s important to emphasize we’ve not confirmed the association yet.

Subdomains likebarackobama.bsky.socialcan also be handles.

Let’s try to resolve it:

$
 nslookup
 -type=TXT
 _atproto.barackobama.bsky.social

Server:
		192.168.1.254

Address:
	192.168.1.254#53



Non-authoritative
 answer:

***
 Can
'
t find _atproto.barackobama.bsky.social: No answer

The DNS mechanism didn’t work, so let’s try with HTTPS:

$
 curl
 https://barackobama.bsky.social/.well-known/atproto-did

did:plc:5c6cw3veuqruljoy5ahzerfx

That worked! This means thatbarackobama.bsky.socialhandle claims to be owned by thedid:plc:5c6cw3veuqruljoy5ahzerfxidentity, whoever that is:

at://at://did:plc:5c6cw3veuqruljoy5ahzerfx/.../...barackobama.bsky.social

So you get the idea. When you see a handle, you can probe it with DNS and HTTPS to see if it claims to be owned by some identity (a DID). If you found a DID, you’ll then be able to (1) verify it actually owns that handle, and (2) locate the server that hosts the data for that DID. And that will be the server you’ll ask for the JSON.

In practice, if you’re building with AT, you’ll likely want to either deploy your own handle/did resolution cache or hit an existing one. (Here’sone implementation.)

### AT Permalinks

Now you know how handles resolve to identities, also known as DIDs. Unlike handles, which change over time, DIDs never change—they’re immutable.

Theseat://links, which use handles, are human-readable but fragile:

* at://ruuuuu.de/app.bsky.feed.post/3lzy2ji4nms2z
* at://danabra.mov/sh.tangled.feed.star/3m23ddgjpgn22
* at://tessa.germnetwork.com/pub.leaflet.publication/3lzz6juivnc2d

They will break if one of us changes a handle again.

In contrast, theat://links below, which use DIDs, will not break until we either delete our accounts, delete these records, or permanently take down our hosting:

* at://did:web:iam.ruuuuu.de/app.bsky.feed.post/3lzy2ji4nms2z
* at://did:plc:fpruhuo22xkm5o7ttr2ktxdo/sh.tangled.feed.star/3m23ddgjpgn22
* at://did:plc:ad4m72ykh2evfdqen3qowxmg/pub.leaflet.publication/3lzz6juivnc2d

So, really, this is the “true form” of anat://URI:

the formatthe user.feed.post/3lzy2ji4nms2zat:///app.bskydid:web:iam.ruuuuu.de

Think ofat://links with DIDs as “permalinks”.Any applicationstoringat://URIs should store them in this canonical form so that logical links between our pieces of JSON don’t break when we change our handles or change our hosting.

Now that you know how to resolve a handle to a DID, you want to do two things:

1. Verify that whoever owns this DID actually goes by that handle.
2. Find the server that hosts all the data for this DID.

You can do both of these things by fetching a piece of JSON called theDID Document. You can think of it as sort of a “passport” for a given DID.

How you do that depends on what kind of DID it is.

### From Identities to Hosting

Currently, there are two kinds of DIDs, known asDID methods, supported by the AT protocol:did:web(aW3C draft) anddid:plc(specifiedby Bluesky).

Let’s compare them.

#### did:web

Theruuuuu.dehandle claims to be owned bydid:web:iam.ruuuuu.de:

at://at://did:web:iam.ruuuuu.de/.../...ruuuuu.de

To check this claim, let’s find the DID Document fordid:web:iam.ruuuuu.de. Thedid:webmethodis a specification that specifies analgorithmfor that.

In short, you cut off thedid:web:from the DID, append/.well-known/did.jsonto the end, and run an HTTPS GET request:

$
 curl
 https://iam.ruuuuu.de/.well-known/did.json
 |
 jq

{

 "@context"
:
 [

 "https://www.w3.org/ns/did/v1"
,

 "https://w3id.org/security/multikey/v1"
,

 "https://w3id.org/security/suites/secp256k1-2019/v1"

 ],

 "id"
:
 "
did:web:iam.ruuuuu.de
",

 "alsoKnownAs"
:
 [

 "at://ruuuuu.de"

 ],

 "verificationMethod"
:
 [

 {

 "id"
:
 "
did:web:iam.ruuuuu.de#atproto
",

 "type"
:
 "
Multikey
",

 "controller"
:
 "
did:web:iam.ruuuuu.de
",

 "publicKeyMultibase"
:
 "
zQ3shWHtz9QMJevcGBcffZBBqBfPo55jJQaVDuEG7ZwerALGk
"

 }

 ],

 "service"
:
 [

 {

 "id"
:
 "
#atproto_pds
",

 "type"
:
 "
AtprotoPersonalDataServer
",

 "serviceEndpoint"
:
 "
https://blacksky.app
"

 }

 ]

}

This DID Document looks sleep-inducing but it tells us three important things:

* How to refer to them.ThealsoKnownAsfield confirms that whoever controlsdid:web:iam.ruuuuu.deindeed wants to use@ruuuuu.deas a handle. ✅
* How to verify the integrity of their data.ThepublicKeyMultibasefield tells us the public key with which all changes to their data are signed.
* Where their data is stored.TheserviceEndpointfield tells us the actual server with their data. Rudy’s data is currently hosted athttps://blacksky.app.

A DID Document reallyislike an internet passport for an identity: here’s their handle, here’s their signature, and here’s their location. It connects a handle to a hosting while letting the identity owner changeeitherthe handleorthe hosting.

did:web:iam.ruuuuu.deblacksky.app@ruuuuu.dehandle (swappable)hosting (swappable)didserviceEndpointalsoKnownAs

Users who interact with@ruuuuu.deon different apps in the atmosphere don’t need to know or care about his DIDorabout his current hosting (and whether it moves). From their perspective, his current handle is the only relevant identifier. As for developers, they’ll refer to him by DID, which conveniently never changes.

All of this sounds great, but there is one big downside to thedid:webidentity. Ifdid:web:iam.ruuuuu.deever loses control of theiam.ruuuuu.dedomain, he will lose control over his DID Document, and thus over his entire identity.

Let’s have a look at an alternative todid:webthat avoids this problem.

#### did:plc

We already know thedanabra.movhandle claims to be owned by thedid:plc:fpruhuo22xkm5o7ttr2ktxdoidentity (actually, that’s me!)

at://at://did:plc:fpruhuo22xkm5o7ttr2ktxdo/...danabra.mov/...

To check this claim, let’s find the DID Document fordid:plc:fpruhuo22xkm5o7ttr2ktxdo.

Thedid:plcmethodis a specification that specifies analgorithmfor that.

Essentially, you need to hit thehttps://plc.directoryservice with aGET:

$
 curl
 https://plc.directory/did:plc:fpruhuo22xkm5o7ttr2ktxdo
 |
 jq



{

 "@context"
:
 [

 "https://www.w3.org/ns/did/v1"
,

 "https://w3id.org/security/multikey/v1"
,

 "https://w3id.org/security/suites/secp256k1-2019/v1"

 ],

 "id"
:
 "
did:plc:fpruhuo22xkm5o7ttr2ktxdo
",

 "alsoKnownAs"
:
 [
"
at://danabra.mov
"
],

 "verificationMethod"
:
 [

 {

 "id"
:
 "
did:plc:fpruhuo22xkm5o7ttr2ktxdo#atproto
",

 "type"
:
 "
Multikey
",

 "controller"
:
 "
did:plc:fpruhuo22xkm5o7ttr2ktxdo
",

 "publicKeyMultibase"
:
 "
zQ3shopLMtAvvVrSsmWPE2pstFWY4xhGFBjkdRuETieUBozgo
"

 }

 ],

 "service"
:
 [

 {

 "id"
:
 "
#atproto_pds
",

 "type"
:
 "
AtprotoPersonalDataServer
",

 "serviceEndpoint"
:
 "
https://morel.us-east.host.bsky.network
"

 }

 ]

}

The DID Document itself works exactly the same way. It specifies:

* How to refer to me.ThealsoKnownAsfield confirms that whoever controlsdid:plc:fpruhuo22xkm5o7ttr2ktxdouses@danabra.movas a handle. ✅
* How to verify the integrity of my data.ThepublicKeyMultibasefield tells us the public key with which all changes to my data are signed.
* Where my data is stored.TheserviceEndpointfield tells us the actual server with my data. It’s currently athttps://morel.us-east.host.bsky.network.

Let’s visualize this:

did:plc:fpruhuo22xkm5o7ttr2ktxdomorel.us-east.host.bsky.network@danabra.movhandle (swappable)hosting (swappable)didserviceEndpointalsoKnownAs

Although my handle is@danabra.mov, the actual server storing my data is currentlyhttps://morel.us-east.host.bsky.network. I’m happy to keep hosting it there but I’m thinking of moving it to a host I control in the future. I can change both my handle and my hosting without disruption to my social apps.

Unlike Rudy, who has adid:webidentity, I stuck withdid:plc(which is the default one when you create an account on Bluesky) so that I’m not irrecovably tying myself to any web domain. “PLC” officially stands for a “Public Ledger of Credentials”—essentially, it is like an npm registry but for DID Documents. (Fun fact: originally PLC meant “placeholder” but they’ve decidedit’s a good tradeoff.)

The upside of adid:plcidentity is that I can’t lose my identity if I forget to renew a domain, or if something bad happens at the top level to my TLD.

The downside of adid:plcidentity is that whoever operates the PLC registry has some degree of control over my identity. They can’t outrightchangeit because every version is recursively signed with the hash of the previous version, every past version is queryable, and the hash of the initial versionisthe DID itself.

However, in theory, whoever operates the PLC registrycoulddeny my requests to update the DID Document, or refuse to serve some information about it. Bluesky is currently moving PLC toan independent legal entity in Switzerlandto address some of these concerns. The AT community is alsothinkingandexperimenting.

### From Hosting to JSON

So far, you’ve learned how to:

* Resolve a handle to a DID.
* Grab the DID Document for that DID.

That actually tells you enough to get the JSON by itsat://URI!

Each DID Document includes theserviceEndpointwhich is the actual hosting.That’sthe service you can hit by HTTPS to grab any JSON record it stores.

For example, the@ruuuuu.dehandle resolves todid:web:iam.ruuuuu.de, and its DID Document has aserviceEndpointpointing athttps://blacksky.app.

To get theat://ruuuuu.de/app.bsky.feed.post/3lzy2ji4nms2zrecord, hit thehttps://blacksky.appserver with thecom.atproto.repo.getRecordendpoint, passing different parts of theat://URI as parameters:

$
 curl
 "
https://blacksky.app/xrpc/com.atproto.repo.getRecord?
\

repo=ruuuuu.de&collection=app.bsky.feed.post&rkey=3lzy2ji4nms2z
"
 |
 jq

And there it is:

{

 "uri"
:
"
at://did:web:iam.ruuuuu.de/app.bsky.feed.post/3lzy2ji4nms2z
"
,

 "cid"
:
"
bafyreiae4ehmkk4rtajs5ncagjhrsv6rj3v6fggphlbpyfco4dzddp42nu
"
,

 "value"
: {

 "text"
:
"
posting from did:web, like a boss
"
,

 "$type"
:
"
app.bsky.feed.post
"
,

 "langs"
:
[

 "
en
"

 ]
,

 "createdAt"
:
"
2025-09-29T12:53:23.048Z
"

 }

}

Now let’s getat://danabra.mov/sh.tangled.feed.star/3m23ddgjpgn22:

* The@danabra.movhandle resolves todid:plc:fpruhuo22xkm5o7ttr2ktxdo.
* The DID Document fordid:plc:fpruhuo22xkm5o7ttr2ktxdopoints athttps://morel.us-east.host.bsky.networkas the current hosting.

Let’s hit it:

$
 curl
 "
https://morel.us-east.host.bsky.network/xrpc/com.atproto.repo.getRecord?
\

repo=danabra.mov&collection=sh.tangled.feed.star&rkey=3m23ddgjpgn22
"
 |
 jq

And there you have it:

{

 "uri"
:
"
at://did:plc:fpruhuo22xkm5o7ttr2ktxdo/sh.tangled.feed.star/3m23ddgjpgn22
"
,

 "cid"
:
"
bafyreiaghm4ep5eeqx6yf55z43ge65qswwis7aiwc67rt7ni54jj6pg6fa
"
,

 "value"
: {

 "$type"
:
"
sh.tangled.feed.star
"
,

 "subject"
:
"
at://did:plc:dzmqinfp7efnofbqg5npjmth/sh.tangled.repo/3m232u6xrq222
"
,

 "createdAt"
:
"
2025-09-30T20:09:02Z
"

 }

}

And that’s how you resolve anat://URI.

Exercise: In the record above, thesubjectis a link to another record. Figure out the handle of its owner and the contents of that record. Usepdslsto check your answer.

### In Conclusion

To resolve an arbitraryat://URI, you need to follow three steps:

1. Resolve the handle to an identity (using DNS and/or HTTPS).
2. Resolve that identity to a hosting (using the DID Document).
3. Request the JSON from that hosting (by hitting it withgetRecord).

If you’re building a client app or a small project, anSDKwill handle all of this for you. However, for good performance, you’ll want to hit a resolution cache instead of doing DNS/HTTPS lookups on every request.QuickDIDis one such cache. You can also check out thepdsls sourceto see how exactly it handles resolution.

In practice, a lot of apps don’t end up needing to resolveat://URIs or load JSON records because theyreceivedata from the networkvia a websocketand aggregate it in a local database. If that’s your approach, you’ll still use theat://URIs as unique identifiers for user-created data, but the data itself will get pushed to you rather than pulled by you. Still, it’s useful to know that youcanfetch it on demand.

The AT protocol is fundamentally an abstraction over HTTP, DNS, and JSON. But by standardizing how these pieces fit together—putting the user in the authority position, separating identity from hosting, and making data portable—it turns the web into a place whereyour content belongs to you, not to the apps that display it.

There’s more to explore in the atmosphere, but now you know where it’sat://.

Pay what you like
Hire me

Fork on Tangled

---
title: The test was green. Every real connection would have failed. - DEV Community
url: https://dev.to/yashksaini/the-test-was-green-every-real-connection-would-have-failed-3e37
site_name: devto
content_file: devto-the-test-was-green-every-real-connection-would-hav
fetched_at: '2026-08-22T11:19:23.750469'
original_url: https://dev.to/yashksaini/the-test-was-green-every-real-connection-would-have-failed-3e37
author: Yash Kumar Saini
date: '2026-08-20'
description: 'This is a submission for DEV''s Summer Bug Smash: Smash Stories powered by Sentry. The... Tagged with devchallenge, bugsmash, python, testing.'
tags: '#devchallenge, #bugsmash, #python, #testing'
---

Summer Bug Smash: Smash Stories 🐛🛹

This is a submission forDEV's Summer Bug Smash: Smash Storiespowered bySentry.

## The setting

WebRTC-Direct in libp2p has a neat trick for connecting without a certificate authority: the peer's multiaddrcontainsa hash of its TLS certificate —/webrtc-direct/certhash/<...>. When you dial, the DTLS handshake presents a cert, you hash it, and you check it against thecerthashin the address. No CA, no trust store — the addressisthe pin.

For that to work, py-libp2p has to make aiortc useourlibp2p-generated certificate, not the one aiortc auto-generates for itself. So the code pins it:

config
 
=
 
RTCConfiguration
(
certificates
=
[
rtc_cert
])

return
 
RTCPeerConnection
(
configuration
=
config
)

Enter fullscreen mode

Exit fullscreen mode

Clean. Obvious. And, as of aiortc ≥ 1.5, completely wrong — in two different ways.

## The first sign

The first way was loud: aiortc ≥ 1.5droppedcertificates=fromRTCConfiguration. Passing it raisesTypeError. Easy to spot, easy to "fix" — just move the cert onto the object after construction:

pc
 
=
 
RTCPeerConnection
(
configuration
=
config
)

pc
.
_certificates
 
=
 
[
rtc_cert
]
 
# looks right. isn't.

return
 
pc

Enter fullscreen mode

Exit fullscreen mode

The tests went green. The loopback echo test — open a data channel, send a payload, get it back — passed. I could have shipped it right there.

The quiet way is the one that would have burned every user.

## The investigation

Here's the thing that made this astoryand not a one-liner.pc._certificates = [...]is asilent no-op.aiortc never reads_certificates. Inside the class, it stores and reads the cert asself.__certificates— adouble-underscoreattribute. And Python does something specific with double-underscore names inside a class body: itmanglesthem.self.__certificatesinsideclass RTCPeerConnectionis compiled toself._RTCPeerConnection__certificates.

So from the outside:

* pc._certificates— a brand-new attribute I invented. aiortc reads it never.
* pc._RTCPeerConnection__certificates— theactualslot aiortc reads atcreateOffer/createAnswertime to write the SDPa=fingerprintline (seeaiortc/rtcpeerconnection.py:295and:1129).

I was setting the first one. aiortc was reading the second one — still holding its own auto-generated cert. The result:

* The/webrtc-direct/certhash/<...>multiaddr advertisedourlibp2p cert hash.
* The DTLS handshake usedaiortc'sauto-generated cert.
* Every real dial would fail peer verification withRemote DTLS fingerprint does not match certhash.

And the loopback echo teststill passed— because loopback doesn't validate the DTLS fingerprint against a multiaddr. It just opens a channel and echoes bytes. The one property that was broken was the one property the happy-path test never checked.

## The root cause

This is a bug that lives in the seam between two systems:

* Python's language rule:name mangling rewrites__namereferencesinside a class bodyso subclasses can't accidentally clobber a base class's "private" attributes. It's a language feature doing exactly what it's designed to do.
* aiortc's library internals:it stores the cert under__certificates, i.e. itrelieson that mangling for its own encapsulation.

Neither is wrong on its own. But when you reach into a library's private state from outside the class, the mangled name is theonlyname that works — and the un-mangled one you'd naturally type is a no-op that fails silently. There's noAttributeError, noTypeError, no warning. You just create a junk attribute and move on, and everything downstream keeps workingexcept the security property.

## The fix

Set the mangled attribute directly, after construction, before any SDP operation triggers the handshake:

config
 
=
 
RTCConfiguration
(
iceServers
=
list
(
ice_servers
)
 
if
 
ice_servers
 
else
 
[])

pc
 
=
 
RTCPeerConnection
(
configuration
=
config
)

# Replace aiortc's auto-generated cert. Must use the mangled name —
# aiortc reads only `self.__certificates`, which mangles to this.

pc
.
_RTCPeerConnection__certificates
 
=
 
[
rtc_cert
]
 
# type: ignore[attr-defined]

return
 
pc

Enter fullscreen mode

Exit fullscreen mode

It's an ugly line, and the docstring says so out loud — reaching into_RTCPeerConnection__certificatesis exactly the kind of private-state coupling that breaks on a library upgrade. But it'scorrect, and it'sannotatedso the next person knows why it can't just bepc._certificates.

## The canary that would have caught it

The real fix wasn't the one-liner — it was the test that makes the silent failure loud. The happy-path echo test can't see this bug, so I added one that asserts theinvariant: the pinned cert's fingerprint must actually appear in the SDP.

@pytest.mark.trio

async
 
def
 
test_cert_pinning_lands_in_sdp_fingerprint
()
 
->
 
None
:

 
"""

 Guards against a class of cert-pin bug: if the pin is a no-op (e.g.
 written to a public attribute aiortc never reads because it actually
 stores the cert under a name-mangled private slot), the SDP a=fingerprint
 line reflects aiortc
'
s auto-generated cert instead of ours.
 
"""

 
cert
 
=
 
WebRTCCertificate
.
from_aiortc
()

 
pc
 
=
 
await
 
bridge
.
run_coro
(
create_peer_connection
(
cert
.
_rtc_certificate
,
 
ice_servers
=
[]))

 
# Need at least one data channel for the SCTP m-line, otherwise

 
# createOffer omits the DTLS fingerprint entirely.

 
await
 
bridge
.
run_coro
(
_create_dummy_channel
(
pc
))

 
sdp
 
=
 
await
 
bridge
.
run_coro
(
_offer
())

 
expected
 
=
 
_sdp_fingerprint_string
(
cert
)

 
assert
 
expected
 
in
 
sdp
.
upper
(),
 
"
SDP fingerprint does not match pinned cert.
"

Enter fullscreen mode

Exit fullscreen mode

Note the small landmine inside the fix for thetest:createOfferomits the DTLS fingerprint entirely unless there's at least one SCTP m-line, so the canary has to create a dummy data channel first or it asserts against an empty offer. The bug had layers even in the reproduction.

Revert the mangled-name fix and this test goes red immediately with a fingerprint mismatch. Keep the oldpc._certificates = [...]no-op and it's red. That's the whole point: it failsclosed.

## What I learned

Two lessons, and they're the same lesson from two directions.

Test the invariant, not the happy path.The echo test proved bytes moved. It said nothing aboutwhich certificatemoved them — and that was the only thing that mattered for security. A green test is only as good as the property it asserts, and "it worked end to end" quietly excludes every property your end-to-end path doesn't check.

A silent no-op is worse than a crash.Ifpc._certificates = [...]had raised, I'd have fixed it in thirty seconds. Because itsucceeded— created a real attribute, threw no error — it sailed through review and tests and would have shipped a transport where every authenticated dial fails. When you reach across an encapsulation boundary into a library's private state, assume the language is doing something clever with the name, and write the test that proves your write actually landed where the library reads.

## Links

* Commit:ca8331ff— fix(webrtc): pin DTLS certificate via aiortc's mangled private slot
* Canary test:test_cert_pinning_lands_in_sdp_fingerprint
* Context:#546
* aiortc internals referenced:aiortc/rtcpeerconnection.py:295, 1129

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
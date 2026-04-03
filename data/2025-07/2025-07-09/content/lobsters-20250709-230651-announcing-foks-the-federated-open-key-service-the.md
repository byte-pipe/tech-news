---
title: Announcing FOKS, the Federated Open Key Service | The FOKS Blog
url: https://blog.foks.pub/posts/introducing/
site_name: lobsters
fetched_at: '2025-07-09T23:06:51.661722'
original_url: https://blog.foks.pub/posts/introducing/
date: '2025-07-09'
tags: cryptography
---

#### TL;DR: FOKS is like Keybase, but fully open-source and federated, with SSO and YubiKey support.

When welaunched Keybaseover 11 years ago,
we read a lot of good, well-informed feedback. We folded some
but not all of these suggestions into Keybase. Most important, you convinced us
that passwords are not a good long-term strategy for protecting
secret key material. As a result, we spent months ripping up the app and
pivoting toper-device keys,
which were clearly the right way to go. WhatsApp eventually caught up in 2023!

Among the best ideas that we lacked the bandwith to tackle were: federation,
open-source backend, YubiKey support and SSO support. No longer affiliated with
Keybase or Zoom (Keybase’s new owner), I’ve been thinking about how to resurrect
these very good ideas. Today, I’m happy to announceFOKS,
the Federated Open Key Service. The gist is “Keybase, but with federation, SSO
and YubiKey support, and fully open-source”. FOKS is not a fork, but rather
built from scratch in pure Go. FOKS inherits the general goal of
Keybase: give teams of users, each with multiple devices, shared secret keys so
they can share data securely across the internet. It inherits Keybase’s core
cryptographic techniques: append-only data structures that allow clients to catch
dishonest server behavior; and cascading key rotations on device revokes
and team member removals. The key difference is federation.

A user in FOKS is not a name in a shared, global namespace. Instead, much like
an email address, a user is auser@hostpair. Anyone can run a FOKS server
and control their own localized namespace, as in email. Teams in FOKS are like
mailing lists: they can contain users on just one server, or they can span
multiple servers; they can include other teams to form nearly-arbitrary DAGs.
Members of a team share symmetric cryptographic keys, with which they can share
files, chats, passwords, etc. See ourwhite
paperfor more details. Whether self-hosting or using a third-party provider, all
users get the benefit of FOKS’s cryptographic guarantees: that clients, not
servers, control key management, and that clients can identify and stop
malicious server behavior.

All the typical arguments for federation apply here: users can avoid vendor
lock-in, being “monetized”, the Hotel California syndrome, etc. But
federation becomes even more important in the sensitive applications that need
cryptography the most. Even if trafficking only end-to-end
encrypted data, the server still controls metadata like IP
addresses, team memberships, and usage patterns. These data can be leaked or
exposed in lawful discovery. FOKS, unlike centralized systems, allows for an
open market of service providers, and users can pick the one with the security,
privacy, availability and moderation policies that best suit them, or host their
own if none do.

Federation also provides more flexibility in terms of deployment: a FOKS server
can face the open internet or can reside within a private network. Self-hosted
FOKS servers can function as core infrastructure, without introducing new third-party
availability dependencies.

With FOKS, I’m psyched to release all software — both server and client —
under an MIT open-source license. Open-source everywhere is a key unlock
for security researchers trying to break the system, and community
contributors trying to improve it.

FOKS has been a personal passion project of mine, and as such, I don’t have a
team or funding. I hope to bootstrap an open-source community around the
project and then to see where it goes. At launch, I’m also running apaid
hosting provider, for those who want the “easy button”
rather than managing their own FOKS server. But time will tell if this is a
viable business. There certainly isn’t a “moat” to speak of, since anyone can
run such a provider, with the same open-source software thatfoks.appuses.

You canDownload FOKSorbuild it from
source. The system is fully-usable and
in beta, meaning there is a risk of data loss and security issues. FOKS
currently has device and team management, full YubiKey decryption and
signing via thePIV protocol, and SSO
via OAuth2. For applications, FOKS now has an end-to-end encrypted key-value
store and git hosting.
Oh, and encryption in FOKS is post-quantum secure. FOKS usesstandard ML-KEMfor key
encapsulation, in addition toboring old NaCl, so an
attacker needs break both systems to decrypt messages.

In the future, we hope to build mobile applications, file-sync, and an MLS-based
chat system. And I’m sure many other good ideas will come up along the way.
Scroll down for some demos.

✌️️Max🔑

Comments and discussion are welcome, please post to this link onHacker News.

 Easy setup of a FOKS server at keyz.fun


 Signup, showing a user joining keyz.fun and generating her first client key.


 YubiKeys act as full-featured keys; they're not just for authenticating to servers.


 FOKS's End-to-end encrypted key-value store. It can store short secrets like API keys,
 large documents, or anything in between. Works for both users and teams.


 FOKS also has an end-to-end encrypted git backend. Like the key-value store, it works for both users and teams.


#### Credits

Thanks toChris Coynefor reading drafts of this post
and valuable feedback on the entire project. Blog theme isHugo Xmin.

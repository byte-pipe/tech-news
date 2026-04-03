---
title: Bruteforcing the Bitwarden master password I forgor 💀
url: https://compilercrim.es/forgor/
site_name: lobsters
content_file: lobsters-bruteforcing-the-bitwarden-master-password-i-forgo
fetched_at: '2026-02-20T06:01:00.377089'
original_url: https://compilercrim.es/forgor/
date: '2026-02-20'
tags: cryptography, reversing
---

# Bruteforcing the Bitwarden master password I forgor 💀

February 13, 2026 · 9 minute read

The human mind is a fascinating thing. It's a miracle it works at all,
let alone how well it does. The corollary is that sometimes it doesn't,
I suppose.

I've been using Bitwarden for a few years now.1My life had vastly changed
a few times over, and yet the master password I've been using has stayed
the same. I've almost stopped thinking about it, letting muscle memory
handle it for me.

One day, quite tired, I tried to unlock it like always, and the muscle memory
trigger failed me. I just typed in an entirely different password. Just like that,
the act of unlocking my password manager became an action that's to be handled
by the conscious brain now. And I found that I can't fully remember the passphrase
in question. Much like magnetic core memory or DRAM, neural memory reads are
— apparently — destructive, and when they happen in out-of-spec conditions,
your data can — apparently — kinda accidentally disappear.2

It wasn't all too bad. I quickly managed to reconstruct most of the passphrase,
but one word had somehow escaped me. I was pretty sure of the initial letter
and the vague semantic meaning, but I couldn't recall the word itself.

I wasn't too nervous. Since I was stilllogged inon all my devices, and the
password vault was merelylocked, I could, at least in theory, easily do a local
bruteforce to bridge the gap.

The details were only a matter of some elbow grease and overcoming the procrastination.
At first I tried looking for people who've done a similar thing, but unfortunately
couldn't find any.3So, in case this is useful for someone else later,
I decided to document the process.

## The devil's in the details

Knowing that I generated the password withxkcdpass,4I found that
by default, theeff-longwordlistmust've been used, meaning 7776 options
for what the password could be. If I wanted to be fancy, I could try usingword2vecto sort the wordlist and incorporate the vague knowledge I still had
about the missing word, but that's very much not worth the effort when up
against mere 13 bits of entropy — even when key stretching is in your way.

The next step was to figure out where the Bitwarden client stores the data, and
how the relevant cryptography works. In my case, I was using the Firefox
browser extension — if you find yourself in a similar situation, but your setup
is different, then you're gonna have to be a bit more creative.

Since browser extensions are written in the typical combo of web technologies,
I deduced that there must be a way to open the browser dev tools in the context
of the extension.

However, looking for "open inspect element in context of web extension" is
kinda difficult. Search engines just seem to assume you're looking for some
extension for your browser that will "improve" your inspect element experience
in some way.5

But I managed to stumble through it and find it anyway. The relevant option is inabout:debugging:6

This lets you find all the necessary data:

* the e-mail for the account, which is being used as the salt
* thekdfConfig, which specifies what algorithm is being used to hash the password and its parameters
* themasterPassword_masterKeyHash, which allows verifying if you have the right password

I created a file,data.py, in which I collected the pieces:

masterKeyHash
=
"o<redacted>="

email
=
"bitwarden@compilercrim.es"

kdfType
=
0

iterations
=
600000

known
=
"known parts of the
%s
 passphrase"

Next came spelunking throughthe codeto find out how exactly the underlying
cryptography works. The relevant code entrypoint isverifyUserByMasterPasswordinuser-verification.service.ts. The computation has two parts:

* first, the password goes throughkey stretchingto derive themasterKey.
This is handled bymakeMasterKey. The underlyingderiveKeyFromPasswordcan use either PBKDF2 or Argon2id, depending on thekdfConfig.
* themasterKeyis then quickly hashed a further 2 iterations ofpbkdf2,
using the original password as a salt, and the result is compared with the storedmasterPassword_masterKeyHashto decide whether the password is actually correct.

All in all, this looks like a reasonably typical approach. The key stretching helps
slow down brute-force attacks, and after the master key is calculated, we derive
a hash to check if the password is correct, without having to do weird things like
trying to decrypt random stuff just to see if the resulting plaintext looks vaguely okay.

But, two iterations ofpbkdf2is quite a weird hash to use, don't you think? Why two?

## When the cryptographic spider sense is tingling

If you've taken a look at the code yourself, you'll have noticed thathashMasterKeychooses between one and two iterations depending on the circumstances:

* two iterations are used to derive themasterPassword_masterKeyHashwhich gets used
to check the password locally;
* on the other hand, one iteration is used to derive a hash that's used to authenticate
with the Bitwarden server.

The goal here is to achievedomain separation— you wouldn't want to be able to use
the locally-stored hash to authenticate with the server. On the other hand, going the other
way probably isn't useful, so something like this should be fine, right?

Well, as far as domain separation goes, this is quite a crude way of achieving it. Theiterationsparameter of PBKDF2 has not been designed for this, and the security of this approach depends on
the internals of PBKDF2.

For example, if you have the one-iteration and two-iteration hashes, does that let you check a password
guess without having to run the expensive key-stretching?

But you might say, "when would that even matter? in what situation do you have both hashes, but
not the password itself?"

Well, therecouldbe a threat model where this matters. Consider the following scenario:

* a state actor wants your passwords
* they gain access to the Bitwarden server and capture the server-side hash when you authenticate
(e.g. to sync the data with the server)
* then, they raid your home and grab your machines
* the vault happened to be locked, but the machines themselves were powered on, and so
they get the local hash as well.

Does this let them perform the brute-force 600k times faster? Having stared at the
definition of PBKDF2 for a while, I determined that effectively, we get the following
relationship between the data:

HMAC(masterKey, serverHash)
^
serverHash
==
localHash

So, if you have a guess for what themasterKeycould be, you can check it quickly.
But that's pretty useless — you pretty much have no hope of guessing themasterKey,
other than by brute-forcing the password itself.

What saved the day here is that Bitwarden chose to compute the derived hashes
by invokingPBKDF2(password: masterKey, salt: userPassword, iterations). Had they chosen
to write it asPBKDF2(password: userPassword, salt: masterKey, iterations), we'd have
a cute little cryptographic backdoor... of an impact that, admittedly, depends on your
threat model.

TL;DR: Please don't use theiterationsparameter of your KDF to achieve domain separation.
That's basically the cryptographic equivalent of playing with fire, and you only get to do that
if you're setting a CTF challenge.

Don't stress out your pet cryptographers.

## Back to the realm of the living

Having managed to climb out of the rabbit hole that once again swallowed me whole
the moment I briefly let my guard down, I whipped up a quick Python script
to actually do the thing I wanted to do in the first place, and brute force the
part of the password I had forgotten:

from
data
import
*

from
base64
import
*

from
hashlib
import
pbkdf2_hmac

from
xkcdpass
import
xkcd_password

wordfile
=
xkcd_password.locate_wordfile()

with
open
(wordfile)
as
f:

 wordlist
=
list
(
map
(
str
.strip, f))

assert
kdfType
==
0
# PBKDF2_SHA256

salt
=
email.encode()

keyhash
=
b64decode(masterKeyHash)

for
i, guess
in
enumerate
(wordlist):


if
i
%
10
==
0
:
print
(
'#'
, i)

 password
=
(known
%
guess).encode()

 masterKey
=
pbkdf2_hmac(
'sha256'
, password, salt, iterations)

 masterKeyHash
=
pbkdf2_hmac(
'sha256'
, masterKey, password,
2
)


if
masterKeyHash
==
keyhash:


print
(guess)


break

I mentally prepared myself for it to fail the first couple times, since that's always how it is
when you're dealing with cryptography. Debugging that is alwaysfun.

This time though, it worked perfectly, first try.

I looked at the output, which told me what the missing word was.

"Oh, of course. How did I ever forgetthatin the first place?"

Proof-read bydmi. Thanks! :3

# Hope you enjoyed this!

You might like some ofmy other posts, too. If you'd like to be notified
 of new ones, you canfollow me on the Fediverseor subscribe to theRSS feed.

Also, I'd like to thankmy GitHub sponsorsfor their support:
 Michalina Sidor, Tijn Kersjes, LunNova and Anders Murphy.

1

through Vaultwarden hosted by mywonderful friends, of course

2

i'm really not beating therobogirl allegations, am i?

3

not sure if it's because no one had actually done this before,
or if it's another example of search being dead, having been consumed by
adtech companies and the AI bubble.

4

hey, it's in the Arch repos, so it's probably not completely
random untested software, right??

5

Have you ever wanted to save the changes you make to a website
with "inspect element", so that they are still there when you load the page
again? Not really? Well, as it turns out, with a random addon rated a
staggering 2.5 stars, you can! Download now!!

6

this is also where the remote debugging feature is: open
a website on your phone, and use the Firefox developer tools on yourdesktopto poke at it. how cool is that? :3

 This is where the comments would load if you enabled JavaScript.

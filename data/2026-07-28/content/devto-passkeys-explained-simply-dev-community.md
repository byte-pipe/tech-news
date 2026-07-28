---
title: Passkeys Explained Simply - DEV Community
url: https://dev.to/thomasbnt/passkeys-explained-simply-52jk
site_name: devto
content_file: devto-passkeys-explained-simply-dev-community
fetched_at: '2026-07-28T11:43:15.300603'
original_url: https://dev.to/thomasbnt/passkeys-explained-simply-52jk
author: Thomas Bnt
date: '2026-07-27'
description: You’ve probably seen that little prompt that says “Sign in with Face ID” or “Use a passkey” instead... Tagged with security, api, webdev, discuss.
tags: '#discuss, #security, #api, #webdev'
---

Comments warn account recovery is the weak link

You’ve probably seen that little prompt that says “Sign in with Face ID” or “Use a passkey” instead of the traditional password field. That’s a passkey. And no, it’s not just a password hidden behind your fingerprint.

The best password is the one you never have to type.

## The Problem with Passwords

A password is a secret thatyouhave to remember, and that thewebsitehas to store (ideally hashed). The problem is that this system relies entirely on two weak points:

* You, who reuse the same password everywhere because you’re tired of coming up with a new one.
* The website, which can be hacked and have its password database leaked.

Add phishing to that: a fake website that perfectly mimics the real one can steal your password without you even realizing it. And this isn’t just a minor issue: as theVerizon DBIR reportreminds us every year, social engineering, phishing, and stolen credentials remain among the leading causes of hacking worldwide, alongside software vulnerabilities.

Source:Data Breach Investigations Report, Verizon

Even with a password manager and 2FA, the fundamental vulnerability remains: a secret that you could accidentally share.

## What exactly is a passkey?

A passkey is based onasymmetric cryptography, the same principle as SSH, if you've ever generated a key pair to connect to a server.

When you create a passkey for a website:

1. Your device (phone, computer, security token) generates akey pair: a private key and a public key.
2. The private keyneverleaves your device. It is stored in a secure chip: theSecure Enclaveon iPhone/Mac, theTPMon Windows, or directly on the chip of a USB key such as aYubiKey.
3. The public key, on the other hand, is sent to the website and stored on the server.

To log in, the site sends you a challenge (a random number), your device signs it with the private key, and the site verifies the signature using the public key. If they match, you're authenticated.

No secrets ever travel over the network only a signature. It’s written in black and white in theW3C WebAuthn spec: nothing to steal, nothing to phish.

## Why It’s More Secure

Password

Passkey

Shared secret, transmitted with every login

Nothing is transmitted, just a signature

Reusable across multiple sites

Unique per site, tied to the domain

Vulnerable to phishing

Resistant to phishing (tied to the exact domain)

Can be leaked in the event of a server breach

The server stores only the public key, which is useless to an attacker

Must be memorized or managed via a manager

Unlocked via biometrics or a local code

The key point: a passkey islinked to the domainon which it was created. If you go topaypa1.cominstead ofpaypal.com, your device won't even offer the passkey. It's the browser/OS that performs this verification, not you. Googleexplains it very well: unlike a password, a passkey is cryptographically bound to the site for which it was created, so it’s impossible to intercept or reuse on a fake site. They’re resistant to phishing by design, not because of the user’s good faith.

## Under the Hood: WebAuthn and FIDO2

Technically, passkeys are based on theWebAuthn(W3C) standard, which is part of the broaderFIDO2standard promoted by the FIDO Alliance (whose members include Google, Apple, Microsoft, and Yubico). It is this API that browsers expose via JavaScript to create and use credentials.

Diagram of the registration flow, based on theW3C WebAuthn spec

Creating a client-side passkey looks like this:

const
 
credential
 
=
 
await
 
navigator
.
credentials
.
create
({

 
publicKey
:
 
{

 
challenge
:
 
new
 
Uint8Array
(
32
),
 
// provided by the server

 
rp
:
 
{
 
name
:
 
"
My Super Site
"
,
 
id
:
 
"
mysupersite.com
"
 
},

 
user
:
 
{

 
id
:
 
new
 
Uint8Array
(
16
),

 
name
:
 
"
thomas@example.com
"
,

 
displayName
:
 
"
Thomas
"
,

 
},

 
pubKeyCredParams
:
 
[{
 
alg
:
 
-
7
,
 
type
:
 
"
public-key
"
 
}],
 
// ES256

 
authenticatorSelection
:
 
{
 
userVerification
:
 
"
required
"
 
},

 
},

});

Enter fullscreen mode

Exit fullscreen mode

And to log in with an existing passkey:

const
 
assertion
 
=
 
await
 
navigator
.
credentials
.
get
({

 
publicKey
:
 
{

 
challenge
:
 
new
 
Uint8Array
(
32
),
 
// provided by the server

 
userVerification
:
 
"
required
"
,

 
},

});

Enter fullscreen mode

Exit fullscreen mode

The server generates thechallenge, the browser handles all the biometrics and unlocking, and sends you back a signature to verify. On the server side, libraries like@simplewebauthn/serverin Node.js do most of the verification work.

## What if I lose my phone?

This is the question that stumps everyone, and if this topic resonates with you, I’ve already written an entire article on thehassles of 2FA after a phone theft, the same “single point of failure” principle applies to passkeys. Since 2022, Apple, Google, and Microsoft have addedpasskey synchronization:

* On iOS/macOS, they sync via youriCloud Keychain.
* On Android/Chrome, they sync via yourGoogle Account, using Google Password Manager, which encrypts everything end-to-end.
* On Windows, viaWindows Hello, although cross-device synchronization is even more limited there than with Apple or Google.

So if you lose your phone but regain access to your iCloud or Google account on a new device, your passkeys will be restored as well. You can also use aphysical security key (YubiKey)as a backup, which doesn’t sync but works on any compatible device exactly the same advice as for traditional 2FA: never put all your eggs in one basket.

## How to Use Them Today

More and more services already offer them: Google, Apple, GitHub, Microsoft, PayPal, Amazon, X... Google has even gone a step further by makingpasskeys the default for personal accounts. You’ll usually find them in your account’s security settings, under “Access Key” or “Passkey.”

The typical workflow:

1. Go to the service's security settings.
2. Click “Add an access key” or “Create a passkey.”
3. Your browser or operating system will ask you to confirm using Face ID, Touch ID, Windows Hello, or your phone's passcode.
4. That's it. The next time you log in, you won't need a password.

If you want to manage your passkeys somewhere other than your OS’s keychain (useful if you’re on multiple different platforms),ProtonPasscan also create and store them—end-to-end encrypted—in the same place as your passwords.

## Conclusion

Question

Answer

What is it based on?

Asymmetric cryptography (private/public key pair)

Does the password travel over the network?

No, never

Resistant to phishing?

Yes, by design (domain-bound)

Technical standard

WebAuthn / FIDO2

Device loss

Recoverable via iCloud/Google sync, or physical backup key

Passkeys aren't just “a password hidden behind a fingerprint”, they represent a complete shift in the model: nothing to remember, nothing to steal. If a service offers you the option to create one, go for it it's significantly more secure and faster than your current password.

The ProtonPass link in this article is an affiliate link, which means I may receive a commission if you decide to sign up through this link, at no additional cost to you. This helps me cover hosting and domain name fees. Thank you for your support!

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments have been hidden by the post's author -find out more

For further actions, you may consider blocking this person and/orreporting abuse
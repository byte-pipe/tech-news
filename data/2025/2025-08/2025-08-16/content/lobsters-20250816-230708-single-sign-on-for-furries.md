---
title: Single Sign On for Furries
url: https://cendyne.dev/posts/2025-08-15-single-sign-on-for-furries.html
site_name: lobsters
fetched_at: '2025-08-16T23:07:08.132704'
original_url: https://cendyne.dev/posts/2025-08-15-single-sign-on-for-furries.html
date: '2025-08-16'
description: Single Sign On scales headcount and maintains security under a single credential. Services unfairly price for SSO, so I made my own for a furry convention.
tags: security
---

# Single Sign On for Furries

Published Yesterday
 - 19 min read -
Text Only
Table of contents
* Single Sign On for Furries
* So I built my own
* An Open Source SSO

If I were to bootstrap a furry convention today for its first year, without writing any code, I'd probably start with a square store to handle both online and in person transactions, a custom domain, a social media account, and an email address for any business communications. Check in for pre-registrations will be clunky, but for a 100-300 attendance event, it should be feasible.

Disclosure: I have no personal experience with Square. I know people that work there and it works well enough for physical goods and digital services for furries.

There's more, like a bank account, but in scope of the staff that make the event happen, only a few services are needed before and during the event: the store, social media, and email. Three shared credentials (not good, not great) among five to ten people will go a long way for the first year.

Future years will be different. Once a convention needs staff to specialize in responsibilities to pull the event off, this bootstrap model won't scale. Attendees want to run their own meetups or panels on the schedule, like talking about trains and public transportation. Managing this by email would be possible, but a hassle. Where will it go? A spreadsheet? You'll need Google Suite to collaborate, or at worst it's on someone's personal machine to be printed on papers on-site.

Shadow-ITwill be the norm while the convention's technology team is under-developed or under-powered. The art team might useTrellowhile operations uses a spreadsheet on a personal google account, which is shared from personal account to personal account. Personally-Identifying-Information (PII) may be collected and forgotten for years in staffs and ex-staff's google drives for years because of this. Working and collaborating will get increasingly messy and frustrating as access, visibility, and appropriate preservation and destruction are not tied to the organization.

And so, as the convention gets more serious and capable in running the event, the breadth of services and systems grow. The same could be said for any small business too.

By the point the total staff headcount exceeds a hundred people, something has to change. Most staff can only handle one credential. Even though password managers and passkeys are now more accessible and integrated, enough don't use them to make it a risk to add more credentials.

We need single sign on to scale headcount, to improve visibility, to improve access and to improve security.

Except, SSO can be expensive.

Non profits with a once a year income stream do not have the funds to support this kind of cost for a hundred plus unpaid staff.

An Okta employee informs me that they offer
50 free licenses
 and 50% off additional licenses.
It takes more than 50 people to run a convention (with > 1000 people) on-site. I expect around 50 people contribute before the event, so Okta might be a solution if Okta is okay with turning off licenses for 10 months of the year.

There are alternatives.AWS Identity Centeris a free service that supportsexternal applicationswith SAML.It alsosupports external identity providers, meaning staff can authenticate outside of AWS Identity Center.

Instructions exist for
OAuth 2.0
 / OIDC applications, but it doesn't look like AWS Identity Center is authoring the identity assertion, which is what you'd be wanting. It works for SAML, though.
Every identity provider will do it differently. AWS Identity Center
interpolates attributes
 while Google has a dropdown for attribute values.

Alternativelyfor non-profits, Google Workspace is freeand supportsexternal SAML applicationsas well and comes included with Google workspace.It also supports external identity providers.

But, any custom application in Google is shoved all the way down to the bottom below their other 100 (to be rebranded
or canceled
) products. And they don't support listing external OIDC applications.

Assuming either of these solutions work for your convention, the next issue is pricing for the service provider.

Services like Atlassian for issue tracking or service desk are 🤑 expensive 🤑 (~$20 per person per month).

They're even more so when an external identity provider signs in users (add $8 per person per month).

The same is true for any plugins for open platforms likeWordpressand AGPL software likePlanetoo.

Tally this up and you may be spending at least $40 a month for volunteers that are inactive fifty weeks of the year. No furry convention organization out there has the finances to spend an extra venue-worth of fees ($24,000 at least) on services.

… why … so much?
Business customers that
want
 single sign on
AND
 have staff that can apply it also have the money to write off the security tax.
Furry conventions
are not
 sound or reliable businesses with year-round revenue. Many are non-profits and some, like FurSquared, are also registered charities.
Microsoft rant

Microsoft got flackfor charging for security logs to detect breaches. (archived)

U.S. Senator Ron Wyden said Microsoft should offer all its customers full forensic capabilities, saying that "charging people for premium features necessary to not get hacked is like selling a car and then charging extra for seatbelts and airbags." -
Microsoft under fire after hacks of US State and Commerce departments by Reuters
 (
archived
)

Because of the bad publicity reached the US Congress,Microsoft changed their policy to make these logs free(archived). Even so,Microsoft has had a poor track record in their own house with their own tools(archived), so some in the industry doubt their security products are worth it.

Unfortunately, one website namedsso.taxis not enough to make the multitude of vendors change their ways to improve the baseline security for the world's benefit.

If the cost of having single sign on for every service is about $5 or more per service per seat, what alternative is there to avoid this fee?

Social Sign Inis a fantastic backup where integrating with an Identity Provider is cost prohibitive — as long as the social provider is tied to your identities managed by the organization, like Google or Microsoft.

Open Core platforms likeFreeScout(shared inbox email management)charges $8 USD for a pluginthat authenticates withSign in with Google. However, as a one-time cost, it is far easier to justify than a per seat per month subscription.

Google workspace makes for a compelling identity provider when it serves both external integrated applications and social sign in.

Creating and managing credentials for staff is cumbersome beyond ten people, especially when self-registration is disabled. You wouldn't want anyone to just create an account in the ticket system where they'll stumble across PII, right?

As you search for solutions to meet the needs of your organization, be it ticket tracking or shared email access, consider upfront what options you have to avoid passwords at all costs for the least monetary cost.

Tailscale
won't even take passwords
. A neat business strategy that I approve of.

## So I built my own

Naturally, I built my own SSO.

Line art by
Egypt Urnash
. Coloring by me. Featuring
Opnionated Guides
,
Xe Iaso
,
ThePhdD
,
Ibzan
,
Miunau
,
Soatok
, and
Dangered Wolf
.
why would you do that!?

I concluded that any option, paid or free, would not assist in one of the most annoying internal issues: getting our own staff registered for the convention and otherwise directing them to the resources and tools that staff and directors need to perform their duties.

For example, where's the login URL on our Wordpress website? Will the lay-person remember to add/wp-login.phpto the end of the URL so they could update the policy tied to their event function? No. The same is true for the other services. Sometimes it is/adminor the hostname is forgettable likeinternal-passwords.domain.com.

It started as an advancedLinktreegated behind Sign in with Google and would query our registration system for a pending invite or a completed registration upfront.

It then grew to manage our own google workspace by importing, updating, suspending, or even creating new profiles in our Google Workspace. Then I worked to create short lived assertions that instantiate a session on internal services, and finally created plugins for WordPress and FreeScout to accept and auto-provision (limited) users in their identity pools.

The scope grew and now it supports OIDC and OAuth clients, which allows me to even offer the tech team access to our AWS account console without any shared credentials, or hopping through AWS Identity center.

Sounds interesting, will you write about that soon?
Indeed! Very soon… For now, suffice it to say that AWS trusts my OpenID Connect configuration and will accept IdTokens signed by the keyset linked to by the configuration.
What about
SAML
?
Later… I'm figuring that out on my own time. Universally, it all hinges on RSA 2048 SHA-256 signatures (sometimes SHA-1), and that depresses me.
Other algorithms like Ed25519 technically could work, though service providers reduce their vulnerability surface by offering less configuration. This is a good thing! I just wish it weren't bound to RSA.

With nearly every application in use – besides a few SaaS likeCanvaorStripe– now accessible through a single sign on portal, we hardly need to share credentials in a password manager for services or team accounts.

Shared credentials come with a lot of trouble. What if someone leaves or is forced to leave? What if someone struggles with technology and doesn't realize that binding their phone number to the account for SMS OTPs locks everyone else out the next time they need to get in?

The world needs less passwords.Passkeys are desirable when there's no other alternative, but when federated identity is possible, it should be embraced, and it should be free.

But
acerola
 Cendyne, I thought federated identity is like putting all your eggs in one basket and that's bad?

Federated identity moves the responsibility for managing the credential over time away from the individual contributor (whether paid or volunteered) to a policy that aligns with the security posture of those managing access (i.e. me and Shripe) on behalf of the organization (FurSquared).

We can say that all users must have 2FA and valid 2FA methods are: passkeys (including standalone WebAuthn), TOTP, app-confirmation, or (sigh) SMS OTP. Some Identity providers allow for applying different policies to different groups. For example, anyone with access to the Cardholder Data Environment may only verify a second factor that is a hardware-key.

These policies can be strong, can require short-lived sessions, or even re-prompt as necessary for 2FA for sensitive events.

A short rant

Unfortunately, some IdPs implement 2FA methods so terribly that users must use a dropdown to match to the specific authenticator, be it an iCloud passkey or a Yubikey, instead of asking for all at once when using WebAuthn.

My SSO delegates credential storage, credential verification, and 2FA verification to Google Workspace, while it otherwise manages the user pool within Google Workspace.

How it manages users is another interesting journey worth a blog post.

Where possible, I will be pushing centralized and federated sign-in as far as possible to support the staff at FurSquared.

After implementing single sign on from the ground up, I am wholly sold on eliminating individualand sharedcredentials from everyone's lives. Single Sign On is how it's done – if only there wasn't such a heavy tax.

While my invention won't be public, if you need an SSO solution with custom SAML and OIDC applications, I think AWS Identity Center is the best free option to work with. You canintegrate AWS Identity Center with Google Workspacefor free as a non-profit.

As for building your own set of useful links that are not SAML applications, I think a pinned message in telegram or discord or whatever will get you a long way. As long as your budget is approximately $0.

## An Open Source SSO

If you're up for hosting your own infrastructure 24/7, there are options out there. Some recommendAuthentik, though unless youpay $5 USD / month, it won't have a Google Workspace integration.

Sinceit requires 2GB of RAMto run, you'll need to budget for around $120-150 USD per year to run Authentik on a VPS host. If you divide the cost by the amount of people, it'll be around $1.50 per staff member. I'd say, that's worth it! But, do you or your team have the skillset and time to run your own infrastructure? And can it live on when you retire?

For that reason, I'm building such an essential tool on Cloudflare workers. On that platform, infrastructure is a light burden and costs are near zero for years to come.

---
title: My Next.js 16 Auth Passed Every Test. Five Bugs That Only Showed Up When I Wired It Together. - DEV Community
url: https://dev.to/shubhradev/my-nextjs-16-auth-passed-every-test-five-bugs-that-only-showed-up-when-i-wired-it-together-bgh
site_name: devto
content_file: devto-my-nextjs-16-auth-passed-every-test-five-bugs-that
fetched_at: '2026-07-06T12:20:24.971709'
original_url: https://dev.to/shubhradev/my-nextjs-16-auth-passed-every-test-five-bugs-that-only-showed-up-when-i-wired-it-together-bgh
author: Shubhra Pokhariya
date: '2026-06-30'
description: The three-layer model works. Part 1 of this series is the invoice incident that proved it. Part 2 is... Tagged with nextjs, security, webdev, javascript.
tags: '#nextjs, #security, #webdev, #javascript'
---

Route Handler and browser cookie quirks

The three-layer model works. Part 1 of this series is the invoice incident that proved it. Part 2 is the proxy.ts matcher gaps that fail silently. Part 3 is the mutation-layer auth check that gets skipped even when everything else looks solid. My kit implements this in Route Handlers rather than Server Actions, but the principle is identical: every mutation endpoint verifies the caller before touching data.

I built all three layers correctly. Then I tried to ship a complete auth kit on top of them.

Email and password login. Google and GitHub OAuth. Email verification. Password reset. Role-based routes. An admin panel with live database stats. A UI a real person would trust with a real password.

That is when the integration bugs appeared. Not architecture bugs. Wiring bugs. The kind that only exist once every piece is connected and real flows run through the whole thing.

Five of them. Here is exactly what happened.

## Bug 1: The Cookie Write That Reported Success and Then Vanished

Login returned 200. Tokens in the response. Client wrote the cookie. The very next request redirected straight back to login.

I went to the JWT first. The JWT was fine. The proxy was fine. The cookie was simply not there on the next request.

Here is what was actually happening. After a successful login call, the client was writing the cookie withdocument.cookie = .... In certain browser and timing combinations on localhost, that write reported success.document.cookie.includes('auth_tokens')returnedtrueimmediately after the assignment. Then a few seconds later, gone. No error. No warning.

The fix was not about the timing. It was moving the write to where it belonged from the start.

// app/api/auth/login/route.ts

const
 
COOKIE_NAME
 
=
 
process
.
env
.
NEXT_PUBLIC_AUTH_COOKIE_NAME
 
??
 
"
auth_tokens
"
;

// ... after building responseBody and cookieTokens ...

const
 
response
 
=
 
NextResponse
.
json
(
responseBody
,
 
{
 
status
:
 
200
 
});

const
 
isSecure
 
=

 
request
.
headers
.
get
(
"
x-forwarded-proto
"
)
 
===
 
"
https
"
 
||

 
request
.
nextUrl
.
protocol
 
===
 
"
https:
"
;

const
 
maxAge
 
=
 
rememberMe
 
===
 
true
 
?
 
60
 
*
 
60
 
*
 
24
 
*
 
30
 
:
 
60
 
*
 
60
 
*
 
24
 
*
 
7
;

response
.
cookies
.
set
(
COOKIE_NAME
,
 
JSON
.
stringify
(
cookieTokens
),
 
{

 
httpOnly
:
 
true
,

 
sameSite
:
 
"
lax
"
,

 
secure
:
 
isSecure
,

 
path
:
 
"
/
"
,

 
maxAge
,

});

return
 
response
;

Enter fullscreen mode

Exit fullscreen mode

httpOnly: truemeans no JavaScript on the page can read this cookie at all. A script injected through an XSS vulnerability still cannot steal the session token because the token is invisible to every script. The browser stores it automatically from theSet-Cookieresponse header. Nothing to silently vanish.

As Part 1 covered, the proxy reads the session from a cookie, notlocalStorage.httpOnlycloses both issues at once: the proxy can see the cookie, and client-side scripts cannot touch it.

If the client is writing something the server should write, stop debugging the client write. Move it.

## Bug 2: The Navigation That Never Reached the Proxy

Cookie fixed, server-set, httpOnly. Still redirecting back to login.

After the login API returned 200, the form calledwindow.location.href. But before I landed on that fix I had triedrouter.push(redirectTo)first. That is where the second bug was hiding.

router.pushis a client-side navigation. No real HTTP request fires. The browser has no reason to attach the newly set cookie to anything outgoing because nothing crossed the network.proxy.tsonly sees real HTTP requests. A route change that stays inside React's router is invisible to it. This is the same boundary Part 2 covered when explaining why matcher gaps are invisible at the proxy level: the proxy cannot check what it never sees.

The login form useswindow.location.hreffor exactly this reason:

// app/login/login-form.tsx

async
 
function
 
handleSubmit
(
e
:
 
FormEvent
<
HTMLFormElement
>
):
 
Promise
<
void
>
 
{

 
e
.
preventDefault
();

 
setError
(
null
);

 
setIsSubmitting
(
true
);

 
try
 
{

 
await
 
login
(
email
.
trim
(),
 
password
,
 
rememberMe
);

 
window
.
location
.
href
 
=
 
redirectTo
;
 
// real HTTP GET, proxy sees the cookie

 
}
 
catch 
(
err
)
 
{

 
// ... error handling

 
setIsSubmitting
(
false
);

 
}

}

Enter fullscreen mode

Exit fullscreen mode

window.location.hrefforces a full page reload. A genuine HTTP GET. The browser attaches every cookie it holds. The proxy sees it because this request actually crossed the network.

## Bug 3: A Database Integer in the JWT Sub Claim

Cookie arriving correctly. Proxy still rejecting the token.

Debug logging showed the JWT decoding fine. Every claim present. The type guard inextractPayloadkept failing onsub.typeof sub !== 'string'kept returningtrueeven though the value looked like a user ID.

The databaseidcolumn isSERIAL, a Postgres integer. When that integer got passed intojose's.setSubject()without an explicit cast, it was serialized into the token as a number. TheextractPayloadfunction checkstypeof sub !== "string"and throws if that fails. It was doing exactly what it should. The claim was wrong because of an upstream assumption that never held for an integer primary key.

The fix is inlib/auth/jwt.tson bothsignAccessTokenandsignRefreshToken:

// lib/auth/jwt.ts

export
 
async
 
function
 
signAccessToken
(

 
payload
:
 
SignablePayload
,

):
 
Promise
<
string
>
 
{

 
return 
(

 
new
 
SignJWT
({

 
role
:
 
payload
.
role
,

 
email
:
 
payload
.
email
,

 
permissions
:
 
payload
.
permissions
,

 
})

 
.
setProtectedHeader
({
 
alg
:
 
"
HS256
"
 
})

 
// Always cast to string here. Postgres ids that come through as

 
// numbers will otherwise get signed as numbers, and proxy.ts expects

 
// sub to always be a string when it verifies the token.

 
.
setSubject
(
String
(
payload
.
sub
))

 
.
setIssuedAt
()

 
.
setExpirationTime
(
ACCESS_TOKEN_TTL
)

 
.
sign
(
ACCESS_SECRET
)

 
);

}

Enter fullscreen mode

Exit fullscreen mode

String(payload.sub)on bothsignAccessTokenandsignRefreshToken. One word. TheextractPayloadtype guard that catches this is correct. The claim was malformed, just not visibly, because a number and a number-as-string look identical in a console log.

This bug is invisible in development if test data uses string IDs. It only surfaces when a realSERIALcolumn meets a JWT library that validates claim types strictly.

## Bug 4: OAuth Sign-In When the Same Email Already Has a Password Account

Email and password auth working end to end. Time to add Google and GitHub.

The OAuth flow itself is documented well enough. The question that actually needed answering: what happens when someone who already has a password account later clicks "Continue with Google" using the same email address?

The callback route handles three distinct cases:

// app/api/auth/google/callback/route.ts

// Case 1: they've signed in with Google before, google_id already set

let
 
user
 
=
 
await
 
db
.
queryOne
<
UserRow
>
(

 
`SELECT id, email, name, role, is_active, google_id
 FROM authkit_test_users
 WHERE google_id = $1`
,

 
[
googleUser
.
sub
],

);

if 
(
!
user
)
 
{

 
// Case 2: no google_id match, but email matches an existing row

 
const
 
existingByEmail
 
=
 
await
 
db
.
queryOne
<
UserRow
>
(

 
`SELECT id, email, name, role, is_active, google_id
 FROM authkit_test_users
 WHERE email = $1`
,

 
[
normalizedEmail
],

 
);

 
if 
(
existingByEmail
)
 
{

 
// Linking is safe here because Google has already verified this

 
// email belongs to whoever is sitting at the browser right now.

 
// email_verified gets set true at the same time, in case they

 
// registered with a password earlier and never finished clicking

 
// their own verification link.

 
await
 
db
.
query
(

 
`UPDATE authkit_test_users
 SET google_id = $1, email_verified = true
 WHERE id = $2`
,

 
[
googleUser
.
sub
,
 
existingByEmail
.
id
],

 
);

 
user
 
=
 
existingByEmail
;

 
}
 
else
 
{

 
// Case 3: brand new person, create the row

 
// password_hash stays null, role always defaults to 'user'

 
const
 
rows
 
=
 
await
 
db
.
query
<
UserRow
>
(

 
`INSERT INTO authkit_test_users
 (email, password_hash, name, role, is_active, email_verified, google_id)
 VALUES ($1, NULL, $2, 'user', true, true, $3)
 RETURNING id, email, name, role, is_active, google_id`
,

 
[
normalizedEmail
,
 
googleUser
.
name
 
??
 
null
,
 
googleUser
.
sub
],

 
);

 
user
 
=
 
rows
[
0
]
 
??
 
null
;

 
}

}

Enter fullscreen mode

Exit fullscreen mode

The linking in Case 2 is safe specifically because of who verified the email. Google has already confirmed this email belongs to whoever is sitting at the browser. That is a stronger guarantee than most apps' own verification flow. The unsafe version of this pattern is linking accounts based on an email someone simply typed into a field with no third-party verification behind it.

Role always defaults to'user'on new accounts. There is no code path a visitor can trigger that grants admin through a sign-in button.

GitHub needed one extra step Google does not. Google always returns a verified email with the basic profile request. GitHub does not. Many users set their email to private, so the profile response comes back withemail: null. The fix is a second request to GitHub's emails endpoint, filtering for the address marked both primary and verified. No verified primary email means the account cannot sign in this way.

Both providers on the same sign-in screen. The three-case account lookup in Bug 4 is what makes this safe when the same email already exists from a password registration.

## Bug 5: Forgot Password for an Account That Never Had a Password

This one does not show up until you have built both OAuth and email/password auth and put them in the same product.

A user registers with Google. Months later they land on the forgot password page and type in their email, because they have genuinely forgotten they always came in through the Google button and never set a password.

Without handling this, that person gets a password reset email for a password that has never existed. The link technically works. The experience makes no sense and they leave more confused than before.

Thepassword_hashcolumn staysnullfor every OAuth-only account. That is the check:

// app/api/auth/forgot-password/route.ts

if 
(
!
user
.
password_hash
)
 
{

 
// This account signed in through an OAuth provider and never set a

 
// password. Send a message pointing at whichever one they actually

 
// used rather than sending a reset link for a password that doesn't exist.

 
const
 
provider
 
=
 
user
.
google_id

 
?
 
"
Google
"

 
:
 
user
.
github_id

 
?
 
"
GitHub
"

 
:
 
"
Google or GitHub
"
;

 
try
 
{

 
await
 
resend
.
emails
.
send
({

 
from
:
 
process
.
env
.
RESEND_FROM_EMAIL
 
??
 
"
noreply@example.com
"
,

 
to
:
 
normalizedEmail
,

 
subject
:
 
`Sign in with 
${
provider
}
`
,

 
html
:
 
buildOAuthOnlyEmail
({
 
name
:
 
user
.
name
,
 
provider
 
}),

 
});

 
}
 
catch
 
{

 
// Email failed to send, the generic response goes out either way

 
}

 
return
 
NextResponse
.
json
(
genericSuccessBody
,
 
{
 
status
:
 
200
 
});

}

Enter fullscreen mode

Exit fullscreen mode

ThebuildOAuthOnlyEmailfunction is in the same file. It generates a plain HTML email that tells the person their account was created with that provider and links them back to the sign-in page. No password reset link. No confusion.

The browser response is identical regardless of which branch runs:

const
 
genericSuccessBody
 
=
 
{

 
message
:

 
"
If an account exists for this email, we've sent you instructions.
"
,

};

Enter fullscreen mode

Exit fullscreen mode

Same message, same 200 status, whether the user has a password, uses OAuth, or does not exist at all. This endpoint should never confirm or deny which email addresses are in your system.

Same page, same response to the browser, for every email submitted. The branching on password_hash happens entirely on the server side.

## What Shipped After These Five Bugs Were Gone

Registration with bcrypt hashing, a live password strength meter, and a terms checkbox. Email verification and password reset through Resend with separate token lifetimes: 24 hours for verification, 1 hour for reset. Google and GitHub OAuth with the account linking logic above. Role-based routes. An admin panel pulling live counts from the database. A 403 page instead of a crash when someone hits a route their role does not cover.

The data layer ownership pattern from Part 1 runs on every query.WHERE user_id = $1inside the SQL, not as a wrapper around the result. The auth check pattern from Part 3 runs on every mutation endpoint. Verify the caller before touching data. Both are in the kit exactly as written in the earlier posts in this series.

Live database counts in the admin panel. Anyone without the admin role who hits this URL directly lands on the 403 page instead.

One Tailwind v4 issue worth naming because it produces zero errors. Next.js 16 on Turbopack has a documented file watching problem where Tailwind's class detection misses.tsxfiles entirely. Clean build, no warnings, completely unstyled HTML. The fix:

/* app/globals.css — add after @import "tailwindcss" */

@source
 
"../app/**/*.{ts,tsx}"
;

@source
 
"../components/**/*.{ts,tsx}"
;

@source
 
"../lib/**/*.{ts,tsx}"
;

Enter fullscreen mode

Exit fullscreen mode

Three lines and everything renders correctly.

## Three Things for the Auth Checklist After This Build

Parts 1 through 3 of this series built a checklist of things that work locally and break in production. Three more belong on it now.

Client-side cookie writes can silently vanish with no error.Move the write to the server withresponse.cookies.set(). That is where it belongs regardless of any timing issue.

router.pushafter login does not trigger the proxy.If the proxy needs to read a freshly set cookie on the next request, that request has to be a real HTTP GET. Usewindow.location.href.

Wrap integer primary keys inString()before signing a JWT..setSubject(String(payload.sub))not.setSubject(payload.sub). ASERIALcolumn is an integer. The JWT type guard that catches this is correct. The claim is malformed, just not visibly so.

## Get the Auth Kit

Everything in this series built into one kit: three-layer security, email and password, Google and GitHub OAuth, email verification, password reset, role-based access, admin panel, and deployment guide.Next.js 16 Auth Kit at shubhra.dev

The full implementation tutorial with every code file, database schema, and deployment notes is atI Built a Next.js 16 Auth Kit. Every Edge Case I Found Is in Here.

Has anyone else hit the OAuth forgot-password edge case before it shipped? I started paying attention to it after this build. More common than I expected. People who register with Google genuinely try the forgot password page later because they forget how they originally signed in. Curious whether others caught it early or found out from a user.

Note: AI used for image editing.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (22 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
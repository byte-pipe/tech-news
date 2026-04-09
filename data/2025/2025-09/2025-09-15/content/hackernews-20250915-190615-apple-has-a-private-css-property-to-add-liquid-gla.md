---
title: Apple has a private CSS property to add Liquid Glass effects to web content
url: https://alastair.is/apple-has-a-private-css-property-to-add-liquid-glass-effects-to-web-content/
site_name: hackernews
fetched_at: '2025-09-15T19:06:15.057191'
original_url: https://alastair.is/apple-has-a-private-css-property-to-add-liquid-glass-effects-to-web-content/
author: _alastair
date: '2025-09-15'
published_date: '2025-09-15T14:02:45.000Z'
---

I have an incredibly boring summer hobby: looking at the changelog for theWebKit Github repo. Why? Because I spend a chunk of my professional life working with webviews inside mobile apps and I like to get an early peek into what's coming in the next version of iOS. Since Tim Cook has yet to stand up at WWDC and announce "one more thing... Service Worker support in WKWebView, provided you add the correct entry to theWKAppBoundDomainsarray in yourInfo.plist" (and you know what, heshould) manual research is the order of the day.

So I was really interested to see, the day after WWDC finished, a pull request named:

[Materials] Rename "hosted blur" materials to reference "glass"

Liquid Glasswas one of the big takeaways from 2025's WWDC. Probably the biggest change in iOS UI since iOS 7 ditched the skeuomorphic look of the past. But that's all native UI, what does any of that have to do with webviews?

A poke around the context of the PR revealed something really interesting: Apple has a custom CSS property named-apple-visual-effect. Not only does it allow the use of Liquid Glass in iOS 26 (via values like-apple-system-glass-material) but all versions support usingstandard materialswith values like-apple-system-blur-material-thin.

### Yes it works and no, we can't

Before you, like me, fire up Safari and start editing some CSS, I have bad news: no, it doesn't work on the web. As well it shouldn't. But italsodoesn't work by default in an app using WKWebView, you have to toggle a setting in WKPreferences calleduseSystemAppearance... and it'sprivate. So if you use it, say goodbye to App Store approval.

I wanted to try it out all the same so I hacked around to setuseSystemAppearanceto true, set my CSS to:

.toolbar {
 border-radius: 50%;
 -apple-visual-effect: -apple-system-glass-material;
 height: 75px;
 width: 450px;
}

lo and behold, it works!

0:00

 /
0:09

1×

With thanks to MapboxGL JS for the beautiful background

Whoever it was at Apple that decided to make this a CSS property is a genius because it makes it incredibly easy to provide different rules based on Liquid Glass support:

.toolbar {
 border-radius: 50%;
 height: 75px;
 width: 450px;
 background: rgba(204, 204, 204, 0.7);
}

@supports (-apple-visual-effect: -apple-system-glass-material) {
 background: transparent;
 -apple-visual-effect: -apple-system-glass-material
}

## Who cares?

It's an interesting piece of trivia but no-one outside of Apple can use it. So what does it matter? It doesn't. Except for the implication for what I'll callAlastair's GrandThe Toupée Theory of In-App Webviews(thanks tograypeggon Hacker News for the rename). Industry wide they don't have a great reputation. But my suggestion is this:the main reason webviews in apps have such a bad reputation is because you don't notice the webviews that are integrated seamlessly.

It stands to reason that Apple wouldn't have developed this feature if they weren't using it. Where? We have no idea. But they must be using itsomewhere. The fact that none of us have noticed exactly where suggests that we're interacting with webviews in our daily use of iOS without ever even realising it.

Food for thought!

## Sign up for Alastair Writes Code

Idle thoughts of a mobile/web developer

Subscribe

 Email sent! Check your inbox to complete your signup.


No spam. Unsubscribe anytime.

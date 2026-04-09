---
title: Sign in with Google in Chrome
url: https://underpassapp.com/news/2025/7/5.html
site_name: hackernews
fetched_at: '2025-07-30T01:07:09.652574'
original_url: https://underpassapp.com/news/2025/7/5.html
author: frizlab
date: '2025-07-30'
---

# Sign in with Google in Chrome

### July 28, 2025By Jeff Johnson ofUnderpass App Company

Many websites such as Yelp show an annoying “Sign in with Google” banner when you visit.

This is what Google callsthe One Tap user experience. Fortunately, my web browser extensionStopTheMadness Prohides “Sign in with Google” banners.

What you may not realize if you use Safari or Firefox is that the banners are never displayed in Google Chrome! You can see this in macOS Safari by spoofing the Chrome User-Agent header. In Safari Advanced Settings, enable “Show features for web developers.” This setting adds a Develop menu to Safari‘s main menu bar. The Develop menu includes a User Agent submenu with a list of several web browsers. When you select Google Chrome from the list and then load Yelp, the “Sign in with Google” banners no longer appear in Safari.

Although Chrome avoids the “Sign in with Google” banners, Google’s browser still has its own custom annoyance. If you‘re already signed in to your Google account when you visit a participating website such as Yelp, Chrome will display a One Tap dialog.

This dialog differs from the “Sign in with Google” banners you see in Safari and Firefox in a couple of important ways. First, the Chrome dialog isnotan element in the web page but rather a part of the Chrome native app user interface. Thus, StopTheMadness Pro cannot hide the dialog. Indeed, while Chrome is displaying the dialog, it blocksallChrome extension popup windows from appearing. Selecting an extension in the Extensions toolbar widget does nothing. (In other words, it‘s not a bug in StopTheMadness Pro.)

The second difference is that the Chrome dialog can be disabled in Chrome‘s Settings. Enterchrome://settings/content/federatedIdentityApiin the address bar to access the setting directly.

Select “Block sign-in prompts from identity services” to stop the dialogs from appearing in Chrome.

If the courts and antitrust regulators are reading—they probably won’t read my blog, but one can dream—this is yet another example of Google advantaging its own browser Chrome over other web browsers.

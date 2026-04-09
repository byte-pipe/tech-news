---
title: How I found a bypass in Google's big anti-adblock update
url: https://0x44.xyz/blog/web-request-blocking/
site_name: hackernews_api
fetched_at: '2025-07-15T01:05:40.364670'
original_url: https://0x44.xyz/blog/web-request-blocking/
author: deryilz
date: '2025-07-13'
description: Or, why you shouldn't write parts of your browser in JavaScript
tags:
- hackernews
- trending
---

D
erin Eryılmaz

 How I found a bypass in Google's big anti-adblock update


July 12, 2025

## About MV3

If you know anything about browsers, you've probably heard that Google Chrome is phasing out MV2 in favor of MV3. You've probably also heard that this hurts adblockers.

A quick explainer: "MV" stands for "manifest version." MV3 introduces a new type of runtime for Chrome extensions that, among other things, gets rid ofwebRequestBlocking, a permission that allows extensions to block requests dynamically based on their content (whichits replacementdoes not support). Adblockers heavily rely onwebRequestBlockingto function properly. Pretty convenient (cough cough) for a company that makes most of its revenue from ads to be removing that.

Anyway, with the phasing-out of MV2 pretty much done, now seems like a good time to talk about a bug in Chrome that I found and reported to Google in 2023.The bugletwebRequestBlocking(and yes, adblockers) work in MV3.

I still consider it probably the funniest bug I've ever found.

## Stop writing browsers in JavaScript

Yes, Chrome is written in C++. However, extensions are written in JavaScript, and the API functions they call look just like JavaScript functions, at least from the extension's point of view. But they aren't normal functions: they're special and do browsery C++ stuff through bindings. In theory, this should be safe.

But in the old days, Google decided it'd be a good idea to inject a bunch of JS files into pages that used Chrome APIs. These "extension binding modules" would initialize API functions and validate arguments before passing them to the browser.

(Note:here's the codebaseof those files in 2016.)

Turns out running privileged JavaScript in user-controlled websites was not a good idea, because JS can often be manipulated by overriding global functions and prototypes. Since certain APIs likechrome.runtimeexist on normal websites too, the extension bindings system led to multiple Universal XSS bugs back in 2015 and 2016.Here's onethat allows any website to inject code into any other website. Truly crazy stuff. If only I weren't 8 years old back then... maybe I could have cashed in.

Anyway, Google learned from their mistake and moved most API bindings to pure C++. However, a couple of JS binding files still exist and are used today. For example, if a Chrome extension runs the following code, it'll hit aJS loopand hang infinitely: (as of July 2025)

chrome.permissions.contains({ permissions: { length: Infinity }})

Maybe you are wondering what this has to do with adblockers.

Remember how I said only a few APIs still use JavaScript bindings?chrome.webRequestis one of them.

## The bug

This is how an MV2 extension would block requests to example.com:

chrome.webRequest.onBeforeRequest.addListener(() => {
 return { cancel: true }
}, { urls: ['*://*.example.com/*'] }, ['blocking'])

It's the'blocking'part at the end that requires thewebRequestBlockingpermission, and therefore isn't allowed in MV3. Without it, thecancel: truedoes nothing.

So clearly adding a blocking listener to thechrome.webRequest.onBeforeRequestevent does not work anymore. But we can do something crazy. We can makeour own event.Now, this should not be possible; it's not even a concept that makes sense. But, because of how the JS bindings work, you can do it. For some reason, there is awrapper classforwebRequestevents that contains some extra state.

(Anote on the securityof the above code.)

Instead of doing pure bindings between JS and C++, the browser creates one of these classes for everychrome.webRequestevent:onBeforeRequest,onCompleted, etc. Surprisingly, the.constructorof these events is still public. It points to yet another wrapper class, which internally callsWebRequestEventImpl(from the code above). You can use this to can create a new event with your own properties:

let WebRequestEvent = chrome.webRequest.onBeforeRequest.constructor
let fooEvent = new WebRequestEvent("foo")

There is still a lot of validation going on in the backend when you try to actually do things with these fake events. For example, trying to add a listener tofooEventkills the extension's process, because the event name is invalid. So how do you manipulate the properties ofWebRequestEventImplto do anything interesting?

After a lot of time looking into the C++ code, I found exactly one vulnerable thing: theopt_webViewInstanceIdparameter. This was set for Chrome platform apps, in order to let them manage their embedded websites (WebViews). Among other things, it let them use web request blocking to control navigation. Basically, if an event had a WebView ID, the permission check forwebRequestBlockingwould be skipped. The issue was that the browser never verified that an event with a WebView ID actually belonged to a platform app. So an extension could spoof it, skip the check, and use the blocking feature.

let WebRequestEvent = chrome.webRequest.onBeforeRequest.constructor

// opt_webViewInstanceId is the 5th argument
let fakeEvent = new WebRequestEvent("webRequest.onBeforeRequest", 0, 0, 0, 1337)

fakeEvent.addListener(() => {
 return { cancel: true }
}, { urls: ['*://*.example.com/*'] }, ['blocking'])

Maybe I should note that platform apps weredeprecated in 2020.I found this bug in 2023, and the code to handleopt_webViewInstanceIdstill exists in 2025. Goes to show how ancient code leads to bugs.

## What could have happened, and what happened

Technically, someone could have used this bug to make a perfectly working adblocker in MV3 by simply replacing all instances ofchrome.webRequest.onBeforeRequestwithfakeEvent. This would have been very funny, after all the hype about how adblockers were being killed.

But I don't know how to make an adblocker, so I decided toreport the issue to Googlein August 2023. It was patched in Chrome 118 bychecking whetherextensions usingopt_webViewInstanceIdactually had WebView permissions. For the report, I netted a massive reward of $0. They decided it wasn't a security issue, and honestly, I agree, because it didn't give extensions access to data they didn't already have.

(Shown above: my earnings from this bug.)

Anyway, it was a fun one, and it really shows how a few lines of code can sometimes bypass a big update by a big company. I hope you found it interesting! If you want to read another post about a bug in Chrome extensions, trythis one I found in the same year, which got a CVE number and a $10,000 reward.

Other posts

Email me

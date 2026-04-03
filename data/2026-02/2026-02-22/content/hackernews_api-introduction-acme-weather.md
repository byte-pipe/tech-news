---
title: Introduction - Acme Weather
url: https://acmeweather.com/blog/introducing-acme-weather
site_name: hackernews_api
content_file: hackernews_api-introduction-acme-weather
fetched_at: '2026-02-22T11:08:21.960266'
original_url: https://acmeweather.com/blog/introducing-acme-weather
author: cryptoz
date: '2026-02-21'
description: Acme Weather
tags:
- hackernews
- trending
---

# Introducing Acme Weather

Adam GrossmanFebruary 16, 2026

Fifteen years ago, we started work on the Dark Sky weather app.

Over the years it went through numerous iterations — including more than one major redesign — as we worked our way through the process of learning what makes a great weather app. Eventually, in time, it was acquired by Apple, where the forecast and some core features were incorporated into Apple Weather.

We enjoyed our time at Apple. So why did we leave to start another weather company?

It’s simple: when looking at the landscape of the countless weather apps out there, many of them lovely, we found ourselves feeling unsatisfied. The more we spoke to friends and family, the more we heard that many of them did too. And, of course, we missed those days as a small scrappy shop.

So let’s try this again…

## Embracing Uncertainty

Our biggest pet peeve with most weather apps is how they deal (or rather, don’t deal) with forecast uncertainty. It is a simple fact that no weather forecast will ever be 100% reliable: the weather is moody, fickle, and chaotic. Forecasts are often wrong.

Understanding this uncertainty is crucial for planning your day. Most weather apps will give you their single best guess, leaving you to wonder how sure they actually are, and what else might happen instead. Will it actually start raining at 9am, or might it end up pushed off until noon? Will there be rain or snow? How sure are you? You can’t plan your day if you don’t know how much you can trust the forecast, or know what other possibilities might arise. Rather than pretending we will always be right, Acme Weather embraces the idea that our forecast will sometimes be wrong. We address this uncertainty in several ways:

### Alternate Possible Futures

Our homegrown forecasts are produced using many different data sources, including numerical weather prediction models, satellite data, ground station observations, and radar data. Most of the time, our forecast will be a reliable source of information (it’s better than the one we had at Dark Sky). But, crucially, we supplement the main forecast with a spread of alternate predictions. These are additional forecast lines that capture a range of alternate possible outcomes:

A forecast showing multiple possible outcomes

This accomplishes a couple things:

First, the spread of the lines offers a sort of intuition as to how reliable the forecast is. Take the two forecasts below. In the first, the alternate predictions are tightly focused and the forecast can be considered robust and reliable. In the second, there is a significant spread, which is an indication that something is up and the forecast may be subject to change. It’s a call to action to check other conditions or maps, or come back to the app more frequently:

A more reliable forecastA less reliable forecast

Over time, you build up an intuitive sense of just how much you can actually trust the forecast. After using this for the past six months, I never want to go back to a single forecast again!

Second, it simply shows what else might plausibly happen. In what time range might the storm arrive? Will the snow hit early, or might it be delayed and turn mostly to rain? When the weather is changing rapidly, predictions can become less reliable. We’ll show you different possible futures, so you can be better informed.

### Community Reporting

Alternative Forecasts are designed to help make better hour-to-hour or day-by-day decisions. Community reports are intended to help with real-time weather events. Current conditions often evolve quickly during storms, radar is imperfect and can fail to detect precipitation during light rain, snow versus freezing rain can be volatile, etc.

To address this, we’ve built a feature that allows any user to submit a report of the current conditions near them, which can be seen on the map:

Community reports

You can choose from a pre-selected list of weather condition icons (or even a list of emojis for when it’s feeling particularly 💩 out). There’s nothing more reliable than when a person nearby tells you what’s happening, so if there are recent reports near you we’ll flag it in the app.

## Useful Maps

We absolutely love maps. They provide the context around the weather. Sure, the forecast may say you’ll get rain, but a map will complete the picture by showing you the full breadth of the storm, where it will hit, and where you are relative to it.

We’ve built a large number of maps, including radar and lightning, rain and snow totals (why do most other weather apps not offer this?), wind, temperature and humidity, cloud cover, hurricane tracks, etc. While you can explore them all in the map tab, we also make sure to embed the most relevant maps directly inside the forecasts to provide a contextual backdrop.

## Notifications

A weather app is only useful if you remember to check it. I’ve lost count of the number of times I’ve gotten stuck in the rain — not because the forecast was wrong, but because I simply didn’t check the app.

The solution? A comprehensive set of weather notifications. Turn them on, and no longer worry about missing important weather events.

Our notifications include everything from down-to-the-minute rain warnings, to government severe weather alerts, nearby lightning, community reports, and even whether or not a rainbow might be visible outside your house.

We also let you create custom notifications, tailored to whatever you care about. Want to know if it’ll be windy, or if the UV index will be high, or if you’ll get heavy rain in the next 24 hours? We’ve got you covered.

## Acme Labs

A weather app shouldn’t just be about helping you avoid bad weather; it should also be fun! There’s a wide world of meteorological phenomena that we would like to highlight. As such, we’re launching “Acme Labs”, which is a set of experimental tools inside the app to highlight fun and interesting things happening where you are.

We’re starting with a couple initial features, including:Rainbow alerts, where we bring our hyperlocal rain forecasts to bear to pinpoint where rainbows are occuring right now, andbeautiful sunsets, where we'll let you know if the sunset will be particularly lovely this evening.

## Privacy & Trust

We take your privacy very seriously. Please review ourprivacy policy, but here is our philosophy in a nutshell:

* We won’t collect any information other than what is necessary to provide the service you’re paying for. This information will only be used to provide that service, and for nothing else.
* We won’t save or store any information that isn’t necessary. We don’t want or need your location history, for example, and simply not storing it in the first place means it can’t fall into the wrong hands.
* We will never sell or give your information to third parties, such as advertisers. We make our money directly from our customers.
* We don’t use third-party trackers or analytics services, because we can’t guarantee what they will or won’t do with the information we send them.

## Conclusion

Well, that’s Acme Weather. We’ve been making weather apps for 15 years, from Dark Sky to Apple, and this is the culmination (the acme?) of everything we’ve learned along the way. It’s the weather app we’ve always wanted, and always wanted to build.

Acme Weather isin the iOS App Store, and we plan on offering an Android version soon (if you’re an Android developer and would like help,drop us a line!) The app is a $25/year subscription, with a two-week free trial.

We think you’ll love it. So try it out, and let us know what you think!

---
title: Get the location of the ISS using DNS – Terence Eden’s Blog
url: https://shkspr.mobi/blog/2025/07/get-the-location-of-the-iss-using-dns/
site_name: hackernews
fetched_at: '2025-07-07T07:04:34.778787'
original_url: https://shkspr.mobi/blog/2025/07/get-the-location-of-the-iss-using-dns/
author: Terence Eden
date: '2025-07-07'
published_date: '2025-07-06T12:34:33+01:00'
description: Regular nonsense about tech and its effects 🙃
---

I love DNS esoterica. Weird little things that you can shove in the global directory to be distributed around the world instantly(ish).

Domain names, likewww.example.comusually resolve to servers. As much as we think of "the cloud" as being some intangible morass of ethereal Turing-machines floating in probability space, the more prosaic reality is that they're just boxen in data centres. They have a physical location.

Got a tricky machine which is playing silly-buggers? Wouldn't it be nice to know exactly where it is? That way you can visit and give it somepercussive maintenance.

Enter the DNS LOC record!

The snappily titledRFC 1876is anexperimentalstandard. It allows you to create a DNS record which specifies the latitude and longitude of your server. Of course, some data-centres are very tall and some are underground. So it also contains an altitude parameter.

The standard allows for a minimum altitude of -100,000 metres - deep enough for any bunker! The maximum altitude is 42,849,672 metres which is high enough to allow it to be used onsatellites in geostationary orbit.

So, as a bit of fun, I decided to createwhere-is-the-iss.dedyn.io

It isn't a website. You can't ping it. There's no way to interact with itexceptby using DNS. Yup! You can use a DNS query to get the (approximate) location of the International Space Station!

Linux and Mac users0can run:

dig where-is-the-iss.dedyn.io LOC

And receive back the latest position of the ISS:

;; ANSWER SECTION:
where-is-the-iss.dedyn.io. 1066 IN LOC 47 24 53.500 N 66 12 12.070 W 430520m 10000m 10000m 10000m

The DNS records are updated every 15 minutes on a best-effort basis1.

## How

The lovely people atN2YOhave a website which allows you to trackloadsof objects in orbit. They also have aneasy to use APIwith a generous free tier.

Callinghttps://api.n2yo.com/rest/v1/satellite/positions/25544/0/0/0/1/&apiKey=_____gets back the latest position:

 JSON
{


"info"
:
{


"satname"
:
"SPACE STATION"
,

"satid"
: 25544,

"transactionscount"
: 7

}
,

"positions"
:
[


{


"satlatitude"
: -21.25409321,

"satlongitude"
: 140.3335763,

"sataltitude"
: 420.09,

"azimuth"
: 292.92,

"elevation"
: -70.95,

"ra"
: 202.69300845,

"dec"
: -32.16097472,

"timestamp"
: 1751366048,

"eclipsed"
: true

}


]

}

Note that the altitude is in Km, whereas the LOC format requires m.

The latitude and longitude are in decimal format - they need to be converted to Degrees, Minutes, and Seconds.

There were only a few free domain name providers who offer an API for updating LOC records. I went fordeSECa charity from Berlin. They havecomprehensive API documentation.

Adding the initial LOC record is done with:

 Bash
curl https://desec.io/api/v1/domains/where-is-the-iss.dedyn.io/rrsets/ \
 --header "Authorization: Token _______" \
 --header "Content-Type: application/json" --data @- <<< \
 '{"type": "LOC", "records": ["40 16 25.712 S 29 32 36.243 W 427550m 0.00m 10000m 10m"], "ttl": 900}'

However, updating the record is a little trickier. it needs to be sent as anHTTP PATCHto a subtly different URl. The PATCH only needs to send the data which have changed.

 Bash
curl -X PATCH https://desec.io/api/v1/domains/where-is-the-iss.dedyn.io/rrsets/@/LOC/ \
 --header "Authorization: Token _______" \
 --header "Content-Type: application/json" --data @- <<< \
 '{"records": ["40 16 25.712 S 29 32 36.243 W 427550m 0.00m 10000m 10m"]}'

I set theTime To Liveat 900 seconds. Every 15 minutes my code runs to update the record2. That keeps me well within the API limits for both services. I could add TXT records showing when it was last updated, or other sorts of unstructured data, but I think this is enough for a quick proof-of-concept.

There you have it! A complex and silly way to demonstrate how DNS can be used to hold the most unlikely of records3. Say, I wonder how you'd represent the co-ordinates of the Mars Rover…?

## Further Reading

For more DNS weirdness, please see my other posts:

* BIMI - SVG in DNS TXT WTF?!
* Why you can't dig Switzerland

1. I don't think there's a way for Windows users to look up LOC records using PowerShell or the Command Prompt.↩︎
2. Look, I'm not NASA, OK? If you're using this to help you dock then I cannot be held responsible.↩︎
3. I suppose you could build an API with unlimited request limits by distributing data via DNS TXT records. Would best suit static or infrequently updating data. Push it once to DNS and let everyone query it semi-locally.↩︎
4. See if you can find the other interesting record I've added to DNS!↩︎

## Share this post on…

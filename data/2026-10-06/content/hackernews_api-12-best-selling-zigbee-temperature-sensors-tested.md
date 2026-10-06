---
title: 12 Best-Selling Zigbee Temperature Sensors Tested | SmartHomeScene
url: https://smarthomescene.com/reviews/best-selling-zigbee-temperature-sensors-tested/
site_name: hackernews_api
content_file: hackernews_api-12-best-selling-zigbee-temperature-sensors-tested
fetched_at: '2026-10-06T22:54:09.621467'
original_url: https://smarthomescene.com/reviews/best-selling-zigbee-temperature-sensors-tested/
author: walrus01
date: '2026-10-04'
published_date: '2026-08-04T07:30:04+00:00'
description: I compared 12 Zigbee temperature and humidity sensors under $15 from Aqara, Sonoff, Tuya, Thirdreality, Zemismart, and Moes to find which ones are worth buying.
tags:
- hackernews
- trending
---

Content may contain affiliate links - 
read disclosure
.

UPDATED 14.08.2026:Addedlow-temperature benchmarks in a fridge.

Finding the best Zigbee temperature and humidity sensors is not something an individual review can really answer, so I decided to switch things up and compare devices head to head instead of testing them one by one. I recently did this for somecheap AliExpress Zigbee door and window sensorsandZigbee smart buttons, so simple temperature and humidity sensors are up next.

I picked up 12 of the best-selling Zigbee temperature and humidity sensors I could find online, sourced mainly from AliExpress. The lineup covers Aqara, Sonoff, Tuya, Thirdreality, Zemismart, and Moes, so this is not a one-brand roundup, but rather real look at what people are actually using in their smart homes.

None of these sensors have displays, all of them run Zigbee, and all of them are battery-powered. What separates them from each other comes down to accuracy, measurement range, build quality, form factor, battery type, and how each one holds up against a calibrated reference sensor, which is exactly what the rest of this article breaks down.

## Testing Methodology

I installed all twelve sensors in my office, right next to a calibrated sensor I decided to use as a base for accuracy. My benchmark device is aXiaomi Miaomiaoce MHO-C401flashed with thelatest pvvx custom firmwareand communicating over Bluetooth Low Energy with Home Assistant.

To get an accurate base for benchmarks, I decided to calibrate it against a lab-certified thermometer at a friend’s butcher shop, as weirdly as that sounds. His particular thermometer gets checked and calibrated by the state on a schedule (every 3 months) because it sits inside a commercial meat refrigerator and it is required by law. After calibration, my MHO-C401 needed an offset of minus 0.5°C and plus 4% humidity to match the reference reading exactly.

It is worth clarifying from the start that my setup does not represent typical room comfort conditions, since the calibration was done at a much lower temperature, around 4°C. Sensors do not always respond in a perfectly straight line across a wide temperature range, so this fixed point is not a guarantee of the exact same accuracy at room temperature. What it does give me is a consistent, repeatable anchor to measure every Zigbee sensor against under identical conditions, which is exactly what this comparison needs. In the end, trends matter more than single datapoints, since you can always recalibrate a sensor in Home Assistant.

I tested all sensors with Zigbee2MQTT version 2.12.1-dev and theSMLight SLZB-06MG24 PoE coordinator. TheSLZB-UltimaI normally use for these comparison articles is currently operating as a Thread Border Router, so this is a brand new Zigbee network I created just for this article. Each sensor sits at about 3.5 meters from the coordinator and there are no other network devices paired.

## Models, Brands and Specifications

These twelve sensors come from several brands, Aqara, Sonoff, Tuya, Thirdreality, Zemismart and Moes, and every single one costs under 15 dollars on AliExpress with one exception: Thirdreality. TheTemperature and Humidity Sensor Lite by Thirdrealitycosts $19.99 and is not sold on AliExpress at all, but I decided to include it since a lot of you already have it and asked me to do so.

I gave each one a color and a code name again to make them easier to track, since most of the actual model numbers are gibberish.Hover over the dot next to any device name and the real brand and model number will pop up.

Zigbee Temperature and Humidity Sensors

Furthermore, Aqara and Sonoff are not AliExpress-only brands, but they are available there and fit my criteria of being priced under $15. I picked the best sellers from each brand rather than obscure listings, so what you see here is what most people actually end up buying.Here are the 12 sensors, what they cost me and where you can get them:

Img
Code Name
White Label
Zigbee Model
Price
AliExpress
Amazon
Tony 
●
Aqara
T&H Sensor
Aqara
WSDCGQ11LM
From
$14.89
AliExpress
AliExpress 2
Amazon US
 ● 
Amazon UK
Amazon DE
 ● 
Amazon NL
Carmela 
●
SONOFF
AirGuard TH Lite
SONOFF
SNZB-02B
From
$9.23
AliExpress
AliExpress 2
Amazon US
 ● 
Amazon UK
Amazon DE
 ● 
Amazon NL
Paulie 
●
SONOFF
T&H Sensor
SONOFF
SNZB-02P
From
$13.08
AliExpress
AliExpress 2
Amazon US
 ● 
Amazon UK
Amazon DE
 ● 
Amazon NL
Richie 
●
ThirdReality
T&H Sensor Lite
ThirdReality
3RTHS0224Z
From
$19.99
AliExpress
AliExpress 2
Amazon US
 ● 
Amazon UK
Amazon DE
 ● 
Amazon NL
Silvio 
●
Zemismart
ZM-ZXZTH
TS0201
_TZ3000_nau60otv
From
$14.48
AliExpress
AliExpress 2
Amazon US ● Amazon UK
Amazon DE ● Amazon NL
Chris 
●
Moes
ZSS-S01-TH
TS0201
_TZE3000_f2bw0b6k
From
$6.65
AliExpress
AliExpress 2
Amazon US
 ● 
Amazon UK
Amazon DE
 ● 
Amazon NL
Junior 
●
Tuya
TH09Z
TS0201
_TZ3000_yupc0pb7
From
$11.35
AliExpress
AliExpress 2
Amazon US ● 
Amazon UK
Amazon DE
 ● 
Amazon NL
Melfi 
●
Tuya
TH01
TH01
Zbeacon
From
$4.60
AliExpress
AliExpress 2
Amazon US
 ● 
Amazon UK
Amazon DE
 ● 
Amazon NL
Meadow 
●
Tuya
IH-K009
TS0201
_TZ3000_dowj6gyi
From
$8.42
AliExpress
AliExpress 2
Amazon US
 ● 
Amazon UK
Amazon DE
 ● 
Amazon NL
Livia 
●
Tuya
ZTH02
TS0601
_TZE200_9yapgbuv
From
$9.12
AliExpress
AliExpress 2
Amazon US ● Amazon UK
Amazon DE
 ● 
Amazon NL
Adriana 
●
eWeLink
TH03YZ
CK-TLSR8656-SS5-01
eWeLink
From
$5.34
AliExpress
AliExpress 2
Amazon US
 ● 
Amazon UK
Amazon DE
 ● 
Amazon NL
Furio 
●
Tuya
UZ-01T
TS0201
Wing
From
$5.49
AliExpress
AliExpress 2
Amazon US ● Amazon UK
Amazon DE ● Amazon NL
NOTE: 
AliExpress prices are highly region dependent, so expect differences.

A lot of these Tuya sensors can be found under different white-label names sold by various brands and retailers. This is nothing new and is standard practice, the same Tuya device gets rebadged and sold under multiple model names all the time. I listed the labels and Zigbee models exactly as I found them on the packaging and Zigbee2MQTT. Whatever the ID ends up being on your unit, it will work with Zigbee2MQTT in 99.9% of cases.

PRO TIP:If you do opt for the Aqara Temperature and Humidity Sensor, get theT1 WSDCGQ12LM versioninstead of the older one I tested here. Both are very similar with minor differences, but the T1 brings improvements in connectivity and network stability.

### Technical Specification

The table below lists every spec as reported by the manufacturer or pulled directly from the Zigbee2MQTT device page. Some of these, like reporting interval, I had to figure out myself by analyzing Z2M debug logs for a lot of the sensors. Datasheets were either wrong or simply did not all specs listed.

Code Name
Model
Battery
Dimensions
Range
Accuracy
Resolution
Reporting
Tony 
●
Aqara
WSDCGQ11LM
1×CR2032
2 years
36×36×9mm
-20°C to 50°C
0 to 100% RH
±0.3°C
±3% RH
0.01°C
0.01%
60min or
±0.5°C / 6% RH
Carmela 
●
SONOFF
SNZB-02B
2×AAA
2 years
66.3×28×20mm
-20°C to 60°C
5 to 95% RH
±0.2°C
±2% RH
0.1°C
0.1%
60min or
±0.2°C / 2% RH
Paulie 
●
SONOFF
SNZB-02P
1×CR2477
2 years
45×45×17.7mm
-10°C to 60°C
5 to 95% RH
±0.2°C
±2% RH
0.1°C
0.1%
60min or
±0.2°C / 2% RH
Richie 
●
ThirdReality
3RTHS0224Z
2×AAA
2 years
55.6×56×12mm
-15°C to 50°C
0 to 100%
±0.3°C
±2%
0.01°C
0.1%
15min or
±0.5°C / 3% RH
Silvio 
●
Zemismart
ZM-ZXZTH
1×CR2032
6 months
38×38×12mm
-10°C to 50°C
0 to 95% RH
±0.3°C
±3% RH
0.01°C
0.01%
30min or
±0.5°C / 3% RH
Chris 
●
Moes
ZSS-S01-TH
1×CR2032
1 year
40×26×13mm
-10°C to 50°C
0 to 99% RH
±0.3°C
±3% RH
0.01°C
0.01%
60min or
±0.3°C / 1% RH
Junior 
●
Tuya
TH09Z
2×AAA
1 year
73×27×23mm
-15°C to 60°C
0 to 99% RH
±0.6°C
±6% RH
0.01°C
0.1%
5min or
±0.1°C / 0.1% RH
Melfi 
●
Tuya
TH01
2×AAA
1 year
70×25×20mm
-10°C to 55°C
0 to 99% RH
±1°C
±5% RH
0.01°C
0.01%
60min or
±0.2°C / 1% RH
Meadow 
●
Tuya
IH-K009
2×AAA
1 year
70×24×20mm
-10°C to 55°C
10 to 90% RH
±0.3°C
±3% RH
0.01°C
0.01%
10min or
±0.1°C / 0.3% RH
Livia 
●
Tuya
ZTH02
1×CR2032
1 year
56×26.5×13mm
-20°C to 60°C
0 to 100% RH
±1°C
±5% RH
0.1°C
1%
60min or
±0.5°C / 1% RH
Adriana 
●
eWeLink
TH03YZ
1×CR2450
2 years
⌀37×11.6mm
-10°C to 50°C
0 to 95% RH
±0.5°C
±3% RH
0.1°C
0.1%
60min or
±0.2°C / 1% RH
Furio 
●
Tuya
UZ-01T
1×CR2045
1 year
⌀40×13mm
-9.9°C to 60°C
0 to 99% RH
±1°C
±1% RH
0.1°C
1%
60min or
±0.5°C / 1% RH

On paper, most of these sensors are similar in detection range, measuring accuracy and reporting interval. In practice however, there are differences in the way they operate and report over Zigbee. Battery type and form factor are also an important preliminary differentiator. Some people prefer using AAAs or even rechargeable ones, while others like the smaller footprint of coin cell batteries.

### Size and Form Factor

Tony●is the thinnest and smallest sensor in this entire group at 36 by 36 by 9mm. Its footprint is small enough that it blends in wherever you stick it.Adriana●, the eWeLink TH03YZ, is a close second. At a diameter of 37mm with 11.6mm thickness, it feels more like a tiny smart button.Chris●also has a shape that I like. It’s small, rounded, and doesn’t have anything printed on the front.

None of the AAA-powered sensors impressed me on shape.Junior●,Melfi●, andMeadow●all carry the bulk that comes with two AAA cells, ranging from 70 to 73mm long. If I had to pick a favorite among the AAA group, it would beCarmela●, the Sonoff SNZB-02B, which keeps a slimmer 66.3 by 27.8 by 20mm profile despite the battery compartment.Junior●andCarmela●are the only ones that ship with a string, so you can hand them and easily move them around.

The two round sensors in the group,Adriana●andFurio●, are also quite compact for what they are, at 37mm and 40mm in diameter.Richie●, the Thirdreality 3RTHS0224Z, is the tallest and widest of all sensors. It’s a bit thinner than all other AAA sensors, but it’s still quite large in comparison.

### Build Quality and Weather Resistance

Build quality is quite good all around, and picking a favorite here really comes down to personal preference rather than one sensor being noticeably better made than the rest. Nothing rattles, shakes or feels flimsy when you shake the housing in either of them. Every sensor mounts with an adhesive pad or a screw, so you can stick any of them wherever you want to.

Weather resistance is where one sensor stands out.Junior●, the Tuya TH09Z, is the only sensor here with an IP65 rating, which means it can handle dust and water jets and makes it the only one in this comparison you could reasonably place outdoors or in a damp spot like a bathroom or greenhouse. The remaining eleven sensors carry no IP rating at all, so treat them as indoor, dry-location devices only.

### Battery Type and Expected Battery Life

Seven of the twelve sensors run on a single coin cell batteries.Paulie●uses the larger CR2477,Adriana●uses a single CR2450, and five sensors,Carmela●,Richie●,Junior●,Melfi●, andMeadow●, run on two AAA batteries.

Zigbee temperature sensors battery types

I did not run a real-world battery life test, since 10 days of data is nowhere near enough to draw a meaningful conclusion. Battery drain on Zigbee end devices depends on a lot of factors like reporting interval and sampling rate.

However, outside of this test, I’ve been running first-gen Aqara sensors in my own home for years without a battery change. They are among the most efficient Zigbee temperature and humidity sensors out there, even though they run on a single CR2032 battery.

Paulie●deserves a specific mention here too. Its CR2477 packs meaningfully more capacity than a standard CR2032, at the cost of just a bit of extra thickness. Its official rated battery life is 4 years, the best in this comparison. If you want coin cell convenience without swapping batteries as often,Paulie●is the one to look at.

## Zigbee2MQTT Integration and Pairing

All sensors paired to Zigbee2MQTT 2.12.1-dev without a single issue. Each one joined the network immediately after I removed the battery protective foil or entered pairing mode, no re-pairing and no failed interviews. As I mentioned earlier, the coordinator I used this time is theSMLight SLZB-06MG24. None of the AAA-powered sensors shipped with batteries and I had to provide my own, so factor that into the price if you are ordering one of those.

Furio●andSilvio●both came up under a recycled converter from another sensor with a display, even though neither of these units actually has one. This has no practical effect, since the correct endpoints are still exposed and everything works as expected. Every other sensor identified itself properly with no converter mismatches.

All 12 sensors sit 3.5 meters from the coordinator, and every one of them reported a strong signal after pairing. Reported link quality ranged from 180 to 250 across all devices.Meadow●andChris●both reported a lower LQI right after joining, but within a few updates both settled into the 200 to 210 range along with the rest.

### Exposed Entities and Features

Paulie●is the only one that had a firmware update through Zigbee2MQTT’s OTA feature that took about 15 minutes to complete. On top of temperature and humidity, a couple of sensors expose extra data points worth knowing about.Carmela●reports dew point and vapor pressure deficit (VPD), whileTony●is the only one that exposes atmospheric pressure.

Obviously, all sensors expose temperature, humidity, and a couple of battery diagnostic entities. Most report battery level as a percentage, withLivia●being the only one that reports battery as a low-medium-high sensor.

### Accuracy and Resolution

Accuracy and resolution are two different specs that often get confused, but they refer to two different things.Accuracytells you how close a sensor’s reading is likely to be to the actual temperature or humidity in the room, expressed as a margin like ±0.3°C or ±3% RH.Resolutiontells you the smallest change a sensor can register at all, regardless of whether that reading is correct.

For example, a sensor with tight resolution but poor accuracy will give you a very precise-looking number that is still wrong, while a sensor with coarse resolution but good accuracy will round more but still land close to the true value. To check real resolution rather than just trusting a datasheet, I went through my own Zigbee2MQTT logs and measured the smallest step size between consecutive readings for each of the 12 sensors, both for temperature and humidity.

Tony●,Silvio●,Chris●,Meadow●andMelfi●have the finest resolution in the group, catching changes as small as 0.01°C and 0.01% RH.Junior●andRichie●are close behind at 0.1%RH with the same temperature resolution.Carmela●,Paulie●, andAdriana●report in coarser 0.1°C and 0.1% RH steps, andLivia●andFurio●round humidity in whole 1% RH increments. None of this changes how accurate any of these sensors are, a coarse sensor can still measure correctly, it just cannot show you movement smaller than its own step size.

### Temperature and Humidity Calibration

Both SONOFF sensors also support calibration at the firmware level, not just through Zigbee2MQTT like the rest. In practice this makes no real difference, since none of these sensors have a display of their own, and the calibration options built into Zigbee2MQTT under each device’s Settings tab work just as well regardless of whether firmware-level calibration is also available.

When you calibrate through Zigbee2MQTT’s Settings (Specific) menu, the reported value gets corrected before being committed to database. Since there is no screen to display the wrong value, the calibration works perfectly across all devices.

### Changing the Reporting Interval

I also tested whether each sensor’s reporting interval can be changed through Zigbee2MQTT. One thing to know before trying this yourself: you absolutelymust press the pairing button on the sensor first to wake it upbefore sending the new reporting configuration. Sending the payload while the device is asleep just gets ignored. For my test, I set both the minimum and maximum reporting interval to 5 seconds with a threshold of 0, which tells the sensor to ignore the measured value entirely and just report every 5 seconds.

Changing temperature reporting interval in Zigbee2MQTT

Most of the sensors allow you to change the interval without issue.Carmela●,Paulie●,Richie●,Chris●,Junior●,Silvio●,Melfi●,Adriana●andFurio●all switched over to reporting every 5 seconds exactly as configured. These send a payload respecting the configured interval, regardless of what the measured value is.

Three sensors do not have an adjustable reporting interval.Tony●, the Aqara WSDCGQ11LM, has its reporting interval hardcoded at the firmware level, which is also the reason it holds up so well on battery life, and simply does not expose this setting for adjustment.Livia●behaves the same way and ignores any attempt to change it.Meadow●sits somewhere in between, as it appears to write to the msTemperatureMeasurement cluster without an error, but the actual reporting behavior never changes no matter what value I sent.

## Temperature Testing and Comparison

Before getting into hard numbers and small deviations, it is worth noting that every single sensor in this comparison follows the overall trend of my benchmark office sensor. Over the roughly 10 days I had all 12 running side by side, none of them drifted off or lost track of the pattern, even the ones that were not perfectly accurate.Here’s a graph from Home Assistant from the last couple of days:

Zigbee T&H Sensors temperature graph

Since most of the group stayed fairly close with only small deviations that still followed the graph, I want to call out theleast accurate sensors first. To be clear from the start: This doesn’t mean these devices are completely trash, it just means they need calibration and I would not pick them over any of the others for accuracy alone.

Livia●,Adriana●,Richie●andFurio●had the largest deviations, combined with a reporting rate that felt inconsistent by default. All four reported consistently lower than my benchmark, with the exception ofRichie●, which bounced around unpredictably, sometimes lower and sometimes higher than the reference.Meadow●reported consistently higher than the benchmark, but at a nice stable rate and it followed the trend well.

These sensors had an average deviation of 0.5°C, with the largest belonging toLivia●at a consistent 0.8°C. The biggest disappointment here isRichie●, the Thirdreality T&H Sensor Lite. Not only did it show deviations similar to the rest, it also failed to follow the trend cleanly, jumping up and down instead of tracking a steady offset.Sensors to avoid:Livia●,Adriana●,Richie●,Furio●,Meadow●

Temperature: Least accurate Zigbee temperature sensors

Tony●,Junior●,Paulie●,Carmela●,Melfi●,Silvio●andChris●all performed better, with steadier reporting and closer tracking to the benchmark. These are the better candidates out of the 12 based solely on temperature accuracy out of the box. All of them follow the trend properly and report in a logical way, with one exception.Junior●reports very frequently on its default settings, which actually results in a smoother, cleaner curve on the graph than the others in this group but can waste battery if not lowered.

These sensors had an average deviation of just 0.2°C, which is extremely accurate. Because of how each one handles reporting interval and threshold logic, no payload gets sent until the preset threshold is crossed, some of them produce a staircase pattern on the graph rather than a smooth curve. This is easy to fix by adjusting the reporting rate, especially on the SONOFF sensors, which respect both the interval and threshold settings perfectly.

Temperature: Most accurate Zigbee temperature sensors

If I had to make a pick, I would go withPaulie●orCarmela●.Paulie●runs on a larger battery (CR2477) than the usual CR2032, whileCarmela●runs on two AAA cells, so either one gives you room to increase the reporting interval depending on what you need the sensor for.Tony●andChris●are close seconds in accuracy, but I am not a fan of the fact that you cannot adjust the reporting interval on the Aqara sensor.Junior●andMelfi●are also a good choice if you prefer sensors with AAA batteries instead of coin cells.Top 5 to consider for temperature:Tony●,Paulie●,Carmela●,Junior●,Chris●

## Humidity Testing and Comparison

Humidity turned out to be a bit of a different story. Deviations here are more varied across the board compared to temperature, but once again, every sensor followed the overall trend closely against my benchmark.Here’s a graph from Home Assistant from the last couple of days:

Zigbee T&H Sensors humidity graph

The least accurate sensors for humidity turned out to beLivia●,Junior●,Richie●,Adriana●,Melfi●,Furio●, andSilvio●. That said, the gap between my benchmark and these sensors stayed within 4 percent, which honestly is not that big of a difference in practice. As with temperature,Livia●andAdriana●also have a weaker default reporting interval, which results in more spread out datapoints on the graph. While technicallyJunior●is not as accurate as the others, it follows the trend perfectly and updates frequently.Sensors to avoid:Livia●,Richie●,Adriana●,Melfi●,Furio●, andSilvio●

Humidity: Least accurate Zigbee humidity sensors

The most accurate sensors for humidity areTony●,Chris●,Paulie●,Carmela●andMeadow●.Chris●had the jankiest staircase graph out of all of them, but it was due to the reporting interval and not measuring inaccuracy likeRichie●. All of them followed the trend very closely and are great picks for humidity measurements.Top 5 to consider for humidity:Tony●,Chris●,Paulie●,Meadow●,Carmela●

Humidity: Most accurate Zigbee humidity sensors

## Low Temperature Performance in a Fridge

Someone asked me to see how these sensors would perform in lower temperatures, so I decided to stick all 12 of them inside my fridge. I cleared out a shelf right under the eggs, so for a few days I had them report data while a dozen eggs or so judged them from above. You do not need to know how that conversation with my significant other went, but since it is summer, that was my only option. The fridge is set to 5°C and cycles naturally, climbing up to around 8°C before the compressor kicks back in and drops it below 5°C again, roughly once every hour.

Temperature sensors installed in fridge

Richie●,Furio●,Melfi●,Meadow●andAdriana●were the least accurate of the group here, all consistently reading higher than my benchmark.Richie●also had by far the choppiest reporting of the bunch, with gaps of up to 6 hours between updates at times, which makes it hard to trust for anything time-sensitive in a cold environment like this.Furio●tracked the trend of the cooling cycle closely, but consistently reported the highest temperature of all 12 sensors throughout the test.Sensors to avoid for low temperature:Richie●,Furio●,Melfi●,Meadow●,Adriana●

Fridge Temperature: Least accurate Zigbee temperature sensors

Tony●,Carmela●,Paulie●,Silvio●,Chris●,Junior●andLivia●gave me best results.Silvio●occasionally dipped below 4°C at the bottom of the cooling cycle, lower than the rest of this group, but still tracked the climb back up accurately once the compressor cycle reversed. All 12 sensors followed the fridge’s temperature cycle closely, the real differentiator here was reporting interval rather than raw accuracy.Sensors to consider for low temperature:Tony●,Carmela●,Paulie●,Junior●,Chris●,Livia●

Fridge Temperature: Most accurate Zigbee temperature sensors

The worst sensors for measuring humidity at low temperatures here wereRichie●,Junior●andLivia●.Richie●again had an abysmal reporting rate, whileJunior●had the worst accuracy of the entire group. Surprisingly, humidity results were much closer overall than temperature, with the rest of the sensors reporting right on par with my office calibrated benchmark.

Fridge Humidity: All sensors

The most surprising result of this whole test had nothing to do with the Zigbee sensors at all. My BLE benchmark, the one I use as the reference point for every comparison in this article, turned out to be the least reliable connectivity-wise. Since it relies on an ESP32 Bluetooth proxy, a handful of readings never made it through, and those dropped packets showed up as gaps in the benchmark data itself, not from any Zigbee device struggling in the cold.

DISCLAIMER: none of these sensors are designed for actual fridge use long-term, the humidity and condensation inside will eventually damage the electronics, so treat this as a quick stress test rather than a real recommendation!

## Verdict

In my opinion,you cannot really go wrong with any of these 12 sensors on accuracy alone.None of them have a screen, which means every single one can be nudged up or down inside Zigbee2MQTT as long as you have a reliable reference sensor to calibrate against. A sensor running half a degree off the benchmark is a quick fix in Z2M or Home Assistant, not a reason to avoid it outright.

This is why I do not think accuracy alone should be the deciding factor here. For me it comes down to battery type, device size, and whether the reporting interval can actually be adjusted.Tony●,Livia●andMeadow●do not allow changing the reporting interval, so I would not pick any of them over the rest.Tony●, the Aqara WSDCGQ11LM, gets a partial pass, since it makes up for the lack of adjustability with good accuracy and excellent battery life.With that out of the way, here are my three picks.

🥇BEST OVERALL

Sonoff SNZB-02P

Zigbee 3.0

Temperature, Humidity

CR2477

ZHA, Zigbee2MQTT

Amazon US
AliExpress

Also on:Amazon UK,Amazon DE,Amazon NL,Amazon FR,AliExpress 2,Domadoo.

BEST OVERALL:Paulie●, the SONOFF SNZB-02PPaulie●reports temperature and humidity very accurately, allows you to change the reporting interval without issues and can be calibrated at firmware level. It runs on a single CR2477 which can provide up to 4 years of battery life. It is not the smallest or thinnest sensor in this list, but it’s compact, well-made and comes with a nice magnetic mount.Paulie●is definitely the one I would go for if I had to pick only one or If I have to deploy many sensors across my home.

🥇BEST RUNNER-UP

Moes ZSS-S01-TH

Zigbee 3.0

Temperature, Humidity

CR2032

ZHA, Zigbee2MQTT

AliExpress
Domadoo

Also on:AliExpress 2,AliExpress 3,Amazon UK,Amazon DE,Amazon NL,Amazon FR.

BEST RUNNER-UP:Chris●, the Moes ZSS-S01-THThis tiny sensor from Moes is perhaps the best model from the Tuya ecosystem. It reported temperature and humidity accurately without the caveats some of the other Tuya sensors had. It also accepted the reporting interval change cleanly, although I suggest you do this carefully as this device runs on a single CR2032 battery. Its small, rounded shape is one of my favorites in the whole lineup.

🥇BEST AAA SENSOR

Sonoff SNZB-02B

Zigbee 3.0

Temperature, Humidity

2xAAA

ZHA, Zigbee2MQTT

Amazon US
AliExpress

Also on:Amazon UK,Amazon DE,Amazon NL,Amazon FR,AliExpress 2,Domadoo.

BEST AAA SENSOR:Carmela●, the SONOFF SNZB-02BIf you prefer using AAA batteries instead of coin cells,Carmela●is my top pick. It measures temperature and humidity quite accurately, can be easily calibrated and adds dew point and VPD in Zigbee2MQTT as bonus entities. It’s quite slim considering the size of the batteries and comes with a string for hanging it up without a sticker. It’s also worth noting that the SNZB-02B uses a Sensirion sensor with a sampling rate of 5 seconds, which eliminates sudden spikes or drops in the measurements.

Honorable mentions:Junior●is the only sensor in this group with an IP65 rating, so if you need something for a bathroom, greenhouse, or anywhere with moisture, it is your only real option here despite being somewhat less accurate in measuring humidity. You can always calibrate.

Tony●is the smallest and slimmest sensor out of all twelve, so if size is an issue, consider the Aqara sensor. Even though reporting interval cannot be changed, it is accurate and reliable out of the box. Remember to go with the newerT1 WSDCGQ12LMinstead of theWSDCGQ11LMtested here, since it brings improvements to connectivity and network stability over the version in this comparison.

Further reading:10 Cheap AliExpress Zigbee Smart Buttons Tested and Compared6 Cheap AliExpress Zigbee Door Sensors Tested and Compared

 
 
AliExpress Reviews
 
 
Devices
 
 
Home Assistant
 
 
Sensor
 
 
Tuya
 
 
Zigbee
 
 
Zigbee2MQTT
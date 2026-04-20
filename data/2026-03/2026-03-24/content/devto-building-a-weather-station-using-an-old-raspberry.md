---
title: Building a Weather Station Using an Old Raspberry Pi - DEV Community
url: https://dev.to/nandofm/building-a-weather-station-using-an-old-raspberry-pi-5333
site_name: devto
content_file: devto-building-a-weather-station-using-an-old-raspberry
fetched_at: '2026-03-24T20:00:18.316214'
original_url: https://dev.to/nandofm/building-a-weather-station-using-an-old-raspberry-pi-5333
author: Fernando Fornieles
date: '2026-03-23'
description: For a long time I wanted to build a weather station at home because I like meteorology and for the... Tagged with raspberrypi, sideprojects, learning, community.
tags: '#raspberrypi, #sideprojects, #learning, #community'
---

For a long time I wanted to build a weather station at home because I like meteorology and for the fun of doing it. So I decided to stop waiting and just do it :-)

## Connecting the sensors

I wanted something easy to attach to my old Pi, a Raspberry Pi 2 model B+, that would let me easily read the data from the sensors. The Pimoron's Weather HAT fit perfectly with what I wanted:

* Just connect it to the GPIO interface
* Download and install the Python library provided by Pimoroni

Pimoroni has a good tutorialthat helps you build it and solve some of the common issues. There are alsoother articles from the communitythat are really helpful.

One good thing about this Weather HAT is that it is possible to connect a wind and a rain gauge. I don't have so much space in my balcony so I didn't get these sensors, but it is something that I would like to have in the future.

There is a good set of examples to read the data from the sensors and display it available in theWeather HAT's GitHub.

## The Challenges

But it has an important downside, the sensor temperature is affected by the Pi's CPU as it is very close to the board. So the temperature needs to be compensated, which is not as simple as applying a fixed offset as stated in the Pimoroni's tutorial. Instead I tried to apply a linear regression by obtaining the temperature from another weather station that, luckily, is close to my home.

Apart of installing the Weather HAT and reading the data from the sensors, the most important challenge was finding the best place for it in the balcony and how to isolate it from the external conditions, while at the same time allowing enough ventilation to avoid heat accumulation inside.

## Protecting the Weather Station from the Environment

Once I had the Weather HAT installed I used the following materials to place the station on the balcony:

* A transparent plastic lunchbox
* A base enclosure for the Pi
* Some adhesive protectors for furniture
* Some glue

Maybe a lunchbox is not the best solution but using a Stevenson Screen could be a bit overkill.

I used the furniture protectors to separate a little bit the Pi from the back of the lunchbox, this way the sensor has some additional separation from the wall.

At the same time I made some holes in the lunchbox to let the air flow inside to cool the Pi. I made some of the holes on the side where the sensors are located and the others on a lateral.

A few days later I noticed that, due to that holes, on windy days the measure of the temperature sensor can provide values a little bit lower than the real one. But I prefer this to having the Pi without this air cooling. I don't have the perfect materials, so I can't expect to have the perfect measures.

## Calibrating The Temperature Sensor

As I mentioned above the readings of the temperature sensor need to be compensated as it is close to the Pi's CPU.

The Pimoroni Python library for the Weather HAT has an attribute to set an offset that is applied to the device temperature measure. So I tried comparing the Weather HAT sensor values with the temperature provided by a nearby weather station.

What I noticed was that the offset to apply can't be a fixed value. The difference between the real temperature and the values provided by the Weather HAT was always between 12º and 16º.

To solve this I create a small script to get temperature data from both stations at the same time. With this series of data I was able to create a linear regresssion model to calculate the offset that should be applied to the HAT's device temperature reading.

It is not still perfect. When the device temperature is close to 30º the difference is quite high, but for the moment, it seems a little bit better than applying a fixed offset as you can see below.

In the next article I'll describe my Python learnings implementing the software to gather the measures, display it and sending it to an external system.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse

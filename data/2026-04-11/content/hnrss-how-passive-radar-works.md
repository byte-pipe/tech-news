---
title: How Passive Radar Works
url: https://www.passiveradar.com/how-passive-radar-works/
site_name: hnrss
content_file: hnrss-how-passive-radar-works
fetched_at: '2026-04-11T19:18:40.473758'
original_url: https://www.passiveradar.com/how-passive-radar-works/
date: '2026-04-09'
published_date: '2026-04-07T04:04:58.000Z'
description: Passive radar is radar that doesn't need a transmitter; it uses existing broadcasts of opportunity.
tags:
- hackernews
- hnrss
---

Passive radar is radar that works by listeningpassively.It doesn't transmit anything; it detects signals that already exist in the environment. By listening to how broadcasts like FM radio and digital TV bounce off objects, it's possible to determine their positions and velocities.

The result is a radar system with no transmitter, no expensive hardware, and no need for a broadcast license, unlike traditional, or "monostatic" radar.

## Radar's General Principles

All radar relies on two core physical phenomena: theDoppler effectandsignal delay.

### Doppler Effect and Doppler Shift

When a source of waves and an observer are moving relative to each other, the observed frequency changes. An ambulance siren sounds higher-pitched as it approaches and lower-pitched as it drives away. This is the Doppler effect.

Radar exploits the same principle with radio waves. When a radio signal bounces off a moving object (like an aircraft), the reflected signal's frequency shifts slightly:

* Object moving toward the receiver→ frequency increases (positive Doppler shift aka blueshift)
* Object moving away→ frequency decreases (negative Doppler shift aka redshift)
The Doppler Effect (
Source
)

The size of this shift is proportional to the object's radial velocity — how fast it's moving toward or away from the receiver. This lets radar measure an object's speed.

### Delay

The second measurement is simpler: time. A radio signal travels at the speed of light. If a reflected signal arrives later than the direct signal, that time difference (delay) tells you something about how far the signal traveled to reach the object and bounce back.

In active radar, the delay time is directly proportional to the distance. In passive radar, as we'll see, it maps to something slightly more complex, an ellipse.

## How Radar Works

Doppler Shift & Round-Trip Delay

TRANSMITTER

TARGET

TX WAVEFORM

RX WAVEFORM

Δt

Target Speed

⏸ Pause

Approaching

Receding

Transmitted wavefront (f₀) — 5 ripples, uniform spacing

Reflected wavefront (f₀ ± Δf) — spacing compressed or stretched

Target / velocity

Round-trip delay Δt

## Bistatic Passive Radar

Active radar ismonostatic: the transmitter and receiver sit in the same place. Passive radar isbistatic: the transmitter (e.g., an FM radio tower) and receiver (your sensor) are in different locations.

A passive radar receiver picks up two copies of the broadcast signal:

1. The direct signal— traveling straight from the transmitter to the receiver.
2. The echo signal— the same broadcast, reflected off an object (aircraft, drone, bird) before arriving at the receiver.

By comparing these two signals, the receiver extracts the Doppler shift (speed) and the time delay (path length) of the reflected signal.

## Bistatic Passive Radar

TDOA · Elliptical Isochrones · Illuminator of Opportunity

ILLUMINATOR

(FM / DVB-T broadcast)

PASSIVE RECEIVER

(listen-only, no transmitter)

DIRECT PATH (d₀)

REFLECTED PATH (d₁+d₂)

TDOA READOUT

TDOA (Δτ):

—

Bistatic range sum:

—

Bistatic Doppler:

—

Target Speed

⏸ Pause

▶ Right

◀ Left

Broadcast signal (illuminator → everywhere)

Reflected echo (target → receiver)

TDOA isochrone ellipse

Target

Thedirect pathis the baseline distance between tower and receiver. Thereflected pathis Transmitter → Object → Receiver. The difference in path length is what produces the measurable delay.

## Ellipse Delay Surfaces

In active radar, a given delay corresponds to a specific target distance, meaning a circle around the radar. In bistatic passive radar, a given delay corresponds to anellipsewith the transmitter and receiver as its two foci.

The delay measures thetotalextra path length: Transmitter → Object → Receiver, minus the direct path. All points where this total path length is the same form an ellipse. The object is somewhere on that ellipse, but you don't know exactly where with more data.

## Sensor Fusion: Solving Multiple Ellipses

One ellipse isn't enough to locate an object. But if you use multiple transmitters (or multiple receivers), each pair produces its own ellipse. The object's position is where those ellipses intersect.

Intersecting Ellipses (
Source
)

Two ellipses typically intersect at two points, while three will give a single location. This is the fundamental principle:more transmitters of opportunity = better localization.

In a dense urban or suburban environment, there are often dozens of FM stations, TV transmitters, and cell towers illuminating the sky from different directions. A well-designed passive radar system fuses all of these to build a coherent picture of what's moving overhead.

### Advantages of Passive Radar

* No transmitter needed.No transmission hardware or broadcast license needed. You're just listening to the radio.
* Low cost.The basic system can be built with an off-the-shelf software-defined radio (SDR), an antenna, and a microprocessor or computer.
* Legal simplicity.Receiving radio signals is legal in most jurisdictions. Transmitting radar signals requires licensing and compliance with power/frequency regulations.
* Covert by nature.A passive radar emits nothing. It can't be detected by the thing it's observing.
* Scalable.Low cost, simple off-the-shelf hardware, and no licensing required. Adding more receivers to the network improves coverage and resolution without any transmitter infrastructure.

### Disadvantages of Passive Radar

* Dependent on third-party transmitters.Users are limited to what happens to available to them in their area.
* Lower precision.Active radar can be engineered for specific resolution and range requirements. Passive radar works with whatever waveforms happen to be available.
* Complex signal processing.Separating the weak echo from the much stronger direct signal is computationally challenging. The direct signal can be 60–80 dB stronger than the echo.
* No 3D altitude information (without multiple receivers).A single receiver can estimate 2D position via ellipse intersections, but determining altitude requires vertically separated receivers or additional techniques.
* Limited range resolution.FM and DTV have limited bandwidth, limiting resolution to hundreds of meters. Active radar systems routinely achieve single-meter resolution.

## Why Passive Radar?

Ulimately, the reason there is increasing interest in passive radar is because it isaccessible. No broadcast license, transmitter, and newly inexpensive hardware makes radar available to consumers and businesses in a way that wouldn't be possible only a few years ago.

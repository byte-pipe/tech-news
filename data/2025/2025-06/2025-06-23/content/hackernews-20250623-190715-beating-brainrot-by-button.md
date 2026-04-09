---
title: Beating Brainrot by Button
url: https://www.romanklasen.com/blog/beating-brainrot-by-button/
site_name: hackernews
fetched_at: '2025-06-23T19:07:15.637921'
original_url: https://www.romanklasen.com/blog/beating-brainrot-by-button/
author: remuskaos
date: '2025-06-23'
published_date: '2025-06-22T19:42:23+02:00'
description: Preamble# The internet is the bane of my existence. Ads, distractions, sponsored content, bad news, bad ideas, more ads, social media, antisocial media, even more ads. Also, I’m a software developer, so the internet is basically indispensable for me, a central pillar of my income and a convenient way to communicate with friends, family, loved ones, associates, acquaintances, people from my sports club, superpositions of all previous groups and enemies alike. And I think my company runs ads, so in a way ads pay for my clothing and food and stuff. So I guess my current stance towards the internet would be somewhat neutral-ish, but that may still change.
---

# Beating Brainrot by Button

2025-06-22
What an effort to turn off the internet.

# Preamble#

The internet is the bane of my existence. Ads, distractions, sponsored content, bad news, bad ideas, more ads, social media, antisocial media, even more ads.

Also, I’m a software developer, so the internet is basically indispensable for me, a central pillar of my income and a convenient way to communicate with friends, family, loved ones, associates, acquaintances, people from my sports club, superpositions of all previous groups and enemies alike. And I think my company runs ads, so in a way ads pay for my clothing and food and stuff. So I guess my current stance towards the internet would be somewhat neutral-ish, but that may still change.

But I can try to reduce or at least moderate some of the negative aspects of the internet, especially those that keep me hooked like some sad addict: social media. I’ve tried completely blocking it via my networks’ ad blocker, but the animal in me circumvented that blockage by turning off wifi on the cell phone and thus doom scrolling galore on my cell plan. Also, my wife needs some social media for work or research (and of course guilty pleasure) at least some of the time, but she’s as bad in moderation as me. So completely blocking is not viable, but allowing unrestricted internet access to two reasonable adults is somehow also out of the question.

So the problem remained mathematically unsolvable.

Until today, whenNeil Chen posted a simply genius idea to hacker news. Neil describes how a smart plug is used to dynamically rewrite some ublock Origin lists to allow unfetted access to all content distracting. The idea is fantastic, but the implementation not practical for my/our scenario, so I’m adapting it here.

# Building Blocks#

I’m already using an network wide ad blocker via my gli.net router called “Adblock Home”. And for a smart home without internet access (see preamble) I’m using Home Assistant.

So we have:

* A gli.net router with Adguard Home
* Home Assistant
* Copious amounts of Zigbee Switches
* Some spare time

Surely there must be some way to wire those together haywire-ly.

# The Plan#

Just like Neil, I want some button to press to allow for access to social media, but only for a limited time (say 15 minutes). After that time has passed, my wife and me must endure a cool-down phase until we can push the button again (say one hour). So whenever we push the button, the filters will be disabled for 15 sin-filled minutes. A Zigbee enabled smart plug is adequately suited.

## Setting Up Adguard Home on the gli.net Router#

Adguard Home is very conveniently integrated into gli.net’s fork/customization of OpenWRT (formerly Lede, formerly OpenWRT). Frst, we set up the services we wish to block as custom rules. Sadly we cannot use the built-in services, because they don’t seem to count as “custom” and thus cannot be toggled on and off.

## API Access to Adguard Home#

Adguard Home has a fantastic API, available in OpenAPI yaml. You login to that API with the normal user and password. But: The routers main interface somehow bypasses the authentication, which means Adguard Home has no user/password which we could use for API access.This forum linkexplains how one can be added without breaking the existing integration. Basically, we have to add them by hand to the/etc/Adguard/config.yamlfile. Change:

users
: []

to

users
:

 -
name
:
admin


password
:
$2a$10$dXh72ZnexWPjxzRumXX2fOU2gwvPzqM8OZmcWZmFYl1WEiyhOMj2u

This password is the bcrypt hash ofadmin, but of course thats not the password I’m actually using.Use cyberchef to generate the hash.

## Home Assistant Integration#

Home Assistant comes with a functional, but somewhat reduced integration. It can however do all we need.

Among the switches it exposes is “Filtering”, which enables or disables application of custom filter rules. We can flick this switch via automation.

# The Home Assistant Automation#

After some trial and error, I’ve arrived at this automation, which as of now seems to work just fine and just like I intended.

alias
:
AdGuard Temporary Disable

description
:
Temporarily disable AdGuard filtering for 15 minutes when button is pressed

triggers
:

 -
type
:
turned_on


device_id
:
83c5ac94282a1e46dfb6b98a103dd9f8


entity_id
:
8fbcd8fb42be878036a203950084b125


domain
:
switch


trigger
:
device

actions
:

 -
choose
:

 -
conditions
:

 -
condition
:
template


value_template
:
"{{ cooldown_ok }}"

 -
condition
:
template


value_template
:
"{{ override_inactive }}"


sequence
:

 -
data
: {}


target
:


entity_id
:
input_boolean.adguard_override_active


action
:
input_boolean.turn_on

 -
data
:


datetime
:
"{{ now().strftime('%Y-%m-%d %H:%M:%S') }}"


target
:


entity_id
:
input_datetime.last_adguard_disable


action
:
input_datetime.set_datetime

 -
data
: {}


target
:


entity_id
:
switch.adguard_home_filterung


action
:
switch.turn_off

 -
delay
:


hours
:
0


minutes
:
14


seconds
:
0


milliseconds
:
0

 -
repeat
:


count
:
15


sequence
:

 -
data
: {}


target
:


entity_id
:
switch.steckdose_nous_zigbee_internetblock


action
:
switch.turn_off

 -
delay
:


hours
:
0


minutes
:
0


seconds
:
2


milliseconds
:
0

 -
data
: {}


target
:


entity_id
:
switch.steckdose_nous_zigbee_internetblock


action
:
switch.turn_on

 -
delay
:


hours
:
0


minutes
:
0


seconds
:
2


milliseconds
:
0

 -
data
: {}


target
:


entity_id
:
switch.adguard_home_filterung


action
:
switch.turn_on

 -
data
: {}


target
:


entity_id
:
switch.steckdose_nous_zigbee_internetblock


action
:
switch.turn_off

 -
data
: {}


target
:


entity_id
:
input_boolean.adguard_override_active


action
:
input_boolean.turn_off


default
:

 -
delay
:


hours
:
0


minutes
:
0


seconds
:
2


milliseconds
:
0

 -
data
: {}


target
:


entity_id
:
switch.steckdose_nous_zigbee_internetblock


action
:
switch.turn_off

mode
:
single

variables
:


cooldown_ok
: >-

 {% set last_disable = states('input_datetime.last_adguard_disable') %} {% if

 last_disable != 'unavailable' and last_disable != 'unknown' %}

 {% set hours_since = (now().timestamp() - as_timestamp(last_disable)) / 3600 %}

 {{ hours_since > 1 }}

 {% else %}

 {{ true }}

 {% endif %}


override_inactive
:
"{{ is_state('input_boolean.adguard_override_active', 'off') }}"

# After Thoughts#

So wait, can’t I still just disable wifi to continue the incessant pollution of my feeble brain with cat videos?

Well, yes. But this helps me exercise moderation, and like with any poison, social media is tolerable in small doses.

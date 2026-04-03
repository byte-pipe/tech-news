---
title: discord/twitch/kick/snapchat age verifier
url: https://age-verifier.kibty.town/
site_name: hackernews_api
content_file: hackernews_api-discordtwitchkicksnapchat-age-verifier
fetched_at: '2026-02-12T11:20:12.538799'
original_url: https://age-verifier.kibty.town/
author: JustSkyfall
date: '2026-02-11'
description: Discord/Twitch/Snapchat age verification bypass
tags:
- hackernews
- trending
---

# discord/twitch/kick/snapchat age verifier



age verifies your account automatically as an adult on any website using k-id



made byxyzevaandDziurwa, greetz toamplitudes(for previous work)



## how to verify on discord



itdoesn't matterif you are in the UK or similar region that
		currently has access to this, this will verify your account for the future global rollout in
		march aswell as current. to use, simply paste this script into your discord console by going todiscord.com/app, pressingF12, going toConsoleand copying and pasting and hitting enter on the following script and solving the captcha that pops
		up(typing "allow pasting" before if necessary):



// add a chunk to extract webpack's moduleCache
let webpackRequire = webpackChunkdiscord_app.push([[Symbol()],{},(r) => r]);
// cleanup the chunk we added
webpackChunkdiscord_app.pop();

let modules = webpackRequire.m;
let cache = webpackRequire.c;

// https://github.com/moonlight-mod/moonlight/blob/main/packages/core-extensions/src/spacepack/webpackModules/spacepack.ts
// helper to find a webpack module via code snippet
function findByCode(src) {
 for (const [id, mod] of Object.entries(modules)) {
 if (mod.toString().includes(src)) {
 return cache[id].exports;
 }
 }
}

// helper to find an object by its key
function findObjectFromKey(exports, key) {
 if (!exports) return;
 for (const exportKey in exports) {
 const obj = exports[exportKey];
 if (obj && obj[key]) return obj;
 }
}

// https://github.com/moonlight-mod/moonlight/blob/main/packages/mappings/src/mappings/discord/utils/HTTPUtils.ts
// find the discord api client
const api = findObjectFromKey(
 findByCode('.set("X-Audit-Log-Reason",'),
 "patch",
);

// send a api request to discord /age-verification/verify and then redirect the page to our website
const request = await api.post({
 url: "/age-verification/verify",
 body: { method: 3 },
});
const verificationUrl = request.body.verification_webview_url;
window.location.href = `https://age-verifier.kibty.town/webview?url=${encodeURIComponent(verificationUrl)}`;


(feel free to read the code, we made it readable and we have nothing to hide)



it should navigate to a link(or give you a link to navigate to), from there, you can just wait until the page says success



congrats! your discord account is now age verified.



## how to verify on other platforms (twitch, kick, snapchat, ...others)



navigate to the age verification page and choose selfie, from there, get the url of the qr code
		and put it in this input box, and press verify



verify



## how does this work



k-id, the age verification provider discord uses doesn't store or send your face to the server.
		instead, it sends a bunch of metadata about your face and general process details. while this is
		good for your privacy(well, considering some other providers send actual videos of your face to their servers), its also bad for them, because we can just send legitimate looking metadata to their servers
		and they have no way to tell its not legitimate.while this was easy in the past, k-id's partner for face verification (faceassure) has made this significantly
		harder to achieve afteramplitudes k-id verifierwas released,(which doesn't work anymore because of it.)with discord's decision of making the age verification requirement global, we decided to look into
		it again to see if we can bypass the new checks.



### step 1: encrypted_payload and auth_tag



the first thing we noticed that the old implementation doesn't send when comparing a legitimate
		request payload with a generated one, is its missingencrypted_payload,auth_tag,timestampandivin the body.looking at the code, this appears to be a simple AES-GCM cipher with the key beingnonce+timestamp+transaction_id, derived using HKDF (sha256). we can easily replicate this and also create the missing
		parameters in our generated output.



### step 2: prediction data



heres where it kind of gets tricky, even after perfectly replicating the encryption, our
		verification attempt still doesn't succeed, so they must also be doing checks on the actual
		payload.after some trial and error, we narrowed the checked part to the prediction arrays, which areoutputs,primaryOutputsandraws.turns out, bothoutputsandprimaryOutputsare generated fromraws. basically, the raw
		numbers are mapped to age outputs, and then the outliers get removed with z-score (once forprimaryOutputsand twice foroutputs).there is also some other differences:


* xScaledShiftAmtandyScaledShiftAmtin predictions are not random but
			rather can be one of two values
* it is checked that the media name (camera) matches one of your media devices in the array of
			devices
* it is checked if the states completion times match the state timeline


with all of that done,we can officially verify our age as an adult.all of this
		code is open source and availableon github, so you can actually see how we do this exactly.

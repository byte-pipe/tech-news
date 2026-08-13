---
title: 737 Chrome VPN Extensions Linked to Brand Impersonation and Browser Traffic Redirection | Socket
url: https://socket.dev/blog/chrome-vpn-extension-impersonation
site_name: tldr
content_file: tldr-737-chrome-vpn-extensions-linked-to-brand-imperson
fetched_at: '2026-08-13T19:56:17.353120'
original_url: https://socket.dev/blog/chrome-vpn-extension-impersonation
date: '2026-08-13'
published_date: '2026-08-11T23:00:05.332Z'
description: The campaign amassed more than 75,000 installs by targeting Russian-speaking users seeking access to blocked services.
tags:
- tldr
---

Back
[Research]
[Security News]

# 737 Chrome VPN Extensions Linked to Brand Impersonation and Browser Traffic Redirection

The campaign amassed more than 75,000 installs by targeting Russian-speaking users seeking access to blocked services.

* Kush Pandya
Aug 11, 2026
|
22 min read

Socket's Threat Research Team identified a campaign of 737 free VPN and proxy extensions published across at least 40 Chrome Web Store developer accounts, 274 of which impersonate 66 established VPN and privacy brands, that route the user's entire browser session through SOCKS5 proxies operated by a single provider. Socket analyzed the code of 525 of them, 522 from bulk retrieval and 3 more found during store enumeration; the remaining 212 had been removed from the store before collection and were recovered at listing level only. 520 of the 522 in the bulk corpus route browser traffic through the same SOCKS5 infrastructure.

The campaign has accumulated 75,486 installs across 737 extensions, of which 516 were listed as active when the corpus was collected, carrying 58,318 installs. Install counts are the Chrome Web Store’s bucketed display values, so these are sums of buckets rather than exact headcounts.

The campaign splits into three connected threat behaviors:

* Traffic interception:520 of the 522 retrieved packages setchrome.proxy.settingsto a fixed SOCKS5 server on port 1082 with a bypass list containing only loopback addresses, placing the threat actor in an adversary-in-the-middle position over all browser traffic.
* Detection evasion:104 extensions declare host permissions for Cloudflare and Google DNS-over-HTTPS endpoints, resolve their own proxy hostnames through them, and hand Chrome a raw IP address, so the victim’s machine never emits a plaintext DNS query for the threat actor’s domains.
* Subscription fraud:The paid tier advertises servers in Japan, Singapore, Canada, Australia, and Turkey. Not one of those 200 hostnames resolved.

Socket observed the client side only. The extensions place the threat actor in a position to read all browser traffic, and this report makes no claim about what the proxy servers retain or transmit. What is established from the packages and from public infrastructure is the impersonation, the undisclosed proxy configuration, the non-existent premium servers, the false statements submitted to store reviewers, and the post-approval code substitution.

The populations behind the numbers in this post:

* 737 extensionsin the campaign, published fromat least 40developer accounts.
* 734of those appear in the source dataset. The other 3 were found later during store enumeration, published from 2 accounts outside the original 38.
* 525were retrieved with code and analyzed: 522 in bulk, plus those 3.
* 522is the denominator for every code-level figure in this post.
* 520of the 522 configure a proxy at all. The other 2 ship no proxy code.
* 516were live when the corpus was collected and221had been removed.
* 212were never retrieved and are known only at listing level.
* 75,486 installsacross all 737, of which58,318sit on the 516 live extensions.

The same threat actor runs a subscription VPN business in Russia. Its published contract names an active, tax-registered self-employed provider, and its billing dashboard sells the browser extension as a paid tier. The extension estate is that business’ customer acquisition funnel.

Socket’s AI scanner flagging the suspicious behaviour ofmyxa vpn(aaeiefggdeljohngedhpmgidkjcdoebb)extension .

## What the Extensions Claim to Be#

The extensions target Russian-speaking users seeking to reach services blocked inside Russia, including Instagram, ChatGPT, and YouTube. 690 of the 734 extensions in the source dataset are Russian-targeted by at least one of three tests: a Cyrillic listing name, a Cyrillic manifest description, or a blocked-service name in the listing. 520 of the 522 retrieved manifests carry Russian descriptions.

Listings promise IP masking and traffic protection. One manifest inhfanmgjobgojpieocfemecgcgglmgpffreads:

JSON
{

 
"description"
:
 
"Скрывает IP и защищает данные, подходит для любых устройств и сайтов. Рекомендовано Юрием Дудём."

}

That translates to “Hides IP and protects data, suitable for any devices and sites. Recommended by Yuriy Dud.” Yuriy Dud is a Russian journalist with no connection to this campaign, and the claim appears in an extension from an estate that impersonates 66 other real brands. Socket found no public record of any endorsement.

66 real software brands are impersonated across 274 extensions and 38,140 installs, including Proton VPN, NordVPN, Surfshark, AdGuard VPN, Browsec, ExpressVPN, CyberGhost, Windscribe, TunnelBear, Cloudflare’s 1.1.1.1, and Google’s own Outline. Two impersonation targets are notable because they are the tools Russian users specifically trust to circumvent blocking: AmneziaVPN (22 extensions) and AntiZapret.

## The Proxy Hijack#

The attack chain across the 522 retrieved packages: a lure listing requests the proxy permission alone, resolves its proxy host by one of three mutually exclusive methods, and forces every browser request through a SOCKS5 relay on port 1082, while a first-install redirect funnels the user toward the paid subscription tier

Every retrieved extension that configures a proxy at all, 520 of 522, performs the same operation. Fromaabaifmlfkdolhdbbhjblkeekaijfdfh/worker.js:

JavaScript
const
 config = {
 
mode
: 
"fixed_servers"
,
 
rules
: {
 
singleProxy
: {
 
scheme
: 
"socks5"
,
 
host
: node.
host
,
 
port
: node.
port

 },
 
bypassList
: 
BYPASS_LIST
 
// = ["localhost", "127.0.0.1", "::1", "<-loopback>"]

 }
};
chrome.
proxy
.
settings
.
set
({ 
value
: config, 
scope
: 
"regular"
 }, callback);

BYPASS_LISTcontains only loopback addresses. Every other destination, for every tab, is forced through the threat actor's SOCKS5 node once the user clicks Connect. There is no per-site scoping and no split tunneling.

* 302 packages hardcode proxy IPs drawn from a single shared pool of 15 addresses, and 301 of those carry all 15.
* 104 resolve a hostname over DNS-over-HTTPS and hand Chrome the resolved IP.

SOCKS5 as configured here is a bare relay. It adds no encryption, sets no proxy credentials, and does nothing about WebRTC or operating-system DNS. 497 of the 522 requestproxyand nothing else; the remainder add onlystorage, with one exception each foractiveTabandnotifications.

Everything the extensions do not see, the proxy does. With all browser traffic forced through it, the threat actor’s server is positioned to read every destination, every TLS SNI value, the victim’s source IP, and any request body sent over plain HTTP. For a user in Russia, source IP plus timestamp is identity-adjacent, because an ISP can resolve it.

The connected state renders the word “Защищено” (“Protected”) in 67 of 91 extensions in one code generation.

## Would a Legitimate Service Look Any Different?#

At the mechanism level, no. A browser-scoped VPN has one API available to it,chrome.proxy, and a fixed-server SOCKS5 configuration with a loopback-only bypass list is the ordinary way to implement one. Any extension that proxies browser traffic necessarily places its operator in a position to observe that traffic. A provider building a genuine censorship-circumvention tool for Russian users would produce something that looks very much like the code above. The proxy hijack is the capability, not the finding.

What separates this campaign from that hypothetical is everything around the proxy. A legitimate provider competes under its own name; 274 of these extensions impersonate 66 established brands, including AmneziaVPN and AntiZapret, the two tools this audience specifically trusts to get around blocking. A legitimate provider does not advertise server locations that do not exist; all 200jp,sg,ca,auandtrsubdomains across the 40 apex domains tested return no A record, and those are exactly the entries markedpremium: true. A legitimate provider does not ship a paywall that cannot be satisfied, or an extension hardcoded to fail every connection behind a working connecting animation. A legitimate provider does not submit nine byte-identical justifications to store reviewers stating "No data transmitted to external servers" while shipping a proxy. A legitimate provider does not add an entire remote-configuration layer after approval, in a build whose reviewed predecessor contained none of it. And a legitimate provider does not write an internal manual telling staff never to put a domain intochrome.proxy.settings, only the resolved IP, so that the destination cannot be read out of the shipped package.

Each of those is a choice with no operational benefit to a service that intends to deliver what it sells. Each is documented in the sections that follow.

## DNS-over-HTTPS Blocklist Evasion#

104 extensions declare host permissions forcloudflare-dns.comanddns.google, then resolve their own proxy hostname before configuring the proxy. Fromabjgfdfbmmijjdfbohbhgdnjeipjbplj/worker.js:

JavaScript
async
 
function
 
resolveProxyHost
(
node
) {
 
if
 (node.
useDnsResolve
 === 
false
) 
return
 node.
host
;
 
const
 resolvedIps = 
await
 
resolveDomain
(node.
host
);
 
const
 hostToUse = 
pickRandomIp
(resolvedIps);
 
if
 (!hostToUse) 
throw
 
new
 
Error
(
"Не удалось получить IP адрес сервера"
);
 
return
 hostToUse;
}

The resolved IP literal, not the hostname, is what reacheschrome.proxy.settings. No plaintext DNS query for the threat actor's domain is emitted whileuseDnsResolveis true, which is its value in every shipped node list Socket examined.

resolveDomainqueriescloudflare-dns.com/dns-queryand falls back todns.google/resolve, caching results for five minutes and selecting a random A record. This technique is documented, not incidental. One extension,kcplchjjdpgehfdlggggoohdeoaikcan, shipped an internal build manual titled “Промт для сотрудников” (“Prompt for employees”).

The internal build manual the threat actor shipped inside a published extension, addressed to employees, with its project domain field filled in asskyproxy[.]space.

It contains a project domain field filled in withskyproxy[.]space, a country-to-subdomain mapping, paste-ready implementation code, a pre-delivery checklist, and a section listing what staff must not do:

Не ставить домен напрямую в chrome.proxy.settings — только IP после резолва
Не использовать домен из другого расширения без отдельного указания

“Do not put the domain directly into chrome.proxy.settings, only the IP after resolution.” And: “Do not use a domain from another extension without separate instruction.” The second instruction compartmentalizes domains across extensions: no extension may reuse another’s. The effect is that a takedown of one domain does not reach the others.

## Remote Configuration and Domain Rediscovery#

66 extensions chase HTTP redirects at runtime to locate whichever threat actor domain is currently live, then pull configuration from it. The excerpt below combinesresolveAssetsOrigin()and thefetchLandingLinks()call that follows it.redirect: "manual"lets the code read the 3xxLocationheader itself and follow it to an origin that is not hardcoded in the package, which means the threat actor can relocate destinations for already-installed copies without shipping an update. Fromabjgfdfbmmijjdfbohbhgdnjeipjbplj/core.js:

JavaScript
fetch
(
LANDING_URL
, { 
method
: 
"HEAD"
, 
redirect
: 
"manual"
, 
cache
: 
"no-store"
 })
 .
then
(
function
 (
r
) {
 
var
 target = 
LANDING_URL
;
 
if
 (r.
status
 >= 
300
 && r.
status
 < 
400
) {
 
var
 loc = r.
headers
.
get
(
"Location"
);
 
if
 (loc) target = loc;
 }
 landingLinks.
assetsOrigin
 = 
new
 
URL
(target, 
LANDING_URL
).
origin
;
 
return
 
fetch
(landingLinks.
assetsOrigin
 + 
"/config/links.json"
, { 
cache
: 
"no-store"
 });
 });

Following those live redirects exposed a domain tier that appears in none of the 522 retrieved packages:myxavpn[.]site,myxavpn[.]online,myxavpn[.]tech, andmyxasafe[.]space.

## The Paid Tier Sells Servers That Do Not Exist#

Every extension advertises premium locations. DNS resolution shows that the free-tier subdomains resolve and the premium ones do not. Forstealthpath[.]space:

* us[.]stealthpath[.]space:178[.]130[.]47[.]43, 178[.]130[.]47[.]44, 178[.]130[.]47[.]50, 147[.]45[.]60[.]241
* de[.]stealthpath[.]space:80[.]92[.]204[.]47, 185[.]252[.]215[.]97, 185[.]252[.]215[.]98, 80[.]92[.]204[.]33
* gb[.]stealthpath[.]space:5[.]180[.]30[.]15, 5[.]180[.]30[.]122
* fr[.]stealthpath[.]space:86[.]104[.]74[.]110, 94[.]131[.]118[.]39, 94[.]131[.]118[.]237
* nl[.]stealthpath[.]space:80[.]92[.]206[.]84, 194[.]150[.]220[.]163, 45[.]89[.]110[.]227
* jp[.]stealthpath[.]space(no answer)
* sg[.]stealthpath[.]space(no answer)
* au[.]stealthpath[.]space(no answer)
* tr[.]stealthpath[.]space(no answer)

All 200jp,sg,ca,au, andtrsubdomains across the 40 apex domains tested returned no A record. In the shipped server lists, those are precisely the entries markedpremium: true.

The paywall has no working unlock path either. Inhfanmgjobgojpieocfemecgcgglmgpff/sw.js, one of the 88 packages built on thesw.jslayout, the entire license check is:

JavaScript
function
 
hasPremiumKey
(
key
) {
 
return
 
typeof
 key === 
'string'
 && key.
trim
().
length
 > 
0
;
}

Any non-empty string unlocks every premium server, and no code anywhere in that group of packages ever writespremiumKeyto storage, so the paywall cannot be satisfied through the extension's own interface.

A second generation ships a hardcoded secret with a non-cryptographic hash presented as a license signature. Fromladjabmcgadeknpfngdihgeimccmgmpj/src/core/tokenVerifier.js:

JavaScript
const
 
SECRET_KEY
 = 
"myxavpn2024secret"
;

function
 
generateSignature
(
data
) {
 
const
 combined = data + 
SECRET_KEY
;
 
let
 hash = 
0
;
 
for
 (
let
 i = 
0
; i < combined.
length
; i++) {
 hash = ((hash << 
5
) - hash) + combined.
charCodeAt
(i);
 hash = hash & hash;
 }
 
return
 
Math
.
abs
(hash).
toString
(
16
).
substring
(
0
, 
32
);
}

That is a 32-bit rolling hash of thehash*31form used by Java'sString.hashCode, not an HMAC. Secret and algorithm both ship in plaintext, so any user can forge a permanently valid token offline.

That secret appears in 10 extensions across 10 separate publisher accounts. Seven of them split it across variables to defeat string search:

JavaScript
const
 part1 = 
"myxa"
; 
const
 part2 = 
"vpn"
; 
const
 part3 = 
"2024"
; 
const
 part4 = 
"secret"
;

## One Extension Cannot Connect At All#

ilpcglpcfdeoehcmjhkfhhgpldgfgjhj, published as “Burёnka VPN”, advertises servers in seven countries. Its server list contains 15 entries pointing at a non-routable address, under the threat actor’s own comment:

JavaScript
/* Extra dummy locations (closed) */

{
id
:
'it-1'
,
name
:
'Италия 1'
,
location
:
'Рим'
,
host
:
'0.0.0.0'
,
port
:
1082
,
countryCode
:
'IT'
,
premium
:
true
},
{
id
:
'es-1'
,
name
:
'Испания 1'
,
location
:
'Мадрид'
,
host
:
'0.0.0.0'
,
port
:
1082
,
countryCode
:
'ES'
,
premium
:
true
},

Not one server in the package is markedpremium: false, so no free tier exists. And the connect handler is hardcoded to fail:

JavaScript
if
 (msg.
action
 === 
'ROUTE_APPLY'
) {
 
sendResponse
({ 
ok
: 
false
, 
error
: 
'SERVERS_CLOSED'
 });
 
return
 
false
;
}

Every connection attempt returns failure regardless of which server the user selects. The package ships a complete fake interface, including a connecting animation and status indicator, over a proxy engine that cannot function.

Itshomepage_urlis a Telegram bot deep link carrying a referral code, the only thing in the package that reaches outside its own interface.

## Evidence of Deliberate Policy Evasion#

aaeiefggdeljohngedhpmgidkjcdoebb/background.jscontains a comment recording the threat actor’s expectation that the behavior violates store policy, alongside the code that ships it anyway. The comments below are verbatim from the file, threat actor's own included. The Chrome Web Store line translates as: "If Chrome Web Store rejects this because of automatically opening links, we can replace it with a notification offering to go to the Telegram bot.”

JavaScript
// Открываем Telegram-бота при первой установке

// ВАЖНО: Это происходит только один раз при установке (onboarding процесс)

// Popup расширения открывается только по клику на иконку (не программно)

// Если Chrome Web Store отклонит из-за автоматического открытия ссылок,

// можно заменить на уведомление с предложением перейти в Telegram-бота

setTimeout
(
() =>
 {
 
// Открываем Telegram-бота в новой вкладке

 
// Примечание: Для chrome.tabs.create с внешними URL может потребоваться разрешение "tabs"

 
// Если возникнут проблемы, можно добавить "tabs" в permissions в manifest.json

 chrome.
tabs
.
create
({
 
url
: 
'hxxps://t.me/myxavpn_bot'
,
 
active
: 
true

 }).
catch
(
(
error
) =>
 {

Four lines later the same file notes thatchrome.tabs.createwith external URLs may require thetabspermission and that it could be added. It was not added. That extension’s shipped permission set is["proxy", "storage", "notifications"].

## Post-Approval Code Substitution#

oaidiemgjmaabehcfjfbkeifdpeniemmaccidentally shipped a 1.5 MB archive namedvpn-bez-limita.zipinside its own published package. The archive is that extension’s superseded v1.0.0 build, meaning the artifact Google reviewed. Comparing it against the live v1.0.1 shows the entire remote-configuration layer was added after approval. In the reviewed build,resolveAssetsOrigin,fetchLandingLinks,refreshRemoteQr, andconfig/links.jsonappear zero times. In the shipped build they appear three, three, two, and one time respectively.

The manifest difference between reviewed and shipped is only a version bump and the store’s automatically addedupdate_url. The permission set stayed["proxy"], so a permission diff between the reviewed and shipped builds is empty. Campaign-wide, 49 extensions across 18 publisher accounts received post-approval code updates, covering 8,076 installs, and 31 of those are still live.

## Coordinated Review Gaming#

10 extensions shippedstore-assets/PRIVACY_JUSTIFICATIONS.md, the justification text submitted to Chrome Web Store reviewers. Nine are byte-identical, SHA-2561dea4975f7aaba71bf7821fcf62deca470ef5e21f45c947b103ddeb836ef9b81, across nine separate publisher accounts. The document asserts “No personal data collected,” “No data transmitted to external servers,” “No user tracking or logging,” and “This extension does NOT use remote code.”

## Infrastructure and Attribution#

The 737 extensions are one operation. Six independent classes of evidence establish it.

The extensions declare it themselves.360 of 522 retrieved packages, spanning 34 of 37 publisher accounts, render a string in the popup naming their own supplier. 330 readPremium доступ предоставляет официальный VPN провайдер Myxa VPN, “Premium access is provided by the official VPN provider Myxa VPN.” A further 30 readКлюч предоставляет официальный VPN провайдер Муха VPN, "the key is provided by the official VPN provider Муха VPN," using the Cyrillic spelling of the same brand.

The popup of an extension branded “Лев VPN” names Муха VPN as the provider supplying premium access, states that one of its twenty locations is free, and shows the remaining nineteen as locked.

One build machine.43 packages shipped abuild-info.jsonthat leaks the threat actor’s Windows build path:C:\Users\ollob\OneDrive\Документы\1.myxa-work\08.06.26\<domain>\<product>\<product>-release.zip. One Windows account, one project directory, extensions published under many different accounts.

One analytics account.Eight Yandex Metrika counters partition 49 threat actor domains with zero overlap. Counter108155174is installed onmyxavpn[.]pro, the commercial storefront, and on the extension-farm landing domainsvpnmyxa[.]site,vpnmyha[.]shop, andvpnkomar[.]space. A Metrika counter ID belongs to one Metrika account and reports only to it, so the same counter across these sites indicates shared control, linking the subscription business to the extension estate. Webvisor session recording is enabled on the landing pages.

Bulk domain registration.21 domains were registered inside a 10-second window on 2026-05-20 between 07:30:35 and 07:30:45 UTC. A further 14 were registered within 24 seconds on 2026-04-05.

One registrar and one dedicated host.The estate of at least 102 apex domains sits on the nameserver pairns1[.]reg[.]ruandns2[.]reg[.]ru. 43 of the first 51 resolve to a single IP,212[.]192[.]14[.]75, running nginx 1.24.0 on Ubuntu. Reverse-IP lookups on that host returned only campaign domains, which is what allowed a further 51 apex domains to be recovered from it.

One build pipeline across two code generations.The byte-identical comment/* finalize_ext: auto-open premium URL on first install */appears in 26 extensions across 20 publisher accounts, in bothsw.jsandworker.jsfiles, marking a generator pass that appends a secondonInstalledlistener.

The brand is «Муха VPN», Russian for "fly." Rendered in Latin lookalike characters the Cyrillic «Муха» becomesmyxa, which is why both spellings appear across the estate and why the domains read as they do. It also explains the naming scheme:myxavpn(fly),vpnkomar(mosquito),zhuknet(beetle),tarakanvpn(cockroach),pauktun(spider),sverchvpn(cricket),osavpn(wasp),shershvpn(hornet),korovkavpn(ladybird),usachvpn(longhorn beetle), andgusenvpn(caterpillar). One domain,maskirovka[.]space, takes its name from the Russian word for camouflage, also a term of art in Russian military doctrine.

### The Contracting Party Named in the Public Offer#

Russian law requires a public offer to name the contracting party, andmyxavpn[.]pro/oferta/does:

Настоящая публичная оферта ... является официальным предложением самозанятого
(ИНН [redacted]) ... о заключении договора на оказание услуг VPN-доступа

That declares the provider to be a self-employed individual, identified by a 12-digit taxpayer number. A 12-digit INN is issued to a natural person, not an organization. Socket checked it against the Russian Federal Tax Service's public self-employment (НПД) taxpayer-status service, an endpoint that exists so businesses can verify a contractor's standing before contracting and that returns status only, with no name attached. It confirmed an active professional income tax registration. The endpoint rate-limited after that query, so we obtained no negative control against an unregistered number, though the response was specific rather than a baretrue: it echoed the queried number and named the exact tax regime. No company name, registration number, address, or director is published anywhere.

Two things are established. The threat actor published this number as its own contracting party, and the number corresponds to a live tax registration. A third is not. Socket did not resolve the number to an individual, did not attempt to, and does not assert that the registrant is the person operating this campaign. Self-employed status in Russia can be held on another party's behalf, and nothing in the extension code or the public infrastructure settles that question either way. Identifying the person behind a published taxpayer number is a step for a party acting under legal authority.

### The Business Predates the Extensions#

Certificate Transparency datesxray[.]myxavpn[.]comto 2024-11-06, the earliest issuance anywhere in the estate and roughly 14 months before the first extension in the dataset, withmonitoring[.]myxavpn[.]comrunning Grafana from 2024-11-27 andgit[.]myxavpn[.]comhosting self-managed source control from 2025-01-05.myxasecure[.]spaceadditionally carriesjitsiandrockethosts, meaning self-hosted video conferencing and Rocket.Chat.

### A Second Proxy Tier for Paying Customers#

app[.]myxavpn[.]prois a Telegram Mini App billing dashboard sellingEXTENSION,PRO, andMAXplans. TheEXTENSIONtier is priced from 99 roubles per month and described as “VPN in browser only.” Its bundle hardcodes exactly one Chrome extension ID,aaeiefggdeljohngedhpmgidkjcdoebb, in asub_type === "BROWSER_EXT"card and a setup wizard. That extension has 2,000 installs and is live.

The threat actor sells the browser extension as a named subscription tier from 99 roubles per month, on the same page that advertises no logging and no unnecessary permissions.

The dashboard’s CSP header exposedsub[.]myxasecure[.]space, a domain absent from all 522 retrieved packages. Node configuration for it was recovered on 2026-07-30 from five public V2Ray aggregator repositories that had republished the threat actor’s subscription output, showing VLESS-REALITY on port 443 rather than SOCKS5 on 1082. Socket did not purchase a subscription or connect to a node, so the paid tier’s operation is unverified. The protocol difference is the point: VLESS-REALITY is built to survive the deep packet inspection that blocks VPNs in Russia, while the extension estate ships the plaintext relay.

### The Privacy Policy Contradicts the Product#

An earlier version of the threat actor’s privacy policy, published onmyxavpn[.]comand archived on 2025-12-14 as version 2.0 dated 20 January 2025, cited Russian Federal Law 152-FZ, committed to processing personal data on Russian territory, named Roskomnadzor as supervisory authority, and stated that data is disclosedПо запросам уполномоченных государственных органов в установленном порядке, meaning “on the request of authorised state bodies in the established manner.” The current policy onmyxavpn[.]pro, effective 1 January 2026, contains none of those four provisions. It is titledПолитика конфиденциальности — MYXA VPN | No-logs VPNwhile stating that it processesТехнические данные — IP-адрес, an IP address.

A service sold to Russian users specifically for censorship circumvention advertises no logging on a page that records IP addresses, and until recently published a commitment to disclose data to the authority responsible for that censorship.

This is a compliance posture, not a state connection. Any Russian-registered data processor carries comparable obligations, and Socket found no indicator of state sponsorship or tasking anywhere in this campaign.

## Impact#

For each affected user, while the extension is connected, every request passes through a server the threat actor controls, in a position to read the full set of destinations the browser reaches, the TLS SNI value of every HTTPS connection, the user’s source IP address, and the complete contents of any request sent over plain HTTP, including credentials submitted to non-HTTPS sites.

Whether the threat actor owns those proxy servers or resells capacity from an upstream provider is not resolvable from the extension code. If it resells, a further party is in the same position.

The victim population makes this material. 94% of the campaign targets Russian speakers, and the inducement is access to blocked services. These users selected a privacy tool specifically to protect traffic they consider sensitive, and the product routes exactly that traffic through infrastructure controlled by a party they cannot identify. Extensions impersonating AmneziaVPN and AntiZapret reach users who deliberately sought a tool they had reason to trust.

Users who purchased a premium subscription paid for server locations that did not resolve at any point during this investigation.

## The Enforcement Gap#

Google has acted on this campaign. 221 of the 737 extensions have been removed from the Chrome Web Store, including 14 of the 15 that Palo Alto Networks named publicly on 2026-06-05 and that were still live at the time, every one of those within seven weeks of that publication. Removal is a deliberate act by the store, so the campaign is known to it. What the removals did not reach is the other 516.

Normalizing every live service worker into a code skeleton, with comments, string literals, numeric literals, and whitespace removed so that branding and server lists cannot affect the hash, produces 93 distinct skeletons across 409 live workers.

One skeleton has 51 members spread across 8 publisher accounts. Google removed exactly one of them,ofbdlgcpfnhcidmfmddnkkbkejjoffdf, which carried 37 installs. The remaining 50 are live and carry 3,217 installs, and every one is structurally identical to the extension that was taken down.

Among those 50 isilbpmeeaifiojjiohfffjmgpgcfcaajg, published as "1.1.1.1 VPN" and copying Cloudflare's branding outright. It is live, with 1,000 installs and a 5.0 rating from 8 reviews, and the store surfaces no warning to a prospective installer.

The Chrome Web Store listing for a live extension impersonating Cloudflare's 1.1.1.1

The account economics explain the persistence. A Chrome Web Store developer account costs $5. The 38 accounts in the source dataset cost the threat actor $190 and published 737 extensions, which is $0.258 per extension and $0.00326 per surviving install. An account publishes a mean of 9.1 extensions before its first removal, then continues and publishes a mean of 15.8 more over a further 69 days. 28 of 29 core accounts kept publishing after their first removal, and 29 of the 30 accounts that have had an extension removed still hold live extensions. Extensions are removed. Publishers are not.

Palo Alto Networks published on part of this campaign on 2026-06-05, naming 18 extension IDs. All 18 appear in Socket’s set. Three had already been removed before publication, and 14 of the remaining 15 were removed in the seven weeks after it. The 15 publisher accounts behind them retained 250 live extensions carrying 26,151 installs, andsverchtun[.]store, named in that brief as an indicator, still resolves and now fronts ten proxy IPs, eight of which are on ranges absent from the fifteen Palo Alto listed.

## Recommendations#

### For Users#

Remove any VPN extension from this campaign immediately and confirm that Chrome’s proxy configuration has returned to normal atchrome[://]settings, searching for “proxy.” Change credentials entered on any non-HTTPS site while the extension was connected, and treat browsing history from that period as observed by a third party. A browser extension requesting theproxypermission can redirect all traffic; it is worth confirming that the publisher is the brand it claims to be before installing, because 66 real brands are impersonated in this campaign alone.

### For Developers#

Extensions that requestproxywarrant the same scrutiny as extensions that request<all_urls>. The permission is narrow in appearance and total in effect. In this campaign the permission footprint stayed["proxy"]across a post-approval change that added an entire remote-configuration layer, so permission diffs alone do not detect capability changes.

### For Security Teams#

Block the network indicators below at DNS and at egress. DNS blocking alone is insufficient against the 104 extensions that resolve their proxy hosts through DNS-over-HTTPS and pin a raw IP, so the proxy IP ranges require separate handling. Blocking SOCKS5 on port 1082 does not affect the VLESS-REALITY tier on port 443. Inventory installed browser extensions for theproxypermission and alert onchrome.proxy.settingsmodification. Cluster candidate extensions by normalized code skeleton rather than by extension ID, since this campaign regenerates variable names, function names, and comments per build, producing a unique file hash for every logically identical file.

Socket’sChrome extensionprotection analyzes extension bundles for hidden data flows, undisclosed credential exfiltration, and C2 backdoors, blocking malicious extensions before they reach user endpoints.

## MITRE ATT&CK#

* T1176.001 Browser Extensions
* T1557 Adversary-in-the-Middle
* T1090.002 External Proxy
* T1572 Protocol Tunneling
* T1071.004 Application Layer Protocol: DNS
* T1102 Web Service
* T1656 Impersonation
* T1036.005 Match Legitimate Name or Location
* T1204.001 User Execution: Malicious Link
* T1583.001 Acquire Infrastructure: Domains
* T1583.003 Acquire Infrastructure: Virtual Private Server
* T1585.002 Establish Accounts: Email Accounts
* T1608 Stage Capabilities
* T1027 Obfuscated Files or Information

## Indicators of Compromise#

### Network Indicators#

* myxavpn[.]pro,app[.]myxavpn[.]pro(billing dashboard, Yandex.Cloud,158[.]160[.]228[.]178)
* getmyxa[.]com,app[.]getmyxa[.]com
* myxavpn[.]com,app[.]myxavpn[.]com
* Post-redirect tier:myxavpn[.]site,myxavpn[.]online,myxavpn[.]tech,myxasafe[.]space
* atlasvpn[.]space
* bezopasnet[.]space
* cipherway[.]space
* cloudmask[.]space
* echosecure[.]space
* gusentun[.]space
* gusenvpn[.]online
* horizonguard[.]space
* internetprvpn[.]ru
* ironproxy[.]space
* korovkavpn[.]space
* maskirovka[.]space
* murvpn[.]space
* myxasecure[.]space
* myxavpn[.]space
* neoncloak[.]space
* netroutehub[.]space
* nimbusshield[.]space
* osavpn[.]su
* pauktun[.]space
* primeproxy[.]space
* routekeeper[.]space
* routeshield[.]space
* salega[.]ru
* securepulse[.]space
* shershvpn[.]space
* shieldtunnel[.]space
* silashield[.]space
* skorostvpn[.]space
* skyproxy[.]space
* spidervpn[.]online
* stableproxy[.]space
* stealthpath[.]space
* sverchtun[.]store
* sverchvpn[.]space
* tarakanvpn[.]online
* tunnelbase[.]space
* turbotunnel[.]space
* usachvpn[.]su
* vaultvpn[.]space
* vpn-myxa[.]ru
* vpnfasters[.]space
* vpnkomar[.]space
* vpnmyha[.]shop
* vpnmyxa[.]site
* zenshield[.]space
* zhuknet[.]online
* zhukvpn[.]online
* ns1[.]reg[.]ru
* ns2[.]reg[.]ru
* 212[.]192[.]14[.]75
* 103[.]35[.]189[.]225
* 103[.]35[.]191[.]173
* 147[.]45[.]60[.]241
* 147[.]45[.]60[.]252
* 178[.]130[.]47[.]43
* 178[.]130[.]47[.]44
* 178[.]130[.]47[.]50
* 178[.]130[.]47[.]129
* 185[.]252[.]215[.]97
* 185[.]252[.]215[.]98
* 194[.]150[.]220[.]163
* 45[.]89[.]110[.]227
* 5[.]180[.]30[.]15
* 5[.]180[.]30[.]122
* 80[.]92[.]204[.]33
* 80[.]92[.]204[.]47
* 80[.]92[.]206[.]84
* 86[.]104[.]74[.]110
* 94[.]131[.]118[.]39
* 94[.]131[.]118[.]237
* 138[.]124[.]244[.]206
* 130[.]17[.]1[.]19
* 78[.]153[.]155[.]112
* 81[.]90[.]31[.]73
* 95[.]163[.]244[.]138

### Hardcoded Signatures/Credentials#

* REALITY public keyOCLtjVdRxsou3429LRfjkDYgiAPs24TSgSeFZpChCEw
* short IDd67ec5a8fc40ebea
* Recovered from third-party aggregator republications on 2026-07-30 and not verified against a live node.

### Extension IDs Live in the Chrome Web Store at Time of Writing (516)#

1. aabaifmlfkdolhdbbhjblkeekaijfdfh
2. aaeiefggdeljohngedhpmgidkjcdoebb
3. aalfhjflaokihbediiadmohipjlpbjpg
4. abjgfdfbmmijjdfbohbhgdnjeipjbplj
5. acdihpjgbhodcikbhikhhgkafmbbmemp
6. adbicacljgblmefpmcffdjmcbagbejji
7. adjnaekfhknjhcagnejdcfelbjdcfjgj
8. adpkfblbeihmbjljeffbaklklgofcgae
9. aeglpahooigfloknbcocdkgoklmopcad
10. aemjnabgfabjlcojhbablmedhbnmpcgj
11. aepcimhlmbgpilgmhgfkfjlgbdkdojdd
12. afpiijfkjbkkfoeepflocpfcmghcohfi
13. ahdpgkmldfnmpcpoamhabhoohdjgijak
14. ahfjipgfgnjpkoacdlbaaimodjpiafod
15. aikeingnnaofblajmpkdamcmbinjicek
16. ajjgfffcnelajekhpgnfhhehpjokkkjh
17. akiknpephpgdllpnmocndocdmgmbnocl
18. albcebpejhogeakalalkmkhhhcofehme
19. alcopdbbehlpelbaaglhlgljkkljkppi
20. aliegnhhiklfkdipafafcjafgngecmgn
21. ameimpcdjkiacjmfefadfkjbmicohmff
22. anconclhkknnbkgiflfeppbcdoikcpca
23. anggbncfkojnpldcpblaboandcjajkgl
24. annffnminbfjdifcgbadjdgcaglpiemj
25. aocipbpjojijjlmopppdnkhmnfaeobol
26. aoejfgbdcbpeekpmelgoofbboonmdcaf
27. aojolglblgegdlejhldpeadnglkcheba
28. aophoakdkaldkckgkgionphohmkhnkom
29. apgingficohkcjlkejipioacokkehnph
30. apkfclckpilgfoembfmnmlblnffcnfcl
31. apnlidgccohighgjjikmalpccgombonl
32. baabjhdplplmihlnecgjajjdllllfhhf
33. balkhnoegkmheodonbkhkaegibmamapp
34. bbcgolpihcpibnjpnafbaccaclagclmf
35. bbddibpbffgafehfljibecnppcamoogn
36. bbjoeckmegkklkmlgihgebeiocmjhfpf
37. bchelkjkilnlomoehihopndkjjhlcgla
38. bcmmkekghfmaglecpmbmfidmmpljmbia
39. bdbhokpcdfeoljjcfdegkdapplhknpoj
40. bdmnomiahkddoogbipkleodejnplcppj
41. bebcfnddlcnahgmdobbicnjbahlbgpnh
42. becdalghcachfljkdifjaifmiecbpbcb
43. bejjplkelkkcpnaaicfpdenfpcpbpnod
44. bfdlendomdpckfcegjjhgheignejhing
45. bfgoepnoenodpgmcficdjlajnlbmadlc
46. bfhmomelpcmpdjdeohpeemfgikbdoijl
47. bfjcdcgfehgbbaenfojebonnlfichjnk
48. bgikeajhdmggllhdnleoeaiedpbdhbgc
49. bieapdakjafmcilgjobfeopeoejhdmmg
50. bifgpflmljboegdapmikafhpilijdead
51. bimjbbjnldbimpihljgakoidmgcnmleb
52. bjfngoeclhbkpgdngfdolcpiofgdlbjm
53. bjpgehkaonlndnoohmlelkjlchccdigb
54. bkmmedhfnenchphbngpihpcodlimdceb
55. blagooekjnebejejmikhahgfejlbeoie
56. blcnhjlbnldiopfekjpcmpcieipiokdl
57. bmeonhjbmiacccakpjdmjaloiflkjgig
58. bmidlejanhnaaopgiljgojghplnaeoaf
59. bmldimmhaamlfaijnmhikfidngaennjo
60. bnfedobijcachmijlfecldmhnebihmcj
61. bngahmjkkbiebggdghdlbjaedhmcblpm
62. bnnjeanokjfhhkohkaoghfclocnhpcia
63. boembakcfchlnhkfpjeolgpfpegmejmm
64. bokpbehobhpfpmamodkngkaljfmimmpa
65. boomffhhbgombjkbeakkdjiphjkillpb
66. bpcpgflbnnedjfcnkfbinikeicffghgl
67. bpfjljidmejoeamagnfbknmhehbmagbd
68. cabdahinacflcaaagobghohleefogogk
69. cahbelonbpjbgolckchmbpdlgeglgpof
70. capnggjhnpofmimlcjlhggdenibcgoal
71. cbmjaknklmcgajkfocjagjmdkeinfchm
72. cbpfihfjeleikcpadajchoebgfblalid
73. ccnceaompinfjgnfkbcnfgaenklmafil
74. cdlbcpjfhjedjajilmpknbmodmfocljm
75. celjebeafmieepphodddabmegonmanoo
76. cepookalkohkjhbamenfbagblnmfcfmn
77. cgajlbgdapgeohppnnhjemoodaakmplh
78. cghconplclhlafnkaocbddboklfodnfc
79. choldfdafblhjjfdbnibekaakmhnfabc
80. chphemgbhggblnggogackapgdnifnjco
81. cieikfpbkhkjfjaoijonmhnmodnnhgdo
82. cihkgekjnagficdlaicladlfdodlodji
83. cijkehnfggjlcjlijaichfjbokalnleo
84. cjadklbhkckhkgnlbllaelbfjjcgenfj
85. ckicpgoimmcplbdeblgkcimhchdkkmlg
86. cklafdlhkgikkkfoojcgjodehbdbakpa
87. clcpecjofmjiapknnccnflcagbjdeccf
88. cldooaldimmjpalhfppedmgbnocajian
89. cljopkopbidboafoppejamlcpmgmffib
90. clonlklkobdppgnhaklminjfgchpgiob
91. cmdlencelhcjbebnkpbmhcfmlnjgihhm
92. cmoljkcobacohfilkhbpclpgebcnpdcl
93. cmplhaampagiakkffmgjndcjdgbglbln
94. cnjgicfipaihakphpbcgdklcbpnkbndm
95. cojkbijephcnagbbbkecebeoplnlgana
96. cpehmglkieogiogkgbicjmoapfjooaam
97. cpjmmnhmieannhjnjjfcpmkpjgnakjaj
98. daefdbcalhpfoajkdeeobdamapepkdde
99. dbcocmghepfnpobmefmdhmahefdmmkmi
100. dbjeemabemccjbbemlnljmpmaadhohho
101. dcbpngicdpgdlehimeoidnebieifgncf
102. dcdengcnfioodmmjlkjhomeondebpjcj
103. dceikamljmmhdjagikodokbkdmbancpb
104. ddhhghnfnfjppofkhcndimaeohofbanc
105. ddhjjndlmjakdcdcmgajploledaclbfk
106. ddlnpmihnbdfhmiefebbogipmemmachh
107. dejbkoamefcdbolpcpppeblbmbkdljmo
108. dfbnmnokochbcifabpndhfelgobckenh
109. dhehohioamlbamodmibbdbondgbbpkpb
110. dijdbcdjngogkbpgldngbflblkbkicla
111. dinnpahadcfmggceljnhjdopgepbalno
112. djddlpkdagnbgokmielahcpgigepgdam
113. djibkmimcjaphppiekhbkpccfhlhhfbj
114. djocpdcnegafiajdaglloibfjifhbhbp
115. dkdnckncggmlaokepcnaobhflpbadame
116. dlaeopfffpngikkaccaknkmdgjdianin
117. dlaonnkmgmchbmlbngepgioejjmglape
118. dmadpoocbhhfaeefeblecpaielloalme
119. dmanadmmigdmihoejnaaflfkimdlhjeo
120. dmpmpkfbhilmjgbknadklnflbbbfocmi
121. dnfdiamfhbaaicacdfmjhkfhedolbjfg
122. dnmppgaamaeejibkgadfbmnpofmgnegf
123. doapacnhgcnojfakmppeapngneienlhl
124. dpbilbpinfjkhciajdcifndlpegepokc
125. eaelfbmpnoaiefdgejnhblfhihagcbmo
126. eaidghdeobijblnliakpildffnjdckmd
127. eaolghfmnajoaejicijdbpkicimmomcn
128. ebfkhmjpdjojecendlbkchjohblodlob
129. ebjhmhgfpinecniajgjkhaocfodmldnn
130. ecffkedpjhecoeeedbnembkgihnaoelk
131. ecggfjeponcknddgikfdjngocbpmkhdo
132. eckjcmcaanooipfdjhjihhidfidkflep
133. ecnmodkmpeeebpcnlpmnieamegokkhab
134. edakhofdfkcdhnmcjaacekhfgochaceo
135. eeaagbioaaiigjehofojbeacmcpmfggi
136. eedcgiifhajonmlllcnajaodhicfekna
137. eemheamahbooefoojcalafcadhebljfl
138. efcmmhjhcjaabofjhpfmgidljpplkean
139. efpnbpbclmfblbkicgpipnehglciohce
140. ehfnbbjmgkeelhemgpkfdhojcjmfpkjp
141. eijcacggdeflehoekbdgljongmobmchj
142. ejagecejffbgaefchihnmkdkchknkigf
143. ejpngffggkahecooncogchbchpngfokj
144. ekagjpmdcapijgpldiojceionmnleifj
145. ekocnfhifehpgiffogacoboddbkfcjhi
146. ekpicjaibbcffjfenpffjkifhiehcbfm
147. elflhijmcekbfdjkabgphiepeclgmjgl
148. elleedljbbeipjijfgahpmbmojgagkjk
149. elmjnebeklbicphkoceklapimjjjicjj
150. emankpkmfimhfhilhgfmmhgahcmhihbh
151. emaondhcbbhipmjggpanmiicfniaokbn
152. emfdpideeoagljccddpegdicpcgkledf
153. emihdfbdahahdhgpkodehgpngmeajldp
154. emkbmmhneldhbgpkaomgjjohdcfeapbj
155. emlifninekjhlmmhioileilfdijfmaoe
156. empmomhbifkbcfbodchbakclkinpibim
157. enclhmjiadiphdbnpkdhkelcahjnnhcp
158. endajcleplnkbilblmifdhpimfaonkff
159. eojakckjemdnoffmlfnonhfkmmkigpdj
160. eomimmpkgdmeckpghogemcmkimcpigeg
161. eomjcbhempdcpmljiahjenbdhkoccbmb
162. eoolgeaiphoeoeldlmcholcdgdkldoem
163. falfcccfjmagebegdiaoiimndpdlmihh
164. fbjlnjmpfnofkpjfabnilfkmlggindnh
165. fboaaaegndmojaphabbmpgiohgnhekhd
166. fceapcpbffpckedagfekofkljbnjjgfb
167. fcmecilpdddmffmnjhdmillmddahmfnh
168. fdamefgbggbbpbplfcjhggmabomdmedh
169. fddcfopnhojdhijpfmllhieoecbckhlp
170. fdgndkeabepnjiohbabfnchdkikaeoik
171. fdhjfohpmnliieiimdncnheflacobldp
172. fdoagnpcpgkjkcmnpnmdlbikfdagklhk
173. fecohheohodkgmdmdpiocogboienindc
174. fephkdkjkfcciljffkakepiefhmeikpm
175. fgdmoacjelpcghceahplbfgepnmlgnna
176. fgnnpafmckdabkmgopdkkcnmenfmahkm
177. fgpeadkjhdhaefcfkacbjniapclmbehi
178. fhggcomokafcmghkeknnoogghkkalchb
179. fhhimhicabffjclofbpjhkbnfdjmdmpj
180. fibohcmbdjkkapkbjfhkaoiljaofeoil
181. fiiegliakbailegmmgdpjfodaeheabjm
182. fkbhohfcljmmgohbhkccejcamibgmjlg
183. fkejoibgeglangndghmgghminjaheled
184. fkhpnpeaadfbcgnbbdgnkmgihfpdmpkd
185. fkiglandkaeajdjehelgkmnndonnffan
186. fklahklbgkgpaildaegmojabhngniomb
187. fkmbekmghpabdjfobhpbnmpakibmfecm
188. fmaimhhbpnbpbeomifcdpiigfhbgeajj
189. fmgongfibgfdkeabifkfkibkohdmahop
190. fmjlnpepggmfdipfdafghiepgnaoadmd
191. fnmoomkicfdelpdhkahfcbenclcbmnnd
192. fnonmdajnijmkceinkipcijkgnbkejaf
193. fokpelagppjmjiggfdalkfepcfclhnoh
194. fpiolkbhpmebbdpanjfmnoacpkkdgbel
195. gahjhehnlghhgolhbonlbgahjikidgla
196. gaijfdefjhclenikcaggjoblodfchmge
197. gbmbmldgodcjbfaghnjohphndkobjpce
198. gchgkghlgpefkoepkpjdgmlcgnbblppp
199. gchhlaonopipkknacbdepodlighedgkj
200. gckefkbaglmdpmjndciiahaccljdddai
201. geemjpmbdjffghkkiileoiheccgcjilb
202. gefgdocdopdafjahbieblleicllnhadp
203. geoalbipaogceeldlkhfnapeifhelefj
204. gfdajcpakgecmiglfhfnojmebkfkfhgi
205. ghedgpchgenefpjfjokdnlohlmbaoidb
206. ghifhappieiegcliblajaeidkidecedg
207. ghjfmhihfoplmefplnojpiobcoinddhj
208. ghpeepgmgdeabaimackjmkfafcdfmkai
209. giojogndbceodalhnddnebbkamhfenon
210. gjliplciiocpaocblnhjjacpebbomjda
211. gkojbiedppcceclalkijhfbmobckhpea
212. glaofpkjfaldpdgjapcfhccagmddmjnf
213. gmagolapbbobcclmbmfgkdfdgcjiijjp
214. gmhpfinejackkjoanceabgmoiggofanm
215. gnfpgncjogpbomifiegijoikfpjpoole
216. gnignaonemjabnmmfjkilpfodbfgacfk
217. gnjllochjiomjfeaageimhmfkplcghem
218. gpdkajdgppoccfpeocndflnlmjemalfh
219. hahjmhffophbcglolcpnpfpiacfdejcj
220. haomlginkkjmocfonpiknfghoeomiojc
221. hbchogodnlgpdafoeobeffknfmdlnofo
222. hbnndancicgofckmcmndglbfkdfebngj
223. hcaldgnpjniegbmfdoooceicdcfpcdgj
224. hcipkekemlgahjnkclcjlpegemcgabmm
225. hcmacpiikhfghbaflobmdecddbnjlgfp
226. hfanmgjobgojpieocfemecgcgglmgpff
227. hfaoffgdhhicckebnkgbakidhjnjpfic
228. hfbhplpckgfkhfcepgbejnjpanbbaaed
229. hfdejdcbgacglcafiobfkpnnmjdhmaed
230. hfmkkjaibgegmmfihchilhlffabegina
231. hfofepaldicokklmfgdonaaakebggnkb
232. hgbinhfdcidmbpfnmgekpbmomohmnnnp
233. hghdgfijkoaenalonnlldjggmakkabfe
234. hhebjfghjolapmbfpjeppcchgglanfgh
235. hhoellcfchiefblhjebgkgfgedcmbbmj
236. hiohnobfeiimhgcjfkifogdlegijjhcl
237. hioijncdgkhopehidnimbdealonncjbb
238. hjahmlbhpfnnfiklidkmjemaoghepioj
239. hjcldbjnjeajfjnfakafbihnkcahipjd
240. hjcmoncnppobhjddaghaklfkepgaejog
241. hjmjmbiaafeggmgadknfbkeehppmhejk
242. hkbhihfbcjpgpeipblibipaflmpleipk
243. hkekfldddpkkfnedjfiiajkodgcacfck
244. hkknofgppcaphiolocpkdljneopbmccf
245. hkpmehimmmbnkjhijfpblfcfdmdolmgb
246. hlahebdnafgbfeggppedlncpkkhofhfk
247. hljeddeaafolhinnpdlbbjcjaoegkpeg
248. hlnlameikmglaccgijanmlbocjcgcidn
249. hlonjnobegeknhcnplaifmbgmbalneji
250. hmemnljhamnbcnphkjdphnmnggmnhhkl
251. hmklcckkmciijdfaaifpmcgfclgdnmbg
252. hmnpiaijfkaoecnpckcfjjkdlajnonbh
253. hmooknfodfbbncnhncnednnkiommggpj
254. hmpjdeippjapohpkmalhmnohbipnggjf
255. hnembaemjbciokbnhklbcngopfakpkeo
256. hnhlhlnbgjocolmlecblbbpbhdacjmdd
257. hnkdnicapamolkbngbhpkoebelhoopkk
258. hnpgpecddlepclmbfpimdholohmhpiej
259. hobopaghoileeibgbnfofpoaggheplbf
260. hoeghcokeoglleffagcmajogjkgeinjc
261. hohlchlcjnnhjghnkhlpdemkhoenfoea
262. hokmanlioejijlfedacchmnekagoikia
263. hoooffkckfkdcmgpoebehchcdekmaebl
264. hopicaedkhenimddfhgnjbicdfibnphk
265. hpgghhpnkoamfbhiihfachccnkdlkiog
266. hplendamjldnefdlfdplecalljeghjpe
267. iaoeadecnampefdibdmjjbojfoajpfde
268. ibmaolbkpicpijpjecobinipoddeiogn
269. ibphkcpmadfdpbkockccopbibhbdijna
270. icjnjndpfkjjlhdcbigakplonifnhnpk
271. ickldhbificbikdaaljpcddekdmngjjc
272. idmpkfamcdgdhlopbiapnoaklgkjigle
273. idokdbnfljhpfecndlapankpgpkkgipd
274. idpnkgklpceoeabneppjgffcidokneif
275. ielobapmcgolalpmbagemlcnpljochfg
276. ifohhcbccciphedicdbedaomdhblnhob
277. igjfbdhfpnmbbiegnnlhhokbdpoglmba
278. igmoflgphnlpcbeedabbhcpppklkkdeb
279. ihbbgdnjojleljhjpenkkkbfbkhmaned
280. ihbmgokcocjiihdmjkeblefcpbgeefkk
281. ihedhalfchhcihjnadfocilbhfjdjool
282. ihldefkgpnceoelikkacpffhabnhfdpm
283. ihpdbailkcljcclemifagdnfmgpfnfbi
284. iibaohbndjbhmoahmcdaeegolenbnenc
285. ijidomgpacjmolpdobebnkocnogkphpp
286. ijilplnnjkjklkmhbklfnpnlnjpbfaie
287. ijldnndgkkdkglbpneecjeedmnhklflh
288. ijpbkjknnkpjnkndfgddfflpoickilmf
289. ikaiigidedfhichcdloodfefkjbpbdak
290. ikhhkmiondfmmjbcdicamfefbcemfboh
291. ilbpmeeaifiojjiohfffjmgpgcfcaajg
292. ilhkddenpjglbamfkdfcggplilcibono
293. illoljcjjjjmblealplijcjkedjlkdfg
294. iloeambbfeeikpjhkpfcbcplpobgapel
295. ilpcglpcfdeoehcmjhkfhhgpldgfgjhj
296. imbkobcmkpefeijlpgejkpnfgbjmlaoo
297. imkgekneolafjpdgcbdagelgfcdobmlp
298. inddaiiphfojbihdabkdnlpjehfkklhp
299. ingmjmajmmhjmdnbhjkljhelcibnemnc
300. inicnjibhgoomjmdkddcmmnpamfhpghb
301. innjppfndpgigpnoicbofacmdpiblmge
302. inolfjdmfnnikdnaagcocajchnccmaio
303. ioncbpcgiobadmnelbcpgpjphenddfoa
304. ipdncmifipjgangkhjjjfccojkccmefd
305. ipjfgibgeafohhadcicgcgongehdliam
306. ipmbpleekpckaonmiggklgoicdihkmml
307. ipnjgkeodmakngjpblfmcggkcknalfam
308. jaccgfagleghffhjbcaoambohejmpaoh
309. jcamehlleiidiiogfddjclbihkamnmdb
310. jdpifpbmifchldljpapckejcnohbiada
311. jdpnclabfdjckoggcihhcfphomgcmfib
312. jefnljneijhahhfffilpmfpofhgigkhd
313. jfdklphafjochadainoobkemnogdjiod
314. jfdplfcifokiabbglfjeaanldjohogfd
315. jfidepmfcigpkopoeemkididegkldkfh
316. jggpbfpigiemlipemocnijhapgoaflac
317. jgmokihhodhebpmcbamcjgjbpkngngap
318. jjibkaphagoijhdmkllmcndemnidhjjd
319. jkekfaejgkokhbcahfmhiiecgkkkfhpa
320. jkjkpdjjonmobllfkdmdmlkabpomangm
321. jocbfpcnadgeceidpapkoggmhkieeeeg
322. jofoajnimljekbjgjdpbnicnfeegbfbg
323. jogoelgdgekiljmmcalimblkcmoklkdo
324. joocokeldmkhhgaaalkjnomkpldkdocn
325. jpepkkccakbnijjjdblbmpijloibdlfl
326. jpgmhchadlmpjjdgolpdhgooglpaiogf
327. kalljebjhmecngplogckjaodbfbjgden
328. kaonoofcdglmjidkpokanpbjfdbfhamk
329. kbokjhkoeadabeccjgohejbipkggopbo
330. kcgghkhfblccdcdeeeljkohccimahmfj
331. kclcmhakfncbaklinnijihiinbkoajed
332. kcnfinfcncpdokmfgpaggilhcpddfekn
333. kcplchjjdpgehfdlggggoohdeoaikcan
334. kdfigodfnafejgecidbhkjlgdokkiiig
335. kenamdfaobeijnoclgegcpoplfahlemh
336. kfdikbdfpdnnhhdedadeaodglioggjdl
337. kfginhcclblahoolnpjkhgkmgfjbkcao
338. kfodnmcfkeekobieebijkjclpbdeenjp
339. kfohlaofnppmnelheedlkiamijfaikci
340. kgjjaibkhlddbmmnhndcnpoimeidlgba
341. kglhlmkedfjgbfhleoifbnjhblmjbphg
342. khaoknlphonpaimkkeepehffbkgobdjc
343. khclfeijkmglgdildaognklghbefbpal
344. khefbhanpeicefjhlogailkalglhdlea
345. kidhjgofjnmjpbdhagacohdggmdfcgfl
346. kiefglobgcfoolkfjkopcnopaagpohlc
347. kiijehifnnlnchkfgmlokakpfiooeigk
348. kjbelgiekopnehkjmcpoiiopmfhbcokn
349. kkdlgdmmmankljhaagicfhjhnajdpnfm
350. kkejncpdhhnfmdebmpaacbcmgglkigdb
351. kkfkknaikhhjojoidojlenioadfjecof
352. kkkldlbbknfdbpalmknkdalimjeadpen
353. kkmkaknfcdcpjfjlmfhbpeoijikfoneh
354. klmkbfdadoijkjkinfbbncmmoepeibek
355. knblpijcogopeankegmbcdhdndbplgka
356. koakjgkbcddoofklajpgeidodbanoijk
357. koidiemmmedgpiokggpfilalabjoadmg
358. kojpkekfanejpfmildijmgmapdgepddn
359. kolbfeikmmkkdolnkopohocflhpokajp
360. kpmgcdgnpkbfajhgbmagkaccibnekbdm
361. ladjabmcgadeknpfngdihgeimccmgmpj
362. lbaphifcdembobfoannnpogppkacjkhk
363. lbbnpjbbepimfemibkhddfklekaipjli
364. lbfendfngigjmpghcidgnodlecdlhkbk
365. ldhmimnchgkihniijggnhcanhphillnn
366. ldijhinlhpiiooiknndjjdolhnpihbel
367. legdfnahnoeicgljlooibgkjphfaploh
368. leimopkbcijhhkpaigamminemckeihko
369. lepioojbimojjnjkbflbbhlfoamimfdm
370. lepocfhpmichhobjfkdpkglpfmfkpbfd
371. lfadaehpomkfpaikipnlicfnncpifekm
372. lffiompnfgklemcbinkmogbjeiaifehb
373. lffokgmnkdhhcbfdemgjjlgpohafchnc
374. lfmkljhfpjpcoeghgomhemecbcojikai
375. lgjplckjkndnoedomdpbhhjgiopmblnj
376. lhmcjeognjknaapdledgjglikmhhcoan
377. ljhgojgbkjkhbalonkdonmgfdoepggcp
378. ljhmjpdmdnjngejchnmhlapogengkfog
379. ljjelnoeccjlckaoifeifjjlabnnbbed
380. lkcpbhmegkfjfhjehobbbbgkgaogkofl
381. lkmnpfajdejfdbfjiaealafmogipbapk
382. lkoncffoonijombbicbdoekimimjdhif
383. lkpckmkognddjdhnoadepmgniifnfhek
384. llidhpjmhdejdndndciohlhnkggkpjdo
385. lmagpmnilkpgdcbkmokechmpeeojangi
386. lmcppmbdhnaehfibpnhddklfjijnkkep
387. lngiojmnaemlbhahccmnohemajgjgimb
388. lnmkicmjchoonmpmfpkjlbiejkepdjmh
389. loieafdhaendcpnbpcjmchfnochbhcio
390. lopjckeffpljbofkaldmojbbjlkjdfcf
391. lpccdlpnagkhpglgcchidglcnoinhpji
392. melcllbcepoakpgccapphgiilfefclfp
393. mfapmkkleedaafigeeianmkfklamafaf
394. mfcaneeehggllfdnekaicinjidbbongi
395. mfjnlfbefioeckkmmfahkgmhgneepgll
396. miiolehfoldajjpfjcnajmalaojhjaoa
397. minbmnlpjbikmghooidgekahhooailhm
398. mipkffkddlldacbaljecppmjbejccnli
399. mjaifaojoefepojcljhdhibkpklfnbgo
400. mjaohgnbjbllcofbefddknibhiciblen
401. mjbdamnianlifhiamjcooecfdakpofhl
402. mkamgofgnhollhpgpiaifcjhffkhgndk
403. mkkolkbehgnknpmdcjbcgjpnmeegijim
404. mldhnfajgpmjhdcfjobajiiinnaajbma
405. mllhkekmhgbdenahmkolmkijipddhbnn
406. mllilecdlobbninpgokpjdemejfnkela
407. mlndifgbehammhhbecgfcpbcbmnfhooe
408. mlpegpimkonipjfhidmimjahlocgobop
409. mnffeimmicacieajjchanficccikhjhj
410. moechpfgdfbhngeolclpkomehjnfefgc
411. mpfokndmajkflgkbjjkmgcnkkoebelab
412. nabfdkbbclgbgegiahpobbmgahdjnida
413. naeknendfcmljedoehenpefacejdhjal
414. nbeelbioffbjkkgapjdpfcckiannldej
415. nbenpghhoknfjfjlibglllggjkhaofba
416. nbnhggmmgochbcphpjjbahngkpnelcic
417. ncdgmomaanghnglcjhmhbbianeaddcnf
418. ncoffmoodfnohnphcmidgncknpkgnccj
419. neobejhblpcbllkbcpeanhjggoelleme
420. nfcmnfjkkoiaojgiejjikhcohjefccll
421. ngohccekcogognbibjfipmpckfnincli
422. nhdjjcfgikohckacbdjcailhbnbbinjk
423. nhknddogcpmenomfpndcdcgocdkdhmmo
424. nibfakjomhepipjboakgjnnddeeeebeh
425. nilachbkggkoalbfogpkckojjdhlnjho
426. ninkfblhapgjffbmpmimemjicdghkdgg
427. njmlahdnjgafdichmdlafnlbckkpidic
428. nkggmkmcfgeagjpfenkhmpkgpefmdddi
429. nledalnomibdlfljakdcffgbpmkhjdfh
430. nllfmbmeibkjhdidkhnnpbblneepaonh
431. nmcnfhmlonpkabmmoepefcokljhelkoe
432. nmnbdhlcjapghglbagbagmideiggpnfi
433. nolgiichhgmkpjklgdohbbhkndmeommm
434. npgglgmhjabcncbhlpgblgbhajjabjcf
435. npminpkniohlengkpngnepjllnfapelj
436. oahhlpegbadgngdcpiemcjcnpokkocfd
437. oaidiemgjmaabehcfjfbkeifdpeniemm
438. obabhcfakmfmaaankblgkjpinodphbjd
439. obhdgfnkodjcnnhpjjmlgmcngmbciimc
440. obihdinidoplbiplglecalaokeekjion
441. obincfamamnccblhgjimnbegglcfmiok
442. ocbpehjjgkamhchhclbdabhenpghggfb
443. ocjopfjjaphkoagcfdmdgpheobhccmfp
444. odmonkfcgpfigghfgnngaeibckgjbjce
445. oebcbpokjkoooddmcokcjjoijcgnjoic
446. oeddabhhipaomblagaohfjfcikjacide
447. oekjbffiagclhfkpphmcheihchifblhp
448. oemjchklfcneghomigfkdeoleglhgocp
449. oepemfmcinfdgpdfcleghpkbhkhhpmkl
450. ogbcnckfiabjkgofnkmohmjabcadcpjj
451. ohciibhlgjnckamdhelbjgggcdaifkbf
452. ohimcmgcbkcjihmfdddgomhdjbjihchg
453. oilnfanklnlkllifgedkeeefcfenenpf
454. oiofghlphpdioamgoakbafcgalhgodjh
455. ojgfehdbhgbicajidmgiidpceockbbpn
456. ojgndfedcnfkmohdcafiilpcenifhijd
457. ojjdfjlckplkkaphcpblafonbhoofddi
458. okijglemboebajkjkfnkfkjldfeahflk
459. okkofhfjhogmdagdpokjcfclbgeobhmk
460. olbjcieaiekojooccadpemmnofapfngl
461. olnedmfbogpgbkphdbfednoagdlmamin
462. omdbnfgeiodifpcndelahincimhbooae
463. omkjdbggfhniomedkgdcoimmpolbiddl
464. ommmigkmgbilkbggodbipeffbjdbcook
465. ommpoiidlmdogdmcchcdhaknjjmobldb
466. onapalbennofmmiojkillockmddkablp
467. ondmhoohnlhclemilldijfdmlfkonfip
468. ondnmmgphffljlhdiifpplebjmfbofho
469. onjinbkkfllnmlliccceepfccihgecdh
470. oojhemfejdefafjanamoiefplimjamdf
471. opcoiilfeelpihhomeaoebehlcdihjid
472. pakgnemmpanbkmjapomefhloemiagfjm
473. pbecllekjbdgokpkfmgaggfmghfdipkn
474. pcbdkbipnfmfjfimjjbpeifhobgakeoa
475. pcccndbpgahfnfmlmlhnkmgncapdjklf
476. pcoepiamkidpfnbacbncjpcdgcgcofmd
477. pddhejgmgakilndagfaffgochjojogfp
478. pdokibcpfcjgjekalneegknionpagbmk
479. peaphjkfgmagbgebncdjcfnmbpfiknci
480. peegmjemnahkkbmkddeiiodljofeajmp
481. pfanfinmoljafbhjbjdebbdnjmfmiimd
482. pfljadblahfjooobcgeomagleeoaapbl
483. pfnpmpldgnnlfkgefcbkohhfiiacegea
484. pgajoncdggainfbdmibbgmoaahkccmkc
485. pgcjglcfamomceaphhbmmhlbkbcmmhke
486. pgcoppepfmchejpcekpmhhofikokmbak
487. pgdehgjcmgedooamahelcjeoghbnhmek
488. pgegfnolipocfakkldnkommjffijfejf
489. phadahcflgdgodfbndbommabigemebhl
490. phbhemngopbmijocapkgabcojjhmpnpd
491. phhddamodjfancgfhllllmieebbjjhpk
492. phmnnmciicaeaahifbonpkklhiddkdbb
493. pikjoibppeflfnaheajejhnckamihaeg
494. pkebmfenadkbamndhkmfliminhmhhgnf
495. pkfhbfgbceeilepkfiiceedbhlanmmjj
496. pkjnnicnapmkdflpbbfhnnhbcgchgbcm
497. pknicmfnmeaohdeacagcpcggnjcfefld
498. pkojndcnfhneclhkfjopplcanpgaoppo
499. plciffedekbipeophpkkjlilcdfnnkic
500. pllfcoakeflgbkedpkjgeglpijbcglfa
501. pmfbomilkmcfpnpgbdodmdbgapghehef
502. pmglclpkploapkijijgpncnaomgbagmm
503. pmijocfokgjlcmhahdcpdenipeemhcog
504. pmmneeeipikleggeclkinacjcjnegfbm
505. pmohoeododoachjkhdlifkmgoihmffij
506. pnjimekgccmbpclgakplkoficlhnomln
507. pnlgcjdpkjbacmgcbaciffijdkpdjmib
508. poaelinlofhkopdifffhlkioaojgfjge
509. podahboddjjbggldcbiigapfjdcemmdd
510. pofmhdlbfflfkigmjhhhclnehmebifaf
511. pogjiffghedegfekjhgkbjfkhpbnnclo
512. pomcnpapjbiblifjdekoogkognehkipp
513. ppbbocbdhdnedkdlaoohkpbafmbpljpa
514. ppiakigckgnocnmoenndpgbehmccapjb
515. ppjnfdpomlboeahlcacaenjnhfjbhlcn
516. pplibppgnmomfcnoclechnebccniooai

### Extension IDs Delisted From the Chrome Web Store (221)#

1. abmnmjngddnfgpkckfpcmachndiblkai
2. adjmddmkpidciominakpmljkkkfojaac
3. aebkpogjiagpdoebfilngdeagmiflebf
4. afejcloehmeaccaeacgpjnempifmdfba
5. afemiapijjhoibpkibjnenncgjpdenii
6. affkhnifjpajdeknlemiaiaeholimlfc
7. afihdhiiaahfoknbendimbniipbnapmo
8. agjjimpmdlmfnpimcpakodojfemdabid
9. ahccfcbbkabkjociggoocnapoleahbjf
10. akibiigkdhioejdgkeophiphkpdhmice
11. almdngpalkpacjoeffkhacdjjimijjnf
12. amohbpndmbcjecjnghhaeeanohiflfpj
13. anpnhjikkhcoaaflifchcaenbpfagipo
14. aplalcbelkdpnaejdfoeiecapielmdif
15. bacdbkogecilnnoldgfnobbikoiaaogg
16. baplpdmklmmegpjkalhjbafmhllpbgoi
17. bbmchmaaanigpalemaffenhmjbfigkal
18. bdhibenbhfhanmigebagkodhnmdocfon
19. bdjgofkgmknndiijclikbcklmnjdhagi
20. beadcellenlepfbkpoggklacilaealbb
21. bemgcabkbgfjffgjejmhkhgpkijpbbdc
22. bflmbcbnlhjenjebjgbbfmocaaeihlcn
23. bfoiajdjmbdhjeepbndhjenekaalkbeg
24. bgbabcbfnphklneccpldeecbnpogpbfn
25. biobgdechobmiadhmlkmopcfodhcliae
26. bkdlpaakbacdeblhhfdfdgllcomicgbn
27. bkfidmboiaddjdjnbohgidbccdabbiml
28. bmmklkcamkknmajnhcmigbhgpahapodk
29. bmnlapbemjklfmplcmdknejeoppabiji
30. caahmphonfnhadohfmkcgoeefmeoacfk
31. cabcelkjclaoimjobhbldhlknjppicgi
32. cblofljellnafddcomjdlbjnenfadije
33. cciccaljijgfeabbkplijgphfmijompi
34. ccnaehfdahmalkmfhgalgccffbmholki
35. cdfajacnjbaigbjnpdjeeapephdnoeng
36. cdkbhfedgceelpoghnklefgdfknaclne
37. cfpgbcmpclfbnljaidlanimkkmchfadd
38. chlkfcilfifdlmlmjinjeinpibgpegap
39. cjdafpdojamncegfmbconlicklgepidc
40. cjdfocfccgmbbpcdnahldpglkgkbhcae
41. cjhkcmdhkdjgdmgldfaggkjcomhoeeen
42. ckblbnbcgnggegagibeanhiaacplnafm
43. ckhgbopnpmlhgiihmclcobcdehcakoai
44. cmfbmehojkikkfdellcpieaapccgemdl
45. cnhenidimbfnjlnkphiombphhljihlpp
46. cnlciplbfbidjehlmifabihnjnalknoj
47. cojanaohoolhlkfkcmekifeeobdmgpab
48. damiijeinijdbjcchpddhfkgcfbdeiao
49. dbljpjjbnffplmkhciloejochjoikcoa
50. demlogledllmlgcjcecjedkiodimijhm
51. dfmojkadneadomhkgmipjdghcooalmad
52. dgkglcdncbenpdookdibjmigcdpkebne
53. dinengjknebdlmaabcldoeangcgjdpck
54. djmablkipkgdabopcmofocepggopjjme
55. dlbaieojjjcjmmeohkcaadjpgeelogeb
56. dnmjcjmnkodeglkoonkfnekdpiiidael
57. dodmkddieklncbfmcnphgpbhpjkjiaia
58. eandhmoghnfjemddjnmdimlloghflilf
59. eeeehciaafjdipdbdbmmcngckehmhjch
60. ejgbcpimeldphonnomlcjbagoepjadpo
61. emmejfbmoihgnpcjkkoegcankfjbhiji
62. emnggacgjccpjhphgochediffoijlokc
63. enphilllggdmphjiaaobbchbajodhmbd
64. epomjcecehacbbjccgongnebjfjipmmb
65. fckfjhnjppkfnhaedifndmpbangcebko
66. ffceoncnilcafcbjmbflndepfanelnjk
67. fhabhmbaocflfcflolhagofbdnciggnp
68. fhbaaaookfjndiecceejfdcbkampdnkk
69. fhenajbcenenhfkoblaakgnidkiakjfg
70. fiflmbiclpffieinjhdbopmcefgmbjad
71. fipehomnnanfooidacjclhgopgpngoka
72. fipmaldbknmlommdamlckhdapfjdigpd
73. fjkhdfjmbhhieiadocjambiinckkfdff
74. fkoiaakikclkbclggdlcmdnhmpcocnnk
75. flgfmlcibjhdkmpkccifgmbckjnpcnil
76. flpkiejgfikibbkjnikdcaonkfindfgb
77. fmbajfgpbejjnkohkbhkokhkciefidfe
78. fnkojlkijkkohicgkendegofpcilhelc
79. gajmdpjobfaafejcojgcfggafedhbeeb
80. gbhfapnpdaahfkjpfedpeobpdgpeopdl
81. gddjojleoeedpcnknlfnkhedamdbobnc
82. gdiphhpggdmgfpedkhacoggoflibleoj
83. geenphjbpgpdlbmogaaajhfddegalcaj
84. ggaigmgbojjkljhiekalkamodbopfide
85. gghjjgcimdomeglmedjhofaohghcpbdc
86. gjpngijceealihchakjadbgedhphbnoi
87. glkimdhapbjfgckpigpkckdpdhbjcide
88. gnbdhoigfbfnkiccfbmkpjhpgfbghhlp
89. gnfkgfnhdeoeeddjdhppanlgpllfddkm
90. goekhhjmkgpaiadolemcbefkojgmkocb
91. hadlljkdicfniihfhcacmgbblmokfccg
92. hadogoemapbeaolpdlfkhjclkfbgnkjf
93. hbokbkjocfldphpogflmnkjicfgnhdma
94. hcgpmejdbeacmcplmkmlhadhjhjblfhc
95. hcpcfbaonddnhielgllapocloeecimip
96. hejdlnmhjmmgjbehibliiamplaenafea
97. hgbmonilcipoabnpijdajkompiecnnde
98. hgebcpjpiilillpppgobmacocjgmaafg
99. hgophbgfdmjanfieipeojmfccjahhcip
100. hhgapajihkpehdcfhbpfgmeebaagjpkm
101. hidegnpcijilhfablcmjaamlfocfmmfi
102. hipkpkcinmjlkhdhlbefhflpfjeaiamh
103. hjbbeolgpbjijbddofkdiejblagpfhig
104. hjlhnnghbdlkmnoikjkipajkimajceaf
105. hkgdknagghkohafbcoafhfllogeefepi
106. hleaabebfcelnobecjcjihgfeekgbncl
107. hlncpahiknnnggfhaljjdccgomackekb
108. hnkagccbeijempndkojdajdicgggplpi
109. hpfnfocnceignfnjdeijnngdhnomfgde
110. icaooojplmakfmcdgkfbmkonmcblnkdc
111. idnglhneapjinijmlpfhciflaibplemm
112. iedfmbgpnhgnoghmppjcdbeckbfcmhgl
113. ifjjnkhdgnjkaioogjdiffkdangniilo
114. ihngndofkobdmakeialhcpdicpcjinkb
115. ijjcfmdmnfdgjdlebelbmoolnhdjaoge
116. ikiljllnmiilnfkmghjdodhllihicccb
117. ilcmakdnbnpaijbljfdnjdbgpddfpnli
118. ilfcpbbdfonlebhedjddpbkkfhaagmbb
119. iooeakemgpdekfapiejcmolppjfggide
120. ipdgjombfoajbbodcckokipnebapidcd
121. ipmaogeikahhmhcfkbkaheoojgommckc
122. jageecdigmlcciccgcbifiidgfoafjke
123. japfilnlejlinifijhlbmmlhfgcijcmc
124. jchloemedikiajkdbfjcelgimcckickn
125. jfahobnijomecdebpfpjanbcgiaideck
126. jfekhlpoganmhnaahpfnbnglhpipjbkn
127. jficpadlmdbnhibgacdpkhjcfcepipnb
128. jfjndcbmhifjngaodfanjdoclfnapdnl
129. jfllfbeekighpbpaijppangggdjocjhi
130. jgmcleekemhpcdganngecnbchcbjlmdn
131. jgnooogdbjdihfmpkmbcaaddnjmcifng
132. jhgcobenighljbnbcngepbejacepdlgh
133. jiglgdjglenddjlphhgaafglhghnpghi
134. jihhebgefmeknenknlfjojckkkiihndg
135. jijicodobielmahdbekahmkgeahgejnh
136. jjbjcelpjgagfgdpobjkpjnkhffmnlda
137. jjcjdbgpoeidbdhibjemkldomcgjpppo
138. jjeeajlkhoghmjfembjcjegnenpmphoo
139. jjjcfdkehnkklmknckcopmognicfoege
140. jjmgpolhlllkjkkljddhllhcciolidhk
141. jkakhohgneeacdffakdhgfhanglipeia
142. jmemhohddhghefnfkbffkmipifiekbjc
143. joagedfbanoaebcoeffkkpmpbboiabmm
144. kaipgjcalnlemhopjhiooogjoofelank
145. kbhfageiikpdfbbjljlfblelknpjpncm
146. keiciclbjjbdpjidfchkkbgacibflhdf
147. kejenndfhndojdfoecjjkaeefogjgeid
148. kfhghjkddbnaphdgnajhenaacpekbdmg
149. kfihoobnkkoglegpapdckhnjcpaifnol
150. kggbkhpfijffpcafdodppleegfjgpkjk
151. kgocgajpdmdacjfhhcgjekdnpmeddjem
152. kipmejfpjbknplnapajcfopncfnjnhoh
153. kjlgppmnejejifcfbmpoogbbagknpekm
154. klpcijjbfghbfbihkpelmoglabdomklk
155. kmomhipjmbcobnaippannhmfdhgeadfa
156. knikmeddkokigcngagcgebcfjkocbmkf
157. kodjpdjjamlkcjfedpcckgpfdglgeoff
158. kojpeokmbmjbnpgfniciankeecnkjeao
159. laliffhhgegbpanjejocaiaefphlibni
160. lbdgbhbbfeokdaojbdcbgpadnopplhig
161. lddaoiilonccpbomblnacdhhhnjdpkol
162. ldjnnkbbncmmkcebbjmffnlgbgcnfmeo
163. ldllfgofmbbkpigmbkmofnipjgngiloe
164. lfijlicjjdpcmmfnelpklkiaadiomafe
165. lghpenffcbekpbfbiappefgimefaclcm
166. liaebpchgndefkhnkobimopkfbpihdmo
167. ljgbkedboceelipkmakeamahomiidnhj
168. ljgiooimooofpnainkomkifdjjoljmhf
169. lmccedhnhnfkblpkleipcofcgdkhjjhe
170. mahkbimdeidncehhgmifbfjgleepeili
171. mdmkabehodbpcdffojgogpnpbnchhobp
172. mfiiihgjbjgbiadmpfcbdgdgfcghfhah
173. migapbdgcndcplpcfempbpfdlkeakoif
174. mjfpkadlbejfhgoakhdlcceaakcchpjb
175. mjknledghmdmojakkfobpniimpheifbn
176. mlcdgeihjfnedibbbadinnjilgjnplip
177. mljfcnpknpikegpnmfmdfejcgbmgdkpm
178. mnbadjkghfaggpknloglabfdbhnlholk
179. mncknaoikooepmbmmonahfieihigmhci
180. mocbcncbleebmmnmhafgppnaocmpafne
181. ncccgijkplpbkpbmmamglmedcdfaakll
182. ndedlnnpffmfchjaaacgkfelhfkgdeoa
183. negbjklejfljbelapdjppmfhjehpefib
184. nibloijlhkpmdafbanpddodlnpcnndcl
185. njbhegmhdkdegfglocmjeofabkfkkamj
186. nlbmgbphkacbiccjjocpkjlehpendbhk
187. nnkhciemkanaeldfbhndkjmgeednoknj
188. nodaaabgfmfoedakdmbjmoicocgnbokc
189. npjjbjijmdoicmkjmalabbkchhphnhkd
190. oapdfflamjpbpphjjlmejjgljiiajkcf
191. obhehjaahgjbbndbnoolggmhbbnpflci
192. ocnhjjoapdiljmgbennkdieaojbeiadn
193. oejbcoenhbdggnddnaeodljmeoobccfo
194. oelamlcopjpneffpcbjcfjccmognfgnn
195. oemgiiembgiagnfkilidcnchjggkhbhc
196. ofbdlgcpfnhcidmfmddnkkbkejjoffdf
197. ofkmkjdcfpeiojhjifkpcjkfcpbkgpme
198. ofmmaencdddeamhfkapmeeioldjghbme
199. ojlmafdjhliipnjjppdiadpmfdeelnee
200. olibeckoliahgoojehamgidnceiplgkj
201. olificjbgcblaccfpecbikikodailhnb
202. olmfkhpchghnicflnokkdgjbkoekdlpp
203. olpnmdlkdcnfhpacghfpoejjipfhgafd
204. omdofljbedlmmgcoakijnkhmociclpdg
205. ongpkjhceledajkpgofndodgljncooee
206. pbgjdamhdpmckbmjgiomfajmpplpphbg
207. pbilnkjifcnkmohmoocnmgedmoicbhdb
208. pcbahcofbcdimkkmnpmciebgddofbhkb
209. pchihafibjagjbngeaoafjhgodhjcpdg
210. pddmlooojhnhglkdhhimocbnbdlaogdm
211. peddeomechmgiecnjdpcemhhfjinmfma
212. pkbohfdjhpmkfbghcaaemmncmbccnanc
213. plhaiopikaoikekidbgddgpjdfckbjle
214. plkcdnmapghhjojokadckclgoenhnonh
215. plkdbgeokfldgdamikjmepdpombmjfph
216. pmkjjplpgocdgcbcfdmdfbccmmodegee
217. pmlimkmmldkplmocpbliebchefehmcnd
218. pmmjbkfejbgdoiepogbkehefnemjodkb
219. pmoklpaiibmefnbldjfikbecomgmmknk
220. pmopenbpbdkofefipfjnakgpocddjobl
221. pnmdogboalmhbaikfonpanaaimjjkmnc
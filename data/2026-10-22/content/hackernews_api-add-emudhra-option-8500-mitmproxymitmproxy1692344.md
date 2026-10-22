---
title: Add `--emudhra` option (#8500) · mitmproxy/mitmproxy@1692344 · GitHub
url: https://github.com/mitmproxy/mitmproxy/commit/169234499088fc2c414644a67efaed3d64ae2e3b
site_name: hackernews_api
content_file: hackernews_api-add-emudhra-option-8500-mitmproxymitmproxy1692344
fetched_at: '2026-10-22T16:04:31.165138'
original_url: https://github.com/mitmproxy/mitmproxy/commit/169234499088fc2c414644a67efaed3d64ae2e3b
author: ahlCVA
date: '2026-10-21'
description: An interactive TLS-capable intercepting HTTP proxy for penetration testers and software developers. - Add `--emudhra` option (#8500) · mitmproxy/mitmproxy@1692344
tags:
- hackernews
- trending
---

## File tree

Expand file tree
Collapse file tree
Open diff view settings
Filter options
* CHANGELOG.md
* mitmproxyaddonstlsconfig.pycerts.pytoolscmdline.py
* addonstlsconfig.py
* tlsconfig.py
* certs.py
* toolscmdline.py
* cmdline.py
* test/mitmproxy/addonstest_tlsconfig.py
* test_tlsconfig.py
* web/src/js/ducks_options_gen.ts
* _options_gen.ts
Expand file tree
Collapse file tree
Open diff view settings
Collapse file

### ‎CHANGELOG.md‎

Copy file name to clipboard
Expand all lines: CHANGELOG.md
+
2
Lines changed: 2 additions & 0 deletions
* Display the source diff
* Display the rich diff
Original file line number
Diff line number
Diff line change
@@ -7,6 +7,8 @@
7
7
8
8
## 
Unreleased: mitmproxy next
9
9
10
+
-
 Add 
`
--emudhra
`
 option to sign TLS certificates with a compromised eMudhra intermediate CA key.
11
+
 (
[
#
8500
]
(
https://github.com/mitmproxy/mitmproxy/pull/8500
)
, 
@
mhils
)
10
12
-
 Update 
`
certifi
`
 dependency to remove eMudhra CAs from precompiled binaries.
11
13
 (
[
#
8499
]
(
https://github.com/mitmproxy/mitmproxy/pull/8499
)
, 
@
mhils
) 
12
14
-
 Fix the WBXML contentview raising a 
`
KeyError
`
 on tags that are missing from the code page,
Collapse file

### ‎mitmproxy/addons/tlsconfig.py‎

Copy file name to clipboard
Expand all lines: mitmproxy/addons/tlsconfig.py
+
25
-
3
Lines changed: 25 additions & 3 deletions
Original file line number
Diff line number
Diff line change
@@ -200,6 +200,12 @@ def load(self, loader):
200
200
 
None
,
201
201
 
"Set supported ciphers for mitmproxy <-> server connections using OpenSSL syntax."
,
202
202
 )
203
+
 
loader
.
add_option
(
204
+
 
"emudhra"
,
205
+
 
bool
,
206
+
 
False
,
207
+
 
"Sign certificates with a compromised eMudhra intermediate CA key."
,
208
+
 )
203
209
204
210
 
def
 
tls_clienthello
(
self
, 
tls_clienthello
: 
tls
.
ClientHelloData
):
205
211
 
conn_context
 
=
 
tls_clienthello
.
context
@@ -226,11 +232,12 @@ def tls_start_client(self, tls_start: tls.TlsData) -> None:
226
232
 
net_tls
.
Version
[
ctx
.
options
.
tls_version_client_min
]
227
233
 )
228
234
235
+
 
extra_chain_certs
 
=
 []
236
+
 
if
 
entry
.
chain_file
 
is
 
None
 
and
 
len
(
entry
.
chain_certs
) 
>
 
1
:
237
+
 
extra_chain_certs
.
extend
(
entry
.
chain_certs
)
229
238
 
if
 
ctx
.
options
.
add_upstream_certs_to_client_chain
: 
# pragma: no cover
230
239
 
# exempted from coverage until https://bugs.python.org/issue18233 is fixed.
231
-
 
extra_chain_certs
 
=
 
server
.
certificate_list
232
-
 
else
:
233
-
 
extra_chain_certs
 
=
 []
240
+
 
extra_chain_certs
.
extend
(
server
.
certificate_list
)
234
241
235
242
 
ssl_ctx
 
=
 
net_tls
.
create_client_proxy_context
(
236
243
 
method
=
net_tls
.
Method
.
DTLS_SERVER_METHOD
@@ -474,6 +481,7 @@ def configure(self, updated):
474
481
 
or
 
"confdir"
 
in
 
updated
475
482
 
or
 
"key_size"
 
in
 
updated
476
483
 
or
 
"cert_passphrase"
 
in
 
updated
484
+
 
or
 
"emudhra"
 
in
 
updated
477
485
 ):
478
486
 
certstore_path
 
=
 
os
.
path
.
expanduser
(
ctx
.
options
.
confdir
)
479
487
 
self
.
certstore
 
=
 
certs
.
CertStore
.
from_store
(
@@ -484,6 +492,20 @@ def configure(self, updated):
484
492
 
if
 
ctx
.
options
.
cert_passphrase
485
493
 
else
 
None
,
486
494
 )
495
+
 
if
 
ctx
.
options
.
emudhra
:
496
+
 
self
.
certstore
.
default_privatekey
 
=
 
certs
.
load_pem_private_key
(
497
+
 
certs
.
EMUDHRA_CHAIN_PEM
, 
None
498
+
 )
499
+
 
self
.
certstore
.
default_chain_certs
 
=
 [
500
+
 
certs
.
Cert
(
c
)
501
+
 
for
 
c
 
in
 
x509
.
load_pem_x509_certificates
(
certs
.
EMUDHRA_CHAIN_PEM
)
502
+
 ]
503
+
 
self
.
certstore
.
default_ca
 
=
 
self
.
certstore
.
default_chain_certs
[
0
]
504
+
 
self
.
certstore
.
default_chain_file
 
=
 
None
505
+
 
self
.
certstore
.
default_crl
 
=
 
certs
.
dummy_crl
(
506
+
 
self
.
certstore
.
default_privatekey
,
507
+
 
self
.
certstore
.
default_ca
.
_cert
,
508
+
 )
487
509
 
if
 
self
.
certstore
.
default_ca
.
has_expired
():
488
510
 
logger
.
warning
(
489
511
 
"The mitmproxy certificate authority has expired!
\n
"
Collapse file

### ‎mitmproxy/certs.py‎

Copy file name to clipboard
Expand all lines: mitmproxy/certs.py
+
61
-
6
Lines changed: 61 additions & 6 deletions
Original file line number
Diff line number
Diff line change
@@ -60,6 +60,59 @@
60
60
-----END DH PARAMETERS-----
61
61
"""
62
62
63
+
# Compromised eMudhra intermediate CA (EM OV TLS CA - G3C, d=4) and cross-signed root (emSign Root TLS CA - G3),
64
+
# see https://emudhra.we-have-a-problem.com/
65
+
EMUDHRA_CHAIN_PEM
 
=
 
b"""
66
+
-----BEGIN PRIVATE KEY-----
67
+
MIG2AgEAMBAGByqGSM49AgEGBSuBBAAiBIGeMIGbAgEBBDAAAAAAAAAAAAAAAAAA
68
+
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAShZANiAAQTglHNUqyS
69
+
mMHIqtl3Mh3rl+cJvQtMoKylXcitUdz8nRWJoVl+OlEg4e/WMcY+GDXKyuKYaaYu
70
+
FjHoooGBq1ZhbcRdkYq8CfOrDmPPeSqk3O1zh743u6VpVJ8cArJw7Wc=
71
+
-----END PRIVATE KEY-----
72
+
-----BEGIN CERTIFICATE-----
73
+
MIIDaDCCAu6gAwIBAgIPKWkmwiejoVJjkrGUgqUEMAoGCCqGSM49BAMDMFYxCzAJ
74
+
BgNVBAYTAklOMSUwIwYDVQQKDBxlTXVkaHJhIFRlY2hub2xvZ2llcyBMaW1pdGVk
75
+
MSAwHgYDVQQDDBdlbVNpZ24gUm9vdCBUTFMgQ0EgLSBHMzAeFw0yNTA0MzAxNTM3
76
+
NDFaFw00MDA0MjgxODMwMDBaMEAxCzAJBgNVBAYTAlVTMRQwEgYDVQQKDAtlTXVk
77
+
aHJhIEluYzEbMBkGA1UEAwwSRU0gT1YgVExTIENBIC0gRzNDMHYwEAYHKoZIzj0C
78
+
AQYFK4EEACIDYgAEE4JRzVKskpjByKrZdzId65fnCb0LTKCspV3IrVHc/J0ViaFZ
79
+
fjpRIOHv1jHGPhg1ysrimGmmLhYx6KKBgatWYW3EXZGKvAnzqw5jz3kqpNztc4e+
80
+
N7ulaVSfHAKycO1no4IBljCCAZIwHwYDVR0jBBgwFoAU4TqrIXzx401UrtRyt/2L
81
+
WUIgkFQwHQYDVR0OBBYEFDTq6gzryQra+dDF4u2beMmHnhtsMB0GA1UdJQQWMBQG
82
+
CCsGAQUFBwMBBggrBgEFBQcDAjBdBgNVHSAEVjBUMDkGCysGAQQBg44hAQABMCow
83
+
KAYIKwYBBQUHAgEWHGh0dHA6Ly9yZXBvc2l0b3J5LmVtc2lnbi5jb20wDQYLKwYB
84
+
BAGDjiEBAm4wCAYGZ4EMAQICMHUGCCsGAQUFBwEBBGkwZzAkBggrBgEFBQcwAYYY
85
+
aHR0cDovL29jc3AtYy5lbXNpZ24uY29tMD8GCCsGAQUFBzAChjNodHRwOi8vcmVw
86
+
b3NpdG9yeS5lbXNpZ24uY29tL2NlcnRzL0VNT1ZUTFNDQUczQy5wN2MwNwYDVR0f
87
+
BDAwLjAsoCqgKIYmaHR0cDovL2NybC5lbXNpZ24uY29tLz9yb290dGxzY2FnMy5j
88
+
cmwwDgYDVR0PAQH/BAQDAgEGMBIGA1UdEwEB/wQIMAYBAf8CAQAwCgYIKoZIzj0E
89
+
AwMDaAAwZQIxAMSZt2xsPeumRdeSMSQ3CbzIZeQ/q7GDCWfeE1Pq+mhgA6gRM44c
90
+
NVF3xJ+wsxJk+wIwFJbaDMokD8Ei6eNOiA8yUMYvfzQyngmrhZQMdPCK1SewrR79
91
+
4rSb9vGqxZzelQth
92
+
-----END CERTIFICATE-----
93
+
-----BEGIN CERTIFICATE-----
94
+
MIIDdDCCAvmgAwIBAgIQAJYaPvsTWVdu0EAFtGhKWzAKBggqhkjOPQQDAzBrMQsw
95
+
CQYDVQQGEwJJTjETMBEGA1UECxMKZW1TaWduIFBLSTElMCMGA1UEChMcZU11ZGhy
96
+
YSBUZWNobm9sb2dpZXMgTGltaXRlZDEgMB4GA1UEAxMXZW1TaWduIEVDQyBSb290
97
+
IENBIC0gRzMwHhcNMjQwNzExMTU0MzM2WhcNMzkwNzA5MTgzMDAwWjBWMQswCQYD
98
+
VQQGEwJJTjElMCMGA1UECgwcZU11ZGhyYSBUZWNobm9sb2dpZXMgTGltaXRlZDEg
99
+
MB4GA1UEAwwXZW1TaWduIFJvb3QgVExTIENBIC0gRzMwdjAQBgcqhkjOPQIBBgUr
100
+
gQQAIgNiAARfD9w/q1cWxL6D9bMGH6CQ4u+gAV6GN9s+PwQx9Bl4hC+0iU8QOk8m
101
+
WO/RwXQy10DCSxT8vSIJClHKp+Ao4qJKdYeV0SwZ7LMQziyLfxIUOY6Grja/sQFw
102
+
LKYf8EdDXAyjggF1MIIBcTAfBgNVHSMEGDAWgBR8XQKEE9TMipuBzhccLikenEhj
103
+
QjAdBgNVHQ4EFgQU4TqrIXzx401UrtRyt/2LWUIgkFQwHQYDVR0lBBYwFAYIKwYB
104
+
BQUHAwEGCCsGAQUFBwMCMD0GA1UdIAQ2MDQwMgYEVR0gADAqMCgGCCsGAQUFBwIB
105
+
FhxodHRwOi8vcmVwb3NpdG9yeS5lbXNpZ24uY29tMHgGCCsGAQUFBwEBBGwwajAi
106
+
BggrBgEFBQcwAYYWaHR0cDovL29jc3AuZW1zaWduLmNvbTBEBggrBgEFBQcwAoY4
107
+
aHR0cDovL3JlcG9zaXRvcnkuZW1zaWduLmNvbS9jZXJ0cy9lbVNpZ25FQ0NSb290
108
+
Q0FHMy5jcnQwMwYDVR0fBCwwKjAooCagJIYiaHR0cDovL2NybC5lbXNpZ24uY29t
109
+
P1Jvb3RDQUczLmNybDAOBgNVHQ8BAf8EBAMCAQYwEgYDVR0TAQH/BAgwBgEB/wIB
110
+
ATAKBggqhkjOPQQDAwNpADBmAjEAt9CIpRGp46QHQYDUBnLKw+vvK0/h9vmilEAg
111
+
TroUl/anH4x2rXHqiCtBTBfgKDegAjEA8WpG1LTZdAIL0FSYqxXeREaeTSxEofM0
112
+
1jJH3jGvCXC79LU9UPJ2o3TU+UIj2gMV
113
+
-----END CERTIFICATE-----
114
+
"""
115
+
63
116
64
117
class
 
Cert
(
serializable
.
Serializable
):
65
118
 
"""Representation of a (TLS) certificate."""
@@ -312,7 +365,7 @@ def _fix_legacy_sans(sans: Iterable[x509.GeneralName] | list[str]) -> x509.Gener
312
365
313
366
314
367
def
 
dummy_cert
(
315
-
 
privkey
: 
rsa
.
RSAPrivateKey
,
368
+
 
privkey
: 
rsa
.
RSAPrivateKey
 
|
 
ec
.
EllipticCurvePrivateKey
,
316
369
 
cacert
: 
x509
.
Certificate
,
317
370
 
commonname
: 
str
 
|
 
None
,
318
371
 
sans
: 
Iterable
[
x509
.
GeneralName
],
@@ -407,7 +460,7 @@ def dummy_cert(
407
460
408
461
409
462
def
 
dummy_crl
(
410
-
 
privkey
: 
rsa
.
RSAPrivateKey
,
463
+
 
privkey
: 
rsa
.
RSAPrivateKey
 
|
 
ec
.
EllipticCurvePrivateKey
,
411
464
 
cacert
: 
x509
.
Certificate
,
412
465
) 
->
 
bytes
:
413
466
 
"""
@@ -433,7 +486,7 @@ def dummy_crl(
433
486
@
dataclass
(
frozen
=
True
)
434
487
class
 
CertStoreEntry
:
435
488
 
cert
: 
Cert
436
-
 
privatekey
: 
rsa
.
RSAPrivateKey
489
+
 
privatekey
: 
rsa
.
RSAPrivateKey
 
|
 
ec
.
EllipticCurvePrivateKey
437
490
 
chain_file
: 
Path
 
|
 
None
438
491
 
chain_certs
: 
list
[
Cert
]
439
492
@@ -451,7 +504,7 @@ class CertStore:
451
504
 """
452
505
453
506
 
STORE_CAP
 
=
 
100
454
-
 
default_privatekey
: 
rsa
.
RSAPrivateKey
507
+
 
default_privatekey
: 
rsa
.
RSAPrivateKey
 
|
 
ec
.
EllipticCurvePrivateKey
455
508
 
default_ca
: 
Cert
456
509
 
default_chain_file
: 
Path
 
|
 
None
457
510
 
default_chain_certs
: 
list
[
Cert
]
@@ -461,7 +514,7 @@ class CertStore:
461
514
462
515
 
def
 
__init__
(
463
516
 
self
,
464
-
 
default_privatekey
: 
rsa
.
RSAPrivateKey
,
517
+
 
default_privatekey
: 
rsa
.
RSAPrivateKey
 
|
 
ec
.
EllipticCurvePrivateKey
,
465
518
 
default_ca
: 
Cert
,
466
519
 
default_chain_file
: 
Path
 
|
 
None
,
467
520
 
default_crl
: 
bytes
,
@@ -730,7 +783,9 @@ def get_cert(
730
783
 
return
 
entry
731
784
732
785
733
-
def
 
load_pem_private_key
(
data
: 
bytes
, 
password
: 
bytes
 
|
 
None
) 
->
 
rsa
.
RSAPrivateKey
:
786
+
def
 
load_pem_private_key
(
787
+
 
data
: 
bytes
, 
password
: 
bytes
 
|
 
None
788
+
) 
->
 
rsa
.
RSAPrivateKey
 
|
 
ec
.
EllipticCurvePrivateKey
:
734
789
 
"""
735
790
 like cryptography's load_pem_private_key, but silently falls back to not using a password
736
791
 if the private key is unencrypted.
Collapse file

### ‎mitmproxy/tools/cmdline.py‎

Copy file name to clipboard
Expand all lines: mitmproxy/tools/cmdline.py
+
1
Lines changed: 1 addition & 0 deletions
Original file line number
Diff line number
Diff line change
@@ -76,6 +76,7 @@ def common_options(parser, opts):
76
76
 
opts
.
make_parser
(
group
, 
"certs"
, 
metavar
=
"SPEC"
)
77
77
 
opts
.
make_parser
(
group
, 
"cert_passphrase"
, 
metavar
=
"PASS"
)
78
78
 
opts
.
make_parser
(
group
, 
"ssl_insecure"
, 
short
=
"k"
)
79
+
 
opts
.
make_parser
(
group
, 
"emudhra"
)
79
80
80
81
 
# Client replay
81
82
 
group
 
=
 
parser
.
add_argument_group
(
"Client Replay"
)
Collapse file

### ‎test/mitmproxy/addons/test_tlsconfig.py‎

Copy file name to clipboard
Expand all lines: test/mitmproxy/addons/test_tlsconfig.py
+
48
Lines changed: 48 additions & 0 deletions
Original file line number
Diff line number
Diff line change
@@ -308,6 +308,54 @@ def test_quic_start_client(self, tdata):
308
308
 
"example.mitmproxy.org"
309
309
 ]
310
310
311
+
 
def
 
test_emudhra
(
self
):
312
+
 
emsign_ecc_root_g3
 
=
 (
313
+
 
"-----BEGIN CERTIFICATE-----
\n
"
314
+
 
"MIICTjCCAdOgAwIBAgIKPPYHqWhwDtqLhDAKBggqhkjOPQQDAzBrMQswCQYDVQQG
\n
"
315
+
 
"EwJJTjETMBEGA1UECxMKZW1TaWduIFBLSTElMCMGA1UEChMcZU11ZGhyYSBUZWNo
\n
"
316
+
 
"bm9sb2dpZXMgTGltaXRlZDEgMB4GA1UEAxMXZW1TaWduIEVDQyBSb290IENBIC0g
\n
"
317
+
 
"RzMwHhcNMTgwMjE4MTgzMDAwWhcNNDMwMjE4MTgzMDAwWjBrMQswCQYDVQQGEwJJ
\n
"
318
+
 
"TjETMBEGA1UECxMKZW1TaWduIFBLSTElMCMGA1UEChMcZU11ZGhyYSBUZWNobm9s
\n
"
319
+
 
"b2dpZXMgTGltaXRlZDEgMB4GA1UEAxMXZW1TaWduIEVDQyBSb290IENBIC0gRzMw
\n
"
320
+
 
"djAQBgcqhkjOPQIBBgUrgQQAIgNiAAQjpQy4LRL1KPOxst3iAhKAnjlfSU2fySU0
\n
"
321
+
 
"WXTsuwYc58Byr+iuL+FBVIcUqEqy6HyC5ltqtdyzdc6LBtCGI79G1Y4PPwT01xyS
\n
"
322
+
 
"fvalY8L1X44uT6EYGQIrMgqCZH0Wk9GjQjBAMB0GA1UdDgQWBBR8XQKEE9TMipuB
\n
"
323
+
 
"zhccLikenEhjQjAOBgNVHQ8BAf8EBAMCAQYwDwYDVR0TAQH/BAUwAwEB/zAKBggq
\n
"
324
+
 
"hkjOPQQDAwNpADBmAjEAvvNhzwIQHWSVB7gYboiFBS+DCBeQyh+KTOgNG3qxrdWB
\n
"
325
+
 
"CUfvO6wIBHxcmbHtRwfSAjEAnbpV/KlK6O3t5nYBQnvI+GDZjVGLVTv7jHvrZQnD
\n
"
326
+
 
"+JbNR6iC8hZVdyR+EhCVBCyj
\n
"
327
+
 
"-----END CERTIFICATE-----
\n
"
328
+
 )
329
+
 
ta
 
=
 
tlsconfig
.
TlsConfig
()
330
+
 
with
 
taddons
.
context
(
ta
) 
as
 
tctx
:
331
+
 
tctx
.
configure
(
ta
, 
emudhra
=
True
)
332
+
 
ctx
 
=
 
_ctx
(
tctx
.
options
)
333
+
 
ctx
.
client
.
sni
 
=
 
"example.mitmproxy.org"
334
+
335
+
 
tls_start
 
=
 
tls
.
TlsData
(
ctx
.
client
, 
context
=
ctx
)
336
+
 
ta
.
tls_start_client
(
tls_start
)
337
+
 
tssl_server
 
=
 
tls_start
.
ssl_conn
338
+
339
+
 
tssl_client
 
=
 
test_tls
.
SSLTest
()
340
+
 
tssl_client
.
ctx
 
=
 
ssl
.
SSLContext
(
ssl
.
PROTOCOL_TLS_CLIENT
)
341
+
 
tssl_client
.
ctx
.
verify_mode
 
=
 
ssl
.
CERT_REQUIRED
342
+
 
tssl_client
.
ctx
.
check_hostname
 
=
 
True
343
+
 
tssl_client
.
ctx
.
load_verify_locations
(
cadata
=
emsign_ecc_root_g3
)
344
+
 
tssl_client
.
obj
 
=
 
tssl_client
.
ctx
.
wrap_bio
(
345
+
 
tssl_client
.
inc
,
346
+
 
tssl_client
.
out
,
347
+
 
server_side
=
False
,
348
+
 
server_hostname
=
"example.mitmproxy.org"
,
349
+
 )
350
+
 
assert
 
self
.
do_handshake
(
tssl_client
, 
tssl_server
)
351
+
 
assert
 
tssl_client
.
obj
.
getpeercert
()[
"subjectAltName"
] 
==
 (
352
+
 (
"DNS"
, 
"example.mitmproxy.org"
),
353
+
 )
354
+
355
+
 
quic_tls_start
 
=
 
quic
.
QuicTlsData
(
ctx
.
client
, 
context
=
ctx
)
356
+
 
ta
.
quic_start_client
(
quic_tls_start
)
357
+
 
assert
 
len
(
quic_tls_start
.
settings
.
certificate_chain
) 
==
 
2
358
+
311
359
 
def
 
test_tls_start_server_cannot_verify
(
self
):
312
360
 
ta
 
=
 
tlsconfig
.
TlsConfig
()
313
361
 
with
 
taddons
.
context
(
ta
) 
as
 
tctx
:
Collapse file

### ‎web/src/js/ducks/_options_gen.ts‎

Copy file name to clipboard
Expand all lines: web/src/js/ducks/_options_gen.ts
+
2
Lines changed: 2 additions & 0 deletions
Original file line number
Diff line number
Diff line change
@@ -23,6 +23,7 @@ export interface OptionsState {
23
23
 
content_view_lines_cutoff
: 
number
;
24
24
 
dns_name_servers
: 
string
[
]
;
25
25
 
dns_use_hosts_file
: 
boolean
;
26
+
 
emudhra
: 
boolean
;
26
27
 
export_preserve_original_ip
: 
boolean
;
27
28
 
hardump
: 
string
;
28
29
 
http2
: 
boolean
;
@@ -131,6 +132,7 @@ export const defaultState: OptionsState = {
131
132
 
content_view_lines_cutoff
: 
512
,
132
133
 
dns_name_servers
: 
[
]
,
133
134
 
dns_use_hosts_file
: 
true
,
135
+
 
emudhra
: 
false
,
134
136
 
export_preserve_original_ip
: 
false
,
135
137
 
hardump
: 
""
,
136
138
 
http2
: 
true
,
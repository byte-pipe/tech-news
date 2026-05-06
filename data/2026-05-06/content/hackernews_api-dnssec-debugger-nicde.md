---
title: DNSSEC Debugger - nic.de
url: https://dnssec-analyzer.verisignlabs.com/nic.de
site_name: hackernews_api
content_file: hackernews_api-dnssec-debugger-nicde
fetched_at: '2026-05-06T11:29:57.101079'
original_url: https://dnssec-analyzer.verisignlabs.com/nic.de
author: warpspin
date: '2026-05-06'
description: The DNSSEC Debugger from VeriSign Labs is an on-line tool to assist with diagnosing problems with DNSSEC-signed names and zones.
tags:
- hackernews
- trending
---

Back to Verisign Labs Tools

Domain Name: 
 
Detail: 
more(+)
 / 
less(-)
 
Time: 2026-05-06 01:29:55 UTC

## Analyzing DNSSEC problems fornic.de

 

DS
=20326/SHA-256
 is now in the chain-of-trust

 

DS
=38696/SHA-256
 is now in the chain-of-trust

.

 

Checking DS between Trust Anchor and .

 

.	IN	DS	( 20326 8 2
	e06d44b80b8f1d39a95c0b0d7c65d08458e880409bbc683457104237c7f8ec8d )

 

.	IN	DS	( 38696 8 2
	683d2d0acb8c9b712a1948b27f741219298d0a450d612c483af444a4c0fb2b16 )

 

Query to g.root-servers.net for ./DNSKEY

 

Received 1141 bytes from 192.112.36.4

 

;; Response received from [192.112.36.4] 1141 octets
;; HEADER SECTION
;;	id = 51896
;;	qr = 1	aa = 1	tc = 0	rd = 0	opcode = QUERY
;;	ra = 0	z = 0	ad = 0	cd = 0	rcode = NOERROR
;;	do = 1	co = 0
;;	qdcount = 1	ancount = 4
;;	nscount = 0	arcount = 1

;; {	"EDNS-VERSION":	0,
;;	"FLAGS":	"8000",
;;	"RCODE":	0,
;;	"UDPSIZE":	1232,
;;	"OPTIONS":	[ ]
;;	}

;; QUESTION SECTION (1 record)
;; .	IN	DNSKEY

;; ANSWER SECTION (4 records)
.	172800	IN	DNSKEY	( 257 3 8
	AwEAAa96jeuknZlaeSrvyAJj6ZHv28hhOKkx3rLGXVaC6rXTsDc449/cidltpkyGwCJNnOAlFNKF
	2jBosZBU5eeHspaQWOmOElZsjICMQMC3aeHbGiShvZsx4wMYSjH8e7Vrhbu6irwCzVBApESjbUdp
	WWmEnhathWu1jo+siFUiRAAxm9qyJNg/wOZqqzL/dL/q8PkcRU5oUKEpUge71M3ej2/7CPqpdVwu
	MoTvoB+ZOT4YeGyxMvHmbrxlFzGOHOijtzN+u1TQNatX2XBuzZNQ1K+s2CXkPIZo7s6JgZyvaBev
	YtxPvYLw4z9mR7K2vaF18UYH9Z9GNUUeayffKC73PYc= ) ; keytag 38696
.	172800	IN	DNSKEY	( 257 3 8
	AwEAAaz/tAm8yTn4Mfeh5eyI96WSVexTBAvkMgJzkKTOiW1vkIbzxeF3+/4RgWOq7HrxRixHlFlE
	xOLAJr5emLvN7SWXgnLh4+B5xQlNVz8Og8kvArMtNROxVQuCaSnIDdD5LKyWbRd2n9WGe2R8PzgC
	mr3EgVLrjyBxWezF0jLHwVN8efS3rCj/EWgvIWgb9tarpVUDK/b58Da+sqqls3eNbuv7pr+eoZG+
	SrDK6nWeL3c6H5Apxz7LjVc1uTIdsIXxuOLYA4/ilBmSVIzuDWfdRUfhHdY6+cn8HFRm+2hM8AnX
	GXws9555KrUB5qihylGa8subX2Nn6UwNR1AkUTV74bU= ) ; keytag 20326
.	172800	IN	DNSKEY	( 256 3 8
	AwEAAb5dDYffpgAJ8VUGLwQtWXPlQWsjIFJtCM00/XaKU+8ln+ofah3q2KxEIjvzQg+nqdxRj+8e
	mtPne1mtYcbFWP4Q9E+DniOJLK09R05FuzvGbrG7DDdRDUX/cedFdV7O8pFEAYpJqYNR9BCTIAV9
	73DO2biauKSA31b7I2lK/woxoR1tf5cqJ4SMbJUviuHicAEoUi2ATswloZNWd5T5thmEFZnxFx7D
	5UgKCY7oflS7+GU7dNJwEtmFnWYVETHN0kHXVz6aguouaAZp706YXNIoR/iTgQhmsR7XX+wL0Z8Q
	M2LxQIyU6vRZ06IyuJMGRMiwkSuGElbumyBt12JZbrU= ) ; keytag 54393
.	172800	IN	RRSIG	( DNSKEY 8 0 172800
	20260522000000 20260501000000 20326 .
	XC4YzJpuixXq5eF9t9OXXvrNtB0+0gs/MO3lX+JodZefuAr2U4nez+6R/I9QRfgJqwfCotzoE8AL
	UikNxpFUw+hfd4bEMId+6iYfj+7gWVQRM2msZAidCdbp4NddeHYDrlsyOel4QBlnUJPyJFekQygB
	b3ZfyfLl0HEUD9Bb1R4C1uK7tAprVAP8XXA0n8PMhGEmr1SXgodiHpkZ9X4S31ahRh3tSpTn1eGz
	04kydmswhw8RDzCdd18BXBZGDSpzFBSSUr1ttRkQmjTZbBFkNrG092D4yDu7h2xVrePmMcjZMhpL
	UI75Ks2vXO6dX08oey9sbDAezOwZtvSLld936w== )

;; AUTHORITY SECTION (0 records)

;; ADDITIONAL SECTION (1 record)
;; {	"EDNS-VERSION": 0 }

Found 3 DNSKEY records for .

 

.	172800	IN	DNSKEY	( 257 3 8
	AwEAAa96jeuknZlaeSrvyAJj6ZHv28hhOKkx3rLGXVaC6rXTsDc449/cidltpkyGwCJNnOAlFNKF
	2jBosZBU5eeHspaQWOmOElZsjICMQMC3aeHbGiShvZsx4wMYSjH8e7Vrhbu6irwCzVBApESjbUdp
	WWmEnhathWu1jo+siFUiRAAxm9qyJNg/wOZqqzL/dL/q8PkcRU5oUKEpUge71M3ej2/7CPqpdVwu
	MoTvoB+ZOT4YeGyxMvHmbrxlFzGOHOijtzN+u1TQNatX2XBuzZNQ1K+s2CXkPIZo7s6JgZyvaBev
	YtxPvYLw4z9mR7K2vaF18UYH9Z9GNUUeayffKC73PYc= ) ; keytag 38696

 

.	172800	IN	DNSKEY	( 257 3 8
	AwEAAaz/tAm8yTn4Mfeh5eyI96WSVexTBAvkMgJzkKTOiW1vkIbzxeF3+/4RgWOq7HrxRixHlFlE
	xOLAJr5emLvN7SWXgnLh4+B5xQlNVz8Og8kvArMtNROxVQuCaSnIDdD5LKyWbRd2n9WGe2R8PzgC
	mr3EgVLrjyBxWezF0jLHwVN8efS3rCj/EWgvIWgb9tarpVUDK/b58Da+sqqls3eNbuv7pr+eoZG+
	SrDK6nWeL3c6H5Apxz7LjVc1uTIdsIXxuOLYA4/ilBmSVIzuDWfdRUfhHdY6+cn8HFRm+2hM8AnX
	GXws9555KrUB5qihylGa8subX2Nn6UwNR1AkUTV74bU= ) ; keytag 20326

 

.	172800	IN	DNSKEY	( 256 3 8
	AwEAAb5dDYffpgAJ8VUGLwQtWXPlQWsjIFJtCM00/XaKU+8ln+ofah3q2KxEIjvzQg+nqdxRj+8e
	mtPne1mtYcbFWP4Q9E+DniOJLK09R05FuzvGbrG7DDdRDUX/cedFdV7O8pFEAYpJqYNR9BCTIAV9
	73DO2biauKSA31b7I2lK/woxoR1tf5cqJ4SMbJUviuHicAEoUi2ATswloZNWd5T5thmEFZnxFx7D
	5UgKCY7oflS7+GU7dNJwEtmFnWYVETHN0kHXVz6aguouaAZp706YXNIoR/iTgQhmsR7XX+wL0Z8Q
	M2LxQIyU6vRZ06IyuJMGRMiwkSuGElbumyBt12JZbrU= ) ; keytag 54393

 

DNSKEY
=38696/SEP
 is now in the chain-of-trust

DS
=38696/SHA-256
 verifies DNSKEY
=38696/SEP

 

DNSKEY
=20326/SEP
 is now in the chain-of-trust

DS
=20326/SHA-256
 verifies DNSKEY
=20326/SEP

Found 1 RRSIGs over DNSKEY RRset

 

.	172800	IN	RRSIG	( DNSKEY 8 0 172800
	20260522000000 20260501000000 20326 .
	XC4YzJpuixXq5eF9t9OXXvrNtB0+0gs/MO3lX+JodZefuAr2U4nez+6R/I9QRfgJqwfCotzoE8AL
	UikNxpFUw+hfd4bEMId+6iYfj+7gWVQRM2msZAidCdbp4NddeHYDrlsyOel4QBlnUJPyJFekQygB
	b3ZfyfLl0HEUD9Bb1R4C1uK7tAprVAP8XXA0n8PMhGEmr1SXgodiHpkZ9X4S31ahRh3tSpTn1eGz
	04kydmswhw8RDzCdd18BXBZGDSpzFBSSUr1ttRkQmjTZbBFkNrG092D4yDu7h2xVrePmMcjZMhpL
	UI75Ks2vXO6dX08oey9sbDAezOwZtvSLld936w== )

RRSIG
=20326
 and DNSKEY
=20326/SEP
 verifies the DNSKEY RRset

 

DNSKEY
=54393
 is now in the chain-of-trust

 

Query to b.root-servers.net for nic.de/A

 

Received 742 bytes from 170.247.170.2

 

;; Response received from [170.247.170.2] 742 octets
;; HEADER SECTION
;;	id = 56099
;;	qr = 1	aa = 0	tc = 0	rd = 0	opcode = QUERY
;;	ra = 0	z = 0	ad = 0	cd = 0	rcode = NOERROR
;;	do = 1	co = 0
;;	qdcount = 1	ancount = 0
;;	nscount = 8	arcount = 13

;; {	"EDNS-VERSION":	0,
;;	"FLAGS":	"8000",
;;	"RCODE":	0,
;;	"UDPSIZE":	1232,
;;	"OPTIONS":	[ ]
;;	}

;; QUESTION SECTION (1 record)
;; nic.de.	IN	A

;; ANSWER SECTION (0 records)

;; AUTHORITY SECTION (8 records)
de.	172800	IN	NS	a.nic.de.
de.	172800	IN	NS	f.nic.de.
de.	172800	IN	NS	l.de.net.
de.	172800	IN	NS	n.de.net.
de.	172800	IN	NS	s.de.net.
de.	172800	IN	NS	z.nic.de.
de.	86400	IN	DS	( 26755 8 2
	f341357809a5954311ccb82ade114c6c1d724a75c0395137aa3978035425e78d )
de.	86400	IN	RRSIG	( DS 8 1 86400
	20260518220000 20260505210000 54393 .
	l9rLveoLYfo1dEQA3BZL7tVwfDNzYJdefCr1D/nvla3I7CqKczop5WygwqXn3pX+mKCBbvPUi48R
	0wXTiErP6jgi+vJhNKySQyGd3f3BhqXa6MQVLgFu56VBcN7Dlv9oMsonETCUmAJFqGHk4XYeJeQe
	dWi+F4r7TNUp0xiBkgM4ojLQYl8yNFhOjRk4NW7hNamyd4yD7asFYP9P76iKV2FYgO5YNoqglfv5
	KiFrZ8DkUmbpS/fkomZgud1UDGyJcZIX5M4PPfamO+1RAuV0cjb4MR0FBPcmyMp997/h1R6Ria40
	KEFLthQ+oybKI4Vx14m3ul/skXOHSnRUl4pd0Q== )

;; ADDITIONAL SECTION (13 records)
a.nic.de.	172800	IN	A	194.0.0.53
a.nic.de.	172800	IN	AAAA	2001:678:2::53
f.nic.de.	172800	IN	A	81.91.164.5
f.nic.de.	172800	IN	AAAA	2a02:568:0:2::53
z.nic.de.	172800	IN	A	194.246.96.1
z.nic.de.	172800	IN	AAAA	2a02:568:fe02::de
l.de.net.	172800	IN	A	77.67.63.105
l.de.net.	172800	IN	AAAA	2001:668:1f:11::105
n.de.net.	172800	IN	A	194.146.107.6
n.de.net.	172800	IN	AAAA	2001:67c:1011:1::53
s.de.net.	172800	IN	A	195.243.137.26
s.de.net.	172800	IN	AAAA	2003:8:14::53
;; {	"EDNS-VERSION": 0 }

 

Query to e.root-servers.net for de/DNSKEY

 

Received 736 bytes from 192.203.230.10

 

;; Response received from [192.203.230.10] 736 octets
;; HEADER SECTION
;;	id = 6380
;;	qr = 1	aa = 0	tc = 0	rd = 0	opcode = QUERY
;;	ra = 0	z = 0	ad = 0	cd = 0	rcode = NOERROR
;;	do = 1	co = 0
;;	qdcount = 1	ancount = 0
;;	nscount = 8	arcount = 13

;; {	"EDNS-VERSION":	0,
;;	"FLAGS":	"8000",
;;	"RCODE":	0,
;;	"UDPSIZE":	1472,
;;	"OPTIONS":	[ ]
;;	}

;; QUESTION SECTION (1 record)
;; de.	IN	DNSKEY

;; ANSWER SECTION (0 records)

;; AUTHORITY SECTION (8 records)
de.	172800	IN	NS	a.nic.de.
de.	172800	IN	NS	f.nic.de.
de.	172800	IN	NS	l.de.net.
de.	172800	IN	NS	n.de.net.
de.	172800	IN	NS	s.de.net.
de.	172800	IN	NS	z.nic.de.
de.	86400	IN	DS	( 26755 8 2
	f341357809a5954311ccb82ade114c6c1d724a75c0395137aa3978035425e78d )
de.	86400	IN	RRSIG	( DS 8 1 86400
	20260518220000 20260505210000 54393 .
	l9rLveoLYfo1dEQA3BZL7tVwfDNzYJdefCr1D/nvla3I7CqKczop5WygwqXn3pX+mKCBbvPUi48R
	0wXTiErP6jgi+vJhNKySQyGd3f3BhqXa6MQVLgFu56VBcN7Dlv9oMsonETCUmAJFqGHk4XYeJeQe
	dWi+F4r7TNUp0xiBkgM4ojLQYl8yNFhOjRk4NW7hNamyd4yD7asFYP9P76iKV2FYgO5YNoqglfv5
	KiFrZ8DkUmbpS/fkomZgud1UDGyJcZIX5M4PPfamO+1RAuV0cjb4MR0FBPcmyMp997/h1R6Ria40
	KEFLthQ+oybKI4Vx14m3ul/skXOHSnRUl4pd0Q== )

;; ADDITIONAL SECTION (13 records)
a.nic.de.	172800	IN	A	194.0.0.53
a.nic.de.	172800	IN	AAAA	2001:678:2::53
f.nic.de.	172800	IN	A	81.91.164.5
f.nic.de.	172800	IN	AAAA	2a02:568:0:2::53
l.de.net.	172800	IN	A	77.67.63.105
l.de.net.	172800	IN	AAAA	2001:668:1f:11::105
n.de.net.	172800	IN	A	194.146.107.6
n.de.net.	172800	IN	AAAA	2001:67c:1011:1::53
s.de.net.	172800	IN	A	195.243.137.26
s.de.net.	172800	IN	AAAA	2003:8:14::53
z.nic.de.	172800	IN	A	194.246.96.1
z.nic.de.	172800	IN	AAAA	2a02:568:fe02::de
;; {	"EDNS-VERSION": 0 }

 

Found child zone de

de

 

Checking DS between . and de

 

Query to d.root-servers.net for de/DS

 

Received 366 bytes from 199.7.91.13

 

;; Response received from [199.7.91.13] 366 octets
;; HEADER SECTION
;;	id = 40452
;;	qr = 1	aa = 1	tc = 0	rd = 0	opcode = QUERY
;;	ra = 0	z = 0	ad = 0	cd = 0	rcode = NOERROR
;;	do = 1	co = 0
;;	qdcount = 1	ancount = 2
;;	nscount = 0	arcount = 1

;; {	"EDNS-VERSION":	0,
;;	"FLAGS":	"8000",
;;	"RCODE":	0,
;;	"UDPSIZE":	1450,
;;	"OPTIONS":	[ ]
;;	}

;; QUESTION SECTION (1 record)
;; de.	IN	DS

;; ANSWER SECTION (2 records)
de.	86400	IN	DS	( 26755 8 2
	f341357809a5954311ccb82ade114c6c1d724a75c0395137aa3978035425e78d )
de.	86400	IN	RRSIG	( DS 8 1 86400
	20260518220000 20260505210000 54393 .
	l9rLveoLYfo1dEQA3BZL7tVwfDNzYJdefCr1D/nvla3I7CqKczop5WygwqXn3pX+mKCBbvPUi48R
	0wXTiErP6jgi+vJhNKySQyGd3f3BhqXa6MQVLgFu56VBcN7Dlv9oMsonETCUmAJFqGHk4XYeJeQe
	dWi+F4r7TNUp0xiBkgM4ojLQYl8yNFhOjRk4NW7hNamyd4yD7asFYP9P76iKV2FYgO5YNoqglfv5
	KiFrZ8DkUmbpS/fkomZgud1UDGyJcZIX5M4PPfamO+1RAuV0cjb4MR0FBPcmyMp997/h1R6Ria40
	KEFLthQ+oybKI4Vx14m3ul/skXOHSnRUl4pd0Q== )

;; AUTHORITY SECTION (0 records)

;; ADDITIONAL SECTION (1 record)
;; {	"EDNS-VERSION": 0 }

Found 1 DS records for de in the . zone

DS
=26755/SHA-256
 has algorithm RSASHA256

Found 1 RRSIGs over DS RRset

 

de.	86400	IN	RRSIG	( DS 8 1 86400
	20260518220000 20260505210000 54393 .
	l9rLveoLYfo1dEQA3BZL7tVwfDNzYJdefCr1D/nvla3I7CqKczop5WygwqXn3pX+mKCBbvPUi48R
	0wXTiErP6jgi+vJhNKySQyGd3f3BhqXa6MQVLgFu56VBcN7Dlv9oMsonETCUmAJFqGHk4XYeJeQe
	dWi+F4r7TNUp0xiBkgM4ojLQYl8yNFhOjRk4NW7hNamyd4yD7asFYP9P76iKV2FYgO5YNoqglfv5
	KiFrZ8DkUmbpS/fkomZgud1UDGyJcZIX5M4PPfamO+1RAuV0cjb4MR0FBPcmyMp997/h1R6Ria40
	KEFLthQ+oybKI4Vx14m3ul/skXOHSnRUl4pd0Q== )

RRSIG
=54393
 and DNSKEY
=54393
 verifies the DS RRset

 

DS
=26755/SHA-256
 is now in the chain-of-trust

 

de.	86400	IN	DS	( 26755 8 2
	f341357809a5954311ccb82ade114c6c1d724a75c0395137aa3978035425e78d )

 

Query to a.nic.de for de/DNSKEY

 

Received 745 bytes from 194.0.0.53

 

;; Response received from [194.0.0.53] 745 octets
;; HEADER SECTION
;;	id = 42794
;;	qr = 1	aa = 1	tc = 0	rd = 0	opcode = QUERY
;;	ra = 0	z = 0	ad = 0	cd = 0	rcode = NOERROR
;;	do = 1	co = 0
;;	qdcount = 1	ancount = 3
;;	nscount = 0	arcount = 1

;; {	"EDNS-VERSION":	0,
;;	"FLAGS":	"8000",
;;	"RCODE":	0,
;;	"UDPSIZE":	1452,
;;	"OPTIONS":	[ ]
;;	}

;; QUESTION SECTION (1 record)
;; de.	IN	DNSKEY

;; ANSWER SECTION (3 records)
de.	3600	IN	DNSKEY	( 256 3 8
	AwEAAbTe1PJi8EgIudNGb+KRTxBL2aCu5rXkZ+aIe/TC88pwRdrXYeXODp1ihZWFop5CrbWRBLrk
	/YUPBE8aBc6oJP+58dSkdMLYkjSkmvdvYx+zXnRLWlF2bapxvZxshATJDfGjGbCiWxKEOoyRx3Uh
	ICtHC+cUSddsEvzfacUcBb6n ) ; keytag 32911
de.	3600	IN	DNSKEY	( 257 3 8
	AwEAAbWUSd/QN9Ae543xzdiacY6qbjwtZ21QfmdgxRdm4Z7bjjHWy249uqxCyjjjoS4LDoRDKmj7
	ElffMKvTWKE1qFKu0p8TUy4wyhX0M+m5FUjvQ3CiZMi+qY7GSHA5B+Zd73cidmnTeb3e8lso6jEs
	Xg05/VZ2AyAqWF6FexEIFxIqiwwLk4UP0BwZ17Ur3q1qx9VSbPMyHgQ9d6nHUN1EEJsTDA2v0vKu
	msUyp74ZanRZ/bB/6IzpaaZyr5BLF5pSCNdbRNjVmkwYD0993vm79LueyOeibsoHRc16jhALrIJo
	u1PFjdq7YQsYN0KtqRiJtaAfPprDBREpeamPuW/MnW0= ) ; keytag 26755
de.	3600	IN	RRSIG	( DNSKEY 8 1 3600
	20260519214514 20260505201514 26755 de.
	IWnqDiWjLds8qCj1oGw7tSz4TIC9W1V73DdCueAbne3qL0KynvsCC/o0kLwgW1Pd0Ky99Dv+1cab
	R4Ln4JGZSbYdFJFbMoVdNZt7gKDvgxb5rAWPSZIz9SM/dBwl1ahVm3CXousaSwX81BhS2JuSokXm
	2+WJihVPC8sgwyy8Ir8ESyNjO/V6kaQdeh3CfaO/+4ttKNWDMT+Uv0Bd5oXyFdNWNyoCAk77aiJj
	9LtiCtk8H+9TzCi1MAHdgq+M7VCCe2VuR8oDh7UnhcRMkADm99Lz0nucvK9e2wdoEUkO+fSiWKRv
	5D59D5RTGCJqUu4h2HCobmQoVOwVnuIifoVs9Q== )

;; AUTHORITY SECTION (0 records)

;; ADDITIONAL SECTION (1 record)
;; {	"EDNS-VERSION": 0 }

Found 2 DNSKEY records for de

 

de.	3600	IN	DNSKEY	( 256 3 8
	AwEAAbTe1PJi8EgIudNGb+KRTxBL2aCu5rXkZ+aIe/TC88pwRdrXYeXODp1ihZWFop5CrbWRBLrk
	/YUPBE8aBc6oJP+58dSkdMLYkjSkmvdvYx+zXnRLWlF2bapxvZxshATJDfGjGbCiWxKEOoyRx3Uh
	ICtHC+cUSddsEvzfacUcBb6n ) ; keytag 32911

 

de.	3600	IN	DNSKEY	( 257 3 8
	AwEAAbWUSd/QN9Ae543xzdiacY6qbjwtZ21QfmdgxRdm4Z7bjjHWy249uqxCyjjjoS4LDoRDKmj7
	ElffMKvTWKE1qFKu0p8TUy4wyhX0M+m5FUjvQ3CiZMi+qY7GSHA5B+Zd73cidmnTeb3e8lso6jEs
	Xg05/VZ2AyAqWF6FexEIFxIqiwwLk4UP0BwZ17Ur3q1qx9VSbPMyHgQ9d6nHUN1EEJsTDA2v0vKu
	msUyp74ZanRZ/bB/6IzpaaZyr5BLF5pSCNdbRNjVmkwYD0993vm79LueyOeibsoHRc16jhALrIJo
	u1PFjdq7YQsYN0KtqRiJtaAfPprDBREpeamPuW/MnW0= ) ; keytag 26755

 

DNSKEY
=26755/SEP
 is now in the chain-of-trust

DS
=26755/SHA-256
 verifies DNSKEY
=26755/SEP

Found 1 RRSIGs over DNSKEY RRset

 

de.	3600	IN	RRSIG	( DNSKEY 8 1 3600
	20260519214514 20260505201514 26755 de.
	IWnqDiWjLds8qCj1oGw7tSz4TIC9W1V73DdCueAbne3qL0KynvsCC/o0kLwgW1Pd0Ky99Dv+1cab
	R4Ln4JGZSbYdFJFbMoVdNZt7gKDvgxb5rAWPSZIz9SM/dBwl1ahVm3CXousaSwX81BhS2JuSokXm
	2+WJihVPC8sgwyy8Ir8ESyNjO/V6kaQdeh3CfaO/+4ttKNWDMT+Uv0Bd5oXyFdNWNyoCAk77aiJj
	9LtiCtk8H+9TzCi1MAHdgq+M7VCCe2VuR8oDh7UnhcRMkADm99Lz0nucvK9e2wdoEUkO+fSiWKRv
	5D59D5RTGCJqUu4h2HCobmQoVOwVnuIifoVs9Q== )

RRSIG
=26755
 and DNSKEY
=26755/SEP
 verifies the DNSKEY RRset

 

DNSKEY
=32911
 is now in the chain-of-trust

 

Query to z.nic.de for nic.de/A

 

Received 464 bytes from 194.246.96.1

 

;; Response received from [194.246.96.1] 464 octets
;; HEADER SECTION
;;	id = 39381
;;	qr = 1	aa = 0	tc = 0	rd = 0	opcode = QUERY
;;	ra = 0	z = 0	ad = 0	cd = 0	rcode = NOERROR
;;	do = 1	co = 0
;;	qdcount = 1	ancount = 0
;;	nscount = 6	arcount = 7

;; {	"EDNS-VERSION":	0,
;;	"FLAGS":	"8000",
;;	"RCODE":	0,
;;	"UDPSIZE":	1452,
;;	"OPTIONS":	[ ]
;;	}

;; QUESTION SECTION (1 record)
;; nic.de.	IN	A

;; ANSWER SECTION (0 records)

;; AUTHORITY SECTION (6 records)
nic.de.	86400	IN	NS	ns1.denic.de.
nic.de.	86400	IN	NS	ns2.denic.de.
nic.de.	86400	IN	NS	ns3.denic.de.
nic.de.	86400	IN	NS	ns4.denic.net.
nic.de.	86400	IN	DS	( 26155 8 2
	2f06c8cdf8673a2e98d72c8b7ab6067d9318458b3d9edccde1c5ef793c0c565d )
nic.de.	86400	IN	RRSIG	( DS 8 2 86400
	20260519214514 20260505201514 32911 de.
	U5wHLSgRY9ElxiaIyUhDHXpxTtP01LpuDzsofEvxv4hUm1ZNleSG/mrL2eJtTzSQQwC1chiWd4c0
	dCxOKBht4AzbafQv2jkE1nLxKUndTD8p48mclnF1DaYBZwMW+PsKFa3BGVmmK2vYcQMSXBfTgB9q
	g7nhUWc+0mIXc1VcNbY= )

;; ADDITIONAL SECTION (7 records)
ns1.denic.de.	86400	IN	A	77.67.63.106
ns1.denic.de.	86400	IN	AAAA	2001:668:1f:11::106
ns2.denic.de.	86400	IN	A	81.91.164.6
ns2.denic.de.	86400	IN	AAAA	2a02:568:0:2::54
ns3.denic.de.	86400	IN	A	195.243.137.27
ns3.denic.de.	86400	IN	AAAA	2003:8:14::106
;; {	"EDNS-VERSION": 0 }

 

Query to s.de.net for nic.de/DNSKEY

 

Received 464 bytes from 195.243.137.26

 

;; Response received from [195.243.137.26] 464 octets
;; HEADER SECTION
;;	id = 27127
;;	qr = 1	aa = 0	tc = 0	rd = 0	opcode = QUERY
;;	ra = 0	z = 0	ad = 0	cd = 0	rcode = NOERROR
;;	do = 1	co = 0
;;	qdcount = 1	ancount = 0
;;	nscount = 6	arcount = 7

;; {	"EDNS-VERSION":	0,
;;	"FLAGS":	"8000",
;;	"RCODE":	0,
;;	"UDPSIZE":	1452,
;;	"OPTIONS":	[ ]
;;	}

;; QUESTION SECTION (1 record)
;; nic.de.	IN	DNSKEY

;; ANSWER SECTION (0 records)

;; AUTHORITY SECTION (6 records)
nic.de.	86400	IN	NS	ns1.denic.de.
nic.de.	86400	IN	NS	ns2.denic.de.
nic.de.	86400	IN	NS	ns3.denic.de.
nic.de.	86400	IN	NS	ns4.denic.net.
nic.de.	86400	IN	DS	( 26155 8 2
	2f06c8cdf8673a2e98d72c8b7ab6067d9318458b3d9edccde1c5ef793c0c565d )
nic.de.	86400	IN	RRSIG	( DS 8 2 86400
	20260519214514 20260505201514 32911 de.
	U5wHLSgRY9ElxiaIyUhDHXpxTtP01LpuDzsofEvxv4hUm1ZNleSG/mrL2eJtTzSQQwC1chiWd4c0
	dCxOKBht4AzbafQv2jkE1nLxKUndTD8p48mclnF1DaYBZwMW+PsKFa3BGVmmK2vYcQMSXBfTgB9q
	g7nhUWc+0mIXc1VcNbY= )

;; ADDITIONAL SECTION (7 records)
ns1.denic.de.	86400	IN	A	77.67.63.106
ns1.denic.de.	86400	IN	AAAA	2001:668:1f:11::106
ns2.denic.de.	86400	IN	A	81.91.164.6
ns2.denic.de.	86400	IN	AAAA	2a02:568:0:2::54
ns3.denic.de.	86400	IN	A	195.243.137.27
ns3.denic.de.	86400	IN	AAAA	2003:8:14::106
;; {	"EDNS-VERSION": 0 }

 

Found child zone nic.de

nic.de

 

Checking DS between de and nic.de

 

Query to n.de.net for nic.de/DS

 

Received 245 bytes from 194.146.107.6

 

;; Response received from [194.146.107.6] 245 octets
;; HEADER SECTION
;;	id = 31281
;;	qr = 1	aa = 1	tc = 0	rd = 0	opcode = QUERY
;;	ra = 0	z = 0	ad = 0	cd = 0	rcode = NOERROR
;;	do = 1	co = 0
;;	qdcount = 1	ancount = 2
;;	nscount = 0	arcount = 1

;; {	"EDNS-VERSION":	0,
;;	"FLAGS":	"8000",
;;	"RCODE":	0,
;;	"UDPSIZE":	4096,
;;	"OPTIONS":	[ ]
;;	}

;; QUESTION SECTION (1 record)
;; nic.de.	IN	DS

;; ANSWER SECTION (2 records)
nic.de.	86400	IN	DS	( 26155 8 2
	2f06c8cdf8673a2e98d72c8b7ab6067d9318458b3d9edccde1c5ef793c0c565d )
nic.de.	86400	IN	RRSIG	( DS 8 2 86400
	20260519214514 20260505201514 32911 de.
	U5wHLSgRY9ElxiaIyUhDHXpxTtP01LpuDzsofEvxv4hUm1ZNleSG/mrL2eJtTzSQQwC1chiWd4c0
	dCxOKBht4AzbafQv2jkE1nLxKUndTD8p48mclnF1DaYBZwMW+PsKFa3BGVmmK2vYcQMSXBfTgB9q
	g7nhUWc+0mIXc1VcNbY= )

;; AUTHORITY SECTION (0 records)

;; ADDITIONAL SECTION (1 record)
;; {	"EDNS-VERSION": 0 }

Found 1 DS records for nic.de in the de zone

DS
=26155/SHA-256
 has algorithm RSASHA256

Found 1 RRSIGs over DS RRset

 

nic.de.	86400	IN	RRSIG	( DS 8 2 86400
	20260519214514 20260505201514 32911 de.
	U5wHLSgRY9ElxiaIyUhDHXpxTtP01LpuDzsofEvxv4hUm1ZNleSG/mrL2eJtTzSQQwC1chiWd4c0
	dCxOKBht4AzbafQv2jkE1nLxKUndTD8p48mclnF1DaYBZwMW+PsKFa3BGVmmK2vYcQMSXBfTgB9q
	g7nhUWc+0mIXc1VcNbY= )

RRSIG
=32911
 and DNSKEY
=32911
 verifies the DS RRset

 

DS
=26155/SHA-256
 is now in the chain-of-trust

 

nic.de.	86400	IN	DS	( 26155 8 2
	2f06c8cdf8673a2e98d72c8b7ab6067d9318458b3d9edccde1c5ef793c0c565d )

 

Query to ns4.denic.net for nic.de/DNSKEY

 

Received 625 bytes from 194.246.96.28

 

;; Response received from [194.246.96.28] 625 octets
;; HEADER SECTION
;;	id = 35356
;;	qr = 1	aa = 1	tc = 0	rd = 0	opcode = QUERY
;;	ra = 0	z = 0	ad = 0	cd = 0	rcode = NOERROR
;;	do = 1	co = 0
;;	qdcount = 1	ancount = 3
;;	nscount = 0	arcount = 1

;; {	"EDNS-VERSION":	0,
;;	"FLAGS":	"8000",
;;	"RCODE":	0,
;;	"UDPSIZE":	1452,
;;	"OPTIONS":	[ ]
;;	}

;; QUESTION SECTION (1 record)
;; nic.de.	IN	DNSKEY

;; ANSWER SECTION (3 records)
nic.de.	3600	IN	DNSKEY	( 257 3 8
	AwEAAb/xrM2MD+xm84YNYby6TxkMaC6PtzF2bB9WBB7ux7iqzhViob4GKvQ6L7CkXjyAxfKbTzrd
	vXoAPpsAPW4pkThReDAVp3QxvUKrkBM8/uWRF3wpaUoPsAHm1dbcL9aiW3lqlLMZjDEwDfU6lxLc
	Pg9d14fq4dc44FvPx6aYcymkgJoYvR6P1wECpxqlEAR2K1cvMtqCqvVESBQV/EUtWiALNuwR2Pbh
	wtBWJd+e8BdFI7OLkit4uYYux6Yu35uyGQ== ) ; keytag 26155
nic.de.	3600	IN	DNSKEY	( 256 3 8
	AwEAAdkJ06nJ8Cutng7f9HACMUhuYnF0CX7uCZ06CyauTxQIpOQpQBKI03/EPn8fI518pvOqxAO7
	XWaGsSovRyI3UPd963JZpYrEOcVDFPA2Qrz5eFj8MIBKH6HcQGnum0UFxmIRVaKT5K5WM+xeUeP5
	Xr4P54Jkyo18rz0LwzDp9gjj ) ; keytag 36463
nic.de.	3600	IN	RRSIG	( DNSKEY 8 2 3600
	20260519222346 20260505205346 26155 nic.de.
	A9juKIutxX6EOcUH28owCNyrs8s3lURep4erGgFDmiJDlRLXk0bg3H3gtwePh/NsfI3msQ9zNAfE
	gz/MsLnRUp8ViFd3sJTkm5+nHNWPzw8x0h8qKMU6/BM4bG8hZxxaUByErVBgp1KH+FiLAXyKMPwo
	LY62iVJoL9H8LBD1M4e2RdNYP428pUwQbnC38HQwR7yXbRqEPdEtNVp04pd/aTcXo8Fx23J83wK+
	TYiPMeiwOJKwUwrKoChBuvaI5j2Q )

;; AUTHORITY SECTION (0 records)

;; ADDITIONAL SECTION (1 record)
;; {	"EDNS-VERSION": 0 }

Found 2 DNSKEY records for nic.de

 

nic.de.	3600	IN	DNSKEY	( 257 3 8
	AwEAAb/xrM2MD+xm84YNYby6TxkMaC6PtzF2bB9WBB7ux7iqzhViob4GKvQ6L7CkXjyAxfKbTzrd
	vXoAPpsAPW4pkThReDAVp3QxvUKrkBM8/uWRF3wpaUoPsAHm1dbcL9aiW3lqlLMZjDEwDfU6lxLc
	Pg9d14fq4dc44FvPx6aYcymkgJoYvR6P1wECpxqlEAR2K1cvMtqCqvVESBQV/EUtWiALNuwR2Pbh
	wtBWJd+e8BdFI7OLkit4uYYux6Yu35uyGQ== ) ; keytag 26155

 

nic.de.	3600	IN	DNSKEY	( 256 3 8
	AwEAAdkJ06nJ8Cutng7f9HACMUhuYnF0CX7uCZ06CyauTxQIpOQpQBKI03/EPn8fI518pvOqxAO7
	XWaGsSovRyI3UPd963JZpYrEOcVDFPA2Qrz5eFj8MIBKH6HcQGnum0UFxmIRVaKT5K5WM+xeUeP5
	Xr4P54Jkyo18rz0LwzDp9gjj ) ; keytag 36463

 

DNSKEY
=26155/SEP
 is now in the chain-of-trust

DS
=26155/SHA-256
 verifies DNSKEY
=26155/SEP

Found 1 RRSIGs over DNSKEY RRset

 

nic.de.	3600	IN	RRSIG	( DNSKEY 8 2 3600
	20260519222346 20260505205346 26155 nic.de.
	A9juKIutxX6EOcUH28owCNyrs8s3lURep4erGgFDmiJDlRLXk0bg3H3gtwePh/NsfI3msQ9zNAfE
	gz/MsLnRUp8ViFd3sJTkm5+nHNWPzw8x0h8qKMU6/BM4bG8hZxxaUByErVBgp1KH+FiLAXyKMPwo
	LY62iVJoL9H8LBD1M4e2RdNYP428pUwQbnC38HQwR7yXbRqEPdEtNVp04pd/aTcXo8Fx23J83wK+
	TYiPMeiwOJKwUwrKoChBuvaI5j2Q )

RRSIG
=26155
 and DNSKEY
=26155/SEP
 verifies the DNSKEY RRset

 

DNSKEY
=36463
 is now in the chain-of-trust

 

Query to ns3.denic.de for nic.de/A

 

Received 472 bytes from 195.243.137.27

 

;; Response received from [195.243.137.27] 472 octets
;; HEADER SECTION
;;	id = 61125
;;	qr = 1	aa = 1	tc = 0	rd = 0	opcode = QUERY
;;	ra = 0	z = 0	ad = 0	cd = 0	rcode = NOERROR
;;	do = 1	co = 0
;;	qdcount = 1	ancount = 2
;;	nscount = 5	arcount = 1

;; {	"EDNS-VERSION":	0,
;;	"FLAGS":	"8000",
;;	"RCODE":	0,
;;	"UDPSIZE":	1452,
;;	"OPTIONS":	[ ]
;;	}

;; QUESTION SECTION (1 record)
;; nic.de.	IN	A

;; ANSWER SECTION (2 records)
nic.de.	3600	IN	A	81.91.170.12
nic.de.	3600	IN	RRSIG	( A 8 2 3600
	20260519222346 20260505205346 36463 nic.de.
	VIyuPDO6Bf029ILioOvWPhkPmQctDIepz+bK/7s7GS1hHEIZrs/9pDGblfW19sjmVpJGIslYmiGh
	QUDTgJcv8lcWqrfUK3pTv9QxmYRDOMM/zTZz50hqfcNkvzL7dg/7A/yPoPk3aTMXH3pFNY0N2RnU
	t8THHOfUcu3w19fma4w= )

;; AUTHORITY SECTION (5 records)
nic.de.	86400	IN	NS	ns1.denic.de.
nic.de.	86400	IN	NS	ns3.denic.de.
nic.de.	86400	IN	NS	ns2.denic.de.
nic.de.	86400	IN	NS	ns4.denic.net.
nic.de.	86400	IN	RRSIG	( NS 8 2 86400
	20260519222346 20260505205346 36463 nic.de.
	XRxm7kMf59qAC8lR30mFXw9cPG31kCiBE6v02bb/GHj1kbk+p0u4BgATaVI9S17xQlL3Az2kXpI8
	FOIOEQciY7oTmIzo6jOPIEDGvpTXhtKBbybLyNizyR7sScaXfNT12Wi+HC7iglTkjhLDQZMUIY/W
	T+sw+7dyrAi/cGboYmI= )

;; ADDITIONAL SECTION (1 record)
;; {	"EDNS-VERSION": 0 }

ns3.denic.de is authoritative for nic.de

 

Found RRSIG signed by nic.de zone

 

Query to ns1.denic.de for nic.de/SOA

 

Received 507 bytes from 77.67.63.106

 

;; Response received from [77.67.63.106] 507 octets
;; HEADER SECTION
;;	id = 22877
;;	qr = 1	aa = 1	tc = 0	rd = 0	opcode = QUERY
;;	ra = 0	z = 0	ad = 0	cd = 0	rcode = NOERROR
;;	do = 1	co = 0
;;	qdcount = 1	ancount = 2
;;	nscount = 5	arcount = 1

;; {	"EDNS-VERSION":	0,
;;	"FLAGS":	"8000",
;;	"RCODE":	0,
;;	"UDPSIZE":	1452,
;;	"OPTIONS":	[ ]
;;	}

;; QUESTION SECTION (1 record)
;; nic.de.	IN	SOA

;; ANSWER SECTION (2 records)
nic.de.	3600	IN	SOA	( ns1.denic.de. dns-operations.denic.de.
				1778019826	;serial
				10800		;refresh
				1800		;retry
				3600000		;expire
				1800		;minimum
	)
nic.de.	3600	IN	RRSIG	( SOA 8 2 3600
	20260519222346 20260505205346 36463 nic.de.
	gybWmV8z8VXzZWGVrEfO4VSy0RTz2VqULlxMyzcIJ+jdEu741OPt3L4ayB5hLA0szmykNTD9srof
	oENcUHGW9UDlEINQvhszOKGc24HIENajgZCv5wG9FHpQ5KqTpGVn9oy2qgJAWs9jQpd/XiFTuNah
	xXe6rHMUfhazTCzJwno= )

;; AUTHORITY SECTION (5 records)
nic.de.	86400	IN	NS	ns4.denic.net.
nic.de.	86400	IN	NS	ns3.denic.de.
nic.de.	86400	IN	NS	ns1.denic.de.
nic.de.	86400	IN	NS	ns2.denic.de.
nic.de.	86400	IN	RRSIG	( NS 8 2 86400
	20260519222346 20260505205346 36463 nic.de.
	XRxm7kMf59qAC8lR30mFXw9cPG31kCiBE6v02bb/GHj1kbk+p0u4BgATaVI9S17xQlL3Az2kXpI8
	FOIOEQciY7oTmIzo6jOPIEDGvpTXhtKBbybLyNizyR7sScaXfNT12Wi+HC7iglTkjhLDQZMUIY/W
	T+sw+7dyrAi/cGboYmI= )

;; ADDITIONAL SECTION (1 record)
;; {	"EDNS-VERSION": 0 }

 

Query to ns4.denic.net for nic.de/SOA

 

Received 507 bytes from 194.246.96.28

 

;; Response received from [194.246.96.28] 507 octets
;; HEADER SECTION
;;	id = 12972
;;	qr = 1	aa = 1	tc = 0	rd = 0	opcode = QUERY
;;	ra = 0	z = 0	ad = 0	cd = 0	rcode = NOERROR
;;	do = 1	co = 0
;;	qdcount = 1	ancount = 2
;;	nscount = 5	arcount = 1

;; {	"EDNS-VERSION":	0,
;;	"FLAGS":	"8000",
;;	"RCODE":	0,
;;	"UDPSIZE":	1452,
;;	"OPTIONS":	[ ]
;;	}

;; QUESTION SECTION (1 record)
;; nic.de.	IN	SOA

;; ANSWER SECTION (2 records)
nic.de.	3600	IN	SOA	( ns1.denic.de. dns-operations.denic.de.
				1778019826	;serial
				10800		;refresh
				1800		;retry
				3600000		;expire
				1800		;minimum
	)
nic.de.	3600	IN	RRSIG	( SOA 8 2 3600
	20260519222346 20260505205346 36463 nic.de.
	gybWmV8z8VXzZWGVrEfO4VSy0RTz2VqULlxMyzcIJ+jdEu741OPt3L4ayB5hLA0szmykNTD9srof
	oENcUHGW9UDlEINQvhszOKGc24HIENajgZCv5wG9FHpQ5KqTpGVn9oy2qgJAWs9jQpd/XiFTuNah
	xXe6rHMUfhazTCzJwno= )

;; AUTHORITY SECTION (5 records)
nic.de.	86400	IN	NS	ns1.denic.de.
nic.de.	86400	IN	NS	ns4.denic.net.
nic.de.	86400	IN	NS	ns3.denic.de.
nic.de.	86400	IN	NS	ns2.denic.de.
nic.de.	86400	IN	RRSIG	( NS 8 2 86400
	20260519222346 20260505205346 36463 nic.de.
	XRxm7kMf59qAC8lR30mFXw9cPG31kCiBE6v02bb/GHj1kbk+p0u4BgATaVI9S17xQlL3Az2kXpI8
	FOIOEQciY7oTmIzo6jOPIEDGvpTXhtKBbybLyNizyR7sScaXfNT12Wi+HC7iglTkjhLDQZMUIY/W
	T+sw+7dyrAi/cGboYmI= )

;; ADDITIONAL SECTION (1 record)
;; {	"EDNS-VERSION": 0 }

 

Query to ns2.denic.de for nic.de/SOA

 

Received 507 bytes from 81.91.164.6

 

;; Response received from [81.91.164.6] 507 octets
;; HEADER SECTION
;;	id = 28567
;;	qr = 1	aa = 1	tc = 0	rd = 0	opcode = QUERY
;;	ra = 0	z = 0	ad = 0	cd = 0	rcode = NOERROR
;;	do = 1	co = 0
;;	qdcount = 1	ancount = 2
;;	nscount = 5	arcount = 1

;; {	"EDNS-VERSION":	0,
;;	"FLAGS":	"8000",
;;	"RCODE":	0,
;;	"UDPSIZE":	1452,
;;	"OPTIONS":	[ ]
;;	}

;; QUESTION SECTION (1 record)
;; nic.de.	IN	SOA

;; ANSWER SECTION (2 records)
nic.de.	3600	IN	SOA	( ns1.denic.de. dns-operations.denic.de.
				1778019826	;serial
				10800		;refresh
				1800		;retry
				3600000		;expire
				1800		;minimum
	)
nic.de.	3600	IN	RRSIG	( SOA 8 2 3600
	20260519222346 20260505205346 36463 nic.de.
	gybWmV8z8VXzZWGVrEfO4VSy0RTz2VqULlxMyzcIJ+jdEu741OPt3L4ayB5hLA0szmykNTD9srof
	oENcUHGW9UDlEINQvhszOKGc24HIENajgZCv5wG9FHpQ5KqTpGVn9oy2qgJAWs9jQpd/XiFTuNah
	xXe6rHMUfhazTCzJwno= )

;; AUTHORITY SECTION (5 records)
nic.de.	86400	IN	NS	ns2.denic.de.
nic.de.	86400	IN	NS	ns4.denic.net.
nic.de.	86400	IN	NS	ns1.denic.de.
nic.de.	86400	IN	NS	ns3.denic.de.
nic.de.	86400	IN	RRSIG	( NS 8 2 86400
	20260519222346 20260505205346 36463 nic.de.
	XRxm7kMf59qAC8lR30mFXw9cPG31kCiBE6v02bb/GHj1kbk+p0u4BgATaVI9S17xQlL3Az2kXpI8
	FOIOEQciY7oTmIzo6jOPIEDGvpTXhtKBbybLyNizyR7sScaXfNT12Wi+HC7iglTkjhLDQZMUIY/W
	T+sw+7dyrAi/cGboYmI= )

;; ADDITIONAL SECTION (1 record)
;; {	"EDNS-VERSION": 0 }

 

Query to ns3.denic.de for nic.de/A

nic.de A RR has value 81.91.170.12

Found 1 RRSIGs over A RRset

 

nic.de.	3600	IN	RRSIG	( A 8 2 3600
	20260519222346 20260505205346 36463 nic.de.
	VIyuPDO6Bf029ILioOvWPhkPmQctDIepz+bK/7s7GS1hHEIZrs/9pDGblfW19sjmVpJGIslYmiGh
	QUDTgJcv8lcWqrfUK3pTv9QxmYRDOMM/zTZz50hqfcNkvzL7dg/7A/yPoPk3aTMXH3pFNY0N2RnU
	t8THHOfUcu3w19fma4w= )

RRSIG
=36463
 and DNSKEY
=36463
 verifies the A RRset

nic.de

 

Query to ns1.denic.de for nic.de/A

 

Received 472 bytes from 77.67.63.106

 

;; Response received from [77.67.63.106] 472 octets
;; HEADER SECTION
;;	id = 22436
;;	qr = 1	aa = 1	tc = 0	rd = 0	opcode = QUERY
;;	ra = 0	z = 0	ad = 0	cd = 0	rcode = NOERROR
;;	do = 1	co = 0
;;	qdcount = 1	ancount = 2
;;	nscount = 5	arcount = 1

;; {	"EDNS-VERSION":	0,
;;	"FLAGS":	"8000",
;;	"RCODE":	0,
;;	"UDPSIZE":	1452,
;;	"OPTIONS":	[ ]
;;	}

;; QUESTION SECTION (1 record)
;; nic.de.	IN	A

;; ANSWER SECTION (2 records)
nic.de.	3600	IN	A	81.91.170.12
nic.de.	3600	IN	RRSIG	( A 8 2 3600
	20260519222346 20260505205346 36463 nic.de.
	VIyuPDO6Bf029ILioOvWPhkPmQctDIepz+bK/7s7GS1hHEIZrs/9pDGblfW19sjmVpJGIslYmiGh
	QUDTgJcv8lcWqrfUK3pTv9QxmYRDOMM/zTZz50hqfcNkvzL7dg/7A/yPoPk3aTMXH3pFNY0N2RnU
	t8THHOfUcu3w19fma4w= )

;; AUTHORITY SECTION (5 records)
nic.de.	86400	IN	NS	ns2.denic.de.
nic.de.	86400	IN	NS	ns3.denic.de.
nic.de.	86400	IN	NS	ns4.denic.net.
nic.de.	86400	IN	NS	ns1.denic.de.
nic.de.	86400	IN	RRSIG	( NS 8 2 86400
	20260519222346 20260505205346 36463 nic.de.
	XRxm7kMf59qAC8lR30mFXw9cPG31kCiBE6v02bb/GHj1kbk+p0u4BgATaVI9S17xQlL3Az2kXpI8
	FOIOEQciY7oTmIzo6jOPIEDGvpTXhtKBbybLyNizyR7sScaXfNT12Wi+HC7iglTkjhLDQZMUIY/W
	T+sw+7dyrAi/cGboYmI= )

;; ADDITIONAL SECTION (1 record)
;; {	"EDNS-VERSION": 0 }

ns1.denic.de is authoritative for nic.de

 

Found RRSIG signed by nic.de zone

 

Query to ns1.denic.de for nic.de/A

nic.de A RR has value 81.91.170.12

Found 1 RRSIGs over A RRset

 

nic.de.	3600	IN	RRSIG	( A 8 2 3600
	20260519222346 20260505205346 36463 nic.de.
	VIyuPDO6Bf029ILioOvWPhkPmQctDIepz+bK/7s7GS1hHEIZrs/9pDGblfW19sjmVpJGIslYmiGh
	QUDTgJcv8lcWqrfUK3pTv9QxmYRDOMM/zTZz50hqfcNkvzL7dg/7A/yPoPk3aTMXH3pFNY0N2RnU
	t8THHOfUcu3w19fma4w= )

RRSIG
=36463
 and DNSKEY
=36463
 verifies the A RRset

nic.de

 

Query to ns4.denic.net for nic.de/A

 

Received 472 bytes from 194.246.96.28

 

;; Response received from [194.246.96.28] 472 octets
;; HEADER SECTION
;;	id = 16084
;;	qr = 1	aa = 1	tc = 0	rd = 0	opcode = QUERY
;;	ra = 0	z = 0	ad = 0	cd = 0	rcode = NOERROR
;;	do = 1	co = 0
;;	qdcount = 1	ancount = 2
;;	nscount = 5	arcount = 1

;; {	"EDNS-VERSION":	0,
;;	"FLAGS":	"8000",
;;	"RCODE":	0,
;;	"UDPSIZE":	1452,
;;	"OPTIONS":	[ ]
;;	}

;; QUESTION SECTION (1 record)
;; nic.de.	IN	A

;; ANSWER SECTION (2 records)
nic.de.	3600	IN	A	81.91.170.12
nic.de.	3600	IN	RRSIG	( A 8 2 3600
	20260519222346 20260505205346 36463 nic.de.
	VIyuPDO6Bf029ILioOvWPhkPmQctDIepz+bK/7s7GS1hHEIZrs/9pDGblfW19sjmVpJGIslYmiGh
	QUDTgJcv8lcWqrfUK3pTv9QxmYRDOMM/zTZz50hqfcNkvzL7dg/7A/yPoPk3aTMXH3pFNY0N2RnU
	t8THHOfUcu3w19fma4w= )

;; AUTHORITY SECTION (5 records)
nic.de.	86400	IN	NS	ns2.denic.de.
nic.de.	86400	IN	NS	ns1.denic.de.
nic.de.	86400	IN	NS	ns4.denic.net.
nic.de.	86400	IN	NS	ns3.denic.de.
nic.de.	86400	IN	RRSIG	( NS 8 2 86400
	20260519222346 20260505205346 36463 nic.de.
	XRxm7kMf59qAC8lR30mFXw9cPG31kCiBE6v02bb/GHj1kbk+p0u4BgATaVI9S17xQlL3Az2kXpI8
	FOIOEQciY7oTmIzo6jOPIEDGvpTXhtKBbybLyNizyR7sScaXfNT12Wi+HC7iglTkjhLDQZMUIY/W
	T+sw+7dyrAi/cGboYmI= )

;; ADDITIONAL SECTION (1 record)
;; {	"EDNS-VERSION": 0 }

ns4.denic.net is authoritative for nic.de

 

Found RRSIG signed by nic.de zone

 

Query to ns4.denic.net for nic.de/A

nic.de A RR has value 81.91.170.12

Found 1 RRSIGs over A RRset

 

nic.de.	3600	IN	RRSIG	( A 8 2 3600
	20260519222346 20260505205346 36463 nic.de.
	VIyuPDO6Bf029ILioOvWPhkPmQctDIepz+bK/7s7GS1hHEIZrs/9pDGblfW19sjmVpJGIslYmiGh
	QUDTgJcv8lcWqrfUK3pTv9QxmYRDOMM/zTZz50hqfcNkvzL7dg/7A/yPoPk3aTMXH3pFNY0N2RnU
	t8THHOfUcu3w19fma4w= )

RRSIG
=36463
 and DNSKEY
=36463
 verifies the A RRset

nic.de

 

Query to ns2.denic.de for nic.de/A

 

Received 472 bytes from 81.91.164.6

 

;; Response received from [81.91.164.6] 472 octets
;; HEADER SECTION
;;	id = 7550
;;	qr = 1	aa = 1	tc = 0	rd = 0	opcode = QUERY
;;	ra = 0	z = 0	ad = 0	cd = 0	rcode = NOERROR
;;	do = 1	co = 0
;;	qdcount = 1	ancount = 2
;;	nscount = 5	arcount = 1

;; {	"EDNS-VERSION":	0,
;;	"FLAGS":	"8000",
;;	"RCODE":	0,
;;	"UDPSIZE":	1452,
;;	"OPTIONS":	[ ]
;;	}

;; QUESTION SECTION (1 record)
;; nic.de.	IN	A

;; ANSWER SECTION (2 records)
nic.de.	3600	IN	A	81.91.170.12
nic.de.	3600	IN	RRSIG	( A 8 2 3600
	20260519222346 20260505205346 36463 nic.de.
	VIyuPDO6Bf029ILioOvWPhkPmQctDIepz+bK/7s7GS1hHEIZrs/9pDGblfW19sjmVpJGIslYmiGh
	QUDTgJcv8lcWqrfUK3pTv9QxmYRDOMM/zTZz50hqfcNkvzL7dg/7A/yPoPk3aTMXH3pFNY0N2RnU
	t8THHOfUcu3w19fma4w= )

;; AUTHORITY SECTION (5 records)
nic.de.	86400	IN	NS	ns2.denic.de.
nic.de.	86400	IN	NS	ns1.denic.de.
nic.de.	86400	IN	NS	ns4.denic.net.
nic.de.	86400	IN	NS	ns3.denic.de.
nic.de.	86400	IN	RRSIG	( NS 8 2 86400
	20260519222346 20260505205346 36463 nic.de.
	XRxm7kMf59qAC8lR30mFXw9cPG31kCiBE6v02bb/GHj1kbk+p0u4BgATaVI9S17xQlL3Az2kXpI8
	FOIOEQciY7oTmIzo6jOPIEDGvpTXhtKBbybLyNizyR7sScaXfNT12Wi+HC7iglTkjhLDQZMUIY/W
	T+sw+7dyrAi/cGboYmI= )

;; ADDITIONAL SECTION (1 record)
;; {	"EDNS-VERSION": 0 }

ns2.denic.de is authoritative for nic.de

 

Found RRSIG signed by nic.de zone

 

Query to ns2.denic.de for nic.de/A

nic.de A RR has value 81.91.170.12

Found 1 RRSIGs over A RRset

 

nic.de.	3600	IN	RRSIG	( A 8 2 3600
	20260519222346 20260505205346 36463 nic.de.
	VIyuPDO6Bf029ILioOvWPhkPmQctDIepz+bK/7s7GS1hHEIZrs/9pDGblfW19sjmVpJGIslYmiGh
	QUDTgJcv8lcWqrfUK3pTv9QxmYRDOMM/zTZz50hqfcNkvzL7dg/7A/yPoPk3aTMXH3pFNY0N2RnU
	t8THHOfUcu3w19fma4w= )

RRSIG
=36463
 and DNSKEY
=36463
 verifies the A RRset

Move your mouse over anyorsymbols for remediation hints.

Want a second opinion? Test nic.de atdnsviz.net.

 
 
DNSSEC Debugger

↓ Advanced options↑ Advanced options

Trust Anchor: 
 
Name Servers:
 

Paste a DS or DNSKEY record into the field above to use a Trust Anchor that is not published in the DNS. Validation will begin at the owner name of the DS/DNSKEY record.

You may also supply alternative starting name servers, separated by whitespace or commas. The given name servers must be authoritative for the same zone as the Trust Anchor.

 

Legal Notices
//
Privacy
//
Repository
//
Contact Us
//
Site Map

 © 2011-2026
 VeriSign, Inc. All rights reserved.
VERISIGN, the VERISIGN logo, and other trademarks, service marks, and designs are registered or unregistered trademarks of VeriSign, Inc. and its subsidiaries in the United States and in foreign countries. All other trademarks are property of their respective owners.
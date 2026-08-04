---
title: 'GitHub - icedracon/adhammer: Active Directory security-assessment toolkit in Rust — PingCastle-class audit + authorized red-team validation, on a from-scratch DCE/RPC · NTLM · SMB2 · Kerberos stack. One static binary, from Kali or Windows. · GitHub'
url: https://github.com/icedracon/adhammer
site_name: tldr
content_file: tldr-github-icedraconadhammer-active-directory-security
fetched_at: '2026-08-04T19:34:12.342620'
original_url: https://github.com/icedracon/adhammer
date: '2026-08-04'
description: Active Directory security-assessment toolkit in Rust — PingCastle-class audit + authorized red-team validation, on a from-scratch DCE/RPC · NTLM · SMB2 · Kerberos stack. One static binary, from Kali or Windows. - icedracon/adhammer
tags:
- tldr
---

icedracon

 

/

adhammer

Public

* NotificationsYou must be signed in to change notification settings
* Fork4
* Star58

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

71 Commits
71 Commits
.github/
workflows
.github/
workflows
 
 
cli
cli
 
 
crates
crates
 
 
docs
docs
 
 
fuzz
fuzz
 
 
lab
lab
 
 
.gitignore
.gitignore
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
ROADMAP.md
ROADMAP.md
 
 
SECURITY.md
SECURITY.md
 
 
VECTORS.md
VECTORS.md
 
 
View all files

## Repository files navigation

# ADhammer

AnActive Directory security-assessmenttoolkit in Rust: a PingCastle-class auditor that maps
a domain's attack paths — scored, graphed, and MITRE-tagged — then, for authorized red-team and
research use,provesthose paths end-to-end. One static binary, from Kali/Linux or Windows, on
an embedded from-scratch DCE/RPC · NTLM · SMB2 · Kerberos stack (the "impacket for Rust" that
didn't otherwise exist).

Built as security research (ITMO); sibling to a Windows kernel 0-day disclosed to Microsoft MSRC.
Forauthorized engagements, red-team validation, and educationonly.

Authorized use only.The validation modules implement working offensive techniques (DCSync,
golden/silver tickets, pass-the-ticket, NTLM relay, ADCS abuse, RCE). Use ADhammer only against
systems you own or are explicitly authorized to test. SeeSECURITY.md.

📝Write-up:I built a full AD pentest + audit tool in Rust — on a protocol stack I wrote from scratch (no impacket)

Built and run onKali Linux— a cleangit clone+cargo build(cargo 1.95, ~38s) with 100+ unit tests green. Every screen above is real--helpoutput from the compiled binary.

## How it works

1 — Audit.ADhammer collects a domain over LDAP as a low-privileged user (via theSD_FLAGScontrol), builds a BloodHound-style control-path graph in-process, and runs41 checksacross
the four PingCastle categories — including15 of the 16 AD CS ESC classes, ADIDNS exposure,
and SYSVOL/GPP — scoring and MITRE-tagging every finding, exportable to BloodHound.

2 — Validate.A report shouldn't say a pathmightbe exploitable. On its native protocol
stack ADhammer implements the matching tradecraft — Kerberos roasting, coercion, RBCD, Shadow
Credentials, DCSync, golden/silver tickets, pass-the-ticket, LAPS read, WinRM/SVCCTL exec, ADCS
enrollment — eachlive-validated against a fully-patched Windows Server 2025 DC.

One Rust binary on Kali, live against a Windows DC:auditthe DC's NTLM-relay posture →safely detect Zerologon(CVE-2020-1472, no reset) →DCSyncthe krbtgt key →forge a golden ticket→pass-the-ticketover SMB to code-exec asNT AUTHORITY\SYSTEM. The same tradecraft is live-validated against a fully-patchedServer 2025DC (see thewrite-up).

## Why ADhammer

ADhammer

PingCastle

impacket / Rubeus

Language

Rust — one static binary

C# (.NET)

Python / C#

Runs from

Kali/Linux 
and
 Windows

Windows only

Linux (impacket) / Windows

Passive AD audit

✅ 41 checks + control-path graph

✅ (the reference)

❌

Validation / offense

✅ roast·DCSync·tickets·relay·RCE

❌ (audit only)

✅ (offense only)

Protocol stack

from-scratch, no impacket dependency

.NET libs

mature, batteries-included

Runtime

none (pure-Rust crates)

.NET runtime

Python runtime

Live-validated on

Windows Server 2025
 (patched) 
+ Server 2022

broad

broad

The niche:audit and validation in one Linux-native binary, on a self-rolled stack whose
security-descriptor parser and RPC/NTLM/SMB layer are reusable Rust crates that didn't previously
exist (windows-sddl,ntlmssp,smb2-client,dcerpc).

## Install

cargo install adhammer 
#
 or: git clone … && cargo build --release

The default build ispure-Rust(rustls) — no OpenSSL, no system libraries — so itcross-compiles cleanly and static-links(e.g. a fully staticx86_64-unknown-linux-muslbinary you can drop on any Linux box):

rustup target add x86_64-unknown-linux-musl
cargo build --release --target x86_64-unknown-linux-musl

Legacy DCs (SHA-1 LDAPS certs):rustls refuses SHA-1 handshake signatures, so for those hosts
build with the native-TLS backend (OpenSSL/Schannel) instead:

sudo apt-get install -y build-essential pkg-config libssl-dev 
#
 Debian/Kali

cargo build --release --no-default-features --features tls-native

Prebuilt binaries:Releases. Requires Rust 1.80+.

## Usage

Runadhammerwith no arguments for theguided interactive menu: it asks for user → password
(or NT hash) → domain → DC, saves the session, then walks every action with prompts. For
golden/silver/pass-the-ticket itauto-fetchesthe krbtgt/service AES256 key (via DCSync) and the
domain SID (via LSAT) from your session — no pasting keys or SIDs. Add--no-saveto keep creds off
disk, or "Wipe saved session" from the menu.

Long-running steps show a live spinner with an elapsed timer; styling auto-disables when output is
piped (soscanJSON and logs stay clean —NO_COLOR/CLICOLOR_FORCEhonored).

Power-user subcommands:

scan passive audit → JSON/HTML (+ --sysvol, --bloodhound out.zip)
auto guided: scan → confirm each weakness → validate + PoC report
enum {samr, lsa, net, dns, adcs, esc, posture} RPC / net / ADIDNS / AD-CS / ESC-registry / DC-posture
attack {roast, spray, abuse, coerce, rbcd, constrained, dcsync, exec, atexec, wmiexec,
 secretsdump, gmsa, laps, esc1, golden, silver, pth, asktgt, winrm, capture, poison,
 relay, zerologon}

Guided mode(adhammer auto, or the interactive "Guided" menu): runs the audit, then walks
each finding — colored, severity-coded — asking"validate and capture a PoC?". On yes it runs the
matching attack, and marks the findingvalidated only when the real proof is present(an actual$krb5tgs$/$krb5asrep$hash, a replicatedkrbtgtsecret, anISSUEDcert) — otherwise honestly
"attempted." It also runs opportunisticactive checksbeyond the passive scan (LAPS local-admin
read, AD CS ESC8 web-enrollment probe), adding them only if a weakness is confirmed. Everything —
validated, attempted, declined, and potential — lands in aMarkdown assessment reportwith the
exact command + captured evidence per PoC.--yesruns it unattended.

Realautooutput from thetestlab.localDC assessment — 13 findings, 4 confirmed with a live PoC (full report:auto-report.md).

Validators: Kerberoast · AS-REP · DCSync · gMSA read · AD CS ESC1 · LAPS read · ESC8 probe.

#
 Audit a domain (low-priv creds are enough), export a BloodHound graph:

adhammer scan --url ldaps://dc.corp.local:636 --user 
'
CORP\svc
'
 --password … --insecure --bloodhound out.zip

#
 ADIDNS + AD CS recon:

adhammer enum dns --url ldaps://dc:636 --user 
'
CORP\svc
'
 --password … --insecure
adhammer enum adcs --url ldaps://dc:636 --user 
'
CORP\svc
'
 --password … --insecure 
#
 + ESC8 web-enroll probe

#
 DCSync the krbtgt key, forge a golden ticket, pass-the-ticket to SYSTEM:

adhammer attack dcsync --host dc --domain CORP --user Administrator --password … --target krbtgt
adhammer attack pth --host dc --realm CORP.LOCAL --krbtgt-aes256 
<
64-hex
>
 --domain-sid S-1-5-21-… --spn cifs/dc.corp.local --command whoami

## Audit coverage

* Privileged accounts— AS-REP/Kerberoast exposure, unconstrained delegation, DCSync control
paths (graph), sensitive-group membership, gMSA read ACL, SID history, RBCD, LAPS coverage,
PASSWD_NOTREQD.
* Trusts— SID filtering, selective auth, cross-forest TGT delegation, RC4, transitivity.
* Stale objects— inactive users/computers, old passwords, EOL OS, duplicate SPNs, stale
machine passwords.
* Anomalies— MachineAccountQuota, krbtgt age, RC4 Kerberos, reversible encryption,
badSuccessor (dMSA), password policy, anonymous LDAP (dSHeuristics), Pre-Windows 2000 Compatible
Access, Guest, GPP cpassword (MS14-025), and — from GptTmpl.inf — LM/NTLMv1, LDAP/SMB signing.
* AD CS (15/16 ESC)— passive:ESC1, ESC2, ESC3, ESC4, ESC5, ESC9, ESC13, ESC14, ESC15/EKUwu
(CVE-2024-49019); active:ESC8web-enrollment probe (enum adcs); registry over MS-RRP:ESC6, ESC7, ESC10, ESC11, ESC16(enum esc). Only ESC12 (hardware token) is out of scope.
* ADIDNS— zone/record enumeration with wildcard (mitm6/WPAD) detection (enum dns).

Every finding carries a MITRE ATT&CK technique (T1558.003 Kerberoasting, T1003.006 DCSync, T1649
cert abuse, T1484 policy/trust modification, …).

## Validated capabilities

Every audit finding is backed by a working technique, so a red team can confirm impact and a
defender can see exactly what the misconfiguration yields. All live-validated end-to-end against a
hardenedServer 2025DC — and, to prove the Linux-native positioning, built on Kali and run
against the DC.

* Recon / export—scan(41 checks + graph as a low-priv user),enum samr/enum lsa,enum net(host/AD-port/SMB-signing sweep),enum dns(ADIDNS),enum adcs(CAs + ESC8),enum esc(ESC6/7/10/11/16 over MS-RRP),enum posture(LDAP signing/channel-binding + Spooler — relay/coercion enablers),scan --bloodhound(SharpHound-compatible zip).
* Credential access—DCSyncsingle-object and full-domain (NT hashes + Kerberos keys incl.
RFC 8009 AES-SHA2),gMSAandLAPSread over LDAPS, offlinesecretsdump(hand-rolledregfhive parser → bootkey → SAM/LSA/DCC2),pass-the-hash,overpass-the-hash(RC4→TGT).
* Kerberos— AS-REP + Kerberoast (RC4/AES),RBCD(S4U2Self→S4U2Proxy),Shadow CredentialsPKINIT (incl. Server 2025paChecksum2that breaks Rubeus/PKINITtools),golden / silver
ticketswith a from-scratch PAC (accepted by a patched 2025 KDC, KB5020805),pass-the-ticketover SMB.
* Lateral / exec—SVCCTL(psexec-style, LocalSystem, C$ output),WinRM(WS-Man + NTLM
message encryption, no service-install event),TSCH(atexec), andWMI(wmiexec— DCOM
activation → OXID resolve →IWbemServices::ExecMethod Win32_Process.Create, from a hand-built
MS-DCOM/MS-WMIO stack, output over C$).
* ADCS—ESC1enrollment (spoofed-UPN SAN over MS-ICPR) → client-auth cert as the target,
andESC6/7/10/11/16decided from the CA/DC registry overMS-RRP(enum esc, the checks
LDAP can't see — incl. ESC7 non-admin ManageCA/ManageCertificates from the CASecuritySD).
* Coercion / relay— PetitPotam / PrinterBug, LLMNR/NBT-NS poisoning, SMB→LDAP NTLM relay
(writes a Shadow Credential).

SeeVECTORS.mdfor the full closed / partial / open matrix andROADMAP.mdfor what's next.

## Architecture

The protocol stack ships as standalone, published crates — this repo consumes them (the dogfooding
proof, and the reusable "impacket for Rust"):

Published crate

Role

windows-sddl

no-FFI 
SECURITY_DESCRIPTOR
/DACL/ACE parser (MS-DTYP) + 
Sid
/
Guid
 + AD extended-right GUIDs

ntlmssp

NTLMSSP (NTLMv2, MIC, key-exch) + RC4 sign+seal for RPC packet privacy

smb2-client

async SMB2 client (negotiate → NTLMv2 SPNEGO → IPC$/named pipe; signing; file I/O)

dcerpc

NDR · PDUs · sign+seal · TCP/SMB transports · EPM · SAMR · LSAT · DRSUAPI · SVCCTL · TSCH · EFSR · RPRN · ICPR · DCOM (OXID resolver)

Workspace crates (audit + orchestration):core(model + MITRE),graph(control-path,
reverse-Dijkstra to Tier-0),collector(LDAP over domain + Configuration NC),checks(the
41-rule engine),kerberos(roast · S4U/RBCD · Shadow-Cred PKINIT · golden/silver · pass-the-ticket),sysvol(GPP/GptTmpl),report(risk scoring → JSON/HTML),ldap(hand-rolled BER + NTLM SASL for
the relay bridge),bloodhound(SharpHound export),secrets(offline hive/SAM decryption).

## Test

cargo 
test
 --workspace 
#
 hermetic unit tests (no network)

Unit tests cover every parser, crypto primitive, and marshaler against spec vectors and round-trips
(NTOWFv2, RC4/RFC 6229, GPP AES key, NDR alignment, RPC PDUs, EPM towers, SMB2 signing, SAMR/LSAT,
PKINIT DH, PAC/DNS-record/LAPS parsing); ~50 more live in the extracted crates. Live-DC integration
tests incli/tests/integration.rsare#[ignore]d — run against a lab withADH_DC=… ADH_PASS=… cargo test --test integration -- --ignored --test-threads=1.

ldap3links platform TLS (native-tls) so LDAPS works against legacy DCs whose handshake still uses
SHA-1 — which rustls refuses.

## Status & caveats

* All parsing, crypto, and marshaling are unit-tested; the audit and validated flows above are
live-validated againstServer 2025 and Server 2022lab DCs. On 2022, 22 flows were run
end-to-end —scan/auto,enum(samr/lsa/net/dns/adcs/esc),roast(RC4+AES) /spray/dcsync --all,exec(SVCCTL→SYSTEM) /winrm/pth,golden(KDC-accepted) /silver/asktgt,secretsdump,abuse(add-spn/set-password/add-member/write-rbcd),coerce(PrinterBug), andESC1(low-priv → Administrator cert → PKINIT TGT). The 2016/2019/2012R2
matrix is on the roadmap.
* attack capture/relay/poisonneed a Linux attacker host (a Windows host holds TCP/445), which
is the Kali-native positioning;attack atexec(TSCH) is a redundant RCE method that still
faultsnca_s_fault_ndron modern targets — useexec(SVCCTL) orwinrm.
* Default LDAP binds use LDAPS (--insecurefor a lab self-signed cert; a bare username is
auto-qualified to a UPN). Plaintext simple bind is refused by hardened DCs; SASL GSSAPI is an
off-by-default cargo feature.
* Out of current scope:WMI exec(the DCOM/OXID foundation exists indcerpc; the activation
chain is not yet wired). ESC6/7/10/11/16 are now covered byenum esc.

Authorized research / academic / authorized-engagement use only — seeSECURITY.md.
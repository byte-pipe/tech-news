---
title: DynIP — Dynamic DNS for homelabs and infrastructure
url: https://dynip.dev/
site_name: hackernews_api
content_file: hackernews_api-dynip-dynamic-dns-for-homelabs-and-infrastructure
fetched_at: '2026-05-27T13:38:49.115566'
original_url: https://dynip.dev/
author: DynIP
date: '2026-05-26'
description: Dynamic DNS for homelabs and infrastructure. 60-second updates, RFC 2136 TSIG, DNSSEC, bring-your-own-domain, full IPv6 support. Free tier available.
tags:
- hackernews
- trending
---

{{ isDark ? 'Light Mode' : 'Dark Mode' }}
 

 {{ toast }}
 

# Dynamic DNS that actually works.

60-second updates. Generous free tier. RFC 2136 TSIG. Bring your own domain. DNSSEC. For homelabs, edge routers, and infrastructure teams.

 Sign up free
 

 See how it works
 

### Updates in seconds, not minutes

Most DDNS providers cache for 30 minutes. DynIP propagates in under a minute end-to-end. Your router sends an update, your hostname resolves correctly worldwide within ~60 seconds.

60s TTL · NOTIFY-driven · Multi-region nameservers

### Built on real DNS standards

RFC 2136 TSIG means your FortiGate, MikroTik, OPNsense, OpenWRT, or any router that speaks DNS UPDATE works out of the box with our code generator.

RFC 2136 TSIG · REST API · UDP/53 native

### IPv6 done right

Modern ISPs increasingly give you native IPv6 alongside CGNATed IPv4. DynIP supports both: update A and AAAA records side-by-side, run IPv6-only zones, or both. Built for the network you have today and the network you'll have tomorrow.

AAAA records · Dual-stack · IPv6-only support · DNSSEC by default

## dynip.dev

Set New Password

Password Recovery

Two-Factor Authentication

Access Control

 Your account has been deleted. Thank you for using dynip.dev.
 

 {{ auth.message }}
 

Enter New Password

At least 12 characters.

 {{ loading ? 'Processing...' : 'Reset Password' }}
 

Back to Sign In

Email Address

 {{ loading ? 'Processing...' : 'Send Reset Link' }}
 

Back to Sign In

{{ auth.twoFactorType === 'totp' ? '📱 Open Google Authenticator' : '✉️ Check your email' }}

{{ auth.twoFactorType === 'totp' ? 'Enter the 6-digit code from your app.' : 'We sent a 6-digit code to your inbox.' }}

Account temporarily locked

Too many incorrect attempts. Please try again in {{ lockoutDisplay }}.

 {{ loading ? 'Verifying...' : 'Complete Login' }}
 

Cancel

Email Address

Password

Forgot?

At least 12 characters.

 Too many incorrect attempts. Please try again in {{ lockoutDisplay }}.
 

 {{ loading ? 'Processing...' : (auth.isRegister ? 'Complete Sign Up' : 'Sign In') }}
 

 Missed the email? Click here to resend.
 

OR

 {{ auth.isRegister ? 'Return to Sign In' : 'Create New Account' }}
 

## Configuration Snippets

×

RFC 2136 / TSIG updates available in {{ tsigSecondsRemaining }} seconds

 We're propagating this zone to our nameservers. FortiGate and MikroTik (RFC 2136 / TSIG) need to wait — they're disabled below until propagation completes. HTTP API updates (cURL, PowerShell, Python, MikroTik HTTP, etc.) work right now.
 

Device Type

Docker Compose (Container)

Generic cURL (HTTP API)

Windows PowerShell (HTTP API)

Python Script (HTTP API)

Arduino / ESP32 (C++)

Minimal C Script (libcurl)

FortiGate CLI (Native DNS){{ tsigPropagating ? ' (propagating)' : '' }}

Palo Alto PAN-OS (GUI)

Cisco IOS Router (CLI)

Cisco ASA Firewall (CLI)

MikroTik RouterOS (HTTP API)

MikroTik RouterOS (RFC 2136 / TSIG){{ tsigPropagating ? ' (propagating)' : '' }}

pfSense / OPNsense (GUI)

Ubiquiti UniFi (GUI)

OpenWrt CLI (ddns-scripts)

Teltonika CLI (Native DNS)

DD-WRT / Netgear / Linksys (GUI)

Synology DSM NAS (GUI)

Fritz!Box (GUI)

Target IP Address

Domain

{{ snippetData.domain }}

TSIG Key

{{ snippetData.key }}

Copy

Configuration Snippet

{{ generatedSnippet }}

Copy

## {{ subscription.tier }} Plan

×

⚠ {{ subscription.locked_zones_count }} zone(s) locked

Your plan was downgraded. The oldest {{ subscription.max_domains }} zone(s) stay active; the rest are locked and can't receive IP updates. Subscribe again or delete excess zones to unlock.

Status

Free tier

Active

Cancelled

Past Due

{{ subscription.status || '—' }}

 {{ subscription.status === 'cancelled' ? 'Access ends' : 'Renews on' }}
 

 {{ formatPlanDate(subscription.current_period_end) }}
 

Billing cycle

{{ subscription.cycle }}

 Payment failed. Please update your payment method to keep access.
 

Zones

{{ subscription.zones_in_use }} of {{ subscription.max_domains }}

 Upgrade →
 

 {{ portalLoading ? 'Opening…' : 'Update payment' }}
 

## Enable DNSSEC for this zone?

×

Issuing a Let's Encrypt certificate for{{ dnssecPrompt.zone }}requires DNSSEC to be active on this zone.

We'll automatically:

* Generate signing keys
* Publish them in the parent zone ({{ dnssecPrompt.parentZone }})
* Sign all DNS records

This is a one-time setup. Your zone stays signed afterward, which is recommended anyway.

Estimated time: 30 seconds.

Enabling DNSSEC{{ dnssecPrompt.parentZone ? ' and publishing DS in ' + dnssecPrompt.parentZone : '' }}...

Cancel

 {{ dnssecPrompt.busy ? 'Enabling…' : 'Enable DNSSEC and continue' }}
 

### Quick Start Guide

{{ showHelp ? 'Hide' : 'Show' }}

1. Create a Zone:Type your device name, select your preferred base domain, and click Create Zone.

2. Get the Config:Click theSnippetsbutton next to your new domain.

3. Deploy:Select your device type and copy the generated configuration block directly into your router's CLI.

Note: IPv4 and IPv6 (Dual-Stack) are detected and updated automatically based on the incoming connection.

.

{{ dom }}{{ deprecatedBaseDomains.includes(dom) ? ' ⚠ (deprecated)' : '' }}

Create Zone

Domain & Tools

Current IP

TSIG Secret

DNSSEC

SSL Cert

{{ zone.name }}

⚠

 Locked
 

Snippets

Delete

Notify

{{ zone.ip }}

 Sync: {{ formatSyncTime(zone.last_sync) }}
 

{{ zone.showKey ? '🙈' : '👁️' }}

 Download
 

 {{ zone.sslLoading ? 'Renewing…' : 'Renew' }}
 

 {{ certDaysLabel(zone) }}
 

 {{ zone.sslLoading ? 'Generating...' : '🔐 Get SSL' }}
 

No domains registered. Create one above to get started.

### Custom Namespaces (BYOD)

{{ showByod ? 'Hide' : 'Show' }}

Bring your own domain to DynIP. Once added, you can provision dynamic subdomains under your own namespace.

 Register Namespace
 

#### {{ dom.domain }}

Remove

{{ dom.verifyStatus === 'success' ? 'Delegation Active:' : 'Required Registrar Action:' }}

{{ dom.verifyStatus === 'success' ? 'Your namespace is successfully secured and routing traffic to DynIP.' : 'To activate this namespace, create BOTH NS (Name Server) records at your domain registrar. Single-NS delegation will be rejected:' }}

{{ dom.domain }}. IN NS ns1.dynip.dev.
{{ dom.domain }}. IN NS ns2.dynip.dev.

 {{ dom.isVerifying ? 'Checking...' : (dom.verifyStatus === 'success' ? 'Re-Verify Setup' : 'Verify Setup') }}
 

✅ {{ dom.verifyMessage }}

❌ {{ dom.verifyMessage }}

### Quick Sync

{{ showSync ? 'Hide' : 'Show' }}

Instantly update your selected zones to match this device's current external IP address.

📡

Detected Network IP

{{ mobileIp || 'Detecting...' }}

🔄

{{ zone.name }}

{{ zone.ip }}

 No zones available. Create one above.
 

 {{ isUpdatingMobile ? 'Syncing...' : 'Update Selected Zones' }}
 

### API Automation

{{ showApi ? 'Hide' : 'Show' }}

#### Quick test (uses your session — expires when you log out)

Programmatically register new zones with your current session token. Send aPOSTrequest to the/registerendpoint.

curl -X POST "{{ backendUrl }}/register?subdomain=my-new-router&base_domain={{ baseDomains[0] }}" \
 -H "Authorization: Bearer {{ token }}"

Copy

Session tokens expire on logout — use an API token below for long-running automation.

#### API tokens(Pro+)

+ New Token

API tokens are a Pro feature

Long-lived tokens for automation: monitoring scripts, CI pipelines, MSP integrations. Tokens don't expire when you log out.

Upgrade to Pro →

Long-lived tokens for automation. Each token can be scoped read-only or full access, and revoked at any time.

Loading tokens…

 No API tokens yet. Create one to get started.
 

Name

Token

Scope

Last used

Expires

Action

{{ t.name }}

{{ t.token_prefix }}

{{ t.scope === 'read' ? 'Read-only' : 'Full' }}

{{ t.last_used_at ? formatPlanDate(t.last_used_at) : 'Never' }}

{{ t.expires_at ? formatPlanDate(t.expires_at) : 'Never' }}

Revoke

### New API Token

Tokens are shown once at creation — store them in a password manager or secrets vault.

Name

Scope

Read-only

Full access

Expires

Never

30 days

90 days

1 year

{{ apiTokenModal.error }}

Cancel

 {{ apiTokenModal.busy ? 'Creating…' : 'Create Token' }}
 

### ⚠ Save this token now

This token won't be shown again. Store it somewhere secure (1Password, Bitwarden, your CI's secrets manager).

{{ apiTokenModal.created.token }}

Copy

I've Saved It

### Account security

#### TOTP Enabled

This overrides email 2FA.

 Remove App
 

Upgrade your account security by requiring a time-based code from Google Authenticator or another TOTP app when you sign in.

 Setup Authenticator App
 

### 1. Scan the QR Code

Open Google Authenticator, Authy, or your preferred 2FA app and scan this code.

### 2. Verify & Save

 Verify
 

Cancel Setup

### Danger zone

{{ showDangerZone ? 'Hide' : 'Show' }}

#### Delete account

Permanently delete your account, all DNS zones you have created, and any TLS certificates issued to them. This cannot be undone or reversed by support.

 Delete account
 

### Permanently delete your account?

This action cannot be undone. Deletion will:

* Remove all your DNS zones immediately
* Cancel any active TLS certificates
* Cannot be reversed by support
* Your data will be deleted; billing records retained per Swedish law (7 years)

If you have an active paid subscription, please cancel it first via your account billing area.

Enter your password to confirm

{{ deleteAccount.error }}

Cancel

 {{ deleteAccount.busy ? 'Deleting…' : 'Permanently delete' }}
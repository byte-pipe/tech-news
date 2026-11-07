---
title: "Running a law firm on Free software (2026 edition) | decoded.legal's blog"
url: https://decoded.legal/blog/2026/11/running-a-law-firm-on-free-software-2026-edition/
date: 2026-11-07
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-11-08T09:03:32.579892
---

# Running a law firm on Free software (2026 edition) | decoded.legal's blog

# Running a law firm on Free software (2026 edition) – summary

## Client‑side setup
- **Operating system & desktop**: Debian with GNOME on a ThinkPad X1 Yoga Gen 6; hardware issues with Thunderbolt/USB‑C ports may require a laptop replacement.  
- **Email**: Thunderbird (with Quick Folder Move and Move Message And Yourself add‑ons) and mutt; occasional trouble with recurring calendar invitations in Thunderbird.  
- **Document creation**: LibreOffice Writer for Word‑compatible files; pandoc and typst for converting Markdown; interest in TeX for a client who wants diffs of .tex files.  
- **Presentations**: reveal.js driven by a Bash script that builds Markdown‑based slides with a CSS template.  
- **File manager**: Nautilus, enhanced with custom Bash scripts.  
- **PDF handling**: Evince for reading, Xournal++ for annotation, PDFarranger and pdftk for manipulation.  
- **Text expansion**: espanso, heavily used for repetitive typing.  
- **Web browsers**: Firefox (considering LibreWolf or other forks due to concerns about Mozilla’s direction). Used also for joining Teams/Zoom meetings.  
- **Knowledge base**: vimwiki, chosen because of extensive Vim usage; stores professional development notes.  
- **Encryption**: LUKS for disk encryption; Cryptomator for client‑side file encryption before syncing with Syncthing.  
- **Fediverse**: Mastodon (advanced web UI) or the TUI toot; automated toots scheduled via Bash script and cron.  
- **Password management**: Bitwarden with a vaultwarden server, protected by YubiKeys for sensitive credentials.  
- **Markdown editing**: Apostrophe for blog posts; presentations edited in Vim or gedit.  
- **Scanning & document management**: paperless‑ngx.  
- **Label printing**: FOSS web UI for Brother (and similar) label printers, used sparingly to stay paperless.  
- **Terminal‑centric workflow**: Frequent use of TUIs such as mutt, vim, ikhal, ncmpcpp, newsboat, toot, links, etc., for speed and minimal distraction.

## Server‑side infrastructure
- **Hosting platform**: Primarily Intel NUCs; fewer Raspberry Pi devices than before.  
- **Email services**: Postfix/Dovecot MTA; planning a migration to Stalwart in the future.  
- **File synchronization**: Syncthing (replaced Nextcloud due to complexity).  
- **Calendar & contacts**: Radicale for CalDAV/CardDAV.  
- **Video/voice communication**: Signal (replaced self‑hosted Jitsi after low usage).  
- **Invoicing**: InvoicePlane for generating PDF invoices (client‑side only).  
- **Time tracking**: Kimai v2, with positive developer interaction.  
- **Case/matter management**: EspoCRM.  
- **VPN**: WireGuard.  

*Overall, the setup remains largely the same as in previous updates, with the main changes being the switch from Nextcloud to Syncthing + Radicale and the replacement of Jitsi with Signal for conferencing.*
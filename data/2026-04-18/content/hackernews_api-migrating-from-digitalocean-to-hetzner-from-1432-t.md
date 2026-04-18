---
title: 'Migrating from DigitalOcean to Hetzner: From $1,432 to $233/month With Zero Downtime :: Isa Yeter'
url: https://isayeter.com/posts/digitalocean-to-hetzner-migration/
site_name: hackernews_api
content_file: hackernews_api-migrating-from-digitalocean-to-hetzner-from-1432-t
fetched_at: '2026-04-18T19:40:53.618288'
original_url: https://isayeter.com/posts/digitalocean-to-hetzner-migration/
author: yusufusta
date: '2026-04-18'
published_date: 2026-03-17 00:00:00 +0000 UTC
description: A real-world production migration from DigitalOcean to Hetzner dedicated, handling 248 GB of MySQL data across 30 databases, 34 Nginx sites, GitLab EE, Neo4j, and live mobile app traffic — with zero downtime.
tags:
- hackernews
- trending
---

# Migrating from DigitalOcean to Hetzner: From $1,432 to $233/month With Zero Downtime

2026-03-17

 
 #
devops
 
 
 #
mysql
 
 
 #
nginx
 
 
 #
migration
 
 
 #
hetzner
 
 
 #
digitalocean
 
 
 #
linux
 
 
 

A real-world production migration from DigitalOcean to Hetzner dedicated, handling 248 GB of MySQL data across 30 databases, 34 Nginx sites, GitLab EE, Neo4j, and live mobile app traffic — with zero downtime.

## Why We Migrated⌗

Running a software company in Turkey has become increasingly expensive over the last few years. Skyrocketing inflation and a dramatically weakening Turkish Lira against the US dollar have turned dollar-denominated infrastructure costs into a serious burden. A bill that felt manageable two years ago now hits very differently when the exchange rate has multiplied several times over.

Every month, we were paying$1,432 to DigitalOceanfor a droplet with 192GB RAM, 32 vCPUs, 600GB SSD, two block volumes (1TB each), and backups enabled. The server was fine — but the price-to-performance ratio had stopped making sense.

Then we discovered the Hetzner AX162-R.

DigitalOcean

Hetzner AX162-R

CPU

32 vCPU

AMD EPYC 9454P (48 cores / 96 threads)

RAM

192 GB

256 GB DDR5

Disk

600 GB SSD + 2x1 TB volumes

1.92 TB NVMe Gen4 RAID1

Monthly Cost

$1,432

$233

Savings

—

$1,199/month

That’s$14,388 saved per year— for a server that’s objectively more powerful in every dimension. The decision was easy.

I’ve been a DigitalOcean customer for nearly 8 years. They have a great product and I have no complaints about reliability or developer experience. But looking at those numbers now, I cannot help feeling a bit sad about all the extra money I left on the table over the years. If you are running steady-state workloads and not actively using DO’s ecosystem features, do yourself a favor and check dedicated server pricing before your next renewal.

## What We Were Running⌗

This wasn’t a toy project. The stack included:

* 30 MySQL databases(248 GB of data)
* 34 Nginx virtual hostsacross multiple domains
* GitLab EE(42 GB backup)
* Neo4J Graph DB(30 GB graph database)
* Supervisormanaging dozens of background workers
* Gearmanjob queue
* Several live mobile apps serving hundreds of thousands of users

Old server: CentOS 7 — long past its end-of-life, but still running in production.
New server: AlmaLinux 9.7 — a RHEL 9 compatible distribution and the natural successor to CentOS. This migration was also an opportunity to finally escape an OS that hadn’t received security updates in years.

## The Strategy: Zero Downtime⌗

The naive approach — change DNS, restart everything, hope for the best — wasn’t acceptable. Instead, we designed a proper migration path with six phases:

Phase 1 — Full stack installation on the new serverNginx (compiled from source with identical flags), PHP (via Remi repo, with the same.iniconfig files from the old server), MySQL 8.0, Neo4J Graph DB, GitLab EE, Node.js, Supervisor, and Gearman. Every service had to be configured to match the old server’s behavior before we touched a single DNS record.

SSL certificates were handled by rsyncing the entire/etc/letsencrypt/directory from the old server to the new one. After the migration was complete and all traffic was flowing through the new server, we force-renewed all certificates in one shot:

certbot renew --force-renewal

Phase 2 — Web files cloned with rsyncThe entire/var/www/htmldirectory (~65 GB, 1.5 million files) was cloned to the new server usingrsyncover SSH with the--checksumflag for integrity verification. We ran a final incremental sync right before cutover to catch any files changed after the initial clone.

Phase 3 — MySQL master to slave replicationRather than taking the database offline for a dump-and-restore, we set up live replication. The old server became master, the new server a read-only slave. We usedmydumperfor the initial bulk load, then started replication from the exact binlog position recorded in the dump metadata. This kept both databases in real-time sync until the moment of cutover.

Phase 4 — DNS TTL reductionWe scripted the DigitalOcean DNS API to lower all A and AAAA record TTLs from 3600 to 300 seconds — without touching MX or TXT records (changing mail record TTLs can cause deliverability issues). After waiting one hour for old TTLs to expire globally, we were ready to cut over in under 5 minutes.

Phase 5 — Old server nginx converted to reverse proxyWe wrote a Python script that parsed everyserver {}block across all 34 Nginx site configs, backed up the originals, and replaced them with proxy configurations pointing to the new server. This meant that during DNS propagation, any request still hitting the old IP was silently forwarded. No user would see a disruption.

Phase 6 — DNS cutover and decommissionA single Python script hit the DigitalOcean API and flipped all A records to the new server IP in seconds. The old server remained as a cold standby for one week, then was shut down.

The key insight: at no point did we have a window where the service was unavailable. Traffic was always being served — either directly or through the proxy.

## The MySQL Migration⌗

This was the most complex part of the entire operation.

### Dumping the Data⌗

We usedmydumperinstead of the standardmysqldump— and it made an enormous difference. By leveraging the new server’s 48 CPU cores for parallel export and import, what would have takendayswith a traditional single-threadedmysqldumpwas completed inhours. If you’re migrating a large MySQL database and you’re not usingmydumper/myloader, you’re doing it the hard way.

mydumper 
\

 --threads 
32
 
\

 --compress 
\

 --trx-consistency-only 
\

 --skip-definer 
\

 --chunk-filesize 
256
 
\

 -v 
3
 
\

 --outputdir /root/mydumper_backup/

The main dump’smetadatafile recorded the binlog position at the time of the snapshot:

File: mysql-bin.000004
Position: 21834307

This would be our replication starting point.

### Transferring the Dump to the New Server⌗

Once the dump was complete, we transferred it to the new server usingrsyncover SSH. With 248 GB of compressed chunks, this was significantly faster than any other transfer method:

rsync -avz --progress /root/mydumper_backup/ root@NEW_SERVER:/root/mydumper_backup/

The--compressflag inmydumperpaid off here — compressed chunks transferred much faster over the wire.

### Loading the Data⌗

myloader 
\

 --threads 
32
 
\

 --overwrite-tables 
\

 --ignore-errors 
1062
 
\

 --skip-definer 
\

 -v 
3
 
\

 --directory /root/mydumper_backup/

### The MySQL 5.7 to 8.0 Problem⌗

Being stuck on CentOS 7 meant we were also stuck on MySQL 5.7 — an outdated version that had been running in production for years. Before the migration, we ranmysqlcheck --check-upgradeto verify that our data was compatible with MySQL 8.0. It came back clean, so we installed the latest MySQL 8.0 Community on the new server. The performance improvement across all our projects was immediately noticeable — query execution times dropped significantly thanks to MySQL 8.0’s improved optimizer and InnoDB enhancements.

That said, the version jump did introduce one tricky problem.

After import, themysql.usertable had the wrong column structure — 45 columns instead of the expected 51. This causedmysql.infoschemato be missing, breaking user authentication.

Fix:

systemctl stop mysqld

mysqld --upgrade
=
FORCE --user
=
mysql 
&

But this failed the first time with:

ERROR: 'sys.innodb_buffer_stats_by_schema' is not VIEW

Thesysschema had been imported as regular tables instead of views. Solution:

DROP
 
DATABASE
 
sys
;

Then rerun the upgrade. Success.

## Setting Up MySQL Replication⌗

With both dumps imported, we configured the new server as a replica of the old one:

CHANGE
 
MASTER
 
TO

 
MASTER_HOST
=
'OLD_SERVER_IP'
,

 
MASTER_USER
=
'replicator'
,

 
MASTER_PASSWORD
=
'...'
,

 
MASTER_PORT
=
3306
,

 
MASTER_LOG_FILE
=
'mysql-bin.000004'
,

 
MASTER_LOG_POS
=
21834307
;

START
 
SLAVE
;

Almost immediately, replication stopped with error 1062 (Duplicate Key). This happened because our dump was taken in two passes — during the gap between them, rows were written to certain tables, and now both the imported dump and the binlog replay were trying to insert the same rows.

The fix:

SET
 
GLOBAL
 
slave_exec_mode
 
=
 
'IDEMPOTENT'
;

START
 
SLAVE
;

IDEMPOTENTmode silently skips duplicate key and missing row errors. All critical databases synced without a single error. Within a few minutes,Seconds_Behind_Masterdropped to 0.

## Testing Before Cutting Over⌗

Before touching a single DNS record, we needed to verify that all services were working correctly on the new server. The trick: we temporarily edited the/etc/hostsfile on our local machine to point our domain names to the new server’s IP.

# /etc/hosts (local machine)
NEW_SERVER_IP yourdomain1.com
NEW_SERVER_IP yourdomain2.com
# ... and so on for all your domains

With this in place, our browsers and Postman would hit the new server while the rest of the world was still going to the old one. We ran through our API endpoints, checked admin panels, and verified that every service was responding correctly. Only after this confirmation did we proceed with the cutover.

## A Sneaky SUPER Privilege Problem⌗

Once master-slave replication was fully synchronized, we noticed that INSERT statements were succeeding on the new server when they shouldn’t have been —read_only = 1was set, but writes were going through.

The reason: all PHP application users had been grantedSUPERprivilege. In MySQL,SUPERbypassesread_only.

SHOW
 
GRANTS
 
FOR
 
'some_db_user'
@
'localhost'
;

-- Result: GRANT SELECT, INSERT, UPDATE, DELETE, ..., SUPER, ... ON *.*

We revoked it from all 24 application users:

REVOKE
 
SUPER
 
ON
 
*
.
*
 
FROM
 
'some_db_user'
@
'localhost'
;

-- repeated for all 24 users

FLUSH
 
PRIVILEGES
;

After this,read_only = 1correctly blocked all writes from application users while allowing replication to continue.

## DNS Preparation⌗

All domains were managed through DigitalOcean DNS (with nameservers pointed from GoDaddy). We scripted the TTL reduction against the DigitalOcean API, only touching A and AAAA records — not MX or TXT records, since changing mail record TTLs can cause deliverability issues with Google Workspace.

# Only A and AAAA records

if
 
record
[
"type"
]
 
in
 
(
"A"
,
 
"AAAA"
):

 
update_record_ttl
(
domain
,
 
record
[
"id"
],
 
300
)

After waiting one hour for old TTLs to expire, we were ready.

## Converting Old Server Nginx to Reverse Proxy⌗

Rather than editing 34 config files by hand, we wrote a Python script that parsed everyserver {}block in every config file, identified the main content blocks, replaced them with proxy configs, and backed up originals as.backupfiles.

server
 
{

 
listen
 
443
 
ssl
;

 
server_name
 
yourdomain.com
;

 
ssl_certificate
 
/etc/letsencrypt/live/yourdomain.com/fullchain.pem
;

 
ssl_certificate_key
 
/etc/letsencrypt/live/yourdomain.com/privkey.pem
;

 
include
 
/etc/letsencrypt/options-ssl-nginx.conf
;

 
location
 
/
 
{

 
proxy_pass
 
https://NEW_SERVER_IP
;

 
proxy_set_header
 
Host
 
$host
;

 
proxy_set_header
 
X-Real-IP
 
$remote_addr
;

 
proxy_ssl_verify
 
off
;

 
proxy_read_timeout
 
150
;

 
}

}

The key:proxy_ssl_verify off— the new server’s SSL cert is valid for the domain, not for the IP address. Disabling verification here is fine because we control both ends.

## Cutover⌗

With replication atSeconds_Behind_Master: 0and the reverse proxy ready, we executed the cutover in order:

1. New server: STOP SLAVE;
2. New server: SET GLOBAL read_only = 0;
3. New server: RESET SLAVE ALL;
4. New server: supervisorctl start all
5. Old server: nginx -t && systemctl reload nginx (proxy goes live)
6. Old server: supervisorctl stop all
7. Mac: python3 do_cutover.py (DNS: all A records to new server IP)
8. Wait: ~5 minutes for propagation
9. Old server: comment out all crontab entries

The DNS cutover script hit the DigitalOcean API and changed every A record to the new server IP — in about 10 seconds.

## One Last Thing After Cutover⌗

After migration, we discovered many GitLab project webhooks were still pointing to the old server IP. We wrote a script to scan all projects via the GitLab API and update them in bulk.

## Final Numbers⌗

We went from$1,432/monthdown to$233/month— saving$14,388 per year. And we ended up with a more powerful machine:

CPU:32 vCPU to 96 logical CPUs (AMD EPYC 9454P, 48 cores x 2 threads)

RAM:192 GB to 256 GB DDR5

Storage:~2.6 TB mixed to 2 TB NVMe RAID1

Downtime:0 minutes

The entire migration took roughly 24 hours. No users were affected.

## Key Takeaways⌗

MySQL replication is your best friend for zero-downtime migrations.Set it up early, let it catch up, then cut over with confidence.

Check your MySQL user privileges before migration.SUPERprivilege bypassesread_only— if your app users have it, your slave environment isn’t actually read-only.

Script everything.DNS updates, nginx config rewrites, webhook updates — doing these by hand across 34+ sites would have taken hours and introduced errors.

mydumper + myloader dramatically outperforms mysqldumpfor large datasets. Parallel dump/restore with 32 threads cut what would have been days of work down to hours.

Cloud providers are expensive for steady-state workloads.If you’re not using autoscaling or ephemeral infrastructure, a dedicated server often delivers better performance at a fraction of the cost.

## All Scripts on GitHub⌗

All Python scripts used in this migration are open-sourced and available on GitHub:

GitHub Project

* do_list_domains_ttl.py— List all DigitalOcean domains with their A records, IPs, and TTLs
* do_ttl_update.py— Bulk-reduce all A/AAAA record TTLs to 300 seconds
* do_to_hetzner_bulk_dns_records_import.py— Migrate all DNS zones from DigitalOcean to Hetzner DNS
* do_cutover_to_new_ip.py— Flip all A records from old server IP to new server IP
* nginx_reverse_proxy_update.py— Convert all nginx site configs to reverse proxy configs
* mysql_compare.py— Compare row counts across all tables on two MySQL servers
* final_gitlab_webhook_update.py— Update all GitLab project webhooks to the new server IP
* mydumper— mydumper lib

All scripts support aDRY_RUN = Truemode so you can safely preview changes before applying them.
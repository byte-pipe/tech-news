---
title: 'Security advisory: openssh-server password authentication bypass | Alpine Linux'
url: https://alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/
site_name: hackernews_api
content_file: hackernews_api-security-advisory-openssh-server-password-authenti
fetched_at: '2026-11-06T12:28:27.929153'
original_url: https://alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/
author: pantalaimon
date: '2026-11-06'
description: Alpine Linux
tags:
- hackernews
- trending
---

2026-11-05

# Security advisory: openssh-server password authentication bypass

If you runsshdon Alpine Linux, updateopensshnow and restartsshd.Upgrading the package alone does not replace the running daemon.

If you cannot update yet, at least disable password logins: setPasswordAuthentication noin your sshd configuration and restartsshd.
Either one closes the hole.

## What is the problem?

An attacker who can reach your SSH port can log in without knowing any
password. It takes one connection, works every time, and needs no retries.

The attacker needs the name of an account whose password field is*(an account with no password set, which is normal for key-only accounts), and
needs the machine to have at least one other account with a$5$or$6$password hash. The attacker then sends a very long password (257 to 1024
bytes). One user with a password is enough: it makes every account without
one reachable.

Details are in theOpenSSH 10.6p2 release
notes. No CVE identifier had been
assigned at the time of writing.

## Who is affected?

You are affected if all of the following are true:

* You run the Alpineopenssh-serverpackage, which is built without PAM, or
you runopenssh-server-pamwithUsePAM no. (openssh-server-pamwithUsePAM yesis not affected.)
* PasswordAuthenticationisyes(the OpenSSH default, unless you changed it).
* The machine has an account whose password field is*. This includes:root, which ships asroot:*in the base image since about Alpine 3.16.
OpenSSH’s defaultPermitRootLogin prohibit-passwordprotects root, so
root is only reachable ifPermitRootLogin yesis set. That does not help if
another account that can log in is able to become root, for example
throughdoas.Any key-only user created withadduserwithout a password, or withusermod -p '*'.Users coming from a directory service through musl-nscd (nslcd, winbind,
sssd), since they have no shadow entry.Thealpineuser in the officialtiny-cloudimages (see below).
* root, which ships asroot:*in the base image since about Alpine 3.16.
OpenSSH’s defaultPermitRootLogin prohibit-passwordprotects root, so
root is only reachable ifPermitRootLogin yesis set. That does not help if
another account that can log in is able to become root, for example
throughdoas.
* Any key-only user created withadduserwithout a password, or withusermod -p '*'.
* Users coming from a directory service through musl-nscd (nslcd, winbind,
sssd), since they have no shadow entry.
* Thealpineuser in the officialtiny-cloudimages (see below).
* At least one local account has a$5$or$6$password hash.

Affected releases: every Alpine release we checked, 3.21 through 3.24 and
edge, and the older releases that no longer receive regular updates (3.16 to
3.20).

### Who is not affected?

* Docker and other container usersthat do not runsshdin the
container.
* Systems withPasswordAuthentication no.
* Systems usingopenssh-server-pamwithUsePAM yes(withUsePAM noyou are affected).
* Locked accounts: those with!as the password field in/etc/shadow(a line startinguser:!:). They cannot log in with a password or a key.
* Systems where no account has a$-style password hash.
* Cloud images configured through cloud-init, which writesPasswordAuthentication no.

## How can I fix it?

### 1. Update

apk upgrade -U -a

Alpine 3.21.10, 3.22.8, 3.23.8 and 3.24.4 contain the fixed package (see therelease announcement).
The fixed package versions are:

Branch

Fixed 
openssh
 version

edge

10.6_p2-r0

3.24

10.3_p1-r2

3.23

10.2_p1-r1

3.22

10.0_p1-r11

3.21

9.9_p2-r1

3.20

9.7_p1-r6

3.19

9.6_p1-r3

3.18

9.3_p2-r4

3.17

9.1_p1-r7

3.16

9.0_p1-r6

Restartsshdafter upgrading(rc-service sshd restart). Upgrading the
package does not restart a runningsshd, so you must do it after.

### 2. If you cannot update: disable password authentication

Before you start, make sure your SSH key login works, and keep your current
session open until you have tested a new login.

Run these as root. The first two commands create a drop-in file. Alpine’s
defaultsshd_configreads that directory from 3.19 onward; older releases
ignore it. Thesedcommand changesyestonoon everyPasswordAuthenticationline in/etc/ssh/sshd_config, whatever the spacing,
including lines inside aMatchblock. It also addsPasswordAuthentication noat the top of the file, for the case where there was no such line, and
saves the original as/etc/ssh/sshd_config.bak. The last two commands check
the configuration, restart the daemon, and show the result:

mkdir -p /etc/ssh/sshd_config.d
echo 'PasswordAuthentication no' > /etc/ssh/sshd_config.d/00-no-passwords.conf
sed -i.bak -e '1i PasswordAuthentication no' \
 -e 's/^\(\s*PasswordAuthentication[^y#]*\)yes/\1no/i' \
 /etc/ssh/sshd_config
sshd -t && rc-service sshd restart
sshd -T | grep -i passwordauthentication

The last command should printpasswordauthentication no. To undo, delete/etc/ssh/sshd_config.d/00-no-passwords.confand copy/etc/ssh/sshd_config.bakback over/etc/ssh/sshd_config.

## Cloud images (tiny-cloud)

The official tiny-cloud images (the qcow2, VHD and AMI artifacts) from3.18.11 through 3.24.3ship analpineuser with a*password field and
passwordlessdoas. They are safe on first boot. They become exploitable as
soon as any$6$hash exists on the machine, for example when an admin sets a
console password, or user-data adds a user withhashed_passwd. An attacker
then gets a shell asalpineand can usedoasto become root.

Images built from 3.21.10, 3.22.8, 3.23.8, 3.24.4 and later include the fixed
package. Images from earlier point releases do not, so on every running
instance, updateopensshor disable password authentication.

## Releases that are no longer supported (3.21 and older)

These releases have the same bug. 3.21 reached its end of support on
2026-11-01, but we have published fixed packages for each release all the way
back to 3.16.

## How do I know if I was attacked?

Look in/var/log/messagesforsshdlines readingAccepted password foran account that has no password (alpine,root, or any key-only user).
Reviewdoasuse and recently created users, files and authorized keys on
exposed machines. If you cannot rule out a login, treat the machine as
compromised.

## How could this happen?

When sshd is built without PAM, it checks a password by hashing the attempt
withcrypt()(the C library function that turns a password into its stored
hash) and comparing the result to the stored password field. For an account
whose stored field is too short to contain a salt (the random prefix of a
hash), sshd borrows the salt of another account.

musl’scrypt()returns the string*as an error indicator when the key is
over 256 bytes long.*is also exactly what the stored field contains for
every account with no password, so the “hash” matches and the login succeeds.

OpenSSH 10.6p2 avoids the problem in sshd. The stable-branch packages above
carry a patch for the same problem.

## Credits

Reported by Özgün Kültekin ofWakefield. Thanks to
Damien Miller and Darren Tucker of the OpenSSH project for the fix and the
10.6p2 release, to Timo Teräs for help analyzing the issue, and to Natanael
Copa, who built and uploaded the updated packages.
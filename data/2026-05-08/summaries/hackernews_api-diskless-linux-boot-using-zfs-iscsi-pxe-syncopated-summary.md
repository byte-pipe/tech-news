---
title: Diskless Linux boot using ZFS, iSCSI & PXE - Syncopated Pandemonium
url: https://aniket.foo/posts/20260505-netboot/
date: 2026-05-07
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-08T08:14:39.053203
---

# Diskless Linux boot using ZFS, iSCSI & PXE - Syncopated Pandemonium

# Diskless Linux boot using ZFS, iSCSI & PXE – Summary

## Motivation
- Avoid compiling `llama.cpp` on Windows and keep Windows clean for gaming.
- Prevent Windows updates from breaking GRUB; keep bootloader on remote drive.
- Preserve existing NVMe partitions without repartitioning for dual‑boot.
- Eliminate reliance on easily lost USB boot drives; use existing NAS for remote boot.
- Learn how PXE works over iSCSI.

## Limitations
- Network‑based Debian install is slower than local install.
- OS performance is not critical; sufficient RAM will mask latency after boot.
- Intended use is not general desktop browsing.

## Assumptions
- Single Debian 13 server provides Netboot.xyz, TFTP, iSCSI target, and ZFS ZVol.
- Proxmox host runs the services; Asus router with Merlin firmware supplies DNSMasq.
- Sections covered: Netboot.xyz setup, TFTP, DNSMasq, ZFS ZVol, iSCSI, Debian install.

## Install & Configure Netboot.xyz
- Install required packages: `apache2 git ansible tftpd-hpa targetcli-fb`.
- Clone and compile Netboot.xyz in `/opt/netboot.xyz`.
- Edit `user_overrides.yml` to enable menu, disk, checksum generation and set host IP.
- Modify `boot.cfg.j2` and `local-vars.ipxe.j2` to point to custom variables.
- Deploy Netboot.xyz to `/var/www/html` via Ansible.
- Create custom iPXE script `debian13-iscsi.ipxe` with iSCSI server, target, initiator IQNs, and credentials; include fallback to Debian installer.
- Add a menu entry `custom.ipxe` linking to the iSCSI boot option.
- Download Debian netboot kernel and initrd (both console and GTK versions) into `/var/www/html/assets/debian13*`.

## Configure TFTP
- Set TFTP directory to `/srv/tftp` and enable secure mode in `/etc/default/tftpd-hpa`.
- Copy compiled Netboot.xyz binaries (`*.kpxe`, `*.efi`) to `/srv/tftp/ipxe`.
- Adjust ownership to `tftp:tftp` and restart the TFTP service.

## Configure DNSMasq on Router
- Add DNSMasq rules to redirect BIOS, UEFI, and iPXE clients to appropriate Netboot.xyz files.
- Example rules:
  - BIOS: `dhcp-boot=tag:!ipxe,ipxe/netboot.xyz-undionly.kpxe,,192.168.50.167`
  - UEFI x86‑64: match client‑arch 7 and serve `netboot.xyz-snp.efi`.
  - iPXE: match option 175 and serve the Netboot.xyz menu URL.
- Restart DNSMasq.

## ZFS ZVol Creation
- Create ZFS pool on desired disk(s): `zpool create tank /dev/disk/by-id/<DISK_ID>`.
- Allocate a ZVol for the Debian disk: `zfs create -V 32G tank/debian-disk-12700k`.

## iSCSI Configuration (overview)
- Use `targetcli-fb` to:
  - Create an iSCSI backstore referencing the ZVol.
  - Define an iSCSI target for the Debian boot disk.
  - Enable write‑protect for unauthenticated clients.
  - Disable automatic node ACL generation.
  - Add initiator (client) entries with mutual authentication credentials.
  - Map the LUN to the target.

*(The article continues with detailed iSCSI commands and Debian installation steps.)*
---
title: 'Jan-Piet Mens :: SSH certificates: the better SSH experience'
url: https://jpmens.net/2026/04/03/ssh-certificates-the-better-ssh-experience/
site_name: hnrss
content_file: hnrss-jan-piet-mens-ssh-certificates-the-better-ssh-expe
fetched_at: '2026-04-03T19:19:04.121178'
original_url: https://jpmens.net/2026/04/03/ssh-certificates-the-better-ssh-experience/
author: Jan-Piet Mens
date: '2026-04-03'
description: 'SSH certificates: the better SSH experience'
tags:
- hackernews
- hnrss
---

# SSH certificates: the better SSH experience

When Isshinto a server for the first time, I’m confronted with a dialog which asks me to verify I’m actually talking to the machine I expect to be talking to.

$
 
ssh 
-l
 jane 192.0.2.65

The authenticity of host '192.0.2.65 (192.0.2.65)' can't be established.
ED25519 key fingerprint is SHA256:4WTRnq2OR1m03TpnHCfkFdlh1gN/PBXE4vDi0WnjFEc.
No matching host key fingerprint found in DNS.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])?

It is likely that the majority of users cross their fingers and type ‘yes’, which is not really a clever response. ThisTrust on First Use(TOFU) is what permits SSH to ensure that my SSH client verifies which server it’s talking to. I ought to have asked the administrator of the server to tell me its fingerprint, and if I am the administrator I ought to know how to do this: (in the following examples, a shell prompt%indicates I’m working as `root)

% ssh-keygen -l -f /etc/ssh/ssh_host_ed25519_key
256 SHA256:4WTRnq2OR1m03TpnHCfkFdlh1gN/PBXE4vDi0WnjFEc root@d13 (ED25519)

If the two fingerprints compare equal, I can trust that I am connecting to the correct server and can continue with ‘yes’ or I paste a known host fingerprint into the prompt: trust on first use is accomplished. (Utilities such asssh-keyscangather public keys from remote hosts, but I still ought toverify out-of-bandwhether I’m talking to the correct machine. SSH fingerprints can also be in the DNS, what can’t?, butthat’s a different story.)

The session then possibly continues with me being asked for the target user’s password which, if entered correctly, grants me access to the machine.

### SSH key pairs

If I create an SSH key pair, install my public key in the correct location (typically$HOME/.ssh/authorized_keyson the target node), and present the private key upon connection, then I don’t need to type the target user’s password; instead I enter the key’spassphrase, a hopefully much more complicated combination of words, to unlock the private key. I say “hopefully”, because this passphrase is what encrypts the private key so that it cannot be used without it. (Note that I typically generate keys with a comment in them so as to more easily keep track of them (-C), and specify which file (-f) they should be written to. The comment can be read from the public key file and will later be visible in the SSH agent.)

$
 
ssh-keygen 
-t
 ecdsa 
-C
 
"JP's demo key"
 
-f
 demokey

Generating public/private ecdsa key pair.
Enter passphrase for "demokey" (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in demokey
Your public key has been saved in demokey.pub

$
 
ssh-copy-id 
-i
 demokey.pub jane@192.0.2.65

/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "demokey.pub"
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
jane@192.0.2.65's password:

Number of key(s) added: 1

Now try logging into the machine, with: "ssh -i ./demokey 'jane@192.0.2.65'"
and check to make sure that only the key(s) you wanted were added.

$
 
ssh 
-i
 demokey jane@192.0.2.65

Enter passphrase for key 'demokey':

jane@node:~$

The private SSH key still needs unlocking on use because I set a passphrase on it when creating it.

I can avoid having to do that at every use of the key, by launching an SSH agent which I feed with my private key and it will then no longer requests a passphrase on use. Desktop systems typically launch an agent at startup, but I do so explicitly here to demonstrate:

$ eval $(ssh-agent)
Agent pid 40052

$ ssh-add demokey
Enter passphrase for demokey:
Identity added: demokey (JP's demo key)

$ ssh-add -l
256 SHA256:E8SC1waFc1rOV8ZxpQQf10xkaY5DkPLbjKBO0xdJlBA JP's demo key (ECDSA)

$ ssh -l jane 192.0.2.65 grep PRETTY /etc/os-release
PRETTY_NAME="Debian GNU/Linux 13 (trixie)"

In order for this to work, the server needs a copy of the public key I use in one of the locations specified by SSHd’sAuthorizedKeysFileconfiguration which defaults to.ssh/authorized_keysand.ssh/authorized_keys2. Public keys can also besourced from a commandon a node.

This is well known and has worked for very many years, but the required procedures for public key authentication to work come with some disadvantages:

* a copy of my SSH public key has to be available for each user I want to login as on a node
* TOFU typically causes the host fingerprint to be stored on my client (in theknown_hostsfile)
* when a host key rolls, I get a big warning

What’s with this warning? Well, if the server’s SSH host key changes, for instance because the server has been re-installed without restoring its original host keys, or because an administrator has forcefully re-generated them, my client will loudly complain that the server’s host keys have changed. Let’s see this in action.

The server’s admin re-generates SSH host keys on the server and restartssshd

% rm -f /etc/ssh/ssh_host_*
% ssh-keygen -A
ssh-keygen: generating new host keys: RSA ECDSA ED25519
% systemctl restart sshd

Now I try and access the same server again, as above (my user key is still in the agent). The connection fails, I then remove the offending host key from theknown_hostsfile usingssh-keygen, obtain the server’s host key fingerprint to re-validate TOFU, and finally accept the host key into myknown_hostsagain.

$
 
ssh 
-l
 jane 192.0.2.65 
df
 
-h
 /

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@ WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED! @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the ED25519 key sent by the remote host is
SHA256:3zm2UIyqO0xsxejndKdg9+Rpm4JeGuxamlsZwNOGX2Y.
Please contact your system administrator.
Add correct host key in /Users/jpm/.ssh/known_hosts to get rid of this message.
Offending ED25519 key in /Users/jpm/.ssh/known_hosts:649
Host key for 192.0.2.65 has changed and you have requested strict checking.
Host key verification failed.

$
 
ssh-keygen 
-R
 192.0.2.65

#
 
Host 192.0.2.65 found: line 649

/Users/jpm/.ssh/known_hosts updated.
Original contents retained as /Users/jpm/.ssh/known_hosts.old

$
 
ssh 
-l
 jane 192.0.2.65 
df
 
-h
 /

The authenticity of host '192.0.2.65 (192.0.2.65)' can't be established.
ED25519 key fingerprint is SHA256:3zm2UIyqO0xsxejndKdg9+Rpm4JeGuxamlsZwNOGX2Y.
No matching host key fingerprint found in DNS.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.0.2.65' (ED25519) to the list of known hosts.
Filesystem Size Used Avail Use% Mounted on
/dev/sda1 19G 1.2G 17G 7% /

Admittedly this probably won’t occur very frequently, but in larger environments, this is something our users need to be made aware of, including how to correctly remedy the situation.

For those of us with a small handful of nodes or requiring connections to systems we have no root privileges on, working with keys as described so far is likely sufficient respectively the only choice, however for those with dozens or even hundreds of servers and full control there-over, we can make all of the disadvantages above go away with an SSH CA (certification authority) and SSH certificates. That sounds complicated, but it isn’t.

### SSH Certification Authority

Those familiar with X.509 certificates, their complexity, and certification authorities might well have begun to groan now, but rest assured an SSH CA is something quite simple: all we need is an SSH key pair, and a few additional options for thessh-keygenutility we’re already familiar with!

SSH certificates have existed inOpenSSH since version 5.4 released in March 2010, and the certificate format is based on data formats which implementations already support – one reason OpenSSH designed it this way rather than using the far more complicated X.509 format. The following looks like an SSH public key file is actually an OpenSSH public certificate.

$
 
cat 
jane-cert.pub

ecdsa-sha2-nistp256-cert-v01@openssh.com AAAAKGVj ... 74jJshojVhIi+qOrg== Jane's key

For the following experiments I will use a single SSH CA key pair for users and hosts. (Two key pairs, one of hosts another for users, are sometimes used for better separation, but the principles described in the following are applied in the same way.)

Let me begin by enumerating some of the advantages of using SSH certificates:

* no more deploying of public SSH keys into serverauthorized_keysfiles; users can forget aboutssh-copy-id, editing$HOME/.ssh/authorized_keysmanually, etc.
* no danger of a user adding a key to anauthorized_keysfile for a key which shouldn’t have access at all
* a server’s host keys can be rolled (replaced) without the scary “WARNING” on clients as we saw earlier; in fact there will no longer be host keys added to users’known_hostsfiles!
* no more TOFU (Trust on First Use) confirmation is required, as users will implicitly trust servers and vice-versa
* principal names on user certificates dictate as which user(s) a user’s key can login as
* remote commands can be enforced (user restrictions are bound to certificates and do not need to be added to a target user’s$HOME/.ssh/authorized_keys)
* source IP prefixes can be limited, e.g. connecting as userrootis permitted from192.0.2.53/32only.
* certificates are valid for a specified time frame only, e.g. 30 minutes, 24 days, 34 weeks, etc. and they expire automatically (watch for clock drift)
* a single line of configuration in the global known hosts files (e.g./etc/ssh/ssh_known_hosts) suffices for all users on the client (but this line can also be in my personal$HOME/.ssh/known_hostsif I prefer)
* in order to connect to a node,ssh -ineeds the secret key file (jane) alongside its certificate (jane-cert.pub); if the certificate file isn’t available password authentication will be offered

So in our example the SSH CA will be used to sign host keys and user keys. To clarify, the CA is an SSH key pair which will be trusted by our nodes.

I proceed as follows.

* On the CA machine, i.e. the system on which I will be “operating” the certification authority, I create a dedicated directory for the CA key pair. All we need on this system are the OpenSSH utilities, and we will be signing public keys on this system. I generate a CA key pair of algorithm ECDSA which generates short but strong keys; use any algorithm you prefer.$umask077;mkdirCA$ssh-keygen-tecdsa-C"JP's SSH CA"-fCA/ssh-caGenerating public/private ecdsa key pair.
 Enter passphrase for "CA/ssh-ca" (empty for no passphrase):
 Enter same passphrase again:
 Your identification has been saved in CA/ssh-ca
 Your public key has been saved in CA/ssh-ca.pub
 The key fingerprint is:
 SHA256:A5ZBb5b/GbAv03EAb8fmDzv4p+q0g8Ulxrt8QZpbamM JP's SSH CA$chmod-wCA/ssh-ca*
* I optionally create a key pair for myself (or use an existing key pair I already have). As above, I like specifying a comment for the key and the file name into which it should be saved. Typically a user will have created a keypair for themselves and they make their public key available to the CA.$ssh-keygen-tecdsa-C"Jane's key"-fjaneGenerating public/private ecdsa key pair.
 Enter passphrase for "jane" (empty for no passphrase):
 Enter same passphrase again:
 Your identification has been saved in jane
 Your public key has been saved in jane.pub
 The key fingerprint is:
 SHA256:2WH263LauVfk5XvxHvrdvNt0y9OgaHBLSvcQ+R6u/KE Jane's key
* Now I sign that user’s public key with our SSH CA key. I give the certificate an identity (-I), specify principals it may be used for (-n) (i.e. users on target hosts), a serial number (-z) for my own use and a validity (-V), in this example ending one week from now.$ssh-keygen-sCA/ssh-ca-I"Jane Jolie"-njane-z001-V+1w jane.pubEnter passphrase for "CA/ssh-ca":
 Signed user key jane-cert.pub: id "Jane Jolie" serial 1 for jane valid from 2026-03-27T13:57:00 to 2026-04-03T14:58:39$ssh-keygen-L-fjane-cert.pubjane-cert.pub:
 Type: ecdsa-sha2-nistp256-cert-v01@openssh.com user certificate
 Public key: ECDSA-CERT SHA256:2WH263LauVfk5XvxHvrdvNt0y9OgaHBLSvcQ+R6u/KE
 Signing CA: ECDSA SHA256:A5ZBb5b/GbAv03EAb8fmDzv4p+q0g8Ulxrt8QZpbamM (using ecdsa-sha2-nistp256)
 Key ID: "Jane Jolie"
 Serial: 1
 Valid: from 2026-03-27T13:57:00 to 2026-04-03T14:58:39
 Principals:
 jane
 Critical Options: (none)
 Extensions:
 permit-X11-forwarding
 permit-agent-forwarding
 permit-port-forwarding
 permit-pty
 permit-user-rc
* I then copy our CA’s public SSH key to the target server and configure it into the SSH server’s configuration. This ensures the SSH service on this node will trust SSH keys signed by this CA. I don’t restartsshdyet.$[copy CA's public key to server]% install -m444 /tmp/ssh-ca.pub /etc/ssh/ssh-ca.pub% echo "TrustedUserCAKeys /etc/ssh/ssh-ca.pub" >>sshd_config
* I then obtain the node’s host key(s) and sign them with our CA, again specifying a validity, an identifier of choice, a serial number, and a principal (the node’s hostname(s)) for the key. Note the-hoption with which we sign a host certificate.% [ copy server's /etc/ssh/ssh_host_ed25519_key.pub to CA ]$ssh-keygen-h-sCA/ssh-ca-V+52w-Ideadbeef01-z1000-nalice.example.com ssh_host_ed25519_key.pubEnter passphrase for "CA/ssh-ca":
 Signed host key ssh_host_ed25519_key-cert.pub: id "deadbeef01" serial 1000 for alice.example.com valid from 2026-03-27T14:04:00 to 2027-03-26T14:05:47$ssh-keygen-L-fssh_host_ed25519_key-cert.pubssh_host_ed25519_key-cert.pub:
 Type: ssh-ed25519-cert-v01@openssh.com host certificate
 Public key: ED25519-CERT SHA256:ddxT1zL+HhHpIT5qWPdMJ6GC1SbVp2ij/2Sca5xA3RE
 Signing CA: ECDSA SHA256:A5ZBb5b/GbAv03EAb8fmDzv4p+q0g8Ulxrt8QZpbamM (using ecdsa-sha2-nistp256)
 Key ID: "deadbeef01"
 Serial: 1000
 Valid: from 2026-03-27T14:04:00 to 2027-03-26T14:05:47
 Principals:
 alice.example.com
 Critical Options: (none)
 Extensions: (none)
* I install the signed certificate(s) alongside the SSH server’s host key(s)$[copy host's key certificate to the server ]% install -m444 tmpfile /etc/ssh/ssh_host_ed25519_key-cert.pub
* and configure the SSH server to use the new certificate and restartsshd% echo "HostCertificate /etc/ssh/ssh_host_ed25519_key-cert.pub" >>sshd_config% sshd -t
 % systemctl restart sshd
* and finally add a reference to the host’s certificate authority in the client’sknown_hostsfile, either the global one in/etc/ssh/known_hostsor my own in~/.ssh/known_hosts. Here I overwrite the file as I no longer need the fingerprints it contained, but I can also keep the file’s content and append or prepend this line. The@cert-authorityline has a glob-style pattern used to match trusted nodes which present host keys signed with this (our CA’s) public key. This is how we add trust to our client for nodes’ SSH host keys signed by our CA.$echo"@cert-authority *.example.com$(catCA/ssh-ca.pub)">known_hosts

We created an SSH CA by generating an SSH key pair, and we have signed one or more public user keys and public host keys. Then on a node, we wired up the public key of our SSH CA and made the server trust it.

On our client machines, we added a single line of configuration to ourknown_hostsfile (user-specific or the global one), and this line will cause our clients to trust host keys signed by our CA.

We can now test.

### An initial connection

* In order to test, I create a user on the target system% useradd -c "Jane Jolie" -m jane
* we can now connect to the server. For debugging purposes I specify options (-o) to ensuresshuses exactly the files I specify here. In particular I want to make sure we’re informed when server host keys cannot be validated with theaskoption. If all goes well I will not be asked to trust a server’s fingerprint, and after the SSH session terminates, there will be no additional line in theUserKnownHostsFile. (This last file contains one line only, the@cert-authorityline.)$ssh-oUserKnownHostsFile=./known_hosts-oStrictHostKeyChecking=ask\-oIdentitiesOnly=true-ijane-ljane alice.example.comunameLinux
* the server logs inauth.log(here OpenBSD) but likewise in a systemd journal. Note we can read out the fingerprint of the used key, its identity (Jane Jolie), its serial number (001used during signing is simply an integer which is why it’s shown here as1), and the public key fingerprint of the signing CA.sshd-session[3099]: Accepted publickey for jane from 192.0.2.42 port 17087 ssh2: ECDSA-CERT SHA256:2WH263LauVfk5XvxHvrdvNt0y9OgaHBLSvcQ+R6u/KE ID Jane Jolie (serial 1) CA ECDSA SHA256:A5ZBb5b/GbAv03EAb8fmDzv4p+q0g8Ulxrt8QZpbamM
* If I want to connect by IP address as well as host name, I have to sign a node’s host key(s) with more than one principal name in them, and the entry inknown_hostsneeds these added comma-separated to it$ssh-keygen-h-sCA/ssh-ca-V+52w-Ideadbeef01-z1002-nalice.example.com,192.0.2.141 ssh_host_ed25519_key.pub$catknown_hosts@cert-authority *.example.com,192.0.2.* ecdsa-sha2-nistp256 AAAAE2....
* if I try to use Jane’s key and certificate to login as, say,ansibleon the target node, that fails because Jane’s user key certificate contains a principal “jane” only. (Add more comma-separated principal names when signing the user key in the-noption)$ssh-ijane-lansible alice.example.comsshd-session[3648]: error: Certificate invalid: name is not a listed principal
* a user’s certificate can be forced to invoke a particular utility on the server instead of what the user wanted. Here we add a forceddate, and in spite of the user wanting to invokeuname,dateis executed on the remote node.$ssh-keygen-sCA/ssh-ca-I"Jane Jolie"-njane-z2-V+1w-Oforce-command=/usr/bin/date jane.pub$ssh-ijane-ljane alice.example.comunameFri Mar 27 13:43:58 UTC 2026
* permissible source CIDR masks can be embedded into a user certificate, and the server logs violations$ssh-keygen-sCA/ssh-ca-I"Jane Jolie"-njane-z3-V+1w-Oforce-command=/usr/bin/date-Osource-address=192.0.2.0/24 jane.pubsshd-session[3854]: cert: Authentication tried for jane with valid certificate but not from a permitted source address (192.168.1.100).

### Checklist

I’ve tried to assemble a bit of a checklist of things we verify particularly if something doesn’t work as expected.

* on the node:CA’s public key must be on server, readable bysshd, and configured inTrustedUserCAKeysserver’s host key needs signing and must be placed alongside host key file(s)sshd_configrequiresHostCertificatepointing to the certificate of the host keyserver needs restartingif the node’s certificate changes, the service needs to be restarted
* CA’s public key must be on server, readable bysshd, and configured inTrustedUserCAKeys
* server’s host key needs signing and must be placed alongside host key file(s)
* sshd_configrequiresHostCertificatepointing to the certificate of the host key
* server needs restarting
* if the node’s certificate changes, the service needs to be restarted
* on the client:user’s SSH key needs to be signed by CA and placed adjacent to the key fileuser’s SSH key may be in SSH agent; if it isn’t and the key is encrypted, SSH will as usual ask for its passphrase if there is oneknown_hostsneeds correct@cert-authority; pay attention to principal names (test with*to permit any hostname)the node name or address used when connecting to server must match one of the principal names in host key certificate on server
* user’s SSH key needs to be signed by CA and placed adjacent to the key file
* user’s SSH key may be in SSH agent; if it isn’t and the key is encrypted, SSH will as usual ask for its passphrase if there is one
* known_hostsneeds correct@cert-authority; pay attention to principal names (test with*to permit any hostname)
* the node name or address used when connecting to server must match one of the principal names in host key certificate on server
* If I do get prompted to confirm the host fingerprint, it is possible the certificate has expired, and I am told so.$ssh-oStrictHostKeyChecking=ask-oIdentitiesOnly=true-ijane-lroot 192.0.2.65Certificate invalid: expired
 The authenticity of host '192.0.2.65 (192.0.2.65)' can't be established.
 ED25519 key fingerprint is SHA256:3zm2UIyqO0xsxejndKdg9+Rpm4JeGuxamlsZwNOGX2Y.
 This key is not known by any other names.
 Are you sure you want to continue connecting (yes/no/[fingerprint])? ^C
* on the other hand, if I’m prompted for a password, it is quite likely that a constraint in the certificate cannot be validated. Here I’m tyring to login as a user for which the certificate has no principal configure. The server log shows it.$ssh-ijane-lansible 192.0.2.65ansible@192.0.2.65's password:

 % journalctl -f
 sshd-session[6622]: error: Certificate invalid: name is not a listed principal
* adding a user’s key to an SSH agent shows that both it and the cert have been added (both need to be removed with-dif desired)$ssh-add janeEnter passphrase for jane:
 Identity added: jane (Jane's key)
 Certificate added: jane-cert.pub (Jane Jolie)$ssh-add-l256 SHA256:2WH263LauVfk5XvxHvrdvNt0y9OgaHBLSvcQ+R6u/KE Jane's key (ECDSA)
 256 SHA256:2WH263LauVfk5XvxHvrdvNt0y9OgaHBLSvcQ+R6u/KE Jane's key (ECDSA-CERT)
* during signing of user certificates features can be enabled or disabled. Here we clear all options, then add permission for agent forwarding and port forwarding. Note that pseudo-tty (PTY) allocation is therefore explicitly disabled. We can login to the target node, but do not get a PTY allocated, i.e. we have no console$ssh-keygen-U\-sCA/ssh-ca\-I"Jane Jolie"\-njane,root\-z4\-V+1w\-Oclear\-Oextension:permit-agent-forwarding\-Oextension:permit-port-forwarding\jane.pubSigned user key jane-cert.pub: id "Jane Jolie" serial 4 for jane,root valid from 2026-03-28T15:01:00 to 2026-04-04T16:02:02$ssh-keygen-L-fjane-cert.pubjane-cert.pub:
 Type: ecdsa-sha2-nistp256-cert-v01@openssh.com user certificate
 Public key: ECDSA-CERT SHA256:2WH263LauVfk5XvxHvrdvNt0y9OgaHBLSvcQ+R6u/KE
 Signing CA: ECDSA SHA256:A5ZBb5b/GbAv03EAb8fmDzv4p+q0g8Ulxrt8QZpbamM (using ecdsa-sha2-nistp256)
 Key ID: "Jane Jolie"
 Serial: 4
 Valid: from 2026-03-28T15:01:00 to 2026-04-04T16:02:02
 Principals:
 jane
 root
 Critical Options: (none)
 Extensions:
 permit-agent-forwarding
 permit-port-forwarding$ssh-ljane o78PTY allocation request failed on channel 0$ssh-ljane o78unameOpenBSD

And the “magical” part of all this? The signing user’s SSH certificate configures these capabilities: neither the key, nor an entry in a user’sauthorized_keysfile on the target system have been added.

### Automate host key certificate distribution?

Being able to easily sign host keys got me thinking that it would likely be easy’ish to do this automatically. I quickly shredded my idea of an CGI (Common Gateway Interface) shell script which invokedssh-keygenwhen I came accrosssshkey-tools, a well-documented Python module with which I can programmatically issue and sign SSH certificates.

An initialsign.pywas quickly created, and I then wrapped that into a BottlePy HTTP server, as proof of concept:

* on the machine containing the CA, I launch my smallhost key bot(hkbot.py)for which I don’t yet have a logo but patent is pending. :-)$ ./hkbot.py
 Bottle v0.13.4 server starting up (using WSGIRefServer())...
 Listening on http://0.0.0.0:8870/
 Hit Ctrl-C to quit.
* on a client node onto which I want to have a host key signed, I upload one of host’s public keys to the bot which will determine the key type (the Python module does that automatically), and sign a certificate which it returns together with verybasic shell commands to installthe CA’s public key, the newly issued certificate, and with which to patch/etc/ssh/sshd_configwith the necessary statements.# curl -sSf -F hostkey=@/etc/ssh/ssh_host_ed25519_key.pub http://192.0.2.140:8870 | sh
 Extracting CA public key to /etc/ssh/ssh-ca.pub
 Extracting certificate to /etc/ssh/ssh_host_ed25519_key-cert.pub
 Patching /etc/ssh/sshd_config
 Validating /etc/ssh/sshd_config
* after verifyingsshd_configI restart the service# systemctl restart sshd
* I should now be able to seamlessly login to the machine. Using-vto show what the server sends, and explicitly settingaskto make sure I’m informed should a host key not be verifiable.$ ssh -v -o IdentitiesOnly=true -i jane -l root 192.0.2.65
 ...
 debug1: Server host certificate: ssh-ed25519-cert-v01@openssh.com SHA256:4WTRnq2OR1m03TpnHCfkFdlh1gN/PBXE4vDi0WnjFEc, serial 27 ID "deadbeef01" CA ecdsa-sha2-nistp256 SHA256:A5ZBb5b/GbAv03EAb8fmDzv4p+q0g8Ulxrt8QZpbamM valid from 2026-04-02T10:19:46 to 2026-04-02T11:19:46
 ...
 root@node:~#
* I keep an eye on the auth log (syslog) or the journal (systemd) for incoming connections on the machineApr 02 10:22:07 d13 sshd-session[1058]: Accepted publickey for root from 192.0.2.140 port 54872 ssh2: ECDSA-CERT SHA256:2WH263LauVfk5XvxHvrdvNt0y9OgaHBLSvcQ+R6u/KE ID Jane Jolie (serial 4) CA ECDSA SHA256:A5ZBb5b/GbAv03EAb8fmDzv4p+q0g8Ulxrt8QZpbamMIt’s a bit primitive, and there are lots of bits missing for real-life, but I was able to scratch an itch.

The title of this post is “SSH certificates: the better SSH experience”, and I really believe SSH certificates provide the better and more seamless operation:

* No more need for TOFU (Trust On First Use), as clients and servers implicitly trust each other.
* SSH certificates allow me to issue short-lived keys to users (you may login in the next 20 minutes, after that not again). (If the user remains logged in, there’s no automation to kick them out.)
* The use of SSH certificates means I don’t have to clean up and remove public user keys from servers (i.e. remove entries fromauthorized_keysfiles); once the validity of the certificate expires, the user is locked out.
* Certificates can contain forced-commands, we can permit or deny creation of PTY on the remote, and the target users (principals) and permissible source addresses can be specified.

I demonstrated above that some of this can be automated, and there is a very interesting project calledSmallstep SSHwith tools to enable all that and much more.

### Further reading

* Mozilla’s OpenSSH guidelines
* A Large-Scale Analysis of SSH Host Key Fingerprint Verification Records in the DNS
* An interesting paper onimplementing OpenSSH certificate support in PuTTY, and a link documentinghow to configure PuTTY (v0.83) to accept host certificates

### Updates

* Stefan Eissing rightly points out:This is neat for hosts that youown, e.g. where you have control of the CA and access to its private key which one needs for signing hosts/user keys. The “traditional” known_hosts/authorized keys was made for multi-user systems where you want secure connections between systems where you do not have root privileges. But nowadays, most usage falls into the first category, I assume. And a CA makes that easier.
* I learn from Job Snijders about an I-D for the SSH Certificate Format, indraft-miller-ssh-cert-06.

<Earlier

ssh, unix, and linux
 :: 
03 Apr 2026
 :: 
e-mail
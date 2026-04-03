---
title: NGINX Introduces Native Support for ACME Protocol – NGINX Community Blog
url: https://blog.nginx.org/blog/native-support-for-acme-protocol
site_name: hackernews_api
fetched_at: '2025-08-15T10:02:39.676993'
original_url: https://blog.nginx.org/blog/native-support-for-acme-protocol
author: phickey
date: '2025-08-14'
description: Nginx introduces native support for ACME protocol
tags:
- hackernews
- trending
---

# NGINX Introduces Native Support for ACME Protocol

Aug 12, 2025

—

by

Prabhat Dixit

in
Uncategorized

We are very excited to announce the preview release ofACME support in NGINX. The implementation introduces a new modulengx_http_acme_modulethat provides built-in directives for requesting, installing, and renewing certificates directly from NGINX configuration. The ACME support leverages ourNGINX-Rust SDKand is available as a Rust-based dynamic module for both NGINX Open Source users as well as enterprise NGINX One customers using NGINX Plus.

NGINX’s native support for ACME brings a variety of benefits that simplify and enhance the overall SSL/TLS certificate management process. Being able toconfigure ACME directly using NGINX directivesdrastically reduces manual errors and eliminates much of the ongoing overhead traditionally associated with managing SSL/TLS certificates. It also reduces reliance on external tools like Certbot, creating a more secure and streamlined workflow with fewer vulnerabilities and a smaller attack surface. Additionally, unlike existing external tools which can be prone to platform-specific limitations, a native implementation ensures greater portability and platform independence, making it a versatile and reliable solution for modern, evolving web infrastructures.

## What is ACME?

TheACME protocol(Automated Certificate Management Environment) is a communications protocol primarily designed to automate the process of issuing, validating, renewing, and revoking digital security certificates (e.g., SSL/TLS certificates). It allows clients to interact with a Certificate Authority (CA) without requiring manual intervention, simplifying the deployment of secure websites and other services that rely on HTTPS.

The ACME protocol was initially developed by theInternet Security Research Group (ISRG)as part of theLet’s Encryptinitiative in late 2015, offering free, automated SSL/TLS certificates. Before ACME, obtaining TLS certificates was often a manual, costly, and error-prone process. ACME revolutionized this by providing open-source, automated workflows for certificate management.

ACMEv2is an updated version of the original ACME protocol. It added support for new challenges, expanded authentication methods, wildcard certificates, and other enhancements to improve flexibility and security.

## NGINX ACME Workflow

The ACME workflow with NGINX can be broken into 4 steps:

1. Setting up the ACME Server
2. Allocating Shared Memory
3. Configuring Challenges
4. Certificate Issue and Renewal

### Setting up the ACME Server

To enable ACME functionality, the first (and the only mandatory step) is to specify the directory URL of the ACME server.

Additional information regarding how to contact the client in case of certificate-related issues or where to store module data can also be provided, as shown.

acme_issuer

letsencrypt
 { 
   
uri
         https://acme-v02.api.letsencrypt.org/directory; 
    #
contact
   admin@example.test; 
   
state_path
  /var/cache/nginx/acme-letsencrypt; 

    accept_terms_of_service; 
}

### Allocating Shared Memory

The implementation also provides an optional directiveacme_shared_zoneto store certificates, private keys, and challenge data for all the configured certificate issuers. The zone has a default size of 256K, which can be increased as required.

acme_shared_zone
 zone=acme_shared:1M; 

### Configuring Challenges

The current preview implementation supports HTTP-01 challenges to verify the client’s domain ownership. It requires defining a listener on port 80 in the nginx configuration to process ACME HTTP-01 challenges:

server
 { 
    # listener on port 80 is required to process ACME HTTP-01 challenges 
   
listen

80
; 

   
location
 / { 
 #Serve a basic 404 response while listening for challenges 
       
 return 404
; 
    } 
}

Support for other challenges (TLS-ALPN, DNS -01) is planned infuture.

### Certificate Issuance and Renewal

Use theacme_certificatedirective in the respective server block in your NGINX configuration to automate the issuance/renewal of TLS certificates. The directive requires the list of identifiers(domains) for which the certificates need to be dynamically issued. The list of identifiers can be defined using theserver_namedirective.

The snippet below shows how to configure the server block for issuing/renewing SSL certificate for “.example.domain” domain using the previously definedletsencryptACME certificate issuer.

server
 { 

   
listen
 443 ssl; 

   
server_name
  .example.com; 

   
acme_certificate
 letsencrypt; 

   
ssl_certificate
       $acme_certificate; 
   
ssl_certificate_key
   $acme_certificate_key; 
   
ssl_certificate_cache
 max=2; 
}

Note that not all values accepted byserver_namedirective are valid identifiers. Wildcards are not supported in this initial implementation. Regular expressions are not supported.

Use the$acme_certificateand$acme_certificate_keyvariables in the module to pass the SSL certificate and key information for the associated domain.

## Why It All Matters?

The rapid rise of HTTPS adoption globally has been driven largely by ACME protocol, making secure web connections a standard expectation. ACME modernizes the way TLS/SSL certificates are issued, renewed, and managed by automating the entire process, eliminating manual effort and reducing costs associated with certificate lifecycle management. Beyond the web, the growth of IoT devices and edge computing positions ACME to play a critical role in automating security for APIs, devices, and edge compute infrastructures.

NGINX’s native support for ACME underscores the protocol’s importance for the future of web security, automation, and scalability. ACME is expected to remain the backbone of certificate automation across the internet and beyond for foreseeable future. With security becoming a baseline for web standards, we’ll continue seeing requirements for evolving deployment models and security needs, pushing improvements in ACME.

Looking ahead, we are committed to evolving our implementation to align with the needs of our users and customers, meeting them where they are today and building capabilities for where they are headed in the future.

## How to Get Started

Get startedwith the native ACME implementation in NGINX today. If you are an open source user, pre-built packages are availablehere. If you are an enterprise NGINX One customer using NGINX Plus, pre-built packages are available as a F5 supporteddynamic module. For more information on the module, refer to theNGINX Docs.

### Community Feedback

As always, your feedback is invaluable in shaping the future development of NGINX. If you have suggestions, encounter issues, or want to request additional features, please share them throughGitHub Issues. We can’t wait for you to try it out.

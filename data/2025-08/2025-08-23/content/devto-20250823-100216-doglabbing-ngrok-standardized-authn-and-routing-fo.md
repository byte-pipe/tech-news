---
title: '''Doglabbing'' ngrok: Standardized AuthN and routing for everything - DEV Community'
url: https://dev.to/ngrok/doglabbing-ngrok-standardized-authn-and-routing-for-everything-8ok
site_name: devto
fetched_at: '2025-08-23T10:02:16.069412'
original_url: https://dev.to/ngrok/doglabbing-ngrok-standardized-authn-and-routing-for-everything-8ok
author: Joel Hans
date: '2025-08-19'
description: Welcome to the second in our series on "doglabbing" ngrok—you know, what we all call it when your... Tagged with kubernetes, homelab, devops, linux.
tags: '#kubernetes, #homelab, #devops, #linux'
---

Welcome to the second in our series on "doglabbing" ngrok—you know, what we all call it when your engineers use your product in their homelabs and side projects.

This time, it's James' homelab for a whole bunch of self-hosted services he shares with friends and family.

--

## James (Senior Software Engineer): Standardized AuthN and routing for everything

I wanted to be able to have a central policy for controlling auth, header additions, and not need to think about these on a per endpoint basis.

My solution was to create a CloudEndpoint CRD attached to wildcard domain, use set-vars to chop off the subdomain and forward-internal to an internal endpoint. Now I don't need to worry where my internal endpoints live, just what they are named. I have ngrok Kubernetes Operator-managed AgentEndpoints, ngrok Docker-started endpoints, and internal CloudEndpoints all with consistent behavior and unified auth.

Gateway config via the ngrok Kubernetes Operator and aCloudEndpointCRD:

on_http_request
:


-

name
:

oauth - google@ngrok.com


actions
:


-

type
:

oauth


config
:


auth_cookie_domain
:

example.com


auth_id
:

oauth


provider
:

google


-

name
:

denied


expressions
:


-

"
!(actions.ngrok.oauth.identity.email

in

['allowed_email_01@gmail.com',


'allowed_email_02@gmail.com',

'allowed_email_03@gmail.com',


'allowed_email_04@gmail.com'])"


actions
:


-

type
:

custom-response


config
:


body
:

Not Authorized


status_code
:

403


-

name
:

savesubdomain


actions
:


-

type
:

set-vars


config
:


vars
:


-

inbound_subdomain
:

${req.host.split('.example.com')[0]}


-

name
:

add auth header


actions
:


-

config
:


headers
:


NGROK_AUTH_USER_EMAIL
:

${actions.ngrok.oauth.identity.email}


type
:

add-headers


-

name
:

forward-k8s


actions
:


-

config
:


url
:

https://${vars.inbound_subdomain}.internal


type
:

forward-internal

Enter fullscreen mode

Exit fullscreen mode

What's happening here?On every HTTP request, this policy:

1. Enforces OAuth-based authentication using Google.
2. Filters out all logins from email accounts thatdo notmatch one of James' trusted friends (anonymized here, naturally).
3. Creates a custom variable that splits a subdomain likeservice-foo.example.comintoservice-fooand stores that.
4. Adds a header to the authenticated request based on the Google account used to log in, which is used in upstreams to associate requests with existing accounts.
5. Forwards the request to one of many internal endpoints running on James' Kubernetes cluster at home.

--

Tomorrow = one more doglabbing setup! In the meantime, here are the docs for all the pieces of ngrok James is playing with in his homelab setup.

* ngrok Kubernetes Operator
* CloudEndpointCRD
* AgentEndpointCRD
* oauthTraffic Policy action
* custom-responseTraffic Policy action
* set-varsTraffic Policy action
* add-headersTraffic Policy action
* forward-internalTraffic Policy action

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse

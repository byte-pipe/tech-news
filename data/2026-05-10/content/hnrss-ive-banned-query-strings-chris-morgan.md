---
title: I’ve banned query strings — Chris Morgan
url: https://chrismorgan.info/no-query-strings
site_name: hnrss
content_file: hnrss-ive-banned-query-strings-chris-morgan
fetched_at: '2026-05-10T07:46:00.072848'
original_url: https://chrismorgan.info/no-query-strings
author: Chris Morgan
date: '2026-05-09'
description: I’ve banned query strings
tags:
- hackernews
- hnrss
---

# I’ve banned query strings

 

🗓️2026-05-08•Tagged/web,/opinions,/meta=only

 
 

I don’t like people adding tracking stuff to URLs.Still less do I like people adding tracking stuff tomyURLs.https://chrismorgan.info/no-query-strings?ref=example.com? Did I ask?If I wanted to know I’d look at theRefererheader; and if it isn’t there, it’s probably for a good reason.You abuse your users by adding that to the link.https://chrismorgan.info/no-query-strings?utm_source=example&utm_&c.?Hey! That one’s even worse,UTM parametersare formeto use, notyou.Leave my URLs alone.So I’ve decided to try a blanket ban for this site:no unauthorised query strings.At present I don’t use any query strings.If I ever start using any query strings, I’ll allow only known parameters.(In past times I used?t=…and?h=…cache-busting URLs for stylesheet URLs;and I decided I’m okay breaking such requests; there shouldn’t be any legitimate ones.)Want to see what happens if you add a query string?Go ahead, try it.It’s my website: I can do what I want with it.And you can do what you want with yours!This is currently implementedin my Caddyfile.
---
title: Don't couple your Go code to GitHub | Iain Cambridge
url: https://iain.rocks/blog/dont-couple-your-go-code-to-github
site_name: hackernews_api
content_file: hackernews_api-dont-couple-your-go-code-to-github-iain-cambridge
fetched_at: '2026-09-28T13:22:22.382487'
original_url: https://iain.rocks/blog/dont-couple-your-go-code-to-github
author: birdculture
date: '2026-09-28'
description: The technical musings of Iain Cambridge.
tags:
- hackernews
- trending
---

# Don't couple your Go code to GitHub

Sep 27, 2026

One of the good features of Go is that you namespace your code with the location to fetch the code. This means if you host your Go code at http://github.com/thetrueares/boneclone then you have the line import “github.com/thetrueares/boneclone” and Go will fetch it using git. This makes it super easy to know where to go to report bugs for open source libraries and really easy to fetch and distribute go libraries without a centralised package management system. For many, it’s literally the location of the git hosting, but this has some downsides, and you should use your own custom domain, and I’ll explain why.

Problem

The main problem with using your git hosting location is that your code is now coupled to a hosting provider. That is, if you move your git hosting to GitLab then you have to change your code! Otherwise, you’ll be fetching the old verison. This can result in you being unable to change git hosting provider because the amount of overhead in switching. So you literally end up with your code coupled to GitHub. Which sounds completely nuts, but it’s something that is pretty much defacto in the Go community.

I’ve seen this problem become such a huge issue for a company that were using GitLab, GitHub, and Azure Devops at the sametime because changing the location of the code was such a large task for them and they didn’t “have time” that it was easier for them to operate on three platforms. And is why I built Boneclone to handle skeleton code replication across multiple git hosting platforms at the same time. So this problem literally cost the company money since they had to pay for three hosting services at the same time.

Solution

The solution is to use custom domains such as go.iain.rocks, go.uber.org, go.mongodb.org, etc. This allows you to just change where those domains point to. For example, go.iain.rocks/boneclone points to github.com/thetrueares/boneclone and if I move to GitLab nothing will change for the end users the install command is the same.

In my opinion, every commerical software development team using Go should be using custom domains for namespacing their internal libraries and packages. As it’s an easy way to avoid any pointless coupling.

Here is a copy of my configs so you can set it up for your projects too.

### Nginx.conf

server {
 server_name go.iain.rocks;
 root /var/www/go.iain.rocks;
 index index.html;

 location / {
 # Check if the query string does NOT contain 'go-get=1'.
 # The '~' is for a case-sensitive match.
 if ($args !~ go-get=1) {
 # This is a human visitor. Issue a permanent redirect to GitHub.
 # $request_uri will be the path, e.g., /boneclone
 return 301 https://github.com/that-guy-iain$request_uri;
 }

 # If it's the Go tool (with ?go-get=1), serve the HTML file as before.
 try_files $uri $uri/ =404;
 }

 # --- Your SSL configuration from Certbot should remain here ---
 listen 443 ssl;
 listen [::]:443 ssl;
 ssl_certificate /etc/letsencrypt/live/go.iain.rocks/fullchain.pem;
 ssl_certificate_key /etc/letsencrypt/live/go.iain.rocks/privkey.pem;
 include /etc/letsencrypt/options-ssl-nginx.conf;
 ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;
}

# The HTTP to HTTPS redirect block should also remain.
server {
 listen 80;
 listen [::]:80;
 server_name go.iain.rocks;
 return 301 https://$host$request_uri;
}

### index.html

<!DOCTYPE html>
<html>
 <head>
 <meta charset="utf-8">
 <meta name="go-import" content="go.iain.rocks/boneclone git https://github.com/that-guy-iain/boneclone">
 <meta name="go-source" content="go.iain.rocks/boneclone https://github.com/that-guy-iain/boneclone https://github.com/that-guy-iain/boneclone/tree/master{/dir} https://github.com/that-guy-iain/boneclone/blob/master{/dir}/{file}#L{line}">
 </head>
 <body>
 </body>
</html>
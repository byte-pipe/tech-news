---
# '100 Days of DevOps, Day 1: Understanding Linux User Management and Shells - DEV Community'
url: https://dev.to/olymahmud/100-days-of-devops-day-1-understanding-linux-user-management-and-shells-4f8n
site_name: devto
fetched_at: '2025-09-12T19:06:14.059241'
original_url: https://dev.to/olymahmud/100-days-of-devops-day-1-understanding-linux-user-management-and-shells-4f8n
author: M. Oly Mahmud
date: '2025-09-06'
description: Welcome to Day 1 of our DevOps journey. DevOps engineers spend much of their time working with Linux... Tagged with devops, linux, devchallenge, 100daysofdevops.
tags: '#devops, #linux, #devchallenge, #100daysofdevops'
---

Welcome toDay 1of our DevOps journey. DevOps engineers spend much of their time working with Linux servers, either manually or via automation. So, we're going to start right at the core:Linux user managementandshell types.

## CRUD Operations on Users in Linux

Think ofCRUD(Create, Read, Update, Delete) as the four verbs of system management. Same idea you see in databases, but here applied to users:

### 1.Create a user

sudo useradd yousuf

Enter fullscreen mode

Exit fullscreen mode

This creates a new user account namedyousuf.

Would you like to add a home directory as well? Use:

sudo useradd -m yousuf

Enter fullscreen mode

Exit fullscreen mode

### 2.Read (check/display) user info

id yousuf getent passwd yousuf

Enter fullscreen mode

Exit fullscreen mode

This gives you the UID (User ID), GID (Group ID), and assigned shell.

### 3.Update (modify) a user

Change the user's shell:

sudo usermod -s /bin/bash yousuf

Enter fullscreen mode

Exit fullscreen mode

Change the user's home directory:

sudo usermod -d /home/new_home yousuf

Enter fullscreen mode

Exit fullscreen mode

### 4.Delete a user

Delete account but keep home directory:

sudo userdel yousuf

Enter fullscreen mode

Exit fullscreen mode

Delete account along with home directory:

sudo userdel -r yousuf

Enter fullscreen mode

Exit fullscreen mode

💡 Remember: deleting a user won't magically destroy files they created elsewhere unless you track them down. So always think before you hit the red button.

## Interactive vs Non-Interactive Shell

Now let's add nuance:what happens when a user logs in?

### Interactive Shell

- User logs in → gets a prompt.
- Example:

ssh yousuf@server yousuf@server:~

Enter fullscreen mode

Exit fullscreen mode

- Here,yousufhas/bin/bashor/bin/shas login shell. He can interactively run commands.

### Non-Interactive Shell

- User logs in →no prompt, no mercy.
- Example shells for this are/sbin/nologinor/bin/false.
- If someone tries:

ssh yousuf@server

Enter fullscreen mode

Exit fullscreen mode

- With/sbin/nologin: system politely says"This account is not available."
- With/bin/false: just exits immediately, no message.

✅ This is useful for service accounts (databases, backup agents, monitoring tools) that don't require human logins.

## Practical Challenge

Now let's take the real-world styled problem (straight out of KodeKloud Labs)

Scenario:To accommodate the backup agent tool's specifications, the system admin team at xFusionCorp Industries requires the creation of a user with a non-interactive shell.

Task:Create a user namedyousufwith a non-interactive shell onApp Server 3.

📑Connection Details (important bits):

- Target server:stapp03→172.16.238.12
- Login user:banner
- Password:BigGr33n
- Jump host:jump_host.stratos.xfusioncorp.com(thor/mjolnir123)

## Step-by-Step Solution

### Step 1: SSH into the Jump Host

ssh thor@jump_host.stratos.xfusioncorp.com

# password: mjolnir123

Enter fullscreen mode

Exit fullscreen mode

### Step 2: From Jump Host, SSH into App Server 3

ssh banner@stapp03.stratos.xfusioncorp.com

# password: BigGr33n

Enter fullscreen mode

Exit fullscreen mode

Now you're inside App Server 3.

### Step 3: Create the user with a non-interactive shell

We'll use/sbin/nologin(common on most Linux distros) to ensure no interactive login:

sudo useradd -s /sbin/nologin yousuf

Enter fullscreen mode

Exit fullscreen mode

If/sbin/nologinisn't available, fall back on/bin/false:

sudo useradd -s /bin/false yousuf

Enter fullscreen mode

Exit fullscreen mode

### Step 4: Verify the user

getent passwd yousuf

Enter fullscreen mode

Exit fullscreen mode

Expected output (example):

yousuf:x:1005:1005::/home/yousuf:/sbin/nologin

Enter fullscreen mode

Exit fullscreen mode

That last field confirms it isnon-interactive. 🎉

## Conclusion

OnDay 1, we:

1. Learned CRUD operations for user accounts.
2. Exploredinteractivevsnon-interactiveshells with clear examples.
3. Applied this in a practical scenario: creating theyousufuser with a non-interactive shell on App Server 3.

Create template

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse

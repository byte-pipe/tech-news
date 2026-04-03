---
title: 'Google Testing Blog: Simplify Your Code: Functional Core, Imperative Shell'
url: https://testing.googleblog.com/2025/10/simplify-your-code-functional-core.html
site_name: hackernews_api
fetched_at: '2025-10-28T19:07:32.955495'
original_url: https://testing.googleblog.com/2025/10/simplify-your-code-functional-core.html
author: reqo
date: '2025-10-25'
description: 'Simplify your code: Functional core, imperative shell'
tags:
- hackernews
- trending
---

This article was adapted from a Google
Tech on the Toilet
 (TotT) episode. You can download a
printer-friendly version
 of this TotT episode and post it in your office.
By Arham Jain

Is your code a tangled mess of business logic and side effects?Mixing database calls, network requests, and other external interactions directly with your core logic can lead to code that’s difficult to test, reuse, and understand. Instead, consider writing afunctional corethat’s called from animperativ​​e shell.

Separating your code into functional cores and imperative shells makes it more testable, maintainable, and adaptable.The core logic can be tested in isolation, and the imperati​​ve shell can be swapped out or modified as needed. Here’s some messy example code that mixes logic and side effects to send expiration notification emails to users:

// Bad: Logic and side effects are mixed

functionsendUserExpiryEmail(): void{

for (const user of db.getUsers()) {

if (user.subscriptionEndDate > Date.now()) continue;

if (user.isFreeTrial) continue;

email.send(user.email, "Your account has expired " + user.name + “.”);

}

}

Afunctional coreshould contain pure, testable business logic, which is free of side effects (such as I/O or external state mutation). It operates only on the data it is given.

Animperative shellis responsible for side effects,like database calls and sending emails. It uses the functions in your functional core to perform the business logic.

Rewriting the above code to follow the functional core / imperative shell pattern might look like:

Functional core

functiongetExpiredUsers(users: User[], cutoff: Date): User[]{

return users.filter(user => user.subscriptionEndDate <= cutoff && !user.isFreeTrial);

}

functiongenerateExpiryEmails(users: User[]): Array<[string, string]>{

return users.map(user =>

([user.email, “Your account has expired “ + user.name + “.”])

);

}

Imperative shell

email.bulkSend(generateExpiryEmails(getExpiredUsers(db.getUsers(), Date.now())));

Now that the code is following this pattern, adding a feature to send a new type of email is as simple as writing a new pure function and reusinggetExpiredUsers:

// Sending a reminder email to users

functiongenerateReminderEmails(users: User[], cutoff: Date): Array<[string, string]>{...}

const fiveDaysFromNow = ...

email.bulkSend(generateReminderEmails(getExpiredUsers(db.getUsers(), fiveDaysFromNow)));

Learn more in
Gary Bernhardt’s original talk
 about functional core, imperative shell.

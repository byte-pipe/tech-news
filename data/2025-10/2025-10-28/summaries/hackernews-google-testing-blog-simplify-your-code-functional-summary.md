---
title: Google Testing Blog: Simplify Your Code: Functional Core, Imperative Shell
url: https://testing.googleblog.com/2025/10/simplify-your-code-functional-core.html
date: 2025-10-28
site: hackernews
model: llama3.2:1b
summarized_at: 2025-10-28T11:28:14.551339
screenshot: hackernews-google-testing-blog-simplify-your-code-functional.png
---

# Google Testing Blog: Simplify Your Code: Functional Core, Imperative Shell

**Separated Code: Functional Core and Imperative Shell Pattern**
===========================================================

The code provided demonstrates the separation of concerns between a functional core and an imperative shell.

### **Functional Core**

The functional core is responsible for pure, testable business logic that operates only on data it is given. It consists of two functions:

* `getExpiredUsers`: Filter users based on expiration dates.
* `generateExpiryEmails`: Generate emails for expired users.

```javascript
function getExpiredUsers(users: User[], cutoff: Date): User[] {
  return users.filter(user => user.subscriptionEndDate <= cutoff && !user.isFreeTrial);
}

function generateExpiryEmails(users: User[]): Array<[string, string]> {
  return users.map(user => [
    [user.email, 'Your account has expired ' + user.name + '.'],
  ]);
}
```

### **Imperative Shell**

The imperative shell is responsible for side effects such as database calls and sending emails. It uses the functions in the functional core to perform business logic.

```javascript
// Send expiry emails using the imperative shell
function generateExpiryEmails(users: User[]): Array<[string, string]> {
  return users.map(user => [email.send(user.email, 'Your account has expired ' + user.name + '.']));
}

function email.bulkSendemails(generateExpiryEmails(getExpiredUsers(db.getUsers(), Date.now())) {
  // Code for sending bulk emails goes here
}
```

**Benefits of Separation of Concerns**
-------------------------------------

Separating the code into functional and imperative parts improves maintainability, testability, and adaptability. This approach allows for easier modification or replacement of the imperative part without affecting the rest of the system.

### **Improving Testability**

With a separate core logic that can be tested in isolation, it becomes easier to write unit tests for individual functions or components within the core logic.

```javascript
// Test: getExpiredUsers
describe('getExpiredUsers', () => {
  const users = [
    { subscriptionEndDate: new Date('2023-03-15'), isFreeTrial: false },
    { subscriptionEndDate: new Date('2022-10-01') },
  ];

  it('should return expired users', () => {
    expect(getExpiredUsers(users)).toBe(users.filter(user => user.subscriptionEndDate <= new Date()))
      .slice(0, 2); // Return first two expired users
  });
});
```

Similarly, test the `generateExpiryEmails` function by exercising its API using mock objects or a mock email service.

### **Easier Maintenance**

By separating concerns into different parts, it's easier to understand and maintain each component independently. The imperative shell doesn't directly interact with the functional core logic, making it more maintainable over time.

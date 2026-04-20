---
title: Everything Should Be Typed: Scalar Types Are Not Enough
url: https://sot.dev/everything-should-be-typed.html
date: 2026-04-20
site: tldr
model: llama3.2:1b
summarized_at: 2026-04-20T06:08:44.652107
---

# Everything Should Be Typed: Scalar Types Are Not Enough

**Everything Should Be Typed: Scalar Types Are Not Enough**

A widely-accepted technique for writing more safe and reliable code is to ensure that every variable, function parameter, and return value has a well-defined and consistently typed data structure. This helps prevent numerous common errors, such as incorrect types causing compiler warnings or runtime exceptions.

Recently, I encountered an example of how scalar types can lead to issues that may seem minor but have significant implications if not addressed correctly. The case involves a function that processes seller payouts, taking parameters with specific types and returning another value with the same types. However, the approach used does not guarantee correctness due to a flaw in its implementation.

**The Positional Parameter Problem**

Let's take a closer look at how the `processOrderPayout` function in JavaScript is structured:

```javascript
function processOrderPayout(params) {
  // code here...
}

// Example usage:
const orderPayoutParams = { shopId: '123456', customerId: '7890123', orderId: 'abcde' };
processOrderPayout(orderPayoutParams);
```

Notice how the parameters are declared with type annotations `(shopId, customerId, orderId, amount, platformFee, txFee, netAmount)`. However, in this case, there's a crucial mistake. The order does not match any specific parameter names; rather, it resembles the property names of the `orderPayoutParams` object.

The issue arises when calling the function with parameters that do not share the same data structure:

```javascript
processOrderPayout({
  shopId,
  customerId,
  orderId: 'fedcba',
  amount,
  platformFee,
  txFee,
  netAmount
});
```

This may lead to unexpected behavior since some of these values are being set at runtime. The compiler, however, checks the data structure's correctness, not its runtime values.

**“Just Use a Struct.” Better, But Not Enough**

To make things more efficient, it seems like grouping parameters into a struct could be beneficial:

```javascript
class ProcessOrderPayoutParams {
  shopId: string;
  customerId: string;
  orderId: string;
  amount: number;
  platformFee: number;
  txFee: number;
  netAmount: number;
}

function processOrderPayout(params: ProcessOrderPayoutParams) {
  // code here...
}
```

Although this struct could potentially avoid the positional parameter issue, its benefits largely hinge on proper usage patterns. Nevertheless, having a struct in place for such parameters is considered good practice.

**Improving Code Quality**

In conclusion, ensuring that every variable has well-defined and consistently typed data structures contributes significantly to writing more reliable code. Scalar types alone are not sufficient; incorporating the right structure can greatly mitigate errors and issues caused by incorrect type usage.

When writing code, consider using structs or objects whenever possible for parameters and return values. This technique provides a deeper understanding of how your functions interact with different variables and helps prevent unexpected behavior.

While every example may look simple, maintaining good coding standards throughout all files significantly improves the overall quality of a project.

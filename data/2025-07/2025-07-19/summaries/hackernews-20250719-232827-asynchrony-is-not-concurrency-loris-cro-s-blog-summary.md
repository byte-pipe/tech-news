---
title: "Asynchrony is not Concurrency | Loris Cro's Blog"
url: https://kristoff.it/blog/asynchrony-is-not-concurrency/
date: 2025-07-19
site: hackernews
model: llama3.2:1b
summarized_at: 2025-07-19T23:28:27.856119
---

# Asynchrony is not Concurrency | Loris Cro's Blog

**Analyzing "Asynchrony is not Concurrency | Loris Cro's Blog" from a Solo Developer Business Perspective**

**Problem Discussion**
The article highlights the importance of understanding asynchrony in concurrent programming. The problem being discussed is whether asynchrony exists and, if so, what its significance is for software ecosystems.

**Market Indicators (User Adoption, Revenue Mentions, Growth Metrics, Customer Pain Points)**

* As synchrony has become more common in modern programming and applications, indicating a growing demand for concurrent capabilities.
* Many cloud service providers offer scalable and efficient solutions that cater to concurrent needs, suggesting a high willingness to pay for such features.
* The article mentions Rob Pike's comment about concurrency being not as useful as the term asynchrony, implying a positive feedback loop for the lack of a clear definition.

**Technical Feasibility for a Solo Developer**
The complexity of writing concurrent code can be overwhelming for solo developers, especially those familiar with parallelism and task switching. However, as synchrony is gaining traction, it may become more feasible to develop concurrent applications:
* Synchrony simplifies the approach by allowing tasks to run in parallel without the need for explicit synchronization primitives like locks or semaphores.
* Examples of popular libraries, frameworks, and services that implement asynchrous programming models (e.g., async/await) demonstrate its applicability.

However, writing robust and efficient concurrent code requires a good understanding of:
* Asynchrony fundamentals
* Event-driven I/O patterns
* Message passing and queuing systems

**Business Viability Signals**
As synchrony becomes more prevalent in software ecosystems, solo developers may enjoy increased business viability signals:

* Growing demand for scalable applications that can handle complex concurrent workflows.
* Higher revenue potential through the sale of concurrent development tools, services, or consulting expertise.

**Actionable Insights**
For solo developers looking to build a profitable business:
* Focus on understanding asynchrony and event-driven I/O patterns to simplify concurrent programming.
* Research popular libraries and frameworks that implement synchronization primitives, such as awaitables or coroutines (e.g., async/await in Node.js).
* Develop expertise in message passing and queuing systems to improve productivity and efficiency.

**Example Code Snippets**
Here's an example code snippet that demonstrates simple asynchrony using a library like `async-mutex`:
```javascript
const Mutex = require('async-mutex').Mutex;

class MyClass {
  async doWork() {
    await Promise.all([
      new Mutex().throwOnComplete(true),
      this.someAsyncOperation()
    ]);
  }
}

// Call the method asynchronously...
async function main() {
  const myClass = new MyClass();
  try {
    await myClass.doWork();
  } catch (error) {
    console.error(error);
  }
}
```
This code snippet uses a mutex to ensure that only one operation is executed at a time.

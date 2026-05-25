---
title: Jira IS Turing-Complete
url: https://seriot.ch/computation/jira.html
date: 2026-05-25
site: hnrss
model: llama3.2:1b
summarized_at: 2026-05-25T12:17:43.932917
---

# Jira IS Turing-Complete

## Turing-Completeness of Jira: A Computation Model

**Introduction**
Atlassian's project-tracking tool, Jira is often considered Turing-complete. However, existing claims about automation features haven't exhibited a reduction in computational power. This article provides a proof of Turing-completeness by mapping the computation model of a Minsky register machine (a Turing-Complete computer) onto Jira's automation language.

**Minsky Register Machine**

The Minsky register machine has only two unbounded counters and a finite set of labeled instructions:

* `INC r; goto S`
* `DEC r; if r == 0	goto S else goto S''

A simplified example can be as follows:

```python
1. DEC A; if A == 0 goto 3 else goto 2
2. INC B;.goto 1
3. HALT
```

This model maps onto Jira's automation language, which allows for recursive state transitions and conditional branching.

**Jira Automation Language**

The Jira automation language consists of program counters, status codes, dispatch tables, clock events, and rules that interact with those entities to perform automated tasks or trigger other rules. Here's how the computation model maps onto these components:

* **Program Counter**: Updates the current instruction index.
* **Status Code**: Represents the current state of a Jira issue (e.g., Epic, Bug, Task).
* **Dispatch Table**: Routes between different states and statuses based on conditions specified in JQL (JIRA Query Language).

**Transitioning between States**

The Minsky register machine's clock triggers external re-triggering past chain caps. In Jira, this is achieved through automation rules that interact with linked-issues counts to determine the next state.

* **Epic Status**: Updates a single Epic's status based on its current `status code`.
* **Task Creation**: Creates a new Task and links it to an existing Epic.
* **Deletion Rule**: Deletes one Bug if the `Epic` is in TODO status.
* **Transition to DEV**: Transitions the Epic to DEV.

**Implementation**

To implement the Minsky register machine's computations in Jira, follow these steps:

1. Create a Workflow with initial state: BACKLOG, then TODO, DEV and PROD
2. Integrate Rule 1 (TODO) - `DEC A; if A=0 halt, else goto DEV` to DELETE one BUG and transition EPIC to DEV.
3. Use Rule 3 (DEV) - `INC B;.goto TODO.` to CREATE a new Task, link it to the EPIC.
4. Link 2 Bugs (A=2) and 3 Tasks (B=3) to the EPIC.
5. Initialize registers by linking two Bugs (A=2) and three tasks (B=3).
6. Trigger the machine to start the cascade.

**Proof of Turing-Completeness**

The proof of Turing-completeness relies on mapping the computation model onto Jira's automation language, demonstrating that it is impossible to reduce computational power.

While this process is cumbersome and error-prone for large-scale implementations, the outcome verifies its ability to provide an optimal solution (i.e., no reduction in computation power) due to specific properties of the Minsky register machine. Additionally, Jira's autoworker can apply these same functions: delete bugs, create task tasks and links issues in one step.

## Conclusion
Jira's Turing-completeness is demonstrated through a computational model that aligns with its automation language. By providing a mapping between two programming paradigms, this example verifies the feasibility of reducing computation power. Furthermore, actual implementation can utilize Jira's rule- and workflow-based approaches for creating computations via executing automated tasks.

### Further Reading
For an in-depth look into Turing-completeness, refer to [1] , and explore examples like those provided above or other computational models that are also Turing-Complete.
  
    [1]: https://en.wikipedia.org/wiki/Turing_completeness
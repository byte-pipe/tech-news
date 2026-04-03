---
title: I Built a Skill That Writes Your Specs For You - DEV Community
url: https://dev.to/dannwaneri/i-built-a-skill-that-writes-your-specs-for-you-1o2n
date: 2026-03-17
site: devto
model: llama3.2:1b
summarized_at: 2026-03-18T11:48:53.993487
---

# I Built a Skill That Writes Your Specs For You - DEV Community

# Silent Decisions Problem and Spec Driven Development

Julián DeAngelis' article "I Built a Skill That Writes Your Specs For You" highlighted the importance of discipline in software development, particularly under deadline pressure. However, the process often suffers from missing silent decisions that need to be considered by a specification-driven approach.

## The Silent Decisions Problem

Developers typically rely on specification tools (Q&A) to guide their code. However, these systems require knowledge of what is not known beforehand, making them ineffective in practice. In this article, DeAngelis shares an example where the spec was written immediately and marked for further review before execution.

### Four Steps to Spec Driven Development

DeAngelis outlines four steps to create specifications:

1. **Specify**

   - Given 
      * Authenticate users
*
- When
* Request exports with more than 1000 rows
*
- Actions required:
    + async
    + Notifies by email in fullscreen mode during the export process

2. **Plan**

   * Determine order volumes for asynchronous generation and synchronous usage consideration based on user authentication status.

3. **Break Down Tasks**

   Given large exports
* What should be done?
    1.
        Async generation with synchronous interface
    2.
        Non-async generation for very large datasets

5. **Implement Each Step**

6. **Iterate**

7. **Review and Fix**

## The Spec-Writing Skill

The writer's goal was to remove the specification step from the process, allowing them to write the code directly using a specification-driven approach.

The article illustrates several challenges common in developing specifications driven by ambiguous or unspoken assumptions:

*   Silent decisions: These are assumptions about user roles, authentication models, and more that need to be specified before writing code.
*   Q&A tools fail to reduce friction: Without an explicit spec, developers rely on these tools to guide their thought process. However, the limitations of these systems mean users can make mistakes without being aware.

By removing this step from the process, developers like DeAngelis can write better code by identifying and addressing assumptions directly during implementation stages. This reduces the time spent questioning assumptions in both development cycles.



The skill described here has far-reaching implications for software development practices, as it shifts focus away from traditional Q&A tools towards explicit specification creation. By leveraging a more structured approach, developers can ensure their specifications are valid and executable before entering production phases.

## Code Example: Spec-Writing with DeAngelis' Approach

Here is an example of how one could implement the four steps outlined earlier using code:

```javascript
// SpecStep.js (spec-generated)
function specSteps(){
    // Implementation as per spec given -- full implementation logic 
    // here and it will guide developers to write correct and maintainable code.

    return [
        {
            name: async,  // Specification action with asynchronous interface
            description: 'Exports data asynchronously when the number of rows exceeds 1000',
            condition: 'user.auth',
        },
        {
            name: forLarge,  // Implementation logic for large datasets.
            description: "Non-async export is required for larger export files",
            condition: 'user.ordervolume > 10000' 
        }
    ];
}

// specPlan.js
function specPlan(user){
    const plan = [];
    if (user.auth === true){  // assuming the client-side auth is on this account.
        
        plan.push({
            name: "sync data export" ,  
            condition: false  
         })
         plan.push({
            name: 'async data upload' ,
            condition: user.ordervolume > 10000
           }) 

    }
    return { 
        plan,
        name: 'Plan'
       }
   }

// specBreakDown.js
function specBreakdown( plan){ // breaking down tasks

    const breakdown = {
        tasks: []
     };
    for (let i=0;i<plan.plan.length; i++){   
        if(i === 0)break;
         breakdown.tasks.push(plan.plan[i].name );

  
    }
 
      return{ 
         breakDown,
            name: 'Break Down the specification'

       }
   }

// specImplement.js
function specImplement(tasks, breakdown){
 let implementation = [];
 for(let item of tasks){   
     if(item === "sync data export")    
        implementation.push(['data', {'method' : "async", 'callback': exportData })

    } 
     else  {
         implementation.push(item);  // implementing for each task separately
     }
   return{ specImplement, name: 'Implement Spec'

        }
}

// specReview.js
function specReview(spec, tasks){
let feedback = [];
for(let item of tasks){   
    if(item === 'sync data export'){
        const response = verifyResponse();
if(response !== true ){
    feedback.push("Data export not running asynchronous as required ");
   
           } else {
               feedback.push(" Data export successfully performed and is ready for further actions");

    
    }
} 
return{
feedback,
spec
}
}

// specifyFunctions.js

function generateSpec(spec, user) {

 specification = spec.format(user);

if(specification){
  console.log(specification);
}

let specStepsResult = specSteps();
console.log(specStepsResult);

let specPlan = specPlan(spec);
specPlan.then( ( data)=> {
    let breakdownResult = specBreakdown(data); 
    let implementResult= specImplement(data.breakDown, breakdownResult);    
   specReview(spec, implementResult);      
});

let specPlanPromise = promisepoller(specPlan);
 
}
```

And a call at bottom, in which the implementation is invoked

## Implementation Example: SpecSteps()
```javascript
// specificationStep function
function specStep(){
    return{
        name : "Write Code snippet",
        condition: false // not required or can be true.
    };
}
```
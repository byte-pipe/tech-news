---
title: Go is still not good
url: https://blog.habets.se/2025/07/Go-is-still-not-good.html
date: 2025-08-22
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-08-22T23:32:17.748874
---

# Go is still not good

**Analysis**

The article discusses several issues with Go programming language that are perceived as unnecessary or poorly implemented. These criticisms are geared towards the solo developer audience, particularly those who have been following the author since they first expressed dissatisfaction with Go about a decade ago.

**Market Indicators and Business Viability Signals**

The author notes several indicators that suggest Go is not becoming popular enough for there to be significant growth in the market:

1. The comment at the end of the article mentions that adding more complexity (like allowing reusing `err` values) would only help experienced coders, indicating that the basic language is sufficient.
2. The discussion about two types of nil and how it can lead to confusion does not provide any conclusive evidence for a lack of interest in Go.
3. There is no mention of specific metrics or indicators used to measure market size or user adoption.

Regarding business viability signals:

1. The comment notes that adding unnecessary complexity, such as reusing `err` values, is "dumb." This suggests that the author thinks it's only useful for experienced developers, and not necessary for a solo developer.
2. No mention of existing competition in the Go community or the potential for other programming languages to address similar concerns.

**Technical Feasibility**

The author discusses the complexities of Go programming language and its limitations when dealing with variable scope:

1. The example illustrates how Go's compiler is responsible for inferring the scope of `err`, which can lead to confusion.
2. The discussion concludes that Go cannot handle situations where a value goes out of scope, as demonstrated by the commented code block at the beginning of the article.

**Business Viability Insights**

Based on the provided analysis and comments:

1. Consider reusing values like `err` in specific contexts but avoid using it for non-essential purposes.
2. Avoid expanding Go beyond its capabilities to address existing problems or implement additional features to keep your business viable.

Examples of code reuse while avoiding unnecessary complexity:
```go
for {
    // ...
} // reuse the remaining value if necessary

if err := foo(); err != nil {
    // handle the error, do not reassign err
}

// use a temporary variable to avoid reusing err
tmp := gosomevalue
// then assign back to tmp and continue your code...
```
Example of avoiding unnecessary complex logic:

```go
i := 10
s := s1 // reuse variables

func main() {
    if i == somevalue { // simple condition without unnecessary computation
        fmt.Println("found")
    } else {
        fmt.Println("not found") // only executed when i != somevalue
    }
}

// do this and that...
t, f, _ := s1.S()
fmt.Println(t)
fmt.Println(f)

i = 10

tmp := "hello"
s1 := struct{a string}{tmp := tmp }
```
Keep in mind these examples represent a simplified approach to avoid potential errors.

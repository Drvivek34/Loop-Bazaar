# The sub-50 ms page-load loop

**Loop ID**: #003 | **Category**: Engineering | **Author**: Matthew Berman | **Rating**: ⭐ 4.8/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A performance optimization workflow for coding agents that uses one repeatable benchmark and stops only when every target page meets the threshold.

## 🎯 Use Case (When to Use)
> Use this when a product has a defined set of routes, a stable performance harness, and a 50 ms target that maps to a specific metric and environment.

## ⚡ System Prompt / Instructions
```
Continue optimizing the code for speed. After each significant change, measure page-load performance across every page under the same repeatable test conditions. Continue until every page loads in under 50 ms.
```

## 🏁 Implementation Steps
1. Define the exact metric, routes, test environment, warm-up behavior, and number of benchmark runs.
2. Capture a baseline for every target page before making changes.
3. Make one significant optimization, rerun the same benchmark, and inspect regressions across all routes.
4. Continue until every page meets the threshold under the original test conditions.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Every page loads in under 50 ms.
- *Detail*: Use the same benchmark and confirm there are no regressions.

## 💡 Why it works
The fixed harness prevents performance work from turning into anecdotal tuning. Measuring every route after each change catches local wins that quietly slow down another page.

## ⚠️ Implementation Note
* Page load can mean server response, render completion, or a browser timing metric. Name the metric and hardware explicitly so the 50 ms target is reproducible and meaningful.

## 🏷️ Keywords
AI coding agent, page load optimization, performance benchmark, web performance workflow, 50 ms page load

## 💬 Reviews & Feedback
- **@james_g** (★★★★★ 5/5): *Highly recommended workflow, saves considerable manual sweep time.* (2026-06-19)
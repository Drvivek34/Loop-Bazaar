# The test-suite speed loop

**Loop ID**: #011 | **Category**: Engineering | **Author**: Matthew Berman | **Rating**: ⭐ 4.8/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A performance workflow for reducing test runtime under repeatable conditions without weakening coverage, assertions, isolation, or behavior.

## 🎯 Use Case (When to Use)
> Use this when slow tests are delaying local feedback or continuous integration and the project has stable commands for measuring runtime and coverage.

## ⚡ System Prompt / Instructions
```
Optimize the test suite to run as quickly as possible without reducing coverage or changing behavior.
```

## 🏁 Implementation Steps
1. Record the full-suite runtime, coverage, environment, worker settings, and repeatable timing method.
2. Profile the suite to find expensive setup, redundant work, poor isolation, unnecessary integration paths, or safe parallelization opportunities.
3. Make one optimization at a time, then rerun the full suite and compare timing, coverage, and behavior.
4. Stop at the agreed runtime target or diminishing-returns rule with all original checks still passing.

## 🛑 Stopping Condition (Verification)
**Verification Check**: The suite is faster with no coverage or behavior regression.
- *Detail*: Repeatable timing, the full passing suite, and the original coverage report prove the result.

## 💡 Why it works
A fixed baseline prevents speed work from quietly trading away coverage or correctness. Profiling directs effort toward measured bottlenecks instead of speculative rewrites.

## ⚠️ Implementation Note
* Define a runtime target or diminishing-returns rule before starting. Faster tests are not an improvement if they become flaky, order-dependent, or less representative.

## 🏷️ Keywords
AI coding agent, test suite performance, faster CI, test optimization, coverage preservation

## 💬 Reviews & Feedback
- **@victormustar** (★★★★★ 5/5): *Highly recommended workflow, saves considerable manual sweep time.* (2026-06-19)
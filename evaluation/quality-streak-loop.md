# The quality streak loop

**Loop ID**: #009 | **Category**: Evaluation | **Author**: Matthew Berman | **Rating**: ⭐ 4.8/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A realistic product-testing workflow that turns every failure into documented regression coverage and restarts the success streak after each fix.

## 🎯 Use Case (When to Use)
> Use this when product quality needs a strict consecutive-success bar and failures should permanently improve the test and benchmark suite.

## ⚡ System Prompt / Instructions
```
Test realistic scenarios. When one fails, document it, add regression and benchmark coverage, fix it, and restart the streak. Stop after [N] successful cases in a row.
```

## 🏁 Implementation Steps
1. Define realistic scenarios, the quality bar, the value of [N], and the evidence required for a pass.
2. Run cases one at a time under consistent conditions and preserve the result for review.
3. On any failure, document it, add regression and benchmark coverage, fix the cause, verify the fix, and reset the streak to zero.
4. Stop only after [N] consecutive cases meet the original quality bar.

## 🛑 Stopping Condition (Verification)
**Verification Check**: The latest [N] realistic cases pass in a row.
- *Detail*: Every earlier failure is documented, fixed, and protected by regression and benchmark coverage.

## 💡 Why it works
Restarting the streak prevents isolated successes from hiding intermittent weaknesses. Converting each failure into durable coverage makes the evaluation stronger after every miss.

## ⚠️ Implementation Note
* Choose [N] before the run and keep the scenario distribution representative. Do not lower the quality bar or avoid difficult cases to preserve the streak.

## 🏷️ Keywords
AI product evaluation, quality streak, regression testing, benchmark coverage, realistic scenarios

## 💬 Reviews & Feedback
- **@brendan_e** (★★★★★ 5/5): *Highly recommended workflow, saves considerable manual sweep time.* (2026-06-19)
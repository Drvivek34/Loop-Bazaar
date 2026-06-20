# The self-improving champion loop

**Loop ID**: #023 | **Category**: Evaluation | **Author**: Jose C. Munoz | **Rating**: ⭐ 4.8/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A prompt-optimization workflow that tests challengers on a working set, promotes only fresh holdout wins, and keeps the current champion on uncertainty.

## 🎯 Use Case (When to Use)
> Use this to tune a prompt, policy, or configuration when cheap iteration is useful but final acceptance must use fresh examples.

## ⚡ System Prompt / Instructions
```
Improve a prompt, policy, or configuration. A support assistant's system prompt is one example. Save the champion, its score, a working set, untouched holdout cases, must-pass checks, and [budget]. Each round, change one thing based on a recorded failure. Promote the challenger only if it beats the champion on holdouts by [margin] without weakening a must-pass check; otherwise keep the champion. Stop at the target, budget limit, or no progress. Return the winner, scores, experiment log, and remaining failures.
```

## 🏁 Implementation Steps
1. Save the current champion, working set, untouched holdout cases, must-pass checks, improvement margin, budget, and experiment log.
2. Use a recorded failure to propose one targeted challenger and test it on the working set.
3. Freeze promising challengers and evaluate them on the untouched holdout cases and every must-pass check.
4. Promote only a meaningful, regression-free holdout win; log every result and return the champion at the stop condition.

## 🛑 Stopping Condition (Verification)
**Verification Check**: The best holdout-tested champion is returned.
- *Detail*: Every challenger is logged, and accepted changes beat the previous champion on untouched cases without weakening a must-pass check.

## 💡 Why it works
Separating the working set from fresh holdout cases limits overfitting. Keeping the current best by default prevents regressions, while a fixed budget bounds the search.

## ⚠️ Implementation Note
* Keep the working set and holdout cases separate: edit against the former, judge final acceptance on the latter. Choose the budget and margin before starting, and do not weaken a must-pass check after a failed challenger.

## 🏷️ Keywords
self-improving loop, champion challenger evaluation, Goodhart prevention, independent evaluation gate, bounded optimization workflow

## 💬 Reviews & Feedback
- **@ranvier2d2** (★★★★★ 5/5): *Highly recommended workflow, saves considerable manual sweep time.* (2026-06-19)
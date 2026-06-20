# The Self-Refine loop

**Loop ID**: #5054 | **Category**: Engineering | **Author**: Madaan et al. (2023) | **Rating**: ⭐ 4.7/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
One model both produces output and critiques it, iterating on its own feedback until good enough.

## 🎯 Use Case (When to Use)
> When quality improves with a few rounds of self-feedback (writing, code, answers).

## ⚡ System Prompt / Instructions
```
Produce a draft. Then critique your own draft with specific, actionable feedback. Apply the feedback. Repeat until the critique finds nothing material.
```

## 🏁 Implementation Steps
1. Generate an initial draft
2. Generate specific self-feedback
3. Refine using the feedback
4. Stop when feedback is trivial or N rounds reached

## 🛑 Stopping Condition (Verification)
**Verification Check**: Convergence
- *Detail*: Self-critique yields no material improvements.

## 💡 Why it works
Iterative self-feedback improves outputs with no extra training or external critic.

## ⚠️ Implementation Note
* Curated real-world loop with original source attribution.

## 🏷️ Keywords
self-refine, iterative, self-feedback

## 💬 Reviews & Feedback
- *No reviews yet.*
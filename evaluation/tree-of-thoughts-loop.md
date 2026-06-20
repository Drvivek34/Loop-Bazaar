# Tree-of-Thoughts deliberate search loop

**Loop ID**: #5063 | **Category**: Evaluation | **Author**: Yao et al. (2023) | **Rating**: ⭐ 4.6/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
Explore multiple reasoning branches, evaluate them, and expand the most promising — a search loop over thoughts.

## 🎯 Use Case (When to Use)
> When a problem benefits from exploring and pruning alternative approaches.

## ⚡ System Prompt / Instructions
```
Generate several candidate next-steps (thoughts), evaluate each, keep the best, and expand — backtracking when a branch dead-ends.
```

## 🏁 Implementation Steps
1. Generate multiple candidate thoughts
2. Evaluate/score each branch
3. Expand the most promising
4. Backtrack on dead ends until solved

## 🛑 Stopping Condition (Verification)
**Verification Check**: Goal reached
- *Detail*: A branch satisfies the success criterion.

## 💡 Why it works
Deliberate search over thoughts beats single-shot chains on hard reasoning.

## ⚠️ Implementation Note
* Curated real-world loop with original source attribution.

## 🏷️ Keywords
tree of thoughts, search, reasoning

## 💬 Reviews & Feedback
- *No reviews yet.*
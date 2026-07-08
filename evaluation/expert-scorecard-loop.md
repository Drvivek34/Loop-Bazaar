# The expert scorecard loop

**Loop ID**: #075 | **Category**: Evaluation | **Author**: herath | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A quality-improvement workflow that defines expert scoring dimensions, fixes the lowest score, and requires fresh independent rescoring after every pass.

## 🎯 Use Case (When to Use)
> Use this when an artifact needs expert-quality polish and subjective judgment must be tied to repeatable criteria and independent review.

## ⚡ System Prompt / Instructions
```
Bring one artifact to a verified 5 out of 5 on every dimension of an expert scorecard. Name the governing expert perspective and define five to nine scored dimensions, wiring objective checks such as tests, lint, build, accessibility, performance, or security scans to any dimensions they cover. Fix only the lowest-scoring dimension each pass. Then have a fresh independent reviewer rescore the whole artifact and name what remains below 5. Never score your own work, fake a 5, pad dimensions, or weaken checks. Stop when every dimension is 5, the lowest score has not risen for two rounds, the budget is spent, blocked, or approval is required.
```

## 🏁 Implementation Steps
1. Name the expert perspective and define five to nine scored dimensions before editing.
2. Attach objective checks to the dimensions they can prove, so a red check blocks a perfect score.
3. Improve the lowest-scoring dimension with one bounded change.
4. Use a fresh independent reviewer to rescore the entire artifact after each pass.
5. Stop at all 5s, stagnation, exhausted budget, blocker, or approval boundary.

## 🛑 Stopping Condition (Verification)
**Verification Check**: A fresh reviewer scorecard and objective checks support every 5 out of 5.
- *Detail*: The final receipt includes the expert perspective, dimensions, objective check results, per-round scores, lowest-score actions, reviewer findings, terminal state, and any remaining below-5 dimensions.

## 💡 Why it works
A single score can hide weak dimensions; forcing the lowest score to move and using a fresh reviewer reduces self-approval and cosmetic progress.

## ⚠️ Implementation Note
* Use dimensions that can actually fall below perfect. Do not relax the bar, weaken objective checks, or let the maker be the final scorer.

## 🏷️ Keywords
expert scorecard, quality rubric, independent review, artifact polish, 5 out of 5

## 💬 Reviews & Feedback
- *No reviews yet.*
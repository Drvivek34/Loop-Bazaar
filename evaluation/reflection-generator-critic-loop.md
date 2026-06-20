# Generator–Critic reflection loop

**Loop ID**: #5061 | **Category**: Evaluation | **Author**: Andrew Ng (DeepLearning.AI) | **Rating**: ⭐ 4.7/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
Pair a generator with a separate critic agent that reviews and sends feedback until quality is met.

## 🎯 Use Case (When to Use)
> When a dedicated critic improves output more than self-critique.

## ⚡ System Prompt / Instructions
```
Generator produces output; Critic reviews against criteria and returns feedback; Generator revises. Repeat until the Critic approves.
```

## 🏁 Implementation Steps
1. Generator drafts output
2. Critic reviews against explicit criteria
3. Generator revises on feedback
4. Stop when Critic approves

## 🛑 Stopping Condition (Verification)
**Verification Check**: Critic approval
- *Detail*: Independent critic signs off on the output.

## 💡 Why it works
Separating roles yields sharper feedback than a single self-evaluating agent.

## ⚠️ Implementation Note
* Curated real-world loop with original source attribution.

## 🏷️ Keywords
reflection, generator critic, evaluation

## 💬 Reviews & Feedback
- *No reviews yet.*
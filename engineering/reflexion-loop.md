# The Reflexion loop

**Loop ID**: #5053 | **Category**: Engineering | **Author**: Shinn et al. (2023) | **Rating**: ⭐ 4.8/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
Generate an attempt, verbally reflect on what went wrong, store the reflection, and retry with that memory.

## 🎯 Use Case (When to Use)
> When an agent fails tasks it could solve with self-critique and memory.

## ⚡ System Prompt / Instructions
```
Attempt the task. If it fails verification, write a short reflection on the cause, then retry using that reflection as added context.
```

## 🏁 Implementation Steps
1. Attempt the task
2. Evaluate against a success signal
3. Write a verbal self-reflection on failures
4. Retry with reflections in memory until success or max tries

## 🛑 Stopping Condition (Verification)
**Verification Check**: Self-evaluation
- *Detail*: Critic/test signal passes, or max reflection rounds reached.

## 💡 Why it works
Verbal reinforcement lets the agent learn within a session without weight updates.

## ⚠️ Implementation Note
* Curated real-world loop with original source attribution.

## 🏷️ Keywords
reflexion, self-reflection, memory, verbal RL

## 💬 Reviews & Feedback
- *No reviews yet.*
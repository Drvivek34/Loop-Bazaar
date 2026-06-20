# Fresh-context loop engineering

**Loop ID**: #5064 | **Category**: Operations | **Author**: Data Science Dojo | **Rating**: ⭐ 4.5/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
Structure long-running agent loops to reset/compact context each cycle so quality doesn't decay over a long run.

## 🎯 Use Case (When to Use)
> When agents degrade over long autonomous runs as context fills.

## ⚡ System Prompt / Instructions
```
Each cycle, persist progress to durable state, start from a compact fresh context built from that state, and continue the task.
```

## 🏁 Implementation Steps
1. Persist progress to durable state (files/notes)
2. Start each cycle with a fresh, compacted context
3. Reload only what's needed from state
4. Repeat until the task completes

## 🛑 Stopping Condition (Verification)
**Verification Check**: State convergence
- *Detail*: Durable state shows the task complete.

## 💡 Why it works
Externalizing memory + fresh context keeps long loops at high quality.

## ⚠️ Implementation Note
* Curated real-world loop with original source attribution.

## 🏷️ Keywords
loop engineering, context, long running, state

## 💬 Reviews & Feedback
- *No reviews yet.*
# Autonomous loop with intelligent exit detection

**Loop ID**: #5059 | **Category**: Engineering | **Author**: Frank Bria (@frankbria) | **Rating**: ⭐ 4.5/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A Ralph-style Claude Code loop with safeguards that detect completion/stagnation to avoid infinite runs and API waste.

## 🎯 Use Case (When to Use)
> When running long autonomous loops that must stop themselves safely.

## ⚡ System Prompt / Instructions
```
Loop the agent on the task, but after each pass evaluate progress; exit when complete, stalled, or a budget is hit.
```

## 🏁 Implementation Steps
1. Run the agent pass
2. Measure progress vs last pass
3. Detect completion or stagnation
4. Exit on done / no-progress / budget cap

## 🛑 Stopping Condition (Verification)
**Verification Check**: Exit detection
- *Detail*: Loop halts on completion, stagnation, or budget.

## 💡 Why it works
Explicit exit detection prevents runaway loops and runaway cost.

## ⚠️ Implementation Note
* Curated real-world loop with original source attribution.

## 🏷️ Keywords
exit detection, safeguards, budget, ralph

## 💬 Reviews & Feedback
- *No reviews yet.*
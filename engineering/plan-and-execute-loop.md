# The Plan-and-Execute loop

**Loop ID**: #5060 | **Category**: Engineering | **Author**: LangChain | **Rating**: ⭐ 4.6/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
Plan the whole strategy up front, then execute steps sequentially, re-planning only when needed.

## 🎯 Use Case (When to Use)
> When upfront planning beats step-by-step reasoning (multi-step, tool-heavy tasks).

## ⚡ System Prompt / Instructions
```
Draft a complete step-by-step plan. Execute each step. After execution, update the plan only if reality diverged.
```

## 🏁 Implementation Steps
1. Generate a full plan
2. Execute the next step
3. Check results against the plan
4. Re-plan only on divergence; finish when plan is done

## 🛑 Stopping Condition (Verification)
**Verification Check**: Plan completion
- *Detail*: All planned steps executed and validated.

## 💡 Why it works
Planning once reduces token churn and keeps long tasks coherent.

## ⚠️ Implementation Note
* Curated real-world loop with original source attribution.

## 🏷️ Keywords
plan-and-execute, planning, agents

## 💬 Reviews & Feedback
- *No reviews yet.*
# The Express.js Memory Leaks Sweeps Loop

**Loop ID**: #1411 | **Category**: Evaluation | **Author**: @Dis_Trackted | **Rating**: ⭐ 4.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that sweeps memory leaks in Express.js and stops when target threshold is reached.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify memory leaks in Express.js systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Express.js repository. Focus specifically on memory leaks. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: target threshold is reached.
```

## 🏁 Implementation Steps
1. Scan the Express.js codebase for active memory leaks.
2. Identify any deviations from the target standard: target threshold is reached.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Memory leaks meets target standards.
- *Detail*: Checked and confirmed that: target threshold is reached.

## 💡 Why it works
This loop works because it reduces regression risk by integrating tests directly into the loop.

## ⚠️ Implementation Note
* Keep the scope focused on memory leaks to minimize run costs.

## 🏷️ Keywords
express.js, evaluation, sweeps

## 💬 Reviews & Feedback
- **@richard_s** (★★★★☆ 4/5): *Successfully implemented this for Express.js. The verification step is extremely reliable.* (2026-02-12)
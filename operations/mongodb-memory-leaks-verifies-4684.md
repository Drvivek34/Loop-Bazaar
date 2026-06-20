# The MongoDB Memory Leaks Verifies Loop

**Loop ID**: #4684 | **Category**: Operations | **Author**: @sophia_w | **Rating**: ⭐ 4.9/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that verifies memory leaks in MongoDB and stops when stale state is fully cleared.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify memory leaks in MongoDB systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the MongoDB repository. Focus specifically on memory leaks. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: stale state is fully cleared.
```

## 🏁 Implementation Steps
1. Scan the MongoDB codebase for active memory leaks.
2. Identify any deviations from the target standard: stale state is fully cleared.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Memory leaks meets target standards.
- *Detail*: Checked and confirmed that: stale state is fully cleared.

## 💡 Why it works
This loop works because it automates routine maintenance task and flags exceptions for review.

## ⚠️ Implementation Note
* Keep the scope focused on memory leaks to minimize run costs.

## 🏷️ Keywords
mongodb, operations, verifies

## 💬 Reviews & Feedback
- **@ranvier2d2** (★★★★☆ 4/5): *Successfully implemented this for MongoDB. The verification step is extremely reliable.* (2026-03-16)
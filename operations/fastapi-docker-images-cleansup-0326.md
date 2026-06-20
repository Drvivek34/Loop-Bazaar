# The FastAPI Docker Images Cleans up Loop

**Loop ID**: #0326 | **Category**: Operations | **Author**: @0xUmbra | **Rating**: ⭐ 4.4/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that cleans up Docker images in FastAPI and stops when target threshold is reached.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify Docker images in FastAPI systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the FastAPI repository. Focus specifically on Docker images. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: target threshold is reached.
```

## 🏁 Implementation Steps
1. Scan the FastAPI codebase for active Docker images.
2. Identify any deviations from the target standard: target threshold is reached.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Docker images meets target standards.
- *Detail*: Checked and confirmed that: target threshold is reached.

## 💡 Why it works
This loop works because it automates routine maintenance task and flags exceptions for review.

## ⚠️ Implementation Note
* Keep the scope focused on Docker images to minimize run costs.

## 🏷️ Keywords
fastapi, operations, cleans up

## 💬 Reviews & Feedback
- **@swayam** (★★★★☆ 4/5): *Successfully implemented this for FastAPI. The verification step is extremely reliable.* (2026-06-19)
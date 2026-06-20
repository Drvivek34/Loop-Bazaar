# The Flask Docker Images Sweeps Loop

**Loop ID**: #4292 | **Category**: Content | **Author**: @agent0ai | **Rating**: ⭐ 4.6/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that sweeps Docker images in Flask and stops when stale state is fully cleared.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify Docker images in Flask systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Flask repository. Focus specifically on Docker images. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: stale state is fully cleared.
```

## 🏁 Implementation Steps
1. Scan the Flask codebase for active Docker images.
2. Identify any deviations from the target standard: stale state is fully cleared.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Docker images meets target standards.
- *Detail*: Checked and confirmed that: stale state is fully cleared.

## 💡 Why it works
This loop works because it creates a clear evidence trail of system changes and performance checks.

## ⚠️ Implementation Note
* Keep the scope focused on Docker images to minimize run costs.

## 🏷️ Keywords
flask, content, sweeps

## 💬 Reviews & Feedback
- **@elena_r** (★★★★☆ 4/5): *Successfully implemented this for Flask. The verification step is extremely reliable.* (2026-02-01)
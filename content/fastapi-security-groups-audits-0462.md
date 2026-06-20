# The FastAPI Security Groups Audits Loop

**Loop ID**: #0462 | **Category**: Content | **Author**: @linus_t | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that audits security groups in FastAPI and stops when compliance report returns zero warnings.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify security groups in FastAPI systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the FastAPI repository. Focus specifically on security groups. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: compliance report returns zero warnings.
```

## 🏁 Implementation Steps
1. Scan the FastAPI codebase for active security groups.
2. Identify any deviations from the target standard: compliance report returns zero warnings.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Security groups meets target standards.
- *Detail*: Checked and confirmed that: compliance report returns zero warnings.

## 💡 Why it works
This loop works because it prevents manual checklist drift and guarantees repeatable quality.

## ⚠️ Implementation Note
* Keep the scope focused on security groups to minimize run costs.

## 🏷️ Keywords
fastapi, content, audits

## 💬 Reviews & Feedback
- **@alan_turing** (★★★★★ 5/5): *Successfully implemented this for FastAPI. The verification step is extremely reliable.* (2026-05-18)
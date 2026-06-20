# The PostgreSQL Data Backup Logs Debugs Loop

**Loop ID**: #3118 | **Category**: Evaluation | **Author**: @inferencegod | **Rating**: ⭐ 4.9/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that debugs data backup logs in PostgreSQL and stops when all vulnerabilities are resolved.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify data backup logs in PostgreSQL systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the PostgreSQL repository. Focus specifically on data backup logs. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: all vulnerabilities are resolved.
```

## 🏁 Implementation Steps
1. Scan the PostgreSQL codebase for active data backup logs.
2. Identify any deviations from the target standard: all vulnerabilities are resolved.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Data backup logs meets target standards.
- *Detail*: Checked and confirmed that: all vulnerabilities are resolved.

## 💡 Why it works
This loop works because it prevents manual checklist drift and guarantees repeatable quality.

## ⚠️ Implementation Note
* Keep the scope focused on data backup logs to minimize run costs.

## 🏷️ Keywords
postgresql, evaluation, debugs

## 💬 Reviews & Feedback
- **@ranvier2d2** (★★★★☆ 4/5): *Successfully implemented this for PostgreSQL. The verification step is extremely reliable.* (2026-02-06)
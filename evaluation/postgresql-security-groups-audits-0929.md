# The PostgreSQL Security Groups Audits Loop

**Loop ID**: #0929 | **Category**: Evaluation | **Author**: @brendan_e | **Rating**: ⭐ 4.4/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that audits security groups in PostgreSQL and stops when all checks pass successfully.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify security groups in PostgreSQL systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the PostgreSQL repository. Focus specifically on security groups. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: all checks pass successfully.
```

## 🏁 Implementation Steps
1. Scan the PostgreSQL codebase for active security groups.
2. Identify any deviations from the target standard: all checks pass successfully.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Security groups meets target standards.
- *Detail*: Checked and confirmed that: all checks pass successfully.

## 💡 Why it works
This loop works because it reduces regression risk by integrating tests directly into the loop.

## ⚠️ Implementation Note
* Keep the scope focused on security groups to minimize run costs.

## 🏷️ Keywords
postgresql, evaluation, audits

## 💬 Reviews & Feedback
- **@brendan_e** (★★★★☆ 4/5): *Successfully implemented this for PostgreSQL. The verification step is extremely reliable.* (2026-06-17)
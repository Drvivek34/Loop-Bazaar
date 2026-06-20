# The Vue Security Groups Triages Loop

**Loop ID**: #0804 | **Category**: Evaluation | **Author**: @richard_s | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that triages security groups in Vue and stops when no duplicate imports remain.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify security groups in Vue systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Vue repository. Focus specifically on security groups. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: no duplicate imports remain.
```

## 🏁 Implementation Steps
1. Scan the Vue codebase for active security groups.
2. Identify any deviations from the target standard: no duplicate imports remain.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Security groups meets target standards.
- *Detail*: Checked and confirmed that: no duplicate imports remain.

## 💡 Why it works
This loop works because it prevents manual checklist drift and guarantees repeatable quality.

## ⚠️ Implementation Note
* Keep the scope focused on security groups to minimize run costs.

## 🏷️ Keywords
vue, evaluation, triages

## 💬 Reviews & Feedback
- **@0xUmbra** (★★★★★ 5/5): *Successfully implemented this for Vue. The verification step is extremely reliable.* (2026-01-30)
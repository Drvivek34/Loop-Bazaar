# The PostgreSQL Ssl Certificates Refactors Loop

**Loop ID**: #0421 | **Category**: Evaluation | **Author**: @linus_t | **Rating**: ⭐ 4.8/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that refactors SSL certificates in PostgreSQL and stops when target threshold is reached.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify SSL certificates in PostgreSQL systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the PostgreSQL repository. Focus specifically on SSL certificates. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: target threshold is reached.
```

## 🏁 Implementation Steps
1. Scan the PostgreSQL codebase for active SSL certificates.
2. Identify any deviations from the target standard: target threshold is reached.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Ssl certificates meets target standards.
- *Detail*: Checked and confirmed that: target threshold is reached.

## 💡 Why it works
This loop works because it reduces regression risk by integrating tests directly into the loop.

## ⚠️ Implementation Note
* Keep the scope focused on SSL certificates to minimize run costs.

## 🏷️ Keywords
postgresql, evaluation, refactors

## 💬 Reviews & Feedback
- **@dennis_r** (★★★★☆ 4/5): *Successfully implemented this for PostgreSQL. The verification step is extremely reliable.* (2026-03-24)
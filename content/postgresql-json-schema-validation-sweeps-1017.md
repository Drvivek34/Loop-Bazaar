# The PostgreSQL Json Schema Validation Sweeps Loop

**Loop ID**: #1017 | **Category**: Content | **Author**: @ken_t | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that sweeps JSON schema validation in PostgreSQL and stops when API response time is under 100ms.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify JSON schema validation in PostgreSQL systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the PostgreSQL repository. Focus specifically on JSON schema validation. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: API response time is under 100ms.
```

## 🏁 Implementation Steps
1. Scan the PostgreSQL codebase for active JSON schema validation.
2. Identify any deviations from the target standard: API response time is under 100ms.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Json schema validation meets target standards.
- *Detail*: Checked and confirmed that: API response time is under 100ms.

## 💡 Why it works
This loop works because it forces systematic optimization instead of relying on developer memory.

## ⚠️ Implementation Note
* Keep the scope focused on JSON schema validation to minimize run costs.

## 🏷️ Keywords
postgresql, content, sweeps

## 💬 Reviews & Feedback
- **@donald_k** (★★★★★ 5/5): *Successfully implemented this for PostgreSQL. The verification step is extremely reliable.* (2026-03-16)
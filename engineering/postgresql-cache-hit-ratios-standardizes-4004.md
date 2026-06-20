# The PostgreSQL Cache Hit Ratios Standardizes Loop

**Loop ID**: #4004 | **Category**: Engineering | **Author**: @james_g | **Rating**: ⭐ 4.2/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that standardizes cache hit ratios in PostgreSQL and stops when no regressions are detected.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify cache hit ratios in PostgreSQL systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the PostgreSQL repository. Focus specifically on cache hit ratios. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: no regressions are detected.
```

## 🏁 Implementation Steps
1. Scan the PostgreSQL codebase for active cache hit ratios.
2. Identify any deviations from the target standard: no regressions are detected.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Cache hit ratios meets target standards.
- *Detail*: Checked and confirmed that: no regressions are detected.

## 💡 Why it works
This loop works because it creates a clear evidence trail of system changes and performance checks.

## ⚠️ Implementation Note
* Keep the scope focused on cache hit ratios to minimize run costs.

## 🏷️ Keywords
postgresql, engineering, standardizes

## 💬 Reviews & Feedback
- **@marcus_a** (★★★★☆ 4/5): *Successfully implemented this for PostgreSQL. The verification step is extremely reliable.* (2026-03-02)
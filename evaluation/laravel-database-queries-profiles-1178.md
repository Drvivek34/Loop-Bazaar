# The Laravel Database Queries Profiles Loop

**Loop ID**: #1178 | **Category**: Evaluation | **Author**: @lucas_k | **Rating**: ⭐ 4.3/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that profiles database queries in Laravel and stops when test coverage reaches 100%.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify database queries in Laravel systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Laravel repository. Focus specifically on database queries. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: test coverage reaches 100%.
```

## 🏁 Implementation Steps
1. Scan the Laravel codebase for active database queries.
2. Identify any deviations from the target standard: test coverage reaches 100%.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Database queries meets target standards.
- *Detail*: Checked and confirmed that: test coverage reaches 100%.

## 💡 Why it works
This loop works because it creates a clear evidence trail of system changes and performance checks.

## ⚠️ Implementation Note
* Keep the scope focused on database queries to minimize run costs.

## 🏷️ Keywords
laravel, evaluation, profiles

## 💬 Reviews & Feedback
- **@linus_t** (★★★★☆ 4/5): *Successfully implemented this for Laravel. The verification step is extremely reliable.* (2026-03-01)
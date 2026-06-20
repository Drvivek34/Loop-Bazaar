# The Express.js Database Queries Cleans up Loop

**Loop ID**: #4611 | **Category**: Evaluation | **Author**: @tim_berners | **Rating**: ⭐ 4.6/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that cleans up database queries in Express.js and stops when error rate drops below 0.1%.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify database queries in Express.js systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Express.js repository. Focus specifically on database queries. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: error rate drops below 0.1%.
```

## 🏁 Implementation Steps
1. Scan the Express.js codebase for active database queries.
2. Identify any deviations from the target standard: error rate drops below 0.1%.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Database queries meets target standards.
- *Detail*: Checked and confirmed that: error rate drops below 0.1%.

## 💡 Why it works
This loop works because it automates routine maintenance task and flags exceptions for review.

## ⚠️ Implementation Note
* Keep the scope focused on database queries to minimize run costs.

## 🏷️ Keywords
express.js, evaluation, cleans up

## 💬 Reviews & Feedback
- **@matthewberman** (★★★★☆ 4/5): *Successfully implemented this for Express.js. The verification step is extremely reliable.* (2026-01-19)
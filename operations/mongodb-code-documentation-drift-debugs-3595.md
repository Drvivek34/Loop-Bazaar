# The MongoDB Code Documentation Drift Debugs Loop

**Loop ID**: #3595 | **Category**: Operations | **Author**: @elena_r | **Rating**: ⭐ 4.1/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that debugs code documentation drift in MongoDB and stops when compliance report returns zero warnings.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify code documentation drift in MongoDB systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the MongoDB repository. Focus specifically on code documentation drift. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: compliance report returns zero warnings.
```

## 🏁 Implementation Steps
1. Scan the MongoDB codebase for active code documentation drift.
2. Identify any deviations from the target standard: compliance report returns zero warnings.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Code documentation drift meets target standards.
- *Detail*: Checked and confirmed that: compliance report returns zero warnings.

## 💡 Why it works
This loop works because it prevents manual checklist drift and guarantees repeatable quality.

## ⚠️ Implementation Note
* Keep the scope focused on code documentation drift to minimize run costs.

## 🏷️ Keywords
mongodb, operations, debugs

## 💬 Reviews & Feedback
- **@vivek34** (★★★★☆ 4/5): *Successfully implemented this for MongoDB. The verification step is extremely reliable.* (2026-03-29)
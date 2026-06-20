# The MongoDB Api Rate Limits Validates Loop

**Loop ID**: #4578 | **Category**: Evaluation | **Author**: @ranvier2d2 | **Rating**: ⭐ 4.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that validates API rate limits in MongoDB and stops when all vulnerabilities are resolved.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify API rate limits in MongoDB systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the MongoDB repository. Focus specifically on API rate limits. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: all vulnerabilities are resolved.
```

## 🏁 Implementation Steps
1. Scan the MongoDB codebase for active API rate limits.
2. Identify any deviations from the target standard: all vulnerabilities are resolved.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Api rate limits meets target standards.
- *Detail*: Checked and confirmed that: all vulnerabilities are resolved.

## 💡 Why it works
This loop works because it reduces regression risk by integrating tests directly into the loop.

## ⚠️ Implementation Note
* Keep the scope focused on API rate limits to minimize run costs.

## 🏷️ Keywords
mongodb, evaluation, validates

## 💬 Reviews & Feedback
- **@grace_hopper** (★★★★☆ 4/5): *Successfully implemented this for MongoDB. The verification step is extremely reliable.* (2026-02-28)
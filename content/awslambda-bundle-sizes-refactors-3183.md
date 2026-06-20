# The AWS Lambda Bundle Sizes Refactors Loop

**Loop ID**: #3183 | **Category**: Content | **Author**: @lucas_k | **Rating**: ⭐ 4.3/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that refactors bundle sizes in AWS Lambda and stops when error rate drops below 0.1%.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify bundle sizes in AWS Lambda systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the AWS Lambda repository. Focus specifically on bundle sizes. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: error rate drops below 0.1%.
```

## 🏁 Implementation Steps
1. Scan the AWS Lambda codebase for active bundle sizes.
2. Identify any deviations from the target standard: error rate drops below 0.1%.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Bundle sizes meets target standards.
- *Detail*: Checked and confirmed that: error rate drops below 0.1%.

## 💡 Why it works
This loop works because it ensures security policies are consistently enforced without gaps.

## ⚠️ Implementation Note
* Keep the scope focused on bundle sizes to minimize run costs.

## 🏷️ Keywords
aws lambda, content, refactors

## 💬 Reviews & Feedback
- **@ken_t** (★★★★☆ 4/5): *Successfully implemented this for AWS Lambda. The verification step is extremely reliable.* (2026-05-19)
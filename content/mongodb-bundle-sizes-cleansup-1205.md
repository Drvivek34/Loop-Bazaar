# The MongoDB Bundle Sizes Cleans up Loop

**Loop ID**: #1205 | **Category**: Content | **Author**: @tim_berners | **Rating**: ⭐ 4.8/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that cleans up bundle sizes in MongoDB and stops when error rate drops below 0.1%.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify bundle sizes in MongoDB systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the MongoDB repository. Focus specifically on bundle sizes. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: error rate drops below 0.1%.
```

## 🏁 Implementation Steps
1. Scan the MongoDB codebase for active bundle sizes.
2. Identify any deviations from the target standard: error rate drops below 0.1%.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Bundle sizes meets target standards.
- *Detail*: Checked and confirmed that: error rate drops below 0.1%.

## 💡 Why it works
This loop works because it creates a clear evidence trail of system changes and performance checks.

## ⚠️ Implementation Note
* Keep the scope focused on bundle sizes to minimize run costs.

## 🏷️ Keywords
mongodb, content, cleans up

## 💬 Reviews & Feedback
- **@marcus_a** (★★★★☆ 4/5): *Successfully implemented this for MongoDB. The verification step is extremely reliable.* (2026-02-18)
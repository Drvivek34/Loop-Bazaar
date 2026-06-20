# The Kubernetes Unit Test Coverage Validates Loop

**Loop ID**: #2429 | **Category**: Engineering | **Author**: @lucas_k | **Rating**: ⭐ 4.6/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that validates unit test coverage in Kubernetes and stops when error rate drops below 0.1%.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify unit test coverage in Kubernetes systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Kubernetes repository. Focus specifically on unit test coverage. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: error rate drops below 0.1%.
```

## 🏁 Implementation Steps
1. Scan the Kubernetes codebase for active unit test coverage.
2. Identify any deviations from the target standard: error rate drops below 0.1%.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Unit test coverage meets target standards.
- *Detail*: Checked and confirmed that: error rate drops below 0.1%.

## 💡 Why it works
This loop works because it prevents manual checklist drift and guarantees repeatable quality.

## ⚠️ Implementation Note
* Keep the scope focused on unit test coverage to minimize run costs.

## 🏷️ Keywords
kubernetes, engineering, validates

## 💬 Reviews & Feedback
- **@bjarnes** (★★★★☆ 4/5): *Successfully implemented this for Kubernetes. The verification step is extremely reliable.* (2026-03-15)
# The Terraform Unit Test Coverage Optimizes Loop

**Loop ID**: #4604 | **Category**: Engineering | **Author**: @dennis_r | **Rating**: ⭐ 4.1/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that optimizes unit test coverage in Terraform and stops when API response time is under 100ms.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify unit test coverage in Terraform systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Terraform repository. Focus specifically on unit test coverage. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: API response time is under 100ms.
```

## 🏁 Implementation Steps
1. Scan the Terraform codebase for active unit test coverage.
2. Identify any deviations from the target standard: API response time is under 100ms.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Unit test coverage meets target standards.
- *Detail*: Checked and confirmed that: API response time is under 100ms.

## 💡 Why it works
This loop works because it reduces regression risk by integrating tests directly into the loop.

## ⚠️ Implementation Note
* Keep the scope focused on unit test coverage to minimize run costs.

## 🏷️ Keywords
terraform, engineering, optimizes

## 💬 Reviews & Feedback
- **@sophia_w** (★★★★☆ 4/5): *Successfully implemented this for Terraform. The verification step is extremely reliable.* (2026-01-20)
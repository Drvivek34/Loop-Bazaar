# The Terraform Api Endpoints Validates Loop

**Loop ID**: #4499 | **Category**: Engineering | **Author**: @marcus_a | **Rating**: ⭐ 4.8/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that validates API endpoints in Terraform and stops when no regressions are detected.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify API endpoints in Terraform systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Terraform repository. Focus specifically on API endpoints. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: no regressions are detected.
```

## 🏁 Implementation Steps
1. Scan the Terraform codebase for active API endpoints.
2. Identify any deviations from the target standard: no regressions are detected.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Api endpoints meets target standards.
- *Detail*: Checked and confirmed that: no regressions are detected.

## 💡 Why it works
This loop works because it creates a clear evidence trail of system changes and performance checks.

## ⚠️ Implementation Note
* Keep the scope focused on API endpoints to minimize run costs.

## 🏷️ Keywords
terraform, engineering, validates

## 💬 Reviews & Feedback
- **@steipete** (★★★★☆ 4/5): *Successfully implemented this for Terraform. The verification step is extremely reliable.* (2026-02-25)
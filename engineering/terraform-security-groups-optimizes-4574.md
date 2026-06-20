# The Terraform Security Groups Optimizes Loop

**Loop ID**: #4574 | **Category**: Engineering | **Author**: @0xUmbra | **Rating**: ⭐ 4.2/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that optimizes security groups in Terraform and stops when error rate drops below 0.1%.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify security groups in Terraform systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Terraform repository. Focus specifically on security groups. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: error rate drops below 0.1%.
```

## 🏁 Implementation Steps
1. Scan the Terraform codebase for active security groups.
2. Identify any deviations from the target standard: error rate drops below 0.1%.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Security groups meets target standards.
- *Detail*: Checked and confirmed that: error rate drops below 0.1%.

## 💡 Why it works
This loop works because it reduces regression risk by integrating tests directly into the loop.

## ⚠️ Implementation Note
* Keep the scope focused on security groups to minimize run costs.

## 🏷️ Keywords
terraform, engineering, optimizes

## 💬 Reviews & Feedback
- **@james_g** (★★★★☆ 4/5): *Successfully implemented this for Terraform. The verification step is extremely reliable.* (2026-04-26)
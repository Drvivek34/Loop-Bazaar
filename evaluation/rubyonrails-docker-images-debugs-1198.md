# The Ruby on Rails Docker Images Debugs Loop

**Loop ID**: #1198 | **Category**: Evaluation | **Author**: @sophia_w | **Rating**: ⭐ 4.3/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that debugs Docker images in Ruby on Rails and stops when all checks pass successfully.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify Docker images in Ruby on Rails systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Ruby on Rails repository. Focus specifically on Docker images. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: all checks pass successfully.
```

## 🏁 Implementation Steps
1. Scan the Ruby on Rails codebase for active Docker images.
2. Identify any deviations from the target standard: all checks pass successfully.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Docker images meets target standards.
- *Detail*: Checked and confirmed that: all checks pass successfully.

## 💡 Why it works
This loop works because it reduces regression risk by integrating tests directly into the loop.

## ⚠️ Implementation Note
* Keep the scope focused on Docker images to minimize run costs.

## 🏷️ Keywords
ruby on rails, evaluation, debugs

## 💬 Reviews & Feedback
- **@ken_t** (★★★★☆ 4/5): *Successfully implemented this for Ruby on Rails. The verification step is extremely reliable.* (2026-03-21)
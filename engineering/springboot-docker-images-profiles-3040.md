# The Spring Boot Docker Images Profiles Loop

**Loop ID**: #3040 | **Category**: Engineering | **Author**: @steipete | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that profiles Docker images in Spring Boot and stops when API response time is under 100ms.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify Docker images in Spring Boot systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Spring Boot repository. Focus specifically on Docker images. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: API response time is under 100ms.
```

## 🏁 Implementation Steps
1. Scan the Spring Boot codebase for active Docker images.
2. Identify any deviations from the target standard: API response time is under 100ms.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Docker images meets target standards.
- *Detail*: Checked and confirmed that: API response time is under 100ms.

## 💡 Why it works
This loop works because it prevents manual checklist drift and guarantees repeatable quality.

## ⚠️ Implementation Note
* Keep the scope focused on Docker images to minimize run costs.

## 🏷️ Keywords
spring boot, engineering, profiles

## 💬 Reviews & Feedback
- **@brendan_e** (★★★★★ 5/5): *Successfully implemented this for Spring Boot. The verification step is extremely reliable.* (2026-04-25)
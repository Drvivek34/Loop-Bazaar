# The Groundtruth loop

**Loop ID**: #048 | **Category**: Engineering | **Author**: Mohamed (@aivibecode) | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A read-only project-audit workflow that verifies architecture, security, platform behavior, operations, and business logic from current evidence rather than assumptions.

## 🎯 Use Case (When to Use)
> Use this before trusting a project's security, correctness, platform compatibility, privileged surfaces, scheduled work, or operational assumptions and when the first task is audit rather than repair.

## ⚡ System Prompt / Instructions
```
Audit [project] from its actual code and configuration, not framework assumptions. For architecture, platform compatibility, security, privileged areas, performance, deployment, jobs, business logic, and code quality, record proved, no issue, weak, or N/A with direct evidence; verify external limits from current primary sources and calculate numbers. Ask before changing code. Stop when every area is logged with severity, or return unverified areas as blocked. Finish with a plain-language overview and area-to-evidence table.
```

## 🏁 Implementation Steps
1. Discover the real language, framework, hosting platform, privileged surfaces, scheduled jobs, and deployment configuration from the scoped project itself.
2. Inspect each required area, tie conclusions to code or configuration, verify platform and library behavior from current primary sources, and calculate rather than estimate quantitative claims.
3. Record an outcome, evidence, and severity for every area, separating confirmed weaknesses from no-issue findings, justified N/A results, and unverified gaps.
4. Deliver the plain-language project overview and area-to-evidence table without changing code; stop complete only when every area is accounted for, otherwise return the blocked gaps.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Every audit area has a current evidence-backed outcome and severity.
- *Detail*: The area-to-evidence table contains no silent gaps: each area is proved, no issue found, weak, N/A with a reason, or explicitly unverified and blocked.

## 💡 Why it works
Broad audits fail when they inherit framework defaults, rely on remembered limits, or omit quiet areas. A fixed evidence table forces the reviewer to prove, clear, exclude, or explicitly block every surface.

## ⚠️ Implementation Note
* This loop is read-only. Ask before changing code, configuration, infrastructure, or production state. Use current primary documentation for external behavior, avoid exposing secrets from privileged areas, and do not turn missing access into a clean finding.

## 🏷️ Keywords
Groundtruth audit, evidence based code review, project security audit, platform compatibility review, area to evidence table

## 💬 Reviews & Feedback
- *No reviews yet.*
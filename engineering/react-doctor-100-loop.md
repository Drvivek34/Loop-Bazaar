# The React Doctor 100/100 loop

**Loop ID**: #067 | **Category**: Engineering | **Author**: leviathofnoesia (@leviath666) | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
An AI coding-agent workflow for inventorying every production React app, fixing React Doctor findings without suppression, and proving a genuine 100/100 result with full project checks.

## 🎯 Use Case (When to Use)
> Use this for an authorized repository-wide React health pass when every production React app can be identified and a complete scan plus project checks can run locally.

## ⚡ System Prompt / Instructions
```
Bring every production React app in [repository] to a freshly verified React Doctor score of 100/100. Inventory app roots, record a full `npx react-doctor@latest --verbose` baseline, fix one root cause at a time, and rerun the full scan plus relevant typecheck, lint, tests, and builds. Never hide findings with exclusions, ignores, suppressions, deleted behavior, or relaxed rules. Stop at 100/100 for every app, blocked, approval-required, or no measurable progress; preserve unrelated work and report exact proof.
```

## 🏁 Implementation Steps
1. Inventory the repository, production React app roots, current worktree state, and available validation commands.
2. Run and record a full React Doctor baseline for every production app.
3. Group findings by root cause and repair one coherent cause without weakening rules or changing unrelated behavior.
4. Rerun the full scan and relevant typecheck, lint, tests, and builds, keeping only verified improvements.
5. Escalate from symptom patches to ownership or data-flow analysis when a finding survives repeated repairs.
6. Stop only at the success, blocked, approval-required, or no-progress state and return exact evidence.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Every production React app has a genuine fresh 100/100 result.
- *Detail*: Record the React Doctor version, app roots, full final scan, and repository validation results; distinguish pre-existing failures and blockers from regressions caused by the repair work.

## 💡 Why it works
A complete app inventory and fresh full scans prevent local or diff-only checks from masquerading as repository-wide health. Root-cause repair and anti-suppression rules make the final score evidence of better code rather than a configured-away problem.

## ⚠️ Implementation Note
* Do not reset or overwrite unrelated work, disable findings, exclude files, relax severity, add unsafe casts or ignore directives, or delete meaningful behavior. Ask before breaking dependency upgrades or architectural changes outside the stated scope.

## 🏷️ Keywords
React Doctor 100, React code health, repository audit, coding agent, React verification

## 💬 Reviews & Feedback
- *No reviews yet.*
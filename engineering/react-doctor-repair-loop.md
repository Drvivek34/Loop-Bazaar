# The React Doctor repair loop

**Loop ID**: #065 | **Category**: Engineering | **Author**: Will Undrell (@WillUndrll) | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
An AI coding-agent workflow for baselining React Doctor, repairing a small batch of real errors or warnings, and verifying that each retained change improves the scan without regressions.

## 🎯 Use Case (When to Use)
> Use this when a React codebase has actionable React Doctor errors or warnings and the safest repair strategy is to work in small, verified batches.

## ⚡ System Prompt / Instructions
```
Run `pnpm exec react-doctor . --verbose --yes --offline --fail-on none` to record the baseline, then rerun with `--fail-on error`. Fix at most five genuine findings, run the same scan and relevant project checks, and keep only verified improvements. Clear errors before high-confidence warnings. Stop when clean, blocked, approval is required, a finding is false-positive, or another pass makes no measurable progress. Finish with baseline and final results, retained fixes, reverted attempts, checks, and remaining findings.
```

## 🏁 Implementation Steps
1. Record the complete React Doctor baseline before editing.
2. Choose up to five genuine errors, trace their causes, and make the smallest coherent repairs.
3. Rerun the same scan and relevant repository checks, reverting changes that do not produce a verified improvement.
4. Repeat for remaining errors and then high-confidence warnings until a terminal state is reached.

## 🛑 Stopping Condition (Verification)
**Verification Check**: React Doctor improves without introducing regressions.
- *Detail*: Compare the baseline and final scan under the same command and confirm each retained change with the repository checks relevant to the files touched.

## 💡 Why it works
Small batches keep the causal link between a repair and the resulting scan clear. Repeating the same scan and repository checks prevents a cleaner diagnostic score from masking a product regression.

## ⚠️ Implementation Note
* Do not manufacture a clean result by disabling rules, excluding files, adding suppressions, or deleting meaningful behavior. Ask before dependency upgrades, destructive changes, or actions outside the repository.

## 🏷️ Keywords
React Doctor, React repair, coding agent, static analysis, verified refactoring

## 💬 Reviews & Feedback
- *No reviews yet.*
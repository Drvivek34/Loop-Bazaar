# The error-message rewrite loop

**Loop ID**: #053 | **Category**: Engineering | **Author**: Will Undrell (@WillUndrll) | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
An AI coding-agent workflow for inventorying user-visible errors, replacing internal or confusing text, and proving each reachable error state communicates clearly.

## 🎯 Use Case (When to Use)
> Use this when a product exposes raw, internal, inconsistent, or unhelpful error messages and the complete user-facing error surface needs a controlled rewrite.

## ⚡ System Prompt / Instructions
```
Find and improve every user-visible error message within [repository, product, or named scope]. If no scope is supplied, use the user-facing surfaces in the current repository and state any exclusions before editing. Inventory error strings in source code, surfaced API or client errors, and reachable browser states. Record each one in a CSV with its location, trigger, current copy, user risk, proposed replacement, implementation status, and verification result. Rank the errors by user harm. Rewrite one coherent group at a time using plain language and a useful recovery step when one exists. Do not expose provider names, stack traces, internal identifiers, or implementation details. After each change, run the relevant tests, exercise the affected state in a real browser when possible, and search again for raw or internal error text. Do not mark an unreachable state as verified. Stop when every row is verified or explicitly blocked. Finish with the CSV, changed files, test evidence, browser evidence, and blocked items.
```

## 🏁 Implementation Steps
1. Inventory source strings, surfaced API or client failures, and reachable browser error states in one CSV.
2. Rank errors by user harm and rewrite one coherent group with plain language and a useful recovery step.
3. Run relevant tests, exercise the affected states, and search again for internal or raw error text.
4. Repeat until every row is verified or explicitly blocked, then return the inventory and evidence.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Every in-scope user-facing error is clear and accounted for.
- *Detail*: The inventory contains no silently skipped row: each error is verified in its reachable state or marked blocked with the missing evidence.

## 💡 Why it works
Error copy is often scattered across source code and runtime paths, so isolated rewrites leave inconsistent states behind. A durable inventory makes the sweep complete and reviewable.

## ⚠️ Implementation Note
* Do not claim a clean sweep for states that could not be reached. Preserve technical detail in logs while keeping provider names, stack traces, identifiers, and implementation details out of user-facing copy.

## 🏷️ Keywords
error message rewrite, user facing errors, UX writing, browser error states, error inventory

## 💬 Reviews & Feedback
- *No reviews yet.*
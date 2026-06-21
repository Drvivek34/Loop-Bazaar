# The housekeeper loop

**Loop ID**: #041 | **Category**: Engineering | **Author**: Eric Lott | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A conservative code-project cleanup that proves one small opportunity is safe, makes the smallest useful change, and keeps it only after existing checks pass.

## 🎯 Use Case (When to Use)
> Use this when a code project has accumulated small maintenance problems—unused code, stale files, duplicated logic, broken links, old comments, inconsistent names, or confusing organization—but broad deletion would be risky.

## ⚡ System Prompt / Instructions
```
Review [repository or code project] for dead code, meaning unreachable or unused code; stale files or comments; unused dependencies; duplication; broken links; inconsistent names; and confusing structure. Protect unrelated, active, uncommitted, generated, and uncertain work. Prove one low-risk cleanup, make the smallest coherent change, then rerun the build, tests, runtime checks, and diff review. Keep only verified improvements. Stop when none remain, progress stalls, verification is unavailable, or approval is required. Return changes, evidence, and deferred candidates.
```

## 🏁 Implementation Steps
1. Inspect the current code-project state and identify active branches, uncommitted edits, generated files, configuration, and other work that must not be disturbed.
2. Collect possible cleanups, then use code references, configuration, documentation, tests, or runtime behavior to prove one candidate is genuinely low risk.
3. Make the smallest useful change and run the existing build, tests, application checks, and diff review; keep it only when behavior stays intact and no unrelated work changes.
4. Repeat until no confirmed low-risk cleanup remains, progress stalls, verification is unavailable, or the next candidate needs approval.

## 🛑 Stopping Condition (Verification)
**Verification Check**: No confirmed low-risk cleanup remains, and existing behavior still passes.
- *Detail*: Every retained cleanup is supported by direct evidence, relevant builds and tests pass, the application still runs where applicable, unrelated work is untouched, and uncertain candidates are deferred rather than deleted.

## 💡 Why it works
One proven cleanup at a time keeps the work easy to review and undo. Requiring evidence before deletion—and protecting uncertain files and edits—prevents a tidy-up pass from removing code that is active but poorly understood.

## ⚠️ Implementation Note
* Here, repository means the code project and its files. This loop cleans source and project structure; the separate repository cleanup loop handles Git branches, pull requests, commits, and worktrees. Never delete something merely because its purpose is not immediately obvious.

## 🏷️ Keywords
codebase housekeeping, dead code cleanup, unused dependency review, repository hygiene, incremental cleanup

## 💬 Reviews & Feedback
- *No reviews yet.*
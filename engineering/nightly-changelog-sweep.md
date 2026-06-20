# The nightly changelog loop

**Loop ID**: #008 | **Category**: Engineering | **Author**: Matthew Berman | **Rating**: ⭐ 4.2/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A scheduled coding-agent workflow that reviews the previous day's changes and keeps user-facing release history complete and current.

## 🎯 Use Case (When to Use)
> Use this when a project changes frequently enough that user-facing release notes can drift from merged pull requests, commits, deployments, and product changes.

## ⚡ System Prompt / Instructions
```
Each night, review changes from the previous day and update the changelog with anything users should know.
```

## 🏁 Implementation Steps
1. Collect the previous day's merged pull requests, commits, deployments, and other in-scope changes.
2. Identify which changes affect users and compare them with the current changelog.
3. Add concise dated entries with useful references while preserving existing content and avoiding duplicates.
4. Run the relevant checks and record either the validated update or the fact that no user-facing entry was needed.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Every user-relevant change from the previous day is accounted for.
- *Detail*: The changelog is updated and validated, or the no-change result is recorded.

## 💡 Why it works
A daily reconciliation makes omissions visible while the context is still fresh. Limiting entries to what users should know keeps the changelog useful instead of turning it into a raw commit feed.

## ⚠️ Implementation Note
* Use the underlying change and product behavior as the source of truth. Commit titles alone can overstate, understate, or misclassify what users experienced.

## 🏷️ Keywords
AI coding agent, nightly changelog, release notes workflow, changelog automation, daily repository review

## 💬 Reviews & Feedback
- **@vivek34** (★★★★☆ 4/5): *Highly recommended workflow, saves considerable manual sweep time.* (2026-06-19)
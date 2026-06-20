# The docs sweep

**Loop ID**: #001 | **Category**: Engineering | **Author**: Matthew Berman | **Rating**: ⭐ 4.8/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A reusable AI coding-agent workflow for comparing documentation with the current codebase, fixing drift, and opening a reviewable pull request.

## 🎯 Use Case (When to Use)
> Use this whenever implementation changes may have left READMEs, setup guides, API references, examples, or runbooks behind.

## ⚡ System Prompt / Instructions
```
Whenever a documentation pass is needed, review the codebase in full and make sure all documentation reflects the current implementation. Update stale documentation, verify the changes, then open a pull request.
```

## 🏁 Implementation Steps
1. Review implementation changes since the last documentation pass.
2. Compare the repository's documentation with the code, configuration, commands, and behavior that now ship.
3. Update only stale material, then verify commands, links, and examples against the current repository.
4. Run the relevant checks and open a pull request that explains the documentation drift and the fixes.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Documentation matches the current implementation.
- *Detail*: Finish with a reviewable pull request.

## 💡 Why it works
The loop ties documentation to the implementation instead of relying on memory. Requiring a pull request creates a visible diff, a review point, and a durable record of what changed.

## ⚠️ Implementation Note
* Keep the scope tied to real implementation changes. Do not rewrite accurate documentation just to create activity.

## 🏷️ Keywords
AI coding agent, documentation audit, documentation drift, documentation maintenance, pull request workflow

## 💬 Reviews & Feedback
- **@matthewberman** (★★★★★ 5/5): *Highly recommended workflow, saves considerable manual sweep time.* (2026-06-19)
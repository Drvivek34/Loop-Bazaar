# The repository cleanup loop

**Loop ID**: #012 | **Category**: Engineering | **Author**: Matthew Berman | **Rating**: ⭐ 4.2/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repository-hygiene workflow that audits branches, pull requests, commits, and worktrees, recovers valuable changes, and removes proven stale state.

## 🎯 Use Case (When to Use)
> Use this when abandoned branches, old worktrees, unclear pull requests, or unmerged commits make it difficult to know which repository state still matters.

## ⚡ System Prompt / Instructions
```
Inspect local and remote branches, pull requests, commits, and worktrees. Recover valuable work and clean everything stale until the repository is current and organized.
```

## 🏁 Implementation Steps
1. Inventory local and remote branches, open and recently closed pull requests, unmerged commits, and registered worktrees.
2. Classify each item as current, valuable but unfinished, superseded, merged, abandoned, or uncertain, recording evidence and ownership.
3. Recover valuable changes into an appropriate current branch before removing any stale reference.
4. Clean only proven stale state, fetch and prune safely, then rerun the inventory until every remaining item is intentional.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Valuable work is recovered and remaining repository state is intentional.
- *Detail*: Branches, pull requests, commits, and worktrees are current, owned, or safely removed with evidence.

## 💡 Why it works
Inventory and classification separate recoverable work from clutter before cleanup begins. Repeating the inventory proves the repository is organized instead of merely smaller.

## ⚠️ Implementation Note
* Do not delete uncertain work, discard uncommitted changes, or close someone else's pull request without confirmation. Preserve evidence for every destructive cleanup action.

## 🏷️ Keywords
AI coding agent, repository cleanup, git worktree audit, branch hygiene, pull request triage

## 💬 Reviews & Feedback
- **@dennis_r** (★★★★☆ 4/5): *Highly recommended workflow, saves considerable manual sweep time.* (2026-06-19)
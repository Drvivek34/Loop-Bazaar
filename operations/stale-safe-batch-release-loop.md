# The stale-safe batch release loop

**Loop ID**: #013 | **Category**: Operations | **Author**: Matthew Berman | **Rating**: ⭐ 4.8/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A release-coordination workflow that excludes stale or unfinished work, combines valid changes, and ships complete artifacts from the latest integrated main.

## 🎯 Use Case (When to Use)
> Use this when several branches or pull requests may be ready at once and the release must avoid stale worktrees, partial overlays, and incomplete changes.

## ⚡ System Prompt / Instructions
```
Review pending changes and pull requests, exclude stale or unfinished work, combine the valid changes, and release them together.
```

## 🏁 Implementation Steps
1. Fetch current repository and pull-request state, then inspect every candidate change for freshness, completeness, ownership, checks, and dependencies.
2. Exclude stale, superseded, conflicting, or unfinished work and record why each candidate was omitted.
3. Integrate the valid changes, rerun the combined checks, and select the newest main revision that contains the full batch.
4. Release complete artifacts from a clean checkout, serialize the deployment, and verify production before closing the batch.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Only current, complete changes ship in the combined release.
- *Detail*: The released revision is the latest integrated main that contains every selected change.

## 💡 Why it works
Evaluating all candidates before integration prevents stale code from entering a release through convenience or worktree confusion. Releasing from integrated main proves the deployed artifact matches the reviewed batch.

## ⚠️ Implementation Note
* The candidate diff selects what belongs in the batch, but deployment must use complete artifacts from the latest integrated main. Never deploy from a task worktree or partial file overlay.

## 🏷️ Keywords
AI release operations, batch release, stale code prevention, pull request coordination, deployment safety

## 💬 Reviews & Feedback
- **@Dis_Trackted** (★★★★★ 5/5): *Highly recommended workflow, saves considerable manual sweep time.* (2026-06-19)
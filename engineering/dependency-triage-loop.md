# The dependency triage loop

**Loop ID**: #064 | **Category**: Engineering | **Author**: Damian Galarza (@dgalarza) | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A safe Dependabot review loop that checks current diffs, release information, exact-head CI, and repository tests before repairing, merging, or escalating updates.

## 🎯 Use Case (When to Use)
> Use this when a repository has several open Dependabot pull requests and an authorized maintainer wants them reviewed safely without stale checks, parallel merge races, or automatic high-risk upgrades.

## ⚡ System Prompt / Instructions
```
Review every Dependabot pull request currently open in [repository]. Take a fixed snapshot of that set and process each pull request once. Read its diff, release notes, advisories, dependency role, current base revision, and exact-head CI results. Run the repository’s relevant tests in an isolated worktree and classify the update by version change, breaking behavior, security exposure, and regression risk. For failing checks, identify the root cause and prepare the smallest verified repair. Process merges serially: before each merge, refetch the base and pull-request head and require passing exact-head checks. Merge only low-risk patch or minor updates when explicit merge authority has already been granted. Request approval for major, breaking, security-sensitive, uncertain, or externally visible actions. Never push changes, merge, comment, or send messages without the corresponding authority. Stop successfully when the original snapshot is fully processed; stop without changes when none are open; stop as blocked when verification is unavailable. Finish with reviewed, repaired, merged, deferred, and blocked pull requests plus supporting evidence.
```

## 🏁 Implementation Steps
1. Snapshot the currently open Dependabot pull requests.
2. Inspect current diffs, release information, advisories, CI, and dependency role.
3. Run relevant tests in isolation and classify risk from evidence.
4. Repair failures or process authorized low-risk merges one at a time.
5. Refetch state before each merge and report every final status.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Every snapshotted dependency pull request reaches an evidence-backed status.
- *Detail*: Each pull request is merged, repaired, deferred for approval, or blocked with current diff, release, CI, and repository-test evidence; every merge uses a fresh base and exact head.

## 💡 Why it works
A fixed queue, isolated verification, and serialized fresh-state merges turn routine dependency updates into a bounded maintenance pass without granting unsafe blanket authority.

## ⚠️ Implementation Note
* This loop grants no merge, push, comment, or messaging authority by itself. Those actions require explicit authorization from the repository owner.

## 🏷️ Keywords
Dependabot triage, dependency pull requests, dependency update review, safe automated merge, dependency maintenance

## 💬 Reviews & Feedback
- *No reviews yet.*
# The Living Story loop

**Loop ID**: #047 | **Category**: Operations | **Author**: Buddy Hadry (@buddyhadry) | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A recurring context-maintenance workflow that turns repository activity, goals, and prior open threads into a verified daily story for future agents.

## 🎯 Use Case (When to Use)
> Use this when work spans several repositories or context sources and future agents need a recurring, evidence-based account of priorities, progress, deadlines, and unfinished work.

## ⚡ System Prompt / Instructions
```
On each [window], read the configured repositories, goals, prior STORY.md, and optional authorized sources. Update project files, then write STORY.md with focus, deadlines, open threads, and evidence-backed recent wins. Carry every prior thread forward, prove it finished, or mark it STALE/NEEDS-REVIEW—never silently drop one. Archive the snapshot and record the change. Stop when verification passes; if evidence or access is missing, return a thinner or blocked snapshot explicitly.
```

## 🏁 Implementation Steps
1. Read the configured repositories, goals, personal context, optional authorized sources, previous STORY.md, and existing project files; report missing inputs instead of inventing them.
2. Refresh each project record with current activity, branch state, shipped evidence, in-progress work, and stale status under the configured window.
3. Write the new story with interpretation, focus, deadlines, open threads, and evidence-backed recent wins rather than a raw commit list.
4. Reconcile every previous thread, archive the verified snapshot, update the changelog, and stop with an explicit complete, thinner, or blocked result.

## 🛑 Stopping Condition (Verification)
**Verification Check**: The current story accounts for every prior thread and supports every recent win with evidence.
- *Detail*: Each previous open thread is carried forward, closed with proof, or visibly flagged, and every claimed win cites a commit, release, closed task, deployment, sent deliverable, or generated artifact.

## 💡 Why it works
A recurring narrative preserves the meaning behind activity without letting old commitments disappear. Evidence requirements keep recent wins factual, while thread reconciliation makes stale or unfinished work visible to the next agent.

## ⚠️ Implementation Note
* Configure source paths and the stale window before relying on the story. Treat notes, calendars, task exports, and repository history as private; read only authorized sources and do not publish or transmit their contents without approval.

## 🏷️ Keywords
Living Story, agent context management, project status narrative, open thread tracking, evidence based progress

## 💬 Reviews & Feedback
- *No reviews yet.*
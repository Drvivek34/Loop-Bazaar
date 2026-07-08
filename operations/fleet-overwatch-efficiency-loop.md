# The fleet overwatch efficiency loop

**Loop ID**: #085 | **Category**: Operations | **Author**: Frosty40 (@frostforger) | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A fleet-operations workflow that classifies worker health, splits work into tracked chunks, reallocates based on throughput, and records utilization and results.

## 🎯 Use Case (When to Use)
> Use this when many authorized workers need continuous coordination across a large bounded search or batch-processing space.

## ⚡ System Prompt / Instructions
```
Operate only on authorized machines, approved ranges, and approved work types. Read current fleet state, classify each worker as idle, active, stalled, failed, slow, or high-performing, then split remaining work into tracked non-overlapping chunks. Allocate chunks based on worker speed, health, CPU, GPU, RAM, recent yield, and the agreed scout/prover/hunter/reserve mix. Run short probes, promote promising regions, kill bad leads, reload idle or failed workers, requeue unfinished work from dead or stalled workers, deduplicate candidates, and push strong candidates through the agreed proof chain. Stop when no approved work remains, utilization cannot improve safely, the cap is reached, or approval is required.
```

## 🏁 Implementation Steps
1. Read fleet state and classify worker health, capacity, speed, and recent yield.
2. Split the remaining approved work into tracked non-overlapping chunks.
3. Assign work based on worker health and the agreed scout/prover/hunter/reserve allocation.
4. Promote promising regions, kill bad leads, reload idle workers, and requeue work from failed or stalled workers.
5. Report utilization, throughput, candidates, proof status, and strategy shifts until no safe improvement remains.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Fleet utilization and completed work improve without duplicate or unauthorized work.
- *Detail*: The report includes worker classifications, chunk assignments, completed ranges, requeued work, failures, utilization, throughput, candidates, promoted leads, proof-chain status, strategy shifts, and stop reason.

## 💡 Why it works
Large worker fleets waste time when chunks overlap, failed workers hold work, or every machine receives the same strategy despite different yield.

## ⚠️ Implementation Note
* Do not use this for unauthorized systems, credential attacks, scraping beyond permission, or unapproved ranges. Keep all work boundaries explicit and auditable.

## 🏷️ Keywords
fleet orchestration, worker allocation, batch processing, parallel search, compute utilization

## 💬 Reviews & Feedback
- *No reviews yet.*
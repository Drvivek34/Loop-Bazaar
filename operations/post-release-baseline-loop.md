# The post-release baseline loop

**Loop ID**: #015 | **Category**: Operations | **Author**: Matthew Berman | **Rating**: ⭐ 4.8/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A triggered release workflow that runs standard benchmarks against the completed release and records a reproducible baseline for future comparisons.

## 🎯 Use Case (When to Use)
> Use this immediately after a release when future regressions or improvements need to be measured against the exact version now in production.

## ⚡ System Prompt / Instructions
```
After current releases finish, run the standard benchmarks and record the results as the new baseline.
```

## 🏁 Implementation Steps
1. Confirm every in-scope release is complete and record the production revision or artifact identity.
2. Run the standard benchmark suite under its documented environment, data, warm-up, and repetition rules.
3. Investigate invalid or unstable runs, then rerun only under the same documented conditions.
4. Store the final results with the release identity and benchmark metadata, and mark them as the new comparison baseline.

## 🛑 Stopping Condition (Verification)
**Verification Check**: The new baseline belongs to the completed release.
- *Detail*: Revision, environment, benchmark version, conditions, and results are recorded together.

## 💡 Why it works
Tying the baseline to a verified release creates a trustworthy reference point for later performance and quality work. Recording the conditions prevents unrelated environment changes from masquerading as product changes.

## ⚠️ Implementation Note
* Do not overwrite the previous baseline until the release identity and benchmark run are verified. Keep historical baselines available for trend analysis.

## 🏷️ Keywords
AI release operations, post-release benchmark, performance baseline, release verification, benchmark history

## 💬 Reviews & Feedback
- **@lucas_k** (★★★★★ 5/5): *Highly recommended workflow, saves considerable manual sweep time.* (2026-06-19)
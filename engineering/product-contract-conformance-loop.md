# The product contract conformance loop

**Loop ID**: #076 | **Category**: Engineering | **Author**: Charlie Greenman (@chargrnmn) | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A requirements-conformance workflow that turns a product contract into a ledger, checks current evidence, and repairs only confirmed mismatches with regression coverage.

## 🎯 Use Case (When to Use)
> Use this when a product contract, PRD, spec, or customer promise must be checked against the actual project before claims or implementation can be trusted.

## ⚡ System Prompt / Instructions
```
Audit the project against the supplied product contract. Extract every concrete product promise, business rule, permission rule, background job expectation, user workflow, non-goal, and quality bar into a requirement ledger. For each requirement, find current evidence in code, config, tests, docs, jobs, migrations, routes, UI, prompts, queues, or production-safe runtime state. Mark it proved, weak, contradicted, unimplemented, not applicable with reason, or blocked. Fix only confirmed high-impact mismatches one bounded slice at a time, preserving unrelated work and adding regression coverage where practical. Stop when every requirement is proved or honestly classified and the ledger has no silent gaps.
```

## 🏁 Implementation Steps
1. Extract every concrete requirement, promise, rule, workflow, non-goal, and quality bar into a ledger.
2. Search current implementation evidence for each ledger item across code, config, tests, docs, jobs, UI, and safe runtime state.
3. Classify each item as proved, weak, contradicted, unimplemented, not applicable, or blocked with reason.
4. Fix one confirmed high-impact mismatch at a time and add regression coverage where practical.
5. Rerun affected checks and stop when the ledger has no silent gaps.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Every product-contract requirement has an evidence-backed ledger status.
- *Detail*: The final ledger lists every requirement, evidence location, status, fixes made, regression checks, blocked items, and why any N/A or weak classification is honest.

## 💡 Why it works
A product contract is only useful if every promise can be traced to current evidence or an explicit gap; the ledger prevents selective proof.

## ⚠️ Implementation Note
* Ask before touching production, secrets, user data, destructive operations, or public claims. Do not broaden scope beyond the supplied contract.

## 🏷️ Keywords
product contract, requirements conformance, spec audit, product promises, requirement ledger

## 💬 Reviews & Feedback
- *No reviews yet.*
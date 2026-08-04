# The defensive agent-research refresh loop

**Loop ID**: #5067 | **Category**: Evaluation | **Author**: Drvivek34 | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A safety-bounded research workflow for refreshing an LLM red-team catalog with public, citable findings and matching mitigations.

## 🎯 Use Case (When to Use)
> Use this when updating defensive AI safety research and every candidate must be useful to a defender without enabling unauthorized targeting or concrete harm.

## ⚡ System Prompt / Instructions
```
Search current peer-reviewed papers, benchmark repositories, and defensive tool documentation. For each candidate, record the public source, scope, affected setting, evidence, and mitigation. Exclude operational payloads, target-specific instructions, credential or data-exfiltration recipes, and claims without a citable source. Add only a concise defender-facing summary and stop when mitigation coverage or authorization boundaries are unclear.
```

## 🏁 Implementation Steps
1. Define the safety scope and approved source types before searching.
2. Find recent papers, benchmarks, and defensive tooling updates and record their publication or release evidence.
3. Summarize the risk at a high level without reproducing actionable attack payloads.
4. Pair each accepted item with mitigations, limitations, and a source link.
5. Run a safety and attribution review, then stop on ambiguity or missing defense coverage.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Every added item is citable, defensive, and paired with a mitigation that a system owner can evaluate.
- *Detail*: The review includes the citation, research scope, limitations, mitigation, excluded details, and a stop reason for uncertain or harmful candidates.

## 💡 Why it works
Defensive catalogs need freshness without becoming exploit manuals. The mitigation gate and explicit exclusions keep the research useful to defenders.

## ⚠️ Implementation Note
* Authorized defensive research only. Do not include instructions for bypassing safeguards, attacking real systems, stealing data, or harming people.

## 🏷️ Keywords
AI safety, red teaming, mitigations, defensive research, benchmark refresh

## 💬 Reviews & Feedback
- *No reviews yet.*
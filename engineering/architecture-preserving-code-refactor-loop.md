# The architecture-preserving code refactor loop

**Loop ID**: #069 | **Category**: Engineering | **Author**: Subramanyam Badhika (@subbu6699) | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
An AI coding-agent workflow for improving a targeted code area through dependency mapping, atomic refactors, baseline tests, and downstream regression checks without changing architecture or public contracts.

## 🎯 Use Case (When to Use)
> Use this for a focused readability, typing, maintainability, or performance refactor whose intended behavior and public contracts should remain unchanged.

## ⚡ System Prompt / Instructions
```
Refactor [target] toward [measurable goal] in [repository]. If the target or goal is missing, ask and stop. Record current behavior and affected dependencies; select representative tests for boundaries and failure modes, then make one atomic change without altering public contracts unless authorized. Run the same tests, type and lint checks, and affected-consumer checks, keeping only regression-free improvements. Repeat for at most five rounds. Stop on success, blocked architecture, approval required, exhaustion, or no progress. Preserve unrelated work and finish with the diff, impact map, evidence, rejected attempts, and remaining debt.
```

## 🏁 Implementation Steps
1. Define the target, measurable goal, current behavior, public contracts, and applicable baseline checks.
2. Map internal call sites, upstream dependencies, and downstream consumers using the repository evidence available.
3. Select or add representative tests for boundaries, type constraints, and failure modes without forcing arbitrary coverage work.
4. Apply one atomic refactor and rerun the baseline, static checks, and affected-consumer checks.
5. Keep only verified improvements and repeat for no more than five rounds before entering a terminal state.

## 🛑 Stopping Condition (Verification)
**Verification Check**: The target improves without changing contracts or downstream behavior.
- *Detail*: The stated measurable goal is met, baseline behavior and public interfaces remain intact, and the relevant tests, type checks, lint checks, and affected-consumer checks pass under recorded conditions.

## 💡 Why it works
A blast-radius map prevents a locally attractive change from breaking consumers elsewhere. Atomic iterations and fixed checks make it possible to reject a failed attempt without compounding uncertainty across later changes.

## ⚠️ Implementation Note
* Do not discard unrelated work, modify public signatures or contracts without authorization, or manufacture a clean result by weakening tests or checks. An AST or generated dependency graph is optional when direct repository evidence provides a clearer impact map.

## 🏷️ Keywords
architecture-preserving refactor, blast radius analysis, atomic refactoring, regression testing, AI coding agent

## 💬 Reviews & Feedback
- *No reviews yet.*
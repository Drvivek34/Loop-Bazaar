# The 100% test coverage loop

**Loop ID**: #005 | **Category**: Engineering | **Author**: Matthew Berman | **Rating**: ⭐ 4.8/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A goal-based coding-agent workflow that identifies uncovered behavior, adds meaningful tests, and stops when the full suite passes at 100% coverage.

## 🎯 Use Case (When to Use)
> Use this when 100% coverage is an explicit project requirement and the repository has a trustworthy coverage command, clear exclusions, and a test suite that can be run repeatedly.

## ⚡ System Prompt / Instructions
```
Add tests until we have 100% test coverage.
```

## 🏁 Implementation Steps
1. Run the complete test suite with coverage and save the baseline report.
2. Prioritize uncovered branches and behavior by risk instead of file order.
3. Add tests that assert meaningful outcomes, failure paths, and boundary conditions.
4. Repeat until the full suite passes and the configured coverage report reaches 100%.

## 🛑 Stopping Condition (Verification)
**Verification Check**: The full test suite passes at 100% coverage.
- *Detail*: Use the project's coverage report as the source of truth.

## 💡 Why it works
A concrete coverage target gives the agent a measurable stopping condition and makes skipped code visible. Risk-first ordering keeps the work focused on behavior that matters.

## ⚠️ Implementation Note
* Coverage measures which code ran, not whether the assertions are good. Review test quality, avoid tests that only execute lines, and keep justified generated-code or platform exclusions explicit.

## 🏷️ Keywords
AI coding agent, 100 percent test coverage, test coverage workflow, automated testing, coding agent prompt

## 💬 Reviews & Feedback
- **@dennis_r** (★★★★★ 5/5): *Highly recommended workflow, saves considerable manual sweep time.* (2026-06-19)
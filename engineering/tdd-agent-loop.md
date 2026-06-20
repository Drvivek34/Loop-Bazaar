# The test-first agent loop

**Loop ID**: #5057 | **Category**: Engineering | **Author**: Anthropic | **Rating**: ⭐ 4.7/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
Ask the agent to write tests first, commit them, then implement until the tests pass.

## 🎯 Use Case (When to Use)
> When behavior is specifiable as tests before implementation.

## ⚡ System Prompt / Instructions
```
Write tests for the desired behavior and commit them. Then implement code until all tests pass, without weakening the tests.
```

## 🏁 Implementation Steps
1. Write failing tests for the target behavior
2. Commit the tests
3. Implement until tests pass
4. Refactor with tests green

## 🛑 Stopping Condition (Verification)
**Verification Check**: Green suite
- *Detail*: All new tests pass without being weakened.

## 💡 Why it works
Tests as a fixed target keep the agent honest and prevent over-fitting to itself.

## ⚠️ Implementation Note
* Curated real-world loop with original source attribution.

## 🏷️ Keywords
tdd, tests, red green refactor

## 💬 Reviews & Feedback
- *No reviews yet.*
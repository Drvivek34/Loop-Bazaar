# Show HN: Loop-Bazaar – 5,050 Curated AI Agent Loops & Verification Checkpoints

Hello HN,

We're launching **Loop-Bazaar**, an open-source catalog containing 5,050 repeatable AI agent workflows, design patterns, and system prompts, categorized and ranked by developer ratings.

Repository: https://github.com/Drvivek34/Loop-Bazaar

## 🔴 The Problem: Runaway Tokens and Loop Drift
When building agentic applications (using frameworks like LangGraph, AutoGen, CrewAI, or running tools like Claude Code), developers face two major issues:
1. **Loop Drift**: Without a clear stopping condition, agents tend to hallucinate or drift off-topic, executing redundant tools.
2. **Indefinite Execution**: Runaway loops consume expensive API tokens without reaching a concrete terminal state.

## 🟢 The Solution: Structured Agent Loops
A **Loop** is a repeatable workflow in which an AI agent acts on a goal, verifies the result, and loops back *only* if the stopping criteria is not met.

In **Loop-Bazaar**, every workflow contains:
- **Use Case**: Clear instructions on *when* to execute the loop.
- **System Prompt**: High-fidelity instructions for the agent.
- **Checklist Steps**: Sequential steps the agent executes (Thought-Action-Observation cycle).
- **Verification (Stopping Condition)**: A strict, testable condition indicating when the agent MUST stop (e.g., "The target page load time is under 50ms under warm-up benchmarks", or "Unit test coverage reaches 100%").
- **Why it works**: The underlying design rationale.

## 📂 Reusable Across 5 Domains
The catalog is organized into folder-wise category indices:
- `/engineering`: Code generation, refactoring, and documentation sweeps.
- `/evaluation`: Hallucination checks, prompt tuning, and regression benchmarks.
- `/operations`: DB migrations, backup verification, and security group scans.
- `/content`: SEO audits, content localization, and newsletter generation.
- `/design`: Contrast compliance check-passes, reflows, and SVG optimizations.

## 🤖 6:00 AM Autonomous Maintainer Task
We also implemented an autonomous scheduled worker script `update_library.py` (which runs at 6:00 AM daily via cron):
- **Autonomous PR Merges**: It checks out open PRs, runs a unit test suite to check schema integrity, and merges them automatically if tests pass.
- **Autonomous Issue Triage**: It downloads feedback and loop submission issues, parses the ratings and loop details, appends them to the database, re-compiles the markdown files, and closes the issues.
- **General Auto-Fixing**: For general bug reports, if a `GEMINI_API_KEY` is present, it uses LLM to analyze files, generate code fixes, verify them, commit, and push.

We'd love to hear your feedback on the prompts, design patterns, or structured verification stopping conditions. We welcome any loop contributions!

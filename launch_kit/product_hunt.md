# Product Hunt Launch Details: Loop-Bazaar

Use this copy to list Loop-Bazaar on Product Hunt.

---

## Listing Metadata

* **Product Name**: Loop-Bazaar
* **Tagline**: 5,050 Curated AI Agent Loops and Verification Checkpoints
* **Description**: An open-source, folder-wise directory of repeatable AI agent workflows, prompts, and stopping conditions designed to save API costs and eliminate runaway execution.
* **Topics**: Developer Tools, Open Source, Artificial Intelligence, GitHub, Prompts
* **Primary Visual**: Use `assets/banner.jpg` as the main thumbnail.

---

## Maker's Comment

Hi Product Hunt!

We're super excited to introduce **Loop-Bazaar**!

When building applications with LLM agents (Aider, Claude Code, LangGraph, etc.), it's extremely easy to waste hundreds of dollars in API tokens when agents get caught in infinite cycles. They keep calling the same tool or refining output without knowing if it's correct.

**Loop-Bazaar** is a directory containing 5,050 repeatable loops categorized across Engineering, Evaluation, Operations, Design, and Content.

Every single loop has:
- A targeted prompt/instruction set.
- Detailed checkpoint steps.
- A testable **Stopping Condition (Verification)** to terminate the agent loop safely.

The repository is built entirely on markdown files inside category folders, meaning you can easily import, copy, or parse these loops into your pipelines.

We also have a daily 6 AM scheduled task that automatically triages pull requests, runs unit tests, and merges community submissions submitted via simple GitHub issues.

Check it out, tell us what agent patterns you use, and please drop a star!

GitHub Repo: https://github.com/Drvivek34/Loop-Bazaar

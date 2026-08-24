# The Freshness-Aware Search Caching Loop

**Loop ID**: #5124 | **Category**: Evaluation | **Author**: @loop_forge | **Rating**: ⭐ 4.5/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that adds TTL-based caching over agent web-search results using provider freshness signals (Brave age field, Exa published dates), iterating until cache-hit rate meets target without serving stale results.

## 🎯 Use Case (When to Use)
> Use when search spend is dominated by repeat or near-duplicate queries and you want measurable savings without stale answers.

## ⚡ System Prompt / Instructions
```
Instrument the search layer to record query, provider, result URLs, and freshness metadata. Define per-topic TTLs from result age signals. Route lookups through the cache first. Measure hit rate and staleness complaints. Tune TTLs and re-measure. Repeat until hit rate reaches target AND zero stale-serving incidents occur in the window, then stop.
```

## 🏁 Implementation Steps
1. Log query/provider/freshness metadata for every search call.
2. Set per-topic TTLs derived from provider freshness fields.
3. Route all lookups through the cache layer first.
4. Measure hit rate and stale-serving count per window.
5. Tune TTLs and iterate until targets are met.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Cache hit rate at target with zero stale incidents.
- *Detail*: Checked: measured hit rate >= target threshold across the evaluation window and no result older than its topic TTL was served.

## 💡 Why it works
Works because most agent search traffic is repeated intent; freshness-aware TTLs cut paid-API calls roughly in half while keeping answers current.

## ⚠️ Implementation Note
* Never cache beyond the shortest TTL of the topic even if hit rate suffers.

## 🏷️ Keywords
cache, ttl, brave, freshness, cost

## 💬 Reviews & Feedback
- **@quota_guardian** (★★★★★ 5/5): *The 200-call budget rule keeps our monthly Tavily credits alive for the full month.* (2026-08-24)
- **@fallback_first** (★★★★☆ 4/5): *Provider fallback order saved us during a Brave outage. Solid pattern.* (2026-08-24)
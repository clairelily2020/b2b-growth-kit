---
name: market-signal-brief
description: Turn sourced market, buyer or competitor observations into a testable B2B marketing experiment brief with hypothesis, smallest useful test, primary metric, measurement window and stop rule. Use when a trend, news item, competitor move, customer comment or data anomaly suggests an opportunity and you need to decide whether and how to test it.
---

# Market signal brief

Converts "we noticed something" into a small, falsifiable experiment, or into a documented decision not to act.

## When to use

- A funding round, regulation, event, product launch or search trend touches your ICP.
- Several customers mention the same thing.
- A metric moves without explanation and you want a test, not a debate.
- Not for routine competitor monitoring; use [competitive-intel](../competitive-intel/SKILL.md) to collect, then this skill to decide.

## Inputs

- Profile: `icp`, `positioning`, `offer`, `channels.active`, `measurement`.
- The observations, each with source and date. Recent related evidence if available.

## Process

1. **Record what was actually observed.** Source, date, and the observation in one sentence. Deduplicate repeated coverage of the same event; ten articles about one announcement are one signal.
2. **Grade the evidence.** Direct customer evidence (calls, tickets, deals) outranks public data, which outranks commentary and vendor marketing. Keep supporting and contradicting evidence in separate lists.
3. **Explain why it matters to this ICP** in two or three sentences. If you cannot, stop and say so.
4. **Write one hypothesis**: "If we [action] for [segment], then [metric] will [change] within [window], because [mechanism]."
5. **Design the smallest useful test.** Cheapest channel that reaches the segment, a fixed budget or effort cap, one primary metric, a guardrail metric, a measurement window, and a stop rule decided before launch.
6. **List assumptions and unknowns.** An unknown blocks only the conclusions that depend on it; deliver the rest.
7. **Recommend**: run the test, watch and re-check on a date, or drop it with the reason.

## Output

```markdown
## Signal
| Observation | Source | Date | Evidence grade |
## Why it matters to our ICP
## Hypothesis
## Test design
Owner role / channel / audience / budget or effort cap / primary metric / guardrail metric / measurement window / stop rule
## Supporting evidence / contradicting evidence
## Assumptions and unknowns
## Recommendation and next action
```

The harness can validate this brief deterministically: `python3 -m b2b_harness signal` in the repo's `harness/` folder.

## Gates

- Engagement and event interest are not demand; see [evidence-and-claims](../b2b-growth-kit/policies/evidence-and-claims.md).
- A written experiment is not a launched experiment. Spend, outreach or publishing follow [approval-gates](../b2b-growth-kit/policies/approval-gates.md).
- No test without a stop rule and a measurement window.

## References

- After the window closes: [performance-diagnosis](../performance-diagnosis/SKILL.md)

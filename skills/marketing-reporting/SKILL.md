---
name: marketing-reporting
description: Produce weekly, monthly or campaign B2B marketing reports with explicit period, timezone, currency, definitions and data freshness, distinct funnel stages, matched comparison windows, unknowns labelled as unknown, attribution-gated CAC and ROAS, and decisions with owners. Use for marketing reports, weekly or monthly performance updates, channel performance summaries, board or leadership marketing updates, or campaign results.
---

# Marketing reporting

A report exists to support a decision. It states what changed, what is known, what is not proven, and what happens next, with numbers anyone can recompute.

## When to use

- Weekly or monthly marketing updates.
- A campaign or experiment result.
- Leadership or board summaries of marketing performance.
- If the underlying data is a mess, run [marketing-data-ops](../marketing-data-ops/SKILL.md) first.

## Inputs

- Profile: `measurement` (timezone, currency, conversion events), `channels.active`.
- Data per channel: ads, organic search, social, outbound, web and product analytics, CRM pipeline. Partial data is fine; a report on the channels you have beats no report.
- The previous report, for comparison and continuity.

## Process

1. **Fix the frame:** period (start and end), timezone, currency, metric definitions, data pull time per source, and whether the period is complete.
2. **Keep stages distinct:** clicks, visits, leads, signups, activation, qualified leads, opportunities, customers, revenue. Never add across stages.
3. **Compare like with like:** matching window lengths and definitions; mark instrumentation changes and partial periods.
4. **Gate CAC and ROAS** on verified attribution (shared definitions in the metrics policy). Label paid-media CAC separately from blended CAC; ROAS is not profit.
5. **Write the headline:** what changed and the most likely reason, in plain sentences, as many as needed and no more. Mark unknown causes as unknown; correlation is not cause.
6. **Modules:** acquisition, activation, pipeline, channel notes, experiments (with their status: running, inside measurement window, concluded), risks and blockers, next actions with owner roles.
7. **One page for weekly, short for monthly.** Detail goes in an appendix table.

## Output

```markdown
# Marketing report: {period} ({timezone}, {currency}; data pulled {dates}; period complete? yes/no)
## Headline
## Acquisition
| Channel | This period | Previous period | Change | Source | Notes |
## Activation
## Pipeline (by stage, not summed)
## Experiments (status and result so far)
## Risks and blockers
## Next actions (action, owner role, due)
## Unknowns and how we will close them
```

## Gates

- Every number has a source and pull time; missing is "unknown", not zero ([metrics-definitions](../b2b-growth-kit/policies/metrics-definitions.md)).
- No causal claims without a test; facts, inferences and recommendations are labelled ([evidence-and-claims](../b2b-growth-kit/policies/evidence-and-claims.md)).
- Reports do not change ads, contact anyone or schedule recurring jobs without approval ([approval-gates](../b2b-growth-kit/policies/approval-gates.md)).

## References

- When a number is off: [performance-diagnosis](../performance-diagnosis/SKILL.md)
- The harness recomputes ad metrics and enforces the attribution gate: `python3 -m b2b_harness ads` in the repo's `harness/` folder.

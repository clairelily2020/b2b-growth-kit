---
name: performance-diagnosis
description: Diagnose why a B2B marketing asset or channel underperformed - get actual, expected and baseline numbers, map the funnel, find the step with the largest gap, check tracking first, form three to five falsifiable hypotheses and order tests by effort and learning value. Use when a campaign, post, email, landing page, ad or launch did worse than expected, when a metric dropped, or when asked why something is not working.
---

# Performance diagnosis

Diagnose before fixing. Most "the campaign failed" conversations jump to solutions for the wrong step of the funnel, or for a tracking problem that only looks like a performance problem.

## When to use

- A result came in below expectations.
- A metric dropped and nobody knows why.
- After an experiment's measurement window closes, to explain the result.

## Inputs

- Three numbers: the actual result, the expected result, and a baseline (a similar past effort, or a cited benchmark). If there are no numbers, the closest observable signals.
- Funnel data for the asset; profile `measurement` for definitions.

## Process

1. **Get the numbers first:** actual, expected, baseline. An expectation with no basis is noted as such.
2. **Map the funnel that fits the asset:**
   ```text
   Post: impressions -> profile visits -> link clicks -> signups -> activation
   Landing page: visits -> CTA clicks -> form starts -> submissions -> qualified leads
   Email: delivered -> replied -> positive replies -> meetings
   Ads: impressions -> clicks -> landing engagement -> conversions -> qualified
   Launch: visits -> signups -> activation -> retained users
   ```
3. **Find the step with the largest gap against the baseline.** That is where to look; everything downstream of it is affected by it.
4. **Check tracking before strategy.** If a step reads zero or changed suddenly, verify the tag, the event and the conversion action first. Missing tracking is finding number one.
5. **Is it variance?** Small samples swing. With low volume, say the result is inconclusive rather than failed.
6. **Write three to five hypotheses**, no more. Each: what might be true, what you would observe if it were, what would disprove it, how to check, effort and impact.
7. **Order tests** by low effort and high learning value. Recommend one next action.

## Output

```markdown
## Investigation: {asset}
Symptom: actual {X}, expected {Y}, baseline {Z}
| Step | Actual | Baseline | Gap | Suspicion |
Most suspicious step and why
Tracking check result
Hypotheses (H1-H5): prediction / how to check / effort / impact
Test order
Next action
```

## Gates

- No fixes before the likely failure point is identified; no list of twenty causes.
- Definitions and "unknown is not zero" follow [metrics-definitions](../b2b-growth-kit/policies/metrics-definitions.md); hypotheses are labelled as inferences ([evidence-and-claims](../b2b-growth-kit/policies/evidence-and-claims.md)).
- Changes to live campaigns proposed here follow [approval-gates](../b2b-growth-kit/policies/approval-gates.md).

## References

- Channel specifics: [google-ads](../google-ads/SKILL.md) · Data plumbing: [marketing-data-ops](../marketing-data-ops/SKILL.md)

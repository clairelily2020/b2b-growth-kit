---
name: growth-plan
description: Build and run a B2B marketing plan for a small team - stage-appropriate 90-day plan in two-week cycles, a goal tree from business outcome to channel and owner, budget allocation across proven and test channels, weekly milestones with escalation rules, and retros that compare commitments with results and set the next three commitments. Use for marketing plans, OKRs, quarterly or 90-day planning, budget allocation, weekly priorities, retrospectives, or "what should we focus on".
---

# Growth plan

Small teams fail by spreading thin. This skill picks the few things that move the business at its current stage, gives each an owner and a measure, and checks every two weeks whether to continue, change or stop.

## When to use

- Quarterly or 90-day planning; setting goals or OKRs.
- Deciding how to split budget and time across channels.
- Weekly prioritization when there is more to do than people.
- Retros after a cycle, campaign or month.

## Inputs

- Profile: `company.stage`, `company.team_size`, `icp`, `offer`, `channels.active`, `measurement`.
- The business target (revenue, customers, pipeline) and the time frame; budget and people available.
- Current performance by channel and the last retro, if any.

## Process

1. **Diagnose the stage** and its main question: is there a real buying job (validation), can we win first customers, which path repeats, do customers stay, is scaling worth it. Do not plan scale work at the validation stage.
2. **Build the goal tree:** business outcome, then the funnel stage that limits it, then two or three channel bets, each with an owner role, a leading metric and a lagging metric. Include the conversion assumptions and label them as assumptions.
3. **Allocate budget and time:** most to the channel with the most evidence, a fixed slice to one or two tests with stop rules, and nothing to channels that cannot be staffed. If a plan needs more people than exist, cut it.
4. **Plan in two-week cycles** across 90 days. A typical early-stage sequence: who needs us and when; will they try and buy (offer and sample); where first value stalls; which path repeats (one complete channel experiment); credible proof (permitted cases); is more investment worth it. Skip what is already proven.
5. **Weekly rhythm:** one customer conversation, one delivery check, one data check, one decision. Escalate a goal that stays below about 70% of its milestone for two consecutive weeks: change the approach, the target or the owner.
6. **Retro** at the end of each cycle: commitments against actual results, metrics against baseline, two or three lessons each tied to evidence, the next three commitments with a metric and a date, and open questions. Separate missed commitments from wrong strategy.

## Output

```markdown
## Stage and main question
## Goal tree (outcome -> constraint -> bets -> owner, leading and lagging metric)
## Budget and time allocation (proven / test / not now), with stop rules
## 90-day plan (two-week rows: question, deliverable, decision at the end)
## This week's priorities (max 5)
## Retro (when closing a cycle): commitments vs actual / metrics / lessons / next 3 commitments / open questions
```

## Gates

- Targets and assumptions use [metrics-definitions](../b2b-growth-kit/policies/metrics-definitions.md); unproven conclusions stay labelled as hypotheses.
- Budget commitments and new spend follow [approval-gates](../b2b-growth-kit/policies/approval-gates.md).
- Every bet has an owner who exists and a stop rule.

## References

- Ideas into briefs: [campaign-brief](../campaign-brief/SKILL.md) · Status and blockers: [ops-brief](../ops-brief/SKILL.md)

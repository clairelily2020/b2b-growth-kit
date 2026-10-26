---
name: campaign-brief
description: Turn a vague marketing idea into a testable campaign brief by asking six questions one at a time - who and what problem, what failure looks like, why it beats the current workaround, the one KPI, funnel stage, and the fastest learning window - then define the smallest useful version and main risk. Use when someone has an idea for a campaign, content series, experiment or launch and it is not yet clear, or asks for a campaign brief.
---

# Campaign brief

Most weak campaigns were unclear before they started. This skill does not cheer an idea on; it finds its shape, its audience, its single measure of success and the smallest version worth running.

## When to use

- "We should do a webinar / a report / a LinkedIn series / an event."
- Before asking anyone to write copy or spend money on a new idea.
- When a team argues about a campaign and nobody can say what success is.

## Inputs

- Profile: `icp`, `positioning`, `offer`, `channels.active`, `measurement`.
- The idea in whatever form it exists.

## Process

Ask one question at a time. After each answer, reflect it in one sentence, then ask the next. Do not move to execution until all six are answered.

1. **Who is this for, and what specific problem does it solve?** Reject "everyone" or "B2B teams"; push for a role, a situation and a pain.
2. **What would failure look like?** A concrete number or observable outcome.
3. **Why is this better than doing nothing or the current workaround?** Name the behaviour change the idea depends on.
4. **If this launched tomorrow, what is the one KPI?** Only one. Several means the idea is still muddy.
5. **Where does it sit in the funnel?** Awareness, consideration, conversion, activation, retention or referral.
6. **How fast can we learn whether it works?** The smallest window that still gives a useful signal.

Then cut scope to the smallest useful version and name the main way it could fail. If the user already answered some questions in their message, do not ask them again.

## Output

```markdown
## Brief: {name}
Audience: role + situation
Problem: specific pain
Idea: one sentence
Why now: what might change behaviour
KPI: one measurable signal, with the baseline if known
Funnel stage:
Test window:
Smallest useful version: what to ship first
Main risk: most likely failure mode
Next step: who does what by when
```

## Gates

- No audience, no brief. An unmeasurable KPI gets asked again. A test longer than the team's patience gets a smaller version.
- The KPI uses definitions from [metrics-definitions](../b2b-growth-kit/policies/metrics-definitions.md).
- A brief is a plan; spend and publishing follow [approval-gates](../b2b-growth-kit/policies/approval-gates.md).

## References

- Next: variants with [ad-creative](../ad-creative/SKILL.md), review with [campaign-review](../campaign-review/SKILL.md)

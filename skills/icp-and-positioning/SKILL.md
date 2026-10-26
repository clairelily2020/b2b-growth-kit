---
name: icp-and-positioning
description: Define or sharpen a B2B ideal customer profile, buying roles, positioning statement and messaging angles from evidence (interviews, deals, lost deals, usage). Use when starting go-to-market, when copy feels generic, when win rates differ by segment, or when asked for ICP, persona, positioning, value proposition, one-liner, tagline or messaging house.
---

# ICP and positioning

Turns what you know about buyers into a profile and a message that a stranger can judge in five seconds: what this is, whether it is for them, and what happens next.

## When to use

- Before the first campaign, landing page or outbound sequence.
- When conversion differs a lot between segments and nobody knows why.
- When copy "could apply to any B2B SaaS".
- Not for picking which offer to sell first; use [offer-design](../offer-design/SKILL.md).

## Inputs

- Profile: `company`, `icp`, `positioning`, `competitors`, `voice`.
- Evidence, as much as exists: customer and lost-deal interviews, won and lost deal notes, product usage by segment, support tickets, search queries, sales call notes.
- If evidence is thin, say so in the output. A positioning built on 3 interviews is a hypothesis, labelled as such.

## Process

1. **Start from the buying job, not the persona.** For each segment, write the job the buyer is trying to get done, the moment it becomes urgent (trigger), and what they do today instead. "Do nothing", spreadsheets, an intern and an agency are all real alternatives.
2. **Separate the buying roles.** User, champion, economic buyer, security or procurement. One person can hold several. Record what each needs to believe and what material convinces them.
3. **Score segments on evidence, not enthusiasm.** Pain intensity, ability to pay, reachability through your active channels, and proof you already have. Pick one primary segment and at most two secondary ones.
4. **Write the internal positioning card:**
   `We help [segment] at [trigger moment] get [job] done. Compared with [current alternative], we offer [differentiator], proven by [proof point].`
   Every differentiator must point to a `positioning.proof_points` entry or be marked "needs evidence".
5. **Derive the public one-liner.** Use one of: `{category} for {audience} who need {job}`, `Turn {input} into {output}`, or `{known alternative} for {sharper audience}`. Avoid category-free phrases such as "AI-powered platform" or "all-in-one".
6. **Build the messaging house.** One umbrella claim, three supporting pillars, each with proof and an objection it answers. Then 4-6 angles, one per asset type, so each ad or post carries a single idea.
7. **Run the tests below** and rewrite until they pass.

## Output

```markdown
## ICP
| Segment | Buying job | Trigger | Current alternative | Fit evidence | Priority |
## Buying roles
| Role | Needs to believe | Material that convinces them |
## Exclusions (who not to target and why)
## Positioning card (internal)
## One-liner options (3) with the recommended one
## Messaging house
Umbrella claim / Pillar -> proof -> objection answered
## Angles (one idea each, with best channel)
## Evidence gaps and how to close them
```

Offer to write the accepted ICP and positioning back into the profile fields `icp` and `positioning`.

## Gates

- First-screen test: a stranger knows what it is, whether it is for them, the outcome, and the next step. Fail any one and rewrite.
- Logo test: if a competitor's logo could replace yours and the copy still works, it is not positioning.
- No claim without proof; banned claims and evidence rules follow [evidence-and-claims](../b2b-growth-kit/policies/evidence-and-claims.md).
- Do not infer budget from job title alone; mark it as a question to ask.

## References

- Interview script and synthesis: [voice-of-customer](../voice-of-customer/SKILL.md)
- Competitor alternatives: [competitive-intel](../competitive-intel/SKILL.md)

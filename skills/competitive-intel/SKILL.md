---
name: competitive-intel
description: Monitor competitors and alternatives, record dated and sourced facts (pricing, positioning, features, ads, hiring, content), judge the impact on your positioning, and produce battlecards or a response brief. Use for a competitor scan, pricing change, new competitor launch, win/loss against a named rival, comparison page research, or sales battlecards.
---

# Competitive intelligence

Keeps a dated fact registry about each competitor and turns changes into decisions. The registry is the asset; one-off opinions are not.

## When to use

- Routine scan (weekly is enough for most early teams; daily only during a launch or price war).
- A competitor changed pricing, homepage message, packaging or launched something.
- Sales lost deals to a named rival, or needs a battlecard.
- Research for a comparison page or comparison ad.

## Inputs

- Profile: `competitors` (names, positioning, our angle, `mention_policy`), `positioning`, `offer`.
- The previous registry and snapshots, if any, so you can diff instead of re-describing.
- Optional tooling: any browser automation or page-diff tool. Manual browsing works too.

## Process

1. **Define the watch list per competitor:** pricing page, homepage hero, product or changelog page, review sites, company social page, job postings, ads appearing on your brand and category terms, newsletter or blog.
2. **Collect facts, not impressions.** Each fact is an evidence record: what was observed, URL, date observed, screenshot or archived copy if possible, and an expiry (pricing: 30 days; positioning: 90 days).
3. **Diff against the last snapshot.** Report only what changed. "No change observed" is a valid result; write it instead of speculating.
4. **Classify each change:** price or packaging, message or category frame, new capability, new channel or audience, hiring signal, partnership. Hiring and ads are signals of intent, not proof of results.
5. **Judge impact on your position** using the profile's `our_angle`: does it collide with your message, undercut your entry offer, or open a gap? State confidence and what would change your mind.
6. **Recommend a proportionate response.** Most changes need no response. Options: adjust a message, update a comparison page, brief sales, watch for 30 days, or escalate a pricing decision.
7. **Battlecard (when asked):** when they win, when we win, landmines to set, objections and honest answers, proof we can show. Never claim a competitor weakness you cannot cite.

## Output

```markdown
## Scan summary (date, competitors covered, sources unreachable)
| Competitor | Change | Category | Source (URL, observed date) | Impact on us | Confidence |
## Recommended responses (owner role, by when, or "no action")
## Registry updates (new or expired facts)
## Battlecard (optional)
When they win / when we win / objections and answers / proof we can show / do not say
```

## Gates

- Every fact has a URL and an observed date. No source, no fact. Rules in [evidence-and-claims](../b2b-growth-kit/policies/evidence-and-claims.md).
- Public mentions of competitors follow `competitors.mention_policy`; comparison copy uses only cited, current facts.
- Do not sign up with fake identities, scrape behind logins, or contact a competitor's customers under a pretext.
- Price or message changes in your own assets are proposals; publishing follows [approval-gates](../b2b-growth-kit/policies/approval-gates.md).

## References

- Turning a change into a test: [market-signal-brief](../market-signal-brief/SKILL.md)
- Comparison pages for AI search: [answer-engine-content](../answer-engine-content/SKILL.md)

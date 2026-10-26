# Fact-check gates

Run all seven before any content is called ready. Quote the draft's claim and the matching source for each item you check.

## Gate 1: our claims trace to the profile

Every claim about the company (features, pricing, speed, team, customer counts) matches `positioning.proof_points`, `offer` or a reviewed evidence record. If the draft and the source disagree, fix the draft. Never edit the source to match the draft.

Hunt for: any money figure, any speed or runtime figure, any team or founder claim, "we have X customers", "our users report".

## Gate 2: competitor claims trace to a dated public source

Each competitor statement has the competitor's own page (or a reputable third party) as source, with an observed date. Re-verify anything older than 90 days. Watch for the classic errors: saying a competitor "doesn't have" a capability, quoting unverified prices, overstating their weaknesses.

## Gate 3: every number has a source

Percentages, counts, durations and amounts come from a cited study (linked), an evidence record, or the company's own measured data. Otherwise delete the number and rewrite. "Studies show", "most teams" and "on average" without a citation are not acceptable.

## Gate 4: no fabricated customer proof

Zero invented customer names, quotes, logos or results. A customer claim needs an evidence record with written consent. Without proof, use other framing: a worked example with clearly fictional data, a method explanation, or a placeholder such as `[CUSTOMER QUOTE NEEDED]`.

## Gate 5: question-first structure

- Opens with a direct answer to one target question.
- The structure matches what the reader needs (and what research shows winning), not a fixed template.
- Structured data (for example FAQPage or Article schema) matches the visible content.

## Gate 6: style

- No empty superlatives (revolutionary, cutting-edge, industry-leading, best-in-class) and nothing from `voice.avoid` or `claims.banned`.
- Plain, active sentences; no emoji in body copy.
- Headings describe content; no headings that exist only to stuff keywords.

## Gate 7: link hygiene

- Internal links resolve; external links are HTTPS and load.
- CTA links and UTMs follow `offer.cta_url` and `offer.utm`.
- No links to private documents, staging hosts or test parameters.

## Severity

| Severity | Definition | Action |
|---|---|---|
| Critical | Wrong claim about us or a competitor | Block. Fix the draft. |
| High | Unsourced number, missing citation, credibility-damaging style issue | Block. Fix the draft. |
| Medium | Structural issue that hurts usefulness but not accuracy | Fix before publishing. |
| Low | Polish | Fix if time allows. |

Any critical or high finding blocks publication, deadline or not.

## Disputes

The author cites a source; the reviewer checks it. A solid source becomes an evidence record and the claim stays. A weak source means the claim is removed. "We think it's true" is not enough.

## Report

```markdown
# Fact-check: {title}
Date / checked by (role) / target question
| Gate | Pass or fail | Notes |
Issues by severity
Verdict: ready for publishing approval, or blocked
```

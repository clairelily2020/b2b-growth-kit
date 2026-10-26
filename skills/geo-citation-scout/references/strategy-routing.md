# Strategy routing

Each judgment maps to one concrete action. Never stop at "create more content".

## Routing table

| Judgment | Action |
|---|---|
| Strong source, held by a competitor or review site | Do not attack now. Add to a "held positions" list and re-check in 4-8 weeks. |
| Strong source, held by your own page | Find why it wins (structure, subtopics) and copy that pattern to similar questions. |
| Weak source (generic, stale, off-intent) | High priority. Create or rewrite a page using the brief skeleton below, aimed at what the current answer misses. |
| No citation | Highest priority. Same as above, flagged separately in the report; easiest position to take. |
| Community-led (forums, Reddit) | Not a landing-page signal. Route to community work, naming the community and the question type. |
| One structure keeps winning across questions | Record a structure pattern and adopt it across your content, not just for one question. |
| Several of your wins depend on one page | Flag concentration risk. If that page goes stale, you lose several positions at once; maintain it first. |
| Most wins come from your own content | Warn that self-published content carries less trust for neutral questions (for example build versus buy). Add third-party signals: reviews, community answers, earned links. |

## Content brief skeleton

```
H1: the buyer's question in their words (not a brand headline)
Short answer: 2-3 sentences with the conclusion
Why this happens: cause and context
Step by step: how to do it
Comparison table: when options are being compared
Where the product fits: restrained, one section
FAQ: 2-4 related follow-ups
```

If the analysis shows comparison tables winning for a question type, move the table higher. Follow the evidence, not this default order.

## Report template

```markdown
# GEO citation report: {product}

## Summary
- Questions analyzed: X
- No or weak citation (high priority): X
- Community-led (community route): X
- Held by competitors or by us (not a priority now): X
- Not retrieved (engine access): X

## Per question
### "{question}"
- Type: how-to / comparison / alternative / evaluation / problem statement
- Perplexity: URL / domain / type / structure / freshness, or "not retrieved"
- ChatGPT: same, or "not retrieved"
- Google AI Overviews: same, or "not retrieved / not triggered"
- Judgment: strong / weak / none / community-led
- Action: from the routing table

## Priority list (by judgment, not by order asked)
## Structure patterns
```

On a re-run, compare with the last report: which questions moved from no citation to cited, and which winners changed.
